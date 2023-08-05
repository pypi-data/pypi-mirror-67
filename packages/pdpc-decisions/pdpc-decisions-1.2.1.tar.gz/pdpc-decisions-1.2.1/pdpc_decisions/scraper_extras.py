#  MIT License Copyright (c) 2020. Houfu Ang
import logging

from pdpc_decisions.download_file import check_pdf


def get_enforcement(items):
    import spacy
    from spacy.matcher import Matcher
    nlp = spacy.load('en_core_web_sm')
    matcher = Matcher(nlp.vocab)
    financial_penalty_pattern = [{'LOWER': 'financial'},
                                 {'LOWER': 'penalty'},
                                 {'POS': 'ADP'},
                                 {'LOWER': '$'},
                                 {'LIKE_NUM': True}]
    financial_1_id = 'financial_1'
    matcher.add(financial_1_id, [financial_penalty_pattern])
    financial_penalty_pattern2 = [{'LOWER': 'financial'},
                                  {'LOWER': 'penalty'},
                                  {'POS': 'ADP'},
                                  {'LOWER': '$'},
                                  {'LIKE_NUM': True},
                                  {'LOWER': 'and'},
                                  {'LOWER': '$'},
                                  {'LIKE_NUM': True}]
    financial_2_id = 'financial_2'
    matcher.add(financial_2_id, [financial_penalty_pattern2])
    warning_pattern = [{'LOWER': 'warning'},
                       {'POS': 'AUX'},
                       {'LOWER': 'issued'}]
    warning_id = 'warning'
    matcher.add(warning_id, [warning_pattern])
    directions_pattern = [{'LOWER': 'directions'},
                          {'POS': 'AUX'},
                          {'LOWER': 'issued'}]
    directions_id = 'directions'
    matcher.add(directions_id, [directions_pattern])
    logging.info('Adding enforcement information to items.')
    for item in items:
        doc = nlp(item.summary)
        matches = matcher(doc)
        item.enforcement = []
        for match in matches:
            match_id, _, end = match
            if nlp.vocab.strings[financial_2_id] in match:
                span1 = doc[end - 4: end - 3]
                value = ['financial', int(span1.text.replace(',', ''))]
                if not item.enforcement.count(value):
                    item.enforcement.append(value)
                span2 = doc[end - 1:end]
                value = ['financial', int(span2.text.replace(',', ''))]
                if not item.enforcement.count(value):
                    item.enforcement.append(value)
            if nlp.vocab.strings[financial_1_id] in match:
                span = doc[end - 1:end]
                value = ['financial', int(span.text.replace(',', ''))]
                if not item.enforcement.count(value):
                    item.enforcement.append(value)
            if nlp.vocab.strings[warning_id] in match:
                item.enforcement.append(warning_id)
            if nlp.vocab.strings[directions_id] in match:
                item.enforcement.append(directions_id)


def get_decision_citation_all(items):
    logging.info('Adding citation information to items.')
    for item in items:
        get_decision_citation_one(item)


def get_decision_citation_one(item):
    from pdfminer.high_level import extract_text_to_fp
    import requests
    import io
    import re
    r = requests.get(item.download_url)
    item.citation = ''
    item.case_number = ''
    if check_pdf(item.download_url):
        with io.BytesIO(r.content) as pdf, io.StringIO() as output_string:
            extract_text_to_fp(pdf, output_string, page_numbers=[0, 1])
            contents = output_string.getvalue()
        summary_match = re.search(r'SUMMARY OF THE DECISION', contents)
        if not summary_match:
            citation_match = re.search(r'(\[\d{4}])\s+((?:\d\s+)?[A-Z|()]+)\s+\[?(\d+)\]?', contents)
            if citation_match:
                item.citation = citation_match.expand(r'\1 \2 \3')
        case_match = re.search(r'DP-\w*-\w*', contents)
        if case_match:
            item.case_number = case_match.group()


def get_case_references(items):
    logging.info('Adding case reference information to items.')
    import re
    from .download_file import get_text_from_pdf
    citation_regex = re.compile(r'(\[\d{4}])\s+((?:\d\s+)?[A-Z|()]+)\s+\[?(\d+)\]?')
    # construct referring to index
    for item in items:
        if not hasattr(item, 'citation'):
            get_decision_citation_one(item)
        item.referred_by = []
        item.referring_to = []
        if check_pdf(item.download_url):
            contents = get_text_from_pdf(item)
            citation_matches = citation_regex.finditer(contents)
            for match in citation_matches:
                result_citation = match.expand(r'\1 \2 \3')
                if (item.referring_to.count(result_citation) == 0) and (result_citation != item.citation):
                    item.referring_to.append(result_citation)
    # constructed referred by index
    for item in items:
        for reference in item.referring_to:
            result_item = next((x for x in items if x.citation == reference), None)
            if result_item:
                if result_item.referred_by.count(item.citation) == 0:
                    result_item.referred_by.append(item.citation)


def scraper_extras(items):
    logging.info('Start adding extra information to items.')
    get_decision_citation_all(items)
    get_enforcement(items)
    get_case_references(items)
    logging.info('End adding extra information to items.')
    return True

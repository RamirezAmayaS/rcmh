import re
import pickle
import pkg_resources

from pymedtermino import icd10

DATA_PATH = pkg_resources.resource_filename(__name__,'data/icd10_codes.pickle')

EXCEPTIONS = {
    'B7': 'Viral infections characterized by skin and mucous membrane lesions',
    'C8': 'Malignant neoplasms, stated or presumed to be primary, of lymphoid, haematopoietic and related tissue' ,
    'C9': 'Malignant neoplasms, stated or presumed to be primary, of lymphoid, haematopoietic and related tissue and Malignant neoplasms of independent (primary) multiple sites',
    'D1': 'Benign neoplasms',
    'D2': 'Benign neoplasms',
    'E8': 'Metabolic disorders',
    'I4': 'Other forms of heart disease',
    'M1': 'Inflammatory polyarthropathies and Arthrosis',
    'T4': 'Poisoning by drugs, medicaments and biological substances',
    'V1': 'Accidents',
    'V2': 'Accidents',
    'V3': 'Accidents',
    'V4': 'Accidents',
    'V5': 'Accidents',
    'V6': 'Accidents',
    'V7': 'Accidents',
    'V8': 'Accidents',
    'V9': 'Accidents',
    'W0': 'Accidents',
    'W1': 'Accidents',
    'W2': 'Accidents',
    'W3': 'Accidents',
    'W4': 'Accidents',
    'W5': 'Accidents',
    'W6': 'Accidents',
    'W7': 'Accidents',
    'W8': 'Accidents',
    'W9': 'Accidents',
    'X0': 'Accidents',
    'X1': 'Accidents',
    'X2': 'Accidents',
    'X3': 'Accidents',
    'X4': 'Accidents',
    'X7': 'Intentional self-harm',
    'X9': 'Assault',
    'Y2': 'Assault',
    'Y5': 'Assault',
    'Y6': 'Assault',
    'Y7': 'Assault',
}

def get_code_description(code):
    if code in EXCEPTIONS.keys():
        return EXCEPTIONS[code]
    description = ' and'
    for chapter in icd10.ICD10.first_levels():
        if code[0] == 'C':
            it = chapter.children[0].children[0].children
        else:
            it = chapter.children
        terms = [str(term) for term in it if re.search(code,str(term))]
        terms = [term[:-1].split('#')[1] for term in terms]
        if terms:
            description = description.join(terms)[1:]
            break
    return description

def get_full_code_description(code):
    if code in EXCEPTIONS.keys():
        return EXCEPTIONS[code]
    description = ''
    for chapter in icd10.ICD10.first_levels():
        if code[0] == 'C':
            it = chapter.children[0].children[0].children
        else:
            it = chapter.children
        for terminology in it:
            if re.search(code,str(terminology)):
                for desc in terminology.self_and_descendants_no_double():
                    description = description + str(desc).split('#')[1][:-1] + ' '
        if description:
            break
    return description

def validate_codes():
    with open('/Users/RamirezAmayaS/clustering/rcmh/rcmh/data/icd10_codes.pickle','rb') as f:
        codes = pickle.load(f)
        for code in codes:
            print(code,get_code_description(code))

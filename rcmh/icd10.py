import re
import pickle
import pkg_resources

from pymedtermino import icd10

DATA_PATH = pkg_resources.resource_filename(__name__,'data/icd10_codes.pickle')
EXCEPTIONS = {
    'C0': 'Malignant neoplasms of lip, oral cavity and pharynx and Malignant neoplasms of digestive organs',
    'C1': 'Malignant neoplasms of digestive organs',
    'C2': 'Malignant neoplasms of digestive organs',
    'C3': 'Malignant neoplasms of respiratory and intrathoracic organs',
    'C4': 'Malignant neoplasms of bone and articular cartilage and Melanoma and other malignant neoplasms of skin  and Malignant neoplasms of mesothelial and soft tissue',
    'C5': 'Malignant neoplasm of breast and Malignant neoplasms of female genital organs',
    'C6': 'Malignant neoplasms of male genital organs and Malignant neoplasms of urinary tract  and Malignant neoplasms of eye, brain and other parts of central nervous system',
    'C7': 'Malignant neoplasms of eye, brain and other parts of central nervous system and Malignant neoplasms of thyroid and other endocrine glands  Malignant neoplasms of ill-defined, secondary and unspecified sites',
    'C8': 'Malignant neoplasms, stated or presumed to be primary, of lymphoid, haematopoietic and related tissue',
    'C9': 'Malignant neoplasms, stated or presumed to be primary, of lymphoid, haematopoietic and related tissue and Malignant neoplasms of independent (primary) multiple sites',
    'D1': 'Benign neoplasms',
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
    'X9': 'Accidents',
}

def get_code_description(code):
    if code in EXCEPTIONS.keys():
        return EXCEPTIONS[code]
    description = ' and'
    for chapter in icd10.ICD10.first_levels():
        terms = [str(term) for term in chapter.children if re.search(code,str(term)) or (int(code[1]) > int(str(term)[9]) and int(code[1]) < int(str(term)[13]) and code[0] == str(term)[8])]
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
        for terminology in chapter.children:
            if re.search(code,str(terminology)) or (int(code[1]) > int(str(terminology)[9]) and int(code[1]) < int(str(terminology)[13]) and code[0] == str(term)[8]):
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

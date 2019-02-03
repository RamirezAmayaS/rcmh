import re
from pymedtermino import icd10

def get_code_description(code):
    description = ' and'
    for chapter in icd10.ICD10.first_levels():
        terms = [str(term) for term in chapter.children if re.search(code,str(term))]
        terms = [term[:-1].split('#')[1] for term in terms]
        if terms:
            description = description.join(terms)
            break
    return description

def get_full_code_description(code):
    description = ''
    for chapter in icd10.ICD10.first_levels():
        for terminology in chapter.children:
            if re.search(code,str(terminology)):
                for desc in terminology.self_and_descendants_no_double():
                    description = description + str(desc).split('#')[1][:-1] + ' '
        if description:
            break
    return description

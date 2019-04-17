from pymedtermino import icd10

def get_code_description(code):
    description = str(icd10.ICD10.concept(code)).split('#')[1][:-1] + ' '
    return description.lower()

def get_group_description(group):
    description = ' '
    for code in group.codes:
        description = description + get_code_description(code)
    return description

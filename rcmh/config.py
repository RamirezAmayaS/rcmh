DATA_PATH = pkg_resources.resource_filename(__name__,'data/icd10_codes.pickle')

with open('/Users/RamirezAmayaS/clustering/rcmh/rcmh/data/icd10_codes.pickle','rb') as f:
    codes = pickle.load(f)
    k = len(codes)

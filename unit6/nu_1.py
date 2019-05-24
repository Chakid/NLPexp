def gender_features(word):
    return {'last_letter': word[-1]}
gender_features('Shrek')
{'last_letter': 'k'}
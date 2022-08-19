def abbreviate(words):
    acronym = [str[0].upper() for str in words.replace('-',' ').replace('_',' ').split()]
    return ''.join(acronym)
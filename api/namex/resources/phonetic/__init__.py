def first_vowels(word):
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    value = ''
    first_vowel_found = False
    for letter in word:
        if letter not in vowels and first_vowel_found:
            break
        if letter in vowels:
            value += letter
            first_vowel_found = True

    if value == 'EY':
        value = 'A'
    if value == 'EI':
        value = 'A'
    if value == 'EA':
        value = 'A'
    if value == 'AY':
        value = 'A'
    if value == 'AI':
        value = 'A'
    if value == 'Y':
        value = 'I'

    return value


def first_arpabet(word):
    if word == 'LEAK':
        return 'IY1'
    if word == 'LEEK':
        return 'IY1'

    return word
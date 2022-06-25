from spellchecker import SpellChecker

spell = SpellChecker(language='de')

misspelled = spell.unknown(["verschen"])

for word in misspelled:
    print(spell._check_if_should_check(word))
    print(spell.correction(word))
    print(spell.candidates(word))

from spellchecker import SpellChecker

#@author: Hannah Braun
#Aktuell nicht genutzt
#Rechtschreibkontrolle

spell = SpellChecker(language='de')

misspelled = spell.unknown(["tseten"])

for word in misspelled:
    print(spell._check_if_should_check(word))
    print(spell.correction(word))
    print(spell.candidates(word))

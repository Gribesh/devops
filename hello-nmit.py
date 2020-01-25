#! /usr/bin/python3
print("Hello, Unisys")

def pig_latin(word):
    if word[0] in 'aeiou' or 'AEIOU':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + word[0] + 'ay'
    return pig_word

print(pig_latin('TAJ'))
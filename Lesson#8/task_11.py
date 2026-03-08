"""
С клавиатуры вводится текст, определить, сколько в нём гласных, а сколько согласных.

P.s. Использовать латинские буквы.

"""

text = input("Введите текст: ")

vowels = 'aeiouyAEIOUY'
vowel_count = 0
consonant_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1

print(f"Гласных: {vowel_count}, Согласных: {consonant_count}")
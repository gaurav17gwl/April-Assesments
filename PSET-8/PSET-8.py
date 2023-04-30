#Write a script that accepts the user for the input and converts all the vowels `('a','e','i','o','u')` into uppercase.


user_input=input("Enter some text: ")
vowel=user_input.replace('a','A')
vowel=vowel.replace('e', 'E')
vowel=vowel.replace('i', 'I')
vowel=vowel.replace('o', 'O')
vowel=vowel.replace('u', 'U')
print(f'Please find vowels in upper case in the entered text: {vowel}')
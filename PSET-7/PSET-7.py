'''
Write a script that asks the user for some input with the following prompt: `'Enter some text:'`.
 Then use the `.replace()` method to convert the text entered by the user into [`leetspeak`]
 '''

user_value= input("Enter some text:")
upper_input=user_value.upper()
leetspeak=upper_input.replace('A' , '4')
leetspeak=leetspeak.replace('B', 'I3')
leetspeak=leetspeak.replace('E', '3')
leetspeak=leetspeak.replace('I', '1')
leetspeak=leetspeak.replace('H', '#')
leetspeak=leetspeak.replace('M', '/\\/\\')
leetspeak=leetspeak.replace('O', '0')
leetspeak=leetspeak.replace('S', '5')
leetspeak=leetspeak.replace('T', '7')
leetspeak=leetspeak.replace('U', '(_)')
print(leetspeak)
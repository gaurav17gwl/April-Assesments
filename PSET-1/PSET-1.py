'''Consider the following words:

'spinach'
'unpinch'
'hoping'
'pink'
'ping'
'respin'
'legspin'
Write a line of code such that it returns 'pin' when each of thsese are stored in a variable. (A single line of code has to work for all.)'''


given_sting='unpinch'
length_gs=len(given_sting)
#print(length_b)
pin_postion=given_sting.find('pin')
#print(a)
final_output=given_sting[pin_postion:pin_postion+len('pin')]
print(final_output)



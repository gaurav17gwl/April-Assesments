'''
Given a string that contains the name of a person along with whitespaces.
Write a code such that it splits the first name and last name and assigns them to variables first_name 
and last_name without any whitespace. Don't use .split and .partition methods.
Steps :-
Remove the whitespaces.
Find index of first character of last name and last character of the first name.
'''
full_name="Gaurav Gupta"
whitespace=full_name.find(" ")

first_name=full_name[:whitespace]

last_name=full_name[whitespace+1:]

index_last_name=last_name.index(last_name,0)
print(index_last_name)
index_first_name=whitespace-1
#print(index_last_name)
print(index_first_name)
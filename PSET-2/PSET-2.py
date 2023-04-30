#This is a spin-off of PSET-1. As a continuation fetch two strings from user such that the second string is the substring of the first.

first_string="hareram"
sub_string="hare"
find_position=first_string.find(sub_string)
final_output=first_string[find_position:find_position+(len(sub_string))]
print(final_output)
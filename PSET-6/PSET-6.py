#Your script should replace the first occurence of 'piranha' with 'fish'.
paragraph='''Although most people consider **fish**s to be quite dangerous, they are, 
for the most part, entirely harmless. Piranhas rarely feed on large animals; they eat 
smaller fish and aquatic plants. When confronted with humans, piranhas’ first instinct 
is to flee, not attack. Their fear of humans makes sense. Far more piranhas are eaten 
by people than people are eaten by piranhas. If the fish are well-fed, they won’t bite humans.'''

count_piranha=paragraph.count("piranhas") # to findout the total count of piranhas word in the paragraph
print(count_piranha)

change_piranha=paragraph.replace("piranha","fish",1)
print(change_piranha)

count_piranha=change_piranha.count("piranhas") # to findout the total count of piranhas word in the paragraph after change 'piranha' with 'fish'.
print(count_piranha)


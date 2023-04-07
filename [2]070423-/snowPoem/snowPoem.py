import random

poem = "Words fell from the sky today I stood and watched them snowin'"
ending = "and as they settled on the ground, \nthey turned into this poem."
author = "Brian Bilston"


words = poem.split()

for i in range(len(words)):
    indent = random.randint(0,25) * " "
    print(indent + words[i])

print(ending)
print(author)
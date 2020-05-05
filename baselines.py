# generate baselines

import random

def randomize(sentence):
    tokens = sentence.split()
    while len(tokens) > 1:
        merge = random.choice(list(range(len(tokens) - 1)))
        tokens[merge] = "( " + tokens[merge] + " " + tokens[merge + 1] + " )"
        del tokens[merge + 1]
    return tokens[0]

print(randomize('a form of asbestos is used'))
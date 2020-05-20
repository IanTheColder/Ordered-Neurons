# generate baselines

import random
import math

def randomize(sentence):
    tokens = ['(<word> {})'.format(word) for word in sentence.split()]
    while len(tokens) > 1:
        merge = random.choice(list(range(len(tokens) - 1)))
        tokens[merge] = "(" + "<unk> "+tokens[merge] + " " + tokens[merge + 1] + ")"
        del tokens[merge + 1]
    return tokens[0]

def roundup2(N):
    """ Round up using factors of 2. """
    return int(2 ** math.ceil(math.log(N, 2)))

def full_transitions(N, left_full=False, right_full=False):
    """
    Recursively creates a full binary tree of with N
    leaves using shift reduce transitions.
    """

    if N == 1:
        return [0]

    if N == 2:
        return [0, 0, 1]

    assert not (left_full and right_full), "Please only choose one."

    if not left_full and not right_full:
        N = float(N)

        # Constrain to full binary trees.
        assert math.log(N, 2) % 1 == 0, \
            "Bad value. N={}".format(N)

        left_N = N / 2
        right_N = N - left_N

    if left_full:
        left_N = roundup2(N) / 2
        right_N = N - left_N

    if right_full:
        right_N = roundup2(N) / 2
        left_N = N - right_N

    return full_transitions(left_N, left_full=left_full, right_full=right_full) + \
           full_transitions(right_N, left_full=left_full, right_full=right_full) + \
           [1]

def balance(sentence):
    # Modified to provided a "half-full" binary tree without padding.
    # Difference between the other method is the right subtrees are
    # the half full ones.
    tokens = sentence.split()
    if len(tokens) > 1:
        transitions = full_transitions(len(tokens), right_full=True)
        stack = []
        for transition in transitions:
            if transition == 0:
                stack.append(tokens.pop(0))
            elif transition == 1:
                right = stack.pop()
                left = stack.pop()
                stack.append("( " + left + " " + right + " )")
        assert len(stack) == 1
    else: 
        stack = tokens
    return stack[0]

if __name__=='__main__':
    print(randomize('a form of asbestos is used for some reasons'))
    print(balance('a form of asbestos is used for some reasons'))

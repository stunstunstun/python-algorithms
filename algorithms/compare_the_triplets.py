"""
Compare the Triplets - https://github.com/stunstunstun/awesome-algorithms/issues/1
"""


def solve(a0, a1, a2, b0, b1, b2):
    alice_points = [a0, a1, a2]
    bob_points = [b0, b1, b2]
    alice_score = 0
    bob_score = 0

    for i in range(len(alice_points)):
        if alice_points[i] > bob_points[i]:
            alice_score += 1
        elif alice_points[i] == bob_points[i]:
            pass
        else:
            bob_score += 1

    return ' '.join(map(lambda x: str(x), [alice_score, bob_score]))

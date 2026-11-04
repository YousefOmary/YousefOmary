# limits_checks.py
# Checks for file 16 (Garfield and Priest 2003, first limit contradiction).
# Question: does the set of claims the authors make become contradictory only
# when two senses of "ultimate truth" are identified?
#   U1(p): p holds with a status independent of convention
#   U2(p): p is what analysis of a thing's nature finds (a truth about the ultimate)
#   C(p):  p is conventional in status
# Claims kept fixed (all from the paper, see file 16):
#   K1  every truth is conventional in status             (p.6/p.10: all truths are merely conventional)
#   K2  no truth is U1                                     (p.10, rule L)
#   K3  s = "nothing has an ultimate nature" is U2         (p.11-12)
#   K4  s is a truth
# Variable: the identification U1 == U2.
import itertools, json

def consistent(identify):
    # one proposition s; truth-values for U1(s), U2(s), C(s), T(s)
    for u1, u2, c, t in itertools.product([0, 1], repeat=4):
        if identify and u1 != u2:
            continue
        k1 = (not t) or c
        k2 = not u1
        k3 = u2
        k4 = t
        if k1 and k2 and k3 and k4:
            return True
    return False

out = {
    "two senses kept apart": consistent(identify=False),
    "senses identified (U1==U2)": consistent(identify=True),
}
print(json.dumps(out, ensure_ascii=False, indent=1))

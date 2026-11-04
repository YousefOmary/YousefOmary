# revision_model.py
# A revision-theoretic model of Madhyamaka "ultimate analysis" (file 17).
#
# U   : the conventional commitment set (everything a community accepts).
# Ref : given a commitment set X, the contents that analysis refutes USING X.
#       Ref is monotone: more commitments, more refutations (prasanga uses
#       the opponent's own commitments).
# A   : the revision operator  A(X) = U \ Ref(X)
#       "keep whatever the current commitments do not refute".
# Because Ref is monotone, A is antitone and A∘A is monotone, so the
# revision sequence from U splits into a decreasing even chain and an
# increasing odd chain. A content is
#   stably in   : in every term from some point on,
#   stably out  : in no term from some point on,
#   unstable    : alternates forever.
#
# Contents (toy, but each stands for a type that matters):
#   D_pot  "the pot depends on its parts"            (conventional, dependence fact)
#   D_E    "emptiness depends on the empty thing"    (Garfield-Priest 2003 p.6)
#   S_pot  "the pot has svabhava"                    (innate reification)
#   S_E    "emptiness has svabhava"
#   E_pot  "the pot is empty"                        (what analysis finds)
#   G      "all things are empty"                    (MMK 24.19, universal, includes G)
#   P      "the pot holds water"                     (ordinary conventional truth)
#   M      "that is a mirage"                        (conventional observation)
#   W      "there is water on the road"              (conventional falsehood)
#   Z      "nothing exists"                          (nihilism)
#   N      "there is no ultimate truth"              (the Garfield-Priest limit sentence)
#
# Refutation rules (all monotone in X):
#   S_pot refuted iff D_pot in X          (dependence refutes svabhava)
#   S_E   refuted iff D_E in X            (emptiness of emptiness)
#   W     refuted iff M in X              (conventional pramana undermines)
#   Z     refuted iff P in X              (any surviving conventional truth refutes nihilism)
#   N     refuted iff N in X              (N is itself a claim about the ultimate;
#                                           held, it falls under its own scope)
#   everything else: never refuted.
import json

U = ["D_pot", "D_E", "S_pot", "S_E", "E_pot", "G", "P", "M", "W", "Z", "N"]

def Ref(X):
    X = set(X)
    out = set()
    if "D_pot" in X: out.add("S_pot")
    if "D_E" in X:   out.add("S_E")
    if "M" in X:     out.add("W")
    if "P" in X:     out.add("Z")
    if "N" in X:     out.add("N")
    return out

def A(X):
    return set(U) - Ref(X)

def check_monotone():
    import itertools
    items = list(U)
    # sample all pairs of subsets would be 2^22; test on all subsets of a 6-element core
    core = ["D_pot", "D_E", "M", "P", "N", "S_pot"]
    for r in range(len(core) + 1):
        for X in itertools.combinations(core, r):
            for s in range(len(core) + 1):
                for Y in itertools.combinations(core, s):
                    if set(X) <= set(Y) and not Ref(X) <= Ref(Y):
                        return False
    return True

def revision_sequence(start, steps=12):
    seq = [set(start)]
    for _ in range(steps):
        seq.append(A(seq[-1]))
    return seq

def classify(seq, tail=6):
    last = seq[-tail:]
    result = {}
    for x in U:
        pattern = [x in X for X in last]
        if all(pattern):
            result[x] = "stably in"
        elif not any(pattern):
            result[x] = "stably out"
        else:
            result[x] = "unstable"
    return result

seq = revision_sequence(U)
cls = classify(seq)

# fixed points of A∘A reached from U: even and odd limits
even_limit = seq[-2] if len(seq) % 2 == 1 else seq[-1]
odd_limit = seq[-1] if len(seq) % 2 == 1 else seq[-2]
stable_core = even_limit & odd_limit

# The ordinary person's set contains innate reification. The stable core is
# a fixed point of A∘A. A itself has NO fixed point: N is in X iff N is not
# in A(X). So no membership state is left untouched by one step of analysis;
# the attitude to N (neither hold nor drop) is not a membership state but a
# stance on the whole sequence.
core = set(stable_core)
ordinary = set(U) - {"N"}
def has_fixed_point_A():
    import itertools
    for r in range(len(U) + 1):
        for X in itertools.combinations(U, r):
            if A(X) == set(X):
                return True
    return False
report = {
    "Ref monotone on sampled core": check_monotone(),
    "classification": cls,
    "stable core": sorted(stable_core),
    "stable core is a fixed point of A∘A": A(A(core)) == core,
    "A has a fixed point": has_fixed_point_A(),
    "first revision of ordinary set removes": sorted(ordinary - A(ordinary)),
    "N oscillates with period 2": [("N" in X) for X in seq[:8]],
    "G (all things are empty) is": cls["G"],
    "any content both stably in and stably out": False,
}
print(json.dumps(report, ensure_ascii=False, indent=1))

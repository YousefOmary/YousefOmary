# dung_checks.py  (file 25)
# Claim: the revision operator A(X) = U \ Ref(X) with a monotone, set-based
# refutation relation is a SETAF (set-attack argumentation framework,
# Nielsen & Parsons 2006), and A∘A is Dung's characteristic function F
# (F(X) = arguments defended by X). Hence the stable core = grounded
# extension = lfp(F), "stably out" = attacked by the grounded extension,
# and "unstable" = the UNDEC label of the grounded labelling (Caminada 2006).
# We verify (1) A∘A == F on random SETAFs, (2) the toy model of file 17
# receives exactly the grounded labelling, (3) odd/even cycle behaviour.
import itertools, random, json

def make_ref(U, attacks):
    # attacks: list of (frozenset S, x): S attacks x
    def Ref(X):
        X = frozenset(X)
        return {x for (S, x) in attacks if S <= X}
    return Ref

def A(U, Ref):
    return lambda X: set(U) - Ref(X)

def F(U, attacks, X):
    # x is defended by X iff every attacking set S of x is "attacked by X",
    # i.e. some member of S is attacked by a subset of X.
    X = frozenset(X)
    def attacked_by_X(y):
        return any(S <= X and t == y for (S, t) in attacks)
    out = set()
    for x in U:
        if all(any(attacked_by_X(y) for y in S) for (S, t) in attacks if t == x):
            out.add(x)
    return out

def lfp(f, U):
    X = set()
    while True:
        Y = f(X)
        if Y == X: return X
        X = Y

def gfp(f, U):
    X = set(U)
    while True:
        Y = f(X)
        if Y == X: return X
        X = Y

def grounded_labelling(U, attacks):
    IN, OUT = set(), set()
    changed = True
    while changed:
        changed = False
        for x in U:
            if x in IN or x in OUT: continue
            atks = [S for (S, t) in attacks if t == x]
            if all(any(y in OUT for y in S) for S in atks):
                IN.add(x); changed = True
            elif any(S <= IN for S in atks):
                OUT.add(x); changed = True
    UNDEC = set(U) - IN - OUT
    return IN, OUT, UNDEC

# (1) A∘A == F on random SETAFs
random.seed(7)
mismatch = 0
for trial in range(2000):
    n = random.randint(2, 6)
    U = [f"a{i}" for i in range(n)]
    attacks = []
    for _ in range(random.randint(0, 2 * n)):
        k = random.randint(1, 2)
        S = frozenset(random.sample(U, k))
        attacks.append((S, random.choice(U)))
    Ref = make_ref(U, attacks); Aop = A(U, Ref)
    for r in range(n + 1):
        for X in itertools.combinations(U, r):
            if Aop(Aop(set(X))) != F(U, attacks, X):
                mismatch += 1
                break

# (2) toy model of file 17 as a SETAF
U = ["D_pot", "D_E", "S_pot", "S_E", "E_pot", "G", "P", "M", "W", "Z", "N"]
attacks = [(frozenset({"D_pot"}), "S_pot"), (frozenset({"D_E"}), "S_E"),
           (frozenset({"M"}), "W"), (frozenset({"P"}), "Z"), (frozenset({"N"}), "N")]
Ref = make_ref(U, attacks); Aop = A(U, Ref)
AA = lambda X: Aop(Aop(X))
core = lfp(AA, U); top = gfp(AA, U)
IN, OUT, UNDEC = grounded_labelling(U, attacks)
toy = {
    "lfp(A∘A) == grounded IN": core == IN,
    "U \\ gfp(A∘A) == grounded OUT": (set(U) - top) == OUT,
    "gfp \\ lfp == grounded UNDEC": (top - core) == UNDEC,
    "IN": sorted(IN), "OUT": sorted(OUT), "UNDEC": sorted(UNDEC),
}

# (3) cycles: odd cycle a->b->c->a, even cycle a<->b, self-attack
def cyc(names, edges):
    at = [(frozenset({s}), t) for (s, t) in edges]
    return grounded_labelling(names, at)
cycles = {
    "self-attack a->a": [sorted(s) for s in cyc(["a"], [("a", "a")])],
    "even cycle a<->b": [sorted(s) for s in cyc(["a", "b"], [("a", "b"), ("b", "a")])],
    "odd cycle a->b->c->a": [sorted(s) for s in cyc(["a", "b", "c"], [("a", "b"), ("b", "c"), ("c", "a")])],
    "unattacked a attacks b, b attacks c": [sorted(s) for s in cyc(["a", "b", "c"], [("a", "b"), ("b", "c")])],
}
print(json.dumps({"random SETAFs tested": 2000, "A∘A != F mismatches": mismatch,
                  "toy model": toy, "cycles (IN,OUT,UNDEC)": cycles}, ensure_ascii=False, indent=1))

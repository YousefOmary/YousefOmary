# series_paf.py — preference-based resolution of the even cycles in the series' framework (file 29)
# A preference-based AF (Amgoud & Cayrol 2002): an attack a->b DEFEATS b unless b is strictly
# preferred to a. We compute the grounded labelling under three preference regimes.
import json, importlib.util
spec = importlib.util.spec_from_file_location("s", "series_af.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
nodes, attacks = dict(m.N), list(m.A)

# Which Priest commitment each series reply is built from (the prasanga criterion):
FROM_OPPONENT = {
 "C23":        "IC 7.3 (accept/reject/agnostic are acts, not values); IC 1.7 (consistency bought by expressive incompleteness); BLT p.41 (appearance statements unproblematic)",
 "D23.rus":    "BLT p.139 concedes systematic ambiguity works wherever the statement is universally quantified",
 "D23.witt":   "Priest holds the liar is understood although not consistently assertible (IC ch.1, 4)",
 "D23.sex":    "BLT p.41-46: Transcendence requires the statement to be in Σ; appearance statements are outside Σ",
 "D28.brandom":"the reference Priest himself gives (Brandom 1983) via its default-and-challenge structure",
 "D28.kant":   "Kant's own A74-75/B99-101 (the text Priest interprets)",
 "D21.compute":"Priest's own definition of revenge (IC 1.5) computed",
 "D23.act":    "IC 7.3 trichotomy of acts",
 "D16.status": "GP 2003 p.6: ultimate reality only conventionally real",
 "D15.acts":   "IC 19.9 keeps the acts incompatible",
}
IMPORTED = {  # Priest premises not derived from the series' commitments and not argued for in the texts read
 "E.univ": "univocity of assertion (BLT p.48, p.139): argued only by citing Brandom, which does not support it",
 "E.p139": "'there must be such a thought' (psychological premise)",
 "E.p191": "understood ⇒ not nonsense ⇒ proposition ⇒ sayable",
 "E.p48":  "intends us to believe ⇒ asserts univocally",
 "E.p82":  "a limiting judgment applies the categories to objects",
 "E.gap":  "trichotomy ⇒ gap theory",
 "E.rev":  "the model must express its stability predicate",
 "E.D2":   "end-of-analysis ⇒ ultimate status",
 "E.19.9": "rational dilemmas",
 "E.brandom": "Priest's gloss of Brandom as 'objective truth'",
 "E.modal": "'problematic' = category of possibility",
}
def grounded(nodes, defeats):
    IN, OUT = set(), set(); ch = True
    att = {x: [s for (s,t) in defeats if t == x] for x in nodes}
    while ch:
        ch = False
        for x in nodes:
            if x in IN or x in OUT: continue
            if all(s in OUT for s in att[x]): IN.add(x); ch = True
            elif any(s in IN for s in att[x]): OUT.add(x); ch = True
    return IN, OUT, set(nodes) - IN - OUT

def run(pref):   # pref(b, a) -> True if b strictly preferred to a (so a's attack on b fails)
    defeats = [(s,t) for (s,t,_) in attacks if not pref(t, s)]
    IN, OUT, UND = grounded(nodes, defeats)
    lab = lambda x: "IN" if x in IN else "OUT" if x in OUT else "UNDEC"
    claims = sorted(x for x in nodes if nodes[x][0] == "C")
    return {x: lab(x) for x in claims}

regimes = {
 "no preference (plain grounded)": lambda b, a: False,
 "prasanga priority (series replies from Priest's own commitments outrank imported premises)":
     lambda b, a: (b in FROM_OPPONENT and a in IMPORTED),
 "reverse (Priest's premises as default outrank the series' replies)":
     lambda b, a: (b in IMPORTED and a in FROM_OPPONENT),
}
res = {k: run(p) for k, p in regimes.items()}
focus = ["C21.sex","C22.kant","C22.rus","C22.witt","C23","C15","C16","C17"]
json.dump({"regimes": res, "from_opponent": FROM_OPPONENT, "imported": IMPORTED}, open("series_paf_labelling.json","w"), ensure_ascii=False, indent=1)
print(f"{'claim':10s}" + "".join(f"{k[:28]:30s}" for k in res))
for c in focus:
    print(f"{c:10s}" + "".join(f"{res[k][c]:30s}" for k in res))

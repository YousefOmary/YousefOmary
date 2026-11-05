# mmk_af_robustness.py (file 31): how sensitive is the MMK grounded labelling to extraction errors?
import json, random, importlib.util
spec = importlib.util.spec_from_file_location("m", "mmk_af.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
nodes = dict(m.N); base = list(m.A)
def grounded(nodes, attacks):
    IN, OUT = set(), set(); ch = True
    att = {x: [s for (s,t,_) in attacks if t == x] for x in nodes}
    while ch:
        ch = False
        for x in nodes:
            if x in IN or x in OUT: continue
            if all(s in OUT for s in att[x]): IN.add(x); ch = True
            elif any(s in IN for s in att[x]): OUT.add(x); ch = True
    return IN, OUT, set(nodes) - IN - OUT
def key(IN, OUT, UND):
    return {"P.empty IN": "P.empty" in IN, "S.view OUT": "S.view" in OUT,
            "UNDEC exactly 18.7+25.24": UND == {"N18.7","N25.24"},
            "no thesis IN": not any(nodes[x][0]=="T" and x in IN for x in nodes),
            "all P IN": all(x in IN for x in nodes if nodes[x][0]=="P")}
random.seed(11)
ids = list(nodes)
def noisy(p_del, p_add, trials=500):
    agg = {}
    for _ in range(trials):
        at = [e for e in base if random.random() > p_del]
        n_add = int(p_add * len(base))
        for _ in range(n_add):
            s, t = random.choice(ids), random.choice(ids)
            if s != t and nodes[s][0] in ("V","O","P"): at.append((s, t, "noise"))
        k = key(*grounded(nodes, at))
        for kk, v in k.items(): agg[kk] = agg.get(kk, 0) + (1 if v else 0)
    return {kk: round(v / trials, 3) for kk, v in agg.items()}
results = {"baseline": key(*grounded(nodes, base)),
           "delete 10% of attacks (500 trials)": noisy(0.10, 0.0),
           "delete 20% of attacks": noisy(0.20, 0.0),
           "add 10% random attacks from V/O/P nodes": noisy(0.0, 0.10),
           "delete 10% and add 10%": noisy(0.10, 0.10)}
# contested segmentations: flip the status of each O-node to a Nagarjuna argument (its attacks then hit Nagarjuna's targets? no: flipping kind means its attack on V becomes Nagarjuna attacking himself) -> instead model "misattribution": the objection is unanswered (drop the reply edge)
flips = {}
for o in [x for x in nodes if nodes[x][0]=="O"]:
    at = [e for e in base if not (e[1] == o)]   # nobody answers objection o
    IN, OUT, UND = grounded(nodes, at)
    flips[o] = {"P.empty": "IN" if "P.empty" in IN else ("OUT" if "P.empty" in OUT else "UNDEC"),
                "targets of unanswered objection now": sorted({t for (s,t,_) in base if s == o and t not in IN})}
results["each objection left unanswered (reply edges removed)"] = flips
json.dump(results, open("mmk_af_robustness.json","w"), ensure_ascii=False, indent=1)
print(json.dumps(results, ensure_ascii=False, indent=1))

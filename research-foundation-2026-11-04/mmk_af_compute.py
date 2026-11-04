import json, re, importlib.util
spec = importlib.util.spec_from_file_location("mmk_af", "mmk_af.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def grounded(nodes, attacks):
    IN, OUT = set(), set(); changed = True
    att = {x: [s for (s,t,_) in attacks if t == x] for x in nodes}
    while changed:
        changed = False
        for x in nodes:
            if x in IN or x in OUT: continue
            if all(s in OUT for s in att[x]): IN.add(x); changed = True
            elif any(s in IN for s in att[x]): OUT.add(x); changed = True
    return IN, OUT, set(nodes) - IN - OUT

def build(with_vv=False, self_attack=True, n2524_attacks_teachings=False, keep_24_8=True, collapse_view=False):
    nodes = dict(m.N); attacks = list(m.A)
    if with_vv: nodes.update(m.X_N); attacks += m.X_A
    attacks = [t for t in attacks if t[0] in nodes and t[1] in nodes]
    if not self_attack: attacks = [t for t in attacks if t[0] != t[1]]
    if n2524_attacks_teachings:
        for x,(k,_,_) in list(nodes.items()):
            if k == "P" and x != "P24.8": attacks.append(("N25.24", x, "GP reading: no ultimate truth undermines every positive teaching"))
        if keep_24_8: attacks.append(("P24.8", "N25.24", "24.8-24.10: the ultimate is taught by reliance on the conventional"))
    if collapse_view:
        attacks = [(s, "P.empty" if t == "S.view" else t, v) for (s,t,v) in attacks]
    return nodes, attacks

def summarize(nodes, attacks):
    IN, OUT, UND = grounded(nodes, attacks)
    lab = lambda x: "IN" if x in IN else "OUT" if x in OUT else "UNDEC"
    kinds = lambda S: {k: sum(1 for x in S if nodes[x][0]==k) for k in "TVOPSNX" if any(nodes[x][0]==k for x in S)}
    return {"nodes": len(nodes), "attacks": len(attacks), "IN": kinds(IN), "OUT": kinds(OUT), "UNDEC": sorted(UND),
            "theses IN": sorted(x for x in IN if nodes[x][0]=="T"),
            "objections IN": sorted(x for x in IN if nodes[x][0]=="O"),
            "P.empty": lab("P.empty"), "S.view": lab("S.view"), "N13.1": lab("N13.1"), "N18.7": lab("N18.7"), "N25.24": lab("N25.24"),
            "positive claims UNDEC or OUT": sorted(x for x in nodes if nodes[x][0]=="P" and lab(x)!="IN"),
            "labels": {x: lab(x) for x in nodes}}

variants = {
 "A. MMK only": build(),
 "B. MMK + VV layer": build(with_vv=True),
 "C. no self-attack rule (R* off)": build(self_attack=False),
 "D. 25.24 attacks every teaching, 24.8-10 defends": build(n2524_attacks_teachings=True, keep_24_8=True),
 "E. 25.24 attacks every teaching, 24.8-10 ignored": build(n2524_attacks_teachings=True, keep_24_8=False),
 "F. S.view collapsed into P.empty (emptiness itself a view)": build(collapse_view=True),
}
res = {k: summarize(*v) for k,v in variants.items()}
json.dump(res, open("mmk_af_labelling.json","w"), ensure_ascii=False, indent=1)
for k,v in res.items():
    print("==", k, "| nodes", v["nodes"], "attacks", v["attacks"])
    print("   IN", v["IN"], "OUT", v["OUT"], "UNDEC", v["UNDEC"])
    print("   theses IN", v["theses IN"], "| objections IN", v["objections IN"])
    print("   P.empty", v["P.empty"], "S.view", v["S.view"], "N13.1", v["N13.1"], "N18.7", v["N18.7"], "N25.24", v["N25.24"])
    print("   positive claims not IN:", v["positive claims UNDEC or OUT"][:12], "..." if len(v["positive claims UNDEC or OUT"])>12 else "")
# coverage
covered=set()
for (_,_,v) in m.N.values():
    for part in v.split(","):
        mm=re.match(r"\s*(\d+)\.(\d+)(?:[ab])?(?:-(\d+)\.(\d+))?",part)
        if mm:
            c=int(mm.group(1)); s=int(mm.group(2)); e=int(mm.group(4)) if mm.group(4) else s
            for k in range(s,e+1): covered.add((c,k))
counts=[14,25,9,9,8,10,34,13,12,16,8,10,8,8,11,10,33,12,6,24,21,16,25,40,24,12,30]
allv={(c+1,k) for c in range(27) for k in range(1,counts[c]+1)}
print("verse coverage:", len(covered & allv), "/", len(allv), "missing:", sorted(allv-covered))
# audit table
with open("mmk_af_table.md","w") as f:
    f.write("| id | kind | label | verses | label (A: MMK only) | attacked by |\n|---|---|---|---|---|---|\n")
    nodesA, attA = variants["A. MMK only"]; labA = res["A. MMK only"]["labels"]
    for x,(k,l,v) in nodesA.items():
        atk = ", ".join(sorted({s for (s,t,_) in attA if t==x}))
        f.write(f"| {x} | {k} | {l} | {v} | {labA[x]} | {atk} |\n")
print("table rows:", len(nodesA))

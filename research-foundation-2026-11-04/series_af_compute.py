import json, importlib.util
spec = importlib.util.spec_from_file_location("s", "series_af.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
nodes, attacks = m.N, m.A
att = {x: [s for (s,t,_) in attacks if t == x] for x in nodes}
IN, OUT = set(), set(); ch = True
while ch:
    ch = False
    for x in nodes:
        if x in IN or x in OUT: continue
        if all(s in OUT for s in att[x]): IN.add(x); ch = True
        elif any(s in IN for s in att[x]): OUT.add(x); ch = True
UND = set(nodes) - IN - OUT
lab = lambda x: "IN" if x in IN else "OUT" if x in OUT else "UNDEC"
claims = [x for x in nodes if nodes[x][0] == "C"]
rows = []
for x in claims:
    status = lab(x)
    if status == "IN":
        status += " (unattacked)" if not att[x] else " (defended)"
    rows.append((x, status, nodes[x][1], ", ".join(att[x])))
out = {"claims": {x: s for (x, s, _, _) in rows},
       "IN defended": [x for (x,s,_,_) in rows if s=="IN (defended)"],
       "IN unattacked": [x for (x,s,_,_) in rows if s=="IN (unattacked)"],
       "UNDEC": [x for (x,s,_,_) in rows if s=="UNDEC"],
       "OUT": [x for (x,s,_,_) in rows if s=="OUT"],
       "all labels": {x: lab(x) for x in nodes}}
json.dump(out, open("series_af_labelling.json","w"), ensure_ascii=False, indent=1)
for r in rows: print(f"{r[0]:9s} {r[1]:18s} {r[2][:95]}  <- {r[3]}")
print("\nIN defended:", out["IN defended"]); print("IN unattacked:", out["IN unattacked"]); print("UNDEC:", out["UNDEC"]); print("OUT:", out["OUT"])

# lenient variant: recorded limitations (L) are not attacks
nodes2 = {x:v for x,v in nodes.items() if v[0] != "L"}; attacks2 = [t for t in attacks if t[0] in nodes2 and t[1] in nodes2]
att2 = {x: [s for (s,t,_) in attacks2 if t == x] for x in nodes2}
IN2, OUT2 = set(), set(); ch = True
while ch:
    ch = False
    for x in nodes2:
        if x in IN2 or x in OUT2: continue
        if all(s in OUT2 for s in att2[x]): IN2.add(x); ch = True
        elif any(s in IN2 for s in att2[x]): OUT2.add(x); ch = True
UND2 = set(nodes2) - IN2 - OUT2
lab2 = lambda x: "IN" if x in IN2 else "OUT" if x in OUT2 else "UNDEC"
len_ = {"IN defended": sorted(x for x in claims if x in IN2 and att2[x]),
        "IN unattacked": sorted(x for x in claims if x in IN2 and not att2[x]),
        "UNDEC": sorted(x for x in claims if x in UND2), "OUT": sorted(x for x in claims if x in OUT2)}
out["lenient (limitations not attacks)"] = len_
json.dump(out, open("series_af_labelling.json","w"), ensure_ascii=False, indent=1)
print("\nLENIENT:", len_)

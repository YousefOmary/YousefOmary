# pp1_aba.py  (file 32)
# The Buddhapalita / Bhaviveka / Candrakirti debate on MMK 1.1 ("na svatah") in
# Prasannapada chapter one (PsP M §22-§60, MacDonald 2015; PsP L 14-36), formalised as
# assumption-based argumentation (ABA: Bondarenko, Dung, Kowalski & Toni 1997;
# Dung, Kowalski & Toni 2009).  ABA is the structured counterpart of Dung's abstract
# frameworks used in files 25-26: arguments are deductions from a set of ASSUMPTIONS
# through RULES; an argument attacks another iff its conclusion is the contrary of one
# of the other's assumptions.  So an attack can only land on an assumption, and an
# argument that uses no assumption cannot be attacked at all.
#
# Hypothesis under test (file 25 §4): Prasangika = skeptical (grounded) semantics,
# Svatantrika = credulous (preferred) semantics with an added shared datum.
# Rival formalisation: the difference lies in the STRUCTURE, not in the semantics:
#   (i)  assumption ownership: the Madhyamika's arguments carry no assumption of his
#        own (VV 29 "no thesis of mine"; CS 16.25 cited at §26), hence are unattackable;
#   (ii) attack provenance: an attack on a party counts only if built from that party's
#        own theory (§28 burden on the proposer; §57 court rule: never by the plaintiff's
#        word alone), against Dignaga's "ascertained for both" rule (§59);
#   (iii) the qualifier "ultimately" parameterises Bhaviveka's thesis to a context, and the
#        subject of the thesis is parameterised with it (§45-§49), so the thesis undermines
#        its own subject.
# Every variant is labelled under grounded, preferred and stable semantics, so the
# hypothesis can be checked directly: does the semantics make any difference?
import itertools, json, random

# ---------- ABA machinery ----------
def arguments(rules, assumptions, facts=()):
    """All (support, conclusion) pairs derivable; support = set of assumptions used.
    rules: list of (head, body-tuple). facts: atoms with empty body."""
    rules = list(rules) + [(f, ()) for f in facts]
    args = {(frozenset({a}), a) for a in assumptions}
    changed = True
    while changed:
        changed = False
        for head, body in rules:
            # every way of supporting every body atom
            options = []
            for b in body:
                opts = [S for (S, c) in args if c == b]
                if not opts: break
                options.append(opts)
            else:
                for combo in itertools.product(*options):
                    S = frozenset().union(*combo) if combo else frozenset()
                    if (S, head) not in args:
                        args.add((S, head)); changed = True
    # keep only minimal supports per conclusion
    out = set()
    for (S, c) in args:
        if not any((S2 < S and c2 == c) for (S2, c2) in args):
            out.add((S, c))
    return sorted(out, key=lambda x: (x[1], sorted(x[0])))

def attacks(args, contrary):
    """arg i attacks arg j iff conclusion(i) == contrary(alpha) for some alpha in support(j)."""
    at = []
    for i, (S, c) in enumerate(args):
        for j, (S2, c2) in enumerate(args):
            if any(contrary.get(a) == c for a in S2):
                at.append((i, j))
    return at

def grounded(n, at):
    IN, OUT = set(), set(); ch = True
    attackers = {j: [i for (i, k) in at if k == j] for j in range(n)}
    while ch:
        ch = False
        for x in range(n):
            if x in IN or x in OUT: continue
            if all(i in OUT for i in attackers[x]): IN.add(x); ch = True
            elif any(i in IN for i in attackers[x]): OUT.add(x); ch = True
    return IN, OUT, set(range(n)) - IN - OUT

def conflict_free(E, at): return not any((i in E and j in E) for (i, j) in at)
def defends(E, x, at):
    return all(any((k, i) in atset for k in E) for (i, j) in at if j == x for atset in [set(at)])
def admissible(E, at): return conflict_free(E, at) and all(defends(E, x, at) for x in E)
def preferred(n, at):
    adm = [frozenset(E) for r in range(n + 1) for E in itertools.combinations(range(n), r) if admissible(set(E), at)]
    return [E for E in adm if not any(E < F for F in adm)]
def stable(n, at):
    return [frozenset(E) for r in range(n + 1) for E in itertools.combinations(range(n), r)
            if conflict_free(set(E), at) and all((x in E) or any((i, x) in set(at) for i in E) for x in range(n))]

def label(name, atoms_of_interest, rules, assumptions, contrary, facts=(), note=""):
    args = arguments(rules, assumptions, facts)
    at = attacks(args, contrary)
    n = len(args)
    IN, OUT, UND = grounded(n, at)
    pref = preferred(n, at); stab = stable(n, at)
    def status_of(atom):
        idx = [i for i, (S, c) in enumerate(args) if c == atom]
        if not idx: return "not derivable"
        g = "IN" if any(i in IN for i in idx) else "OUT" if all(i in OUT for i in idx) else "UNDEC"
        cred = any(any(i in E for i in idx) for E in pref)
        skep = bool(pref) and all(any(i in E for i in idx) for E in pref)
        st = ("no stable ext" if not stab else
              "IN all" if all(any(i in E for i in idx) for E in stab) else
              "IN some" if any(any(i in E for i in idx) for E in stab) else "IN none")
        return {"grounded": g, "credulous(preferred)": cred, "skeptical(preferred)": skep, "stable": st,
                "supports": [sorted(args[i][0]) for i in idx]}
    res = {"note": note, "n_arguments": n, "n_attacks": len(at),
           "arguments": [f"{{{','.join(sorted(S))}}} |- {c}" for (S, c) in args],
           "attacks": [f"{args[i][1]} -> {args[j][1]} (on {sorted(set(args[j][0]) & {a for a in contrary if contrary[a]==args[i][1]})})" for (i, j) in at],
           "status": {a: status_of(a) for a in atoms_of_interest},
           "n_preferred": len(pref), "n_stable": len(stab)}
    return res

results = {}

# ---------- V1: Buddhapalita's prasanga inside the Samkhya's own theory (§22-§25, §29-§30) ----------
# Samkhya theory T_S.  Assumption: svata ("things arise from self", the thesis proposed).
# Maintained commitments (svabhyupagama, §24): satkarya (the effect pre-exists in its cause by own
# nature), existent_no_rearise (what already exists by own nature does not arise again: the pot in
# front, §30), no_endless_arising (§24 "you do not assent to a succession without end").
# Buddhapalita's two consequences are rules the Samkhya himself must grant:
#   rearising_of_existent <- svata, satkarya        ("from self" = the already existing thing is what arises)
#   pointless            <- rearising_of_existent, existent_no_rearise
#   endless              <- rearising_of_existent   (if the existent arises, it never stops arising)
#   not_svata            <- pointless  ;  not_svata <- endless, no_endless_arising
S_rules = [("rearising_of_existent", ("svata", "satkarya")),
           ("pointless", ("rearising_of_existent", "existent_no_rearise")),
           ("endless", ("rearising_of_existent",)),
           ("not_svata", ("pointless",)),
           ("not_svata", ("endless", "no_endless_arising"))]
S_facts = ["satkarya", "existent_no_rearise", "no_endless_arising"]
S_contrary = {"svata": "not_svata"}
results["V1 prasanga in the Samkhya's own theory"] = label(
    "V1", ["svata", "not_svata"], S_rules, ["svata"], S_contrary, S_facts,
    note="Buddhapalita §22; Candrakirti §24: 'your assertion is illogical and contradicted by what you yourself maintain'. "
         "The Madhyamika contributes no assumption; the only assumption in play is the Samkhya's thesis.")
# NB: with svata as assumption the consequence 'not_svata' is derived FROM svata plus the Samkhya's
# facts, so its support is {svata}: an argument that uses the opponent's thesis to refute it.
# Record both readings: support-carrying (reductio form) and the paraprasiddha inference of §29
# in which the reason 'existing by own nature' is applied directly (support empty).
S_rules_29 = [("not_svata", ("existing_by_own_nature", "existent_no_rearise"))]
results["V1b the inference Candrakirti reads out of the prasanga (§29-§30)"] = label(
    "V1b", ["svata", "not_svata"], S_rules_29, ["svata"], S_contrary,
    ["existing_by_own_nature", "existent_no_rearise"],
    note="§29: reason = 'existing by own nature' (the Samkhya's satkarya), example = the pot in front (acknowledged by the opponent alone, "
         "paraprasiddha). The refuting argument has EMPTY support: nothing in it is the Madhyamika's.")

# ---------- V1c: the Samkhya's own proof of svata (§28) ----------
# §28: the Samkhya's proof has 'nothing but his mere thesis as its core' (pratijnamatra): modelled as
# a proof whose premises are the thesis itself.  Then not even a second argument for svata exists.
results["V1c the Samkhya's proof is his thesis (§28)"] = label(
    "V1c", ["svata"], [("svata", ("svata_proof",)), ("svata_proof", ("svata",))] + S_rules_29, ["svata"],
    S_contrary, ["existing_by_own_nature", "existent_no_rearise"],
    note="§28: 'only the opponent has to employ a proof of the matter proposed'; the burden is his, and his proof is circular.")

# ---------- V2: Bhaviveka's reversal (§23 third charge; §35 reply; §21 prasajya) ----------
# Reversal needs the rule EX: parata <- not_svata (negation of self-arising affirms other-arising).
# §21: a prasajya negation is intended, other-arising will be negated too; §35: the reverse meaning
# 'results only for the opponent, not for us, because there is no thesis of our own'.
# Madhyamika theory T_M for 1.1: facts from MMK 1.3cd (no own-being in the conditions) give not_parata.
M_rules_rev = [("not_parata", ("no_svabhava_in_conditions",))]
def kritanta_virodha(with_EX):
    rules = M_rules_rev + ([("parata", ("not_svata",))] if with_EX else [])
    args = arguments(rules, [], ["no_svabhava_in_conditions", "not_svata"])
    concl = {c for (S, c) in args if not S}
    return {"derives parata": "parata" in concl, "derives not_parata": "not_parata" in concl,
            "contradiction with own tenets (krtantavirodha)": {"parata", "not_parata"} <= concl}
results["V2 the reversal needs the exhaustiveness rule EX"] = {
    "Madhyamika theory without EX (§21 prasajya-pratisedha)": kritanta_virodha(False),
    "Madhyamika theory with EX added (Bhaviveka's reading of the prasanga)": kritanta_virodha(True),
    "note": "The reversal lands on whoever holds EX (§35 'parasyaiva sambandhah'). The Madhyamika's attack on svata is an "
            "attack, not the assertion of parata: 'the adducing of the consequence has as its result the mere negation "
            "(pratisedhamatra) of the opponent's thesis' (§35)."}

# ---------- V3: Bhaviveka's svatantra inference with the qualifier 'ultimately' (§39-§49) ----------
# "Ultimately, the internal bases have not arisen from self, because they exist, like consciousness."
# The inference needs: subject (the internal bases, as locus, dharmin), reason (exist), pervasion.
# (a) subject taken ultimately (§45): assumption subject_ult, contrary not_subject_ult.
#     Madhyamika's own tenet: nothing is established ultimately (no_ult_existence) -> not_subject_ult;
#     and the thesis' own conclusion not_svata_ult with 'what does not arise is no ultimate locus' (§48:
#     'when non-arising is the sadhya the dharmin is lost') -> not_subject_ult.  Self-undermining.
B_rules_a = [("not_svata_ult", ("subject_ult", "exist", "pervasion")),
             ("not_subject_ult", ("no_ult_existence",)),
             ("not_subject_ult", ("not_svata_ult", "nonarisen_no_locus"))]
results["V3a svatantra inference, subject ultimate (§45, §48)"] = label(
    "V3a", ["not_svata_ult", "subject_ult"], B_rules_a, ["subject_ult"], {"subject_ult": "not_subject_ult"},
    ["exist", "pervasion", "no_ult_existence", "nonarisen_no_locus"],
    note="asiddhadhara paksadosa / asrayasiddha hetudosa 'from his own side' (svatah).")
# (a') drop the Madhyamika's general tenet, keep only the self-undermining link (§48 alone)
results["V3a' subject ultimate, self-undermining link only (§48)"] = label(
    "V3a'", ["not_svata_ult", "subject_ult"], B_rules_a[:1] + B_rules_a[2:], ["subject_ult"],
    {"subject_ult": "not_subject_ult"}, ["exist", "pervasion", "nonarisen_no_locus"],
    note="the thesis attacks its own subject: a self-attacking argument.")
# (b) subject taken conventionally (§46-§47): assumption subject_conv (prajnaptisat); the Samkhya holds
#     the bases are dravyasat, not prajnaptisat -> not_subject_conv from HIS theory (parato 'siddhadhara).
B_rules_b = [("not_svata_ult", ("subject_conv", "exist", "pervasion")),
             ("not_subject_conv", ("dravyasat",))]
results["V3b svatantra inference, subject conventional (§47)"] = label(
    "V3b", ["not_svata_ult", "subject_conv"], B_rules_b, ["subject_conv", "dravyasat"],
    {"subject_conv": "not_subject_conv", "dravyasat": "not_dravyasat"}, ["exist", "pervasion"],
    note="the opponent's own assumption dravyasat attacks the Madhyamika's assumption subject_conv; nothing in this local "
         "framework attacks dravyasat (that would be another prasanga, i.e. the whole dispute).")
# (c) general subject (§48 reply): the subject exists for the Madhyamika only through error (viparyasa);
#     error and non-error are exclusive; non-arising as sadhya is the state of non-error -> no subject.
B_rules_c = [("not_svata_ult", ("subject_gen", "exist", "pervasion")),
             ("subject_gen", ("error",)),
             ("not_error", ("not_svata_ult", "nonarising_is_nonerror")),
             ("not_subject_gen", ("not_error", "error_nonerror_exclusive"))]
results["V3c general subject (§48-§49)"] = label(
    "V3c", ["not_svata_ult", "subject_gen", "error"], B_rules_c, ["subject_gen", "error"],
    {"subject_gen": "not_subject_gen", "error": "not_error"},
    ["exist", "pervasion", "nonarising_is_nonerror", "error_nonerror_exclusive"],
    note="§49: 'the proponent of emptiness and the proponent of non-emptiness do not accept a visual faculty in general, "
         "either on the surface or ultimately' - no common subject; formally the same self-attack as (a).")

# ---------- V4: 'the fault of both' (§56): do the Madhyamika's inferences carry assumptions? ----------
v4 = {}
for name, key in [("Buddhapalita/Candrakirti §29 inference", "V1b the inference Candrakirti reads out of the prasanga (§29-§30)"),
                  ("Bhaviveka §39 inference (ultimate subject)", "V3a svatantra inference, subject ultimate (§45, §48)"),
                  ("Bhaviveka §39 inference (conventional subject)", "V3b svatantra inference, subject conventional (§47)")]:
    r = results[key]
    concl = "not_svata" if "V1b" in key else "not_svata_ult"
    v4[name] = {"support of the refuting argument": r["status"][concl]["supports"], "attackable": any(r["status"][concl]["supports"])}
v4["note"] = ("§56 reply: 'this fault occurs for those voicing an independent inference; we do not employ one, because our "
              "inferences result in the negation of the opponent's thesis'. In ABA an attack lands only on an assumption: an "
              "argument with empty support has nothing to be hit.")
results["V4 the fault of both (§56)"] = v4

# ---------- V5: the madman (§25): an opponent who maintains nothing ----------
results["V5 the madman: opponent with no maintained commitments (§25)"] = label(
    "V5", ["svata", "not_svata"], S_rules, ["svata"], S_contrary, [],
    note="'we do not debate with a madman': with no commitments to build from, no prasanga exists and the thesis stands unrefuted. "
         "This is the cost of the method: it refutes only from what the opponent grants.")

# ---------- V6: Bhaviveka's own procedure turned on himself (§50-§53) ----------
# Against the Sarvastivadin, Bhaviveka split the reason: conventionally -> unestablished for the opponent's
# own side; ultimately -> unestablished since nothing is ultimately produced. Candrakirti: apply the same
# split to Bhaviveka's own reasons (sattvat, paratvat, bhutatvat): unestablished 'right from his own side'.
B6_rules = [("not_svata_ult", ("subject_ult", "exist_ult", "pervasion")),
            ("not_exist_ult", ("bhaviveka_split_rule",)),    # his own rule: real-thing reasons are not established ultimately
            ("not_subject_ult", ("bhaviveka_split_rule",))]
results["V6 Bhaviveka's split rule applied to his own reasons (§50-§53)"] = label(
    "V6", ["not_svata_ult"], B6_rules, ["subject_ult", "exist_ult"],
    {"subject_ult": "not_subject_ult", "exist_ult": "not_exist_ult"}, ["pervasion", "bhaviveka_split_rule"],
    note="a prasanga against Bhaviveka: an argument with empty support in HIS theory attacks his assumptions.")

# ---------- V7: attack provenance (§57 court rule) vs Dignaga's ubhayaniscita (§59) ----------
# Two parties, each with its own theory.  Under the court rule an argument may attack an assumption of
# party P only if it is built from P's theory (the defendant's own word) or from a shared theory (the
# witness), never from the plaintiff's theory alone.  Under Dignaga's rule, only arguments built from
# the SHARED theory count as proof or refutation.  Compute what each rule yields for the prasanga V1b.
def provenance(rule):
    shared = []                         # §49: no common subject -> shared theory empty for this debate
    samkhya = ["existing_by_own_nature", "existent_no_rearise"]
    madhyamika = ["no_svabhava_in_conditions"]
    args = arguments(S_rules_29, ["svata"], samkhya)
    refuters = [(S, c) for (S, c) in args if c == "not_svata"]
    ok = []
    for (S, c) in refuters:
        facts_used = set(samkhya)   # all facts of V1b are the Samkhya's
        if rule == "court":   ok.append(facts_used <= set(samkhya) | set(shared))
        if rule == "dignaga": ok.append(facts_used <= set(shared))
    return {"refutation of svata counts": bool(ok) and all(ok)}
results["V7 provenance rule"] = {"court rule (§57: defendant's own word or shared witness)": provenance("court"),
                                 "Dignaga's rule (§59: ascertained for both only)": provenance("dignaga"),
                                 "note": "With no common subject (§49) the shared theory is empty; under Dignaga's rule no refutation and no proof "
                                         "is possible at all in this debate, under the court rule the prasanga counts. This is the file-29 "
                                         "'prasanga priority' as a norm stated by the text."}

# ---------- Theorem check: assumption-free arguments are in every complete extension ----------
random.seed(11); bad = 0; trials = 0
for _ in range(3000):
    atoms = [f"p{i}" for i in range(random.randint(2, 5))]
    assumptions = random.sample(atoms, random.randint(1, len(atoms)))
    contrary = {a: f"n{a}" for a in assumptions}
    rules = []
    for _ in range(random.randint(1, 6)):
        head = random.choice(list(contrary.values()) + atoms)
        body = tuple(random.sample(atoms, random.randint(0, 2)))
        rules.append((head, body))
    args = arguments(rules, assumptions, [])
    at = attacks(args, contrary)
    IN, OUT, UND = grounded(len(args), at)
    for i, (S, c) in enumerate(args):
        if not S:
            trials += 1
            if i not in IN: bad += 1
            # also: in every preferred extension
            if not all(i in E for E in preferred(len(args), at)): bad += 1
results["theorem check"] = {"random ABA frameworks": 3000, "assumption-free arguments found": trials,
                            "not IN (grounded) or missing from some preferred extension": bad}

# ---------- Does the semantics matter?  (the file-25 hypothesis) ----------
sem = {}
for k, r in results.items():
    if isinstance(r, dict) and "status" in r:
        for atom, st in r["status"].items():
            if isinstance(st, dict):
                sem[f"{k} :: {atom}"] = {"grounded": st["grounded"], "credulous": st["credulous(preferred)"],
                                         "skeptical": st["skeptical(preferred)"], "stable": st["stable"]}
differ = [k for k, v in sem.items() if (v["grounded"] == "IN") != v["skeptical"] or (v["grounded"] == "IN") != v["credulous"]]
results["semantics comparison"] = {"cases": sem, "cases where credulous/skeptical/grounded disagree": differ}

json.dump(results, open("pp1_aba.json", "w"), ensure_ascii=False, indent=1)
for k, r in results.items():
    print("==", k)
    if isinstance(r, dict) and "status" in r:
        for atom, st in r["status"].items(): print("  ", atom, "->", st if isinstance(st, str) else {x: st[x] for x in ("grounded", "credulous(preferred)", "skeptical(preferred)", "stable", "supports")})
        print("   args:", r["arguments"]); print("   attacks:", r["attacks"])
    else:
        print("  ", json.dumps(r, ensure_ascii=False)[:600])

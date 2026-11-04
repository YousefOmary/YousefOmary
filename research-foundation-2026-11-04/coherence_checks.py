"""Checks for file 10 (corrected after review 11).

A. Westerhoff's §89 cycle: truth values are a function of expression counts;
   changing a claimed numeral falsifies that sentence only.  Truth-teller
   variant: 2 fixed points; one negation: 0 (bivalent evaluation only).
   This tests the specific example, not how judgments about carriers get
   their truth in general.
B. Review-11 point: a proposition q that coheres with both rival sets S and T
   is coherence-true in both.  So invariance of truth value across the choice
   of specified set does NOT show non-coherence truth.  (Replaces the former
   check C, whose "invariance" was built into the code.)
C. Consistency model: with T taken as the specified set, Spec(T) true,
   Spec(S) false, and "holders of S are wrong about e" true.  So the four
   premises t1-t4 of the first version are jointly satisfiable; the claim of
   inconsistency is withdrawn.
"""
import json, itertools

results = {}

# ---------- A ----------
sentences = {"a": 3, "b": 3, "a'": 3, "b'": 3, "a''": 3, "b''": 3}  # claimed counts
CARRIER_COUNT = 3  # each carrier is (predicate, name, numeral)
def eval_cycle(claims): return {k: (CARRIER_COUNT == v) for k, v in claims.items()}
vals = eval_cycle(sentences)
results["A_cycle_all_true"] = all(vals.values())
alt = dict(sentences); alt["a"] = 4
va = eval_cycle(alt)
results["A_changed_numeral_falsifies_that_sentence_only"] = (not va["a"]) and all(va[k] for k in va if k != "a")
def fps(neg):
    out = []
    for asg in itertools.product([False, True], repeat=3):
        if all(asg[i] == ((not asg[(i+1)%3]) if neg[i] else asg[(i+1)%3]) for i in range(3)):
            out.append(asg)
    return out
results["A_truth_teller_fixed_points"] = len(fps((False, False, False)))
results["A_one_negation_fixed_points"] = len(fps((True, False, False)))

# ---------- B ----------
# atoms: e, q, sS, sT.  S = Cn{e, sS, ~sT, q}; T = Cn{~e, ~sS, sT, q}.
S = {"e": True,  "q": True, "sS": True,  "sT": False}
T = {"e": False, "q": True, "sS": False, "sT": True}
def coh(p, X):           # Coh(p, X) iff X |= p, for literals here
    name, val = p
    return X[name] == val
results["B_q_coherence_true_in_S"] = coh(("q", True), S)
results["B_q_coherence_true_in_T"] = coh(("q", True), T)
results["B_invariance_without_non_coherence_truth"] = (
    results["B_q_coherence_true_in_S"] and results["B_q_coherence_true_in_T"])

# ---------- C ----------
specified = T
def true_(p): return coh(p, specified)
results["C_Spec_T_true"] = true_(("sT", True))
results["C_Spec_S_false"] = not true_(("sS", True))
results["C_not_e_true"] = true_(("e", False))
# "holders of S are wrong about e" := S assigns e a value the specified set rejects
results["C_S_wrong_about_e_in_this_model"] = (S["e"] != specified["e"])
results["C_premises_t1_t4_jointly_satisfiable"] = all([
    results["C_Spec_T_true"], results["C_Spec_S_false"],
    results["C_not_e_true"], results["C_S_wrong_about_e_in_this_model"]])

print(json.dumps(results, indent=2))
with open(__file__.replace(".py", ".json"), "w") as f:
    json.dump(results, f, indent=2)

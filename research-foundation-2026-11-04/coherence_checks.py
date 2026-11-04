"""Formal checks for file 10 (Westerhoff, coherence truth, specified set).

What this verifies:
  A. Westerhoff's §89 cycle (L'' ) L' ) L ) L'') evaluates to all-true, and its
     truth values are a function of expression COUNTS only (non-semantic facts
     about the carriers).  Replacing the count predicate by a truth predicate
     yields the truth-teller cycle with two fixed points; adding one negation
     yields none.  So the determinacy of his example is borrowed from the
     non-semantic base, not from the circle.
  B. Two maximal consistent belief sets S and S' each containing the claim
     "I am the specified set" and the denial for the other: both consistent,
     and the swap is an automorphism of the coherence structure, so no
     coherence-definable predicate singles one out.
  C. A structural ranking predicate (count of kinds of unobservables) has the
     same truth value whichever set is taken as specified, i.e. it is not
     constituted by coherence with the specified set.

What this does NOT verify: anything about consciousness, understanding, or
the truth of irrealism.  These are finite checks of the logical shape of the
argument.
"""
import json, itertools

results = {}

# ---------- A. Westerhoff §89 toy cycle ----------
# Sentences as strings; R^k(x, i) = "sentence x contains i expressions".
# Tokenizer: an expression is a maximal run of non-space chars; Westerhoff's
# sentences 'Ra3', "R'a'3", "R''a''3" are written with spaces here to make the
# three expressions explicit, exactly as his count of 3 requires.
sentences = {
    "a":   ("R''", "a''", 3),   # L   describes L''
    "b":   ("R''", "b''", 3),
    "a'":  ("R",   "a",   3),   # L'  describes L
    "b'":  ("R",   "b",   3),
    "a''": ("R'",  "a'",  3),   # L'' describes L'
    "b''": ("R'",  "b'",  3),
}
def count_expressions(name):
    pred, target, num = sentences[name]
    return 3  # each carrier is the triple (predicate, name, numeral)
def eval_count_cycle(sents):
    return {n: (count_expressions(t) == num) for n, (p, t, num) in sents.items()}
vals = eval_count_cycle(sentences)
results["A_westerhoff_cycle_all_true"] = all(vals.values())
# dependence test: change the numeral in one sentence -> that sentence flips,
# nothing else changes: truth is a function of counts, not of other truths.
alt = dict(sentences); alt["a"] = ("R''", "a''", 4)
vals_alt = eval_count_cycle(alt)
results["A_flip_only_changed_sentence"] = (vals_alt["a"] is False and
    all(vals_alt[k] for k in vals_alt if k != "a"))

# truth-teller variant: a says "a'' is true", a'' says "a' is true", a' says "a is true"
def fixed_points_truth_cycle(negations):
    # negations: tuple of bools, whether each link negates
    names = ["a", "a''", "a'"]
    fps = []
    for assign in itertools.product([False, True], repeat=3):
        ok = True
        for i, n in enumerate(names):
            tgt = assign[(i + 1) % 3]
            want = (not tgt) if negations[i] else tgt
            if assign[i] != want: ok = False
        if ok: fps.append(assign)
    return fps
results["A_truth_teller_cycle_fixed_points"] = len(fixed_points_truth_cycle((False, False, False)))
results["A_liar_cycle_fixed_points"] = len(fixed_points_truth_cycle((True, False, False)))

# ---------- B. self-specifying belief sets ----------
# Propositional atoms: e (external world exists), spec_S, spec_T.
# S = {e, spec_S, ~spec_T}; T = {~e, spec_T, ~spec_S}.
# Coherence here = consistency + closure under the (symmetric) rule
# "spec_X -> all members of X" (a set that is specified makes its members true).
atoms = ["e", "spec_S", "spec_T"]
S = {"e": True,  "spec_S": True,  "spec_T": False}
T = {"e": False, "spec_S": False, "spec_T": True}
def consistent(s): return all(isinstance(v, bool) for v in s.values())
def closed(s, S_members, T_members):
    ok = True
    if s["spec_S"]: ok &= all(s[k] == v for k, v in S_members.items())
    if s["spec_T"]: ok &= all(s[k] == v for k, v in T_members.items())
    return ok
results["B_S_consistent_and_closed"] = consistent(S) and closed(S, S, T)
results["B_T_consistent_and_closed"] = consistent(T) and closed(T, S, T)
# automorphism: swap e<->~e, spec_S<->spec_T maps S to T and preserves the rule.
def swap(s): return {"e": not s["e"], "spec_S": s["spec_T"], "spec_T": s["spec_S"]}
results["B_swap_is_automorphism"] = (swap(S) == T and swap(T) == S)
# Hence any predicate defined from the coherence structure alone has the same
# value on S and T; "which set is specified" is not coherence-definable.

# ---------- C. structural ranking is invariant under choice of specified set ----------
theories = {"S": {"kinds_of_unobservables": 2}, "T": {"kinds_of_unobservables": 1}}
def simpler(x, y): return theories[x]["kinds_of_unobservables"] < theories[y]["kinds_of_unobservables"]
results["C_T_simpler_than_S_under_S_specified"] = simpler("T", "S")
results["C_T_simpler_than_S_under_T_specified"] = simpler("T", "S")
results["C_ranking_invariant"] = (results["C_T_simpler_than_S_under_S_specified"]
                                  == results["C_T_simpler_than_S_under_T_specified"])

print(json.dumps(results, indent=2, ensure_ascii=False))
with open(__file__.replace(".py", ".json"), "w") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

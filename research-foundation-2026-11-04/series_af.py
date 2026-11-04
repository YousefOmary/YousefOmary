# series_af.py — the research series itself as an argumentation framework (file 27)
# kinds: C claim of the series (by file); R objection from an external review (06,08,11);
#        E objection from an external text (Priest, Garfield-Priest); D reply/defence by the series;
#        L a limitation the series itself recorded that functions as an attack (unmet burden).
N = {}; A = []
def n(i,k,l,src): N[i]=(k,l,src)
def a(s,t,why): A.append((s,t,why))

# --- files 04/05: total erasure ---
n("C04","C","Garfield, Priest, Westerhoff are bound to total erasure","04,05")
n("R06.lfp","R","the lfp premise was smuggled via MMK 10.10-11; D=T(D) does not force the least fixed point","review 06"); a("R06.lfp","C04","06 §2")
n("R06.circ","R","the 'framework theorem' assumes the least fixed point","review 06"); a("R06.circ","C04","06")
n("R06.dial","R","accepting a contradiction is not erasure","review 06"); a("R06.dial","C04","06")
n("R06.union","R","the union formula needs finite supports (omega example)","review 06"); a("R06.union","C04","06")
n("R06.kripke","R","Kripke does not call the ungrounded meaningless in every scheme","review 06"); a("R06.kripke","C04","06")

# --- file 07 v1 and corrected ---
n("C07v1","C","the selection fact between fixed points is not dependent / any content realised implies all realised","07 v1")
n("R08.indep","R","inferential independence conflated with ontological independence","review 08"); a("R08.indep","C07v1","08")
n("R08.plenum","R","nonempty fixed point, not plenum","review 08"); a("R08.plenum","C07v1","08")
n("R08.m7","R","m7 overreaches","review 08"); a("R08.m7","C07v1","08")
n("C07","C","independence theorem m1-m7 (corrected): erasure and realisation both independent of universal dependence","07 v2")

# --- file 10 v1 and corrected, file 12 ---
n("C10v1","C","Westerhoff's t1-t4 inconsistent; boundary truths; automorphism; Walker novelty","10 v1")
n("R11.incons","R","unjustified is not inconsistent","review 11"); a("R11.incons","C10v1","11")
n("R11.auto","R","the automorphism is broken by the parsimony relation","review 11"); a("R11.auto","C10v1","11")
n("R11.bound","R","invariance across sets is not a boundary truth","review 11"); a("R11.bound","C10v1","11")
n("R11.int","R","the §118 internal route and §37/§36 nuances were ignored","review 11"); a("R11.int","C10v1","11")
n("C10","C","§113 model/language gap; §89 count-predicate point","10 v2")
n("C12","C","§118 internal route yields representationalism by realist standards; parsimony step needs non-foundational grounding","12")
n("C13","C","Garfield's self-defeat charge does not discriminate his position from Taktsang's","13")
n("C14","C","no epistemic privilege claimed by Garfield (KK p.17-18); asymmetry = expertise","14")

# --- file 15 ---
n("C15","C","from 'empty' no rejection follows in Priest's logic (acts exclusive; agnosticism rule; maxim M)","15")
n("E.19.9","E","rational dilemmas are possible: one can be obliged to accept and reject","IC §19.9"); a("E.19.9","C15","19.9")
n("D15.acts","D","the retraction keeps the acts incompatible: the dilemma 'can be satisfied only by incompatible actions'","15 §3"); a("D15.acts","E.19.9","15")

# --- file 16 ---
n("C16","C","the 2003 first limit contradiction needs status (U1) identified with aboutness (U2); the authors deny it on p.6","16")
n("E.D2","E","an ultimate truth is what analysis finds; so 24.19 is ultimate (reply to the 'merely conventional' objection)","GP 2003 p.12"); a("E.D2","C16","p.12")
n("D16.status","D","D2 reasserts U2; it does not show U2 transfers convention-independent status, which p.6 denies","16 §5"); a("D16.status","E.D2","16")
n("C16b","C","Nagarjuna's ontological paradox needs 'necessary ⇒ independent'; GP p.6 (emptiness dependently arisen) is the counterexample","16")

# --- file 17 and 21: revision model, revenge ---
n("C17","C","the stable core under iterated analysis is a datum-free selector; 'no ultimate truth' oscillates; no content both stably in and out","17")
n("E.rev","E","revision theories face the strengthened liar: contradiction, or the stability predicate is inexpressible","IC §1.5"); a("E.rev","C17","1.5")
n("D21.compute","D","the contradiction horn is impossible (period ≤ 2 for every monotone Ref); the inexpressibility horn is accepted and declared by the tradition (22.11)","21"); a("D21.compute","E.rev","21")
n("E.gap","E","the stable/unstable trichotomy is just a gap theory","IC §1.5"); a("E.gap","C17","1.5")
n("D23.act","D","undec/suspension is an act-status, not a truth value; Priest's own §7.3 separates them","23 §6, 25"); a("D23.act","E.gap","23")

# --- files 18-20 textual tests ---
n("C18","C","MMK withholding idiom falls exactly on self-including status claims; 25.24 the one contestable verse","18")
n("C19","C","VV 29 and 63-64 are self-including universals fixed by 28 and 64; VV 24 denies any exemption","19")
n("C20","C","Candrakirti frames 25.24 as svabhava-negation and answers the self-referential objection by vyavahara","20")
n("L.hand","L","the textual classification was done by one hand and not independently checked","18-20 limits")
a("L.hand","C18","unmet burden"); a("L.hand","C19","unmet burden"); a("L.hand","C20","unmet burden")

# --- file 22/23: the Western catalogue ---
n("C21.sex","C","Sextus has the third idiom and it succeeds (PH I.14-15, 192-193, 206)","21,23")
n("E.p48","E","'I assert nothing' is itself an assertion: Sextus intends us to believe it; assertion = commitment to defend (Brandom)","BLT p.47-48"); a("E.p48","C21.sex","p.48")
n("D23.sex","D","the report of one's state is an appearance statement, outside Σ, by Sextus (I.193) and by Priest's own setup (p.41)","23 §1"); a("D23.sex","E.p48","23")
n("E.brandom","E","Brandom: assertion = undertaking commitment + authorizing reassertion + conditional task-responsibility when challenged (1983: 641-644); Priest glosses it as commitment to 'objective truth' (BLT p.47)","Brandom 1983 via Maroldi 2014, RIFL 2019"); a("E.brandom","D23.sex","Priest p.47")
n("D28.brandom","D","on Brandom's own structure entitlement is by default and conditional on challenge, challenger weighed equally (1994: 177-178), with non-inferential reporter authority (1994: 174, 206-208): commitment without claimed entitlement at a level is a normal deontic status, not a void act","28"); a("D28.brandom","E.brandom","28")
n("L.secondary","L","Brandom read only through two secondary articles; the 1983 text itself not obtained","28 limits"); a("L.secondary","D28.brandom","unmet burden")
n("C22.kant","C","Kant's limit claim is about the faculty (B146); the noumenon is 'problematic', so no univocal assertion","22,23")
n("E.p82","E","even 'there may be things we cannot judge' deploys the categories of plurality, possibility, negation","BLT p.82"); a("E.p82","C22.kant","p.82")
n("D23.kant","D","a problematic judgment claims no objective validity; demanding it be object-level is the univocity premise","23 §2"); a("D23.kant","E.p82","23")
n("E.modal","E","'problematic' is itself the modal category of possibility applied to noumena","BLT p.82"); a("E.modal","D23.kant","p.82")
n("D28.kant","D","Kant A74-75/B99-101: modality 'contributes nothing to the content of a judgement' and concerns only 'the value of the copula in relation to thought'; the problematic proposition 'expresses only logical possibility (which is not objective)'; A781/B809: problematic judgments 'can neither be confuted nor proved' and must not assume 'absolute validity'","28"); a("D28.kant","E.modal","28")
n("C22.rus","C","Russell's VCP is not a univocal assertion (systematic ambiguity); his route is exemption, weaker than Nagarjuna's","22,23")
n("E.p139","E","a systematically ambiguous formula is what a universal quantifier would express; 'there must be such a thought'","BLT p.139"); a("E.p139","C22.rus","p.139")
n("D23.rus","D","the schema is a stance on the hierarchy, not a content in it","23 §3"); a("D23.rus","E.p139","23")
a("E.p139","D23.rus","the same premise, restated: mutual attack")   # even cycle
n("C22.witt","C","understanding a content ≠ stably asserting it; 'unsinnig' is the wrong label","21,23")
n("E.p191","E","if the Tractatus propositions are understood they are not nonsense, hence propositions, hence sayable","BLT p.191"); a("E.p191","C22.witt","p.191")
n("D23.witt","D","everyone understands the liar; understanding gives content, not stable assertibility","23 §4"); a("D23.witt","E.p191","23"); a("E.p191","D23.witt","mutual")
n("C23","C","Priest's catalogue rests on one premise: an utterance meant to be understood is a univocal assertion with full status","23")
n("E.univ","E","the univocity premise (p.48, p.139)","BLT"); a("E.univ","C23","it is the premise C23 denies"); a("C23","E.univ","C23 denies it: mutual")

# --- files 25/26 ---
n("C25","C","the revision model is Dung's grounded semantics (A∘A = F), verified","25")
n("C26","C","the MMK framework: all theses out, all Nagarjuna claims in, exactly 18.7 and 25.24 undec; rival readings need one of three extraction decisions","26")
n("L.extract","L","the attack relation was extracted by one hand following the commentarial segmentation","26 §5"); a("L.extract","C26","unmet burden")

# --- novelty claims ---
n("C.nov","C","the revision/argumentation reading of Madhyamaka is new","17,25")
n("L.lit","L","no literature search was done (catuskoti logic, revision theory, formal Indian argumentation)","17 §8, 25 §5"); a("L.lit","C.nov","unmet burden")

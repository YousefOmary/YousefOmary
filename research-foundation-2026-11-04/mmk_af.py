# mmk_af.py  — the Mulamadhyamakakarika as an argumentation framework (file 26)
#
# NODE KINDS
#   T  opponent thesis (a svabhava-position the chapter examines)
#   V  Nagarjuna argument (prasanga) — verse range
#   O  opponent objection / defence (purvapaksa) — verse range
#   P  Nagarjuna positive claim (asserted, not derived by reductio)
#   S  status node: a claim about the STATUS of a Nagarjuna claim
#   N  self-including universal (its scope covers itself)
#   X  external layer (Vigrahavyavartani) — switchable
#
# ATTACK (src -> tgt, verses): "src refutes tgt" as the text does it.
# ONE RULE for self-attack (R*): a node of kind N attacks itself, because its
# own universal scope covers itself and denies it the status it exercises.
# Nothing else is self-attacking. Mutual exclusion between opponent theses
# is NOT encoded (it changes nothing when every thesis is attacked by an
# unattacked argument).
N = {}   # id -> (kind, label, verses)
A = []   # (src, tgt, verses)
def n(i,k,l,v): N[i]=(k,l,v)
def a(s,t,v): A.append((s,t,v))

# ---------- ch.1 conditions ----------
n("T1.arise","T","arising from self / other / both / no cause (intrinsic)","1.1")
n("V1.1","V","no thing arises from self, other, both, none","1.1,1.6,1.7"); a("V1.1","T1.arise","1.1")
n("P1.2","P","four conditions are taught, no fifth","1.2")
n("T1.svb","T","essence of things exists in the conditions","1.3")
n("V1.3","V","no essence in conditions; without own-being no other-being","1.3"); a("V1.3","T1.svb","1.3")
n("T1.act","T","activity possesses / lacks conditions (intrinsically)","1.4")
n("V1.4","V","neither activity with conditions nor without","1.4-1.5"); a("V1.4","T1.act","1.4")
n("T1.cond","T","the objective, immediate and dominant conditions exist intrinsically","1.8-1.10")
n("V1.8","V","an existent dharma has no object; nothing ceases if unborn; 'when this exists that arises' fails for the essenceless","1.8-1.10"); a("V1.8","T1.cond","1.8-1.10")
n("T1.eff","T","the effect exists in the conditions / does not and yet arises from them","1.11-1.12")
n("V1.11","V","not in them, nor from what are not its conditions; effect of conditions-nature impossible","1.11-1.14"); a("V1.11","T1.eff","1.11-1.14")

# ---------- ch.2 motion ----------
n("T2.gone","T","going is in the gone / not-yet-gone","2.1"); n("V2.1","V","no going in gone or not-gone","2.1"); a("V2.1","T2.gone","2.1")
n("O2.2","O","where there is moving there is going (going is in the being-moved)","2.2"); a("O2.2","V2.1","2.2")
n("V2.3","V","going-in-the-being-moved doubles going and goer","2.3-2.7"); a("V2.3","O2.2","2.3-2.7")
n("T2.goer","T","a goer goes (intrinsically)","2.8"); n("V2.8","V","neither goer nor non-goer goes; 'a goer goes' doubles going","2.8-2.11"); a("V2.8","T2.goer","2.8-2.11")
n("T2.begin","T","going has a beginning","2.12"); n("V2.12","V","no beginning in gone, not-gone, being-gone","2.12-2.14"); a("V2.12","T2.begin","2.12-2.14")
n("T2.stay","T","a goer stays / reverses (intrinsically)","2.15"); n("V2.15","V","as for going, so for staying and reversal","2.15-2.17"); a("V2.15","T2.stay","2.15-2.17")
n("T2.same","T","going and goer are the same / different","2.18"); n("V2.18","V","same ⇒ act=agent; different ⇒ going without goer","2.18-2.21"); a("V2.18","T2.same","2.18-2.21")
n("V2.22","V","goer does not go in any of three ways; conclusion","2.22-2.25"); a("V2.22","T2.goer","2.22-2.25")

# ---------- ch.3 senses ----------
n("P3.1","P","six faculties and their objects (exposition)","3.1")
n("T3.see","T","seeing sees (intrinsically)","3.2"); n("V3.2","V","seeing does not see itself, so cannot see another","3.2"); a("V3.2","T3.see","3.2")
n("O3.3","O","fire illuminates itself and others: so seeing sees","3.3a"); a("O3.3","V3.2","3.3")
n("V3.3","V","the fire example is refuted by gone/not-gone/going","3.3b"); a("V3.3","O3.3","3.3")
n("V3.4","V","no act of seeing when nothing is seen; seer explained likewise","3.4-3.6,3.8-3.9"); a("V3.4","T3.see","3.4-3.6")
n("P3.7","P","consciousness arises dependent on eye and form (as a child on parents)","3.7")

# ---------- ch.4 aggregates ----------
n("T4.form","T","form apart from its cause / cause apart from form","4.1-4.3")
n("V4.1","V","form without cause and cause without fruit are untenable","4.1-4.5"); a("V4.1","T4.form","4.1-4.5")
n("T4.like","T","fruit is like / unlike its cause","4.6"); n("V4.6","V","neither tenable","4.6"); a("V4.6","T4.like","4.6")
n("P4.7","P","the same holds for all aggregates","4.7")
n("M4.8","V","an objection raised by presupposing non-emptiness begs the question (sadhyasama)","4.8-4.9")

# ---------- ch.5 elements ----------
n("T5.space","T","space exists prior to its characteristic / a thing without characteristic","5.1-5.2")
n("V5.1","V","prior to characteristic it would be uncharacterised; nothing uncharacterised exists","5.1-5.2"); a("V5.1","T5.space","5.1-5.2")
n("T5.char","T","characteristics extend to the characterised / uncharacterised","5.3"); n("V5.3","V","to neither; so neither characterised nor characteristic","5.3-5.5"); a("V5.3","T5.char","5.3-5.5")
n("T5.nonthing","T","space is a thing / a non-thing","5.6"); n("V5.6","V","without a thing, no non-thing; space neither","5.6-5.7"); a("V5.6","T5.nonthing","5.6-5.7")
n("P5.8","P","those who see existence and non-existence do not see the pacification","5.8")

# ---------- ch.6 desire ----------
n("T6.prior","T","desirous one exists before desire","6.1"); n("V6.1","V","then desire would depend on him; without him no desire","6.1-6.2"); a("V6.1","T6.prior","6.1-6.2")
n("T6.co","T","desire and desirous one co-exist (as identical / as different)","6.3"); n("V6.3","V","identity excludes co-existence; difference does too","6.3-6.9"); a("V6.3","T6.co","6.3-6.9")
n("P6.10","P","like desire, all phenomena are not established as co-existent or not","6.10")

# ---------- ch.7 arising ----------
n("T7.comp","T","arising is compounded / uncompounded","7.1"); n("V7.1","V","compounded ⇒ regress of three marks; uncompounded ⇒ not a mark","7.1-7.3"); a("V7.1","T7.comp","7.1-7.3")
n("T7.arise2","T","the arising-of-arising produces the root arising","7.4"); n("V7.4","V","what is not yet born cannot give birth","7.4-7.7"); a("V7.4","T7.arise2","7.4-7.7")
n("O7.8","O","as a lamp lights itself and others, arising arises itself and others","7.8"); a("O7.8","V7.4","7.8")
n("V7.9","V","lamp does not meet darkness; if it did, darkness would darken itself","7.9-7.12"); a("V7.9","O7.8","7.9-7.12")
n("T7.born","T","the born / unborn / being-born arises","7.13"); n("V7.13","V","none arises; shown by gone/not-gone/going","7.13-7.15,7.17-7.21"); a("V7.13","T7.born","7.13-7.21")
n("P7.16","P","whatever arises dependently is pacified by nature","7.16")
n("T7.abide","T","what has abided / not abided / is abiding abides","7.22"); n("V7.22","V","none abides; all things age and die","7.22-7.25"); a("V7.22","T7.abide","7.22-7.25")
n("T7.cease","T","what has ceased / not ceased / is ceasing ceases","7.26"); n("V7.26","V","none ceases; not by itself nor another","7.26-7.32"); a("V7.26","T7.cease","7.26-7.32")
n("V7.33","V","no compounded, hence no uncompounded","7.33"); a("V7.33","T7.comp","7.33")
n("P7.34","P","arising, abiding, ceasing taught to be like dream, illusion, gandharva city","7.34")

# ---------- ch.8 agent and act ----------
n("T8.exist","T","an existent agent performs an existent act","8.1"); n("V8.1","V","the existent has no activity; act without agent","8.1-8.2"); a("V8.1","T8.exist","8.1-8.2")
n("T8.nonex","T","a non-existent agent performs a non-existent act","8.3"); n("V8.3","V","then act and agent uncaused; no cause, fruit, dharma, path","8.3-8.6"); a("V8.3","T8.nonex","8.3-8.6")
n("T8.mixed","T","agent both existent and not performs act existent and not (and mixed cases)","8.7"); n("V8.7","V","existence and non-existence contradictory in one; mixed cases fail likewise","8.7-8.11"); a("V8.7","T8.mixed","8.7-8.11")
n("P8.12","P","agent depends on act and act on agent; no other establishment is seen","8.12-8.13")

# ---------- ch.9 prior entity ----------
n("T9.prior","T","an entity exists prior to seeing, hearing, feeling","9.1-9.2")
n("V9.3","V","what makes it known before them? without them it is not evident; many selves","9.3-9.11"); a("V9.3","T9.prior","9.3-9.11")
n("V9.12","V","conceptions 'exists'/'does not exist' about what is not evident turn back (nivrtta)","9.12"); a("V9.12","T9.prior","9.12")
n("T9.nonex","T","that entity does not exist (as a thesis asserted)","9.12"); a("V9.12","T9.nonex","9.12")

# ---------- ch.10 fire and fuel ----------
n("T10.same","T","fire is fuel","10.1"); n("V10.1a","V","then agent and act are one","10.1"); a("V10.1a","T10.same","10.1")
n("T10.other","T","fire is other than fuel","10.1"); n("V10.1b","V","then fire burns without fuel, permanently, needs no kindling","10.1-10.5"); a("V10.1b","T10.other","10.1-10.5")
n("O10.6","O","as a woman connects with a man, fire though other connects with fuel","10.6"); a("O10.6","V10.1b","10.6")
n("V10.7","V","only if mutually excluding; then fire would have to connect, which was refuted","10.7"); a("V10.7","O10.6","10.7")
n("T10.dep","T","fire and fuel are established by mutual dependence (as svabhava-establishment)","10.8"); n("V10.8","V","which is established first? what is established dependently is not yet established","10.8-10.11"); a("V10.8","T10.dep","10.8-10.11")
n("V10.12","V","no fire dependent or independent of fuel; not in it, not possessing it","10.12-10.15"); a("V10.12","T10.other","10.12-10.15"); a("V10.12","T10.same","10.14")
n("P10.16","P","those who teach identity or difference of self and things are not wise","10.16")

# ---------- ch.11 before and after ----------
n("P11.1","P","the Muni said samsara has no beginning or end","11.1")
n("T11.order","T","birth before ageing-death / after / simultaneous","11.3"); n("V11.3","V","each order impossible","11.2-11.6"); a("V11.3","T11.order","11.2-11.6")
n("P11.7","P","not only samsara: cause and fruit, characteristic and basis, all lack a before-extreme","11.7-11.8")

# ---------- ch.12 suffering ----------
n("T12.self","T","suffering made by itself","12.1"); n("V12.2","V","then not dependently arisen; who would be the maker outside it?","12.2,12.4"); a("V12.2","T12.self","12.2,12.4")
n("T12.other","T","suffering made by another","12.1"); n("V12.3","V","the other would be self-made for him; no one outside suffering gives it","12.3,12.5-12.8"); a("V12.3","T12.other","12.3,12.5-12.8")
n("T12.both","T","made by both / by neither (uncaused)","12.1"); n("V12.9","V","both fails as each; uncaused fails","12.9"); a("V12.9","T12.both","12.9")
n("P12.10","P","external things too lack the four aspects","12.10")

# ---------- ch.13 samskaras ----------
n("N13.1","N","all compounded things are deceptive hence false (read as including this statement)","13.1")
a("N13.1","N13.1","R*: the statement is compounded")
n("O13.2a","O","if the deceptive is false, what is deceived? (nihilism charge)","13.2a"); a("O13.2a","N13.1","13.2a")
n("P13.1G","P","all compounded things lack svabhava (13.1 as illumination of emptiness)","13.1-13.2b")
n("O13.3","O","things have svabhava since otherwise there would be no bearer of change","13.3-13.4"); a("O13.3","P13.1G","13.3-13.4")
n("V13.5","V","nothing changes into another: youth does not age, milk is not curd","13.5-13.6"); a("V13.5","O13.3","13.5-13.6")
n("T13.7","T","emptiness exists as an entity / something non-empty exists","13.7"); n("V13.7","V","without a non-empty bit no empty bit; no non-empty exists","13.7"); a("V13.7","T13.7","13.7")
n("S.view","S","emptiness held as a view/thesis with ultimate status (sunyata-drsti, pratijna)","13.8,22.11")
n("V13.8","V","emptiness is the relinquishing of all views; who views emptiness is incurable","13.8"); a("V13.8","S.view","13.8")

# ---------- ch.14 connection ----------
n("T14.conn","T","seen, seeing, seer connect (as others)","14.1"); n("V14.1","V","no connection in pairs or all; others do not exist as others","14.1-14.4,14.8"); a("V14.1","T14.conn","14.1-14.8")
n("T14.other","T","otherness is intrinsic","14.5"); n("V14.5","V","other depends on other; without the other not other","14.5-14.7"); a("V14.5","T14.other","14.5-14.7")

# ---------- ch.15 essence ----------
n("D15","P","essence is uncontrived and independent (definition shared with the opponent)","15.2")
n("T15.made","T","essence arises from causes and conditions","15.1"); n("V15.1","V","then it would be made; a made essence is a contradiction","15.1-15.2"); a("V15.1","T15.made","15.1-15.2")
n("T15.other","T","other-being exists without essence","15.3"); n("V15.3","V","other-being is the essence of the other","15.3-15.5"); a("V15.3","T15.other","15.3-15.5")
n("P15.6","P","who sees essence/other-being/thing/non-thing does not see suchness; the Buddha negated both in the Katyayana advice","15.6-15.7")
n("T15.change","T","essence exists and things change","15.8"); n("V15.8","V","with essence nothing becomes other; without, what becomes other? (reductio of essence)","15.8-15.9"); a("V15.8","T15.change","15.8-15.9")
n("P15.10","P","'exists' is eternalism, 'does not exist' annihilationism; the wise dwell in neither","15.10-15.11")

# ---------- ch.16 bondage ----------
n("T16.samsk","T","samskaras transmigrate (permanent or impermanent)","16.1"); n("V16.1","V","permanent cannot move, impermanent cannot either","16.1"); a("V16.1","T16.samsk","16.1")
n("T16.person","T","a person transmigrates","16.2"); n("V16.2","V","not found in five ways; clinging and becoming regress","16.2-16.3"); a("V16.2","T16.person","16.2-16.3")
n("T16.nirv","T","samskaras / beings attain nirvana (intrinsically)","16.4"); n("V16.4","V","in no way feasible; bound and freed alike","16.4-16.5"); a("V16.4","T16.nirv","16.4-16.5")
n("T16.bind","T","clinging binds / binding precedes the bound / the bound is freed","16.6"); n("V16.6","V","each fails; bondage and freedom would be simultaneous","16.6-16.8"); a("V16.6","T16.bind","16.6-16.8")
n("S.nirv","S","'nirvana is mine, I am beyond' held as grasping","16.9"); n("V16.9","V","such grasping is great grasping; nirvana not superimposed, samsara not removed","16.9-16.10"); a("V16.9","S.nirv","16.9-16.10")

# ---------- ch.17 karma ----------
n("P17.1","P","actions as intention and intended; seven kinds; Dharma as seed of fruits (exposition)","17.1-17.5")
n("O17.6","O","if action lasts to ripening it is permanent; if it ceases how a fruit?","17.6"); a("O17.6","P17.1","17.6")
n("O17.7","O","seed-continuum theory: fruit from continuum, neither annihilation nor permanence","17.7-17.11"); a("O17.7","O17.6","17.7-17.11")
n("V17.12","V","that analysis entails many great errors; not valid here","17.12"); a("V17.12","O17.7","17.12")
n("O17.13","O","irrevocability (avipranasa) like a debt-contract; produces the fruit","17.13-17.20"); a("O17.13","O17.6","17.13-17.20")
n("T17.svb","T","action exists by its own nature","17.21"); n("V17.21","V","action unborn hence natureless; by nature it would be permanent, undone, ripen repeatedly","17.21-17.25"); a("V17.21","T17.svb","17.21-17.25"); a("V17.21","O17.13","17.21-17.25")
n("V17.26","V","afflictions not real, so action not real; no agent, no fruit, no consumer","17.26-17.30"); a("V17.26","T17.svb","17.26-17.30"); a("V17.26","O17.6","17.26-17.30")
n("P17.31","P","actions, agents, fruits like a magical creation, gandharva city, mirage, dream","17.31-17.33")

# ---------- ch.18 self ----------
n("T18.self","T","self is the aggregates / other than them","18.1"); n("V18.1","V","same ⇒ arising and ceasing; other ⇒ not their characteristics","18.1"); a("V18.1","T18.self","18.1")
n("P18.2","P","without self no mine; grasping ceases; birth ceases; freedom through ceasing of action and affliction; fixations stopped by emptiness","18.2-18.5")
n("P18.6","P","'self' taught, 'no-self' taught, neither taught (positive tetralemma on teaching)","18.6")
n("N18.7","N","the nameable has turned back, the mind's domain has turned back","18.7"); a("N18.7","N18.7","R*: this is a naming")
n("P18.8","P","everything real, not real, both, neither: the Buddha's teaching","18.8")
n("P18.9","P","not known through another, peaceful, unfabricated, non-conceptual, non-plural: the mark of suchness","18.9")
n("P18.10","P","the dependently arisen is neither same nor other; the teaching neither severed nor permanent","18.10-18.12")

# ---------- ch.19 time ----------
n("T19.dep","T","present and future depend on the past (intrinsically)","19.1"); n("V19.1","V","then they would exist in the past; if not there, no dependence; so not established","19.1-19.4"); a("V19.1","T19.dep","19.1-19.4")
n("T19.apart","T","time exists apart from things / as a non-dwelling thing","19.5"); n("V19.5","V","non-dwelling time not grasped; without things no time","19.5-19.6"); a("V19.5","T19.apart","19.5-19.6")

# ---------- ch.20 assemblage ----------
n("T20.in","T","fruit exists in the assemblage / does not and arises from it","20.1"); n("V20.1","V","if in it, it would be apprehended; if not, causes like non-causes","20.1-20.4"); a("V20.1","T20.in","20.1-20.4")
n("T20.cease","T","cause ceases after / before giving; fruit simultaneous / prior","20.5"); n("V20.5","V","double nature; uncaused fruit; producer=produced; cause born again","20.5-20.9"); a("V20.5","T20.cease","20.5-20.9")
n("T20.conn","T","cause connected / unconnected with fruit across times","20.10"); n("V20.10","V","no simultaneous connection in any time; connected or not, no production","20.10-20.15"); a("V20.10","T20.conn","20.10-20.15")
n("T20.empty","T","cause empty / non-empty of fruit produces it; fruit empty / non-empty","20.16"); n("V20.16","V","neither produces; non-empty unproducible, empty unproducible","20.16-20.18"); a("V20.16","T20.empty","20.16-20.18")
n("T20.same","T","cause and fruit identical / other","20.19"); n("V20.19","V","identical ⇒ producer=produced; other ⇒ cause like non-cause","20.19-20.24"); a("V20.19","T20.same","20.19-20.24")

# ---------- ch.21 arising and passing ----------
n("T21.with","T","passing without / together with arising (and conversely)","21.1"); n("V21.1","V","no death without birth, none simultaneous","21.1-21.7"); a("V21.1","T21.with","21.1-21.7")
n("T21.things","T","arising/passing of things, of the empty, of the non-empty; identical/other","21.8"); n("V21.8","V","mutually dependent, none established; neither for empty nor non-empty","21.8-21.13"); a("V21.8","T21.things","21.8-21.13")
n("T21.exist","T","things exist (so permanence/annihilation follow)","21.14"); n("V21.14","V","asserting things entails eternalism and annihilationism","21.14"); a("V21.14","T21.exist","21.14")
n("O21.15","O","no: the continuity of cause-effect avoids both extremes","21.15"); a("O21.15","V21.14","21.15")
n("V21.16","V","what has passed is not created again: the cause is annihilated; essence cannot become nothing","21.16-21.21"); a("V21.16","O21.15","21.16-21.21")

# ---------- ch.22 Tathagata ----------
n("T22.five","T","Tathagata is the aggregates / other / possesses / in them / they in him","22.1"); n("V22.1","V","none of the five; not from own-nature, not from other-nature","22.1-22.8"); a("V22.1","T22.five","22.1-22.8")
n("T22.grasp","T","what is grasped and the grasper exist from their own nature","22.9"); n("V22.9","V","neither from own nor other nature; both empty in every way","22.9-22.10"); a("V22.9","T22.grasp","22.9-22.10")
n("P22.10","P","the appropriated and the appropriator are empty in every respect","22.10")
n("V22.11","V","'empty', 'non-empty', both, neither are not to be asserted; said for designation","22.11"); a("V22.11","S.view","22.11")
n("T22.after","T","Tathagata exists / does not after nirvana; permanent etc.","22.12"); n("V22.12","V","the four do not apply to the peaceful one; inappropriate for one empty of own-nature","22.12-22.14"); a("V22.12","T22.after","22.12-22.14")
n("P22.15","P","who fixates on the Buddha beyond fixation does not see him; Tathagata and world lack own-nature","22.15-22.16")

# ---------- ch.23 error ----------
n("P23.1","P","afflictions arise from conceptuality, dependent on pleasant/unpleasant/confusion; hence without own-nature","23.1-23.2")
n("T23.whose","T","afflictions belong to a self (found in five ways)","23.3"); n("V23.3","V","self not established; afflictions not in the afflicted in five ways","23.3-23.5"); a("V23.3","T23.whose","23.3-23.5")
n("T23.pleas","T","pleasant and unpleasant exist intrinsically","23.6"); n("V23.6","V","objects like gandharva cities; pleasant depends on unpleasant and conversely","23.6-23.12"); a("V23.6","T23.pleas","23.6-23.12")
n("O23.13","O","grasping the impermanent as permanent is error; so error exists","23.13"); a("O23.13","P23.1","23.13")
n("V23.14","V","in the empty no impermanence either: so 'impermanence' would be error too; apprehensions pacified","23.14-23.16"); a("V23.14","O23.13","23.14-23.16")
n("T23.who","T","error occurs for the erring / not-yet-erring / now-erring","23.17"); n("V23.17","V","for none; unborn error, no erring one","23.17-23.20"); a("V23.17","T23.who","23.17-23.20")
n("T23.four","T","self, purity, permanence, happiness exist / do not","23.21"); n("V23.21","V","if they existed they would not be errors; if not, their opposites would not exist","23.21-23.22"); a("V23.21","T23.four","23.21-23.22")
n("P23.23","P","by stopping error ignorance stops, and the links","23.23")
n("T23.aband","T","afflictions with own-nature are abandoned / without own-nature are abandoned","23.24"); n("V23.24","V","neither can be let go of","23.24-23.25"); a("V23.24","T23.aband","23.24-23.25")

# ---------- ch.24 four truths ----------
n("P.empty","P","whatever is dependently arisen is emptiness, a dependent designation, the middle way; nothing non-empty exists","24.18-24.19")
n("O24.1","O","if all is empty there is no arising/ceasing, no four truths, no fruits, no Sangha, Dharma, Buddha; conventions destroyed","24.1-24.6"); a("O24.1","P.empty","24.1-24.6")
n("V24.7","V","you misunderstand the purpose, nature and meaning of emptiness","24.7,24.11-24.13"); a("V24.7","O24.1","24.7,24.13")
n("P24.8","P","the Dharma rests on two truths; without the conventional the ultimate is not taught","24.8-24.10")
n("V24.14","V","for whom emptiness works, everything works; you transfer your own faults","24.14-24.15"); a("V24.14","O24.1","24.14-24.15")
n("T24.svb","T","things exist by own-nature (the opponent's presupposition)","24.16")
n("V24.16","V","with own-nature: no causes, conditions, agents, arising, ceasing; no suffering, origin, cessation, path, fruits, Sangha, Buddha; nothing to be done","24.16-24.17,24.20-24.39"); a("V24.16","T24.svb","24.16-24.39"); a("V24.16","O24.1","24.20-24.39")
n("P24.40","P","who sees dependent origination sees the four truths","24.40")

# ---------- ch.25 nirvana ----------
n("O25.1","O","if all is empty, nothing arises or ceases, so no nirvana","25.1"); a("O25.1","P.empty","25.1")
n("V25.2","V","if all were non-empty the same would follow","25.2"); a("V25.2","O25.1","25.2")
n("P25.3","P","nirvana: no letting go, attainment, annihilation, permanence, ceasing, birth","25.3")
n("T25.thing","T","nirvana is a thing","25.4"); n("V25.4","V","then ageing and death, compounded, dependent","25.4-25.6"); a("V25.4","T25.thing","25.4-25.6")
n("T25.nothing","T","nirvana is a non-thing","25.7"); n("V25.7","V","no non-thing without a thing; a non-thing is dependent","25.7-25.8"); a("V25.7","T25.nothing","25.7-25.8")
n("P25.9","P","nirvana is taught as not dependent, not caused; the Teacher taught abandoning of being and non-being","25.9-25.10")
n("T25.both","T","nirvana both thing and non-thing","25.11"); n("V25.11","V","then dependent, compounded; light and dark in one","25.11-25.14"); a("V25.11","T25.both","25.11-25.14")
n("T25.neither","T","nirvana neither thing nor non-thing","25.15"); n("V25.15","V","established only if thing and non-thing are; by what is it indicated?","25.15-25.16"); a("V25.15","T25.neither","25.15-25.16")
n("T25.tath","T","the Bhagavan exists / not / both / neither after or during","25.17"); n("V25.17","V","none can be indicated","25.17-25.18"); a("V25.17","T25.tath","25.17-25.18")
n("P25.19","P","no distinction whatever between samsara and nirvana","25.19-25.20")
n("T25.views","T","views on end/no-end, permanence/impermanence of the world","25.21"); n("V25.21","V","in the emptiness of all things, what end, what permanence?","25.21-25.23"); a("V25.21","T25.views","25.21-25.23")
n("P25.24a","P","pacification of all apprehension and of fixation is peace","25.24a")
n("N25.24","N","no dharma was taught by the Buddha anywhere to anyone","25.24b"); a("N25.24","N25.24","R*: itself a taught dharma")

# ---------- ch.26 twelve links ----------
n("P26","P","the twelve links of dependent origination and their cessation (exposition)","26.1-26.12")

# ---------- ch.27 views ----------
n("T27.past","T","I existed in the past (same as now) / did not (other)","27.1,27.3,27.9"); n("V27.3","V","what was is not this; if other, arises without it, acts wasted; self neither clung-to nor other","27.3-27.13"); a("V27.3","T27.past","27.3-27.13")
n("T27.fut","T","I will / will not exist in the future","27.2,27.14"); n("V27.14","V","like the views of the past","27.14"); a("V27.14","T27.fut","27.14")
n("T27.god","T","divine and human same / different / partly","27.15"); n("V27.15","V","same ⇒ permanence; different ⇒ no continuity; partly ⇒ both extremes","27.15-27.20"); a("V27.15","T27.god","27.15-27.20")
n("T27.end","T","the world has an end / no end / both / neither","27.21"); n("V27.21","V","how would the next world arise? aggregates like a lamp; partly fails","27.21-27.28"); a("V27.21","T27.end","27.21-27.28")
n("P27.29","P","because all things are empty, about what and in whom would views arise?","27.29")
n("P27.30","P","homage to Gautama who taught the Dharma for abandoning all views","27.30")

# ---------- external layer: Vigrahavyavartani (switchable) ----------
X_N = {}; X_A = []
def xn(i,k,l,v): X_N[i]=(k,l,v)
def xa(s,t,v): X_A.append((s,t,v))
xn("O.VV1","X","if all things are empty your statement is empty and cannot negate svabhava","VV 1-4"); xa("O.VV1","P.empty","VV 1")
xn("O.VV4","X","your thesis is refuted by its own thesis-characteristic","VV 4"); xa("O.VV4","P.empty","VV 4")
xn("O.VV5","X","you negate things after apprehending them by pramanas; so pramanas and things exist","VV 5-6"); xa("O.VV5","P.empty","VV 5-6")
xn("V.VV21","X","an empty statement functions, like a magical man negating a magical man; no exemption and no inconsistency (vaisamikatva)","VV 21-28"); xa("V.VV21","O.VV1","VV 21-28")
xn("V.VV29","X","I have no thesis with the thesis-characteristic; in all empty things it is not attained","VV 29"); xa("V.VV29","O.VV4","VV 29"); xa("V.VV29","S.view","VV 29")
xn("V.VV30","X","I apprehend nothing by pramanas, so no charge; pramanas not self-established nor established by prameyas","VV 30-51"); xa("V.VV30","O.VV5","VV 30-51")
# MMK-internal pre-emption of the VV1-type objection:
xa("M4.8","O.VV1","4.8-4.9"); xa("V22.11","O.VV4","22.11")

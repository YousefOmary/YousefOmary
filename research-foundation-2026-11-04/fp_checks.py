from itertools import combinations
def powerset(U):
    U=list(U)
    for r in range(len(U)+1):
        for c in combinations(U,r): yield frozenset(c)
def T(rules,Y):
    return frozenset(x for x,S in rules if S<=Y)
def fixed_points(U,rules):
    return [Y for Y in powerset(U) if T(rules,Y)==Y]

# Reviewer §2: a<-b, b<-a
U={'a','b'}; rules=[('a',frozenset({'b'})),('b',frozenset({'a'}))]
print("two-cycle fixed points:", [sorted(Y) for Y in fixed_points(U,rules)])

# Independence theorem check on all 'total, baseless' structures with single-element supports, n=3
import itertools
U=[0,1,2]; count=0; both=0
for sup in itertools.product(U,repeat=3):           # each x supported by exactly one y
    rules=[(x,frozenset({sup[x]})) for x in U]
    if any(S==frozenset() for _,S in rules): continue
    F=fixed_points(set(U),rules); count+=1
    if frozenset() in F and frozenset(U) in F: both+=1
print("total baseless single-support structures n=3:",count,"; both ∅ and U fixed:",both)

# Beginningless chain on finite prefix of N with wraparound-free truncation can't be enumerated; show ω example instead
# Universe N∪{ω} truncated at 6, Est(0,∅), Est(n+1,{n}), Est(ω, {0..5}); iterate T from ∅
N=list(range(6)); rules=[(0,frozenset())]+[(n+1,frozenset({n})) for n in range(5)]+[('w',frozenset(N))]
Y=frozenset(); stages=[]
while True:
    Z=T(rules,Y); stages.append(sorted(map(str,Z)))
    if Z==Y: break
    Y=Z
print("stages to least fixed point:",len(stages)-1, "; final:",stages[-1])

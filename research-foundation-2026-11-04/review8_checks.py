from itertools import combinations, product
from collections import Counter
def powerset(U):
    U=list(U)
    for r in range(len(U)+1):
        for c in combinations(U,r): yield frozenset(c)
def T(rules,Y): return frozenset(x for x,S in rules if S<=Y)
def fps(U,rules): return [Y for Y in powerset(U) if T(rules,Y)==Y]

# §3: two-cycle + datum a∈D
rules=[('a',frozenset('b')),('b',frozenset('a'))]
F=fps({'a','b'},rules); print("two-cycle FPs containing a:", [sorted(Y) for Y in F if 'a' in Y])
# p example
rules=[('a',frozenset('bp')),('b',frozenset('ap')),('p',frozenset('ab'))]
print("p-example FPs:", [sorted(Y) for Y in fps(set('abp'),rules)])
# §4: five nodes, 2-cycle + 3-cycle
rules=[('a',frozenset('b')),('b',frozenset('a')),('c',frozenset('d')),('d',frozenset('e')),('e',frozenset('c'))]
print("5-node FPs:", [sorted(Y) for Y in fps(set('abcde'),rules)])
# §7: table of fixed-point counts over 27 structures
U=[0,1,2]; cnt=Counter()
for f in product(U,repeat=3):
    cnt[len(fps(set(U),[(x,frozenset({f[x]})) for x in U]))]+=1
print("FP-count table:", dict(sorted(cnt.items())))

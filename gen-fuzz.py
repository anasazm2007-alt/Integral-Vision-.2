"""Generates random polynomial cases with reference values from SymPy/mpmath (independent of the JS engine).
Usage: python3 tests/gen-fuzz.py   (needs sympy, mpmath)"""
import random, json, sympy as sp, mpmath as mp
mp.mp.dps=30; x=sp.symbols('x'); random.seed(2026); cases=[]
def poly():
    d=random.randint(1,3); return sum(random.randint(-3,3)*x**i for i in range(d+1))
def rts(p,a,b):
    p=sp.Poly(p,x)
    if p.is_zero or p.degree()<1: return []
    return [float(r.evalf(30)) for r in sp.real_roots(p) if a<float(r.evalf(30))<b]
while len(cases)<30:
    f,g=poly(),poly(); a=random.choice([-2,-1,0,0.5]); b=a+random.choice([1,1.5,2,3])
    if sp.expand(f-g)==0: continue
    F=sp.lambdify(x,f,'mpmath'); G=sp.lambdify(x,g,'mpmath')
    br=sorted(set([a,b]+rts(f-g,a,b)+rts(f,a,b)+rts(g,a,b)+rts(f+g,a,b)))
    area=sum(mp.quad(lambda t:abs(F(t)-G(t)),[lo,hi]) for lo,hi in zip(br,br[1:]))
    def RR(t):
        u,v=F(t),G(t); hi,lo=max(u,v),min(u,v)
        if lo>=0: return hi,lo
        if hi<=0: return -lo,-hi
        return max(hi,-lo),0
    vol=sum(mp.quad(lambda t:mp.pi*(RR(t)[0]**2-RR(t)[1]**2),[lo,hi]) for lo,hi in zip(br,br[1:]))
    co=lambda p:[float(c) for c in reversed(sp.Poly(p,x).all_coeffs())]
    cases.append(dict(f=co(f),g=co(g),a=a,b=b,area=float(area),volx=float(vol),ftxt=str(f),gtxt=str(g)))
json.dump(cases,open('tests/fuzz-cases.json','w'),indent=1); print(len(cases),'cases written')

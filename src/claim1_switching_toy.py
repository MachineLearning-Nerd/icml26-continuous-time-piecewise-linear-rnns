"""One-dimensional cPLRNN: dz/dt=-z+relu(z-1)-1, exact per-region switching."""
import json, math
# z0=2: for z>1, z'= -2 -> hits 1 at .5; then z'=-z-1 => z=2e^{-(t-.5)}-1
def exact(t): return 2-2*t if t<=.5 else 2*math.exp(-(t-.5))-1
def euler(t, h=1e-5):
 z=2.; n=round(t/h)
 for _ in range(n): z+=h*(-z+max(z-1,0)-1)
 return z
if __name__=='__main__':
 ts=[0,.25,.5,.75,1.]; rows=[{'t':t,'exact':exact(t),'euler':euler(t),'abs_error':abs(exact(t)-euler(t))} for t in ts]
 out={'method':'source-inspired 1D regionwise analytic switching fixture','switch_time':.5,'rows':rows,'verdict':'toy','scope':'Exact scalar piecewise-linear ODE trajectory and switching time; not a trained cPLRNN or benchmark reproduction.'}
 open('outputs/claim1_switching_toy/summary.json','w').write(json.dumps(out,indent=2)+'\n')

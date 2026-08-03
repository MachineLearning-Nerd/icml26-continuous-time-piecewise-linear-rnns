"""Finite 1-D SCYFI-style regional fixed-point toy; not trained cPLRNN evidence."""
import json, hashlib
from pathlib import Path
OUT=Path('outputs/claim2_scyfi_fixedpoint_toy')
def main():
    # dx/dt = A*x + W*ReLU(x) + h, with A=-2, W=1, h=-1.
    # For each activation region s, solve (A+W*s)x+h=0 then validate s.
    A,W,h=-2.0,1.0,-1.0
    rows=[]
    for s in (0,1):
        x=-h/(A+W*s)
        valid=(x<=0) if s==0 else (x>=0)
        residual=(A+W*s)*x+h
        rows.append({'region_active':s,'virtual_fixed_point':x,'region_valid':valid,'residual':residual})
    valid=[r for r in rows if r['region_valid']]
    payload={'method':'regional virtual-fixed-point search','system':{'A':A,'W':W,'h':h},'candidates':rows,'valid_fixed_points':valid,'verdict':'toy','scope':'1-D regional fixed-point search only; no trained cPLRNN, limit-cycle, or trajectory-tracking reproduction.'}
    OUT.mkdir(parents=True,exist_ok=True); (OUT/'summary.json').write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    (OUT/'PROTOCOL.md').write_text('Pre-specified deterministic 1-D regional linear solve; enumerate both ReLU regions and validate membership/residual.\n')
    (OUT/'SHA256SUMS').write_text(''.join(f'{hashlib.sha256((OUT/n).read_bytes()).hexdigest()}  {n}\n' for n in ['PROTOCOL.md','summary.json']))
if __name__=='__main__': main()

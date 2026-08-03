import json, subprocess, sys
subprocess.run([sys.executable,'src/claim2_scyfi_fixedpoint_toy.py'],check=True)
d=json.load(open('outputs/claim2_scyfi_fixedpoint_toy/summary.json'))
assert len(d['valid_fixed_points'])==1
assert d['valid_fixed_points'][0]['virtual_fixed_point']==-0.5
assert d['valid_fixed_points'][0]['residual']==0

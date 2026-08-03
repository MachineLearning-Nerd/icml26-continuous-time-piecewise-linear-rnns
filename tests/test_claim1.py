import sys; sys.path.insert(0,'.')
from src.claim1_switching_toy import exact
assert abs(exact(.5)-1)<1e-12
assert abs(exact(1)-(2*__import__('math').exp(-.5)-1))<1e-12

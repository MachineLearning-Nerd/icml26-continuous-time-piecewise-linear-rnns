# Scoped reproduction report

Date: 2026-08-17

## Result

This repository is a published, source-pinned audit of the ICML 2026 paper “Continuous-Time Piecewise-Linear Recurrent Neural Networks.” Its overall verdict is:

INCONCLUSIVE_SCOPED_TO_SOURCE_AND_BOUNDED_TOY

The source identity and claim-production paths are documented. Claim 1 has a scalar switching fixture, Claim 2 has a scalar regional fixed-point fixture, and Claims 3–5 remain unverified because the implementation, datasets, checkpoints, logs, and metric calculations required for end-to-end reproduction are absent.

## Claim matrix

| Claim | Local result | Evidence boundary |
| --- | --- | --- |
| C1: regional analytic ODE solution and switching | TOY_SOURCE_SWITCHING | One-dimensional structural fixture only; no matrix/root-finder/training stack |
| C2: regional equilibria and limit cycles | TOY_SOURCE_REGIONAL_FIXED_POINT | One-dimensional fixed-point enumeration only; no trained model or limit-cycle solve |
| C3: irregular LIF attractor reconstruction | UNVERIFIED | Source table only; no data, model, checkpoint, trajectory, or metric output |
| C4: cPLRNN runtime advantage | UNVERIFIED | Source timing table only; no local training or timing logs |
| C5: cortical recording result | UNVERIFIED | Source table only; no recording, embedding, model, or metric output |

## Bounded local results

Claim 1:

~~~text
system: dz/dt = -z + ReLU(z-1) - 1
initial state: z(0) = 2
regional switch: t = 0.5
~~~

Claim 2:

~~~text
system: dx/dt = -2x + ReLU(x) - 1
valid fixed point: x = -0.5 in the inactive region
rejected virtual candidate: x = -1 in the active region
~~~

These are finite structural checks, not paper-scale training or benchmark results.

## Limitations and handoff

- The source archive contains no official experiment repository or training implementation.
- The paper’s benchmark claims require model training, multiple seeds, raw trajectories, timing logs, and metric calculations that are not locally available.
- The next audit should begin with a different ICML repository; this repository’s next action is recorded in AUTONOMOUS_STATE.json.

# Status

- Repository: MachineLearning-Nerd/icml26-continuous-time-piecewise-linear-rnns
- Former name: icml26-repro-JuaulCZ7gE-continuous-time-piecewise-linear-rnns
- OpenReview ID: JuaulCZ7gE
- Paper: Continuous-Time Piecewise-Linear Recurrent Neural Networks
- Claims / maximum points: 5 / 10
- Source: arXiv 2602.15649v1, SHA-256 pinned in evidence/source/SHA256SUMS.
- Phase: published_and_verified
- Overall verdict: INCONCLUSIVE_SCOPED_TO_SOURCE_AND_BOUNDED_TOY
- Publication of benchmark claims: false
- Compute: local CPU/local GTX 1050 only; no paid, remote, upgraded, or HF compute.
- Branches: main only
- Claim C1: TOY_SOURCE_SWITCHING
- Claim C2: TOY_SOURCE_REGIONAL_FIXED_POINT
- Claim C3: UNVERIFIED
- Claim C4: UNVERIFIED
- Claim C5: UNVERIFIED
- Next action: select the next ICML repository for a scoped source-and-claim audit.

## Evidence boundary

The pinned source is arXiv 2602.15649v1. The source archive contains the paper, figures, bibliography, and LaTeX/style files, but no cPLRNN training implementation, datasets, checkpoints, benchmark logs, or metric pipeline. The two local programs therefore validate only small structural fixtures:

- Claim 1: a one-dimensional piecewise-linear ODE with an exact regional switch at t=0.5 and a small-step Euler comparison.
- Claim 2: a one-dimensional regional virtual-fixed-point enumeration with one valid fixed point and one rejected candidate.

Claims 3–5 remain paper-source documentation only. No benchmark number is represented as independently reproduced.

## Completed checkpoints

- Pinned arXiv 2602.15649v1 PDF and source archive with checksums.
- Documented the cPLRNN analytic solution, switching-time, implicit-gradient, SCYFI, and limit-cycle production paths.
- Executed and recorded the Claim 1 scalar switching toy.
- Executed and recorded the Claim 2 scalar regional fixed-point toy.
- Normalized the repository identity and branch inventory.
- Published the standardized dossier, evidence manifest, and final verifier.

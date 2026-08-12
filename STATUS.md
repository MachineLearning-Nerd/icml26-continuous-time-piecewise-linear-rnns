# Status
- OpenReview ID: `JuaulCZ7gE`
- Paper: *Continuous-Time Piecewise-Linear Recurrent Neural Networks*
- Live contract: 5 claims / 10 points, pinned from `outputs/live/20260803T103038Z` using anchored precedence.
- Source: arXiv 2602.15649v1 archive/PDF pinned in `evidence/source/SHA256SUMS`.
- Compute: local CPU/local GTX 1050 only; no HF/paid/remote compute.
- Claim 1: **toy** — source-inspired 1-D regionwise analytic switching-time fixture. It is not trained cPLRNN, LIF, neuronal, or Neural-ODE benchmark evidence.
- Claim 2: **toy** — deterministic 1-D regional virtual-fixed-point enumeration (SCYFI-style). One valid fixed point is found by solving and region-validating both ReLU regions. It is not trained cPLRNN, limit-cycle, or Eq. 14–16 trajectory-tracking evidence. Evidence: `outputs/claim2_scyfi_fixedpoint_toy/`.
- Claims 3–5: **unverified** — paper tables are pinned, but no benchmark data, implementation, checkpoint, training log, generated trace, or independent metric calculation is present.
- Next: independently review the two toys against the pinned source, then assess whether a full cPLRNN reproduction is feasible under the local-only compute policy.

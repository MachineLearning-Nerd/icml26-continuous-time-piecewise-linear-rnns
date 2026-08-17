# Claim-to-evidence audit

This dossier separates the paper’s production paths from the evidence actually present in this repository. The live five-claim contract is preserved in contract/live_claims.json.

## Paper production path

The paper’s method and evaluation path is:

1. Define a continuous-time PLRNN with ReLU-selected coordinates and partition the latent state space into up to 2^P linear regions.
2. Solve the regional linear ODE with a matrix exponential and locate the first boundary crossing with interval root finding.
3. Differentiate switching times through the implicit-function formula while training with sparse teacher forcing and an MSE readout.
4. Analyze trained equilibria by solving the regional fixed-point equation and validating region membership; analyze limit cycles by solving boundary-crossing and return constraints with a trust-region/variable-projection procedure.
5. Train cPLRNN, standard PLRNN, and Neural ODE baselines on Lorenz-63, regular and irregular LIF data, and cortical membrane-potential recordings; calculate attractor geometry, spectral, and short-term prediction metrics.

## C1 — Regional analytic solution and switching

Contract text: “The continuous-time PLRNN formulation (Equation 5, Section 3.1) solves the piecewise-linear ODE analytically within each of the 2^P linear subregions by tracking switching times between regions, bypassing numerical integration entirely (Section 3.1, Equation 5).”

Paper production path:

- The cPLRNN vector field and regional matrix are defined in main.tex lines 193–198.
- The regional matrix-exponential solution and one-coordinate sum-of-exponentials form are given in lines 200–216.
- The first ReLU zero crossing defines the switching time in lines 218–223.
- The paper’s interval root finder, custom first-root search, implicit switching-time derivative, and state-computation algorithm are described in lines 225–286.

Local evidence:

- src/claim1_switching_toy.py solves dz/dt = -z + ReLU(z-1) - 1 from z(0)=2.
- outputs/claim1_switching_toy/summary.json records the exact scalar switch at t=0.5, regional trajectory values, and a small-step Euler comparison.
- The toy reaches a finite structural check only; it does not implement matrix eigen-decomposition, interval arithmetic, first-root branch-and-prune, automatic differentiation, sparse teacher forcing, or cPLRNN training.

Status: TOY_SOURCE_SWITCHING.

## C2 — Equilibria and limit cycles

Contract text: “Equilibria and limit cycles of trained cPLRNNs are determined semi-analytically per region using a SCYFI-style fixed-point search and the trajectory-tracking equations 14-16 (Section 3.2).”

Paper production path:

- The trained-model state-space analysis begins in main.tex lines 294–297.
- Regional equilibria solve z* = -W_region^-1 h and are validated as real or virtual fixed points in lines 298–308.
- Limit cycles are represented by a sequence of regions, boundary-crossing times, and a return condition in lines 310–328.
- The paper solves the resulting system with a trust-region solver and variable projection in lines 330–330.

Local evidence:

- src/claim2_scyfi_fixedpoint_toy.py enumerates both ReLU regions for dx/dt = -2x + ReLU(x) - 1.
- outputs/claim2_scyfi_fixedpoint_toy/summary.json records the valid fixed point x=-0.5 in the inactive region and the rejected virtual candidate x=-1 from the active region.
- outputs/claim2_scyfi_fixedpoint_toy/PROTOCOL.md and its checksum preserve the deterministic setup.

Status: TOY_SOURCE_REGIONAL_FIXED_POINT.

The toy does not use a trained cPLRNN, solve a limit cycle, solve the paper’s multi-region trajectory constraints, or evaluate stability/topology on a learned model.

## C3 — Irregular LIF attractor reconstruction

Contract text: “On irregularly-sampled leaky integrate-and-fire (LIF) data, the standard discrete-time PLRNN fails badly with D_stsp=4.3±0.3, while the cPLRNN reconstructs the attractor accurately with D_stsp=0.26±0.03 (Table 3).”

Paper production path:

- The LIF regular/irregular benchmark and its sampling treatment are described in main.tex lines 461–472.
- Table 3 reports the geometry, spectral, and MAE comparison in lines 474–493; the irregular values include cPLRNN D_stsp=0.26±0.03 and standard PLRNN D_stsp=4.3±0.3.
- The source defines D_stsp and D_H in the evaluation-metrics appendix.

Local evidence:

- The benchmark protocol and reported table are pinned in the source PDF/archive.
- No LIF data, implementation, model checkpoint, generated trajectory, repeated-run log, or independent metric calculation is present.

Status: UNVERIFIED.

## C4 — Training speed versus Neural ODE baselines

Contract text: “cPLRNN trains roughly 4-5x faster than Neural ODE baselines using RK4 or Tsit5 solvers while matching their reconstruction performance (Table 2).”

Paper production path:

- The paper compares cPLRNN, standard PLRNN, and Neural ODE solvers on Lorenz-63 in main.tex lines 341–403.
- The runtime table and 10-run timing protocol are in lines 407–449.
- Reconstruction quality is assessed with D_stsp, D_H, and short-term error.

Local evidence:

- The source table and hyperparameters are pinned.
- No local cPLRNN implementation, Neural ODE baseline, training run, timing trace, or matched-quality metric output is present.

Status: UNVERIFIED.

## C5 — Cortical membrane-potential recordings

Contract text: “On real neuronal recordings, cPLRNN attains D_stsp=0.71±0.02, slightly outperforming Neural ODE competitors on the same benchmark (Table 4).”

Paper production path:

- The membrane-potential benchmark and cPLRNN delay embedding are described in main.tex lines 521–524 and 1010–1019.
- Table 4 reports cPLRNN D_stsp=0.71±0.02 alongside Neural ODE and standard PLRNN baselines in lines 498–517.
- The evaluation appendix defines the geometry and spectral metrics in lines 1024–1060.

Local evidence:

- The protocol, table, and metric definitions are source-pinned.
- The recording, delay-embedding pipeline, trained models, identified cycle/fixed point, and independent metric outputs are absent.

Status: UNVERIFIED.

## Evidence vocabulary

- TOY_SOURCE_SWITCHING and TOY_SOURCE_REGIONAL_FIXED_POINT mean bounded finite structural fixtures were executed and checked.
- UNVERIFIED means the paper claim is documented but the required independent data/model/protocol evidence is absent.
- REPRODUCED is intentionally not used for any contracted claim.

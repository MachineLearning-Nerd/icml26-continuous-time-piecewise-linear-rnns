# Continuous-Time PLRNNs: Source-Pinned ICML 2026 Reproduction Audit

Repository identity: MachineLearning-Nerd/icml26-continuous-time-piecewise-linear-rnns. The former repository name was icml26-repro-JuaulCZ7gE-continuous-time-piecewise-linear-rnns.

This repository is a claim-by-claim audit of **“Continuous-Time Piecewise-Linear Recurrent Neural Networks.”** It pins the paper’s arXiv `v1` PDF/source, explains how the cPLRNN method and benchmark claims are produced, and records two bounded one-dimensional toys. The local toys are deliberately labeled as toys: this repository does not contain the paper’s trained cPLRNN implementation, datasets, checkpoints, benchmark logs, or a full end-to-end reproduction.

> **Current status:** published source-pinned audit with verdict **INCONCLUSIVE_SCOPED_TO_SOURCE_AND_BOUNDED_TOY**. Claim 1 has a **source-inspired scalar switching toy**. Claim 2 has a **deterministic scalar regional fixed-point toy**. Claims 3–5 and the paper’s trained-model results remain **unverified locally**.

## Paper and resources

- Paper: [arXiv:2602.15649](https://arxiv.org/abs/2602.15649)
- OpenReview: [JuaulCZ7gE](https://openreview.net/forum?id=JuaulCZ7gE)
- Pinned paper PDF: `evidence/source/arxiv-2602.15649.pdf`
- Pinned paper source: `evidence/source/arxiv-2602.15649-source.tar.gz`
- Contracted claims: `contract/live_claims.json`

The local PDF is explicitly marked **arXiv:2602.15649v1, 17 February 2026**. The canonical arXiv record later lists a revised `v2`; this repository keeps the original pinned artifacts and does not silently replace them. The source archive contains `main.tex`, bibliography/style files, and figures, but no training code or benchmark dataset.

The paper’s authors are Alena Brändle, Lukas Eisenmann, Florian Götz, and Daniel Durstewitz.

## What the paper does

The paper addresses dynamical-systems reconstruction from regularly or irregularly sampled time series. Its claim-production path is:

1. Define a continuous-time piecewise-linear recurrent neural network (cPLRNN) with
   `dz/dt = A z + W Phi*(z) + h`, where `Phi*` applies ReLU to selected coordinates. ReLU sign patterns divide the state space into up to `2^P` linear regions.
2. Within one region, rewrite the vector field as `dz/dt = W_region z + h` and solve it analytically with a matrix exponential. The solution is valid until a ReLU coordinate crosses zero.
3. Find the earliest boundary crossing using interval/root-bracketing logic for the sum-of-exponentials coordinate solutions. Restart the regional solution after each switch, and differentiate switching times through the implicit-function formula when training `A`, `W`, and `h`.
4. Train cPLRNNs with sparse teacher forcing and an MSE readout loss. The paper compares cPLRNNs with discrete-time PLRNNs and ReLU Neural ODEs using Euler, RK4, and Tsit5 solvers.
5. Analyze equilibria by solving `z*_region = -W_region^-1 h` in each region and validating whether the candidate lies in that region. Candidates outside their region are virtual fixed points; the paper adapts SCYFI-style search to reduce the regional search cost.
6. Analyze limit cycles by specifying a sequence of visited regions, solving the boundary-crossing and return constraints, and using a trust-region solver with variable projection.
7. Evaluate reconstruction on Lorenz-63, regular and irregular leaky-integrate-and-fire (LIF) data, and cortical membrane-potential recordings. The reported metrics include attractor geometry `D_stsp`, spectral Hellinger distance `D_H`, and short-term MAE.

## Repository status

| Area | Current state |
| --- | --- |
| Compute | Local CPU / local GTX 1050 only |
| Primary source | arXiv `2602.15649v1`, SHA-256 pinned |
| Claim 1 | Scalar exact regional solution and Euler comparison toy; not a trained cPLRNN or benchmark run |
| Claim 2 | Scalar regional virtual-fixed-point toy; no trained equilibria, limit cycles, or trajectory tracking |
| Claims 3–5 | Unverified locally |
| cPLRNN training implementation | Not present |
| Datasets/checkpoints/training logs | Not present |
| Benchmark reproduction | Not performed |
| Publication of benchmark results | Not allowed without model, data, protocol, logs, and independently checked metrics |

## Contents

| Path | Purpose |
| --- | --- |
| `contract/live_claims.json` | Five paper claims and verification labels |
| `evidence/source/` | Pinned arXiv PDF/source archive and checksums |
| `src/claim1_switching_toy.py` | One-dimensional piecewise-linear switching fixture |
| `outputs/claim1_switching_toy/summary.json` | Exact scalar trajectory, switch time, Euler comparison, and scope |
| `src/claim2_scyfi_fixedpoint_toy.py` | One-dimensional regional fixed-point enumeration |
| `outputs/claim2_scyfi_fixedpoint_toy/` | Protocol, result summary, and checksums |
| `logbook/claim-2.md` | Claim 2 evidence boundary |
| `tests/` | Small executable checks for the two toys |
| `STATUS.md` | Human-readable phase and next actions |
| `AUTONOMOUS_STATE.json` | Machine-readable evidence boundary and run state |

## Branch inventory

| Branch | Role | State |
| --- | --- | --- |
| `main` | Published source-pinned audit, documentation, and bounded local toys | Current default branch |

Only `main` is present. There are no experiment, legacy, or claim-specific branches carrying separate work.

## Claim-to-evidence ledger

The authoritative claim text is preserved in `contract/live_claims.json`. The table below distinguishes the paper’s production path from what this repository actually checks.

| Claim | How the paper produces it | Evidence in this repository | Status |
| --- | --- | --- | --- |
| 1. cPLRNNs solve each of the `2^P` piecewise-linear ODE regions analytically and determine switching times without numerical integration. | Use the region matrix exponential, find the first ReLU zero crossing with interval root finding, restart in the next region, and differentiate the implicit switch-time equation during training. | `src/claim1_switching_toy.py` solves `dz/dt=-z+ReLU(z-1)-1` from `z(0)=2`, obtains a switch at `t=0.5`, evaluates the post-switch exponential, and compares against small-step Euler. It is source-inspired and scalar; it does not implement the paper’s matrix/eigenvalue/root-finder/training stack. | **Toy only / unverified paper method** |
| 2. Equilibria and limit cycles of trained cPLRNNs can be found semi-analytically with regional fixed-point search and trajectory constraints. | Solve `z*=-W_region^-1h` per region and validate membership; for cycles, solve region-boundary crossing and return equations with a trust-region/variable-projection procedure. | `src/claim2_scyfi_fixedpoint_toy.py` enumerates both ReLU regions for `dx/dt=-2x+ReLU(x)-1`, finds the valid fixed point `x=-0.5`, and rejects the virtual candidate `x=-1` from the active region. It does not train a cPLRNN or solve a limit cycle. | **Toy only / unverified paper method** |
| 3. On irregularly sampled LIF data, cPLRNN reconstructs the attractor much better than the standard discrete-time PLRNN (`D_stsp=0.26±0.03` versus `4.3±0.3`). | Train cPLRNN and discrete PLRNN models on the specified LIF data, generate free trajectories, and compute attractor geometry, spectral, and MAE metrics over repeated runs. | The table and benchmark protocol are in the pinned source. No LIF data, model implementation, checkpoint, generated trace, or metric calculation is present locally. | **Unverified** |
| 4. cPLRNN trains roughly 4–5× faster than Neural ODE baselines while matching reconstruction quality. | Repeat the benchmark training with cPLRNN and ReLU Neural ODEs using Euler/RK4/Tsit5, then compare runtime and `D_stsp`, `D_H`, and MAE. | The paper’s hyperparameters and reported comparisons are pinned in `main.tex`; no local training runtime or metric logs exist. | **Unverified** |
| 5. On cortical membrane-potential recordings, cPLRNN slightly outperforms Neural ODE competitors and obtains `D_stsp=0.71±0.02`. | Delay-embed the recording, train the models, identify the cPLRNN limit cycle/fixed point, and evaluate long-term geometry, spectrum, and short-term prediction. | The source archive contains the paper’s protocol and table. No recording, delay-embedding pipeline, trained model, cycle solve, or independent metric output is present. | **Unverified** |

### Toy evidence boundary

The two local programs preserve only small structural components of Claims 1 and 2. They do not establish the paper’s performance, training speed, irregular-time handling, attractor statistics, topological analysis of trained models, or comparison tables. A paper-reported number remains paper-reported until the required data, model, protocol, logs, and metric calculation are independently available.

## Final verification

Run python3 verify_final.py from the repository root. The verifier checks the canonical repository URL, the single main branch, MachineLearning-Nerd attribution on reachable commits, source/output hashes, toy summaries, claim-status alignment, and the tracked evidence manifest.

## Reproduce the current local evidence

From the repository root:

~~~bash
python3 src/claim1_switching_toy.py
python3 src/claim2_scyfi_fixedpoint_toy.py
python3 tests/test_claim1.py
python3 tests/test_claim2.py
python3 -m pytest -q tests/test_claim1.py tests/test_claim2.py
(cd evidence/source && sha256sum -c SHA256SUMS)
sha256sum -c outputs/claim1_switching_toy/SHA256SUMS
(cd outputs/claim2_scyfi_fixedpoint_toy && sha256sum -c SHA256SUMS)
~~~

The toys use only the Python standard library. If `pytest` is unavailable, the direct Python checks still exercise the recorded evidence.

## Reproduction policy

- A paper-reported benchmark table is not an independently reproduced result.
- A **toy** is evidence only for its finite equations, inputs, output, and declared boundary.
- A claim becomes **reproduced** only when the required model, data, training/simulation procedure, logs, and metric calculation are available and independently checked.
- Resource limits are part of this record: local CPU/local GTX 1050 only; no paid, remote, or upgraded cloud compute.
- The pinned source is preserved by checksum. Later arXiv revisions should be evaluated as new source versions rather than silently substituted.

## Citation

~~~bibtex
@misc{brandle2026continuous,
  title         = {Continuous-Time Piecewise-Linear Recurrent Neural Networks},
  author        = {Alena Brändle and Lukas Eisenmann and Florian Götz and Daniel Durstewitz},
  year          = {2026},
  eprint        = {2602.15649},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url           = {https://arxiv.org/abs/2602.15649}
}
~~~

## Thank you

Thank you to Alena Brändle, Lukas Eisenmann, Florian Götz, and Daniel Durstewitz for developing a tractable continuous-time extension of PLRNNs, exposing the switching-time and topological-analysis procedures, and documenting the benchmark protocols. This audit is intended to credit the original work while making the distinction between paper-reported results, pinned source artifacts, bounded local toys, and true end-to-end reproduction explicit.

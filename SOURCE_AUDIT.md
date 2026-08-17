# Source audit

## Canonical primary source

- Paper: Continuous-Time Piecewise-Linear Recurrent Neural Networks
- Authors: Alena Brändle, Lukas Eisenmann, Florian Götz, Daniel Durstewitz
- arXiv: 2602.15649v1
- OpenReview: JuaulCZ7gE
- PDF: evidence/source/arxiv-2602.15649.pdf
- PDF SHA-256: c30f6f0fbd3eabde8d3124c4965b7d89cb4c20445bc3f671e2e9955f5cb0624c
- Source archive: evidence/source/arxiv-2602.15649-source.tar.gz
- Source archive SHA-256: 4143727b13cd80fe632e96e9ab432f1d344221589cd834b8aa0316252ff58acd

The archive has 15 members: 14 regular files and one Graphics directory. It contains no executable regular files. The archive’s 00README.json identifies the source package metadata. The checksum file uses archive-relative paths for the two canonical source artifacts.

## Source member hashes

| Member | SHA-256 |
| --- | --- |
| 00README.json | d1f6b1a71c9accb812ec5121d1fff7910c025ca7bb201948bacdb40941bc14e5 |
| Graphics/BoundarySwitchFunctionSwitch.pdf | 89afed25e7cde6a503856bb561b9e206762df4cd334c3656d79fc331f4e71345 |
| Graphics/Experimental_results_one_col.png | 0178f8b7df2eea051b1e4404ab002d421dfd14019da08c999194a24537ff5c58 |
| Graphics/bracketing_plot.png | aa54f8a228135d7cd08ddf749f90018c9cffb46610aa37431aff20ae08bfbe1e |
| Graphics/lorenz_three_models_comparison.png | f805e3193505de89b7628e76e183b53807692e9892efae0221ea8e1dd47b767a |
| algorithm.sty | 93fd0eb31c112eb405833db8f1d7f5d238c7e691b1c05680d7276e68f36d564a |
| algorithmic.sty | 48d18794a5d97c0479a588cc2eac0917992feb9da83acc4631b8f55757d80f9b |
| bibliography.bib | bbc6826105d37fa6a4d1215e29d762b0d8b039f24e89ec925af5ae2c3b5eba93 |
| fancyhdr.sty | 9130c52f91087abc6d223164ffa587e207e3257fcbcd069ef09ecb5391043f14 |
| icml2026.bst | 0ec3d5eb9b02efb7e0b44a32f3775882f42a743d0bdc618f34e6936309b98764 |
| icml2026.sty | 7cdcf90f6a59c5219e7f15c88f7ed09fcaf598dad91e6cdddc4dc3cb0e397a95 |
| main.tex | ebe9bfa9f19c0624a49979bbed04932cd0af51f30e258fb58914a5453f3428e3 |
| math_commands.tex | 7235e21e953613f9ff4f3390d4bec31941b9e5166e741406692677bebdcf843c |
| natbib.sty | 99c5c22e84256b8a19af9e88995c488b1846745c0f1a9303cec48404bb58aa13 |

## Source anchors

- Motivation, contribution, and continuous-time cPLRNN context: main.tex lines 121–135 and 193–198.
- Regional analytic solution: lines 200–216.
- Switching-time definition and first-root requirement: lines 218–230.
- Implicit switching-time derivative and state algorithm: lines 232–286.
- Regional fixed points and SCYFI-style search: lines 294–308.
- Limit-cycle region sequence and trajectory constraints: lines 310–330.
- Benchmark design and runtime comparison: lines 341–449.
- Irregular LIF results: lines 461–493.
- Membrane-potential results: lines 498–524.
- Benchmark systems, delay embedding, and metric definitions: lines 984–1060.

The source archive is paper evidence, not an official implementation artifact. It contains no training code, dataset, checkpoint, raw log, or metric-output bundle.

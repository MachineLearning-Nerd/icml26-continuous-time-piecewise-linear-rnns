# Environment and reproduction policy

## Local policy

- Allowed compute: local CPU and local GTX 1050.
- Disallowed for this audit: paid compute, remote compute, upgraded Hugging Face CPU, Hugging Face Jobs, and other external execution.
- The two bounded toys use only the Python standard library.
- No official cPLRNN training implementation or benchmark data is present in the repository.

## Lightweight checks

From the repository root:

~~~bash
python3 verify_final.py
python3 src/claim1_switching_toy.py
python3 src/claim2_scyfi_fixedpoint_toy.py
python3 tests/test_claim1.py
python3 tests/test_claim2.py
python3 -m pytest -q tests/test_claim1.py tests/test_claim2.py
(cd evidence/source && sha256sum -c SHA256SUMS)
sha256sum -c outputs/claim1_switching_toy/SHA256SUMS
(cd outputs/claim2_scyfi_fixedpoint_toy && sha256sum -c SHA256SUMS)
~~~

The final verifier checks internal consistency and publication hygiene. A passing verifier does not upgrade a structural toy or source transcription into a cPLRNN benchmark reproduction.

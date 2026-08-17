#!/usr/bin/env python3
"""Verify the published, source-pinned cPLRNN scoped audit."""

from __future__ import annotations

import hashlib
import json
import subprocess
import tarfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_REPOSITORY = "https://github.com/MachineLearning-Nerd/icml26-continuous-time-piecewise-linear-rnns"
EXPECTED_EMAILS = {
    "MachineLearning-Nerd@users.noreply.github.com",
    "37579156+MachineLearning-Nerd@users.noreply.github.com",
}
REQUIRED_FILES = {
    ".gitignore",
    "README.md",
    "STATUS.md",
    "AUTONOMOUS_STATE.json",
    "CLAIM_EVIDENCE.md",
    "SOURCE_AUDIT.md",
    "ENVIRONMENT.md",
    "REPORT.md",
    "AUTHOR_THANK_YOU.md",
    "CITATION.cff",
    "BRANCH_AUDIT.md",
    "branch-audit.md",
    "claims.json",
    "contract/live_claims.json",
    "evidence/source/SHA256SUMS",
    "evidence/source/arxiv-2602.15649.pdf",
    "evidence/source/arxiv-2602.15649-source.tar.gz",
    "logbook/claim-2.md",
    "outputs/claim1_switching_toy/SHA256SUMS",
    "outputs/claim1_switching_toy/summary.json",
    "outputs/claim2_scyfi_fixedpoint_toy/PROTOCOL.md",
    "outputs/claim2_scyfi_fixedpoint_toy/SHA256SUMS",
    "outputs/claim2_scyfi_fixedpoint_toy/summary.json",
    "src/claim1_switching_toy.py",
    "src/claim2_scyfi_fixedpoint_toy.py",
    "tests/test_claim1.py",
    "tests/test_claim2.py",
    "EVIDENCE_MANIFEST.json",
    "verify_final.py",
}


def run(*args: str) -> str:
    return subprocess.check_output(args, cwd=ROOT, text=True).strip()


def fail(message: str) -> None:
    raise SystemExit(f"FINAL_AUDIT=FAILED {message}")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def check_sha(path: Path, expected: str) -> None:
    if not path.is_file():
        fail(f"missing={path.relative_to(ROOT)}")
    actual = sha256(path)
    if actual != expected:
        fail(f"sha256={path.relative_to(ROOT)}:{actual}")


def check_checksum_file(path: Path) -> None:
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        expected, relative = line.split(maxsplit=1)
        relative = relative.strip()
        candidate = ROOT / relative
        if not candidate.is_file():
            candidate = ROOT / path.parent.relative_to(ROOT) / relative
        check_sha(candidate, expected)


def check_git_state() -> list[str]:
    if run("git", "branch", "--show-current") != "main":
        fail("current_branch")
    if run("git", "remote", "get-url", "origin").removesuffix(".git") != EXPECTED_REPOSITORY:
        fail("origin_url")
    local_branches = run("git", "for-each-ref", "--format=%(refname:short)", "refs/heads").splitlines()
    if local_branches != ["main"]:
        fail(f"local_branches={local_branches}")
    refs = run("git", "for-each-ref", "--format=%(refname)", "refs").splitlines()
    if any(ref.startswith("refs/original/") or "backup" in ref for ref in refs):
        fail("stale_refs")
    commits = run("git", "rev-list", "main").splitlines()
    if len(commits) < 3:
        fail(f"reachable_commits={len(commits)}")
    for commit in commits:
        fields = run("git", "show", "-s", "--format=%an%x00%ae%x00%cn%x00%ce%x00%B", commit).split("\x00", 4)
        author_name, author_email, committer_name, committer_email, body = fields
        if author_name != "MachineLearning-Nerd" or committer_name != "MachineLearning-Nerd":
            fail(f"attribution={commit}")
        if author_email not in EXPECTED_EMAILS or committer_email not in EXPECTED_EMAILS:
            fail(f"email={commit}")
        if "co-authored-by:" in body.lower():
            fail(f"coauthor={commit}")
    return commits


def check_json() -> None:
    state = json.loads((ROOT / "AUTONOMOUS_STATE.json").read_text())
    claims = json.loads((ROOT / "claims.json").read_text())
    contract = json.loads((ROOT / "contract/live_claims.json").read_text())
    expected_statuses = {
        "C1": "TOY_SOURCE_SWITCHING",
        "C2": "TOY_SOURCE_REGIONAL_FIXED_POINT",
        "C3": "UNVERIFIED",
        "C4": "UNVERIFIED",
        "C5": "UNVERIFIED",
    }
    if state["phase"] != "published_and_verified":
        fail("state_phase")
    if state["github_repository"] != EXPECTED_REPOSITORY:
        fail("state_repository")
    if state["branch_set"] != ["main"]:
        fail("state_branches")
    if state["overall_verdict"] != "INCONCLUSIVE_SCOPED_TO_SOURCE_AND_BOUNDED_TOY":
        fail("state_verdict")
    if state["claim_statuses"] != expected_statuses:
        fail("state_claims")
    if claims["repository"]["url"] != EXPECTED_REPOSITORY:
        fail("claims_repository")
    if claims["overall_verdict"] != state["overall_verdict"] or claims["publication_allowed"]:
        fail("claims_verdict")
    if contract["paper"]["orid"] != "JuaulCZ7gE" or contract["paper"]["arxiv"] != "2602.15649":
        fail("contract_source")
    if contract["paper"]["claim_count"] != 5 or len(claims["claims"]) != 5:
        fail("claim_count")


def check_source() -> None:
    check_checksum_file(ROOT / "evidence/source/SHA256SUMS")
    check_checksum_file(ROOT / "outputs/claim1_switching_toy/SHA256SUMS")
    check_checksum_file(ROOT / "outputs/claim2_scyfi_fixedpoint_toy/SHA256SUMS")
    archive = ROOT / "evidence/source/arxiv-2602.15649-source.tar.gz"
    with tarfile.open(archive, "r:gz") as handle:
        members = handle.getmembers()
        regular = [member for member in members if member.isfile()]
        directories = [member for member in members if member.isdir()]
        executable = [member for member in regular if member.mode & 0o111]
    if len(members) != 15 or len(regular) != 14 or len(directories) != 1 or executable:
        fail("source_archive_inventory")


def check_toys() -> None:
    claim1 = json.loads((ROOT / "outputs/claim1_switching_toy/summary.json").read_text())
    if claim1["verdict"] != "toy" or claim1["switch_time"] != 0.5:
        fail("claim1_toy_header")
    if len(claim1["rows"]) != 5 or claim1["rows"][2]["exact"] != 1.0:
        fail("claim1_toy_trace")
    if "not a trained cPLRNN" not in claim1["scope"]:
        fail("claim1_toy_scope")
    claim2 = json.loads((ROOT / "outputs/claim2_scyfi_fixedpoint_toy/summary.json").read_text())
    if claim2["verdict"] != "toy" or len(claim2["candidates"]) != 2:
        fail("claim2_toy_header")
    valid = claim2["valid_fixed_points"]
    if len(valid) != 1 or valid[0]["virtual_fixed_point"] != -0.5:
        fail("claim2_valid_point")
    if claim2["candidates"][1]["region_valid"] or claim2["candidates"][1]["virtual_fixed_point"] != -1.0:
        fail("claim2_virtual_point")


def check_manifest() -> None:
    manifest = json.loads((ROOT / "EVIDENCE_MANIFEST.json").read_text())
    tracked = set(run("git", "ls-files").splitlines())
    excluded = {"AUTONOMOUS_STATE.json", "EVIDENCE_MANIFEST.json"}
    expected = sorted(tracked - excluded)
    entries = manifest.get("entries", [])
    actual = sorted(entry["path"] for entry in entries)
    if actual != expected:
        fail("manifest_paths")
    for entry in entries:
        path = ROOT / entry["path"]
        if not path.is_file():
            fail(f"manifest_missing={entry['path']}")
        if entry["bytes"] != path.stat().st_size or entry["sha256"] != sha256(path):
            fail(f"manifest_hash={entry['path']}")


def main() -> None:
    check_git_state()
    check_json()
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            fail(f"required={relative}")
    check_source()
    check_toys()
    check_manifest()
    print("FINAL_AUDIT=VERIFIED branches=1 claims=C1:toy_source_switching,C2:toy_source_regional_fixed_point,C3:unverified,C4:unverified,C5:unverified publication_allowed=false")


if __name__ == "__main__":
    main()

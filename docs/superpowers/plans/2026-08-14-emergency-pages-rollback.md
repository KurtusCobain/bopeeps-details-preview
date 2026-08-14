# Emergency Pages Rollback Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a manual-only GitHub Pages rollback path that can redeploy the preserved pre-release production snapshot without changing protected `main`.

**Architecture:** Keep `rollback/pre-release-2026-08-14` pinned to production commit `ce3412dd1d4529ec8a65aa816ebcc54da30092b4`. Add a `workflow_dispatch`-only workflow that requires the literal confirmation `ROLLBACK`, checks out that rollback branch, builds a public `_site` artifact from the preserved production files, and deploys it with GitHub Pages actions. A regression test validates that the workflow has no automatic trigger, points to the preserved branch, requires confirmation, and has Pages deployment permissions.

**Tech Stack:** GitHub Actions YAML, pytest, GitHub Pages.

## Global Constraints

- Do not modify `main` during setup.
- Do not run or dispatch the rollback workflow during verification.
- Preserve `rollback/pre-release-2026-08-14` at commit `ce3412dd1d4529ec8a65aa816ebcc54da30092b4`.
- Rollback must not require rewriting or force-updating `main`.
- Rollback deployment must be manual-only and require explicit `ROLLBACK` confirmation.

---

### Task 1: Add rollback workflow regression test

**Files:**
- Create: `tests/test_emergency_rollback_workflow.py`

**Interfaces:**
- Consumes: `.github/workflows/rollback-pages.yml`
- Produces: static assertions for trigger, confirmation gate, rollback ref, Pages permissions, and deployment action.

- [ ] **Step 1: Write the failing test**

```python
from pathlib import Path

WORKFLOW = Path('.github/workflows/rollback-pages.yml')


def test_emergency_rollback_workflow_is_manual_and_pinned():
    text = WORKFLOW.read_text(encoding='utf-8')
    assert 'workflow_dispatch:' in text
    assert 'push:' not in text
    assert "inputs.confirm == 'ROLLBACK'" in text
    assert 'ref: rollback/pre-release-2026-08-14' in text
    assert 'pages: write' in text
    assert 'id-token: write' in text
    assert 'actions/deploy-pages@v4' in text
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest -q tests/test_emergency_rollback_workflow.py`
Expected: FAIL because `.github/workflows/rollback-pages.yml` does not yet exist.

### Task 2: Add manual rollback workflow

**Files:**
- Create: `.github/workflows/rollback-pages.yml`

**Interfaces:**
- Consumes: branch `rollback/pre-release-2026-08-14`
- Produces: manual Pages deployment of the preserved production snapshot.

- [ ] **Step 1: Add the workflow**

The workflow must use `workflow_dispatch` only, require a `confirm` string input, gate the build job on `${{ inputs.confirm == 'ROLLBACK' }}`, check out `rollback/pre-release-2026-08-14`, copy only public site files/directories into `_site`, upload the artifact, and deploy with `actions/deploy-pages@v4`.

- [ ] **Step 2: Run focused test**

Run: `pytest -q tests/test_emergency_rollback_workflow.py`
Expected: PASS.

- [ ] **Step 3: Run full verification**

Run: `pytest -q && node --check script-v3.js`
Expected: all tests pass and JavaScript syntax exits 0.

- [ ] **Step 4: Confirm workflow has not run**

Inspect Actions history for `Emergency rollback to pre-release site`; expected: no run triggered by these commits because the workflow has no `push` trigger.

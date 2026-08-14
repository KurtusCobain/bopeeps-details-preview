from pathlib import Path

WORKFLOW = Path('.github/workflows/rollback-pages.yml')


def test_emergency_rollback_workflow_is_manual_and_pinned():
    text = WORKFLOW.read_text(encoding='utf-8')
    assert 'workflow_dispatch:' in text
    assert '\npush:' not in text
    assert "inputs.confirm == 'ROLLBACK'" in text
    assert 'ref: rollback/pre-release-2026-08-14' in text
    assert 'pages: write' in text
    assert 'id-token: write' in text
    assert 'actions/deploy-pages@v4' in text

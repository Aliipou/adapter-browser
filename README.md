# adapter-browser

Decision OS / AuthGate **execution adapter** for browser automation
(Playwright/Selenium-style actions). It exposes browser actions as **governed
tools**: each tool is the effect *behind* a Policy Enforcement Point and runs
only when the `decision-os-min` kernel authorizes the action. The adapter holds
**no authority** of its own and never bypasses the kernel — every call is
authorized and audited.

> Part of the Decision OS — governed by the Legitimacy ⊥ Authority pipeline
> (FDK legitimacy → AuthGate authority). Adapters adapt tools into governed
> effects and hold **no authority** of their own.

## What it adapts

| Tool | Capability | Effect |
|------|------------|--------|
| `browser_navigate` | `tool:browser_navigate` | Navigate to a URL |
| `browser_click` | `tool:browser_click` | Click an element by selector |

## Install

```bash
pip install -e .          # brings in decision-os-min
# for development:
pip install -e ".[dev]"   # + pytest, ruff, mypy
```

## Usage

```python
from decision_os_min import Governor, set_actor
from dos_adapter_browser import governed_tools

policy = {"grants": {"agent:ops": ["tool:browser_navigate"]}, "default": "deny"}
gov = Governor(policy, audit_path="audit.jsonl")
tools = governed_tools(gov)

set_actor("agent:ops")
tools["browser_navigate"]("https://example.com")   # runs only if the kernel ALLOWs
```

An actor without the matching grant raises `GovernanceRefused` before the effect
runs.

## Status & limitations

**Experimental / interface-only.** The tool bodies are honest stubs that return a
string describing the intended effect — they do **not** drive a real browser
(Playwright/Selenium) yet. Wire the real driver at the `# TODO` markers in
`dos_adapter_browser/__init__.py`. What is real today is the governance wiring:
the capability→tool mapping and the fail-closed authorization boundary.

This is reference software. Review and test before any production use. No session
lifecycle, waits, or error handling is provided.

## License

PolyForm Noncommercial 1.0.0 (see `LICENSE`).

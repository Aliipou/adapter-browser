# adapter-browser — EXPERIMENTAL execution adapter (browser automation (Playwright/Selenium))

A **separate, experimental** consumer of `decision-os-min`. It exposes browser automation (Playwright/Selenium)
actions as **governed tools**: each tool is the effect *behind* the Policy
Enforcement Point, reached only when the kernel permits the action.

```python
from decision_os_min import Governor, set_actor
from dos_adapter_browser import governed_tools

gov = Governor(policy, audit_path="audit.jsonl")
tools = governed_tools(gov)          # every browser automation (Playwright/Selenium) call now authorized + audited
set_actor("agent:ops")
tools["browser_navigate"](...)                # runs only if the kernel says ALLOW
```

**Status: EXPERIMENTAL / INTERFACE-ONLY.** The tool bodies are honest stubs — wire
the real browser automation (Playwright/Selenium) SDK where marked. This adapter holds **no authority** and never
bypasses the kernel. It is a separate repo so the core stays small and frozen.

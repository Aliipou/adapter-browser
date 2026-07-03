"""Decision OS execution adapter for browser automation (Playwright/Selenium). EXPERIMENTAL.

Provides governed tools for browser automation (Playwright/Selenium). Each tool is the effect BEHIND the PEP: it
runs only when the kernel permits the action. The bodies are honest stubs — wire
the real browser automation (Playwright/Selenium) SDK where marked. This adapter holds NO authority and never
bypasses the kernel; `governed_tools(governor)` wraps the tools so every call is
authorized + audited.
"""

from __future__ import annotations

from typing import Any


def browser_navigate(url) -> str:
    # TODO: wire the real browser automation (Playwright/Selenium) SDK here. Until then, an honest stub.
    return f"[browser] navigate {url}"


def browser_click(selector) -> str:
    # TODO: wire the real browser automation (Playwright/Selenium) SDK here. Until then, an honest stub.
    return f"[browser] click {selector}"


# The tool registry + per-tool capability specs (capability = "tool:<name>").
TOOLS = {"browser_navigate": browser_navigate, "browser_click": browser_click}
SPECS = {"browser_navigate": {"capability": "tool:browser_navigate"}, "browser_click": {"capability": "tool:browser_click"}}


def governed_tools(governor: Any) -> dict[str, Any]:
    """Wrap this adapter's tools with a decision_os_min.Governor so every call is
    routed through the kernel. Returns the governed tool registry."""
    return governor.wrap(TOOLS, specs=SPECS)

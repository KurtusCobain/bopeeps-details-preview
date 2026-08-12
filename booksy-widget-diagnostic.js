(() => {
  const RESULT_KEY = "__bopeepsBooksyDiagnostic";
  const state = {
    classification: "B2",
    reason: "Waiting for the Booksy booking modal to open.",
    booksyContainers: 0,
    booksyIframes: [],
    hostDescriptionCandidates: 0,
    stableHostDescriptionCandidates: 0,
    lastScan: null,
  };

  const safeOrigin = src => {
    try {
      return new URL(src, location.href).origin;
    } catch (_) {
      return "unparseable";
    }
  };

  const inspectIframe = iframe => {
    const src = iframe.getAttribute("src") || "";
    let sameDocumentAccess = false;
    let accessResult = "not-tested";

    try {
      const doc = iframe.contentDocument;
      sameDocumentAccess = Boolean(doc && doc.documentElement);
      accessResult = sameDocumentAccess ? "accessible" : "unavailable";
    } catch (_) {
      accessResult = "blocked-by-origin";
    }

    return {
      src,
      origin: safeOrigin(src),
      sameDocumentAccess,
      accessResult,
    };
  };

  const looksStable = element => {
    const cls = String(element.className || "");
    const aria = element.getAttribute("aria-label") || "";
    return Boolean(
      element.hasAttribute("data-testid") ||
      /description/i.test(cls) ||
      /description/i.test(aria)
    );
  };

  const inspectHostDescriptionCandidates = root => {
    const candidates = [];
    root.querySelectorAll("p, div, span").forEach(element => {
      if (element.closest("#bopeeps-booksy-diagnostic")) return;
      const style = getComputedStyle(element);
      const webkitClamp = style.webkitLineClamp || "none";
      const lineClamp = style.lineClamp || "none";
      const clippedByHeight = element.scrollHeight > element.clientHeight + 2;
      const clampActive = webkitClamp !== "none" || lineClamp !== "none";
      const overflowClip = ["hidden", "clip"].includes(style.overflowY) || ["hidden", "clip"].includes(style.overflow);
      if (!clampActive && !(clippedByHeight && overflowClip)) return;

      candidates.push({
        stable: looksStable(element),
        webkitLineClamp: webkitClamp,
        lineClamp,
        maxHeight: style.maxHeight,
        overflow: style.overflow,
        display: style.display,
      });
    });
    return candidates;
  };

  const classify = () => {
    const booksyRoots = [...document.querySelectorAll('[class*="booksy"], [id*="booksy"]')]
      .filter(element => !element.closest("#bopeeps-booksy-diagnostic"));
    const booksyFrames = [...document.querySelectorAll('iframe[src*="booksy"], [class*="booksy"] iframe')];
    const iframeFacts = booksyFrames.map(inspectIframe);

    const hostCandidates = [];
    booksyRoots.forEach(root => {
      hostCandidates.push(...inspectHostDescriptionCandidates(root));
    });

    const inaccessibleBooksyFrame = iframeFacts.some(frame =>
      frame.origin.includes("booksy") && !frame.sameDocumentAccess
    );
    const accessibleBooksyFrame = iframeFacts.some(frame =>
      frame.origin.includes("booksy") && frame.sameDocumentAccess
    );
    const stableCandidates = hostCandidates.filter(candidate => candidate.stable);

    state.booksyContainers = booksyRoots.length;
    state.booksyIframes = iframeFacts;
    state.hostDescriptionCandidates = hostCandidates.length;
    state.stableHostDescriptionCandidates = stableCandidates.length;
    state.lastScan = new Date().toISOString();

    if (inaccessibleBooksyFrame) {
      state.classification = "B3";
      state.reason = "Booksy booking content is inside a Booksy-origin iframe that the BoPeeps host page cannot access. Host-page CSS cannot expand service descriptions inside it.";
      return;
    }

    if (accessibleBooksyFrame && stableCandidates.length > 0) {
      state.classification = "B1";
      state.reason = "Booksy content is accessible and a stable description-like truncation surface was detected. A CSS-only expansion test may be reasonable.";
      return;
    }

    if (booksyRoots.length > 0 || iframeFacts.length > 0) {
      state.classification = "B2";
      state.reason = "Booksy structure is visible, but no stable host-page description surface is available yet. Shipping an override would be brittle.";
      return;
    }

    state.classification = "B2";
    state.reason = "Waiting for the Booksy booking modal to open.";
  };

  const panel = document.createElement("aside");
  panel.id = "bopeeps-booksy-diagnostic";
  panel.setAttribute("aria-live", "polite");
  panel.innerHTML = `
    <strong>Booksy Widget Diagnostic</strong>
    <div data-diag-result>Waiting for widget…</div>
    <small>This development-only panel inspects structure only. It does not read booking or payment fields.</small>
  `;
  Object.assign(panel.style, {
    position: "fixed",
    right: "12px",
    bottom: "12px",
    zIndex: "2147483647",
    width: "min(420px, calc(100vw - 24px))",
    padding: "14px",
    border: "1px solid rgba(255,255,255,.25)",
    borderRadius: "12px",
    background: "rgba(9,9,10,.96)",
    color: "#fff",
    font: "13px/1.45 system-ui, sans-serif",
    boxShadow: "0 18px 55px rgba(0,0,0,.45)",
  });
  panel.querySelector("small").style.color = "#aaa";
  document.body.appendChild(panel);

  const render = () => {
    classify();
    window[RESULT_KEY] = Object.freeze({
      classification: state.classification,
      reason: state.reason,
      booksyContainers: state.booksyContainers,
      booksyIframes: state.booksyIframes.map(frame => ({ ...frame })),
      hostDescriptionCandidates: state.hostDescriptionCandidates,
      stableHostDescriptionCandidates: state.stableHostDescriptionCandidates,
      lastScan: state.lastScan,
    });

    const target = panel.querySelector("[data-diag-result]");
    const frames = state.booksyIframes.length
      ? state.booksyIframes.map(frame => `${frame.origin}: ${frame.accessResult}`).join(" | ")
      : "none yet";
    target.textContent = `${state.classification} — ${state.reason} Booksy iframes: ${frames}.`;
  };

  const observer = new MutationObserver(() => {
    window.clearTimeout(observer._timer);
    observer._timer = window.setTimeout(render, 80);
  });

  observer.observe(document.documentElement, { childList: true, subtree: true, attributes: true });
  render();
})();

# Java in the browser (CheerpJ spike)

Result: **javac from the CheerpJ JDK 21 runtime works** (`com.sun.tools.javac.Main`). ECJ is not needed
(not tried; jar not committed). Prototype `spikes/java/index.html` was deleted in Task 5; the shipped runner is `web/runners/java.js` + `java-frame.html`.

## Working calls
```js
<script src="https://cjrtnc.leaningtech.com/5.0/loader.js"></script>
await cheerpjInit({version: 21});
cheerpOSAddStringFile('/str/Solution.java', src);          // /str/ = JS-injected strings (readable by javac)
const ce = await cheerpjRunMain('com.sun.tools.javac.Main', '/app/',
    '-d', '/files/out', '/str/Solution.java', '/str/Main.java');   // resolves to the exit code; 0 = ok
const re = await cheerpjRunMain('Main', '/files/out/');            // classpath = compiled dir; resolves to exit code
```
- Output dir `/files/out` (IndexedDB-backed, writable, persists across page loads).
- stdout/stderr of both javac and the program go to `<pre id="console">` (CheerpJ's default console element);
  read `textContent` after each `cheerpjRunMain` and clear it. javac diagnostics land there too
  (`/str/Main.java:1: error: incompatible types ...`, compile exit 1).
- Exit code: the promise from `cheerpjRunMain` resolves to it; `System.exit(n)` works (exit 0 / 1 seen).
- Multi-file works: custom `@interface Test` (RUNTIME retention) + `Solution` + `Main` compiled in one javac call;
  `Main` found `@Test` methods by reflection and invoked them -> `PASS addWorks`. So JUnit-like annotations
  compiled with user code are feasible (JUnit itself is not available; ship own mini annotations/assert helpers).
- Expect ~10 harmless 404s in the server log for javac probing `/app/` (`META-INF/services/...`, `compiler_en.properties`).

## Timings (Chrome in Claude browser pane, localhost)
| run | init | compile | run |
|---|---|---|---|
| cold (first ever, CDN download of JDK modules) | 0.6 s | 5.5 s total (incl. init) | 0.45 s |  -> total 6.0 s
| warm (same page, 2nd+ compile) | 0 | ~1.2-1.5 s | ~0.4 s |
Warm total ~1.7-1.9 s per Run. Page reload with browser-cached runtime: first compile ~1.3-2 s.

## Killing a runaway program
`while(true){}` in `Main` freezes the page that hosts CheerpJ (it runs on that page's main thread).
- Same-origin `<iframe>`: shares the renderer process with the parent -> **parent freezes too, `iframe.remove()` timer never fires.** Not usable.
- `<iframe sandbox="allow-scripts">` (opaque origin): CheerpJ never finished initialising (no IndexedDB for opaque origin). Not usable.
- **Cross-site iframe works**: parent `http://localhost:8765`, iframe `http://127.0.0.1:8765` (different site -> separate process).
  The parent stayed responsive, the timeout fired at 6.0 s, `iframe.remove()` killed the loop, and a fresh iframe then
  compiled+ran normally. Results come back via `postMessage` (parent checks `e.source === iframe.contentWindow`).
  Cost: a new origin has its own cache, so the first run in it re-downloads the runtime (cold again, slower: ~8 s compile, ~2.7 s run observed in a hidden pane).
- **Open problem for GitHub Pages:** the runner must live on a different *site* than the main page
  Only a different GitHub user/organization (`*.github.io` is a public suffix, so `<org>.github.io` is a different site)
  or a different registrable/custom domain isolates. Another repo of the same user (`user.github.io/other-repo`) is the
  same origin and site and does NOT isolate. `localhost` vs `127.0.0.1` was the stand-in. Same-site subdomains
  (`a.example.com` / `b.example.com`) are expected NOT to isolate per Chrome site-isolation rules (untested here).
  Alternative if no second site: accept that
  an infinite loop hangs the tab (user closes it) or add a static pre-check; decide in Task 5.

## Gotchas
- Re-navigating a browser tab that previously ran CheerpJ made the next CheerpJ page hang in the first `cheerpjRunMain`
  (old page's runtime/IndexedDB not released). Fresh tab each time fixed it. Likely also hits a user hitting F5 mid-run; use
  a fresh iframe per run (removing the old iframe) rather than reusing one.
- `cheerpjInit` can only be called once per page; memoise the promise.
- Community licence: runtime must stay on the CheerpJ CDN (done).

## Task 5 decisions (shipped)
- **Infinite loop: option (b), loop-guard instrumentation** (`web/runners/java-guard.js`, tests in `tests/java-guard.test.mjs`).
  - Option (a) (run in a Java thread, `join(deadline)` from main) **does not work**: in CheerpJ 5 a tight loop in a
    second thread is never preempted, `join(3000)` never returned, page frozen >90 s (tried twice, cold and warm).
  - Before compiling in the browser, `__LCT.tick()` is inserted into the user's files (subject and tests, never the harness):
    `{ __LCT.tick();` at the start of braced loop/method bodies; for unbraced/empty loops into the condition
    (`while (__LCT.tick() && (c))`, `for (a; __LCT.tick() && (b); c)`); the tail of a braced `do {…} while` is left alone.
    Strings, chars, text blocks and comments are skipped; no newlines are added (javac line numbers unchanged).
  - `tick()` checks the clock every 1024 calls; after the deadline (TestRunner sets 9 s) it prints «Таймаут…» and
    `Runtime.halt(124)`. Page is frozen until then and recovers; output printed before stays visible.
    Measured in the pane: `while(true){}` -> «Таймаут» at 11.9 s total, the next run works (3.0 s).
  - If the guarded code does not compile (a corner the lexer gets wrong, e.g. `while (true)` unbraced as the last statement
    of a non-void method), the runner compiles the original code and runs it unprotected; compile errors are always
    shown from the original code.
  - Non-loop hangs (e.g. `Thread.sleep`) do not freeze the page; a 15 s parent timer removes the iframe (output kept)
    and the next run creates a fresh one (6.1 s).
- Output dir: unique `/files/lct/r<time><rand>` per run; TestRunner deletes sibling dirs on start, so `/files` does not grow
  and stale `.class` files cannot leak.
- **Open problem: after F5 / re-navigation of a tab that ran CheerpJ, CheerpJ in the new page is very slow or stalls**
  (fresh tab: 3–6 s; same tab after reload: compile+run >15 s -> timeout; once a trivial compile hung >2 min).
  Not timer throttling (fresh tab idle 60 s is fast), not IndexedDB (raw IDB ops fast, no version upgrade), removing the
  iframe on `pagehide` does not help. Probably inside CheerpJ (it downloads through its cross-origin `c.html` iframe).
  Seen only in the Claude browser pane; not checked in a regular Chrome. Mitigation: the timer-kill message tells the
  user to open the site in a new tab. Matters for the OAuth return (same-tab navigation) in Task 7/12.

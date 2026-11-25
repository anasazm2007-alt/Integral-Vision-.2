# INTEGRAL VISION — Interactive Area & Volume Visualization Laboratory

University project (Calculus). Interactive web lab: area between curves, solids of revolution (3D),
cross-section explorer, numerical integration lab, sample experiments, experiment comparison, PDF report.
UI languages: English (default) / Arabic with RTL.

## Run
1. **Quickest:** open `index.html` in a modern browser **with internet access** (libraries load from cdnjs:
   Math.js, Plotly, Three.js, KaTeX, jsPDF). For a local server: `npx serve .` or `python3 -m http.server`.
2. **Published version:** https://claude.ai/artifact/Q7ABitzUSPGkkt35fo7chd (PDF download works there).
3. **GitHub Pages:** upload the folder contents to a repository, then Settings → Pages → Deploy from branch (main, root).
   The PDF button downloads directly in normal browsers (outside Claude it uses jsPDF's own save).

## Tests (Node 18+)
```
node tests/run-tests.js          # 90+ engine tests incl. randomized cases and exact results vs SymPy/mpmath references
node tests/validate-volume.js    # independent brute-force check of every volume mode (incl. folded y-axis)
npm install mathjs && node tests/run-tests.js   # also enables the parser/whitelist tests
python3 tests/gen-fuzz.py        # regenerates tests/fuzz-cases.json (needs sympy, mpmath)
```
The app also runs the same kind of self-tests on load (panel "Engine self-tests" in the Area module).

## Structure
```
index.html            the application (UI + embedded copy of the engine)
src/engine.js         the UI-independent mathematical engine (same code as embedded in index.html)
tests/                run-tests.js, validate-volume.js, gen-fuzz.py, fuzz-cases.json
docs/MATH.md          formulas, methods and limitations
```

## Architecture (inside index.html)
Math engine (parse/whitelist, adaptive Simpson, roots, area, volume, sections, numerical rules) ·
Module UIs (Area, Solid, Cross-sections, Numerical lab, Experiments & Reports) · Plotly (2D) · Three.js (3D) ·
KaTeX (MathML output) · jsPDF (report). User expressions are parsed by Math.js into an AST and checked against a
whitelist (x, constants, listed functions); **no `eval`** of user text.

## Known limitations (honest list)
- Numerical results use adaptive Simpson (tolerance 1e-11 per piece, error estimate displayed).
- **Analytical Result** is computed exactly (BigInt rational arithmetic) only for **polynomials of degree ≤ 6 with rational
  coefficients, rational bounds and rational intersection points** (e.g. 1/6, 32π/5, 2π/15), and is cross-checked against
  the numerical value. For other inputs (sin, ln, e^x, irrational intersections, a region on both sides of the y-axis)
  the app says "numerical only" instead of inventing a symbolic result. A general symbolic integrator (e.g. Nerdamer)
  is not included.
- Rotation about the y-axis uses the shell formula (same volume as horizontal washers, which would need inverse
  functions). When the region lies on both sides of the y-axis the solid is the **union** of both revolved sides.
- Functions with poles or outside their domain on [a, b] are refused rather than integrated.
- Region description is "between y=f(x) and y=g(x)"; the axis of rotation is the x- or y-axis (no shifted axes).
- PDF report is English/ASCII only (default PDF fonts lack Arabic and math symbols).
- The browser UI (3D rendering, touch, PDF layout) was verified by smoke tests with stubbed libraries only;
  see the final report for what was checked in a real browser.

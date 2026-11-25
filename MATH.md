# Mathematics used
**Area:** A = ∫ₐᵇ |f(x) − g(x)| dx, evaluated piecewise between consecutive roots of f − g (sign changes found by
sampling + bisection); upper/lower function chosen from the sign of f − g at each piece midpoint.

**Volume about the x-axis (disk/washer).** At each x the region is the y-interval [lo, hi] = [min(f,g), max(f,g)].
Its distance from the axis: if lo ≥ 0: R = hi, r = lo; if hi ≤ 0: R = −lo, r = −hi; if it crosses the axis:
R = max(hi, −lo), r = 0. V = π ∫ (R² − r²) dx, split also at roots of f, g and f + g (where R, r switch).
Method reported = Disk if r = 0 everywhere, otherwise Washer.

**Volume about the y-axis.** V = 2π ∫ |x|·|f − g| dx (shells; equals horizontal washers). If a < 0 < b both sides revolve
onto the same space; the solid is their union: V = 2π ∫₀^ρmax ρ·|Y(ρ)| dρ with |Y| the measure of the union of the
two y-intervals at x = ±ρ.

**Partial rotation θ:** V(θ) = (θ / 2π) · V(360°).

**Cross-section explorer:** accumulated volume up to x₀ = ∫ₐ^x₀ (integrand) dx; share = accumulated / V.

**Numerical rules (n subintervals, Δx = (b − a)/n):** Left Riemann (order 1), Midpoint (2), Trapezoid (2),
Simpson (4, n even — odd n is raised by one). Reference value = adaptive Simpson with error estimate; the lab warns
when the reference itself is uncertain.

**Exact analytical results (polynomials).** f and g are fitted exactly: forward differences at integer nodes give Newton coefficients,
converted to rationals and verified at six extra points (degree ≤ 6). Breakpoints are the roots of f − g (and f, g, f + g for x-axis volumes);
each numeric root must be rationalised AND satisfy P(q) = 0 exactly, otherwise no exact form is reported. Antiderivatives are integrated
term by term with BigInt fractions; results are shown as p/q or (p/q)·π and compared with the numerical value.

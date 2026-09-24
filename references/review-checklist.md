# Scientific figure review checklist

Review at intended paper scale, not only while zoomed in. Compare the rendered image against the source inventory and visual schema.

## Gate 1: scientific fidelity

- Account for every required object.
- Account for every required relationship.
- Verify each arrow's source, target, and direction.
- Verify ordering, branching, loops, hierarchy, and parallel correspondence.
- Reject invented modules, icons with scientific meaning, equations, legends, results, or causal claims.
- Reject any generated empirical value or data mark.

Any failure in this gate blocks acceptance.

## Gate 2: text fidelity

- Compare each visible label character by character with the exact-label list.
- Check that a label is attached to the correct object or arrow.
- Check subscripts, superscripts, Greek letters, signs, and capitalization.
- Reject schema meta-labels such as `ZONE 1`, `Container`, or `Key Text Labels`.
- If a label cannot be corrected reliably in one targeted edit, remove it and add it later with deterministic software.

## Gate 3: visual communication

- Confirm one obvious reading order.
- Confirm related modules are grouped and unrelated modules are separated.
- Check for arrow crossings, ambiguous junctions, clipped arrowheads, and hidden endpoints.
- Check consistent sizes, spacing, line weights, corner radii, and semantic colors.
- Confirm text remains readable at the intended one-column or two-column width.
- Check that grayscale still communicates grouping through shape, border, or line style.

## Gate 4: production quality

- Use a clean white or venue-appropriate background.
- Reject heavy shadows, glow, faux 3D, photo textures, watermarks, and decorative clutter.
- Verify the saved file dimensions and that it is not visibly compressed or cropped.
- Record that the artifact is raster and whether manual redrawing or deterministic text overlay is still required.
- Check the target venue's current AI-image policy before submission.

## Audit record template

```markdown
# Figure audit

- Source reviewed: <paths or citation>
- Visual schema: <path>
- Rendered image: <path>
- Intended size: <one-column/two-column/custom>
- Renderer mode: <built-in ImageGen/approved CLI fallback>

## Findings

| Check | Pass | Evidence or correction |
|---|---:|---|
| Required objects | yes/no | ... |
| Required relationships | yes/no | ... |
| Arrow directions | yes/no | ... |
| Unsupported content absent | yes/no | ... |
| Exact labels | yes/no/deferred | ... |
| Paper-scale readability | yes/no | ... |

## Remaining limitations

- <manual work, venue policy, raster limitation, or none>
```

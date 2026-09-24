---
name: academic-figure-imagegen
description: "Turn paper abstracts, method sections, sketches, or reference figures into publication-ready academic concept illustrations with a source-grounded visual schema, built-in ImageGen rendering, targeted editing, and a scientific-accuracy audit. Use for model architecture diagrams, method pipelines, mechanism schematics, conceptual comparisons, taxonomies, or overview figures for papers and talks. Do not use for plots or tables derived from experimental data; generate those deterministically from the real data instead."
---

# Academic Figure ImageGen

Create academic raster illustrations through four stages: **Architect → Renderer → Editor → Auditor**. Treat the image model as a renderer, never as the source of scientific truth.

## Non-negotiable boundaries

- Use this skill for architecture diagrams, method pipelines, mechanism schematics, conceptual comparisons, taxonomies, and overview figures.
- Do not use generative images for line, bar, scatter, box, violin, heatmap, or other empirical plots. Route those to `$paper-figure` or deterministic plotting code using the real data.
- Do not invent modules, equations, arrows, labels, results, or causal relationships that are absent from the source.
- Treat generated text and geometry as untrusted until checked against the visual schema.
- If the target venue prohibits AI-generated figures, use the output only as a layout draft and redraw it in SVG, Figma, Illustrator, PowerPoint, TikZ, or another accepted tool.
- State that the output is raster. Do not call it editable vector art merely because it uses a vector-like visual style.

## Renderer dependency

Before the first render or image edit, read `${CODEX_HOME:-$HOME/.codex}/skills/.system/imagegen/SKILL.md` completely and follow it. Explicitly invoke `$imagegen` and use its built-in image generation path by default. Do not require `OPENAI_API_KEY` for the built-in path.

Follow the dependency's rules for local input images, edit invariants, project-bound save paths, transparent backgrounds, and CLI fallback. Never switch to its CLI fallback unless the user explicitly requests or approves that path.

## Workflow

### 1. Ground the figure in source material

Extract these facts before designing the layout:

- intended message and figure role;
- required modules, stages, inputs, outputs, and relationships;
- exact labels and equations that may appear;
- ordering, direction, feedback, branching, and grouping constraints;
- output language, aspect ratio, venue column width, and any reference images;
- elements that must not appear.

For every reference image, label its role as `style reference`, `layout reference`, `content reference`, or `edit target`. If a critical scientific relationship is ambiguous, ask one concise question. Otherwise proceed and record the assumption.

### 2. Build a visual schema

Read [references/visual-schema.md](references/visual-schema.md). Select the smallest layout that faithfully expresses the method:

- linear pipeline;
- cyclic or iterative process;
- hierarchical stack or tree;
- parallel or dual stream;
- central hub;
- compact multi-panel comparison.

Define 2–5 physical zones. Describe visible objects rather than abstractions: boxes, token grids, document stacks, feature maps, trees, queues, chips, graphs, or matrices. Specify every arrow's source, target, direction, route, line style, and optional label.

Save the schema as `visual-schema.md` beside the final figure. Validate it before rendering:

```bash
python "${CODEX_HOME:-$HOME/.codex}/skills/academic-figure-imagegen/scripts/validate_schema.py" visual-schema.md
```

Fix validation errors instead of bypassing them.

### 3. Freeze the scientific contract

Create a compact inventory before rendering:

| ID | Visible object | Exact label | Incoming relation | Outgoing relation | Source support |
|---|---|---|---|---|---|

Every visible scientific element must have source support. Mark purely decorative separators or background shapes as `decorative`. This inventory is the truth set used during review.

### 4. Compose the renderer prompt

Combine the visual schema with these execution rules:

- professional academic architecture diagram suitable for a top-tier computer science paper;
- clean white background, flat 2D shapes, thin consistent outlines, restrained pastel palette, balanced whitespace;
- strict spatial arrangement and arrow routing from the schema;
- no photorealism, heavy shadow, glow, texture, fake depth, decorative clip art, watermark, or dense prose;
- render only text explicitly listed as an exact label in the schema;
- never render meta-words such as `ZONE`, `LAYOUT CONFIGURATION`, `Container`, `Visual Structure`, or `Key Text Labels`;
- use a clean sans-serif font and keep labels short enough to survive paper scaling.

Prefer 3–5 stable colors with exact HEX values. Keep the same semantic role on the same color. Use redundant shape, border, or line-style cues so the figure remains understandable in grayscale.

If the diagram needs many or long labels, generate a label-light or label-free base illustration and add text later with deterministic drawing software. Do not keep regenerating the whole image to chase typography.

### 5. Render with ImageGen

Use `$imagegen` in built-in mode. Treat a paper-provided image as a reference unless the user explicitly asks to edit it. For a local edit target, inspect it with `view_image` before invoking the edit flow.

For a project-bound figure:

1. Render from the schema and execution rules.
2. Inspect the result visually.
3. Copy the selected output from the ImageGen default location into `figures/ai_generated/` or the user's requested directory.
4. Use a descriptive, non-destructive filename such as `method-overview-v1.png`.

Do not leave the only project copy under the ImageGen default output directory.

### 6. Audit against the source

Read [references/review-checklist.md](references/review-checklist.md) and inspect the image with `view_image`. Check every inventory row, not merely the overall impression.

Route failures by cause:

- **Logic or layout failure:** revise `visual-schema.md`, revalidate, and render again.
- **Localized visual defect:** edit the existing image with one precise change and repeat all invariants that must remain unchanged.
- **Text defect:** attempt one targeted correction. If text remains unreliable, remove generated labels and add them deterministically outside the image model.
- **Unsupported element or reversed relationship:** reject the image until corrected; visual polish never compensates for scientific error.

Avoid random rerolls when the schema is wrong. Preserve a scientifically correct 80% result and make targeted edits.

### 7. Save the audit trail

Keep these project-bound deliverables together:

- final PNG or WebP;
- `visual-schema.md`;
- `render-prompt.md` containing the exact prompt sent to ImageGen;
- `figure-audit.md` recording checks, remaining limitations, and any human post-processing needed.

Finish by reporting the saved paths, the final prompt, the built-in or fallback mode used, and whether all scientific checks passed.

## Completion criteria

Do not call the figure complete until:

- every required object and relationship is present;
- no unsupported object or relationship was introduced;
- every arrow has the correct endpoints and direction;
- exact labels are correct or intentionally deferred to deterministic post-processing;
- the figure remains readable at its intended paper width;
- the saved project artifact and audit files exist and are non-empty.

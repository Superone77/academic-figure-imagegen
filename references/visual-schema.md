# Visual schema

Use this schema to separate scientific reasoning from raster rendering. Keep it concrete and spatial. Do not put explanatory prose inside the image unless it is an exact label.

## Layout selection

| Layout | Use for | Core rule |
|---|---|---|
| Linear pipeline | preprocessing, encoding-decoding, staged systems | Keep one dominant left-to-right flow. |
| Cyclic or iterative | optimization, reinforcement learning, feedback | Draw an explicit loop-back arrow. |
| Hierarchical stack | multiscale features, trees, coarse-to-fine methods | Make parent-child or scale order visually unambiguous. |
| Parallel or dual stream | multimodal fusion, contrastive learning, teacher-student methods | Align corresponding stages across streams. |
| Central hub | agent-environment, retrieval, knowledge graphs | Place the core module centrally and route spokes without crossings. |
| Multi-panel comparison | baseline vs. proposed method, train vs. inference | Use aligned panels and a shared visual grammar. |

Combine at most two layouts. If more are needed, split the figure into labeled panels.

## Golden schema template

```text
---BEGIN VISUAL SCHEMA---

[STYLE AND META-INSTRUCTIONS]
Purpose: <paper figure role>
Canvas: <aspect ratio and intended width>
Style: clean academic raster illustration with flat vector-like geometry
Palette: <semantic role = HEX value>
Text policy: render only exact labels in double quotes

[LAYOUT CONFIGURATION]
Selected layout: <one layout or a two-layout combination>
Composition logic: <one-sentence spatial summary>
Reading order: <explicit order>

[ZONE 1: <location> - <scientific role>]
Container: <shape, size, and placement>
Visual structure: <visible physical objects>
Exact labels: "<label 1>", "<label 2>"
Must not contain: <forbidden objects or labels>

[ZONE 2: <location> - <scientific role>]
Container: <shape, size, and placement>
Visual structure: <visible physical objects>
Exact labels: "<label>"
Must not contain: <forbidden objects or labels>

[CONNECTIONS]
1. From <object ID> to <object ID>; <straight/curved/orthogonal>; <solid/dashed>; arrowhead at <target>; exact label "<optional label>".
2. <repeat for every relationship>

[GLOBAL CONSTRAINTS]
- <scientific invariants>
- <alignment and spacing invariants>
- No extra scientific objects, arrows, labels, legends, or equations.

---END VISUAL SCHEMA---
```

Use 2–5 zones. Add stable object IDs such as `Z1-A`, `Z2-B`, and reference those IDs in connections. A connection description must specify both endpoints and arrow direction.

## Physical-language conversions

Replace vague concepts with visible structures:

| Avoid | Use instead |
|---|---|
| “the model understands context” | “four token cards enter a blue encoder stack; a context vector exits on the right” |
| “knowledge is integrated” | “two arrows merge at a circular fusion node connected to a small graph of five nodes” |
| “iterative refinement” | “three modules form a clockwise loop; a curved arrow returns from the third to the first” |
| “multiscale features” | “three aligned feature grids of decreasing resolution are stacked vertically” |
| “better representation” | describe the actual tensor, embedding, graph, or output object shown |

Do not turn an unobservable claim into a decorative symbol. Show only structures supported by the source.

## Renderer wrapper

Append this wrapper around the validated schema:

```text
Create a professional academic architecture diagram suitable for a top-tier computer science paper.
Use a clean white background, flat 2D geometric shapes, thin consistent outlines, restrained pastel fills, balanced whitespace, and a clean sans-serif font.
Strictly follow the schema's spatial arrangement, object inventory, and arrow endpoints.
Render only text written in double quotes after "Exact labels" or as an exact connection label.
Do not render schema headings or meta-words, including ZONE, LAYOUT CONFIGURATION, Container, Visual structure, Exact labels, Connections, or Global constraints.
Do not add photorealism, heavy shadow, glow, texture, fake 3D depth, decorative clip art, watermark, or any unlisted scientific object.

<paste validated visual schema here>
```

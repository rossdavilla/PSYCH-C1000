# Spot the Dangerous Criminal

A seven-round classroom activity. Students see three booking photographs at a time — one man
convicted of a violent offense, two convicted of drug offenses — and pick the violent one.
The results screen charts their score against the 2.3 / 7 they'd expect from blind guessing,
which leaves the discussion to you.

## Embedding

The game is one self-contained file that renders in a fixed 720 × 450 box with no scrolling
and no external requests.

```html
<iframe src="https://rossdavilla.github.io/PSYCH-C1000/Spot%20the%20Dangerous%20Criminal/"
        width="720" height="450" frameborder="0" title="Spot the Dangerous Criminal"></iframe>
```

Students can click a photograph or press `1`, `2`, `3`; `Enter` advances.

## Layout

```
index.html           the game — HTML, CSS, and JS in one file
MUGSHOT-PROMPT.md    how the photos were normalized, and the prompt to reuse
tools/pack.py        rebuilds img/faces/ from img/aligned/
img/                 the 21 original photographs, as collected
img/aligned/         1122×1402 normalized masters  (the good copies)
img/faces/           400×500 JPEGs  (what the game actually loads)
img/manifest.json    which pNN came from which original, and its group
```

`p01`–`p14` are drug convictions, `p15`–`p21` are violent convictions. Each violent face is
used once per playthrough and the fourteen drug faces fill the other two slots, so no face
repeats within a run.

## Regenerating the images

The photos went through two passes. First a local geometric one: each face was detected and
the photo rotated, scaled, and cropped so the eyes sit level, centered, 125 px apart and 38%
down from the top — no pixel inside a face repainted. Then a ChatGPT pass for the things
geometry can't fix, giving every photo the same flat grey backdrop and an even sharpness and
exposure. [MUGSHOT-PROMPT.md](MUGSHOT-PROMPT.md) has the prompt, for any photo added later.

`img/aligned/` holds the result at 1122 × 1402, quality-92 JPEG. To rebuild the web set after
changing anything there:

```bash
python3 tools/pack.py
```

That writes 400 × 500 JPEGs into `img/faces/` — 556 KB for all 21. The game draws each photo
222 CSS px wide, so 400 px stays sharp on a retina screen and when the iframe is scaled onto
a projector. `SIZE` and `QUALITY` at the top of the script are the knobs.

## A note on the images

These are real booking photographs taken from public records. The violent/non-violent labels
live in plain sight in `index.html` and in the filenames, so a student who opens the page
source can read the answers. That's fine for an in-class demonstration and not worth
obfuscating, but it's worth knowing before using this for anything graded.

One confound survives normalization. Clothing was deliberately left untouched, and bright
non-orange clothes are lopsided across the groups: green, maroon, red, and blue account for
four of the seven violent men (`p17`, `p19`, `p21`, `p18`) against one of the fourteen drug
men (`p05`). A class may beat chance by reading shirts rather than faces — worth naming in
the debrief, since it makes the point rather than spoiling it.

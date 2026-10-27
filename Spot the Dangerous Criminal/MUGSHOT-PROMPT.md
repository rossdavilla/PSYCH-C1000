# Normalizing the mugshots with ChatGPT

## Status

All 21 photos have been through this pass. `img/aligned/` holds the finished masters at
1122 × 1402. What follows is the record of how, and the prompt to reuse if you add a photo.

## The geometric pass

The 21 source images in `img/` were all over the place: 145×257 up to 1800×1800, seven
different aspect ratios, and five file formats (png, jpeg, webp, jxl, avif).

`img/aligned/p01.jpg` … `p21.jpg` began as those same photos after a **lossless geometric pass**
done locally with face detection. No pixel inside the face was repainted — each photo was
only rotated, scaled, and cropped so that:

| Property | Value |
|---|---|
| Canvas | 600 × 750 px (4:5 portrait) |
| Eye line | 38% down from the top (y ≈ 285) |
| Eye centers | horizontally centered, 125 px apart |
| Head tilt | eyes leveled to horizontal |

So **every face is already the same size, in the same place, at the same resolution.**

What's still inconsistent, and what you want ChatGPT to fix:

1. **Backgrounds** — grey, white, blue, purple, green, dark, tiled, and a few with a visible
   seam or diagonal edge where the original photo ran out during the crop.
2. **Apparent resolution** — the small sources (p06, p10, p11, p12, p13 especially) were
   upscaled 2.5–3.3× and look soft next to the sharp ones.
3. **Exposure and color cast** — some are flat and grey, some are warm, some are blown out.

### Where to start

Most originals were too small or the wrong shape to fill a 4:5 frame, so part of each aligned
image is flat filler rather than real photograph. The worst ones have an obvious grey slab
along an edge, which is a far louder cue than anything in the face. Work down this list:

| Image | Filler | Upscale | Group |
|---|---|---|---|
| p12 | 58% | 2.5× | non-violent |
| p13 | 53% | 2.5× | non-violent |
| p04 | 41% | 2.0× | non-violent |
| p02 | 38% | 1.4× | non-violent |
| p06 | 37% | 3.0× | non-violent |
| p16 | 36% | 1.1× | **violent** |
| p05 | 36% | 2.2× | non-violent |
| p20 | 34% | 1.8× | **violent** |
| p10 | 32% | 2.5× | non-violent |
| p14 | 31% | 1.4× | non-violent |

The rest run 16–29%, except p07 at 1%. Filler averages 31% in the non-violent set and 26% in
the violent set — close enough that it isn't a systematic giveaway, but individual images like
p20 and p16 still read as obviously patched.

---

## The prompt

Upload **one** image at a time from `img/aligned/` and paste this:

> I'm preparing a set of booking photographs for a psychology course activity, and I need
> them to look like they came from the same camera in the same room. Please edit the attached
> image to match this specification exactly.
>
> **Change only these three things:**
>
> 1. **Background.** Replace everything behind the person with a flat, perfectly even, neutral
>    mid-grey (#8A8D8F). No gradient, no vignette, no drop shadow, no texture, no height chart,
>    no wall seams, no visible edge where the original photo ended. The background should be a
>    single uniform color from corner to corner. Some of these images have a flat grey block
>    along an edge where the original photograph ran out — fill that area in: continue the
>    background across it, and where it cuts through the shoulders, extend the shoulders and
>    the same garment naturally so the body is complete.
> 2. **Sharpness and grain.** Bring the image to a clean, moderately sharp quality consistent
>    with a 600×750 booking photo. If the original is soft or pixelated, resolve it — but do
>    not add detail that invents new features.
> 3. **Exposure and white balance.** Neutral, even, front-lit. Correct any strong color cast
>    so skin renders naturally. Keep contrast moderate and flat — no dramatic or moody lighting.
>
> **Do not change anything else. Specifically, preserve exactly:**
>
> - The face. Same identity, same bone structure, same nose, eyes, mouth, jaw, ears, and
>   skin texture. Do not smooth, beautify, slim, age, de-age, or symmetrize the face. Keep
>   every mole, scar, wrinkle, blemish, and stubble pattern.
> - The expression. Same gaze direction, same mouth position, same brow. If he is smiling,
>   he stays smiling. If his eyes are half-closed, they stay half-closed.
> - The hair and facial hair. Same cut, length, density, hairline, and color.
> - The clothing. Same garment, same color, same collar, same visible undershirt.
> - The framing. The output must be 600×750 pixels, and the head must stay in exactly the same
>   position and at exactly the same size as in the input. Do not re-crop, re-center, zoom,
>   rotate, or add padding.
>
> This is a retouch of the attached photograph, not a new portrait. Return a single 600×750 PNG.

Save the result back into `img/aligned/` under the same `pNN` name.

---

## After each image, check these four things

ChatGPT's image editing regenerates the whole picture rather than painting over part of it,
so it *will* drift if you let it. Open the original and the result side by side and check:

1. **Is it still the same person?** This is the one that matters. Look at the nose, the
   distance between the eyes, and the ears.
2. **Did the head move or change size?** Flip between the two images. The head should not
   shift or breathe at all.
3. **Did it clean up the face?** Vanished acne, smoothed skin, straightened teeth, and tidied
   stubble are the most common failures.
4. **Is the background actually flat?** Ask for it again if there's a gradient or a soft shadow
   behind the shoulders.

If something drifted, reply with the specific problem rather than re-running the whole prompt:

> You changed his nose and removed the mole on his left cheek. Go back to the original
> attached photo, keep the face pixel-for-pixel, and only replace the background.

If a particular image keeps coming back wrong after two or three tries, it's usually one of the
heavily upscaled ones — the model has little real detail to hold onto. For those, ask for the
background replacement alone and skip the sharpening:

> Keep this photograph completely unchanged including its softness. Only replace the
> background with flat #8A8D8F. Do not sharpen, denoise, or retouch anything.

---

## Why this matters for the activity

The whole point of the game is that violent and non-violent offenders are indistinguishable by
face. That only holds if nothing *else* distinguishes them. If the violent set ends up sharper,
better lit, or on a different grey than the drug-charge set, students can score above chance by
reading the image quality instead of the face — and the demonstration quietly breaks.

So the real acceptance test isn't "does each photo look good," it's: **shuffle all 21 together
and see whether you can tell which ones were in which group.** If you can, keep normalizing.

Two residual confounds the background pass can't fix, worth knowing about:

- **Clothing.** Orange jumpsuits appear in both groups (good), but p17's green shirt and p21's
  red one are distinctive. You asked not to change clothing, so these stay — just don't let the
  distinctive shirts cluster in one group.
- **Smiling.** p05 is grinning and p11 is smiling; everyone else is neutral. Expression is a
  real cue students may latch onto.

---

## Rebuilding the game's images

The game loads `img/faces/`, not `img/aligned/`. After changing anything in `img/aligned/`,
regenerate the web-sized set:

```bash
python3 tools/pack.py
```

That re-encodes everything in `img/aligned/` to 400×500 progressive JPEG in `img/faces/`,
which is what `index.html` reads. Filenames and the violent/non-violent mapping don't change,
so nothing in the game needs editing.

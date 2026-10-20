# Image prompts for ChatGPT

The game already works with built-in SVG characters. These prompts replace them with
illustrated art. Paste the **Style preamble** once at the start of a new ChatGPT conversation,
then send the prompts one at a time — keeping them in a single conversation is what holds the
look consistent across the set.

Save each result into `cyberball/img/` using the exact filename given. The page checks for the
files on load and swaps them in automatically.

> **All three poses of a character must be present** or that character keeps its built-in art.
> So `p2-idle.png` + `p2-hold.png` + `p2-throw.png` together, or none of them. The hand
> is its own set of three. `ball.png` is independent and can be added on its own.

---

## The one thing that matters most: registration

The three poses of a character are swapped in place, like frames of an animation. If the body
drifts between frames, the character will visibly jump when it throws.

So for every character, ask for the three poses **on the same canvas, at the same size, with the
body in the same spot** — only the arms change. The most reliable way to get this out of ChatGPT
is to generate the idle pose first, then for each following pose attach the previous image and
ask for the arms to be redrawn with everything else untouched.

Small drift is survivable. A character that changes size or shifts sideways is not.

---

## Style preamble

> I'm making character art for a classroom web game about social inclusion. I'll send you a
> series of image requests. Apply this style to every one and keep the look identical across the
> whole set.
>
> **Style:** flat vector illustration, friendly and simple, like a modern mobile game. Bold
> geometric shapes, clean confident linework, generous rounded forms. Every shape carries a
> **thick dark outline in `#1F2233`** — this is the defining feature of the style. No gradients,
> no drop shadows, no 3D, no photorealism, no textures, no background scenery.
>
> **Colors:**
> - Outlines and facial features: deep navy `#1F2233` (never pure black)
> - Participant 2's shirt: violet `#6D28D9` · Participant 2's trousers: slate `#3C3F58`
> - Participant 3's shirt: orange `#F37D26` · Participant 3's trousers: deep blue `#2E4057`
> - Ball: warm orange `#F37D26` with a darker `#C9560F` shaded side
>
> **People:** simple stylized characters, roughly 4 heads tall, standing and facing the viewer.
> Round heads, dot eyes, a small curved smile, no visible nose. Limbs are thick rounded strokes.
> Participant 2 and Participant 3 should clearly be two different people — different hair and different skin
> tone — while reading as the same set.
>
> **Critical technical requirements for every image:**
> - **Transparent background.** No backdrop, no ground, no shadow under the character.
> - **Never include any text, letters, numbers or words.**
> - The character must be fully inside the frame with a small, even margin.
>
> Confirm you've got it and I'll send the first request.

---

## 1. Participant 2 — standing

**File:** `img/p2-idle.png` · **Portrait, roughly 2:3** · transparent

> A single cartoon character standing front-on, full body, head to feet, on a fully transparent
> background. Arms hanging down relaxed at their sides, angled slightly away from the body.
> Feet planted, standing still, calm and neutral. Short dark hair, light skin, violet `#6D28D9`
> sleeveless shirt, slate `#3C3F58` trousers, dark shoes. Thick `#1F2233` outlines, flat colors,
> no background, no shadow, no text.

## 2. Participant 2 — holding the ball

**File:** `img/p2-hold.png` · same canvas, same size, same position

> Same character, same size and same position in the frame — **only the arms change.** Both arms
> now reach down and inward so the hands meet in front of the waist, cupped as if they have just
> caught a ball. Leave the hands empty: I'll draw the ball myself. Everything else — head, hair,
> face, torso, legs, feet, scale, placement — must be pixel-identical to the previous image.
> Transparent background, no shadow, no text.

## 3. Participant 2 — throwing

**File:** `img/p2-throw.png` · same canvas, same size, same position

> Same character again, same size and same position — **only the arms change.** The character's
> left arm (the viewer's right) is raised up and outward in a throwing motion, extended above
> shoulder height toward the upper right, hand open and empty. The other arm stays low and
> slightly out for balance. A small lean into the throw is fine, but the feet and the overall
> footprint must not move. Transparent background, no shadow, no text.

## 4–6. Participant 3 — the same three poses

**Files:** `img/p3-idle.png`, `img/p3-hold.png`, `img/p3-throw.png`

Send the same three prompts again with these two changes:

- Participant 3 has **short textured dark hair and brown skin**, an orange `#F37D26` shirt and deep blue
  `#2E4057` trousers.
- In `p3-throw.png` the raised arm is **mirrored** — Participant 3's right arm (the viewer's left)
  goes up and outward toward the upper *left*, because Participant 3 stands on the right side of the
  screen and throws toward the middle.

Participant 3 should be recognisably a different person from Participant 2 but unmistakably from the same set:
same height, same build, same line weight, same simple face.

---

## 7. Your hand — waiting

**File:** `img/hand-idle.png` · **Landscape, roughly 6:5** · transparent

> A single cartoon hand seen from the back, palm away from the viewer, reaching up from the
> bottom edge of the frame — this is the player's own hand in a first-person view. Four fingers
> point upward with small gaps between them, slightly relaxed rather than rigid. The thumb angles
> out to the left. The wrist runs off the bottom edge of the frame and is cut off there; nothing
> below it. Light skin, thick `#1F2233` outlines, flat color, transparent background, no shadow,
> no sleeve, no text.

## 8. Your hand — closed around the ball

**File:** `img/hand-hold.png` · same canvas, same size, same position

> The same hand, same size and same position in the frame, now **closed into a fist** — the
> fingers curled all the way down so only four small rounded knuckles show along the top edge of
> the hand. Draw no ball: the fist is understood to be holding one, and the app hides the ball
> for this pose. The palm and wrist must stay exactly where they were. Transparent background,
> no shadow, no text.

## 9. Your hand — throwing

**File:** `img/hand-throw.png` · same canvas, same size, same position

> The same hand, same size and same position, fingers now **extended and spread wide**, pushing
> upward and forward in a follow-through, as if the ball has just left the hand. Fingertips reach
> higher in the frame than in the other two poses. The palm and wrist stay put at the bottom
> edge. Transparent background, no shadow, no text.

---

## 10. The ball

**File:** `img/ball.png` · **Square** · transparent

> A single simple cartoon ball, filling the frame with a small even margin, on a fully
> transparent background. Warm orange `#F37D26` with a darker `#C9560F` crescent of shading on
> the lower right and a soft light highlight on the upper left. Two thin curved seam lines in
> dark `#1F2233` crossing the face of the ball, like a playground ball. Thick `#1F2233` outline
> around the whole ball. Flat vector, no drop shadow, no background, no text.

---

## Dropping them in

1. Save all the files into `cyberball/img/` with exactly the filenames above (lowercase, `.png`).
2. Open the page. That's it — no code to edit.
3. If a character still looks like the built-in art, one of its three files is missing or
   misnamed. Check the spelling.
4. If a character jumps or resizes when it throws, the poses aren't registered to each other.
   Regenerate the offending pose from the idle image rather than from scratch.

To go back to the built-in art, move the PNGs out of `img/` again.

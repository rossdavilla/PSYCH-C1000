# Image prompts for ChatGPT

Paste the **Style preamble** once at the start of a new ChatGPT conversation, then send prompts one at a time. Keeping them in a single conversation is what holds the look consistent across the set.

Save results into `Emotion Game/img/` using the filename given with each prompt.

> **The app only places three of these:** `hero.png`, `result-high.png` and `result-low.png` (prompts 1, 2 and 3 below). Everything after that is optional and currently has nowhere to go — see *Not currently used* at the bottom.

---

## Style preamble

> I'm making illustrations for a classroom web app about facial expressions and emotion. I'll send you a series of image requests. Apply this style to every one, and keep the look identical across the whole set.
>
> **Style:** flat vector illustration with a light, airy, friendly feel. Bold geometric shapes, clean confident linework, generous rounded forms. No gradients, no drop shadows, no 3D, no photorealism, no textures. Think modern editorial illustration or a well-designed mobile app onboarding screen.
>
> **Strict color palette — use only these six colors:**
> - Powder petal `#FCEADE` (pale warm blush — the default background for every image)
> - White `#FFFFFF`
> - Strong cyan `#25CED1` (bright turquoise)
> - Coral glow `#FF8A5B` (warm orange-coral)
> - Bubblegum pink `#EA526F` (deep raspberry pink)
> - Deep plum `#36262C` (very dark warm brown-plum — use this for all linework, outlines and facial features)
>
> No other colors. **Backgrounds should always be light** — powder petal or white — never dark. The overall impression should be bright and soft, not moody.
>
> **People:** simple stylized characters with clean deep-plum linework. No visible noses or minimal ones, expressive dot-and-arc eyes, bold eyebrows. Varied body types, hair textures and hairstyles across the set. Faces should read clearly at small sizes.
>
> Render skin in palette colors — cyan, coral, pink or white — rather than naturalistic skin tones. This is intentional and important for the project: it keeps the illustrations from implying that any one group's face is the default.
>
> **Never include any text, letters, numbers or words in the images.** I'll add all typography myself.
>
> Confirm you've got it and I'll send the first request.

---

## 1. Start screen hero  ← **used by the app**

**File:** `img/hero.png` · **Landscape, 3:2**

> A horizontal illustration of two friends playing a guessing game, on a pale powder petal `#FCEADE` background. On the left, a character holds a phone up facing outward away from their own eyes, pulling an exaggerated expression — brows high, mouth open wide. On the right, a second character leans forward, chin in hand, eyebrows raised, clearly concentrating and about to guess. A few small floating geometric shapes — circles, arcs, triangles in cyan, coral and pink — scatter in the space between them to suggest energy and ideas. Light, bright and friendly. Flat vector, no text.

---

## 2. Results — strong score  ← **used by the app**

**File:** `img/result-high.png` · **Square, 1:1**

> A square celebratory illustration on a pale powder petal `#FCEADE` background. Two characters high-fiving or throwing their arms up together, heads tipped back, mouths open in laughter, shoulders raised in triumph. Confetti made of small flat geometric shapes — circles, triangles, short bars in cyan, coral and pink — bursts outward around them. Joyful and energetic, but still light and airy. Flat vector, no text.

---

## 3. Results — low score  ← **used by the app**

**File:** `img/result-low.png` · **Square, 1:1**

> A square illustration on a pale powder petal `#FCEADE` background that is warm and encouraging rather than disappointing. Two characters sitting side by side, shrugging at each other with palms up and amused half-smiles, clearly laughing it off together. One has a single raised eyebrow. A few small question-mark-shaped arcs — but no actual text characters — float above them in cyan. The mood is good-humored, not defeated. Flat vector, no text.

---

## 4. App icon *(optional — needs favicon wiring)*

**File:** `img/icon.png` · **Square, 1024×1024**

> A square app icon on a solid strong cyan `#25CED1` background. Centered: two simple stylized faces in profile looking at each other, one coral and one white, their expressions clearly different — the left face has raised brows and an open round mouth (surprise), the right face has a wide curved smile and crinkled eyes (happiness). Between and slightly above them, a small bubblegum pink spark or burst shape suggesting a guess connecting them. All linework in deep plum `#36262C`. Bold, simple, instantly readable at 60 pixels wide. Flat vector, no text.

---

## 5. Social share card *(optional — needs an og:image tag)*

**File:** `img/share.png` · **Landscape, 1200×630**

> A wide banner illustration on a pale powder petal `#FCEADE` background. Three stylized faces in a row across the left two thirds, each a different palette color and each showing a clearly different expression — surprise, a slumped downward shame posture, and a broad laugh. The right third is left mostly empty background for text to be added later. Balanced and bold, light and bright. Flat vector, no text in the image itself.

---

## Not currently used

These made sense under earlier versions of the design and no longer have a home. Left here in case the app grows.

- **Deck category art** — the two decks are shuffled together and deliberately hidden until the results screen, so showing deck artwork during play would give away the category.
- **How-to-play step illustrations** — the start screen uses a numbered text list instead.
- **Background pattern** — the light background is intentionally plain so the cards carry the contrast.
- **The 12 expression portraits** — there is no post-round review screen; results end on scores only.

---

## Practical notes

- **ChatGPT is unreliable with exact hex values.** It will land close but not perfect. At illustration scale nobody will notice, and I can color-correct to the exact palette if it bothers you.
- **It cannot produce transparent backgrounds.** Every prompt specifies a solid light background on purpose, so the images drop straight into the layout.
- **If text sneaks into an image,** reply "remove all text from the image" and regenerate. It happens most often with the results and share images.
- **Ask for variations** rather than starting over: "same image but make the left character's expression stronger" keeps the style locked.
- **The app looks finished without any of these.** Each image slot stays invisible until the file exists, so you can add them whenever — or never.

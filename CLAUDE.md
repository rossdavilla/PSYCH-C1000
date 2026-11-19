# PSYCH-C1000 — Introduction to Psychology

The course site and class activities for **PSYCH-C1000** at Modesto Junior College. Live at
<https://rossdavilla.github.io/PSYCH-C1000/>.

## Layout

| Path | What it is |
|---|---|
| `index.html` | Course site: syllabus, Know Your Professor, links to the activities |
| `PSYCHC1000-syllabus.html` | The syllabus page; it links `syllabus-assets/style.css` and `syllabus-assets/textbook.js`, which are copies of the textbook site's shared assets |
| `knowyourprof.html` | Know Your Professor |
| `mythorfact.html` | Myth or Fact? — each student gets one claim and locks in true or false; answers stay hidden until the class hears the magic word |
| `dsm.html` | **DSM Booklet** — DSM-5-TR criteria for fourteen disorders, one per screen, swipe or tap to move, with a chapter-grouped index. Criteria are tappable and each group counts checked symptoms against its own threshold. Same content as the printed booklets in the lecture folder. A reference, so it is **not** a 720 × 450 Top Hat activity |
| `Emotion Game/` | **Make a Face** — partners act out an emotion with face and shoulders only, 12 emotions, 15 seconds each |
| `cyberball/` | **Cyberball** — the social-exclusion demo. `index.html` assigns rejection by a 50/50 draw; `cyberball-rejection-nopractice.html` and `cyberball-same.html` are the fixed-condition variants |
| `Spot the Dangerous Criminal/` | Pick the violent offender out of three booking photographs, then see how close to chance you scored |
| `Thief-Game/` | **The Heist** — secretly tells each student whether to steal a prize and whether to lie about it (PSY170 has its own copy as `thiefgame.html`) |

**Read the activity's own notes before changing it.** `Spot the Dangerous Criminal/README.md`,
`Spot the Dangerous Criminal/MUGSHOT-PROMPT.md`, `cyberball/README.md`,
`cyberball/image-prompts.md`, `Emotion Game/emotion-list.md` and `Emotion Game/image-prompts.md`
each document how that activity works and how its images were made.

## Conventions

- Every activity is a single self-contained `.html` file that fits a **720 × 450** Top Hat iframe
  without scrolling, and fetches nothing from outside the repo. Folder names contain spaces, so
  URLs need `%20`.
- Nothing is collected — no backend, no analytics, no accounts.
- **`standalone.html` is gitignored on purpose.** Each activity can be built into a single
  ~1 MB offline file (every image and font embedded) with its own
  `tools/build-standalone.sh`, for classroom machines with no wifi. Those builds are for the
  machine they run on, never a second published copy. Never edit a `standalone.html` by hand —
  edit the activity and rebuild.
- Images: `img/` holds the originals as collected, `img/aligned/` the normalized masters, and
  `img/faces/` the small copies the activity actually loads. `tools/pack.py` regenerates the
  small ones; `img/manifest.json` records where each came from.

## Publishing

GitHub Pages serves `main` from the repository root, so a push to `main` is the deploy.

After adding an activity, add it to `data/sites.json` in the
[`rossdavilla.github.io`](https://github.com/rossdavilla/rossdavilla.github.io) repo with the
`PSY001` tag. Keep instructor-only pages, mockups and review sheets out of the directory by
adding them to that repo's `ignore` globs.

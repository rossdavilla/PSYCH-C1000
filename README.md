# PSYCH-C1000 — Introduction to Psychology

The course site and the in-class activities for PSYCH-C1000 at Modesto Junior College. Every
activity is a single self-contained HTML file: no build step, no dependencies, nothing fetched
from outside the repo, and nothing collected — no accounts, no backend, no analytics.

**Live site:** https://rossdavilla.github.io/PSYCH-C1000/

## The course site

| Page | What it is |
| --- | --- |
| [`index.html`](index.html) | Course home: the syllabus, Know Your Professor, and links to the activities |
| [`PSYCHC1000-syllabus.html`](PSYCHC1000-syllabus.html) | The syllabus |
| [`knowyourprof.html`](knowyourprof.html) | Know Your Professor |

## Activities

| Activity | What happens |
| --- | --- |
| [Myth or Fact?](https://rossdavilla.github.io/PSYCH-C1000/mythorfact.html) | Each student gets one claim about psychology and locks in true or false. Answers stay hidden until the class hears the magic word. |
| [Make a Face](https://rossdavilla.github.io/PSYCH-C1000/Emotion%20Game/) | Partners take turns acting out an emotion with only face and shoulders while the other guesses — 12 emotions, 15 seconds each. |
| [Cyberball](https://rossdavilla.github.io/PSYCH-C1000/cyberball/) | The classic social-exclusion demo: toss a ball with two other players until they stop throwing it to you. The main version assigns rejection by a 50/50 draw; `cyberball-same.html` and `cyberball-rejection-nopractice.html` are the fixed-condition variants. |
| [Spot the Dangerous Criminal](https://rossdavilla.github.io/PSYCH-C1000/Spot%20the%20Dangerous%20Criminal/) | Seven rounds of three booking photographs — one violent conviction, two drug convictions — then your score against the 2.3 / 7 you'd expect from guessing. |
| [The Heist](https://rossdavilla.github.io/PSYCH-C1000/Thief-Game/) | Secretly tells each student whether to steal a prize and whether to lie about it, so the class can practice detecting deception. |

Each activity renders in a fixed **720 × 450** box without scrolling, so it embeds in Top Hat:

```html
<iframe src="https://rossdavilla.github.io/PSYCH-C1000/Spot%20the%20Dangerous%20Criminal/"
        width="720" height="450" style="border:0;max-width:100%"
        title="Spot the Dangerous Criminal"></iframe>
```

Several activities carry their own notes next to the files — how the activity works and how its
images were produced: `Spot the Dangerous Criminal/README.md` and `MUGSHOT-PROMPT.md`,
`cyberball/README.md` and `image-prompts.md`, `Emotion Game/emotion-list.md` and
`image-prompts.md`.

## Offline copies

Each activity can be built into a single file with every image and font embedded — for a
classroom machine with no wifi — using its own `tools/build-standalone.sh`. Those builds
(`standalone.html`) are deliberately not committed and not published: they are for the machine
they will be used on, not a second public copy.

## Running it

Serve the folder, since the activities load local images:

```bash
python3 -m http.server 8000
```

Folder names contain spaces, so URLs need `%20`.

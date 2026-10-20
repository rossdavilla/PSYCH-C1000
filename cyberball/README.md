# Cyberball — PSYCH-C1000

A phone-friendly version of the Cyberball ball-toss paradigm (Williams & Jarvis, 2006).
Students play a short online ball game with two computer-controlled players named Alex and
Casey, and are randomly assigned to be included or excluded.

Open `index.html` — everything is in that one file.

---

## How a student experiences it

1. **Intro** — a short cover story: a ball-tossing game played online with two other people,
   and the instruction to picture the scene vividly (the standard mental-visualization framing).
2. **Practice round** — 12 throws, shared evenly. The first throw always comes to the student
   so they learn the one control: **tap the player you want to throw to.**
3. **"Finding other players"** — a brief connecting screen that names Alex and Casey.
4. **The real round** — 30 throws.
5. **End screen** — "That's the end of the game." **Nothing is revealed.** No condition, no
   throw count, no debrief. That is deliberate: you reveal and debrief in class.

Total time is roughly 2–3 minutes.

## The two conditions

Assignment is a 50/50 coin flip the first time the page is opened on that phone.

| | What happens |
|---|---|
| **Inclusion** | Each computer player passes at random between the other two, so the student receives about **1 in 3** throws (≈10 of 30), spread over the whole round. A safety net forces a throw to them if they have been skipped 5 times in a row. |
| **Exclusion** | The student receives the **1st and 3rd** computer throws, then never again. Alex and Casey throw only to each other for the remaining ~26 passes. |

The condition is saved on the phone, so a reload cannot reshuffle it, and a student who
finishes and reopens the page lands straight back on the end screen.

## What is stored

Nothing leaves the phone. One `localStorage` entry (`psychc1000-cyberball`) holds the assigned
condition, the timestamp, whether they finished, and how many throws they caught. There is no
server, no analytics, no network request of any kind except the Google Fonts stylesheet.

If you want class-level data, collect it the way you already collect anything else — a Top Hat
question after the reveal works well, since by then students know which condition they were in.

## Instructor URLs

Add these to the end of the page URL:

| | |
|---|---|
| `?instructor` | Shows a debug strip along the bottom: condition, round, throw count, catches, plus reset and force links. |
| `?reset` | Clears this phone's assignment so you can play again. |
| `?force=in` | Forces the inclusion condition. |
| `?force=ex` | Forces the exclusion condition. |

Combine them with `&`, e.g. `cyberball/?reset&force=ex&instructor`.

Handy for demoing both conditions on the projector: open `?reset&force=in` on one device and
`?reset&force=ex` on another.

## A note on the cover story

The intro and the "Finding other players" screen tell students they are playing with two other
people. That deception is the paradigm — exclusion by a computer does not sting the same way —
and it is why the end screen says nothing. Students need the in-class debrief to close the loop:
that assignment was random, that Alex and Casey were a program, and that about half the room got
the other version.

If you would rather not run the cover story, delete the `#s-connect` section from the HTML and
soften the intro copy; the game itself works unchanged.

## Tuning

Near the top of the `<script>` block:

```js
const CONFIG = {
  practiceThrows: 12,   // warm-up, ball shared equally
  mainThrows:     30,   // standard Cyberball length
  thinkMin:       520,  // how long a computer player "decides" (ms)
  thinkMax:      1350,
  flightMin:      560,  // ball flight time (ms)
  flightMax:      820,
  afterCatch:     260,  // beat after a catch before the next throw
  playerTimeout: 9000,  // auto-throw if the student doesn't tap
  nudgeAfter:    3200,  // re-show the coach hint after this long
  excludeOn:     [1,3], // in exclusion, these computer throws come to you
  rescueAfter:      5,  // inclusion safety net: never ignored this long
};
```

`ANCHORS` just below sets where the ball sits in each player's hands, as a fraction of the
screen. Nudge those numbers if you swap in illustrated art and the ball doesn't quite land in
the hands.

`NAMES` sets the two players' names — change them if "Alex" and "Casey" collide
with students in your section.

## Artwork

The page ships with built-in SVG characters, so it works as-is. To replace them with illustrated
art, follow [`image-prompts.md`](image-prompts.md) and drop the PNGs into `img/`. The page checks
for them on load and upgrades itself automatically — no code change. A set is only used if **all
three poses** for that character are present, so a half-finished set never breaks the game.

## Phones

Landscape only; a portrait phone gets a "turn your phone sideways" screen. Tapping anywhere on
the left or right half of the screen passes to that side, so it works with a thumb on either
hand. The phone gives a short vibration when the student catches the ball.

If a student switches apps mid-game the animation pauses and picks up where it left off when
they come back.

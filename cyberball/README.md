# Cyberball — PSYCH-C1000

A phone-friendly version of the Cyberball ball-toss paradigm (Williams & Jarvis, 2006).
Students play a short online ball game with two computer-controlled players, labelled
Participant 2 and Participant 3, and are randomly assigned to be included or excluded.

Open `index.html` — everything is in that one file.

---

## How a student experiences it

1. **Intro** — a short cover story: a ball-tossing game played online with two other people,
   and the instruction to picture the scene vividly (the standard mental-visualization framing).
2. **Practice round** — 12 throws, shared evenly. The first throw always comes to the student
   so they learn the one control: **tap the player you want to throw to.**
3. **"Finding other players"** — a brief connecting screen.
4. **The real round** — 20 throws.
5. **End screen** — "That's the end of the game. Thanks for playing." **Nothing is revealed.**
   No condition, no throw count, no debrief. That is deliberate: you reveal and debrief in class.

Total time is roughly two minutes.

## The two conditions

Assignment is a fresh 50/50 coin flip every time the page loads.

| | What happens |
|---|---|
| **Inclusion** | Each computer player passes at random between the other two, so the student receives about **1 in 3** throws (≈7 of 20), spread over the whole round. A safety net forces a throw to them if they have been skipped 5 times in a row. |
| **Exclusion** | The student receives the **1st and 3rd** computer throws, then never again. The other two throw only to each other for the remaining ~16 passes. |

## Replaying

The game is replayable: reload the page and you get a new round and a new coin flip. Nothing is
remembered between visits, so a student can play twice and land in different conditions — worth
knowing if you want them to experience only one.

## What is stored

Nothing. No server, no analytics, no `localStorage`, no network request of any kind except the
Google Fonts stylesheet. The condition lives in a variable and disappears when the tab closes.

If you want class-level data, collect it the way you already collect anything else — a Top Hat
question after the reveal works well, since by then students know which condition they were in.

## Instructor URLs

Add these to the end of the page URL:

| | |
|---|---|
| `?instructor` | Shows a debug strip along the bottom: condition, round, throw count, catches, plus replay and force links. |
| `?force=in` | Forces the inclusion condition. |
| `?force=ex` | Forces the exclusion condition. |

Combine them with `&`, e.g. `cyberball/?force=ex&instructor`.

Handy for demoing both conditions on the projector: open `?force=in` on one device and
`?force=ex` on another.

## A note on the cover story

The intro and the "Finding other players" screen tell students they are playing with two other
people. That deception is the paradigm — exclusion by a computer does not sting the same way —
and it is why the end screen says nothing. Students need the in-class debrief to close the loop:
that assignment was random, that the other two players were a program, and that about half the
room got the other version.

If you would rather not run the cover story, delete the `#s-connect` section from the HTML and
soften the intro copy; the game itself works unchanged.

## Tuning

Near the top of the `<script>` block:

```js
const CONFIG = {
  practiceThrows: 12,   // warm-up, ball shared equally
  mainThrows:     20,   // the round students are scored by
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

`NAMES` sets the two players' labels.

`ANCHORS` sets where the ball sits for each player: `x` and `y` as a fraction of the screen, and
`s`, the size the ball takes there. The two players sit at `s: 0.85` and the student's own hand
at `s: 1.70` — exactly double — so the ball doubles in size as it comes toward them and halves as
it goes away, which is what sells the perspective. It interpolates between the two ends in
flight, and a throw between the two players stays one size, since they are at the same depth.
Nudge `x`/`y` if you swap in illustrated art and the ball doesn't quite land in the hands; nudge
`s` to dial the perspective up or down.

## Artwork

The page ships with built-in SVG characters, so it works as-is. To replace them with illustrated
art, follow [`image-prompts.md`](image-prompts.md) and drop the PNGs into `img/`. The page checks
for them on load and upgrades itself automatically — no code change. A set is only used if **all
three poses** for that character are present, so a half-finished set never breaks the game.

The student's own hand is drawn from the back with no visible thumb. At phone size a thumb only
ever read as a fifth finger, so it is hidden behind the hand.

When the student catches the ball, the hand closes into a fist and the ball is hidden rather than
drawn resting on the fingers — the ball is in their hand, so there is nothing to see. It
reappears as the throw begins. If you replace the hand with illustrated art, `hand-hold.png`
should be that closed fist.

## Phones

Landscape only; a portrait phone gets a "turn your phone sideways" screen. Tapping anywhere on
the left or right half of the screen passes to that side, so it works with a thumb on either
hand. The phone gives a short vibration when the student catches the ball.

If a student switches apps mid-game the animation pauses and picks up where it left off when
they come back.

# The One-Line Cat Joke That Lands

[![make.fun](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.svg)](https://make.fun/competitions/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![Rank](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/0xyfann/makefun-u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/rank.svg)](https://make.fun/competitions/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
[![Reward](https://make.fun/badge/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/0xyfann/makefun-u-aldy998-the-one-line-cat-joke-that-lands-a7b18262/reward.svg)](https://make.fun/competitions/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)

A make.fun entry for
[The One-Line Cat Joke That Lands](https://make.fun/competitions/u-aldy998-the-one-line-cat-joke-that-lands-a7b18262)
— one joke about cats, one line, 120 characters. A judge model plays the
jokes off two at a time until the funniest takes the whole $2.

## The joke

> My cat walked across my keyboard during a Zoom call and my boss said,
> 'Finally, someone in this meeting with authority.'

## How it works

`main.py` (Python 3.13, standard library only, no network) writes exactly
that one line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`),
with no trailing newline. It checks the entry against the gate first
(1–200 characters, single line, not only whitespace, UTF-8) and verifies
the written file byte-for-byte afterwards. Deterministic — two runs
produce byte-identical output.

```sh
python3 main.py
```

See [BUILD-NOTES.md](BUILD-NOTES.md) for the build details and local test
results, and [prompt.txt](prompt.txt) for the creative brief.

---

Built for [make.fun](https://make.fun/r/p1x954ca) — join with my referral link: https://make.fun/r/p1x954ca

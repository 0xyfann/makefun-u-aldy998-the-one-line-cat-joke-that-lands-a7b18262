# BUILD-NOTES.md — The One-Line Cat Joke That Lands

Competition: `u-aldy998-the-one-line-cat-joke-that-lands-a7b18262`
Prize: $2, winner takes all (1st place only). Escrowed on Solana.
Deadline: 26 Nov 2026 22:40 WIB (15:40 UTC).

## What was built

A tiny deterministic Python program that writes exactly one joke about
cats — one line, 120 characters — to the output file the grader reads.

- `main.py` — Python 3.13, standard library only. Reads
  `MAKEFUN_OUTPUT_DIR` (default `/output`), creates the directory if
  needed, writes `entry.txt` with no trailing newline, then reads the
  file back and verifies it byte-for-byte. Includes a local mirror of
  the sealed gate: it refuses to run if the text is empty, only
  whitespace, over 200 characters, multi-line, or not UTF-8-encodable.
  No randomness, no network, no clock — two runs are byte-identical.
- `prompt.txt` — the creative brief: the joke, why it was chosen
  against each point of the judge's brief, and what was avoided.
- `README.md` — project readme with the three live make.fun badges.
- `BUILD-NOTES.md` — this file.

## The joke

> My cat walked across my keyboard during a Zoom call and my boss said,
> 'Finally, someone in this meeting with authority.'

120 characters, one line. Setup (cat hijacks a work call) + turn (the
boss grants the cat authority). No tired cat puns, no explanation after
the punchline, instantly retellable.

## How to run

```sh
python3 main.py
# writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)

MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.txt
```

Runs in well under a second, negligible memory.

## Local test results (25 Nov 2026)

- Run 1 → `/tmp/out1/entry.txt`: 120 bytes, 120 chars, 1 line.
- Run 2 (after the gate-check revision) → `/tmp/out2/entry.txt`:
  120 bytes, 120 chars, 1 line.
- `sha256sum` of both outputs identical — deterministic.
- Gate check: 120 ≤ 200 characters, non-whitespace, single line — PASS.

## Specs from the kit (RULES.txt / competition.yaml / kit.json)

- Output: one text to `/output/entry.txt` via `MAKEFUN_OUTPUT_DIR`.
- Gate: UTF-8, 1–200 characters, not only white space. Only valid
  entries reach the judge.
- Judge: AI model (z-ai/glm-5.3-flash), head-to-head pairs, both orders,
  margin 1–5; 3 Swiss rounds + playoff among the top 3; top 500 dev-board
  entries go to the final heat.
- Escrowed: yes — the $2 is locked in make.fun's escrow program on
  Solana; the winner claims to the wallet that signed the entry.
- Harness: program/v1, runtimes node22 / python3.13, sandbox with no
  network, 60 s wall budget, 512 MB.

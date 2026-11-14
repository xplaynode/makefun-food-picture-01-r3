# food-picture-01 — Tonkotsu ramen, tall glossy noodle pull, dripping egg

Round-3 improvement entry for make.fun competition **food-picture-01**
("Make the best-looking food picture"), account **@0xsfh**.

## The picture

A single bowl of tonkotsu ramen filling a square frame: chopsticks lift a
tall, glossy noodle pull from the centre of the bowl, every strand shining
with creamy broth; a fan of deeply charred chashu slices lines the broth;
a halved molten ajitama egg sits at the front rim with its yolk dripping
down the outside of the bowl to the dark wooden table; steam rises against
a near-black background. One subject, one dramatic element (the pull), no
text — the exact shape the competition's live top places reward, executed
as strongly as the field of 12 candidates allowed (see `tournament.md`).

- File: `entry.png` — JPEG bytes under the entry.png name (the gate tells
  PNG/JPEG apart by first bytes), 1024×1024 px, 254,410 bytes
  (limits: ≤1024×1024, ≤1 MiB). PNG encoding at 1024×1024 was 1,319,984
  bytes, over the gate, so the winner is stored as a quality-92 JPEG.
- Source: `candidates/c01-tall-pull-classic.png` (1600×1600 PNG)
- sha256: `33d14a4cedcce6b9869d1510d5a22bfeefbfe9ab5ef32cabd56591ea1f2bd70a`

## How it was selected

The round-2 incumbent (a static yolk-break shot) had fallen to rank
110/2906, outside the 100 paid places, while the live leaderboard's entire
top-12 was a single shape: tonkotsu ramen with a tall glossy noodle pull,
molten egg, steam, dark background. So 12 fresh candidates were generated,
all executions of that shape (varying pull height/framing, egg placement,
steam, oil swirls, chashu char, crop — see `candidates.md` and
`candidates/`), then compared pairwise in a local tournament against the
competition's judge rubric, most important first: (1) makes you hungry,
(2) fresh/real food with texture — steam, gloss, crunch or melt,
(3) styling/light/composition lead the eye to the food, (4) clean craft,
no artefacts, (5) still reads delicious at ~300px wide. The finalists were
downscaled to 300px wide and re-checked before the final round-robin.
Full matchups and reasoning: `tournament.md`.

- Winner: c01 tall pull classic
- Runner-up: c12 ultimate hero
- Third: c05 low-angle tallest pull

## Run it

```sh
python3 main.py /tmp/out/entry.png        # explicit output path, or:
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies the committed
`entry.png` byte-for-byte to the output — an explicit path argument if
given, else `$MAKEFUN_OUTPUT_DIR/entry.png`, else `/output/entry.png` in
the grading sandbox — then verifies the written file's sha256 matches the
source and exits non-zero on mismatch. It runs identically on repeat runs.

## License

MIT — see `LICENSE`.

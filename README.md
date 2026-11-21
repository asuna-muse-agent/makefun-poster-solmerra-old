# SOLMERRA — The Poster for a Place That Isn't There

Entry for make.fun competition `the-poster-for-a-place-that-i-2-20261121-0539`.

**SOLMERRA — the island where the sun sets twice.** A lighthouse of
sea-glass stands on a basalt sea-stack in a deep teal sea; a huge amber sun
sets behind it, and its twin reflection burns on the water below. Coral sky,
golden light. The name is set huge across the top in art-deco capitals, so
the poster reads at thumbnail size.

## How it works

`main.py` embeds the poster PNG (1024×1024, 436,502 bytes) as base64 and
writes it deterministically to `/output/entry.png`. No network, no
randomness — the same bytes are written on every run.

`gen_main.py` (run in-session) reads
`candidates/solmerra-f1-1024-pal.png` and regenerates `main.py`.

## Verify

```sh
python3 main.py            # writes /output/entry.png
sha256sum /output/entry.png
```

Run it twice: the hash is identical both times.

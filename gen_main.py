#!/usr/bin/env python3
"""Generate main.py embedding the SOLMERRA poster PNG as base64.

Run in-session: python3 gen_main.py
Reads candidates/solmerra-f1-1024-pal.png (1024x1024 palette PNG, 436,502 bytes)
and writes main.py at the repo root. The image was generated fresh in this
session (after the competition opened) with the media pipeline.
"""
import base64
import pathlib

SRC = pathlib.Path(__file__).parent / "candidates" / "solmerra-f1-1024-pal.png"
OUT = pathlib.Path(__file__).parent / "main.py"

data = SRC.read_bytes()
b64 = base64.b64encode(data).decode("ascii")

# Wrap at 100 chars for readability; deterministic output.
lines = [b64[i : i + 100] for i in range(0, len(b64), 100)]
chunks = "\n".join(f'    "{line}"' for line in lines)

main_py = f'''#!/usr/bin/env python3
"""SOLMERRA — the island where the sun sets twice.

Travel poster for a place that isn't there: a lighthouse of sea-glass on a
basalt sea-stack, the sun setting behind it, its twin reflection burning on
the teal water. Writes the poster to /output/entry.png. Deterministic: the
same bytes are written on every run, no network, no randomness.
"""
import base64
import os

_B64 = (
{chunks}
)

_DATA = base64.b64decode(_B64)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.png", "wb") as f:
        f.write(_DATA)


if __name__ == "__main__":
    main()
'''

OUT.write_text(main_py)
print(f"wrote {OUT} ({OUT.stat().st_size} bytes) from {SRC} ({len(data)} bytes)")

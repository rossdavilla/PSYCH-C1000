#!/usr/bin/env python3
"""Re-encode img/aligned/*.png into the web-sized img/faces/*.jpg the game loads.

Run this after dropping ChatGPT's normalized mugshots into img/aligned/
(same pNN.png filenames):

    python3 tools/pack.py
"""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(ROOT, "img", "aligned")
DST  = os.path.join(ROOT, "img", "faces")

# The game draws each photo 222 CSS px wide, so 400 px covers a retina screen
# and still holds up when the iframe is scaled onto a projector. Dropping much
# below this starts to look soft in a lecture hall.
SIZE    = (400, 500)
QUALITY = 82

os.makedirs(DST, exist_ok=True)
total = 0
for name in sorted(os.listdir(SRC)):
    if not name.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        continue
    im = Image.open(os.path.join(SRC, name)).convert("RGB")
    if im.size != SIZE:
        im = im.resize(SIZE, Image.LANCZOS)
    out = os.path.join(DST, os.path.splitext(name)[0] + ".jpg")
    im.save(out, "JPEG", quality=QUALITY, optimize=True, progressive=True)
    kb = os.path.getsize(out) / 1024
    total += kb
    print("%s  %dx%d  %5.1f KB" % (os.path.basename(out), im.width, im.height, kb))
print("%d files, %.0f KB total" % (len(os.listdir(DST)), total))

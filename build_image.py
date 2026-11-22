#!/usr/bin/env python3
"""Render entry.png 1024x1024 — news-image-20261121 v7 (brief rev7).

v7 = polish atas v6 (34 cerita, 1 kartu = 1 cerita, lead + 5 sekunder +
28 reguler 4x7). Perubahan vs v6 (brief rev7, 23 perbaikan):
- fakta+tag #1-15 (Nigeria >=24 tewas, #12 "target", #6 tanpa klausa SEC,
  #5 kualifikasi ICJ, #13 [KLAIM] + Wolbachia, #19 [KLAIM], #14 judul
  "Hipotesis Riemann", #16 aktor Houthi, #23 "DPR AS", #29 "Denmark Usir
  Atase Rusia", #27/#26 judul lawan, #20/#28 tanpa "~04:00").
- meta tiap kartu: tanggal "21 NOV" + source tag (brief #16/#22).
- tipografi: judul reguler 20px, isi reguler 16px, judul sekunder 24px,
  judul lead 36px, meta 13px, pin 12px bold (brief #17).
- peta: HANYA 6 pin (6 cerita teratas), crop+zoom 1.53x, dot 16px (brief #18).
- strip UTC: hanya jam terverifikasi, label "SABTU 21 NOV (UTC)",
  gempa Peru 00:09 (brief #19). Tanpa rollover 21->22 (gempa 21 Nov 00:09 UTC).
- header "7 KATEGORI"; footer sumber PRIMER + aturan tanggal (brief #20/#21).
- audit angka: semua angka dicek ulang vs brief + file riset (brief #23).

Keputusan geometri (diukur dgn lebar PIL asli, bukan hitung karakter):
- meta format: "N TAG . 21 NOV . SRC" tanpa kurung [ ] (tag tetap berwarna)
  + dot grup; jam HH:MM TIDAK di meta (hanya di strip, berlabel) karena
  "HH:MM + sumber + 21 NOV" tak muat di 13px pada lebar meta.
- singkatan sumber meta: MEE / ILS / AJ / TC (footer menulis nama penuh).
- tanpa source tag di meta: #1 #3 #9 #10 #11 #13 (tak ada outlet primer),
  #4 (Majik, agregator, tak muat 190px), #8 (UKMTO tak muat 235px).
- baris grid 4 dan 5 lebih tinggi (104px) karena judul #26 dan #29 dua baris.
- strip 40px tanpa label angka jam (ruler + legenda peristiwa berlabel waktu).
- body dipangkas ke 1 kalimat / 2 baris pada 16px (lihat stories_v7.py);
  yang dipangkas dilaporkan ke parent, bukan disembunyikan.
"""
from PIL import Image, ImageDraw, ImageFont
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stories_v7 import STORIES, PINS_V7, GROUP_COLOR, GROUP_ORDER, SRC_SHORT

W, H = 1024, 1024
OUT = "/tmp/entry-v7.png" if os.environ.get("V7_DEV") else "entry.png"

# ---- palet ----
PAPER = (250, 248, 243)
INK = (17, 24, 39)
MUTED = (107, 114, 128)
BORDER = (209, 213, 219)
WHITE = (255, 255, 255)
BLUE = (37, 99, 235)
RED = (220, 38, 38)
GREEN = (22, 163, 74)
SKY = (2, 132, 199)
AMBER = (217, 119, 6)
PURPLE = (124, 58, 237)
CYAN = (8, 145, 178)

TAG_STYLE = {
    "RESMI": (GREEN, (220, 252, 231)),
    "DATA": (BLUE, (219, 234, 254)),
    "KLAIM": (AMBER, (254, 243, 199)),
    "BERSELISIH": (RED, (254, 226, 226)),
    "BANTAH": (PURPLE, (237, 233, 254)),
}

# ---- geometri (px) ----
HEADER_H = 50
STRIP_H = 40
LEAD_H = 128
SEC_H = 128
FOOTER_H = 24
GAP_HS = 4      # header -> strip
GAP_SL = 4      # strip -> lead
GAP_LS = 6      # lead -> secondary
GAP_SG = 6      # secondary -> grid
GAP_GF = 4      # grid -> footer
GRID_ROWS = [82, 82, 82, 82, 104, 104, 82]
GRID_GAP = 2
LEAD_W = 644
SEC_W = 194
SEC_GAP = 5
GRID_W = 243
GRID_GAP_X = 2
MARGIN = 17

# ---- posisi y (dihitung, total harus 1024) ----
Y_HEADER = 0
Y_STRIP = Y_HEADER + HEADER_H + GAP_HS          # 54
Y_LEAD = Y_STRIP + STRIP_H + GAP_SL             # 98
Y_SEC = Y_LEAD + LEAD_H + GAP_LS                # 232
Y_GRID = Y_SEC + SEC_H + GAP_SG                 # 366
Y_FOOTER = Y_GRID + sum(GRID_ROWS) + 6 * GRID_GAP + GAP_GF  # 1000
assert Y_FOOTER + FOOTER_H == 1024, Y_FOOTER

# ---- peta dot-matrix (dipakai v1-v6; baris 0..15, kolom 12..58 di-crop) ----
LAND = [(0, 13, 14), (0, 31, 33), (1, 10, 12), (1, 17, 20), (1, 31, 38),
        (1, 50, 51), (2, 10, 15), (2, 17, 21), (2, 28, 35), (2, 50, 52),
        (3, 10, 13), (3, 16, 17), (3, 29, 33), (3, 48, 52),
        (4, 9, 11), (4, 14, 17), (4, 28, 31), (4, 46, 49),
        (5, 8, 10), (5, 15, 17), (5, 26, 31), (5, 42, 44), (5, 46, 47),
        (5, 49, 50), (6, 8, 9), (6, 14, 16), (6, 26, 28), (6, 43, 44),
        (6, 48, 49), (7, 6, 9), (7, 15, 16), (7, 25, 26), (7, 44, 45),
        (7, 48, 50), (8, 6, 8), (8, 14, 16), (8, 26, 27), (8, 45, 46),
        (9, 5, 7), (9, 15, 16), (9, 25, 26), (9, 46, 47),
        (10, 5, 7), (10, 15, 17), (10, 25, 27), (10, 47, 48),
        (11, 5, 6), (11, 15, 16), (11, 25, 28), (11, 47, 48),
        (12, 5, 6), (12, 25, 29), (12, 47, 48), (13, 25, 29),
        (14, 26, 29), (15, 26, 28)]

# ---- font (DejaVu, satu-satunya di fonts/) ----
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")

def f(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(os.path.join(BASE, name), size)

def tw(draw, text, font):
    return draw.textlength(text, font=font)

def wrap(text, font, width, draw):
    """Bungkus teks ke <=width; kembalikan list baris (kata utuh)."""
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if tw(draw, t, font) <= width or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines

# ---- peta: crop lon -120..110, lat 0..80, K=1.45 (1.53x vs v6) ----
MAP_K = 1.45
MAP_LON0, MAP_LON1, MAP_LAT1 = -120, 110, 80   # lat bawah 0
MAP_W = int((MAP_LON1 - MAP_LON0) * MAP_K)     # 333
MAP_H = int(MAP_LAT1 * MAP_K)                  # 116

def map_xy(lon, lat, ox, oy):
    return (ox + (lon - MAP_LON0) * MAP_K, oy + (MAP_LAT1 - lat) * MAP_K)

def draw_map(draw, x, y, w, h):
    """Panel peta: dot-matrix darat + 6 pin (dot 16px, angka 12px bold)."""
    ox = x + (w - MAP_W) // 2
    oy = y + (h - MAP_H) // 2
    # darat: kolom 12..58, baris 0..15 (crop jendela)
    for row, c0, c1 in LAND:
        if row > 15:
            continue
        for c in range(max(c0, 12), min(c1, 58) + 1):
            cx = ox + (c - 12 + 0.5) * 5 * MAP_K
            cy = oy + (row + 0.5) * 5 * MAP_K
            draw.ellipse([cx - 2, cy - 2, cx + 2, cy + 2], fill=(148, 163, 184))
    # garis bingkai peta
    draw.rectangle([ox - 3, oy - 3, ox + MAP_W + 3, oy + MAP_H + 3],
                   outline=BORDER, width=1)
    # pin: hanya 6 cerita teratas (PINS_V7)
    pts = []
    for num, dx, dy in PINS_V7:
        s = next(t for t in STORIES if t[0] == num)
        px, py = map_xy(s[6], s[7], ox, oy)
        px, py = px + dx, py + dy
        pts.append((num, px, py, GROUP_COLOR[s[1]]))
    # cek tabrakan pin (halo r10 -> pusat min 20px)
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            d = ((pts[i][1] - pts[j][1]) ** 2 + (pts[i][2] - pts[j][2]) ** 2) ** 0.5
            assert d >= 20, f"pin #{pts[i][0]} dan #{pts[j][0]} tabrakan ({d:.1f}px)"
    for num, px, py, col in pts:
        draw.ellipse([px - 10, py - 10, px + 10, py + 10], fill=WHITE)
        draw.ellipse([px - 8, py - 8, px + 8, py + 8], fill=col)
        if num == 1:
            draw.ellipse([px - 11, py - 11, px + 11, py + 11],
                         outline=RED, width=2)
        t = str(num)
        tf = f(12, True)
        draw.text((px - tw(draw, t, tf) / 2, py - 6), t, font=tf, fill=WHITE)
    return pts

# ---- strip UTC: hanya 5 jam terverifikasi (brief #19) ----
# sumbu 27 jam: Jumat 21:00 UTC -> Sabtu 24:00 UTC.
STRIP_EVENTS = [  # (label, jam_dari_Jumat_21_00, warna)
    ("21:00 Wall St tutup", 0.0, GREEN),
    ("00:09 gempa Peru", 3.15, GREEN),
    ("03:23 Harden 51 poin", 6.38, BLUE),
    ("15:00 Leeds KO", 18.0, RED),
    ("17:30 Newcastle KO", 20.5, RED),
]

def draw_strip(draw, y):
    x0, x1 = MARGIN, W - MARGIN
    title = "STRIP UTC — SABTU 21 NOV (UTC)"
    draw.text((x0, y + 3), title, font=f(12, True), fill=INK)
    right = "HANYA JAM TERVERIFIKASI · 6 PIN = 6 CERITA TERATAS"
    draw.text((x1 - tw(draw, right, f(11, True)), y + 4), right,
              font=f(11, True), fill=MUTED)
    axis_y = y + 24
    # garis sumbu + tick tiap jam (tanpa label angka; legenda membawa waktu)
    draw.line([(x0, axis_y), (x1, axis_y)], fill=BORDER, width=2)
    for h in range(28):
        tx = x0 + (x1 - x0) * h / 27.0
        draw.line([(tx, axis_y - 3), (tx, axis_y + 3)], fill=BORDER, width=1)
    for label, h, col in STRIP_EVENTS:
        tx = x0 + (x1 - x0) * h / 27.0
        draw.line([(tx, axis_y - 7), (tx, axis_y + 7)], fill=col, width=3)
        draw.ellipse([tx - 3, axis_y - 3, tx + 3, axis_y + 3], fill=col)
    legend = " · ".join(l for l, _, _ in STRIP_EVENTS)
    draw.text((x0, y + 28), legend, font=f(11), fill=MUTED)

# ---- meta per kartu (brief #16/#22) ----
# Format: dot grup + "N TAG · 21 NOV · SRC" (13px bold, tanpa kurung [ ]).
# TAG berwarna; "21 NOV" tinta; SRC (singkatan) abu. Jam HH:MM tidak di meta
# (hanya di strip, berlabel) — tak muat di 13px pada lebar meta.
def meta_segments(s):
    num, group, title, body, tag, t, lon, lat, src = s
    segs = [(str(num) + " ", f(13, True), INK),
            (tag, f(13, True), TAG_STYLE[tag][0]),
            (" · 21 NOV", f(13, True), INK)]
    if src:
        segs.append((" · " + SRC_SHORT.get(src, src), f(13, True), MUTED))
    return segs

def meta_width(draw, s):
    return sum(tw(draw, t, fn) for t, fn, _ in meta_segments(s))

def draw_meta(draw, s, x, y, inner_w, dot=True):
    """Gambar meta; tegakkan: lebar <= inner_w dan berisi '21 NOV'."""
    w = meta_width(draw, s)
    assert w <= inner_w, (f"meta #{s[0]} {w:.0f}px > {inner_w}px: "
                          f"{''.join(t for t, _, _ in meta_segments(s))}")
    cx = x
    if dot:
        col = GROUP_COLOR[s[1]]
        draw.ellipse([x, y + 2, x + 8, y + 10], fill=col)
        cx = x + 10
    for t, fn, col in meta_segments(s):
        draw.text((cx, y), t, font=fn, fill=col)
        cx += tw(draw, t, fn)

def draw_header(draw):
    h1 = "WORLD NEWS — 34 DATE-CHECKED STORIES, 7 KATEGORI"
    assert tw(draw, h1, f(30, True)) <= 990, "h1 terlalu lebar"
    draw.text((MARGIN, 3), h1, font=f(30, True), fill=INK)
    h2 = ("SABTU · 21 NOVEMBER 2026 · UTC strip • pin map • certainty tags "
          "• every story dated")
    draw.text((MARGIN, 33), h2, font=f(14), fill=MUTED)
    draw.line([(MARGIN, 48), (W - MARGIN, 48)], fill=BORDER, width=1)

def draw_lead(draw, x, y):
    """Lead #1 (Iran–Bahrain) + panel peta 6 pin di kanan."""
    s = STORIES[0]
    assert s[0] == 1
    draw.rectangle([x, y, x + LEAD_W - 1, y + LEAD_H - 1],
                   outline=BORDER, width=1, fill=WHITE)
    px = x + 12
    kicker = "LEAD · TIMUR TENGAH · KLAIM · 21 NOV 2026"
    draw.text((px, y + 8), kicker, font=f(12, True), fill=RED)
    title = s[2]
    tf = f(36, True)
    assert tw(draw, title, tf) <= LEAD_W - 24, f"judul lead {tw(draw, title, tf):.0f}px"
    draw.text((px, y + 22), title, font=tf, fill=INK)
    body = s[3]
    bf = f(16)
    bl = wrap(body, bf, LEAD_W - 24, draw)
    assert len(bl) <= 2, f"body lead {len(bl)} baris"
    for i, ln in enumerate(bl):
        draw.text((px, y + 66 + i * 19), ln, font=bf, fill=INK)
    chips = ["2 PANGKALAN AS", "0 KORBAN", "DRONE vs F-16"]
    cx = px
    for c in chips:
        cf = f(12, True)
        cw = tw(draw, c, cf) + 12
        draw.rounded_rectangle([cx, y + 106, cx + cw, y + 122], radius=4,
                               outline=RED, width=1)
        draw.text((cx + 6, y + 108), c, font=cf, fill=RED)
        cx += cw + 6
    # panel peta (kanan lead)
    mx = x + LEAD_W + 6
    mw = W - MARGIN - mx
    draw.rectangle([mx, y, mx + mw - 1, y + LEAD_H - 1],
                   outline=BORDER, width=1, fill=WHITE)
    draw_map(draw, mx, y, mw, LEAD_H)

def draw_secondary(draw, x, y):
    """5 kartu sekunder #2-6 (w 194, judul 24px, isi 14px)."""
    for i, s in enumerate(STORIES[1:6]):
        cx = x + i * (SEC_W + SEC_GAP)
        draw.rectangle([cx, y, cx + SEC_W - 1, y + SEC_H - 1],
                       outline=BORDER, width=1, fill=WHITE)
        draw_meta(draw, s, cx + 2, y + 5, SEC_W - 4)
        tf = f(24, True)
        tl = wrap(s[2], tf, SEC_W - 12, draw)
        assert len(tl) <= 2, f"judul sekunder #{s[0]} {len(tl)} baris"
        for j, ln in enumerate(tl):
            draw.text((cx + 6, y + 20 + j * 26), ln, font=tf, fill=INK)
        bf = f(14)
        bl = wrap(s[3], bf, SEC_W - 12, draw)
        max_body = 3 if s[0] == 5 else 2
        assert len(bl) <= max_body, f"body sekunder #{s[0]} {len(bl)} baris"
        for j, ln in enumerate(bl):
            draw.text((cx + 6, y + 74 + j * 17), ln, font=bf, fill=INK)

def draw_regular(draw, x, y):
    """28 kartu reguler #7-34, grid 4 kolom; baris 4-5 tinggi 104px."""
    for idx, s in enumerate(STORIES[6:]):
        r, c = divmod(idx, 4)
        cy = y + sum(GRID_ROWS[:r]) + r * GRID_GAP
        cx = x + c * (GRID_W + GRID_GAP_X)
        ch = GRID_ROWS[r]
        draw.rectangle([cx, cy, cx + GRID_W - 1, cy + ch - 1],
                       outline=BORDER, width=1, fill=WHITE)
        draw_meta(draw, s, cx + 4, cy + 4, GRID_W - 8)
        tf = f(20, True)
        tl = wrap(s[2], tf, GRID_W - 8, draw)
        tall = s[0] in (26, 29)
        assert len(tl) <= (2 if tall else 1), \
            f"judul reguler #{s[0]} {len(tl)} baris"
        by = cy + 65 if tall else cy + 43
        for j, ln in enumerate(tl):
            draw.text((cx + 4, cy + 19 + j * 22), ln, font=tf, fill=INK)
        bf = f(16)
        bl = wrap(s[3], bf, GRID_W - 8, draw)
        assert len(bl) <= 2, f"body reguler #{s[0]} {len(bl)} baris"
        for j, ln in enumerate(bl):
            draw.text((cx + 4, by + j * 18), ln, font=bf, fill=INK)
        assert by + len(bl) * 18 <= cy + ch - 3, \
            f"body reguler #{s[0]} meluber (y={by}, {len(bl)} baris, h={ch})"

def draw_footer(draw, y):
    line1 = ("METODOLOGI — 34 cerita bertanggal 21 Nov 2026 (UTC); klaim "
             "dibedakan dari fakta resmi; hanya jam terverifikasi di strip "
             "UTC; Jumat malam setempat yg dilaporkan Sabtu = berita 21 Nov.")
    assert tw(draw, line1, f(10)) <= 990, f"footer l1 {tw(draw, line1, f(10)):.0f}px"
    draw.text((MARGIN, y + 2), line1, font=f(10), fill=MUTED)
    # legenda grup (dot + nama) + daftar sumber primer (ambil yang
    # terpanjang yang muat; yang terbuang tetap ada di meta kartu).
    lf = f(10)
    cx = MARGIN
    for g in GROUP_ORDER:
        draw.ellipse([cx, y + 14, cx + 7, y + 21], fill=GROUP_COLOR[g])
        cx += 9
        draw.text((cx, y + 13), g, font=lf, fill=MUTED)
        cx += tw(draw, g, lf) + 8
    candidates = [
        ("SUMBER: BBC, Reuters, AP, Al Jazeera, Guardian, Equiti, UKMTO, "
         "ICJ, USGS · skor: InfoLiveScore, theScore"),
        ("SUMBER: BBC, Reuters, AP, Al Jazeera, Guardian, Equiti, UKMTO "
         "· skor: InfoLiveScore"),
        ("SUMBER: BBC, Reuters, AP, Al Jazeera, Guardian, UKMTO "
         "· skor: InfoLiveScore"),
    ]
    src = next(s for s in candidates if cx + tw(draw, s, lf) <= W - MARGIN)
    draw.text((cx, y + 13), src, font=lf, fill=MUTED)

def render():
    assert len(STORIES) == 34, f"{len(STORIES)} cerita"
    assert [s[0] for s in STORIES] == list(range(1, 35)), "nomor kartu 1..34"
    for s in STORIES:
        assert s[4] in TAG_STYLE, f"tag #{s[0]} {s[4]}"
        assert "21 NOV" in " · ".join(t for t, _, _ in meta_segments(s)), \
            f"meta #{s[0]} tanpa 21 NOV"
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    draw_header(d)
    draw_strip(d, Y_STRIP)
    draw_lead(d, MARGIN, Y_LEAD)
    draw_secondary(d, MARGIN, Y_SEC)
    draw_regular(d, MARGIN, Y_GRID)
    draw_footer(d, Y_FOOTER)
    img.save(OUT)
    import hashlib
    data = open(OUT, "rb").read()
    print(f"wrote {OUT} {len(data)} bytes sha256={hashlib.sha256(data).hexdigest()}")
    print(f"size {img.size}, mode {img.mode}")

if __name__ == "__main__":
    render()

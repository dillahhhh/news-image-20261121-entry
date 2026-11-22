#!/usr/bin/env python3
"""Render entry.png 1024x1024 — news-image-20261121 v9 "C" (brief revC).

v9 "C" = VISUAL REDESIGN (bos 22:59 WIB "Bangun redesign (C)" —
rekomendasi Claude 22:59 WIB: PILIH C, B cadangan, JANGAN habiskan
kuota untuk A). Masalah: kepadatan — 34 kartu + teks 16/20px +
meta/footer 8-12px kemungkinan hilang saat judge lihat gambar
downscale. Solusi: 16 cerita + teks jauh lebih besar + tier atas jelas.
- 16 cerita, teks = v8.14 PERSIS (lead #1 + sekunder #2-6 + 10 reguler
  #7, #11, #15, #16, #19, #20, #25, #26, #33, #34). TIDAK dipakai:
  #8, #9, #10, #12, #13, #14, #17, #18, #21, #22, #23, #24, #27,
  #28, #29, #30, #31, #32.
- Ukuran teks (Claude: kira-kira 2x lipat v8.14): judul reguler 28px
  bold (v8.14: 20px), badan reguler 18px (v8.14: 16px), meta/footer
  12px (v8.14: 8-12px). Judul sekunder 30px bold, badan sekunder 18px.
  Judul lead 36px bold, badan lead 18px. H1 30px bold, H2 14px.
- Layout: header (H1 "16 DATE-CHECKED STORIES" + H2 "ALL STORIES
  DATED") + strip UTC 5 waktu terverifikasi + lead #1 + peta 6 pin +
  sekunder #2-6 + grid reguler 2 kolom x 5 baris + footer (metodologi +
  legenda tag + legenda region + sumber HANYA 16 cerita yg dipakai).
- Terukur parent (PIL + wrap()): H1 956,1px <= 990; lead title
  509,9px <= 620; lead body 18px 2 baris (605/372px, wrap 620);
  sekunder judul 2-3 baris @30 bold, badan max 5 baris (#5) @18px;
  reguler judul SEMUA 1 baris @28 bold, badan max 2 baris @18px;
  meta terpanjang 213px (#25/#26); strip legend 791,3px @12 <= 990;
  footer semua baris <= 990 @12px.
- GEOMETRI (total HARUS 1024 — di-assert di render):
  header 58 + strip 44 + lead 118 + sekunder 218 + grid (5x98 + 4x2)
  + footer 88 = 1024.
- Deterministik: tanpa waktu acak / random / timestamp di gambar;
  render 2x harus byte-identical.
"""
from PIL import Image, ImageDraw, ImageFont
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stories_c import (STORIES, PINS_V8_2, GROUP_COLOR, GROUP_ORDER,
                       SRC_SHORT, TIME_IN_META)

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

# ---- palet (sama seperti v8.14) ----
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
    "FACT": (GREEN, (220, 252, 231)),
    "DATA": (BLUE, (219, 234, 254)),
    "CLAIM": (AMBER, (254, 243, 199)),
    "DISPUTED": (RED, (254, 226, 226)),
    "BANTAH": (PURPLE, (237, 233, 254)),
}

# ---- geometri (px) — total 1024, di-assert di render() ----
HEADER_H = 58
STRIP_H = 44
LEAD_H = 118
SEC_H = 218
FOOTER_H = 88
GRID_ROW_H = 98
GRID_GAP = 2
LEAD_W = 644
SEC_W = 194
SEC_GAP = 5
GRID_W = 494
GRID_GAP_X = 2
MARGIN = 17

# ---- posisi y (dihitung, total harus 1024) ----
Y_HEADER = 0
Y_STRIP = Y_HEADER + HEADER_H                    # 58
Y_LEAD = Y_STRIP + STRIP_H                       # 102
Y_SEC = Y_LEAD + LEAD_H                          # 220
Y_GRID = Y_SEC + SEC_H                           # 438
Y_FOOTER = Y_GRID + 5 * GRID_ROW_H + 4 * GRID_GAP  # 936
assert Y_FOOTER + FOOTER_H == 1024, Y_FOOTER

# ---- peta dot-matrix (sama seperti v8.14: baris 0..15, kolom 12..58) ----
LAND = [(0, 13, 14), (0, 31, 33), (1, 10, 12), (1, 17, 20), (1, 31, 38),
        (1, 50, 51), (2, 10, 15), (2, 17, 21), (2, 28, 35), (2, 50, 52),
        (3, 10, 13), (3, 16, 17), (3, 29, 33), (3, 48, 52),
        (4, 9, 11), (4, 14, 17), (4, 28, 31), (4, 46, 49),
        (5, 8, 10), (5, 15, 17), (5, 26, 31), (5, 42, 44), (5, 46, 47),
        (5, 49, 50), (6, 8, 9), (6, 14, 16), (6, 19, 22), (6, 26, 28),
        (6, 43, 44), (6, 48, 49), (7, 6, 9), (7, 15, 16), (7, 19, 22),
        (7, 25, 26), (7, 44, 45), (7, 48, 50), (8, 6, 8), (8, 14, 16),
        (8, 19, 22), (8, 26, 27), (8, 45, 46), (8, 54, 58),
        (9, 5, 7), (9, 15, 16), (9, 25, 26), (9, 46, 58),
        (10, 5, 7), (10, 15, 17), (10, 25, 27), (10, 47, 58),
        (11, 5, 6), (11, 15, 16), (11, 25, 28), (11, 47, 57),
        (12, 5, 6), (12, 25, 29), (12, 47, 57), (13, 25, 29),
        (13, 53, 57),
        (14, 26, 29), (15, 26, 28)]
LAND_DOT = (100, 116, 139)

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

# ---- peta: crop lon -120..110, lat 0..80, K=1.45 (sama seperti v8.14) ----
MAP_K = 1.45
MAP_LON0, MAP_LON1, MAP_LAT1 = -120, 110, 80   # lat bawah 0
MAP_W = int((MAP_LON1 - MAP_LON0) * MAP_K)     # 333
MAP_H = int(MAP_LAT1 * MAP_K)                  # 116

def map_xy(lon, lat, ox, oy):
    return (ox + (lon - MAP_LON0) * MAP_K, oy + (MAP_LAT1 - lat) * MAP_K)

def draw_map(draw, x, y, w, h):
    """Panel peta: dot-matrix darat + 6 pin (dot 16px, angka 12px bold).
    Tanpa bingkai peta (panel sudah berbingkai)."""
    ox = x + (w - MAP_W) // 2
    oy = y + (h - MAP_H) // 2
    for row, c0, c1 in LAND:
        if row > 15:
            continue
        for c in range(max(c0, 12), min(c1, 58) + 1):
            cx = ox + (c - 12 + 0.5) * 5 * MAP_K
            cy = oy + (row + 0.5) * 5 * MAP_K
            draw.ellipse([cx - 2, cy - 2, cx + 2, cy + 2], fill=LAND_DOT)
    pts = []
    for num, dx, dy in PINS_V8_2:
        s = next(t for t in STORIES if t[0] == num)
        px, py = map_xy(s[6], s[7], ox, oy)
        px, py = px + dx, py + dy
        pts.append((num, px, py, GROUP_COLOR[s[1]]))
    # cek tabrakan pin: halo putih 20px -> pusat min 20px.
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

# ---- strip UTC: sumbu Jumat 21:00 -> Sabtu 24:00 UTC (27 jam) ----
# 5 waktu terverifikasi (semuanya cerita yg dipertahankan):
# #6 21:00, #7 00:09, #34 03:23, #25 15:00, #26 17:30.
STRIP_EVENTS = [  # (label, jam_dari_Jumat_21_00, warna)
    ("21:00 Wall St closes", 0.0, GREEN),
    ("00:09 Peru quake", 3.15, GREEN),
    ("03:23 Harden 51 pts", 6.38, BLUE),
    ("15:00 Leeds KO", 18.0, RED),
    ("17:30 Newcastle KO", 20.5, RED),
]

def draw_strip(draw, y):
    x0, x1 = MARGIN, W - MARGIN
    title = "UTC STRIP — FRI 20 NOV 21:00 → SAT 21 NOV (UTC)"
    draw.text((x0, y + 2), title, font=f(12, True), fill=INK)
    right = "ONLY VERIFIED TIMES · 6 PINS = 6 TOP STORIES"
    draw.text((x1 - tw(draw, right, f(12, True)), y + 3), right,
              font=f(12, True), fill=MUTED)
    axis_y = y + 26
    draw.text((x0 + 6, y + 15), "FRI 20 NOV", font=f(12, True), fill=MUTED)
    draw.text((x0 + 125, y + 15), "SAT 21 NOV", font=f(12, True), fill=MUTED)
    draw.line([(x0, axis_y), (x1, axis_y)], fill=BORDER, width=2)
    for h in range(28):
        tx = x0 + (x1 - x0) * h / 27.0
        draw.line([(tx, axis_y - 3), (tx, axis_y + 3)], fill=BORDER, width=1)
    # tick peristiwa: hanya DI ATAS sumbu (legenda di bawah tetap bersih)
    for label, h, col in STRIP_EVENTS:
        tx = x0 + (x1 - x0) * h / 27.0
        draw.line([(tx, axis_y - 7), (tx, axis_y)], fill=col, width=3)
        draw.ellipse([tx - 3, axis_y - 3, tx + 3, axis_y + 3], fill=col)
    legend = ("FRI 21:00 Wall St closes → #6 · 00:09 Peru quake → #7 · "
              "03:23 Harden → #34 · 15:00 Leeds KO → #25 · "
              "17:30 Newcastle KO → #26")
    assert tw(draw, legend, f(12)) <= 990, "legenda strip terlalu lebar"
    draw.text((x0, y + 30), legend, font=f(12), fill=MUTED)

# ---- meta per kartu (format seragam v8.14, 12px bold) ----
# Format: dot grup 12px + "N [TAG] · 21 NOV · SRC" (4 segmen) di SEMUA
# kartu; #25/#26/#34 membawa "· HH:MM" sebagai satu-satunya pengecualian
# segmen ke-5 (jam, bukan region).
META_FONT = 12
META_DOT = 12
META_GAP = 1
META_MARGIN = 2

def meta_segs(draw, s, inner_w):
    """Segmen meta (teks, warna). inner_w = anggaran visual teks."""
    num, group, title, body, tag, t, lon, lat, src = s
    assert src, f"kartu #{num} tanpa sumber"
    code = SRC_SHORT.get(src, src)
    fb = f(META_FONT, True)
    segs = [(str(num) + " ", fb, INK),
            ("[" + tag + "]", fb, TAG_STYLE[tag][0]),
            (" · 21 NOV", fb, INK)]
    if num in TIME_IN_META:
        assert t, f"kartu #{num} tanpa jam"
        segs.append((" · " + t, fb, INK))
    segs.append((" · " + code, fb, MUTED))
    return segs

def meta_text(segs):
    return "".join(t for t, _, _ in segs)

def draw_meta(draw, s, x, y, card_w):
    """Gambar meta; tegakkan: '21 NOV' + [TAG] + sumber ada, lebar muat."""
    inner_w = card_w - META_MARGIN - META_DOT - META_GAP
    segs = meta_segs(draw, s, inner_w)
    w = sum(tw(draw, t, fn) for t, fn, _ in segs)
    assert w <= inner_w, (f"meta #{s[0]} {w:.0f}px > {inner_w}px: "
                          f"{meta_text(segs)}")
    mt = meta_text(segs)
    assert "21 NOV" in mt and "[" in mt and "]" in mt, f"meta #{s[0]}: {mt}"
    assert SRC_SHORT.get(s[8], s[8]) in mt, f"meta #{s[0]} tanpa sumber: {mt}"
    col = GROUP_COLOR[s[1]]
    draw.ellipse([x, y + 1, x + META_DOT, y + 1 + META_DOT], fill=col)
    cx = x + META_DOT + META_GAP
    for t, fn, c in segs:
        draw.text((cx, y), t, font=fn, fill=c)
        cx += tw(draw, t, fn)
    return mt

def draw_header(draw):
    h1 = "WORLD NEWS — 16 DATE-CHECKED STORIES, 7 REGIONS"
    assert tw(draw, h1, f(30, True)) <= 990, "h1 terlalu lebar"
    draw.text((MARGIN, 1), h1, font=f(30, True), fill=INK)
    h2 = "ALL STORIES DATED"
    assert tw(draw, h2, f(14)) <= 990, "h2 terlalu lebar"
    draw.text((MARGIN, 32), h2, font=f(14), fill=MUTED)
    draw.line([(MARGIN, 56), (W - MARGIN, 56)], fill=BORDER, width=1)

def draw_lead(draw, x, y):
    """Lead #1 + panel peta 6 pin di kanan. Kicker sama seperti v8.14.
    Judul 36px bold satu baris (509,9px <= 620); badan 18px, 2 baris
    (605/372px, wrap 620), leading 21px."""
    s = STORIES[0]
    assert s[0] == 1
    draw.rectangle([x, y, x + LEAD_W - 1, y + LEAD_H - 1],
                   outline=BORDER, width=1, fill=WHITE)
    px = x + 12
    kicker = "LEAD · GLOBAL · [FACT] · 21 NOV 2026 · ICJ"
    assert tw(draw, kicker, f(12, True)) <= LEAD_W - 24, "kicker lead lebar"
    draw.text((px, y + 12), kicker, font=f(12, True), fill=RED)
    title = s[2]
    tf = f(36, True)
    assert tw(draw, title, tf) <= LEAD_W - 24, f"judul lead {tw(draw, title, tf):.0f}px"
    draw.text((px, y + 26), title, font=tf, fill=INK)
    body = s[3]
    bf = f(18)
    bl = wrap(body, bf, LEAD_W - 24, draw)
    assert len(bl) <= 2, f"body lead {len(bl)} baris"
    for i, ln in enumerate(bl):
        draw.text((px, y + 70 + i * 21), ln, font=bf, fill=INK)
    # panel peta (kanan lead)
    mx = x + LEAD_W + 6
    mw = W - MARGIN - mx
    draw.rectangle([mx, y, mx + mw - 1, y + LEAD_H - 1],
                   outline=BORDER, width=1, fill=WHITE)
    draw_map(draw, mx, y, mw, LEAD_H)

def draw_secondary(draw, x, y):
    """5 kartu sekunder #2-6 (w 194). Judul 30px bold (leading 31px,
    max 3 baris: #2/#3/#5/#6 3 baris, #4 2 baris); badan 18px (leading
    20px, max 5 baris: #5 5 baris, sisanya 3 baris). Badan mulai dinamis
    4px setelah judul berakhir. Terukur: #5 berakhir y+215 <= y+216."""
    for i, s in enumerate(STORIES[1:6]):
        cx = x + i * (SEC_W + SEC_GAP)
        draw.rectangle([cx, y, cx + SEC_W - 1, y + SEC_H - 1],
                       outline=BORDER, width=1, fill=WHITE)
        draw_meta(draw, s, cx + META_MARGIN, y + 5, SEC_W)
        tf = f(30, True)
        tl = wrap(s[2], tf, SEC_W - 12, draw)
        assert len(tl) <= 3, f"judul sekunder #{s[0]} {len(tl)} baris"
        for j, ln in enumerate(tl):
            draw.text((cx + 6, y + 20 + j * 31), ln, font=tf, fill=INK)
        by = y + 20 + len(tl) * 31 + 4
        bf = f(18)
        bl = wrap(s[3], bf, SEC_W - 12, draw)
        assert len(bl) <= 5, f"body sekunder #{s[0]} {len(bl)} baris"
        assert by + (len(bl) - 1) * 20 + 18 <= y + SEC_H - 2, \
            f"body sekunder #{s[0]} meluber ({len(bl)} baris)"
        for j, ln in enumerate(bl):
            draw.text((cx + 6, by + j * 20), ln, font=bf, fill=INK)

def draw_regular(draw, x, y):
    """10 kartu reguler, grid 2 kolom x 5 baris (w 494, h 98, gap 2).
    Judul 28px bold SEMUA 1 baris (terukur max 352px <= 486); badan
    18px, leading 20px, max 2 baris. Meta 12px bold."""
    for idx, s in enumerate(STORIES[6:]):
        r, c = divmod(idx, 2)
        cy = y + r * (GRID_ROW_H + GRID_GAP)
        cx = x + c * (GRID_W + GRID_GAP_X)
        draw.rectangle([cx, cy, cx + GRID_W - 1, cy + GRID_ROW_H - 1],
                       outline=BORDER, width=1, fill=WHITE)
        draw_meta(draw, s, cx + META_MARGIN, cy + 4, GRID_W)
        tf = f(28, True)
        tl = wrap(s[2], tf, GRID_W - 8, draw)
        assert len(tl) <= 1, f"judul reguler #{s[0]} {len(tl)} baris"
        for j, ln in enumerate(tl):
            draw.text((cx + 4, cy + 20 + j * 30), ln, font=tf, fill=INK)
        bf = f(18)
        bl = wrap(s[3], bf, GRID_W - 8, draw)
        assert len(bl) <= 2, f"body reguler #{s[0]} {len(bl)} baris"
        by = cy + 54
        assert by + (len(bl) - 1) * 20 + 18 <= cy + GRID_ROW_H - 2, \
            f"body reguler #{s[0]} meluber ({len(bl)} baris)"
        for j, ln in enumerate(bl):
            draw.text((cx + 4, by + j * 20), ln, font=bf, fill=INK)

def draw_footer(draw, y):
    # L1: metodologi — 12px, kata lengkap (terukur 556,0px <= 990px).
    line1 = ("METHODOLOGY — 16 stories, 21 Nov 2026 (UTC); claims ≠ "
             "official facts; strip times verified.")
    assert tw(draw, line1, f(12)) <= 990, f"footer l1 {tw(draw, line1, f(12)):.0f}px"
    draw.text((MARGIN, y + 2), line1, font=f(12), fill=INK)
    # L2: legenda tag 12px (nama tag berwarna; terukur 629,5px <= 990px).
    segs = [("FACT", TAG_STYLE["FACT"][0]),
            (" = officially confirmed · ", MUTED),
            ("CLAIM", TAG_STYLE["CLAIM"][0]),
            (" = unverified claim · ", MUTED),
            ("DATA", TAG_STYLE["DATA"][0]),
            (" = statistics · ", MUTED),
            ("DISPUTED", TAG_STYLE["DISPUTED"][0]),
            (" = sources disagree", MUTED)]
    cx = MARGIN
    for t, c in segs:
        draw.text((cx, y + 18), t, font=f(12), fill=c)
        cx += tw(draw, t, f(12))
    assert cx - MARGIN <= 990, "legenda tag terlalu lebar"
    # L3: legenda region 12px (dot 12px + nama penuh; terukur 641,1px).
    lf = f(12)
    cx = MARGIN
    for g in GROUP_ORDER:
        draw.ellipse([cx, y + 34, cx + 11, y + 45], fill=GROUP_COLOR[g])
        cx += 14
        draw.text((cx, y + 34), g, font=lf, fill=INK)
        cx += tw(draw, g, lf) + 8
    assert cx - MARGIN <= 990, "legenda region terlalu lebar"
    # L4+L5: daftar sumber HANYA 16 cerita yg dipakai, nama penuh.
    # v9 C: ICJ, AP, BBC, Majik, Al Jazeera, USGS, Truth Social,
    # Middle East Eye, InfoLiveScore, Sky News (terukur 583,5px).
    # src2: data pasar (#6 Majik), korban gempa (#7 INDECI), skor
    # olahraga (#25/#26/#34 InfoLiveScore, theScore) — terukur 558,5px.
    src1 = ("SRC: ICJ, AP, BBC, Majik, Al Jazeera, USGS, Truth Social, "
            "Middle East Eye, InfoLiveScore, Sky News")
    src2 = ("Market data: Equiti via Majik · Quake victims: INDECI · "
            "Sports scores: InfoLiveScore, theScore")
    assert tw(draw, src1, f(12)) <= 990, f"footer src1 {tw(draw, src1, f(12)):.0f}px"
    assert tw(draw, src2, f(12)) <= 990, f"footer src2 {tw(draw, src2, f(12)):.0f}px"
    draw.text((MARGIN, y + 50), src1, font=f(12), fill=INK)
    draw.text((MARGIN, y + 66), src2, font=f(12), fill=INK)

def render():
    assert len(STORIES) == 16, f"{len(STORIES)} cerita"
    assert [s[0] for s in STORIES] == [1, 2, 3, 4, 5, 6, 7, 11, 15, 16,
                                       19, 20, 25, 26, 33, 34], "nomor kartu"
    for s in STORIES:
        assert s[4] in TAG_STYLE, f"tag #{s[0]} {s[4]}"
        assert s[8], f"kartu #{s[0]} tanpa sumber (16/16 wajib)"
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

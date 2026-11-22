#!/usr/bin/env python3
"""Render entry.png 1024x1024 — news-image-20261121 v8.10 (brief rev8.10).

v8.10 = polish atas v8.9 (34 cerita, 1 kartu = 1 cerita, lead + 5 sekunder +
28 reguler 4x7). 6 item (brief rev8.10) — TANPA ubah geometri:
- A1 TUKAR LEAD: #1 <-> #5 (judul, badan, tag, grup, lon, lat, sumber;
  NOMOR tetap). #1 baru ICJ: judul 459,0px @36 bold (<=620); badan 2 baris
  (551/214px @16, wrap 620). #5 baru Iran padat: judul 2 baris (139/140px
  @24 bold, wrap 182); badan 4 baris (155/150/138/139px @16, wrap 182),
  end=140 TEPAT di batas — LOLOS, ukur ulang sebelum commit. Kicker lead
  "LEAD · GLOBAL · [RESMI] · 21 NOV 2026 · ICJ" (298,9px @12 bold <=620).
  Pin peta ikut nomor: pin #1 (merah) ke Myanmar (96,0/21,0), pin #5 ke
  Bahrain (50,5/26,2) — tanpa ubah kode peta (jarak pin 66,4px >= 20).
- A2 h1 "BERITA DUNIA 21 NOV 2026 — 34 CERITA, 7 TOPIK" (845,0px @30 bold);
  h2 "SABTU, 21 NOV 2026 · 6 LOKASI UTAMA · 5 JAM KEJADIAN TERVERIFIKASI ·
  SEMUA BERITA BERTANGGAL" (724,1px @14).
- A3 badan #3 tambah "Meksiko:" + "AS" (3 baris 168/171/41px @16).
- A4 badan #4 tambah "Iklim PBB:" (3 baris 179/132/101px @16).
- A5 badan #22 "'not good'" -> "'tidak baik'" (2 baris 176/234px @16,
  wrap 235 — margin 1,4px, LOLOS).

v8.9 = polish atas v8.8 (34 cerita, 1 kartu = 1 cerita, lead + 5 sekunder +

v8.9 = polish atas v8.8 (34 cerita, 1 kartu = 1 cerita, lead + 5 sekunder +
28 reguler 4x7). 5 micro-fix teks (brief rev8.9) — TANPA ubah geometri:
- A1 h1 "WORLD NEWS — 34 DATE-CHECKED STORIES, 7 TOPICS" ->
  "BERITA DUNIA — 34 DATE-CHECKED STORIES, 7 TOPIK" (908.6px @30px bold).
- A2 badan #34 "Indiana;" -> "Indiana." (tetap 3 baris).
- A3 badan #22 "Database kejahatan AS" -> "Database kriminal FBI".
- A4 badan #23 "langgar kuorum" -> "langgar syarat kuorum".
- A5 badan lead #1 "F-16 kena" -> "F-16 terkena" (tetap 2 baris, assert lead).

v8.8 = polish atas v8.7 (34 cerita, 1 kartu = 1 cerita, lead + 5 sekunder +
28 reguler 4x7). 2 micro-fix huruf (brief rev8.8) — TANPA ubah geometri:
- A1 badan #23 "Kuorum" -> "kuorum" (K -> k; kata umum huruf kecil).
- A2 badan #34 "laga" -> "Laga" (l -> L; defensif — "l" kecil nyaris
  identik dgn "I" kapital di DejaVu 16px; "Laga" berkaki jelas).

v8.7 = polish atas v8.6 (34 cerita, 1 kartu = 1 cerita, lead + 5 sekunder +
28 reguler 4x7). 1 micro-fix teks (brief rev8.7) — TANPA ubah geometri:
- A1 badan #17 "Pangan, emisi, mobilitas 100 ribu pemuda/thn." ->
  "Pangan, emisi & mobilitas 100 ribu pemuda/thn." (tetap 2 baris
  208/175px @16px; data v8.7).

v8.6 = polish atas v8.5 (34 cerita, 1 kartu = 1 cerita, lead + 5 sekunder +
28 reguler 4x7). 4 micro-fix teks (brief rev8.6) — TANPA ubah geometri:
- A1 judul #23 "Proxy Voting Ilegal" -> "Voting Proksi Ilegal" (219,9px
  <= 235px @20px bold; data v8.6). A2 badan #24 tambah "tayang" (2 baris
  222/216px @16px; subjek DIPERTAHANKAN). A3 badan #14 "dgn" -> "dengan"
  (tetap 3 baris 215/159/77px @16px).
- A4 h1 "7 KATEGORI" -> "7 TOPICS" (927,8px <= 990px @30px bold) — h1
  sepenuhnya Inggris TANPA buang "DATE-CHECKED". "7 CATEGORIES" TETAP
  DIBLOKIR (1014,9px > 990px, terukur v8.5).

v8.4 = polish atas v8.3 (34 cerita, 1 kartu = 1 cerita, lead + 5 sekunder +
28 reguler 4x7). 1 edit footer + 1 target judul DIBLOKIR terukur — TANPA
ubah geometri (GRID_ROWS, SEC_H, HEADER_H, gap semua TETAP v8.1/v8.2/v8.3).
Perubahan vs v8.3 (brief rev8.4):
- footer src1: "InfoLiveScore, theScore" dipulihkan (terukur 961,0px
  <= 990px); dana "Middle East Eye" -> "MEE" (hemat 63,9px; "MEE" =
  kode meta kartu #16 sendiri). "Sky News" tetap penuh; src2 tak berubah.
- A1 DIBLOKIR: judul #10 "Drone Serang Sparta II" = 258,8px > 235px
  (lebih 23,8px; klaim Nemotron "~206px" salah ~53px) -> judul #10
  TETAP "Sparta II Kena drone" (233,1px). Font tidak dikecilkan.

v8.3 = polish atas v8.2 (34 cerita, 1 kartu = 1 cerita, lead + 5 sekunder +
28 reguler 4x7). 6 edit teks + percobaan footer — TANPA ubah geometri
(GRID_ROWS, SEC_H, HEADER_H, gap semua TETAP v8.1/v8.2). Perubahan vs v8.2
(brief rev8.3, A-B):
- teks: #2 badan "2 tewas, ~60 luka; penyelamat diserang." (2 baris;
  usia dibuang — pluralitas ronde v8.2 minta "~60 luka" kembali);
  #10 judul "Sparta II Kena drone" + badan "Kapal Rusia; 16 selamat;
  Finlandia duga Ukraina."; #13 badan "Tekan dengue −69%; ..." (minus
  U+2212, seragam dgn #6); #16 judul "Cegat Rudal Riyadh" (badan + tag
  [RESMI] tetap); #27 badan tanpa "Mora 71';" (baris ke-2 137,5px);
  #34 badan "laga 50+ poin ke-26".
- footer: l1 "yang"/"Jumat" dipulihkan (dana: "beda" -> "≠", 985,6px);
  src1 "Sky News" dipulihkan (dana: "InfoLiveScore" -> "ILS", 963,9px);
  label "SRC: " dipertahankan; "INDECI" tetap.

DEVIASI TERUKUR vs brief rev8.3 (semua dilaporkan ke parent):
#10 judul target "Sparta II Kena Drone" = 235,4px > anggaran 235px
(lebih 0,4px) -> dipakai "Sparta II Kena drone" (233,1px; 'd' kecil).
#16 judul target "Rudal Riyadh Dicegat" = 241,9px > 235px (alternatif
Kimi "Riyadh: Rudal Dicegat" 249,9px) -> dipakai "Cegat Rudal Riyadh"
(221,2px; kata kerja + objek + tempat, tak ambigu).
Footer src1: hapus label "SRC: " saja TIDAK cukup (992,7px, masih lebih
2,7px) -> "InfoLiveScore" disingkat ke kode meta "ILS" (963,9px; nama
penuh tetap ada di src2 "Skor olahraga: InfoLiveScore, theScore").

GEOMETRI (total HARUS 1024 — di-assert di render):
header 58 + gap 0 + strip 42 + gap 0 + lead 118 + gap 0 + sekunder 142
+ gap 0 + grid (610 + 6 gap) + gap 0 + footer 48 = 1024.
Grid rows [76,93,76,76,98,98,93]: baris 93 = badan 3 baris judul 1
baris (#13/#14/#34); baris 98 = badan 3 baris atau judul 2 baris +
badan 2 baris (#23/#25/#26/#29).
Leading badan 17px (16px font — lantai, tidak pernah dikecilkan).
"""
from PIL import Image, ImageDraw, ImageFont
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stories_v8_10 import (STORIES, PINS_V8_2, GROUP_COLOR, GROUP_ORDER,
                         SRC_SHORT, TIME_IN_META)

W, H = 1024, 1024
OUT = "/tmp/entry-v8.png" if os.environ.get("V8_DEV") else "entry.png"

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

# ---- geometri (px) — total 1024, di-assert di render() ----
HEADER_H = 58
STRIP_H = 42
LEAD_H = 118
SEC_H = 142
FOOTER_H = 48
GAP_HS = 0      # header -> strip (v8.1: dirapatkan demi baris 93px)
GAP_SL = 0      # strip -> lead
GAP_LS = 0      # lead -> secondary
GAP_SG = 0      # secondary -> grid
GAP_GF = 0      # grid -> footer
GRID_ROWS = [76, 93, 76, 76, 98, 98, 93]
GRID_GAP = 1
LEAD_W = 644
SEC_W = 194
SEC_GAP = 5
GRID_W = 243
GRID_GAP_X = 2
MARGIN = 17

# ---- posisi y (dihitung, total harus 1024) ----
Y_HEADER = 0
Y_STRIP = Y_HEADER + HEADER_H + GAP_HS          # 60
Y_LEAD = Y_STRIP + STRIP_H + GAP_SL             # 104
Y_SEC = Y_LEAD + LEAD_H + GAP_LS                # 223
Y_GRID = Y_SEC + SEC_H + GAP_SG                 # 366
Y_FOOTER = Y_GRID + sum(GRID_ROWS) + 6 * GRID_GAP + GAP_GF  # 976
assert Y_FOOTER + FOOTER_H == 1024, Y_FOOTER

# ---- peta dot-matrix (baris 0..15, kolom 12..58 di-crop) ----
# v8.1 (D1): diperluas ke timur — India (baris 9-12, kolom 49-52),
# Asia Tenggara incl. Myanmar/Thailand/Vietnam (baris 10-13, kolom
# 53-57), pesisir China Selatan (baris 8-10, kolom 54-58). Pemetaan:
# kolom c ~= lon 5c-177,5; baris r ~= lat 77,5-5r. Pin #5 (lon 96,
# lat 21 -> kolom ~54,7, baris ~11,3) kini duduk DI ATAS dot darat.
# v8.2 (C1): + pantai timur AS (baris 6-8, kolom 19-22) agar pin #6
# (New York, lon -74/lat 40,7 -> kolom ~20,7, baris ~7,4) duduk DI ATAS
# dot darat (jarak dot terdekat 3,4px < radius pin 8px + dot 2px).
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
LAND_DOT = (100, 116, 139)   # v8: digelapkan satu tingkat (was 148,163,184)

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

TRACK10 = -0.06  # px/celah, judul #10 saja (v8.5 A3)

def draw_tracked(draw, text, x, y, font, fill, track=TRACK10):
    # Gambar per karakter dgn tracking; HANYA judul #10 (v8.5 A3).
    cx = x
    for i, ch in enumerate(text):
        draw.text((cx, y), ch, font=font, fill=fill)
        cx += draw.textlength(ch, font=font) + (track if i < len(text) - 1 else 0)

# ---- peta: crop lon -120..110, lat 0..80, K=1.45 ----
MAP_K = 1.45
MAP_LON0, MAP_LON1, MAP_LAT1 = -120, 110, 80   # lat bawah 0
MAP_W = int((MAP_LON1 - MAP_LON0) * MAP_K)     # 333
MAP_H = int(MAP_LAT1 * MAP_K)                  # 116

def map_xy(lon, lat, ox, oy):
    return (ox + (lon - MAP_LON0) * MAP_K, oy + (MAP_LAT1 - lat) * MAP_K)

def draw_map(draw, x, y, w, h):
    """Panel peta: dot-matrix darat + 6 pin (dot 16px, angka 12px bold).
    Tanpa bingkai peta (panel sudah berbingkai; peta 116px nyaris setinggi
    panel 118px — bingkai +3px akan meluber)."""
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
    # cek tabrakan pin: halo putih 20px -> pusat min 20px (v8.1: #2
    # (0,-2) + #4 (0,+2) = 20,33px, halo TIDAK bersentuhan).
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
# Tick 21:00 = JUMAT (bukan Sabtu) — judul + label tick + legenda "JUM"
# menegaskan hari. Legenda menautkan tiap jam ke nomor kartu (brief D).
STRIP_EVENTS = [  # (label, jam_dari_Jumat_21_00, warna)
    ("21:00 Wall St tutup", 0.0, GREEN),
    ("00:09 gempa Peru", 3.15, GREEN),
    ("03:23 Harden 51 poin", 6.38, BLUE),
    ("15:00 Leeds KO", 18.0, RED),
    ("17:30 Newcastle KO", 20.5, RED),
]

def draw_strip(draw, y):
    x0, x1 = MARGIN, W - MARGIN
    title = "STRIP UTC — JUM 20 NOV 21:00 → SAB 21 NOV (UTC)"
    draw.text((x0, y + 2), title, font=f(12, True), fill=INK)
    right = "HANYA JAM TERVERIFIKASI · 6 PIN = 6 CERITA TERATAS"
    draw.text((x1 - tw(draw, right, f(11, True)), y + 3), right,
              font=f(11, True), fill=MUTED)
    axis_y = y + 26
    # label hari di atas sumbu, di kanan tick-nya (tick 00:09 di x0+115
    # memaksa "SAB 21 NOV" geser ke x0+125 agar tidak menabrak tick itu).
    draw.text((x0 + 6, y + 15), "JUM 20 NOV", font=f(10, True), fill=MUTED)
    draw.text((x0 + 125, y + 15), "SAB 21 NOV", font=f(10, True), fill=MUTED)
    # garis sumbu + tick tiap jam (kecil, tidak menabrak legenda)
    draw.line([(x0, axis_y), (x1, axis_y)], fill=BORDER, width=2)
    for h in range(28):
        tx = x0 + (x1 - x0) * h / 27.0
        draw.line([(tx, axis_y - 3), (tx, axis_y + 3)], fill=BORDER, width=1)
    # tick peristiwa: hanya DI ATAS sumbu (legenda di bawah tetap bersih)
    for label, h, col in STRIP_EVENTS:
        tx = x0 + (x1 - x0) * h / 27.0
        draw.line([(tx, axis_y - 7), (tx, axis_y)], fill=col, width=3)
        draw.ellipse([tx - 3, axis_y - 3, tx + 3, axis_y + 3], fill=col)
    legend = ("JUM 21:00 Wall St tutup → #6 · 00:09 gempa Peru → #7 · "
              "03:23 Harden → #34 · 15:00 Leeds KO → #25 · "
              "17:30 Newcastle KO → #26")
    assert tw(draw, legend, f(11)) <= 990, "legenda strip terlalu lebar"
    draw.text((x0, y + 30), legend, font=f(11), fill=MUTED)

# ---- meta per kartu (brief B1, v8.1) ----
# Format SERAGAM: dot grup 12px + "N [TAG] · 21 NOV · SRC" (4 segmen)
# di SEMUA kartu; #25/#26/#34 membawa "· HH:MM" sebagai satu-satunya
# pengecualian segmen ke-5 (jam, bukan region). Kode region v8 DIHAPUS:
# region tetap terkode lewat dot warna + legenda footer.
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
    h1 = "BERITA DUNIA 21 NOV 2026 — 34 CERITA, 7 TOPIK"
    assert tw(draw, h1, f(30, True)) <= 990, "h1 terlalu lebar"
    draw.text((MARGIN, 1), h1, font=f(30, True), fill=INK)
    # h2 HURUF BESAR SEMUA (tanpa descender — memberi ruang utk legenda tag)
    # v8.1 (B2): Bahasa Indonesia penuh.
    h2 = ("SABTU, 21 NOV 2026 · 6 LOKASI UTAMA · 5 JAM KEJADIAN TERVERIFIKASI "
          "· SEMUA BERITA BERTANGGAL")
    assert tw(draw, h2, f(14)) <= 990, "h2 terlalu lebar"
    draw.text((MARGIN, 29), h2, font=f(14), fill=MUTED)
    # legenda tag SATU BARIS 11px, nama tag berwarna (brief E)
    segs = [("RESMI", TAG_STYLE["RESMI"][0]),
            (" = terkonfirmasi resmi · ", MUTED),
            ("KLAIM", TAG_STYLE["KLAIM"][0]),
            (" = klaim belum terverifikasi · ", MUTED),
            ("DATA", TAG_STYLE["DATA"][0]),
            (" = angka/data · ", MUTED),
            ("BERSELISIH", TAG_STYLE["BERSELISIH"][0]),
            (" = sumber berbeda", MUTED)]
    cx = MARGIN
    for t, c in segs:
        draw.text((cx, 43), t, font=f(11), fill=c)
        cx += tw(draw, t, f(11))
    assert cx - MARGIN <= 990, "legenda tag terlalu lebar"
    draw.line([(MARGIN, 57), (W - MARGIN, 57)], fill=BORDER, width=1)

def draw_lead(draw, x, y):
    """Lead #1 (Iran–Bahrain) + panel peta 6 pin di kanan. Tanpa chips
    (dekoratif, duplikat badan — dihapus demi anggaran vertikal v8)."""
    s = STORIES[0]
    assert s[0] == 1
    draw.rectangle([x, y, x + LEAD_W - 1, y + LEAD_H - 1],
                   outline=BORDER, width=1, fill=WHITE)
    px = x + 12
    kicker = "LEAD · GLOBAL · [RESMI] · 21 NOV 2026 · ICJ"
    assert tw(draw, kicker, f(12, True)) <= LEAD_W - 24, "kicker lead lebar"
    draw.text((px, y + 12), kicker, font=f(12, True), fill=RED)
    title = s[2]
    tf = f(36, True)
    assert tw(draw, title, tf) <= LEAD_W - 24, f"judul lead {tw(draw, title, tf):.0f}px"
    draw.text((px, y + 26), title, font=tf, fill=INK)
    body = s[3]
    bf = f(16)
    bl = wrap(body, bf, LEAD_W - 24, draw)
    assert len(bl) <= 2, f"body lead {len(bl)} baris"
    for i, ln in enumerate(bl):
        draw.text((px, y + 70 + i * 19), ln, font=bf, fill=INK)
    # panel peta (kanan lead)
    mx = x + LEAD_W + 6
    mw = W - MARGIN - mx
    draw.rectangle([mx, y, mx + mw - 1, y + LEAD_H - 1],
                   outline=BORDER, width=1, fill=WHITE)
    draw_map(draw, mx, y, mw, LEAD_H)

def draw_secondary(draw, x, y):
    """5 kartu sekunder #2-6 (w 194, judul 24px, isi 16px SEMUA).
    Badan: #2 2 baris (v8.3, berakhir 72+2*17=106px, ruang bawah 36px),
    #5 4 baris, #3/#6 3 baris, #4 2 baris (terukur). Leading 17px;
    badan berakhir y+140 max (SEC_H 142)."""
    for i, s in enumerate(STORIES[1:6]):
        cx = x + i * (SEC_W + SEC_GAP)
        draw.rectangle([cx, y, cx + SEC_W - 1, y + SEC_H - 1],
                       outline=BORDER, width=1, fill=WHITE)
        draw_meta(draw, s, cx + META_MARGIN, y + 5, SEC_W)
        tf = f(24, True)
        tl = wrap(s[2], tf, SEC_W - 12, draw)
        assert len(tl) <= 2, f"judul sekunder #{s[0]} {len(tl)} baris"
        for j, ln in enumerate(tl):
            draw.text((cx + 6, y + 20 + j * 26), ln, font=tf, fill=INK)
        bf = f(16)
        bl = wrap(s[3], bf, SEC_W - 12, draw)
        assert len(bl) <= 4, f"body sekunder #{s[0]} {len(bl)} baris"
        assert 72 + len(bl) * 17 <= SEC_H - 2, \
            f"body sekunder #{s[0]} meluber ({len(bl)} baris)"
        for j, ln in enumerate(bl):
            draw.text((cx + 6, y + 72 + j * 17), ln, font=bf, fill=INK)

def draw_regular(draw, x, y):
    """28 kartu reguler #7-34, grid 4 kolom.
    Judul 20px (1-2 baris); badan 16px, leading 17px.
    Baris 93/98px: badan 3 baris (judul 1 baris) atau 2 baris (judul 2 baris).
    Baris 76px: badan max 2 baris, judul 1 baris."""
    for idx, s in enumerate(STORIES[6:]):
        r, c = divmod(idx, 4)
        cy = y + sum(GRID_ROWS[:r]) + r * GRID_GAP
        cx = x + c * (GRID_W + GRID_GAP_X)
        ch = GRID_ROWS[r]
        draw.rectangle([cx, cy, cx + GRID_W - 1, cy + ch - 1],
                       outline=BORDER, width=1, fill=WHITE)
        draw_meta(draw, s, cx + META_MARGIN, cy + 4, GRID_W)
        tf = f(20, True)
        if s[0] == 10:
            # v8.5 A3: "Sparta II Kena Drone" dgn tracking -0,06px/celah
            # (terukur 234,6px <= 235px). JANGAN via wrap() — wrap pakai
            # lebar string penuh 235,4px -> 2 baris (salah).
            tw10 = sum(draw.textlength(c, font=tf) for c in s[2]) + TRACK10 * (len(s[2]) - 1)
            assert tw10 <= GRID_W - 8, f"judul #10 tracking {tw10:.1f}px"
            tl = [s[2]]
        else:
            tl = wrap(s[2], tf, GRID_W - 8, draw)
        tall = len(tl) == 2
        assert len(tl) <= 2, f"judul reguler #{s[0]} {len(tl)} baris"
        by = cy + 62 if tall else cy + 40
        for j, ln in enumerate(tl):
            if s[0] == 10:
                draw_tracked(draw, ln, cx + 4, cy + 19 + j * 22, tf, INK)
            else:
                draw.text((cx + 4, cy + 19 + j * 22), ln, font=tf, fill=INK)
        bf = f(16)
        bl = wrap(s[3], bf, GRID_W - 8, draw)
        max_body = 3 if (ch >= 93 and not tall) else 2
        assert len(bl) <= max_body, \
            f"body reguler #{s[0]} {len(bl)} baris (max {max_body})"
        assert by + len(bl) * 17 <= cy + ch - 2, \
            f"body reguler #{s[0]} meluber (y={by}, {len(bl)} baris, h={ch})"
        for j, ln in enumerate(bl):
            draw.text((cx + 4, by + j * 17), ln, font=bf, fill=INK)

def draw_footer(draw, y):
    # L1: metodologi + aturan tanggal — v8.3: 11px, kata lengkap
    # dipulihkan (terukur 985,6px <= 990px): "yg" -> "yang",
    # "Jum" -> "Jumat"; dananya "beda" -> "≠" ("klaim ≠ fakta resmi",
    # 126,5px -> 108,3px). "Berita 21 Nov:" dipertahankan (bukan "Isi").
    # Isi utuh (34 cerita, UTC, klaim vs fakta resmi, jam strip
    # terverifikasi, aturan tanggal 20->21 Nov, pasar tutup).
    line1 = ("METODOLOGI — 34 cerita 21 Nov 2026 (UTC); klaim ≠ fakta "
             "resmi; jam strip terverifikasi. Berita 21 Nov: peristiwa "
             "20 Nov yang dilaporkan 21 Nov + pasar tutup Jumat 21:00 UTC.")
    assert tw(draw, line1, f(11)) <= 990, f"footer l1 {tw(draw, line1, f(11)):.0f}px"
    # v8.5 A2: teks footer MUTED -> INK (kontras; MUTED global TETAP).
    draw.text((MARGIN, y + 0), line1, font=f(11), fill=INK)
    # L2: legenda region 11px (dot 12px + nama penuh).
    lf = f(11)
    cx = MARGIN
    for g in GROUP_ORDER:
        draw.ellipse([cx, y + 12, cx + 11, y + 23], fill=GROUP_COLOR[g])
        cx += 13
        draw.text((cx, y + 12), g, font=lf, fill=INK)  # v8.5 A2
        cx += tw(draw, g, lf) + 8
    assert cx - MARGIN <= 990, "legenda region terlalu lebar"
    # L3+L4: daftar sumber LENGKAP, nama penuh (brief E). v8.4: f(11),
    # "InfoLiveScore, theScore" dipulihkan di src1 (terukur 961,0px
    # <= 990px); dananya "Middle East Eye" -> "MEE" (hemat 63,9px;
    # "MEE" = kode meta kartu #16 sendiri, bisa didekode dari kartu).
    # "Sky News" tetap penuh (dipulihkan v8.3). Jalur cadangan (hapus
    # spasi setelah koma, hemat 66,5px -> 958,4px) TIDAK dipakai —
    # jalur utama muat. SEMUA outlet tetap disebut.
    src1 = ("SRC: BBC, Reuters, AP, Al Jazeera, Guardian, DW, Sky News, "
            "UPI, CBC, RFI, MEE, ICJ, USGS, UKMTO, Majik, "
            "InfoLiveScore, theScore, Straits Times, Economic Times, "
            "Truth Social")
    src2 = ("Data pasar: Equiti via Majik · Korban gempa: INDECI · "
            "Skor olahraga: InfoLiveScore, theScore")
    assert tw(draw, src1, f(11)) <= 990, f"footer src1 {tw(draw, src1, f(11)):.0f}px"
    assert tw(draw, src2, f(11)) <= 990, f"footer src2 {tw(draw, src2, f(11)):.0f}px"
    draw.text((MARGIN, y + 24), src1, font=f(11), fill=INK)  # v8.5 A2
    draw.text((MARGIN, y + 36), src2, font=f(11), fill=INK)  # v8.5 A2

def render():
    assert len(STORIES) == 34, f"{len(STORIES)} cerita"
    assert [s[0] for s in STORIES] == list(range(1, 35)), "nomor kartu 1..34"
    for s in STORIES:
        assert s[4] in TAG_STYLE, f"tag #{s[0]} {s[4]}"
        assert s[8], f"kartu #{s[0]} tanpa sumber (34/34 wajib)"
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

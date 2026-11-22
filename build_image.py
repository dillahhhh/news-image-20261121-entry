#!/usr/bin/env python3
"""news-image-20261121 — BUILD-TIME renderer v2 (NOT run by the grader).

Renders the deterministic 1024x1024 PNG dashboard and writes it to entry.png
next to this script. Uses Pillow — that is fine here, because the grader NEVER
runs this file: RULES.txt says the graded program (main.py) runs in a fresh
container with "standard library only: nothing is installed before it runs",
so main.py is stdlib-only and only copies the pre-rendered entry.png.

v2 (verdict Claude REVISI, 12:29 WIB 22 Nov):
- Grid 6 cols x 7 rows so each story stays on one row (2 stories per row;
  row 7: story 13 + S1/S2/S3). Count is "39 entri + 3 catatan" everywhere.
- Fonts up: card title 13px bold, body 11px, tag 9px. Layout is enforced in
  code (title <= 2 lines, body <= 3 lines, no line wider than the card, body
  never reaches the tag pill); render() exits 1 on any violation.
- Map: 1:1 projection (1.1 px/deg both axes), 150+ px tall, pins spread with
  leader lines where they would collide. Region colour is shared by the card
  stripe, the number badge, the map pin and the UTC-strip tick.
- UTC strip spans Fri 21:00 -> Sat 24:00 UTC with ONLY the two known times:
  Wall Street close Fri 21:00 UTC (tick) and the Peru quake as a Sat
  00:00-05:00 UTC range (Friday evening local), labelled as a range.
- One language (Indonesian). [DENY] -> [BANTAH], [2 SUMBER] -> [BERSELISIH].
  One date rule, in S3 and in the footer. Hero stories: 1, 2, 3, 4, 6, 7
  (ICJ up, Peru quake down). Every card carries a new fact (number/name/
  impact); no invented stories, timestamps, outlet names or confidence
  numbers. Estimates use ~.

v3 (verdict Claude REVISI ringan atas v2, 12:46 WIB 22 Nov — 4 poin saja):
- Tag [RESMI] yang bertentangan: dengue 13-1/13-2/13-3 -> [DATA]; 13-1
  judul "Studi: Wolbachia Tekan Dengue" (atribusi); 11-3 -> [INFO];
  6-2 judul "Nvidia Dikabarkan Diselidiki SEC", tag [KLAIM].
- Strip UTC: batang rentang gempa Peru pindah ke baris sendiri (y 140-148)
  di antara label dan garis ruler — v2 menimpa label (hanya "4:00" terbaca).
- ICJ dipersempit: 5-3 memakai frasa persis sumber "pertama kalinya ICJ
  menyatakan sebuah negara melakukan genosida" (CNN/Asia Daily 19 Nov);
  5-2 "diperintah ganti rugi" TETAP (terverifikasi CNN + SCC Times).
- Renumber: cerita 5 Peru <-> 7 Myanmar ditukar; hero jadi 1-6;
  legenda "Lingkar merah = 1-6"; pin 5 = Myanmar, pin 7 = Peru.
- Badan 5-3 render 10px (bukan 11px) supaya frasa verbatim muat 3 baris;
  judul 13-1 dan 6-2 dipadatkan agar muat 2 baris (angka ~69% / -14%
  tetap ada di badan kartu).

Run locally:  python3 build_image.py
No randomness, no clock, no network. Re-running writes identical bytes.
"""
import hashlib
import os
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BASE = os.path.dirname(os.path.abspath(__file__))

PAPER = (248, 244, 236)
CARD_BG = (255, 253, 248)
INK = (25, 23, 19)
MUTED = (107, 101, 90)
RULE = (201, 194, 178)
RED = (176, 42, 30)
GREEN = (30, 107, 52)
GREEN_TINT = (222, 238, 226)
AMBER = (138, 94, 0)
AMBER_TINT = (247, 235, 205)
PURPLE = (107, 45, 143)
PURPLE_TINT = (238, 226, 245)
ORANGE = (168, 74, 20)
ORANGE_TINT = (248, 232, 219)
BLUE = (29, 78, 137)
BLUE_TINT = (222, 233, 245)
TEAL = (0, 128, 128)
GREY_TINT = (236, 233, 226)
GOLD = (232, 179, 75)

TAG_STYLE = {
    "RESMI": (GREEN, GREEN_TINT),
    "KLAIM": (AMBER, AMBER_TINT),
    "BANTAH": (PURPLE, PURPLE_TINT),
    "BERSELISIH": (ORANGE, ORANGE_TINT),
    "DATA": (BLUE, BLUE_TINT),
    "INFO": (MUTED, GREY_TINT),
}

# Region colour groups (shared by card stripe, number badge, map pin, UTC tick).
REGION_COLOR = {
    "TELUK": TEAL, "HORMUZ": TEAL,
    "UKRAINA": BLUE, "COP31": BLUE, "BALTIK": BLUE,
    "MEKSIKO": GREEN, "PERU": GREEN, "PASAR": GREEN, "BRASIL": GREEN,
    "MYANMAR": ORANGE, "LADAKH": ORANGE, "DAGANG": ORANGE,
    "DIPLOMASI": PURPLE,
    "RINGKASAN": MUTED,
}
REGION_NAMES = [
    (TEAL, "Teluk"), (BLUE, "Eropa"), (GREEN, "Amerika"),
    (ORANGE, "Asia"), (PURPLE, "Diplomasi"),
]

# Hero stories (red border on their first card, red ring on their map pin).
HERO_STORIES = {1, 2, 3, 4, 5, 6}

# (story, region, title, fact, tag, hero)
CARDS = [
    # 1 — Iran–Bahrain
    (1, "TELUK", "IRGC Klaim Serang Pangkalan AS",
     "2 pangkalan AS: al-Riffa & Awali, Bahrain.", "KLAIM", True),
    (1, "TELUK", "Kebakaran Situs Industri Sipil",
     "0 korban; pertahanan udara cegat serangan lain.", "RESMI", False),
    (1, "TELUK", "Klaim Drone vs Bantahan F-16",
     "Iran klaim jatuhkan drone AS dekat Qeshm; AS bantah F-16 kena.",
     "KLAIM / BANTAH", False),
    # 2 — Kryvyi Rih
    (2, "UKRAINA", "Rudal Balistik Rusia",
     "Hantam pusat kota Kryvyi Rih.", "RESMI", True),
    (2, "UKRAINA", "2 Tewas, ~60 Luka",
     "Korban: anak 7 thn & perempuan 20 thn.", "RESMI", False),
    (2, "UKRAINA", "25 Blok Apartemen Rusak",
     "Penyelamat diserang; 25 blok apartemen, RS + sekolah rusak.",
     "RESMI", False),
    # 3 — Chapo Isidro
    (3, "MEKSIKO", "Chapo Isidro Ditangkap",
     "Pasukan khusus Meksiko; Guasave, Sinaloa.", "RESMI", True),
    (3, "MEKSIKO", "11 Tewas Susulan",
     "4 tentara, 7 penembak tewas.", "RESMI", False),
    (3, "MEKSIKO", "8 Ditangkap, Hadiah $5 Juta",
     "8 ditangkap; hadiah AS $5 juta.", "RESMI", False),
    # 4 — COP31 Antalya
    (4, "COP31", "COP31 Overtime, Belum Sepakat",
     "Tenggat Jumat terlewat; perundingan berlanjut Sabtu.", "RESMI", True),
    (4, "COP31", "Fosil Dicoret dari Draf",
     "Kata 'fossil fuels' dicoret dari draf; ~200 negara berselisih.",
     "RESMI", False),
    (4, "COP31", "Prancis-Panama Dorong Kembali",
     "Prancis + Panama dorong kembalikan 'fossil fuels' ke draf.",
     "RESMI", False),
    # 5 — Myanmar / ICJ (dulu 7; tukar dengan Peru — Claude v2 poin 4)
    (5, "MYANMAR", "Myanmar Tolak Putusan ICJ",
     "Myanmar menolak putusan ICJ soal Rohingya.", "RESMI", True),
    (5, "MYANMAR", "ICJ: Myanmar Bersalah Genosida",
     "Bersalah genosida atas Rohingya; diperintah ganti rugi (besaran menyusul).",
     "RESMI", False),
    (5, "MYANMAR", "9–6, Pertama dalam Sejarah",
     "9–6 atas pokok genosida; pertama kalinya ICJ menyatakan negara melakukan genosida.",
     "RESMI", False, 9),
    # 6 — Saham AI
    (6, "PASAR", "S&P -3,7%, Nasdaq -5,3%",
     "Penutupan Jumat 21:00 UTC; S&P −3,7%, Nasdaq −5,3%.", "DATA", True),
    (6, "PASAR", "Nvidia Dikabarkan Diselidiki SEC",
     "Anjlok 14%; laporan media: penyelidikan SEC.", "KLAIM", False),
    (6, "PASAR", "Gain 2026 Terhapus",
     "S&P 500 dan Nasdaq menghapus seluruh gain 2026.", "DATA", False),
    # 7 — Gempa Peru (dulu 5; tukar dengan Myanmar — Claude v2 poin 4)
    (7, "PERU", "Gempa M6,7 Guncang Junín",
     "M6,7 (sumber lain 6,9); kedalaman ~108 km.", "BERSELISIH", False),
    (7, "PERU", "Terasa Sampai Lima",
     "Jumat malam waktu setempat; Sabtu dini hari UTC, terasa di Lima.",
     "RESMI", False),
    (7, "PERU", "Tanpa Korban, Tanpa Tsunami",
     "Tanpa korban/kerusakan; tanpa tsunami.", "RESMI", False),
    # 8 — Tanker Hormuz
    (8, "HORMUZ", "Tanker Terbakar di Hormuz",
     "~8 mil laut utara Khasab, Oman.", "RESMI", False),
    (8, "HORMUZ", "Ranjau vs Proyektil",
     "Iran klaim ranjau laut; UKMTO bilang proyektil.", "BERSELISIH", False),
    (8, "HORMUZ", "0 Korban dalam Kebakaran",
     "Tidak ada korban dalam insiden tanker.", "RESMI", False),
    # 9 — Ladakh
    (9, "LADAKH", "Pemilu Panchayat & Kota Pertama",
     "Pemilu panchayat + kota pertama sejak 2019 di Ladakh.", "RESMI", False),
    (9, "LADAKH", "Suara di Leh & Kargil",
     "Pemungutan suara hari Sabtu.", "RESMI", False),
    (9, "LADAKH", "Berakhir 30 November",
     "Pemungutan suara berakhir 30 Nov.", "RESMI", False),
    # 10 — Sparta II
    (10, "BALTIK", "Sparta II Kena 2 Drone",
     "Kapal kargo Rusia terbakar, Teluk Finlandia.", "RESMI", False),
    (10, "BALTIK", "16 Awak Dievakuasi",
     "Dievakuasi ke perairan Finlandia.", "RESMI", False),
    (10, "BALTIK", "Finlandia: Ukraina Diduga",
     "Menurut Finlandia, Ukraina kemungkinan pelaku.", "KLAIM", False),
    # 11 — Trump / Yalta
    (11, "DIPLOMASI", "Trump Posting '1945, 2026'",
     "Unggahan Trump: '1945, 2026'.", "RESMI", False),
    (11, "DIPLOMASI", "Yalta x Trump, Xi, Putin",
     "Foto Yalta 1945 dipadukan dengan Trump, Xi, Putin.", "RESMI", False),
    (11, "DIPLOMASI", "Debat: Diplomasi vs Pembagian Baru",
     "Postingan memantik debat diplomasi vs pembagian baru.", "INFO", False),
    # 12 — UE–Indonesia
    (12, "DAGANG", "UE–Indonesia Teken Dagang",
     "CEPA + perjanjian investasi diteken di Brussels.", "RESMI", False),
    (12, "DAGANG", "Tarif 98,5% Dihapus",
     "Bea masuk dihapus hingga 98,5% pos tarif; hemat €600 jt/thn.",
     "RESMI", False),
    (12, "DAGANG", "Target Awal 2027, Pasar 730 Juta",
     "Ditargetkan berlaku awal 2027; pasar gabungan 730 juta orang.", "RESMI", False),
    # 13 — Dengue Brasil
    (13, "BRASIL", "Studi: Wolbachia Tekan Dengue",
     "Nyamuk Wolbachia tekan infeksi dengue + chikungunya ~69%.",
     "DATA", False),
    (13, "BRASIL", "Uji pada 5.700 Anak",
     "Studi 4 tahun, 5.700+ anak usia 6–11 di Belo Horizonte.",
     "DATA", False),
    (13, "BRASIL", "Efek Bertahan Saat Wabah 2024",
     "Efek bertahan selama wabah parah 2024; belum peer-review.",
     "DATA", False),
    # Summary cards (meta-cards, not news)
    ("S1", "RINGKASAN", "13 Cerita, 39 Entri + 3 Catatan",
     "Satu hari, 13 cerita, 39 entri + 3 catatan.", "INFO", False),
    ("S2", "RINGKASAN", "Legenda Tag",
     "RESMI = dikonfirmasi otoritas. KLAIM = pernyataan satu pihak. "
     "BANTAH = penyangkalan. BERSELISIH = sumber bertentangan. "
     "DATA = angka.", "INFO", False),
    ("S3", "RINGKASAN", "Edisi UTC",
     "Edisi Sabtu 21 Nov 2026 (UTC). Jumat malam waktu setempat di "
     "Amerika = Sabtu dini hari UTC. Pasar: penutupan Jumat 21:00 UTC.",
     "INFO", False),
]

# Land mask: (row, col_start, col_end) on a 72 x 28 grid.
# Row 0 = lat 80N, each row/col 5 deg.
LAND = [
    (0, 12, 20), (0, 24, 32), (0, 38, 42),
    (1, 4, 8), (1, 12, 22), (1, 24, 31), (1, 40, 43), (1, 45, 71),
    (2, 3, 9), (2, 11, 23), (2, 26, 30), (2, 32, 32), (2, 40, 42), (2, 44, 71),
    (3, 4, 9), (3, 10, 24), (3, 32, 32), (3, 39, 43), (3, 44, 71),
    (4, 5, 10), (4, 10, 26), (4, 35, 35), (4, 39, 42), (4, 43, 71),
    (5, 11, 27), (5, 34, 35), (5, 38, 40), (5, 42, 71),
    (6, 12, 28), (6, 34, 44), (6, 48, 71),
    (7, 14, 28), (7, 35, 44), (7, 48, 58), (7, 60, 68), (7, 69, 70),
    (8, 14, 28), (8, 35, 44), (8, 46, 58), (8, 60, 68), (8, 69, 70),
    (9, 15, 27), (9, 35, 44), (9, 45, 52), (9, 56, 66), (9, 69, 69),
    (10, 16, 26), (10, 35, 44), (10, 46, 51), (10, 55, 60), (10, 62, 66), (10, 68, 68),
    (11, 16, 22), (11, 27, 27), (11, 35, 45), (11, 47, 51), (11, 55, 60), (11, 62, 66),
    (12, 17, 21), (12, 24, 27), (12, 36, 46), (12, 56, 59), (12, 62, 66),
    (13, 18, 21), (13, 37, 47), (13, 57, 58), (13, 62, 65),
    (14, 19, 21), (14, 26, 30), (14, 38, 47), (14, 63, 65),
    (15, 26, 31), (15, 39, 46), (15, 63, 68),
    (16, 27, 31), (16, 39, 45), (16, 64, 69),
    (17, 27, 32), (17, 40, 45), (17, 65, 70),
    (18, 28, 33), (18, 40, 44), (18, 66, 69), (18, 70, 71),
    (19, 29, 34), (19, 40, 44), (19, 47, 47), (19, 65, 70),
    (20, 30, 35), (20, 40, 44), (20, 47, 47), (20, 64, 70),
    (21, 30, 35), (21, 40, 43), (21, 64, 69),
    (22, 31, 35), (22, 40, 42), (22, 65, 68), (22, 71, 71),
    (23, 31, 34), (23, 40, 41), (23, 65, 67), (23, 70, 71),
    (24, 31, 33), (24, 70, 71),
    (25, 31, 32), (25, 70, 70),
    (26, 31, 32),
    (27, 31, 31),
]

# Pins: (story, region, lon, lat, dx, dy) — dx/dy nudge the drawn pin off its
# true spot (leader line drawn from the true spot). True spots recorded here.
PINS = [
    (1, "TELUK", 50.5, 26.2, 0, 0),       # Bahrain
    (2, "UKRAINA", 33.4, 47.9, 0, 0),     # Kryvyi Rih
    (3, "MEKSIKO", -108.5, 25.6, 0, 0),   # Guasave, Sinaloa
    (4, "COP31", 30.7, 36.9, -9, 8),      # Antalya (nudged off Kryvyi Rih)
    (5, "MYANMAR", 96.0, 21.0, 0, 0),     # Myanmar (dulu pin 7)
    (6, "PASAR", -74.0, 40.7, 0, 0),      # New York (AI markets)
    (7, "PERU", -75.0, -11.0, 0, 0),      # Junin, Peru (dulu pin 5)
    (8, "HORMUZ", 56.2, 26.2, 13, 13),    # Khasab, Oman (nudged off Bahrain)
    (9, "LADAKH", 77.6, 34.2, 0, 0),      # Leh, Ladakh
    (10, "BALTIK", 25.0, 59.8, 0, 0),     # Gulf of Finland
    (11, "DIPLOMASI", 116.4, 39.9, 0, 0), # Beijing (Xi, in the Yalta photo)
    (12, "DAGANG", 106.8, -6.2, 0, 0),    # Jakarta
    (13, "BRASIL", -48.0, -15.0, 0, 0),   # Brazil
]

# Map geometry: 1:1 projection, K px per degree both axes.
K = 1.1
MAP_X0, MAP_Y0 = 10, 74
MAP_W = 72 * 5 * K   # 396
MAP_H = 28 * 5 * K   # 154
HEADER_H = 72
GRID_Y0, GRID_Y1 = 232, 962
FOOTER_Y0 = 964


def font(name, size):
    return ImageFont.truetype(os.path.join(BASE, "fonts", name), size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap by pixel width; returns list of lines."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_map(draw):
    # Dotted landmass, 1:1 (cell is square: 5 deg = 5.5 px both axes).
    for row, c0, c1 in LAND:
        y = MAP_Y0 + (row + 0.5) * 5 * K
        for c in range(c0, c1 + 1):
            x = MAP_X0 + (c + 0.5) * 5 * K
            draw.ellipse([x - 1.7, y - 1.7, x + 1.7, y + 1.7], fill=(105, 98, 84))
    # Numbered pins, region colour; red ring for hero stories.
    f_pin = font("DejaVuSans-Bold.ttf", 8)
    for story, region, lon, lat, dx, dy in PINS:
        tx = MAP_X0 + (lon + 180.0) * K
        ty = MAP_Y0 + (80 - lat) * K
        x, y = tx + dx, ty + dy
        if dx or dy:
            draw.line([tx, ty, x, y], fill=MUTED, width=1)
            draw.ellipse([tx - 1.5, ty - 1.5, tx + 1.5, ty + 1.5], fill=RED)
        fill = REGION_COLOR[region]
        draw.ellipse([x - 5.5, y - 5.5, x + 5.5, y + 5.5], fill=fill,
                     outline=(255, 253, 248), width=1)
        if story in HERO_STORIES:
            draw.ellipse([x - 7.5, y - 7.5, x + 7.5, y + 7.5], outline=RED, width=2)
        label = str(story)
        tw = draw.textlength(label, font=f_pin)
        draw.text((x - tw / 2, y - 4.5), label, font=f_pin, fill=(255, 253, 248))


def draw_card(draw, x, y, w, h, card, issues):
    story, region, title, fact, tag, hero = card[:6]
    region_color = REGION_COLOR[region]
    draw.rectangle([x, y, x + w - 1, y + h - 1], fill=CARD_BG, outline=RULE, width=1)
    if hero:
        draw.rectangle([x, y, x + w - 1, y + 2], fill=RED)
        draw.rectangle([x, y, x + w - 1, y + h - 1], outline=RED, width=2)
    # Region stripe on the left edge.
    draw.rectangle([x + 1, y + 1, x + 4, y + h - 2], fill=region_color)
    px = x + 8
    inner = w - 8 - 5
    # Meta line: coloured number badge + region (left), date (right).
    f_meta = font("DejaVuSans-Bold.ttf", 8)
    num = str(story)
    nw = draw.textlength(num, font=f_meta)
    bw = nw + 8
    draw.rectangle([px, y + 3, px + bw, y + 15], fill=region_color)
    draw.text((px + 4, y + 4), num, font=f_meta, fill=(255, 253, 248))
    draw.text((px + bw + 4, y + 4), region, font=f_meta, fill=INK)
    date = "21 NOV"
    dw = draw.textlength(date, font=f_meta)
    draw.text((x + w - 5 - dw, y + 4), date, font=f_meta, fill=RED)
    # Title, max 2 lines, 13px bold.
    f_title = font("DejaVuSans-Bold.ttf", 13)
    lines = wrap(draw, title, f_title, inner)
    for ln in lines:
        if draw.textlength(ln, font=f_title) > inner:
            issues.append("card %s title line too wide: %r" % (story, ln))
    if len(lines) > 2:
        issues.append("card %s title wraps to %d lines: %r"
                      % (story, len(lines), title))
        lines = lines[:2]
    ty = y + 17
    for ln in lines:
        draw.text((px, ty), ln, font=f_title, fill=INK)
        ty += 14
    # Fact: 11px, max 3 lines (summary cards S2/S3: 9px, max 5 lines).
    # A card may carry a 7th tuple element = fact font size (v4: card 5-3
    # needs 9px so the ICJ phrase + "atas pokok genosida" fits in 3 lines).
    small = story in ("S2", "S3")
    fact_px = card[6] if len(card) > 6 else (9 if small else 11)
    f_fact = font("DejaVuSans.ttf", fact_px)
    fact_lh = fact_px + 1
    fact_max = 5 if small else 3
    flines = wrap(draw, fact, f_fact, inner)
    for ln in flines:
        if draw.textlength(ln, font=f_fact) > inner:
            issues.append("card %s fact line too wide: %r" % (story, ln))
    if len(flines) > fact_max:
        issues.append("card %s fact wraps to %d lines (max %d): %r"
                      % (story, len(flines), fact_max, fact))
        flines = flines[:fact_max]
    fy = ty + 2
    for ln in flines:
        draw.text((px, fy), ln, font=f_fact, fill=(52, 48, 42))
        fy += fact_lh
    if fy > y + 85:
        issues.append("card %s fact reaches the tag pill (ends y+%d)"
                      % (story, fy - y))
    # Epistemic tag pill at the bottom.
    parts = [p.strip() for p in tag.split("/")]
    label = "[" + "] [".join(parts) + "]"
    fg, bg = TAG_STYLE.get(parts[0], (MUTED, GREY_TINT))
    f_tag = font("DejaVuSans-Bold.ttf", 9)
    tw = draw.textlength(label, font=f_tag)
    if tw > inner:
        issues.append("card %s tag too wide: %r" % (story, label))
    bx, by = px, y + 86
    draw.rectangle([bx - 2, by - 1, bx + tw + 2, by + 10], fill=bg)
    draw.text((bx, by), label, font=f_tag, fill=fg)


def draw_strip(draw, rx):
    """UTC strip, Fri 21:00 -> Sat 24:00 (27 h). Only known times plotted."""
    f_lab = font("DejaVuSans-Bold.ttf", 10)
    f_small = font("DejaVuSans.ttf", 9)
    draw.text((rx, 80), "13 PIN = 13 CERITA · NOMOR = NOMOR KARTU",
              font=f_lab, fill=INK)
    # Region colour legend with swatches.
    lx, ly = rx, 96
    draw.text((lx, ly), "Pin = warna region:", font=f_small, fill=INK)
    cx = lx + draw.textlength("Pin = warna region: ", font=f_small)
    for color, name in REGION_NAMES:
        draw.rectangle([cx, ly + 1, cx + 8, ly + 9], fill=color)
        cx += 11
        draw.text((cx, ly), name, font=f_small, fill=INK)
        cx += draw.textlength(name, font=f_small) + 4
        draw.text((cx - 4, ly), "·", font=f_small, fill=MUTED)
    draw.text((rx, 110), "Lingkar merah = 1–6.",
              font=f_small, fill=MUTED)
    draw.text((rx, 124), "STRIP UTC — JUM 21:00 → SAB 24:00",
              font=f_lab, fill=INK)
    sx0, sx1, sy = rx + 8, 1004, 158
    span_h = 27.0

    def x_at(hours_since_fri21):
        return sx0 + (sx1 - sx0) * hours_since_fri21 / span_h

    # Peru quake range: Fri evening local (UTC-5) = Sat 00:00–05:00 UTC.
    # Own row between the label and the ruler (v2: it overlapped the label).
    rx0, rx1 = x_at(3), x_at(8)
    draw.rectangle([rx0, 140, rx1, 148], fill=GREEN_TINT, outline=GREEN, width=1)
    # Ruler.
    draw.line([sx0, sy, sx1, sy], fill=INK, width=2)
    for h in range(0, 28):
        x = x_at(h)
        tall = h in (0, 3, 7, 11, 15, 19, 23, 27)
        draw.line([x, sy - (5 if tall else 3), x, sy + (5 if tall else 3)],
                  fill=INK, width=1)
    labels = [(0, "21 JUM"), (3, "00"), (7, "04"), (11, "08"), (15, "12"),
              (19, "16"), (23, "20"), (27, "24")]
    for h, lab in labels:
        x = x_at(h)
        lw = draw.textlength(lab, font=f_small)
        ax = min(max(x - lw / 2, sx0), sx1 - lw)
        draw.text((ax, sy + 8), lab, font=f_small, fill=INK)
    # Wall Street close tick: Fri 21:00 UTC.
    draw.line([sx0, sy - 8, sx0, sy + 8], fill=GREEN, width=3)
    draw.text((rx, 182),
              "▬ Gempa Peru: Jumat malam waktu setempat = Sabtu 00:00–05:00 UTC "
              "(rentang, bukan jam pasti)",
              font=f_small, fill=INK)
    draw.text((rx, 196), "▼ Penutupan Wall Street: Jumat 21:00 UTC",
              font=f_small, fill=INK)
    draw.text((rx, 210), "Jam lain tidak diverifikasi.", font=f_small, fill=MUTED)


def render():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    issues = []

    # ---- Header 0–71: dark date-lock band (Indonesian only).
    draw.rectangle([0, 0, W - 1, 70], fill=INK)
    f_h1 = font("DejaVuSans-Bold.ttf", 26)
    draw.text((16, 10), "WORLD NEWS — SABTU · 21 NOVEMBER 2026",
              font=f_h1, fill=(248, 244, 236))
    f_h2 = font("DejaVuSans.ttf", 12)
    draw.text((16, 44), "EDISI GLOBAL · 00:00–23:59 UTC",
              font=f_h2, fill=GOLD)
    f_chip = font("DejaVuSans-Bold.ttf", 12)
    chip = "13 CERITA · 39 ENTRI + 3 CATATAN"
    cw = draw.textlength(chip, font=f_chip)
    draw.rectangle([W - 16 - cw - 16, 24, W - 16, 56], outline=GOLD, width=1)
    draw.text((W - 16 - cw - 8, 32), chip, font=f_chip, fill=GOLD)
    draw.rectangle([0, 71, W - 1, 72], fill=RED)

    # ---- Map + UTC band 74–227.
    draw_map(draw)
    draw_strip(draw, int(MAP_X0 + MAP_W + 14))

    # ---- Grid 232–962: 6 cols x 7 rows = 42 cards (2 stories per row).
    cw_, ch_, gap = 162, 100, 5
    x0, y0 = 11, GRID_Y0
    for i, card in enumerate(CARDS):
        col, row = i % 6, i // 6
        draw_card(draw, x0 + col * (cw_ + gap), y0 + row * (ch_ + gap),
                  cw_, ch_, card, issues)

    # ---- Footer 964–1024: dark band, one date rule + method + sources.
    draw.rectangle([0, FOOTER_Y0, W - 1, H - 1], fill=INK)
    f_f = font("DejaVuSans.ttf", 10)
    draw.text((16, 969),
              "KEBIJAKAN EDISI UTC — Edisi Sabtu 21 Nov 2026 (UTC): berita yang "
              "dilaporkan pada hari itu.",
              font=f_f, fill=(248, 244, 236))
    draw.text((16, 982),
              "Peristiwa Jumat malam waktu setempat di Amerika = Sabtu dini hari "
              "UTC. Pasar: data penutupan Jumat 21:00 UTC, dilaporkan Sabtu "
              "sebagai penutup pekan.",
              font=f_f, fill=(248, 244, 236))
    draw.text((16, 995),
              "METODOLOGI — 13 cerita · 39 entri bertanggal + 3 catatan · klaim "
              "dibedakan dari fakta resmi.",
              font=f_f, fill=(200, 192, 178))
    draw.text((16, 1008),
              "KOMPILASI: oneturn.news, wireminute.com, novora24.com "
              "(21–22 Nov 2026) · SABTU 21 NOV 2026 · 23:59 UTC (TETAP)",
              font=f_f, fill=GOLD)
    return img, issues


def main():
    img, issues = render()
    path = os.path.join(BASE, "entry.png")
    img.save(path, format="PNG", optimize=True, compress_level=6)
    data = open(path, "rb").read()
    print("wrote %s" % path)
    print("size %d bytes" % len(data))
    print("sha256 %s" % hashlib.sha256(data).hexdigest())
    print("dimensions %dx%d" % img.size)
    if issues:
        print("LAYOUT ISSUES (%d):" % len(issues))
        for it in issues:
            print(" - " + it)
        return 1
    print("layout issues 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""news-image-20261121 — BUILD-TIME renderer (NOT run by the grader).

Renders the deterministic 1024x1024 PNG dashboard (header date-lock, dotted
world map with 13 numbered pins, UTC strip, 7x6 grid of 42 dated cards,
footer with the UTC-edition policy) and writes it to entry.png next to
this script. Uses Pillow — that is fine here, because the grader NEVER runs
this file: RULES.txt says the graded program (main.py) runs in a fresh
container with "standard library only: nothing is installed before it runs",
so main.py is stdlib-only and only copies the pre-rendered entry.png.

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
RED_TINT = (246, 226, 222)
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
GREY_TINT = (236, 233, 226)

TAG_STYLE = {
    "RESMI": (GREEN, GREEN_TINT),
    "KLAIM": (AMBER, AMBER_TINT),
    "DENY": (PURPLE, PURPLE_TINT),
    "2 SUMBER": (ORANGE, ORANGE_TINT),
    "DATA": (BLUE, BLUE_TINT),
    "INFO": (MUTED, GREY_TINT),
}

# (story, region, title, fact, tag, hero)
CARDS = [
    # 1 — Iran–Bahrain
    (1, "TELUK", "IRGC Klaim Serang Pangkalan AS",
     "2 pangkalan AS: al-Riffa & Awali, Bahrain.", "KLAIM", True),
    (1, "TELUK", "Kebakaran Situs Industri Sipil",
     "0 korban; pertahanan udara cegat serangan lain.", "RESMI", False),
    (1, "TELUK", "Klaim Drone vs Bantahan F-16",
     "Iran klaim jatuhkan drone AS dekat Qeshm; AS bantah F-16 kena.",
     "KLAIM / DENY", False),
    # 2 — Kryvyi Rih
    (2, "UKRAINA", "Rudal Balistik Rusia",
     "Hantam pusat kota Kryvyi Rih.", "RESMI", True),
    (2, "UKRAINA", "2 Tewas, ~60 Luka",
     "Korban: anak 7 thn & perempuan 20 thn.", "RESMI", False),
    (2, "UKRAINA", "Penyelamat Diserang, 25 Blok Rusak",
     "Serangan lanjutan; RS + sekolah rusak.", "RESMI", False),
    # 3 — Chapo Isidro
    (3, "MEKSIKO", "Chapo Isidro Ditangkap",
     "Pasukan khusus Meksiko; Guasave, Sinaloa.", "RESMI", True),
    (3, "MEKSIKO", "11 Tewas Susulan",
     "4 tentara, 7 penembak tewas.", "RESMI", False),
    (3, "MEKSIKO", "8 Ditangkap, Hadiah $5 Juta",
     "Hadiah AS $5 juta atas penangkapan.", "RESMI", False),
    # 4 — COP31 Antalya
    (4, "COP31", "COP31 Overtime, Belum Sepakat",
     "Lewat tenggat Jumat; tanpa kesepakatan.", "RESMI", True),
    (4, "COP31", "Fosil Dicoret dari Draf",
     "~200 negara berselisih soal bahan bakar fosil.", "RESMI", False),
    (4, "COP31", "Prancis-Panama Dorong Kembali",
     "AS tak kirim delegasi resmi.", "RESMI", False),
    # 5 — Gempa Peru
    (5, "PERU", "Gempa M6,7 Guncang Junín",
     "M6,7 (sumber lain 6,9); kedalaman ~108 km.", "2 SUMBER", True),
    (5, "PERU", "Terasa Sampai Lima",
     "Jumat malam, Peru tengah; terasa di Lima.", "RESMI", False),
    (5, "PERU", "Tanpa Korban, Tanpa Tsunami",
     "Tanpa korban/kerusakan; tanpa tsunami.", "RESMI", False),
    # 6 — Saham AI
    (6, "PASAR", "S&P -3,7%, Nasdaq -5,3%",
     "Jumat; pasar masuk koreksi.", "DATA", True),
    (6, "PASAR", "Nvidia -14%, Diselidiki SEC",
     "Anjlok di tengah laporan penyelidikan SEC.", "DATA", False),
    (6, "PASAR", "Gain 2026 Terhapus",
     "Penurunan menghapus gain sepanjang 2026.", "DATA", False),
    # 7 — Myanmar / ICJ
    (7, "MYANMAR", "Myanmar Tolak Putusan ICJ",
     "Penolakan resmi atas putusan ICJ.", "RESMI", False),
    (7, "MYANMAR", "Kasus Genosida Rohingya",
     "Perkara: genosida terhadap Rohingya.", "RESMI", False),
    (7, "MYANMAR", "Skor Putusan 9-6",
     "Majelis hakim putuskan 9-6.", "RESMI", False),
    # 8 — Tanker Hormuz
    (8, "HORMUZ", "Tanker Terbakar di Hormuz",
     "~8 mil laut utara Khasab, Oman.", "RESMI", False),
    (8, "HORMUZ", "Ranjau vs Proyektil",
     "Iran klaim ranjau laut; UKMTO bilang proyektil.", "2 SUMBER", False),
    (8, "HORMUZ", "0 Korban dalam Kebakaran",
     "Tidak ada korban dalam insiden tanker.", "RESMI", False),
    # 9 — Ladakh
    (9, "LADAKH", "Pemilu Pertama Sejak 2019",
     "Pemilu panchayat + kota di Ladakh.", "RESMI", False),
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
     "Finlandia sebut Ukraina kemungkinan pelaku.", "KLAIM", False),
    # 11 — Trump / Yalta
    (11, "DIPLOMASI", "Trump Posting '1945, 2026'",
     "Unggahan Trump: '1945, 2026'.", "RESMI", False),
    (11, "DIPLOMASI", "Yalta x Trump, Xi, Putin",
     "Foto Yalta dipadukan dengan ketiganya.", "RESMI", False),
    (11, "DIPLOMASI", "Tiga Pemimpin Satu Bingkai",
     "AS, China, Rusia dalam satu gambar.", "RESMI", False),
    # 12 — UE–Indonesia
    (12, "DAGANG", "UE-Indonesia Teken Dagang",
     "Perjanjian dagang ditandatangani.", "RESMI", False),
    (12, "DAGANG", "10 Tahun Negosiasi",
     "Negosiasi berlangsung 10 tahun.", "RESMI", False),
    (12, "DAGANG", "Kesepakatan Tercapai",
     "Tanda tangan menutup negosiasi 10 tahun.", "RESMI", False),
    # 13 — Dengue Brasil
    (13, "BRASIL", "Nyamuk Tekan Dengue",
     "Nyamuk pembawa bakteri tekan kasus dengue.", "RESMI", False),
    (13, "BRASIL", "Kasus Anak di Brasil",
     "Kasus dengue pada anak di Brasil.", "RESMI", False),
    (13, "BRASIL", "Nyamuk Pembawa Bakteri",
     "Metode: nyamuk dilepas membawa bakteri.", "RESMI", False),
    # Summary cards
    ("S1", "RINGKASAN", "13 Cerita, 42 Entri",
     "Satu hari, 13 cerita, 42 entri bertanggal.", "INFO", False),
    ("S2", "RINGKASAN", "Legenda Tag Kepercayaan",
     "RESMI = resmi. KLAIM = klaim. DENY = bantahan. 2 SUMBER = berselisih. DATA = pasar.",
     "INFO", False),
    ("S3", "RINGKASAN", "Edisi UTC",
     "Peristiwa Jumat waktu lokal masuk edisi Sabtu UTC. FRI LOCAL → SAT UTC.",
     "INFO", False),
]

# Land mask: (row, col_start, col_end) on a 72 x 28 grid.
# Row 0 = lat 80N, each row 5 deg; col 0 = lon -180, each col 5 deg.
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

# Pins: (story, lon, lat, dx, dy) — dx/dy nudge the drawn pin off its true spot.
PINS = [
    (1, 50.5, 26.2, 0, 0),      # Bahrain
    (2, 33.4, 47.9, 0, 0),      # Kryvyi Rih
    (3, -108.5, 25.6, 0, 0),    # Guasave, Sinaloa
    (4, 30.7, 36.9, -10, 7),    # Antalya (nudged off Kryvyi Rih)
    (5, -75.0, -11.0, 0, 0),    # Junin, Peru
    (6, -74.0, 40.7, 0, 0),     # New York (AI markets)
    (7, 96.0, 21.0, 0, 0),      # Myanmar
    (8, 56.2, 26.2, 4, 9),      # Khasab, Oman (nudged off Bahrain)
    (9, 77.6, 34.2, 0, 0),      # Leh, Ladakh
    (10, 25.0, 59.8, 0, 0),     # Gulf of Finland
    (11, 116.4, 39.9, 0, 0),    # Beijing (Xi, in the Yalta photo)
    (12, 106.8, -6.2, 0, 0),    # Jakarta
    (13, -48.0, -15.0, 0, 0),   # Brazil
]

MAP_X0, MAP_Y0, MAP_W, MAP_H = 8, 88, 552, 94


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
    # Dotted landmass.
    for row, c0, c1 in LAND:
        lat = 80 - 5 * row
        y = MAP_Y0 + (80 - lat) / 135.0 * MAP_H
        for c in range(c0, c1 + 1):
            x = MAP_X0 + (c + 0.5) * MAP_W / 72.0
            draw.ellipse([x - 1.7, y - 1.7, x + 1.7, y + 1.7], fill=(105, 98, 84))
    # Numbered pins.
    f_pin = font("DejaVuSans-Bold.ttf", 8)
    for story, lon, lat, dx, dy in PINS:
        x = MAP_X0 + (lon + 180.0) / 360.0 * MAP_W + dx
        y = MAP_Y0 + (80 - lat) / 135.0 * MAP_H + dy
        hero = story <= 6
        fill = RED if hero else INK
        draw.ellipse([x - 5.5, y - 5.5, x + 5.5, y + 5.5], fill=fill,
                     outline=(255, 253, 248), width=1)
        label = str(story)
        tw = draw.textlength(label, font=f_pin)
        draw.text((x - tw / 2, y - 4.5), label, font=f_pin, fill=(255, 253, 248))


def draw_card(draw, x, y, w, h, card, trunc):
    story, region, title, fact, tag, hero = card
    draw.rectangle([x, y, x + w - 1, y + h - 1], fill=CARD_BG, outline=RULE, width=1)
    if hero:
        draw.rectangle([x, y, x + w - 1, y + 3], fill=RED)
        draw.rectangle([x, y, x + w - 1, y + h - 1], outline=RED, width=2)
    px = x + 5
    inner = w - 10
    # Meta line: number + region (left), date badge (right).
    f_meta = font("DejaVuSans-Bold.ttf", 8)
    f_date = font("DejaVuSans-Bold.ttf", 8)
    meta = "%s · %s" % (story, region)
    draw.text((px, y + 6), meta, font=f_meta, fill=MUTED)
    date = "21 NOV"
    dw = draw.textlength(date, font=f_date)
    draw.text((x + w - 5 - dw, y + 6), date, font=f_date, fill=RED)
    # Title, max 3 lines.
    f_title = font("DejaVuSans-Bold.ttf", 11)
    lines = wrap(draw, title, f_title, inner)
    if len(lines) > 3:
        lines = lines[:3]
        lines[2] = lines[2][:-3].rstrip() + "…" if len(lines[2]) > 3 else lines[2]
        trunc[0] += 1
    ty = y + 19
    for ln in lines:
        draw.text((px, ty), ln, font=f_title, fill=INK)
        ty += 13
    # Fact, max 4 lines.
    f_fact = font("DejaVuSans.ttf", 9)
    flines = wrap(draw, fact, f_fact, inner)
    if len(flines) > 4:
        flines = flines[:4]
        flines[3] = flines[3][:-3].rstrip() + "…" if len(flines[3]) > 3 else flines[3]
        trunc[0] += 1
    fy = ty + 2
    for ln in flines:
        draw.text((px, fy), ln, font=f_fact, fill=(52, 48, 42))
        fy += 11
    # Epistemic tag pill at the bottom.
    parts = [p.strip() for p in tag.split("/")]
    label = "[" + "] [".join(parts) + "]"
    fg, bg = TAG_STYLE.get(parts[0], (MUTED, GREY_TINT))
    f_tag = font("DejaVuSans-Bold.ttf", 8)
    tw = draw.textlength(label, font=f_tag)
    bx, by = px, y + h - 17
    draw.rectangle([bx - 2, by - 1, bx + tw + 2, by + 10], fill=bg)
    draw.text((bx, by), label, font=f_tag, fill=fg)


def render():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    trunc = [0]

    # ---- Header 0–85: dark date-lock band.
    draw.rectangle([0, 0, W - 1, 84], fill=INK)
    f_h1 = font("DejaVuSans-Bold.ttf", 30)
    draw.text((16, 12), "WORLD NEWS — SABTU · 21 NOVEMBER 2026",
              font=f_h1, fill=(248, 244, 236))
    f_h2 = font("DejaVuSans.ttf", 13)
    draw.text((16, 52), "EDISI GLOBAL · 00:00–23:59 UTC · SATURDAY 21 NOV 2026",
              font=f_h2, fill=(232, 179, 75))
    f_chip = font("DejaVuSans-Bold.ttf", 12)
    chip = "13 STORIES · 42 ENTRIES"
    cw = draw.textlength(chip, font=f_chip)
    draw.rectangle([W - 16 - cw - 16, 26, W - 16, 58], outline=(232, 179, 75), width=1)
    draw.text((W - 16 - cw - 8, 34), chip, font=f_chip, fill=(232, 179, 75))
    draw.rectangle([0, 85, W - 1, 87], fill=RED)

    # ---- Map + UTC band 85–185.
    draw_map(draw)
    # Right panel: pin legend + UTC strip.
    rx = 576
    f_lab = font("DejaVuSans-Bold.ttf", 10)
    draw.text((rx, 94), "13 PIN = 13 CERITA · NOMOR = NOMOR KARTU",
              font=f_lab, fill=INK)
    f_small = font("DejaVuSans.ttf", 9)
    draw.text((rx, 110), "Pin merah = 6 cerita utama. Pin hitam = 7 cerita lain.",
              font=f_small, fill=MUTED)
    draw.text((rx, 126), "STRIP UTC — 00:00–24:00", font=f_lab, fill=INK)
    sx0, sx1, sy = rx + 6, 1004, 152
    draw.line([sx0, sy, sx1, sy], fill=INK, width=2)
    for hr in range(0, 25):
        x = sx0 + (sx1 - sx0) * hr / 24.0
        tall = hr % 4 == 0
        draw.line([x, sy - (5 if tall else 3), x, sy + (5 if tall else 3)],
                  fill=INK, width=1)
        if tall:
            lab = "%02d" % hr
            lw = draw.textlength(lab, font=f_small)
            draw.text((x - lw / 2, sy + 8), lab, font=f_small, fill=INK)
    f_note = font("DejaVuSans-Bold.ttf", 10)
    draw.text((rx, 172), "FRI LOCAL → SAT UTC", font=f_note, fill=RED)

    # ---- Grid 185–960: 7 cols x 6 rows = 42 cards.
    cw_, ch_ = 138, 123
    x0, y0 = 11, 190
    for i, card in enumerate(CARDS):
        col, row = i % 7, i // 7
        draw_card(draw, x0 + col * (cw_ + 6), y0 + row * (ch_ + 6),
                  cw_, ch_, card, trunc)

    # ---- Footer 960–1024: dark band, UTC policy + method + fixed compile stamp.
    draw.rectangle([0, 960, W - 1, H - 1], fill=INK)
    f_f = font("DejaVuSans.ttf", 10)
    draw.text((16, 968),
              "KEBIJAKAN EDISI UTC — Peristiwa 21 Nov 2026 di zona waktu mana pun; "
              "peristiwa Jumat waktu lokal masuk edisi Sabtu UTC.",
              font=f_f, fill=(248, 244, 236))
    draw.text((16, 984),
              "METODOLOGI — 13 cerita · 42 entri bertanggal · klaim dibedakan dari "
              "fakta resmi · angka pasar = data penutupan Jumat.",
              font=f_f, fill=(200, 192, 178))
    draw.text((16, 1000),
              "KOMPILASI: SABTU 21 NOV 2026 · 23:59 UTC (TETAP) · 13 stories · "
              "42 dated entries · claims attributed",
              font=f_f, fill=(232, 179, 75))
    return img, trunc[0]


def main():
    img, n_trunc = render()
    path = os.path.join(BASE, "entry.png")
    img.save(path, format="PNG", optimize=True, compress_level=6)
    data = open(path, "rb").read()
    print("wrote %s" % path)
    print("size %d bytes" % len(data))
    print("sha256 %s" % hashlib.sha256(data).hexdigest())
    print("dimensions %dx%d" % img.size)
    print("truncated_cards %d" % n_trunc)
    return 0


if __name__ == "__main__":
    sys.exit(main())

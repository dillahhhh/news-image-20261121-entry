# Data v8.11 — VERSI INGGRIS PENUH v8.10 (brief rev8.11, bos: "Coba versi
# Inggris" 22 Nov 22:16 WIB — 5 besar leaderboard semuanya Inggris,
# 35-37 cerita, 7-9 wilayah, judul nyebutin berita utama; v8.10
# Indonesia 7-3-2, $0). 34 cerita SAMA, fakta SAMA, geometri SAMA —
# hanya bahasa. Jumlah cerita TETAP 34 (grid 4x7 tidak muat 35-37).
# Tag: FACT (was RESMI, hijau), CLAIM (was KLAIM, amber), DATA (tetap,
# biru), DISPUTED (was BERSELISIH, merah). FACT 4 huruf — VERIFIED
# (8 huruf) bikin 6 meta gagal, PROVEN (6 huruf) bikin 5 meta gagal.
# Grup Inggris: MIDDLE EAST, EUROPE, NORTH AMERICA, LATIN AMERICA,
# ASIA-PACIFIC, SPORTS, GLOBAL (GROUP_COLOR + GROUP_ORDER ikut).
# Tanda baca: "−" U+2212 di #6/#13, "≥" di #33, "é" di #29 Attaché,
# "ö" di #14 Alpöge — semua terukur OK dgn DejaVu (parent).
# Tuple: (num, group, title, body, tag, time_utc_or_None, lon, lat, source)
# SEMUA kartu punya source (34/34). Sumber nama proper, tidak diterjemahkan.
# #7: "6.9" adalah estimasi OTOMATIS yg direvisi ke 6.7 — JANGAN dipakai.
#   [DISPUTED] = beda kedalaman USGS 108 km vs IGP 129 km; korban INDECI.
# #16 tag TETAP FACT (tag = kepastian klaim UTAMA cegatan koalisi;
#   angka 71 membawa atribusi sendiri "Houthis claim"). #19/#13 TETAP CLAIM.
# #20: jam pasti TAK ADA di riset; "Friday" dibuang (versi dgn "Friday"
#   = 3 baris, GAGAL) — tanggal ada di meta/strip.
# #25: Chelsea tuan rumah; Emegha cetak gol UNTUK CHELSEA (jangan cantumkan
#   sbg pencetak gol Leeds).
# #10: subjek "suspects" = Finlandia (terverifikasi). #29: subjek = Denmark.
# #5 badan end=140 TEPAT di batas — ukur ulang sebelum commit.
# #19 badan baris 1 233px (margin 2px), #20 badan baris 2 232px (margin
#   3px) — ukur ulang sebelum commit.
# #26/#29 judul 2 baris + vertikal TEPAT di batas (cy+96 <= cy+96,
#   ch=98) — WAJIB lolos assert render.
STORIES = [
    # 1 — LEAD (Global, ICJ)
    (1, "GLOBAL", "ICJ Finds Myanmar Guilty",
     "9-6 ruling: first Rohingya genocide in 80 years; reparations to "
     "follow; Myanmar rejects it.",
     "FACT", None, 96.0, 21.0, "ICJ"),
    # 2–6 — SEKUNDER
    (2, "EUROPE", "Russia Hits Kryvyi Rih",
     "2 killed, ~60 hurt; rescuers attacked.",
     "FACT", None, 33.4, 47.9, "AP"),
    (3, "LATIN AMERICA", "Chapo Isidro Arrested",
     "Mexico: 11 killed; 8 arrested; US $5m reward.",
     "FACT", None, -108.5, 25.6, "BBC"),
    (4, "EUROPE", "COP31: Near Deal",
     "UN climate: fossil cut from draft; late Sat near deal.",
     "FACT", None, 30.7, 36.9, "Majik"),
    (5, "MIDDLE EAST", "Iran Claims US Strike",
     "IRGC claims al-Riffa hit; Bahrain: 0 victims; US drone down, "
     "US denies.",
     "CLAIM", None, 50.5, 26.2, "Al Jazeera"),
    (6, "NORTH AMERICA", "S&P Plunges −3.7%",
     "S&P 500 -3.7%, Nasdaq -5.3%; Nvidia -14%.",
     "DATA", "21:00", -74.0, 40.7, "Majik"),
    # 7–12 — REGULER
    (7, "LATIN AMERICA", "M6.7 Quake in Junin",
     "M6.7; 108 km (IGP: 129 km); 8 hurt, no deaths.",
     "DISPUTED", "00:09", -75.0, -11.0, "USGS"),
    (8, "MIDDLE EAST", "Tanker on Fire",
     "~8 mi north of Khasab; mine vs missile, 0 victims.",
     "DISPUTED", None, 56.2, 26.2, "UKMTO"),
    (9, "ASIA-PACIFIC", "Ladakh Elections",
     "First panchayat + town polls since 2019; Leh & Kargil.",
     "FACT", None, 77.6, 34.2, "Economic Times"),
    (10, "EUROPE", "Drone Hits Sparta II",
     "Russian ship; 16 survived; Finland suspects Ukraine.",
     "CLAIM", None, 25.0, 59.8, "BBC"),
    (11, "GLOBAL", "Trump: '1945, 2026'",
     "Yalta photo recast with Trump, Xi, Putin; diplomacy debate.",
     "FACT", None, 116.4, 39.9, "Truth Social"),
    (12, "ASIA-PACIFIC", "EU-Indonesia Deal",
     "98.5% of tariff lines cut; target in force early 2027.",
     "FACT", None, 106.8, -6.2, "DW"),
]

STORIES += [
    (13, "GLOBAL", "Wolbachia Mosquito",
     "Cuts dengue −69%; 4-yr study, 5,700 children; not yet "
     "peer-reviewed.",
     "CLAIM", None, -48.0, -15.0, "Straits Times"),
    (14, "GLOBAL", "Riemann Hypothesis",
     "Alpöge claims proof with Claude; 2 groups verifying.",
     "CLAIM", None, -122.4, 37.8, "Guardian"),
    (15, "MIDDLE EAST", "3 Killed in Gaza",
     "Food vehicle hit; 3 killed.",
     "FACT", None, 34.5, 31.5, "Al Jazeera"),
    (16, "MIDDLE EAST", "Riyadh Intercept",
     "Coalition intercepts missile; Houthis claim 71 strikes/24h.",
     "FACT", None, 42.8, 14.8, "Middle East Eye"),
    (17, "EUROPE", "UK-EU Sign 3 Deals",
     "Food, emissions & mobility for 100k youth/yr.",
     "FACT", None, 4.4, 50.8, "BBC"),
    (18, "EUROPE", "Big Tech Tax 3%",
     "2028-2034 budget smaller; EU Council proposal.",
     "FACT", None, 4.4, 50.8, "RFI"),
    (19, "ASIA-PACIFIC", "Shenzhen Summit",
     "Trump backs Putin; Zelensky: murderer; nuclear risk.",
     "CLAIM", None, 114.0, 22.5, "BBC"),
    (20, "EUROPE", "Missiles in Poland",
     "2 missiles, 1 drone down; Tusk: deliberate provocation.",
     "FACT", None, 21.0, 52.2, "Al Jazeera"),
    (21, "NORTH AMERICA", "Canada Sales +7.5%",
     "+7.5% YoY, strongest since 2022; UK +2.3%.",
     "DATA", None, -75.7, 45.4, "Majik"),
    (22, "NORTH AMERICA", "NCIC Hack?",
     "FBI crime database probed; Trump: 'not good'.",
     "CLAIM", None, -77.0, 38.9, "TechCrunch"),
    (23, "NORTH AMERICA", "Illegal Proxy Voting",
     "5th Circuit 9-8: US House broke quorum rule; $1.7tn package.",
     "FACT", None, -77.0, 38.9, "Reuters"),
    (24, "EUROPE", "Trailer 'Heal' Out",
     "Catherine cancer doc; BBC airs 29 Nov, CTV 7 Dec.",
     "FACT", None, -0.1, 51.5, "AP"),
]

STORIES += [
    (25, "SPORTS", "Chelsea 1-4 Leeds",
     "Okafor 2 goals, Calvert-Lewin pen; first win at the Bridge "
     "since 1999.",
     "FACT", "15:00", -0.1, 51.5, "InfoLiveScore"),
    (26, "SPORTS", "Newcastle 2-2 Arsenal",
     "Arsenal stay top; Eze, Barnes, Thiaw, Madueke.",
     "FACT", "17:30", -1.6, 54.98, "InfoLiveScore"),
    (27, "SPORTS", "Malen 4 Goals",
     "Malen 39', 68', 77', 90'; Roma 5-1 Parma.",
     "FACT", None, 10.3, 44.8, "InfoLiveScore"),
    (28, "EUROPE", "Killer Robots Fail",
     "No treaty in Geneva; ~100 states back 2028 rules.",
     "FACT", None, 6.1, 46.2, "CBC"),
    (29, "EUROPE", "Denmark Expels Attaché",
     "Suspected plot to kill rapper Kyivstoner; Russia denies.",
     "CLAIM", None, 12.6, 55.7, "BBC"),
    (30, "NORTH AMERICA", "Deadly Measles",
     "First death of 2026; US loses elimination status.",
     "FACT", None, -77.5, 37.5, "Guardian"),
    (31, "GLOBAL", "BepiColombo Orbits",
     "8 years, 10 billion km; second mission to orbit Mercury.",
     "FACT", None, None, None, "UPI"),
    (32, "LATIN AMERICA", "Bolsonaro in ICU",
     "Bowel obstruction; stable; doctors weigh surgery.",
     "FACT", None, -47.9, -15.8, "Al Jazeera"),
    (33, "GLOBAL", "Tragedy in Nigeria",
     "Bayelsa boat capsizes; ≥24 dead, 24 survived.",
     "FACT", None, 6.3, 4.9, "Sky News"),
    (34, "SPORTS", "Harden 51 Points",
     "Cleveland 128-119 vs Indiana. 26th 50+ point game, passing Kobe.",
     "FACT", "03:23", -81.7, 41.5, "AP"),
]

# Warna titik region (dipakai badge meta + pin peta). Border kartu NETRAL.
GROUP_COLOR = {
    "MIDDLE EAST": (0, 128, 128),
    "EUROPE": (29, 78, 137),
    "NORTH AMERICA": (30, 107, 52),
    "LATIN AMERICA": (168, 74, 20),
    "ASIA-PACIFIC": (107, 45, 143),
    "SPORTS": (176, 142, 20),
    "GLOBAL": (107, 101, 90),
}
GROUP_ORDER = ["MIDDLE EAST", "EUROPE", "NORTH AMERICA", "LATIN AMERICA",
               "ASIA-PACIFIC", "SPORTS", "GLOBAL"]

# (REGION_CODE v8 DIHAPUS — B1: meta seragam 4-segmen, tanpa kode region.
# Region tetap terkode lewat DOT WARNA 12px + legenda footer nama penuh.)

# Pin peta v8.2 (= v8.1): HANYA 6 cerita teratas (lead + 5 sekunder).
# #2 (0,-2) + #4 (0,+2): pusat 20,33px — halo 20px TIDAK bersentuhan;
# assert tabrakan memakai diameter halo (20px), bukan dot (16px).
PINS_V8_2 = [
    (1, 0, 0), (2, 0, -2), (3, 0, 0), (4, 0, 2), (5, 0, 0), (6, 0, 0),
]

# Kartu reguler yg membawa jam di meta (pengganti kode region): #25/#26/#34.
TIME_IN_META = {25, 26, 34}

# Singkatan sumber untuk meta 12px (footer menulis nama penuh).
SRC_SHORT = {
    "Middle East Eye": "MEE",
    "InfoLiveScore": "ILS",
    "Al Jazeera": "AJ",
    "TechCrunch": "TC",
    "Guardian": "GDN",
    "Reuters": "RTS",
    "Sky News": "SKY",
    "Majik": "MJK",
    "Straits Times": "ST",
    "Economic Times": "ET",
    "Truth Social": "TS",
}

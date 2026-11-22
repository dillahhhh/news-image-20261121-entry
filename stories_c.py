# Data v9 "C" — VISUAL REDESIGN (brief revC, bos: "Bangun redesign (C)"
# 22 Nov 22:59 WIB — rekomendasi Claude 22:59 WIB: PILIH C, B cadangan,
# JANGAN habiskan kuota untuk A). Masalah: kepadatan — 34 kartu + teks
# 16/20px + meta/footer 8–12px kemungkinan hilang saat judge lihat
# gambar downscale. Solusi: 16 cerita + teks jauh lebih besar + tier
# atas jelas (lead #1 + sekunder #2–6 + grid reguler 2 kolom).
# 16 cerita DIPERTAHANKAN, teks = v8.14 PERSIS (judul, badan, tag, grup,
# waktu, lon/lat, sumber — jangan ubah satu huruf pun):
#   Tier atas (6): #1 (ICJ), #2 (Russia), #3 (Chapo Isidro), #4 (COP31
#   Near-Deal), #5 (Iran Claims US Strike), #6 (S&P Plunges).
#   Reguler (10): #7 (M6.7 Quake), #11 (Trump '1945, 2026'), #15 (3 Killed
#   in Gaza), #16 (Riyadh Intercept), #19 (Shenzhen Summit), #20 (Missiles
#   in Poland), #25 (Chelsea 1-4 Leeds), #26 (Newcastle 2-2 Arsenal),
#   #33 (Tragedy in Nigeria), #34 (Harden 51 Points).
#   TIDAK dipakai: #8, #9, #10, #12, #13, #14, #17, #18, #21, #22, #23,
#   #24, #27, #28, #29, #30, #31, #32.
# Alasan pilih: 6 teratas tetap (lead + sekunder, peta 6 pin tetap valid);
# 10 reguler = berita terbesar + strip UTC tetap valid (#6 21:00, #7 00:09,
# #25 15:00, #26 17:30, #34 03:23 — semuanya dipertahankan).
# Tuple: (num, group, title, body, tag, time_utc_or_None, lon, lat, source)
# Tag: FACT (hijau), CLAIM (amber), DATA (biru), DISPUTED (merah).
# #16 tag TETAP FACT (tag = kepastian klaim UTAMA cegatan koalisi;
# angka 71 membawa atribusi sendiri "Houthis claim"). #19 TETAP CLAIM.
# #7: "6.9" adalah estimasi OTOMATIS yg direvisi ke 6.7 — JANGAN dipakai.
#   [DISPUTED] = beda kedalaman USGS 108 km vs IGP 129 km; korban INDECI.
# Tanda baca: "−" U+2212 di #6, "≥" di #33 — sama seperti v8.14.
STORIES = [
    # 1 — LEAD (Global, ICJ)
    (1, "GLOBAL", "ICJ Finds Myanmar Guilty",
     "9-6: first time the ICJ finds a state committed genocide "
     "(Rohingya); reparations to follow; Myanmar rejects it.",
     "FACT", None, 96.0, 21.0, "ICJ"),
    # 2–6 — SEKUNDER
    (2, "EUROPE", "Russia Hits Kryvyi Rih",
     "2 killed, ~60 injured; rescuers attacked.",
     "FACT", None, 33.4, 47.9, "AP"),
    (3, "LATIN AMERICA", "Chapo Isidro Arrested",
     "Mexico: 11 killed; 8 arrested; US $5m reward.",
     "FACT", None, -108.5, 25.6, "BBC"),
    (4, "EUROPE", "COP31 Near-Deal",
     "UN climate: fossil fuels cut from draft; deal close late Sat.",
     "FACT", None, 30.7, 36.9, "Majik"),
    (5, "MIDDLE EAST", "Iran Claims US Strike",
     "IRGC claims al-Riffa hit; Bahrain: no casualties; US drone "
     "downed; US denies.",
     "CLAIM", None, 50.5, 26.2, "Al Jazeera"),
    (6, "NORTH AMERICA", "S&P Plunges −3.7%",
     "S&P 500 -3.7%, Nasdaq -5.3%; Nvidia -14%.",
     "DATA", "21:00", -74.0, 40.7, "Majik"),
    # 7–34 — REGULER (10 cerita, grid 2 kolom x 5 baris)
    (7, "LATIN AMERICA", "M6.7 Quake in Junin",
     "M6.7; 108 km (IGP: 129 km); 8 injured, no deaths.",
     "DISPUTED", "00:09", -75.0, -11.0, "USGS"),
    (11, "GLOBAL", "Trump: '1945, 2026'",
     "Yalta photo recast with Trump, Xi, Putin; debate over diplomacy.",
     "FACT", None, 116.4, 39.9, "Truth Social"),
    (15, "MIDDLE EAST", "3 Killed in Gaza",
     "Food vehicle hit; 3 killed.",
     "FACT", None, 34.5, 31.5, "Al Jazeera"),
    (16, "MIDDLE EAST", "Riyadh Intercept",
     "Coalition intercepts missile; Houthis claim 71 strikes/24h.",
     "FACT", None, 42.8, 14.8, "Middle East Eye"),
    (19, "ASIA-PACIFIC", "Shenzhen Summit",
     "Trump backs Putin; Zelensky: murderer; nuclear risk.",
     "CLAIM", None, 114.0, 22.5, "BBC"),
    (20, "EUROPE", "Missiles in Poland",
     "2 missiles, 1 drone down; Tusk: deliberate provocation.",
     "FACT", None, 21.0, 52.2, "Al Jazeera"),
    (25, "SPORTS", "Chelsea 1-4 Leeds",
     "Okafor 2 goals, Calvert-Lewin pen; first win at the Bridge "
     "since 1999.",
     "FACT", "15:00", -0.1, 51.5, "InfoLiveScore"),
    (26, "SPORTS", "Newcastle 2-2 Arsenal",
     "Arsenal stay top; Eze, Barnes, Thiaw, Madueke.",
     "FACT", "17:30", -1.6, 54.98, "InfoLiveScore"),
    (33, "GLOBAL", "Tragedy in Nigeria",
     "Bayelsa boat capsizes; ≥24 dead, 24 survived.",
     "FACT", None, 6.3, 4.9, "Sky News"),
    (34, "SPORTS", "Harden 51 Points",
     "Cleveland beat Indiana 128-119. 26th 50-point game, passing Kobe.",
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

# Pin peta: HANYA 6 cerita teratas (lead + 5 sekunder) — sama seperti v8.14.
# #2 (0,-2) + #4 (0,+2): pusat 20,33px — halo 20px TIDAK bersentuhan;
# assert tabrakan memakai diameter halo (20px), bukan dot (16px).
PINS_V8_2 = [
    (1, 0, 0), (2, 0, -2), (3, 0, 0), (4, 0, 2), (5, 0, 0), (6, 0, 0),
]

# Kartu reguler yg membawa jam di meta: #25/#26/#34 (sama seperti v8.14).
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

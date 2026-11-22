# Data v7 — 34 cerita, 1 kartu = 1 cerita (polish atas v6, brief rev7).
# Tuple: (num, group, title, body, tag, time_utc_or_None, lon, lat, source_or_None)
# time: "HH:MM" Sabtu UTC atau None (jam tak diketahui -> JANGAN ditebak).
# source: outlet primer terverifikasi, atau None (tak ditemukan di file riset
#   -> kartu TANPA source tag, JANGAN mengarang). Tanpa tag: #1, #3, #9, #10,
#   #11, #13. #12 -> Reuters (rev4-brief: "will likely come into effect").
#   #4 (Majik, agregator) dan #8 (UKMTO) tanpa tag di meta: tak muat di
#   13px pada lebar meta (190/235px); keduanya dikredit di footer sumber.
#   Singkatan meta: Middle East Eye->MEE, InfoLiveScore->ILS, Al Jazeera->AJ,
#   TechCrunch->TC. Tag di meta tanpa kurung [ ] (geometri 13px).
# #7 Peru: "8 luka" TIDAK terkonfirmasi di file riset mana pun -> fallback
#   badan lama "tanpa korban" (rev6-brief: tanpa korban/kerusakan).
# #28: "~04:00" DIHAPUS (strip klaim "HANYA JAM TERVERIFIKASI").
# #6: klausa SEC dihapus (tag [DATA] dipertahankan hanya tanpa klaim SEC).
# #13: tag DATA -> KLAIM (studi belum peer-review). #19: RESMI -> KLAIM.
STORIES = [
    # 1 — LEAD (Timur Tengah)
    (1, "TIMUR TENGAH", "Iran Klaim Serang AS, Bahrain",
     "IRGC klaim hantam al-Riffa & Awali; Bahrain: kebakaran situs sipil, "
     "0 korban. Iran klaim jatuhkan drone AS dekat Qeshm; AS bantah F-16 kena.",
     "KLAIM", None, 50.5, 26.2, None),
    # 2–6 — SEKUNDER
    (2, "EROPA", "Rudal di Kryvyi Rih",
     "2 tewas, ~60 luka; penyelamat diserang.",
     "RESMI", None, 33.4, 47.9, "AP"),
    (3, "AMERIKA LATIN", "Chapo Isidro Ditangkap",
     "11 tewas susulan; 8 ditangkap; hadiah $5 jt.",
     "RESMI", None, -108.5, 25.6, None),
    (4, "EROPA", "COP31: Hampir Deal",
     "Fosil dicoret draf; larut Sabtu hampir deal.",
     "RESMI", None, 30.7, 36.9, None),
    (5, "GLOBAL", "ICJ: Myanmar Bersalah",
     "9-6; genosida pertama; ganti rugi menyusul; Myanmar menolak.",
     "RESMI", None, 96.0, 21.0, "ICJ"),
    (6, "AMERIKA UTARA", "Pasar Anjlok -3,7%",
     "S&P 500 -3,7%, Nasdaq -5,3%; Nvidia -14%.",
     "DATA", "21:00", -74.0, 40.7, "Equiti"),
    # 7–12 — REGULER
    (7, "AMERIKA LATIN", "Gempa M6,7 Junin",
     "M6,7 ~108 km; terasa di Lima; tanpa korban.",
     "BERSELISIH", "00:09", -75.0, -11.0, "USGS"),
    (8, "TIMUR TENGAH", "Tanker Terbakar",
     "~8 mil utara Khasab; ranjau vs proyektil, 0 korban.",
     "BERSELISIH", None, 56.2, 26.2, None),
    (9, "ASIA-PASIFIK", "Pemilu Ladakh",
     "Panchayat + kota pertama sejak 2019; Leh & Kargil.",
     "RESMI", None, 77.6, 34.2, None),
    (10, "EROPA", "Sparta II Diserang",
     "Kapal Rusia terbakar; 16 kru selamat; diduga Ukraina.",
     "KLAIM", None, 25.0, 59.8, None),
    (11, "GLOBAL", "Trump: '1945, 2026'",
     "Foto Yalta dipadu Trump, Xi, Putin; debat diplomasi.",
     "RESMI", None, 116.4, 39.9, None),
    (12, "ASIA-PASIFIK", "Deal UE-Indonesia",
     "Tarif dihapus 98,5%; target berlaku awal 2027.",
     "RESMI", None, 106.8, -6.2, "Reuters"),
]

STORIES += [
    (13, "GLOBAL", "Dengue Ditekan",
     "Wolbachia tekan dengue -69%; belum peer-review.",
     "KLAIM", None, -48.0, -15.0, None),
    (14, "GLOBAL", "Hipotesis Riemann",
     "Alpöge klaim bukti dgn Claude; 2 kelompok cek.",
     "KLAIM", None, -122.4, 37.8, "Guardian"),
    (15, "TIMUR TENGAH", "3 Tewas di Gaza",
     "Kendaraan pangan dihantam; 3 tewas.",
     "RESMI", None, 34.5, 31.5, "Al Jazeera"),
    (16, "TIMUR TENGAH", "Houthi vs Saudi",
     "Rudal Riyadh dicegat; Houthi klaim 71 serangan.",
     "RESMI", None, 42.8, 14.8, "Middle East Eye"),
    (17, "EROPA", "UK-UE Teken 3 Deal",
     "Pangan, emisi, mobilitas 100 ribu pemuda/thn.",
     "RESMI", None, 4.4, 50.8, "BBC"),
    (18, "EROPA", "Pajak Big Tech 3%",
     "Anggaran 2028-2034 lebih kecil; Prancis-Jerman beda.",
     "RESMI", None, 4.4, 50.8, "RFI"),
    (19, "ASIA-PASIFIK", "KTT Shenzhen",
     "Trump bela Putin; Zelensky: pembunuh; risiko nuklir.",
     "KLAIM", None, 114.0, 22.5, "BBC"),
    (20, "EROPA", "Rudal di Polandia",
     "2 rudal + 1 drone jatuh 20 Nov; Tusk: provokasi.",
     "RESMI", None, 21.0, 52.2, "Al Jazeera"),
    (21, "AMERIKA UTARA", "Ritel Kanada +7,5%",
     "+7,5% YoY, terkuat sejak 2022; Inggris +2,3%.",
     "DATA", None, -75.7, 45.4, "Equiti"),
    (22, "AMERIKA UTARA", "NCIC Diretas?",
     "Database kejahatan AS diselidiki; Trump: 'not good'.",
     "KLAIM", None, -77.0, 38.9, "TechCrunch"),
    (23, "AMERIKA UTARA", "Proxy Voting Ilegal",
     "5th Circuit 9-8: DPR AS langgar Kuorum; $1,7 triliun.",
     "RESMI", None, -77.0, 38.9, "Reuters"),
    (24, "EROPA", "Trailer 'Heal' Rilis",
     "Dok. kanker Catherine; BBC 29 Nov, CTV 7 Des.",
     "RESMI", None, -0.1, 51.5, "AP"),
]

STORIES += [
    (25, "OLAHRAGA", "Leeds 4-1 Chelsea",
     "Emegha 25', Okafor 2 gol; pertama menang di Bridge.",
     "RESMI", "15:00", -0.1, 51.5, "InfoLiveScore"),
    (26, "OLAHRAGA", "Newcastle 2-2 Arsenal",
     "Eze, Barnes, Thiaw, Madueke.",
     "RESMI", "17:30", -1.6, 54.98, "InfoLiveScore"),
    (27, "OLAHRAGA", "Malen 4 Gol, Roma",
     "Malen 39', 68', 77', 90'; Roma menang 5-1.",
     "RESMI", None, 10.3, 44.8, "InfoLiveScore"),
    (28, "EROPA", "Robot Perang Gagal",
     "Jenewa tanpa traktat; ~100 negara dukung 2028.",
     "RESMI", None, 6.1, 46.2, "CBC"),
    (29, "EROPA", "Denmark Usir Atase Rusia",
     "Diduga plot bunuh rapper Kyivstoner; Rusia bantah.",
     "KLAIM", None, 12.6, 55.7, "BBC"),
    (30, "AMERIKA UTARA", "Campak Mematikan",
     "Kematian pertama 2026; AS kehilangan status eliminasi.",
     "RESMI", None, -77.5, 37.5, "Guardian"),
    (31, "GLOBAL", "BepiColombo Tiba",
     "8 tahun, 10 miliar km; misi kedua orbit Merkurius.",
     "RESMI", None, None, None, "UPI"),
    (32, "AMERIKA LATIN", "Bolsonaro di ICU",
     "Obstruksi usus; stabil; dokter timbang operasi.",
     "RESMI", None, -47.9, -15.8, "Al Jazeera"),
    (33, "GLOBAL", "Tragedi di Nigeria",
     "Perahu terbalik Bayelsa; ≥24 tewas, 24 selamat.",
     "RESMI", None, 6.3, 4.9, "Sky News"),
    (34, "OLAHRAGA", "Harden 51 Poin",
     "Cleveland 128-119; 26th 50+ game, lewati Kobe.",
     "RESMI", "03:23", -81.7, 41.5, "AP"),
]

# Warna titik region (dipakai badge meta + pin peta). Border kartu NETRAL.
GROUP_COLOR = {
    "TIMUR TENGAH": (0, 128, 128),
    "EROPA": (29, 78, 137),
    "AMERIKA UTARA": (30, 107, 52),
    "AMERIKA LATIN": (168, 74, 20),
    "ASIA-PASIFIK": (107, 45, 143),
    "OLAHRAGA": (176, 142, 20),
    "GLOBAL": (107, 101, 90),
}
GROUP_ORDER = ["TIMUR TENGAH", "EROPA", "AMERIKA UTARA", "AMERIKA LATIN",
               "ASIA-PASIFIK", "OLAHRAGA", "GLOBAL"]

# Pin peta v7: HANYA 6 cerita teratas (lead + 5 sekunder).
# Nudge dalam px (leader line dari titik sejati). #2/#4 tetap di-nudge
# (Kryvyi Rih vs Antalya berdekatan).
PINS_V7 = [
    (1, 0, 0), (2, 10, -8), (3, 0, 0), (4, -14, 10), (5, 0, 0), (6, 0, 0),
]

# Singkatan sumber untuk meta 13px (footer menulis nama penuh).
SRC_SHORT = {
    "Middle East Eye": "MEE",
    "InfoLiveScore": "ILS",
    "Al Jazeera": "AJ",
    "TechCrunch": "TC",
}

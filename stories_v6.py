# Data v6 — 34 cerita, 1 kartu = 1 cerita.
# Tuple: (num, group, title, body, tag, time_utc_or_None, lon, lat)
# time: "HH:MM" Sabtu UTC atau None (jam tak diketahui -> JANGAN ditebak).
# lon/lat: None = tidak dipetakan (atau bukan lokasi darat).
# Judul kartu reguler <= ~19 karakter (20px bold, inner 227px);
# badan kartu reguler <= 2 baris @14px (<= ~58 karakter).
STORIES = [
    # 1 — LEAD (Timur Tengah)
    (1, "TIMUR TENGAH", "Iran Klaim Serang AS, Bahrain",
     "IRGC klaim hantam al-Riffa & Awali; Bahrain: kebakaran situs sipil, "
     "0 korban. Iran klaim jatuhkan drone AS dekat Qeshm; AS bantah F-16 kena.",
     "KLAIM", None, 50.5, 26.2),
    # 2–6 — SEKUNDER
    (2, "EROPA", "Rudal di Kryvyi Rih",
     "2 tewas, ~60 luka; penyelamat diserang.",
     "RESMI", None, 33.4, 47.9),
    (3, "AMERIKA LATIN", "Chapo Isidro Ditangkap",
     "11 tewas susulan; 8 ditangkap; hadiah $5 jt.",
     "RESMI", None, -108.5, 25.6),
    (4, "EROPA", "COP31: Hampir Deal",
     "Fosil dicoret draf; larut Sabtu hampir deal.",
     "RESMI", None, 30.7, 36.9),
    (5, "GLOBAL", "ICJ: Myanmar Bersalah",
     "9-6; pertama dalam sejarah; ganti rugi.",
     "RESMI", None, 96.0, 21.0),
    (6, "AMERIKA UTARA", "Pasar Anjlok -3,7%",
     "Nasdaq -5,3%; Nvidia -14% amid kabar SEC.",
     "DATA", "JUM 21:00", -74.0, 40.7),
    # 7–12 — REGULER
    (7, "AMERIKA LATIN", "Gempa M6,7 Junin",
     "M6,7, ~108 km dalam; terasa di Lima; tanpa korban.",
     "BERSELISIH", "00:00-05:00", -75.0, -11.0),
    (8, "TIMUR TENGAH", "Tanker Terbakar",
     "~8 mil utara Khasab; ranjau vs proyektil, 0 korban.",
     "BERSELISIH", None, 56.2, 26.2),
    (9, "ASIA-PASIFIK", "Pemilu Ladakh",
     "Panchayat + kota pertama sejak 2019; Leh & Kargil.",
     "RESMI", None, 77.6, 34.2),
    (10, "EROPA", "Sparta II Diserang",
     "Kapal Rusia terbakar; 16 kru selamat; Ukraina diduga.",
     "KLAIM", None, 25.0, 59.8),
    (11, "GLOBAL", "Trump: '1945, 2026'",
     "Foto Yalta dipadu Trump, Xi, Putin; debat diplomasi.",
     "RESMI", None, 116.4, 39.9),
    (12, "ASIA-PASIFIK", "Deal UE-Indonesia",
     "Tarif dihapus 98,5%; berlaku awal 2027; pasar 730 jt.",
     "RESMI", None, 106.8, -6.2),
]

STORIES += [
    (13, "GLOBAL", "Dengue Ditekan",
     "Dengue + chikungunya -69%; studi 4 thn, 5.700 anak.",
     "DATA", None, -48.0, -15.0),
    (14, "GLOBAL", "Klaim Riemann",
     "Alpoge klaim bukti dgn Claude; 2 kelompok verifikasi.",
     "KLAIM", None, -122.4, 37.8),
    (15, "TIMUR TENGAH", "3 Tewas di Gaza",
     "Kendaraan pangan dihantam; 3 tewas.",
     "RESMI", None, 34.5, 31.5),
    (16, "TIMUR TENGAH", "Houthi vs Saudi",
     "Rudal ke Riyadh dicegat; 71 serangan/24 jam.",
     "RESMI", None, 42.8, 14.8),
    (17, "EROPA", "UK-UE Teken 3 Deal",
     "Pangan, emisi, mobilitas 100 ribu pemuda/thn.",
     "RESMI", None, 4.4, 50.8),
    (18, "EROPA", "Pajak Big Tech 3%",
     "Anggaran 2028-2034 lebih kecil; Prancis-Jerman berselisih.",
     "RESMI", None, 4.4, 50.8),
    (19, "ASIA-PASIFIK", "KTT Shenzhen",
     "Trump bela Putin; Zelensky: pembunuh; bahas risiko nuklir.",
     "RESMI", None, 114.0, 22.5),
    (20, "EROPA", "Rudal di Polandia",
     "2 rudal + 1 drone jatuh 20 Nov; Tusk: provokasi sengaja.",
     "RESMI", None, 21.0, 52.2),
    (21, "AMERIKA UTARA", "Ritel Kanada +7,5%",
     "+7,5% YoY, terkuat sejak 2022; Inggris +2,3%.",
     "DATA", None, -75.7, 45.4),
    (22, "AMERIKA UTARA", "NCIC Diretas?",
     "Database kejahatan AS diselidiki; Trump: 'not good'.",
     "KLAIM", None, -77.0, 38.9),
    (23, "AMERIKA UTARA", "Proxy Voting Ilegal",
     "5th Circuit 9-8: DPR langgar Kuorum; paket $1,7 triliun.",
     "RESMI", None, -77.0, 38.9),
    (24, "EROPA", "Trailer 'Heal' Rilis",
     "Dokumenter kanker Catherine; BBC 29 Nov, CTV 7 Des.",
     "RESMI", None, -0.1, 51.5),
]

STORIES += [
    (25, "OLAHRAGA", "Leeds 4-1 Chelsea",
     "Emegha 25', Okafor 2 gol; pertama di Bridge sejak 1999.",
     "RESMI", "15:00", -0.1, 51.5),
    (26, "OLAHRAGA", "2-2 di Newcastle",
     "Eze, Barnes, Thiaw, Madueke; Arsenal tetap puncak.",
     "RESMI", "17:30", -1.6, 54.98),
    (27, "OLAHRAGA", "Malen 4 Gol",
     "Malen 39', 68', 77', 90'; Mora 71'; Roma menang 5-1.",
     "RESMI", None, 10.3, 44.8),
    (28, "EROPA", "Robot Perang Gagal",
     "Jenewa tanpa traktat; ~100 negara dukung aturan 2028.",
     "RESMI", "~04:00", 6.1, 46.2),
    (29, "EROPA", "Usir Diplomat Rusia",
     "Atase pertahanan diusir; diduga plot bunuh Kyivstoner.",
     "KLAIM", None, 12.6, 55.7),
    (30, "AMERIKA UTARA", "Campak Mematikan",
     "Kematian pertama 2026; AS kehilangan status eliminasi.",
     "RESMI", None, -77.5, 37.5),
    (31, "GLOBAL", "BepiColombo Tiba",
     "8 tahun, 10 miliar km; misi kedua orbit Merkurius.",
     "RESMI", None, None, None),
    (32, "AMERIKA LATIN", "Bolsonaro di ICU",
     "Obstruksi usus; stabil; dokter pertimbangkan operasi.",
     "RESMI", None, -47.9, -15.8),
    (33, "GLOBAL", "Tragedi di Nigeria",
     "Perahu pelayat terbalik di Bayelsa; 24 selamat.",
     "RESMI", None, 6.3, 4.9),
    (34, "OLAHRAGA", "Harden 51 Poin",
     "Cleveland 128-119 Indiana; 26th 50+ game, lewati Kobe.",
     "RESMI", "03:23", -81.7, 41.5),
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

# Pin peta: (num, dx, dy) nudge dalam px (leader line dari titik sejati).
# Hanya 21 pin: 1-13 + 15, 16, 17, 19, 22, 24, 32, 33. (#18 berbagi
# Brussels dgn #17 -> hanya #17; #22/#23 berbagi DC -> hanya #22; #31 luar
# angkasa, tak dipetakan.)
PINS_V6 = [
    (1, 0, 0), (2, 10, -8), (3, 0, 0), (4, -14, 10), (5, 0, 0),
    (6, 12, -6), (7, 0, 0), (8, 13, 12), (9, 0, 0), (10, 8, -10),
    (11, 0, 0), (12, 0, 0), (13, 0, 0), (15, 10, -8), (16, -11, 9),
    (17, -16, -10), (19, 0, 0), (22, -12, 8), (24, -14, 9),
    (32, -16, 12), (33, 0, 0),
]

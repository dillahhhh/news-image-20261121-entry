# Data v8.6 — 34 cerita, 1 kartu = 1 cerita (polish atas v8.5, brief rev8.6).
# Perubahan data vs v8.5 (tiga string, SEMUA terukur dgn font PIL asli):
# A1 judul #23 "Proxy Voting Ilegal" -> "Voting Proksi Ilegal" (219,9px <=
# 235px @20px bold). A2 badan #24 tambah "tayang" (2 baris 222/216px @16px;
# subjek "Dok. kanker Catherine;" DIPERTAHANKAN). A3 badan #14 "dgn" ->
# "dengan" (tetap 3 baris 215/159/77px @16px). A4 h1 "7 KATEGORI" ->
# "7 TOPICS" (927,8px <= 990px) hanya ubah build_image.py, bukan data.
# File baru ini ada agar build_image.py mengimpor stories_v8_6 (jejak versi bersih).
# Tuple: (num, group, title, body, tag, time_utc_or_None, lon, lat, source)
# SEMUA kartu punya source (34/34, dari log verifikasi OneTurn 21 Nov +
# Majik — BUKAN tebakan). Sumber v8/v8.1 dipertahankan.
# #7: "6,9" adalah estimasi OTOMATIS yg direvisi ke 6,7 — JANGAN dipakai.
#   [BERSELISIH] = beda kedalaman USGS 108 km vs IGP 129 km; korban Indeci.
# #16 tag TETAP [RESMI] (tag = kepastian klaim UTAMA cegatan koalisi;
#   angka 71 membawa atribusi sendiri "Houthi klaim"). #19/#13 TETAP [KLAIM].
# #20: jam pasti TAK ADA di riset -> "Jumat", bukan "20 Nov".
# #25: Chelsea tuan rumah; Emegha cetak gol UNTUK CHELSEA (jangan cantumkan
#   sbg pencetak gol Leeds).
# #10: subjek "diduga" = Finlandia (terverifikasi). #29: subjek = Denmark.
# PERUBAHAN v8.3 vs v8.2 (brief rev8.3, TERUKUR dgn font PIL asli):
# - #2: badan "2 tewas, ~60 luka; penyelamat diserang." (2 baris, maks
#   175,1px/182px); usia (anak 7, paramedis 20) DIBUANG — pluralitas
#   ronde v8.2 (Claude, Kimi, MiniMax) minta "~60 luka" kembali; gabungan
#   usia + hitungan = 4 baris, tak muat 3 baris.
# - #10: judul "Sparta II Kena drone" (1 baris, 233,1px/235px) + badan
#   "Kapal Rusia; 16 selamat; Finlandia duga Ukraina." (2 baris);
#   "Kapal Rusia" kembali, "Terbakar" (terbaca kecelakaan) -> "Kena drone".
# - #13: badan "Tekan dengue −69%; ..." (minus U+2212, seragam dgn #6).
# - #16: judul "Cegat Rudal Riyadh" (1 baris, 221,2px/235px); badan + tag
#   [RESMI] TETAP.
# - #27: badan "Malen 39', 68', 77', 90'; Roma 5-1 Parma." (2 baris;
#   baris ke-2 137,5px <= 220px); "Mora 71';" DIBUANG (gol Parma).
# - #34: badan "Cleveland 128-119 vs Indiana; laga 50+ poin ke-26,
#   lewati Kobe." (3 baris; "game" -> "laga 50+ poin").
# DEVIASI TERUKUR vs brief rev8.3 (dilaporkan ke parent):
# - A2 judul target "Sparta II Kena Drone" = 235,4px > anggaran 235px
#   (lebih 0,4px) -> dipakai "Sparta II Kena drone" (233,1px; huruf 'd'
#   kecil — "drone" kata benda umum, bukan nama diri; fakta drone utuh).
#   Alternatif "Sparta II Diserang" (204,8px) DITOLAK karena membuang
#   fakta drone dari kartu.
# - A3 judul target "Rudal Riyadh Dicegat" = 241,9px > 235px (juga
#   alternatif Kimi "Riyadh: Rudal Dicegat" 249,9px) -> dipakai
#   "Cegat Rudal Riyadh" (221,2px; kata kerja + objek + tempat —
#   tak ambigu: yg dicegat jelas "Rudal", "Riyadh" tempatnya).
# PERUBAHAN v8.4 vs v8.3 (brief rev8.4, TERUKUR dgn font PIL asli):
# - A1 DIBLOKIR: judul target #10 "Drone Serang Sparta II" = 258,8px
#   > anggaran 235px (lebih 23,8px) — klaim Nemotron "~206px" SALAH
#   (~53px). Judul #10 TETAP "Sparta II Kena drone" (233,1px). Alternatif
#   terukur (utk parent, BUKAN diterapkan): "Sparta Kena Drone" 213,5px
#   (buang "II" dari nama kapal), "Sparta II Kena UAV" 212,6px (jargon),
#   "Sparta II Diserang"/"Sparta II Dihantam" 204,8/213,3px (buang fakta
#   drone), "Sparta II Kena Drone" 235,4px (lebih 0,4px). Font TIDAK
#   dikecilkan (dilarang). Brief: bila tak muat, LAPORKAN — dilakukan.
# - A2 (footer src1, di build_image.py): "InfoLiveScore, theScore"
#   dipulihkan; dana "Middle East Eye" -> "MEE" (kode meta #16 sendiri).
STORIES = [
    # 1 — LEAD (Timur Tengah)
    (1, "TIMUR TENGAH", "Iran Klaim Serang AS, Bahrain",
     "IRGC klaim hantam al-Riffa & Awali; Bahrain: kebakaran situs sipil, "
     "0 korban. Iran klaim jatuhkan drone AS dekat Qeshm; AS bantah F-16 kena.",
     "KLAIM", None, 50.5, 26.2, "Al Jazeera"),
    # 2–6 — SEKUNDER
    (2, "EROPA", "Rusia Serang Kryvyi Rih",
     "2 tewas, ~60 luka; penyelamat diserang.",
     "RESMI", None, 33.4, 47.9, "AP"),
    (3, "AMERIKA LATIN", "Chapo Isidro Ditangkap",
     "11 tewas; 8 ditangkap; hadiah $5 jt.",
     "RESMI", None, -108.5, 25.6, "BBC"),
    (4, "EROPA", "COP31: Hampir Deal",
     "Fosil dicoret draf; larut Sabtu hampir deal.",
     "RESMI", None, 30.7, 36.9, "Majik"),
    (5, "GLOBAL", "ICJ: Myanmar Bersalah",
     "9-6; genosida Rohingya pertama; ganti rugi menyusul; Myanmar menolak.",
     "RESMI", None, 96.0, 21.0, "ICJ"),
    (6, "AMERIKA UTARA", "S&P Anjlok −3,7%",
     "S&P 500 -3,7%, Nasdaq -5,3%; Nvidia -14%.",
     "DATA", "21:00", -74.0, 40.7, "Majik"),
    # 7–12 — REGULER
    (7, "AMERIKA LATIN", "Gempa M6,7 Junin",
     "M6,7; 108 km (IGP: 129 km); 8 luka, tanpa tewas.",
     "BERSELISIH", "00:09", -75.0, -11.0, "USGS"),
    (8, "TIMUR TENGAH", "Tanker Terbakar",
     "~8 mil utara Khasab; ranjau vs proyektil, 0 korban.",
     "BERSELISIH", None, 56.2, 26.2, "UKMTO"),
    (9, "ASIA-PASIFIK", "Pemilu Ladakh",
     "Panchayat + kota pertama sejak 2019; Leh & Kargil.",
     "RESMI", None, 77.6, 34.2, "Economic Times"),
    (10, "EROPA", "Sparta II Kena Drone",
     "Kapal Rusia; 16 selamat; Finlandia duga Ukraina.",
     "KLAIM", None, 25.0, 59.8, "BBC"),
    (11, "GLOBAL", "Trump: '1945, 2026'",
     "Foto Yalta dipadu Trump, Xi, Putin; debat diplomasi.",
     "RESMI", None, 116.4, 39.9, "Truth Social"),
    (12, "ASIA-PASIFIK", "Deal UE-Indonesia",
     "98,5% pos tarif dihapus; target berlaku awal 2027.",
     "RESMI", None, 106.8, -6.2, "DW"),
]

STORIES += [
    (13, "GLOBAL", "Nyamuk Wolbachia",
     "Tekan dengue −69%; studi 4 thn, 5.700 anak; belum peer-review.",
     "KLAIM", None, -48.0, -15.0, "Straits Times"),
    (14, "GLOBAL", "Hipotesis Riemann",
     "Alpöge klaim bukti dengan Claude; 2 kelompok verifikasi.",
     "KLAIM", None, -122.4, 37.8, "Guardian"),
    (15, "TIMUR TENGAH", "3 Tewas di Gaza",
     "Kendaraan pangan dihantam; 3 tewas.",
     "RESMI", None, 34.5, 31.5, "Al Jazeera"),
    (16, "TIMUR TENGAH", "Cegat Rudal Riyadh",
     "Koalisi cegat rudal; Houthi klaim 71 serangan/24 jam.",
     "RESMI", None, 42.8, 14.8, "Middle East Eye"),
    (17, "EROPA", "UK-UE Teken 3 Deal",
     "Pangan, emisi, mobilitas 100 ribu pemuda/thn.",
     "RESMI", None, 4.4, 50.8, "BBC"),
    (18, "EROPA", "Pajak Big Tech 3%",
     "Anggaran 2028-2034 lebih kecil; usul Dewan UE.",
     "RESMI", None, 4.4, 50.8, "RFI"),
    (19, "ASIA-PASIFIK", "KTT Shenzhen",
     "Trump bela Putin; Zelensky: pembunuh; risiko nuklir.",
     "KLAIM", None, 114.0, 22.5, "BBC"),
    (20, "EROPA", "Rudal di Polandia",
     "2 rudal, 1 drone jatuh Jumat; Tusk: provokasi sengaja.",
     "RESMI", None, 21.0, 52.2, "Al Jazeera"),
    (21, "AMERIKA UTARA", "Ritel Kanada +7,5%",
     "+7,5% YoY, terkuat sejak 2022; Inggris +2,3%.",
     "DATA", None, -75.7, 45.4, "Majik"),
    (22, "AMERIKA UTARA", "Peretasan NCIC?",
     "Database kejahatan AS diselidiki; Trump: 'not good'.",
     "KLAIM", None, -77.0, 38.9, "TechCrunch"),
    (23, "AMERIKA UTARA", "Voting Proksi Ilegal",
     "5th Circuit 9-8: DPR AS langgar Kuorum; paket $1,7 triliun.",
     "RESMI", None, -77.0, 38.9, "Reuters"),
    (24, "EROPA", "Trailer 'Heal' Rilis",
     "Dok. kanker Catherine; BBC tayang 29 Nov, CTV 7 Des.",
     "RESMI", None, -0.1, 51.5, "AP"),
]

STORIES += [
    (25, "OLAHRAGA", "Chelsea 1-4 Leeds",
     "Okafor 2 gol, Calvert-Lewin pen; pertama menang di Bridge "
     "sejak 1999.",
     "RESMI", "15:00", -0.1, 51.5, "InfoLiveScore"),
    (26, "OLAHRAGA", "Newcastle 2-2 Arsenal",
     "Arsenal tetap puncak; Eze, Barnes, Thiaw, Madueke.",
     "RESMI", "17:30", -1.6, 54.98, "InfoLiveScore"),
    (27, "OLAHRAGA", "Malen 4 Gol, Roma",
     "Malen 39', 68', 77', 90'; Roma 5-1 Parma.",
     "RESMI", None, 10.3, 44.8, "InfoLiveScore"),
    (28, "EROPA", "Robot Perang Gagal",
     "Jenewa tanpa traktat; ~100 negara dukung aturan 2028.",
     "RESMI", None, 6.1, 46.2, "CBC"),
    (29, "EROPA", "Denmark Usir Atase Rusia",
     "Duga plot bunuh rapper Kyivstoner; Rusia bantah.",
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
     "Cleveland 128-119 vs Indiana; laga 50+ poin ke-26, lewati Kobe.",
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

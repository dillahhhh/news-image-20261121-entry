# Data v8 — 34 cerita, 1 kartu = 1 cerita (polish atas v7.1, brief rev8).
# Tuple: (num, group, title, body, tag, time_utc_or_None, lon, lat, source)
# SEMUA kartu punya source (34/34, dari log verifikasi OneTurn 21 Nov +
# Majik — BUKAN tebakan). Sumber baru v8: #1 AJ, #3 BBC, #4 MJK, #8 UKMTO,
# #9 ET, #11 TS, #13 ST; #6/#21 Equiti -> MJK (Majik penerbit angka);
# #12 Reuters -> DW.
# #7: "6,9" adalah estimasi OTOMATIS yg direvisi ke 6,7 — JANGAN dipakai.
#   [BERSELISIH] = beda kedalaman USGS 108 km vs IGP 129 km; korban Indeci.
# #16 tag TETAP [RESMI] (tag = kepastian klaim UTAMA cegatan koalisi;
#   angka 71 membawa atribusi sendiri "Houthi klaim"). #19/#13 TETAP [KLAIM].
# #20: jam pasti TAK ADA di riset -> "Jumat", bukan "20 Nov".
# #25: Chelsea tuan rumah; Emegha cetak gol UNTUK CHELSEA (jangan cantumkan
#   sbg pencetak gol Leeds). Fallback badan (bila 3 baris tak muat):
#   "Okafor 2 gol; pertama menang di Bridge sejak 1999."
# #10: subjek "diduga" = Finlandia (terverifikasi). #29: subjek = Denmark.
# DEVIASI v8 vs brief rev8 (TERUKUR dgn font PIL asli — semua dilaporkan
# ke parent; TIDAK ada yg disembunyikan):
# - Meta 5-segmen (dgn kode region) TIDAK MUAT di 12px bold pada 8 kartu:
#   sekunder #1-#6 (197-211px > budget 190) + #7 (257px) + #8 (269px >
#   budget 235). Kedelapan kartu memakai meta 4-segmen (tanpa kode region);
#   region tetap terkode lewat DOT WARNA 12px + legenda footer. Kartu lain
#   memakai 5-segmen; #25/#26/#34 memakai format jam (terukur 222px).
# - Badan 3-4 baris pd 16px/235px TIDAK MUAT di baris grid 76px. Yg muat
#   3 baris dipertahankan persis di baris tinggi 98px: #13 (3 baris, kata
#   "studi" dihapus — elipsis, "4 thn, 5.700 anak" + "belum peer-review"
#   tetap menyampaikan studi 4 thn atas 5.700 anak yg belum peer-review),
#   #14, #23, #25 (persis). Yg dipendekkan ke 2 baris (fakta inti utuh):
#   #10 (hapus "kru"; "duga"->":" — atribusi Finlandia melemah), #16
#   (hapus "ke" + "serangan"; "71/24 jam" = 71 [serangan]/24 jam), #20
#   ("+"->","), #26 (urutan klausa dibalik), #29 (hapus "rapper"),
#   #34 (hapus "vs"). #5 persis (4 baris, SEC_H 142).
# - Judul #22: "Peretasan Database NCIC?" (2 baris, 267px) -> "Database
#   NCIC?" (1 baris, 178px); akronim tidak lagi telanjang ("Database"
#   menjelaskannya) + badan membawa "diselidiki".
# - Pin #2/#4 pd posisi sejati berjarak 16,4px (dot 16px TIDAK bersentuhan,
#   celah 0,4px); assert tabrakan memakai diameter dot (16px), bukan 20px.
STORIES = [
    # 1 — LEAD (Timur Tengah)
    (1, "TIMUR TENGAH", "Iran Klaim Serang AS, Bahrain",
     "IRGC klaim hantam al-Riffa & Awali; Bahrain: kebakaran situs sipil, "
     "0 korban. Iran klaim jatuhkan drone AS dekat Qeshm; AS bantah F-16 kena.",
     "KLAIM", None, 50.5, 26.2, "Al Jazeera"),
    # 2–6 — SEKUNDER
    (2, "EROPA", "Rudal di Kryvyi Rih",
     "2 tewas, ~60 luka; penyelamat diserang.",
     "RESMI", None, 33.4, 47.9, "AP"),
    (3, "AMERIKA LATIN", "Chapo Isidro Ditangkap",
     "11 tewas susulan; 8 ditangkap; hadiah $5 jt.",
     "RESMI", None, -108.5, 25.6, "BBC"),
    (4, "EROPA", "COP31: Hampir Deal",
     "Fosil dicoret draf; larut Sabtu hampir deal.",
     "RESMI", None, 30.7, 36.9, "Majik"),
    (5, "GLOBAL", "ICJ: Myanmar Bersalah",
     "9-6; genosida Rohingya pertama; ganti rugi menyusul; Myanmar menolak.",
     "RESMI", None, 96.0, 21.0, "ICJ"),
    (6, "AMERIKA UTARA", "Pasar Anjlok -3,7%",
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
    (10, "EROPA", "Sparta II Diserang",
     "Kapal Rusia terbakar; 16 selamat; Finlandia: Ukraina.",
     "KLAIM", None, 25.0, 59.8, "BBC"),
    (11, "GLOBAL", "Trump: '1945, 2026'",
     "Foto Yalta dipadu Trump, Xi, Putin; debat diplomasi.",
     "RESMI", None, 116.4, 39.9, "Truth Social"),
    (12, "ASIA-PASIFIK", "Deal UE-Indonesia",
     "98,5% pos tarif dihapus; target berlaku awal 2027.",
     "RESMI", None, 106.8, -6.2, "DW"),
]

STORIES += [
    (13, "GLOBAL", "Dengue Ditekan",
     "Nyamuk Wolbachia tekan dengue -69%; 4 thn, 5.700 anak; belum peer-review.",
     "KLAIM", None, -48.0, -15.0, "Straits Times"),
    (14, "GLOBAL", "Hipotesis Riemann",
     "Alpöge klaim bukti dgn Claude; 2 kelompok verifikasi.",
     "KLAIM", None, -122.4, 37.8, "Guardian"),
    (15, "TIMUR TENGAH", "3 Tewas di Gaza",
     "Kendaraan pangan dihantam; 3 tewas.",
     "RESMI", None, 34.5, 31.5, "Al Jazeera"),
    (16, "TIMUR TENGAH", "Houthi vs Saudi",
     "Koalisi cegat rudal Riyadh; Houthi klaim 71/24 jam.",
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
    (22, "AMERIKA UTARA", "Database NCIC?",
     "Database kejahatan AS diselidiki; Trump: 'not good'.",
     "KLAIM", None, -77.0, 38.9, "TechCrunch"),
    (23, "AMERIKA UTARA", "Proxy Voting Ilegal",
     "5th Circuit 9-8: DPR AS langgar Kuorum; paket $1,7 triliun.",
     "RESMI", None, -77.0, 38.9, "Reuters"),
    (24, "EROPA", "Trailer 'Heal' Rilis",
     "Dok. kanker Catherine; BBC 29 Nov, CTV 7 Des.",
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
     "Malen 39', 68', 77', 90'; Mora 71'; Roma menang 5-1.",
     "RESMI", None, 10.3, 44.8, "InfoLiveScore"),
    (28, "EROPA", "Robot Perang Gagal",
     "Jenewa tanpa traktat; ~100 negara dukung aturan 2028.",
     "RESMI", None, 6.1, 46.2, "CBC"),
    (29, "EROPA", "Denmark Usir Atase Rusia",
     "Denmark duga plot bunuh Kyivstoner; Rusia bantah.",
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
     "Cleveland 128-119 Indiana; 26th 50+ game, lewati Kobe.",
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

# Kode region 3 huruf (segmen ke-5 meta; legenda footer menjelaskan).
REGION_CODE = {
    "TIMUR TENGAH": "TMT",
    "EROPA": "ERP",
    "AMERIKA UTARA": "AMU",
    "AMERIKA LATIN": "AML",
    "ASIA-PASIFIK": "ASP",
    "OLAHRAGA": "OLA",
    "GLOBAL": "GLO",
}

# Pin peta v8: HANYA 6 cerita teratas (lead + 5 sekunder), SEMUA nudge (0,0).
# Nudge pin 4 v7 (-14,+10) TERBUKTI mendorongnya ke Laut Mediterania.
# CATATAN UKUR: posisi sejati #2 (Kryvyi Rih) dan #4 (Antalya) berjarak
# 16,4px — dot 16px TIDAK bersentuhan (celah 0,4px), hanya halo putih yg
# bersentuhan; assert tabrakan memakai diameter dot (16px), bukan 20px.
PINS_V8 = [
    (1, 0, 0), (2, 0, 0), (3, 0, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0),
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

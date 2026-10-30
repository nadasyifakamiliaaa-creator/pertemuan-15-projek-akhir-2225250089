BATAS_LULUS = 60


def hitung_rata_rata(nilai):
    """Menghitung rata-rata nilai siswa."""
    if len(nilai) == 0:
        return 0

    return sum(nilai) / len(nilai)


def status_lulus(nilai, batas=BATAS_LULUS):
    """Menampilkan daftar nilai yang lulus."""
    return [x for x in nilai if x >= batas]


def ringkasan(nilai):
    """Membuat ringkasan nilai siswa."""
    return {
        "jumlah": len(nilai),
        "rata_rata": hitung_rata_rata(nilai),
        "minimum": min(nilai) if nilai else None,
        "maksimum": max(nilai) if nilai else None,
        "lulus": len(status_lulus(nilai)),
        "tidak_lulus": len(nilai) - len(status_lulus(nilai))
    }
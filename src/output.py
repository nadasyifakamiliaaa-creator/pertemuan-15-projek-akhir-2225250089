def tampilkan_hasil(data, nilai):
    print("\n===== HASIL ANALISIS NILAI =====")

    print("Jumlah siswa :", data["jumlah"])
    print("Rata-rata    :", round(data["rata_rata"], 2))
    print("Nilai minimum:", data["minimum"])
    print("Nilai maksimum:", data["maksimum"])

    print("\nJumlah siswa lulus:", data["lulus"])
    print("Jumlah tidak lulus:", data["tidak_lulus"])

    print("\n===== STATUS SISWA =====")

    for i, angka in enumerate(nilai, start=1):
        if angka >= 60:
            status = "LULUS"
        else:
            status = "TIDAK LULUS"

        print(f"Siswa {i}: {angka} - {status}")
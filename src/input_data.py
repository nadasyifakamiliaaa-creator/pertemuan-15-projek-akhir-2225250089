def masukkan_nilai():
    nilai = []

    print("=== INPUT NILAI SISWA ===")
    print("Masukkan nilai 5 siswa.")

    for i in range(5):
        while True:
            try:
                angka = float(input(f"Nilai siswa ke-{i+1}: "))

                if angka < 0 or angka > 100:
                    print("Nilai harus antara 0 sampai 100!")
                    continue

                nilai.append(angka)
                break

            except ValueError:
                print("Input harus berupa angka!")

    return nilai
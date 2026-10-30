from src.input_data import masukkan_nilai
from src.proses import ringkasan
from src.output import tampilkan_hasil


def main():
    print("================================")
    print("   APLIKASI ANALISIS NILAI")
    print("================================")

    nilai = masukkan_nilai()

    hasil = ringkasan(nilai)

    tampilkan_hasil(hasil, nilai)

    print("\nProgram selesai.")


if __name__ == "__main__":
    main()
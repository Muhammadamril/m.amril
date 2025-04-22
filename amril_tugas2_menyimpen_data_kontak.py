# Program kontak gaya list, tidak menampilkan kontak di awal
kontak = {
    "Ali": "081234567890",
    "Budi": "082345678901",
    "Citra": "083456789012"
}

def tampilkan_kontak():
    if not kontak:
        print("Daftar kontak kosong.")
    else:
        print("\nDaftar Kontak:")
        for i, (nama, nomor) in enumerate(kontak.items(), 1):
            print(f"{i}. {nama} - {nomor}")

print("=== Selamat Datang di Aplikasi Kontak ===")

while True:
    print("\nMenu:")
    print("1. Tambah Kontak")
    print("2. Hapus Kontak")
    print("3. Cari Kontak")
    print("4. Lihat Semua Kontak")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        nama = input("Nama kontak: ")
        nomor = input("Nomor telepon: ")
        kontak[nama] = nomor
        print("Kontak berhasil ditambahkan.")

    elif pilihan == '2':
        nama = input("Nama kontak yang akan dihapus: ")
        if nama in kontak:
            del kontak[nama]
            print("Kontak berhasil dihapus.")
        else:
            print("Kontak tidak ditemukan.")

    elif pilihan == '3':
        nama = input("Nama kontak yang dicari: ")
        if nama in kontak:
            print(f"{nama}: {kontak[nama]}")
        else:
            print("Kontak tidak ditemukan.")

    elif pilihan == '4':
        tampilkan_kontak()

    elif pilihan == '5':
        print("Terima kasih, program selesai.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")

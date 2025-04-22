# Kamus sederhana
kamus = {
    "pisang": "Buah dari tanaman herba besar genus Musa, umumnya berwarna kuning saat matang, berdaging lembut dan manis. Tanaman pisang memiliki batang semu dari lapisan daun",
    "apel": "buah berdaging dan berbiji yang umumnya bulat atau lonjong dengan kulit tipis licin berwarna merah, hijau, atau kuning (tergantung jenisnya), memiliki daging buah renyah berair dengan rasa manis atau asam, aroma khas, dan bagian tengah berisi biji yang disebut inti.",
    "jeruk": "buah dari genus Citrus, dikenal dengan aroma segarnya, rasa asam hingga manis, bentuk bulat atau oval dengan kulit berwarna hijau, kuning, oranye, atau merah, daging buah bersegmen kaya vitamin C, dan beberapa jenis memiliki biji."
}

kata = input("Masukkan kata yang ingin dicari artinya: ").lower()

if kata in kamus:
    print(f"Arti dari '{kata}' adalah: {kamus[kata]}")
else:
    print(f"Maaf, arti dari '{kata}' tidak ditemukan dalam kamus.")

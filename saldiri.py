hex_1 = input("Paket 1 (Hex) yapıştır: ").strip()
hex_2 = input("Paket 2 (Hex) yapıştır: ").strip()

c1 = bytes.fromhex(hex_1)
c2 = bytes.fromhex(hex_2)

# İki şifreli paketi XOR'layarak anahtarı ortadan kaldır (Geriye M1 ^ M2 kalır)
xored = bytes([a ^ b for a, b in zip(c1, c2)])

def crib_drag(tahmin_kelime: str):
    crib = tahmin_kelime.encode('utf-8')
    print(f"\n--- '{tahmin_kelime}' kelimesi taranıyor ---")
    for i in range(len(xored) - len(crib) + 1):
        parca = xored[i:i + len(crib)]
        sonuc = bytes([a ^ b for a, b in zip(parca, crib)])
        # Sadece okunabilir karakterler çıkarsa ekrana bas
        if all(32 <= b <= 126 for b in sonuc):
            print(f"Pozisyon {i:02d}: {sonuc.decode('utf-8')}")

while True:
    tahmin = input("\nDenemek istediğin kelime (Çıkmak için 'q'): ")
    if tahmin.lower() == 'q':
        break
    crib_drag(tahmin)

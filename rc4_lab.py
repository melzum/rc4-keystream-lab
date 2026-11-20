def rc4(key: bytes, data: bytes) -> bytes:
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    out = bytearray()
    for byte in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(byte ^ S[(S[i] + S[j]) % 256])
    return bytes(out)

gizli_anahtar = b"CokGizliSistemAnahtari_999"
mesaj_1 = b"Sistem raporu: Sunucu yedeklemeleri basariyla tamamlandi."
mesaj_2 = b"Gizli gorev: Yarin gece operasyon basliyor. CTF{RC4_K3ystr3am_R3us3}"

print(f"Yakalanan Paket 1: {rc4(gizli_anahtar, mesaj_1).hex()}")
print(f"Yakalanan Paket 2: {rc4(gizli_anahtar, mesaj_2).hex()}")

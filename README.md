# RC4 Keystream Reuse Lab

[TR] Aynı anahtarın iki kez kullanıldığı RC4 akış şifrelemesinde, iki şifreli
metni XOR'layarak anahtarı tamamen eleyen ve `crib dragging` ile düz metni
kurtaran küçük bir laboratuvar.

[EN] A small lab demonstrating RC4 keystream reuse: XOR two ciphertexts
encrypted with the same key to cancel the keystream, then recover plaintext
with crib dragging.

> Yalnızca eğitim amaçlıdır. Kendi veriniz veya izinli test ortamları dışında
> kullanmayın.

## Neden çalışıyor?

RC4 bir akış şifresidir:

```
C1 = M1 XOR KS
C2 = M2 XOR KS
C1 XOR C2 = M1 XOR M2
```

Anahtar (dolayısıyla `KS`) iki mesajda aynıysa XOR işlemi anahtarı yok eder ve
geriye yalnızca iki düz metnin XOR'u kalır. Bu durumda:

- Bilinen bir kelime (`crib`) denenerek düz metin parçaları ortaya çıkarılır.
- Aynı anda gönderilen iki mesajda oturum çerezi, token veya sabit başlık gibi
  bilinen alanlar varsa bunlar doğrudan okunabilir.

## Dosyalar

| Dosya | Açıklama |
|---|---|
| `rc4_lab.py` | RC4'ü saf Python ile uygular, aynı anahtarla iki örnek mesajı şifreler ve hex çıktısı verir |
| `saldiri.py` | İki şifreli paketi alır, XOR'lar ve girilen `crib` kelimesini tüm konumlarda dener |

## Kullanım

```bash
python3 rc4_lab.py
# Yakalanan Paket 1: 1f3a...
# Yakalanan Paket 2: 2b7c...

python3 saldiri.py
# Paket 1 (Hex): <1. paket>
# Paket 2 (Hex): <2. paket>
# Denemek istediğin kelime: Sistem
```

Script, yalnızca yazdırılabilir ASCII sonuç veren konumları listeler. Bilinen
bir başlık veya kelimeyle başlayıp çıkan parçalardan yeni crib'ler türetebilirsiniz.

## Örnek çıktı

`rc4_lab.py` içindeki iki mesaj aynı anahtarla şifrelenir. `saldiri.py` ile
`s:`, `Sistem`, `CTF` gibi tahminler girildiğinde karşılık gelen düz metin
parçaları görünür.

## Öğrenilenler

- Akış şifrelerinde **nonce/IV olmadan anahtar yeniden kullanımı** şifrelemeyi
  tamamen kırar.
- XOR'lanmış iki metinde `crib dragging`, istatistiksel analizden daha hızlı
  sonuç verir.
- Çözüm: her mesaj için benzersiz nonce, tercihen AEAD (ör. AES-GCM,
  ChaCha20-Poly1305); RC4 artık kullanılmamalıdır (RFC 7465).

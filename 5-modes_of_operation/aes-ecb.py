from Crypto.Cipher import AES

key = "cokgizlisifre123"
plain_text = "Merhabalar. Ben gizlenmek uzere AES ile siflenecek onemli bir metinim."
PADDING = '{'
pad = lambda s: s + (16 - len(s) % 16) * PADDING

aes = AES.new(key, AES.MODE_ECB)
cipher_text = aes.encrypt(pad(plain_text))
print repr(cipher_text)
plain_text = (aes.decrypt(cipher_text))
print plain_text.rstrip(PADDING)
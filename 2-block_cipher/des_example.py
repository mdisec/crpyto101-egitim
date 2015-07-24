from Crypto.Cipher import DES

key = "g1zl1KEY"
plain_text = "Mehmet-Ince-Blog"

des = DES.new(key, DES.MODE_ECB)
cipher_text = des.encrypt(plain_text)

print "Original CipherText   = {0}".format(repr(cipher_text))
# Cipher text is = '\x9b\xca\x92\xe0\x82\xb0\xf9\xb5\xfa5\x0e\xe0\xbb\x84@`'
# Change one byte= '\x9b\xcb\x92\xe0\x82\xb0\xf9\xb5\xfa5\x0e\xe0\xbb\x84@`'
print "Change only one thing = {0}".format(repr('\x9b\xcb\x92\xe0\x82\xb0\xf9\xb5\xfa5\x0e\xe0\xbb\x84@`'))

print "Original CipherText decryption  = {0}".format(des.decrypt(cipher_text))
manipulated_cipher = '\x9b\xcb\x92\xe0\x82\xb0\xf9\xb5\xfa5\x0e\xe0\xbb\x84@`'
print "One thing changed CipherText    = {0}".format(des.decrypt(manipulated_cipher))
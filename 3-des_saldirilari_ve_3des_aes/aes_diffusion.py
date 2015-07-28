from Crypto.Cipher import AES

key = "g1zl1KEYa1b2c3d6"
plain_text = "Mehmet-Ince-Blog"

aes = AES.new(key, AES.MODE_ECB)
cipher_text = aes.encrypt(plain_text)
print "Original CipherText   = {0}".format(repr(cipher_text))

# Original CipherText   = 'U\xe6\xbf\xbc\x14\xcf\x1a\xfc\x06~\xc1\xb1\xd6\x92{\xd3'
# Change one byte       = 'U\xe6\xbe\xbc\x14\xcf\x1a\xfc\x06~\xc1\xb1\xd6\x92{\xd3'

print "Change only one thing = {0}".format(repr('U\xe6\xbe\xbc\x14\xcf\x1a\xfc\x06~\xc1\xb1\xd6\x92{\xd3'))

print "Original CipherText decryption  = {0}".format(aes.decrypt(cipher_text))
manipulated_ciphertext = 'U\xe6\xbe\xbc\x14\xcf\x1a\xfc\x06~\xc1\xb1\xd6\x92{\xd3'
print "One thing changed CipherText    = {0}".format(aes.decrypt(manipulated_ciphertext))

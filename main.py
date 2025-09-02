from cryptography import caeser, transposition

text = "Moč je uložena v koulích."

key = 14
c = caeser.CaeserCipher(key)
encrypted = c.encrypt(text)
print(f"Encrypting '{text}' with key {key}: {encrypted}")
decrypted = c.decrypt(encrypted)
print(f"Decrypting back: {decrypted}")

transposition_key = 'hdtoKcVPSyqajYmbXeJkWGFUivQzIA guBDfsLCpxNTlrOwHZERMn'
t = transposition.TranspositionCipher(transposition_key)
encrypted = t.encrypt(text)
print(f"Encrypting '{text}' with key {transposition_key}: {encrypted}")
decrypted = t.decrypt(encrypted)
print(f"Decrypting back: {decrypted}")
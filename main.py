from cryptography import caeser, transposition

text = "Lukas Trkan Security and Vulnerability in Networks"
#phone = 10723
key = 23
transposition_key = '21534'
c = caeser.CaeserCipher(key)
encrypted = c.encrypt(text)
print(f"Encrypting '{text}' with key {key}: {encrypted}")
decrypted = c.decrypt(encrypted)
print(f"Decrypting back: {decrypted}")

t = transposition.TranspositionCipher(transposition_key)
encrypted = t.encrypt(text)
print(f"Encrypting '{text}' with key {transposition_key}: {encrypted}")
decrypted = t.decrypt(encrypted)
print(f"Decrypting back: {decrypted}")
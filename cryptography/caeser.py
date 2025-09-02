class CaeserCipher:
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        return self.process(text, self.key)

    def decrypt(self, ciphertext):
        return self.process(ciphertext, -self.key)

    def process(self, text, key):
        result = ""
        for c in text:
            result += self.shift_char(c, key)
        return result

    def shift_char(self, c, key):
        chars = self.upper if c.isupper() else self.lower

        # do not encrypt non-alphabetic characters
        if c not in chars:
            return c

        index = chars.index(c)
        new_index = (index + key) % len(chars)

        return chars[new_index]

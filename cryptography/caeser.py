class CaeserCipher:
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
        char_code = ord(c)

        if char_code < 32 or char_code > 126:
            return c

        # shift to 0-94 range so we can use modulo
        new_code = char_code - 32
        # apply the shift
        new_code += key
        #ensure correct range
        new_code = new_code % 95
        # shift back to ascii range
        new_code += 32
        return chr(new_code)
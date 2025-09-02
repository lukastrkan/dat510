
class TranspositionCipher:
    alphabet = 'qunDMCQASixpyjmFbsYTNBafcrVIGtHeg lJowLWhkdEPUOXvZRzK'

    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        result = ""
        for c in text:
            if c not in self.alphabet:
                result += c
                continue
            index = self.alphabet.index(c)
            result += self.key[index]
        return result

    def decrypt(self, text):
        result = ""
        for c in text:
            if c not in self.key:
                result += c
                continue
            index = self.key.index(c)
            result += self.alphabet[index]
        return result

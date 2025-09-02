
class TranspositionCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        result = ""
        matrix = self.create_matrix_encrypt(text)
        shuffled = self.shuffle_matrix(matrix)

        for i in range(len(self.key)):
            for line in shuffled:
                result += line[int(i)]

        return result

    def decrypt(self, text):
        result = ""
        matrix = self.create_matrix_decrypt(text)
        unshuffled = self.unshuffle_matrix(matrix)

        for line in unshuffled:
            result += "".join(line)

        return result

    def create_matrix_encrypt(self, text):
        rows = len(text) // len(self.key)
        if len(text) % len(self.key) != 0:
            rows += 1

        matrix = [[" "]*len(self.key) for _ in range(rows)]


        col = 0
        row = 0
        for char in text:
            matrix[row][col] = char
            col += 1
            if col == len(self.key):
                col = 0
                row += 1

        return matrix

    def create_matrix_decrypt(self, text):
        rows = len(text) // len(self.key)
        matrix = [[" "]*len(self.key) for _ in range(rows)]
        current_row = 0
        current_col = 0
        for char in text:
            matrix[current_row][current_col] = char
            current_row += 1

            if current_row == rows:
                current_row = 0
                current_col += 1

        return matrix


    def shuffle_matrix(self, matrix):
        result = []
        for line in matrix:
            shuffled = []*len(self.key)
            for i in self.key:
                shuffled.append(line[int(i)-1])
            result.append(shuffled)
        return result

    def unshuffle_matrix(self, matrix):
        result = []
        for line in matrix:
            #create empty list of correct size
            original = [" "] * len(self.key)
            index = 0
            for char in self.key:
                original[int(char)-1] = line[index]
                index += 1
            result.append(original)
        return result

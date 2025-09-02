import random


def main():
    alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    random.Random().shuffle(alphabet)

    print("".join(alphabet))




if __name__ == "__main__":
    main()
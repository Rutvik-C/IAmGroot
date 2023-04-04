from classes.groot import Groot

WORD_LEN = 3
grootSequence = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,/'!?;:()"
assert len(grootSequence) <= 4 ** WORD_LEN

groot = Groot(grootSequence, WORD_LEN)


while True:
    s = input(">> ")
    if s == "":
        break

    enc = groot.encode(s)
    print(f"""Encoded='{enc}'""")

    dec = groot.decode(enc)
    print(f"""Decoded='{dec}'""")

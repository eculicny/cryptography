from message import Message


def encrypt_caesar(msg: Message, shift: int) -> Message:
    content = msg.content.lower()
    encrypted_content = ""
    n = msg.alphabet_len()
    for c in content:
        chr_i = msg.get_ind(c)
        if chr_i is not None:
            encrypted_content += msg.get_chr((chr_i + shift) % n)
        else:
            encrypted_content += c

    return Message(encrypted_content, msg.alphabet_chr, msg.alphabet_num)


def decrypt_caesar(msg: Message, shift: int) -> Message:
    content = msg.content.lower()
    decrypted_content = ""
    n = msg.alphabet_len()
    for c in content:
        chr_i = msg.get_ind(c)
        if chr_i is not None:
            decrypted_content += msg.get_chr((chr_i - shift) % n)
        else:
            decrypted_content += c

    return Message(decrypted_content, msg.alphabet_chr, msg.alphabet_num)


def encrypt_vigenere(msg: Message, key: str) -> Message:
    content = msg.content.lower()
    k = len(key)
    encrypted_content = ""
    n = msg.alphabet_len()
    for i, c in enumerate(content):
        chr_i = msg.get_ind(c)
        j = i % k
        shift = msg.get_ind(key[j])  # get shift value from key
        if chr_i is not None:
            encrypted_content += msg.get_chr((chr_i + shift) % n)
        else:
            encrypted_content += c

    return Message(encrypted_content, msg.alphabet_chr, msg.alphabet_num)


def decrypt_vigenere(msg: Message, key: str) -> Message:
    content = msg.content.lower()
    k = len(key)
    decrypted_content = ""
    n = msg.alphabet_len()
    for i, c in enumerate(content):
        chr_i = msg.get_ind(c)
        j = i % k
        shift = msg.get_ind(key[j])  # get shift value from key
        if chr_i is not None:
            decrypted_content += msg.get_chr((chr_i - shift) % n)
        else:
            decrypted_content += c

    return Message(decrypted_content, msg.alphabet_chr, msg.alphabet_num)


alphabet_en_chr = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
}
alphabet_en_num = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
    8: "i",
    9: "j",
    10: "k",
    11: "l",
    12: "m",
    13: "n",
    14: "o",
    15: "p",
    16: "q",
    17: "r",
    18: "s",
    19: "t",
    20: "u",
    21: "v",
    22: "w",
    23: "x",
    24: "y",
    25: "z",
}
s = "Test String"
key = "asdf"
sh = 6
m = Message(s, alphabet_en_chr, alphabet_en_num)
print(m.content)
print(encrypt_caesar(m, sh).content)
print(decrypt_caesar(encrypt_caesar(m, sh), sh).content)
print(encrypt_vigenere(m, key).content)
print(decrypt_vigenere(encrypt_vigenere(m, key), key).content)

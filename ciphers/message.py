from typing import Dict


class Message:
    # alphabet_chr: Dict[str, int]
    # alphabet_num: Dict[int, str]

    def __init__(
        self, content: str, alph_chr: Dict[str, int], alph_num: Dict[int, str]
    ):
        if len(alph_chr) != len(alph_num):
            raise ValueError("Alphabet dicts don't match in length")
        self.alphabet_chr = alph_chr
        self.alphabet_num = alph_num
        self.content = content

    def alphabet_len(self) -> int:
        return len(self.alphabet_chr)

    def get_ind(self, char: str) -> int:
        return self.alphabet_chr.get(char)

    def get_chr(self, ind: int) -> str:
        return self.alphabet_num.get(ind)

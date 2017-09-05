"""
About String

Ascii - 1 byte 0-255, 0x00-0xFF, A(65)
Unicode - 2 bytes 가(0xAC00)
EUC-KR - 2 bytes
UTF-8 - 2 bytes+ Korean 3 bytes
UTF-16 - 2 bytes+ Korean 4 bytes
"""


class String:

    @classmethod
    def reverse(cls, word: str):
        if (word is None) or (word == ''):
            return None
        start = 0
        end = len(word) - 1
        char_list = list(word)
        while start < end:
            temp = char_list[start]
            char_list[start] = char_list[end]
            char_list[end] = temp
            start += 1
            end -= 1
        return ''.join(char_list)

    @classmethod
    def check_anagrams(cls, str1: str, str2: str):
        if str1 == '' or str1 is None or str2 == '' or str2 is None:
            return False
        if len(str1) != len(str2):
            return False
        str1 = ''.join(sorted(str1))
        str2 = ''.join(sorted(str2))
        return str1 == str2

    @classmethod
    def making_anagrams(cls, str1: str, str2: str):
        delete_count = 0
        letter_counts = [0] * (ord('z') - ord('a') + 1)

        for char in str1:
            letter_counts[ord(char) - ord('a')] += 1

        for char in str2:
            letter_counts[ord(char) - ord('a')] -= 1

        for number in letter_counts:
            delete_count += abs(number)

        return delete_count

    @classmethod
    def advanced_anagrams(cls, input: str):
        if not (len(input) % 2) == 0:
            return -1
        str1 = input[0:int(len(input) / 2)]
        str2 = input[int(len(input) / 2):]
        letter_counts = [0] * (ord('z') - ord('a') + 1)
        count = 0

        for i in range(len(str1)):
            letter_counts[ord(str1[i]) - ord('a')] += 1
            letter_counts[ord(str2[i]) - ord('a')] -= 1

        for number in letter_counts:
            count += abs(number)

        return count / 2

    @staticmethod
    def pangrams(sentence: str):
        sentence = sentence.lower().replace(' ', '')
        letter_counts = [0] * (ord('z') - ord('a') + 1)

        for letter in sentence:
            letter_counts[ord(letter) - ord('a')] += 1

        for count in letter_counts:
            if count == 0:
                return False
        return True

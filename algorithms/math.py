

class Math(object):

    @staticmethod
    def lonely_integer(numbers: list):
        value = 0
        for number in numbers:
            value = value ^ number
        return value

    @staticmethod
    def bin(value: int):
        buffer = [''] * 16
        char_index = len(buffer)
        while value > 0:
            char_index -= 1
            buffer[char_index] = '01'[value % 2]
            value = int(value / 2)
        return ''.join(buffer)

    @staticmethod
    def oct(value: int):
        buffer = [''] * 16
        char_index = len(buffer)
        while value > 0:
            char_index -= 1
            buffer[char_index] = '01234567'[value % 8]
            value = int(value / 8)
        return ''.join(buffer)

    @staticmethod
    def prime(value: int):
        if value == 0 or value == 1:
            return False
        if value == 2 or value == 3:
            return True
        if value % 2 == 0 or value % 3 == 0:
            return False
        j = 5
        while (j ** 2) <= value:
            if value % j == 0 or value % (j + 2) == 0:
                return False
            j += 6
        return True



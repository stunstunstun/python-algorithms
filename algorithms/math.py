

class Math(object):

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



"""
Basic algorithms
"""


class Basic:

    @classmethod
    def factorial(cls, number):
        """
        :return: recursive pattern if n = 5, 5 * 4 * 3 * 2 * 1 = 120 
        """
        if number == 1:
            return 1
        return number * cls.factorial(number - 1)

    @classmethod
    def fibonacci(cls, index):
        """
        :return: 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
        """
        if index == 0 or index == 1:
            return index
        return cls.fibonacci(index - 2) + cls.fibonacci(index - 1)

    @classmethod
    def time_conversion(cls, time: str):
        hours = int(time[:2])
        mins = int(time[3:5])
        seconds = int(time[6:8])
        if 'PM' in time and hours == 12:
            pass
        elif 'PM' in time:
            hours += 12
        elif hours >= 12:
            hours -= 12
        return '{:02}:{:02}:{:02}'.format(hours, mins, seconds)







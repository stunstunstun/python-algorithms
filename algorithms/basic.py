"""
Basic algorithms
"""
from collections import Counter


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
    def time_conversion(cls, formatted_time: str):
        hours = int(formatted_time[:2])
        mins = int(formatted_time[3:5])
        seconds = int(formatted_time[6:8])
        if 'PM' in formatted_time and hours == 12:
            pass
        elif 'PM' in formatted_time:
            hours += 12
        elif hours >= 12:
            hours -= 12
        return '{:02}:{:02}:{:02}'.format(hours, mins, seconds)

    @staticmethod
    def multiple_sum(num1, num2, end):
        total = 0
        for i in range(1, end):
            if i % num1 == 0 or i % num2 == 0:
                total += i
        return total

    @staticmethod
    def ransom_note(magazine: str, ransom: str):
        magazine_words = magazine.split(' ')
        ransom_words = ransom.split(' ')
        magazine_word_counts = Counter(magazine_words)
        ransom_word_counts = Counter(ransom_words)
        for word in ransom_words:
            if magazine_word_counts[word] < ransom_word_counts[word]:
                return False
        return True

    @staticmethod
    def compare_the_triplets(alice_points, bob_points):
        alice_score = 0
        bob_score = 0
        for i in range(len(alice_points)):
            if alice_points[i] > bob_points[i]:
                alice_score += 1
            elif alice_points[i] == bob_points[i]:
                pass
            else:
                bob_score += 1
        return ' '.join(map(lambda x: str(x), [alice_score, bob_score]))



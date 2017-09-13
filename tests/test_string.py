import unittest
import binascii
from algorithms.string import String


class TestString(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(String.reverse('abcde'), 'edcba')
        self.assertEqual(String.reverse(None), None)
        self.assertEqual(String.reverse(''), None)

    def test_binary(self):
        self.assertEqual(int('1010', 2), 10)
        self.assertEqual(hex(255), '0xff')

    def test_ascii(self):
        for i in range(0, 256, 1):
            print('{} {:03} {} {}'.format(chr(i), i, hex(i).upper(), bin(i)))
        self.assertEqual(chr(65), 'A')
        self.assertEqual(chr(44032), '가')

    def test_unicode(self):
        for i in range(ord(u'A'), ord(u'Z'), 1):
            print('{} {:03} {} {}'.format(chr(i), i, hex(i).upper(), bin(i)))
        for i in range(ord(u'가'), ord(u'겮'), 1):
            print('{} {:03} {} {}'.format(chr(i), i, hex(i).upper(), bin(i)))
        self.assertEqual(hex(ord(u'가')), '0xac00')

        b = u'A'.encode(encoding='utf-8')
        print('{} {} {}'.format('A', 'utf-8', binascii.hexlify(b)))
        self.assertEqual(len(b), 1)
        b = u'A'.encode(encoding='euc-kr')
        print('{} {} {}'.format('A', 'euc-kr', binascii.hexlify(b)))
        self.assertEqual(len(b), 1)
        b = u'A'.encode(encoding='utf-16')
        print('{} {} {}'.format('A', 'utf-16', binascii.hexlify(b)))
        self.assertEqual(len(b), 4)

        b = u'가'.encode(encoding='utf-8')
        print('{} {} {}'.format('가', 'utf-8', binascii.hexlify(b)))
        self.assertEqual(len(b), 3)
        b = u'가'.encode(encoding='euc-kr')
        print('{} {} {}'.format('가', 'euc-kr', binascii.hexlify(b)))
        self.assertEqual(len(b), 2)
        b = u'가'.encode(encoding='utf-16')
        print('{} {} {}'.format('가', 'utf-16', binascii.hexlify(b)))
        self.assertEqual(len(b), 4)
        b = u'가'.encode()
        self.assertEqual(len(b), 3)

    def test_check_anagrams(self):
        self.assertEqual(String.check_anagrams('abc', 'cab'), True)
        self.assertEqual(String.check_anagrams('bat', 'tab'), True)
        self.assertEqual(String.check_anagrams('abc', 'eft'), False)
        self.assertEqual(String.check_anagrams('ba', 'tab'), False)
        self.assertEqual(String.check_anagrams('abc', 'cb'), False)
        self.assertEqual(String.check_anagrams('', ''), False)
        self.assertEqual(String.check_anagrams(None, None), False)

    def test_making_anagrams(self):
        self.assertEqual(String.making_anagrams('cde', 'abc'), 4)
        self.assertEqual(String.making_anagrams('fcrxzw', 'jxjw'), 6)
        self.assertEqual(String.making_anagrams('fcrxzwscanmligyxyvym', 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'), 30)

    def test_advanced_anagrams(self):
        self.assertEqual(String.advanced_anagrams('aaabbb'), 3)
        self.assertEqual(String.advanced_anagrams('ab'), 1)
        self.assertEqual(String.advanced_anagrams('abc'), -1)
        self.assertEqual(String.advanced_anagrams('mnop'), 2)
        self.assertEqual(String.advanced_anagrams('xyyx'), 0)
        self.assertEqual(String.advanced_anagrams('xaxbbbxx'), 1)
        self.assertEqual(String.advanced_anagrams('xaxbbbxa'), 1)
        self.assertEqual(String.advanced_anagrams('abxxabbx'), 1)

        self.assertEqual(String.advanced_anagrams('hhpddlnnsjfoyxpciioigvjqzfbpllssuj'), 10)
        self.assertEqual(String.advanced_anagrams('xulkowreuowzxgnhmiqekxhzistdocbnyozmnqthhpievvlj'), 13)
        self.assertEqual(String.advanced_anagrams('dnqaurlplofnrtmh'), 5)
        self.assertEqual(String.advanced_anagrams('aujteqimwfkjoqodgqaxbrkrwykpmuimqtgulojjwtukjiqrasqejbvfbixnchzsahpnyayutsgecwvcqngzoehrmeeqlgknnb'), 26)
        self.assertEqual(String.advanced_anagrams('lbafwuoawkxydlfcbjjtxpzpchzrvbtievqbpedlqbktorypcjkzzkodrpvosqzxmpad'), 15)
        self.assertEqual(String.advanced_anagrams('drngbjuuhmwqwxrinxccsqxkpwygwcdbtriwaesjsobrntzaqbe'), -1)
        self.assertEqual(String.advanced_anagrams('ubulzt'), 3)
        self.assertEqual(String.advanced_anagrams('vxxzsqjqsnibgydzlyynqcrayvwjurfsqfrivayopgrxewwruvemzy'), 13)
        self.assertEqual(String.advanced_anagrams('xtnipeqhxvafqaggqoanvwkmthtfirwhmjrbphlmeluvoa'), 13)
        self.assertEqual(String.advanced_anagrams('gqdvlchavotcykafyjzbbgmnlajiqlnwctrnvznspiwquxxsiwuldizqkkaawpyyisnftdzklwagv'), -1)

    def test_pangrams(self):
        self.assertEqual(String.pangrams('We promptly judged antique ivory buckles for the next prize'), True)
        self.assertEqual(String.pangrams('We promptly judged antique ivory buckles for the prize'), False)

    def test_matched_pattern(self):
        self.assertEqual(String.is_iterative_pattern('a'), True)
        self.assertEqual(String.is_iterative_pattern('aaa'), True)
        self.assertEqual(String.is_iterative_pattern('abcabc'), True)
        self.assertEqual(String.is_iterative_pattern('ababab'), True)

        self.assertEqual(String.is_iterative_pattern(''), False)
        self.assertEqual(String.is_iterative_pattern('ab'), False)
        self.assertEqual(String.is_iterative_pattern('ababc'), False)


import unittest
from lab1_5 import Edit1


class TestEdit1(unittest.TestCase):
    def test_insert1(self):
        md = Edit1(['a\n', 'b\n', 'c\n', '1\n', '2\n', '3\n', 'abc\n'])
        md.insert(2, 'qwer')
        self.assertEqual(md.get_md(), ['a\n', 'qwer\n', 'b\n', 'c\n', '1\n', '2\n', '3\n', 'abc\n'])

    def test_insert2(self):
        md = Edit1(['a\n', 'b\n', 'c\n', '1\n', '2\n', '3\n', 'abc\n'])
        md.insert('qwer')
        self.assertEqual(md.get_md(), ['a\n', 'b\n', 'c\n', '1\n', '2\n', '3\n', 'abc\n', 'qwer\n'])

    def test_append_head(self):
        md = Edit1(['a\n', 'b\n', 'c\n', '1\n', '2\n', '3\n', 'abc\n'])
        md.append_head('qwer')
        self.assertEqual(md.get_md(), ['qwer\n', 'a\n', 'b\n', 'c\n', '1\n', '2\n', '3\n', 'abc\n'])

    def test_append_tail(self):
        md = Edit1(['a\n', 'b\n', 'c\n', '1\n', '2\n', '3\n', 'abc\n'])
        md.append_tail('qwer')
        self.assertEqual(md.get_md(), ['a\n', 'b\n', 'c\n', '1\n', '2\n', '3\n', 'abc\n', 'qwer\n'])







if __name__ == '__main__':
    unittest.main()

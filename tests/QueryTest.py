import unittest
from src.Query import *


class QueryTest(unittest.TestCase):

    # testing for not implemented error
    def test_init(self):
        with self.assertRaises(NotImplementedError):
            c = Query()

    # testing for not implemented error
    def test_execute(self):
        class QuerySub(Query):
            def __init__(self):
                pass
        sub = QuerySub()
        with self.assertRaises(NotImplementedError):
            sub.execute("hi")


class SelectTest(unittest.TestCase):

    def test_one_arg(self):
        s = Select("publishers")
        self.assertEqual(s.query, "SELECT * FROM publishers;")

    def test_both_basic(self):
        s = Select("publishers", ["name", "date"])
        self.assertEqual(s.query, "SELECT name,date FROM publishers;")

    def test_both_second_empty(self):
        s = Select("publishers", [])
        self.assertEqual(s.query, "SELECT * FROM publishers;")

    def test_both_second_None(self):
        s = Select("publishers", None)
        self.assertEqual(s.query, "SELECT * FROM publishers;")


class UpdateTest(unittest.TestCase):

    def test_no_filter_col(self):
        s = Update("publishers", [("name", "Patrick")])
        self.assertEqual(s.query, "UPDATE publishers SET name=Patrick;")


    def test_filter_col(self):
        s = Update("publishers", [("age", "19"), ("gender", "male")], ("name", "Patrick"))
        self.assertEqual(s.query, "UPDATE publishers SET age=19,gender=male WHERE name=Patrick;")

class DeleteTest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()

import unittest
from timer import Timer

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_start_timer(self):
        # pattern AAA
        # A => Arange
        t = Timer()
        # A => Act
        t.start()
        result = t.start_time
        # A => Assert
        self.assertIsNotNone(result, "after time start the result should not be none")

    def test_stop_timer(self):
        # pattern AAA
        # A => Arange
        t = Timer()
        # A => Act
        t.start()
        t.stop()
        result = t.start_time
        # A => Assert
        self.assertIsNone(result, "after time stoped the result should be none")


if __name__ == '__main__':
    unittest.main()

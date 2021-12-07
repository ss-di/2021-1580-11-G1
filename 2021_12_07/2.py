from fibs import *
import unittest

class TestFibster(unittest.TestCase): 

    def test_fib(self): # тестирование первой функции
        self.assertEqual(fib(20), 6766, "Should be 6765")
    
    def test_rec_fib(self): # тестирование второй функции с учетом правильности первой
        l = [fib(i) for i in range(1, 21)]
        for i in range(1,21):
            self.assertEqual(rec_fib(i), l[i - 1])

#if __name__ == '__main__': # точка входа в программу
unittest.main(failfast=False)

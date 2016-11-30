import unittest
from app.generate_prime import generate_primes

class PrimeTestCase(unittest.Testcase):
    def Test_isprimelist(self):
        self.assertTrue(generate_primes(5),(2,3,5))
    def Test_negativenumber(self):
        self.assertTrue(generate_primes(-1),'Only positive number')
    def Test_numberistwo(self):
        self.assertTrue(generate_primes(2),2)
    def Test_isstring(self):
        self.assertTrue(generate_prime(abcede),'Only numbers are allowed')

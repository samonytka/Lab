import unittest
import lab4

class TestFoo(unittest.TestCase):
    
    def test_positive_int(self):
        self.result1, self.result2    = lab4.foo(1,2,3,4)
        self.result3, self.result4    = lab4.foo(1,11,111,1111)
        
        self.assertEquals(self.result1, 2.5)
        self.assertEquals(self.result2, 2)
        self.assertEquals(self.result3, 308.5)
        self.assertEquals(self.result4, 308)

    def test_semipos_int(self):
        self.result1, self.result2    = lab4.foo(-1,2,-3,4)
        self.result3, self.result4    = lab4.foo(2,-22,222,-2222)
        
        self.assertEquals(self.result1,0.5)
        self.assertEquals(self.result2, 0)
        self.assertEquals(self.result3,-505.0 )
        self.assertEquals(self.result4,-505)

    def test_negative_int(self):
        self.result1, self.result2    = lab4.foo(-1,-3,-5,-7)
        self.result3, self.result4    = lab4.foo(-3,-33,-333,-3333)
        
        self.assertEquals(self.result1,  -4.0)
        self.assertEquals(self.result2, -4)
        self.assertEquals(self.result3, -925.5)
        self.assertEquals(self.result4, -926)

    def test_positive_float(self):
        self.result1, self.result2    = lab4.foo(1.01, 2.02, 3.03, 4.04)
        self.result3, self.result4    = lab4.foo(12.5,5.46, 4.0, 1.34)
        
        self.assertEquals(self.result1, 2.5250000000000004)
        self.assertEquals(self.result2, 3)
        self.assertEquals(self.result3, 5.825)
        self.assertEquals(self.result4, 6)

    def test_semipos_float(self):
        self.result1, self.result2    = lab4.foo(-1.01, 2.02, -3.03, 4.04)
        self.result3, self.result4    = lab4.foo(12.5,-5.46, -4.0, 1.34)
        
        self.assertEquals(self.result1, 0.5050000000000001)
        self.assertEquals(self.result2, 1)
        self.assertEquals(self.result3, 1.095)
        self.assertEquals(self.result4, 1)

    def test_negative_float(self):
        self.result1, self.result2    = lab4.foo(-1.01, -2.02, -3.03, -4.04)
        self.result3, self.result4    = lab4.foo(-22.5,-3.46, -8.0, -2.34)
        
        self.assertEquals(self.result1, -2.5250000000000004)
        self.assertEquals(self.result2, -3)
        self.assertEquals(self.result3, -9.075)
        self.assertEquals(self.result4, -9)

if __name__ == '__main__':
    unittest.main()


import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
       
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())
        
    def test_split(self):
        quote = 'rise and shine'
        self.assertEqual(quote.split(), ['rise', 'and', 'shine'])

    def test_for_lesser(self):
        first = 10
        second = 100
        self.assertLess(first, second)

    def test_for_greater(self):
        a=109
        b=34
        self.assertGreater(a,b)

    def test_for_greater(self):
        a=109
        b=34
        self.assertGreater(b,a)

    def test_for_lessequal(self):
        x= 19
        y= 19
        self.assertLessEqual(x,y)

    def test_for_almost(self):
        e=45
        f=45
        self.assertAlmostEqual(e,f)
        

    def test_for_in(self):
        s = 'hello'
        m = 'ell'
        self.assertIn(m,s)

    def test_for_subset(self):
        k = {'name':'krati','age':25, 'college':'medicaps'}
        l = {'name':'krati','age':25}
        self.assertDictContainsSubset(l,k)
       
    def test_for_is(self):
        apple = 500
        mango = 500
        self.assertIs(apple,mango)
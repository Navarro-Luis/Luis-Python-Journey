import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('About to run a function')
    
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'shshsh'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter number')

    def tearDown(self):
        print ('im cleaning up cutie')


if __name__ == '__main__': #lets us know this is test file and will only run if main file is being run
    unittest.main()

#run python3 test.py in terminal
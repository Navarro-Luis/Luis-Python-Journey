import unittest
import excercise_testing


class TestGame(unittest.TestCase):
    def test_input(self):
        result = excercise_testing.run_guess(5,5)
        self.assertTrue(result)
    
    def test_input_incorrect(self):
        result = excercise_testing.run_guess(0,5)
        self.assertFalse(result)

    def test_input_number_range(self):
            result = excercise_testing.run_guess(12,5)
            self.assertFalse(result)

    def test_input_wrong_type(self):
            result = excercise_testing.run_guess('11',5)
            self.assertFalse(result)            
if __name__ == '__main__':
    unittest.main()
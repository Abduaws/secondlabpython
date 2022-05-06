import unittest
import EvenOdd
import MinMaxArray
import random

class TestClass(unittest.TestCase):

    def test_EvenOdd(self):
        for i in range(0, 101, 2):
            result = EvenOdd.EvenOdd.GetEvenOdd(i)
            print("Number is: "+ str(i) +", The Result is: "+result)
            self.assertEqual(EvenOdd.EvenOdd.GetEvenOdd(i), "EVEN", f'Error {i} is Even rather than Odd')
        for i in range(1, 101, 2):
            result = EvenOdd.EvenOdd.GetEvenOdd(i)
            print("Number is: "+ str(i) +", The Result is: "+result)
            self.assertEqual(EvenOdd.EvenOdd.GetEvenOdd(i), "ODD", f'Error {i} is Odd rather than Even')

    def test_MinMaxArray(self):
        print("\n\n\n")
        for i in range(0, 100):
            arr = list()
            for i in range(0, 4):
                arr.append(random.randint(0,100))
            myres = MinMaxArray.MinMaxArray.MinMaxElement(arr)
            print(f"Array is: {arr}, The Max is: {myres[0]}, The Min is: {myres[1]}")
            print(f"Actual max: {max(arr)}, Actual min: {min(arr)}")
            self.assertEqual(myres[0], max(arr), f'Error Expected Max {max(arr)} Instead Got {myres[0]}')
            self.assertEqual(myres[1], min(arr), f'Error Expected Min {min(arr)} Instead Got {myres[1]}')


if __name__ == '__main__':
    unittest.main()
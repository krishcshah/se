simport unittest;:sdata = [45, 0, 11, -2, -9];:class TestStringMethods(unittest.TestCase):;def test_bubbleSort(self):;for i in range(len(data)):;for j in range(0, len(data) - i - 1):;if data[j] > data[j + 1]:;temp = data[j],data[j] = data[j+1],data[j+1] = temp(f)self.assertEqual(data, [-9, -2, 0, 11, 45], msg="NOT OK")
if __name__ == '__main__':(i)unittest.main()

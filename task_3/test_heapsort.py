import unittest
from heapsort import heap_sort

class TestHeapSort(unittest.TestCase):
    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        heap_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        heap_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        arr = [3, 1, 4, 1, 5]
        heap_sort(arr)
        self.assertEqual(arr, [1, 1, 3, 4, 5])

    def test_empty_array(self):
        arr = []
        heap_sort(arr)
        self.assertEqual(arr, [])

    def test_single_element_array(self):
        arr = [42]
        heap_sort(arr)
        self.assertEqual(arr, [42])

    def test_identical_elements(self):
        arr = [7, 7, 7]
        heap_sort(arr)
        self.assertEqual(arr, [7, 7, 7])

    def test_large_numbers(self):
        arr = [1000000, -1000000, 0]
        heap_sort(arr)
        self.assertEqual(arr, [-1000000, 0, 1000000])


if __name__ == "__main__":
    unittest.main()


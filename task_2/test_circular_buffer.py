import unittest
from circular_buffer import CircularBuffer
from circular_buffer_shifts import CircularBufferShifts

class TestCircularBuffer(unittest.TestCase):

    def setUp(self):
        self.buffer = CircularBuffer(capacity=5)

    def test_add_and_get_value(self):
        self.buffer.add_value(1)
        self.buffer.add_value(2)
        self.buffer.add_value(3)
        self.assertEqual(self.buffer.get_front_value(), 1)
        self.assertEqual(self.buffer.show_count(), "Count of variables in FIFO: 3")

    def test_over_capacity(self):
        for i in range(6):  # Adding more than capacity
            self.buffer.add_value(i)
        self.assertEqual(self.buffer.get_front_value(), 1)  # Should still return the first added value
        self.assertEqual(self.buffer.show_count(), "Count of variables in FIFO: 5")  # Count should not exceed capacity

    def test_pop_front(self):
        self.buffer.add_value(1)
        self.buffer.add_value(2)
        self.buffer.pop_front()
        self.assertEqual(self.buffer.get_front_value(), 2)
        self.assertEqual(self.buffer.show_count(), "Count of variables in FIFO: 1")

    def test_pop_empty_buffer(self):
        initial_count = self.buffer.show_count()
        self.buffer.pop_front()  # Should not change anything
        self.assertEqual(initial_count, self.buffer.show_count())

    def test_get_front_empty_buffer(self):
        self.assertEqual(self.buffer.get_front_value(), "FIFO is empty!")

class TestCircularBufferShifts(unittest.TestCase):

    def setUp(self):
        self.shift_buffer = CircularBufferShifts(capacity=5)

    def test_add_and_get_value(self):
        self.shift_buffer.add_value(1)
        self.shift_buffer.add_value(2)
        self.shift_buffer.add_value(3)
        self.assertEqual(self.shift_buffer.get_front_value(), 1)
        self.assertEqual(self.shift_buffer.show_count(), "Count of variables in FIFO: 3")

    def test_over_capacity(self):
        for i in range(6):  # Adding more than capacity
            self.shift_buffer.add_value(i)
        self.assertEqual(self.shift_buffer.get_front_value(), 1)  # Should still return the first added value
        self.assertEqual(self.shift_buffer.show_count(), "Count of variables in FIFO: 5")  # Count should not exceed capacity

    def test_pop_front(self):
        self.shift_buffer.add_value(1)
        self.shift_buffer.add_value(2)
        self.shift_buffer.pop_front()
        self.assertEqual(self.shift_buffer.get_front_value(), 2)
        self.assertEqual(self.shift_buffer.show_count(), "Count of variables in FIFO: 1")


    def test_get_front_empty_buffer(self):
        self.assertEqual(self.shift_buffer.get_front_value(), "FIFO is empty!")

if __name__ == '__main__':
    unittest.main()

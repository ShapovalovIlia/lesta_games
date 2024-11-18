class CircularBuffer:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._front = 0
        self._end = 0
        self._cnt = 0
        self._data = list(range(0, capacity))

    def _move_left(self):
        if self._front < self._capacity - 1:
            self._front += 1
        else:
            self._front = 0

    def __change_count(self):
        if self._cnt < self._capacity:
            self._cnt += 1
        else:
            pass

    def add_value(self, value):
        if self._end <= self._capacity - 1:
            if (self._end == self._front) and (self._cnt != 0):
                self._move_left()
            self._data[self._end] = value
            self._end += 1
            self.__change_count()
        else:
            self._end = 0
            if (self._end == self._front) and (self._cnt != 0):
                self._move_left()
            self._data[self._end] = value
            self._end += 1
            self.__change_count()

    def pop_front(self):
        if self._cnt > 0:
            self._cnt -= 1
            self._move_left()
        else:
            pass

    def get_front_value(self):
        if self._cnt > 0:
            temp = self._data[self._front]
            return temp
        else:
            return "FIFO is empty!"

    def show_count(self):
        return "Count of variables in FIFO: " + str(self._cnt)

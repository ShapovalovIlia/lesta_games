class CircularBufferShifts:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._cnt = 0
        self._data = list(range(0, capacity))

    def _change_count(self):
        if self._cnt < self._capacity:
            self._cnt += 1
        else:
            pass

    def add_value(self, value):
        self._data[-1] = value
        self._change_count()
        self._data.insert(0, self._data.pop())

    def get_front_value(self):
        if self._cnt > 0:
            temp = self._data[self._cnt - 1]
            return temp
        else:
            return "FIFO is empty!"

    def pop_front(self):
        for _ in range(self._cnt - 1):
            self._data.append(self._data.pop())
        self._cnt -= 1

    def show_count(self):
        return "Count of variables in FIFO: " + str(self._cnt)

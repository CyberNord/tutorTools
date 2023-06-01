class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, num):
        self.heap.append(num)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def print_heap(self):
        print("Heap: ", self.heap)

    def heapify_down(self, i):
        size = len(self.heap)
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < size and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)


def split_number(n):
    num_str = str(n)
    while len(num_str) < 8:
        num_str = "0" + num_str
    nr1 = int(num_str[:3])  # Digits 0, 1, 2
    nr2 = int(num_str[3:5])  # Digits 3, 4
    nr3 = int(num_str[5:7])  # Digits 5, 6
    nr4 = int(num_str[7])  # Last digit
    print("k" + num_str + ": n1=" + str(nr1) + ", n2=" + str(nr2) + ", n3=" + str(nr3) + ", n4=" + str(nr4))

    return nr1, nr2, nr3, nr4


###################################################################################
heap = MinHeap()
n1, n2, n3, n4 = split_number(12345678)
numbers = [107, 79, n1, 59, n2, 62, 23, 47, n3, 19, 24, n4, 6]

for num in numbers:
    heap.insert(num)
    heap.print_heap()

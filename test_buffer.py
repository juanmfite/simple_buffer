from unittest import TestCase

from buffer import Buffer
from constants import PolicyCts

class BufferTestCase(TestCase):

    def setUp(self):
        self.fifo_buffer = Buffer(PolicyCts.FIFO)
        self.lifo_buffer = Buffer(PolicyCts.LIFO)

    def test_fifo_buffer(self):
        self.fifo_buffer.insert(1)
        self.fifo_buffer.insert(2)
        self.assertEqual(self.fifo_buffer.size(), 2)

        item = self.fifo_buffer.extract()
        self.assertEqual(item, 2)

        self.fifo_buffer.extract()
        self.assertEqual(self.fifo_buffer.size(), 0)

    def test_lifo_buffer(self):
        self.lifo_buffer.insert(1)
        self.lifo_buffer.insert(2)
        self.assertEqual(self.lifo_buffer.size(), 2)

        item = self.lifo_buffer.extract()
        self.assertEqual(item, 1)

        self.lifo_buffer.extract()
        self.assertEqual(self.lifo_buffer.size(), 0)
    
    def test_empty_buffer(self):
        self.fifo_buffer.insert(1)
        self.fifo_buffer.extract()
        self.fifo_buffer.extract()
        self.assertEqual(self.fifo_buffer.show(), [])
    
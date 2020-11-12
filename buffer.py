from constants import PolicyCts

__all__ = ['Buffer']


class Buffer:
    """
    A buffer that handles insertion & consumption of items.
    Has 2 possible policies: FIFO (First In First Out) and LIFO (Last In
    First Out).
    """

    def __init__(self, policy):
        policy = policy.upper()
        if policy not in PolicyCts.ACCEPTED_POLICIES:
            raise ValueError()
        self._policy = policy
        self._buffer = []

    def insert(self, item):
        self._buffer.append(item)
    
    def extract(self):
        try:
            if self._policy == 'FIFO':
                return self._fifo_extract()
            return self._lifo_extract()
        except IndexError:
            return
    
    def show(self):
        return self._buffer
    
    def size(self):
        return len(self._buffer)
    
    def _fifo_extract(self):
        return self._buffer.pop()
    
    def _lifo_extract(self):
        return self._buffer.pop(0)


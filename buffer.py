

class Buffer:
    """
    A buffer that handles insertion & consumption of items.
    Has 2 possible policies: FIFO (First In First Out) and LIFO (Last In
    First Out).
    """

    def __init__(self, policy):
        policy = policy.upper()
        if policy not in ["FIFO", "LIFO"]:
            raise ValueError()
        self._policy = policy
        self.data = []

    def insert(self, item):
        self.data.append(item)
    
    def extract(self):
        try:
            if self._policy == "FIFO":
                return self._fifo_extract()
            return self._lifo_extract()
        except IndexError:
            return
    
    def _fifo_extract(self):
        return self.data.pop()
    
    def _lifo_extract(self):
        return self.data.pop(0)


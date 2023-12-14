class Dataset:
    def __init__(self):
        self.min = None
        self.max = None
        self.elements = set()
        self.products = []

    def push(self, x):
        self.elements.add(x)
        if self.min is None:
            self.min = x
            self.max = x
        else:
            if self.min > x:
                self.min = x
            if self.max < x:
                self.max = x
        self.products.append(self.min * self.max)

    def pop(self, x):
        self.elements.remove(x)
        self.min = min(self.elements)
        self.max = max(self.elements)
        self.products.append(self.min * self.max)

    def to_array(self):
        return self.products


def maxMin(operations, x):
    ds = Dataset()
    for i in range(len(operations)):
        if operations[i] == "push":
            ds.push(x[i])
        elif operations[i] == "pop":
            ds.pop(x[i])
    return ds.to_array()
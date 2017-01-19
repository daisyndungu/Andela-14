class BinarySearch(list):
    length = 0

    def __init__(self, a, b):
        super(BinarySearch, self).__init__()
        self.length = a
        num = b
        while num <= a * b:
            self.append(num)
            num += b

    def search(self, num):
        count = 0

        element = self

        while len(element) > 1:
            count += 1
            half = len(element) / 2

            if num == element[half]:
              
                element = []
            elif num > element[half - 1]:
                element = element[half:len(element) - 1]
              
            else:
                element = element[0:half]
              
        try:
            index = self.index(num)
        except ValueError:
            index = - 1
        return {'count': count, 'index': index}

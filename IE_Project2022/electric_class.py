class electric:
    def __init__(self, weight, height, leight, price, producer):
        self.weight = weight
        self.height = height
        self.leight = leight
        self.price = price
        self.producer = producer


class tv(electric):
    def __init__(self, weight, height, leight, price, producer, inch, brightness, resolution):
        super().__init__(weight, height, leight, price, producer)  # initiate parent properties
        self.inch = inch
        self.brightness = brightness
        self.resolution = resolution

    def printDetails(self):
        print('weight:{}, height:{}, leight:{}, price:{}, producer:{}, inch:{}, brightness:{}, resolution:{}'.format(
            self.weight, self.height, self.leight, self.price, self.producer, self.inch, self.brightness,
            self.resolution))


# Main:
tv1 = tv(25, 185, 40, 5705, 'Sony', 65, '100%', 88)
tv2 = tv(25, 185, 40, 4300, 'LG', 65, '100%', 77)

print(tv1.printDetails())
print(tv2.printDetails())

print('updating the tv size...')
tv1.inch = 100
print('tv1 new size is:{}'.format(tv1.inch))
print('tv1 new details are: '+ str(tv1.printDetails()))
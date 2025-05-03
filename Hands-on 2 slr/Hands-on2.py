import random

class SLR:
    def __init__(self, dataset):
        self.dataset = dataset
        self.x = self.dataset['advertising']
        self.y = self.dataset['sales']

    # calcular B0
    def b0(self):
        # sumatorias necesarias
        sumX2 = self.sumX2()
        sumX = self.sumX()
        sumY = self.sumY()
        sumXY = self.sumXY()

        arriba = sumX2*sumY - sumX*sumXY
        abajo = len(self.x)*(sumX2) - sumX**2
        return arriba/abajo

    # calcular B1
    def b1(self):
        # sumatorias necesarias
        sumX2 = self.sumX2()
        sumX = self.sumX()
        sumY = self.sumY()
        sumXY = self.sumXY()

        arriba = len(self.x)*(sumXY) - sumX*sumY
        abajo = len(self.x)*(sumX2) - sumX**2
        return arriba/abajo

    # sumatoria de Xi^2
    def sumX2(self):
        sum = 0
        for i in self.x:
            sum += int(i)**2
        return sum
    # sumatoria de Yi
    def sumY(self):
        sum = 0
        for i in self.y:
            sum += int(i)
        return sum
    # sumatoria de Xi
    def sumX(self):
        sum = 0
        for i in self.x:
            sum += int(i)
        return sum
    #sumatoria de Xi*Yi
    def sumXY(self):
        sum = 0
        for i in range(len(self.x)):
            sum += int(self.x[i])*int(self.y[i])
        return sum

if __name__ == '__main__':
    dataset = {
        'sales' : ['651','762','856','1063','1190','1298','1421','1440','1518'],
        'advertising' : ['23','26','30','34','43','48','52','57','58']
    }

    slr = SLR(dataset)
    print(f'y = {slr.b0()} + {slr.b1()}*x')
    print(f'\n \nCalculo de advertising')
    for i in range(0,5):
        advertising = random.randint(20,60)
        y = slr.b0() + slr.b1()*advertising
        print(f'advertising: {advertising}')
        print(f'y = {slr.b0()} + {slr.b1()}*{advertising}')
        print(f'y = {y}')
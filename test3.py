class Vehicle:
    def __init__(self, maxsp, mileage, scap=24):
        self.maxsp=maxsp
        self.mileage=mileage
        self.scap=scap

    def Display(self, maxsp, mileage):
        print("Max speed: ", self.maxsp)
        print("Mileage: ", self.mileage)

    def Calc(self):
        print("Fare: ", self.scap*120)

class Traveller(Vehicle):
    def __init__(self, ms, mil, seat=24):
        self.seat=seat
        self.ms=ms
        self.mil=mil    

    def CalcFare(self):
        Fare = self.seat*120 + (0.1*self.seat*120)
        print("Fare: ", Fare)

p1 = Vehicle(maxsp=50,mileage=10)
p1.Calc()
p2 = Traveller(ms=50,mil=10)
p2.CalcFare()
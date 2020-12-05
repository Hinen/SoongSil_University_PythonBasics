## 클래스 선언 부분 ##
class  Car :
    speed = 0
    def upSpeed(self, value):
        self.speed += value
        
        print("현재 속도(슈퍼 클래스) : %d" % self.speed)

class Sedan(Car) :
    def upSpeed(self, value):
        self.speed += value
        
        if self.speed > 150 :
            self.speed = 150
            
        print("현재 속도(서브 클래스) : %d" % self.speed)

class Truck(Car) :
    pass

class Sonata(Sedan):
    pass

## 변수 선언 부분 ##
sedan1, truck1, sonata1 = None, None, None

## 메인 코드 부분 ##
truck1 = Truck()
sedan1 = Sedan()
sonata1 = Sonata()

print("트럭 --> ", end = "")
truck1.upSpeed(200)

print("승용차 --> ", end = "")
sedan1.upSpeed(200)

print("소나타 --> ", end = "")
sonata1.upSpeed(200)
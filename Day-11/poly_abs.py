#problem-01 the paymant gateway (Polymorphism)
class CreditCardPayment:
    def process_payment(self,amount):
        print(f"Processing credit card payment ${amount}")

class PayPalPayment:
    def process_payment(self,amount):
         print(f"Processing PayPal payment ${amount}")

def execute_payment(paymentObject, amount):
    paymentObject.process_payment(amount)

credit1= CreditCardPayment() 
paypal=PayPalPayment()
execute_payment(credit1, 1000)
execute_payment(paypal, 500)



#problem-02 The vehicle blueprint(Abstraction)
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("car engine roaring to life!")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine revving")

car1=Car()
motor1=Motorcycle()
car1.start_engine()
motor1.start_engine()
try:
    vehicle = Vehicle()
except TypeError as e:
    print(e)    

    
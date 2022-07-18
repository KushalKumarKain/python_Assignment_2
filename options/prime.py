from abc import ABC,abstractmethod
import numbers

class PRIME(ABC):
   @abstractmethod
   def run(self):
      pass
number = int(input("Enter number of choice : "))
class prime(PRIME):
   def run(self, number):

# Number is prime or not

    flag = False

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                flag = True
                break

    if flag:
        print(number, "is not a prime number")
    else:
        print(number, "is a prime number")
        
P = prime()
P.run(number)
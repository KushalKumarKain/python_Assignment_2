from abc import ABC,abstractmethod
import numbers

class fibonacci(ABC):
   @abstractmethod
   def run(self):
      pass
number = int(input("Enter number of choice : "))
class fibo(fibonacci):
   def run(self, number):

      n1 = 0
      n2 = 1

      if number < 0:
         print("Please enter a positive integer")
         
      elif number == 0:
         return n2
      
      # generate fibonacci sequence
      else:
         print("Fibonacci sequence:")
         while n1 < number:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            n1 += 1

F = fibo()
F.run(number)
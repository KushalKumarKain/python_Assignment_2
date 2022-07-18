import main

from abc import ABC,abstractmethod

class fibonacci(ABC):
   @abstractmethod
   def run(self):
      pass
    
class PRIME(ABC):
   @abstractmethod
   def run(self):
      pass
    
class armstrong(ABC):
   @abstractmethod
   def run(self):
      pass
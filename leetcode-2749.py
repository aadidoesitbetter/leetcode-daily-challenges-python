import math

class Solution:
  def makeTheIntegerZero(self, num1: int, num2: int) -> int:
    
    for k in range(1, 101):
        target = num1 - k * num2
        
        if target >= 0 and target.bit_count() <= k and k <= target:
            return k
            
    return -1
#Kieran Uptagrafft
#Rat Class
#9/4/2024
from math import ceil


class Rat:
  def __init__(self, sex, weight):
    self.sex = sex
    self.weight = weight
    self.litters = 0
  def __str__(self):
    return f"{self.weight}{self.sex}"
  def __repr__(self):
    return f"{self.weight}{self.sex}"
  def getWeight(self):
    return self.weight
  def getSex(self):
    return self.sex
  def canBreed(self):
    return self.litters <= 5
  def __lt__(self, obj):
    return ((self.weight) < (obj))

  def __gt__(self, obj):
    return ((self.weight) > (obj))

  def __le__(self, obj):
    return ((self.weight) <= (obj))

  def __ge__(self, obj):
    return ((self.weight) >= (obj))

  def __eq__(self, obj):
    return (self.weight == obj)
  def mutate2(self, scale):
    self.weight = ceil(self.weight * scale)
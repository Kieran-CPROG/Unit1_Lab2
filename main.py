#Kieran Uptagrafft
#A large rat / U1 L1
#9/4/2024

from theColony import Rat
from math import ceil
import random
import time
GOAL = 50000                # Target average weight (grams)
NUM_RATS = 20               # Max adult rats in the lab
INITIAL_MIN_WT = 200        # The smallest rat (grams)
INITIAL_MAX_WT = 600        # The chonkiest rat (grams)
INITIAL_MODE_WT = 300       # The most common weight (grams)
MUTATE_ODDS = 0.01          # Liklihood of a mutation
MUTATE_MIN = 0.5            # Scalar mutation -ghgh least beneficial
MUTATE_MAX = 1.2            # Scalar mutation - most beneficial
LITTER_SIZE = 8             # Pups per litter (1 mating pair)
GENERATIONS_PER_YEAR = 10   # How many generations are created each year
GENERATION_LIMIT = 500      # Generational cutoff - stop breeded no matter what

def calculate_weight(sex, mother, father):
  '''Generate the weight of a single rat'''
  # Use the triangular function from the random library to skew the 
  #baby's weight based on its sex
  min = mother.getWeight()
  max = father.getWeight()
  if sex == "M":
    wt = int(random.triangular(min, max, max))
  else:
    wt = int(random.triangular(min, max, min))
  return wt



def initial_population():
  '''Create the initial set of rats based on constants'''
  rats = [[],[]]
  mother = Rat("F", INITIAL_MIN_WT)
  father = Rat("M", INITIAL_MAX_WT)
  
  for r in range(NUM_RATS):
    if r < 10:
      sex = "M"
      ind = 0
    else:
      sex = "F"
      ind = 1
  
    wt = calculate_weight(sex, mother, father)
    R = Rat(sex, wt)
    rats[ind].append(R)
  return rats



def mutate(pups):
  """Check for mutability, modify weight of affected pups"""
  for group_of_rats in pups:
    for oneRat in group_of_rats:
      num = random.random()
      num2 = random.uniform(MUTATE_MIN, MUTATE_MAX)
      if num <= MUTATE_ODDS:
        oneRat.mutate2(num2)
      
  return pups  



def breed(rats):
  """Create mating pairs, create LITTER_SIZE children per pair"""
  children = [[],[]]
  pairs = []
  for x in range(10):
    pairs.append([])
  
  for group_of_rats in rats:
    for count, oneRat in enumerate(group_of_rats):
      pairs[count].append(oneRat)


  for couple in pairs:
    for parent in range(LITTER_SIZE):
      sex = random.choice(['M', 'F'])
      if sex == 'M':
        ind = 0
      else:
        ind = 1
      father = pairs[parent][0]
      mother = pairs[parent][1]
      pairs[parent][0].litters += 1
      pairs[parent][1].litters += 1
      wt = calculate_weight(sex, mother, father)
      R = Rat(sex, wt)
      children[ind].append(R)

  return children  



def select(rats, pups):
  '''Choose the largest viable rats for the next round of breeding'''
  newColony = [[],[]]
  largest = []
  listSpace = 0
  rats[0].extend(pups[0])
  rats[1].extend(pups[1])
  for group_of_rats in rats:
    group_of_rats.sort(reverse=True)
    for count, oneRat in enumerate(group_of_rats):
      
      if count == 10:
        listSpace += 1
        break

      if oneRat.canBreed == True:
        pass
      else:
        newColony[listSpace].append(oneRat)
  if rats[0][0] > rats[1][0]:
    largest = rats[0][0]
  else:
    largest = rats[1][0] 
  return newColony, largest



def calculate_mean(rats, pups):
  '''Calculate the mean weight of a population'''
  numRats = 0
  sumWt = 0
  rats[0].extend(pups[0])
  rats[1].extend(pups[1])
  
  for group_of_rats in rats:
    numRats += len(group_of_rats)
    for oneRat in group_of_rats:
      sumWt += oneRat.getWeight()
  
  return sumWt // numRats



def fitness(rats, mean):
  """Determine if the target average matches the current population's average"""
  return mean >= GOAL, mean



def draw(means, largest, gen, go, finish):
  count = 0
  print("\n", f"Final Mean: {means[-1]}g", "\n")
  print(f"Excution Time: {finish - go}")
  print(f"Generations: {gen}")
  print(f"Experiment Durations: {gen / GENERATIONS_PER_YEAR} years")
  print(f"Largest Rat: {largest.getWeight()}g ({largest.getSex()})", "\n")
  print("Generations Weight Averages:", "\n")
  for x in means:
    count += 1
    print(x, end = " ")
    if count == 10:
      print()
      count = 0
  print()
  print()



def main():
  count = 0
  Flag = True
  start = time.time()
  ratColony = initial_population()
  ratColony = mutate(ratColony)
  averages = []
  while count <= GENERATION_LIMIT and Flag == True:
    child = breed(ratColony)
    child = mutate(child)
    mean = calculate_mean(ratColony, child)
    ratColony, large = select(ratColony, child)
    metGoal, mean = fitness(ratColony, mean)
    averages.append(mean)
    if metGoal == True:
      Flag = False
    count += 1
  end = time.time()
  draw(averages, large, count, start, end)
if __name__ == "__main__":
  main()
#Kieran Uptagrafft
#9/16/2024
#Unit 1 Lab 2

import matplotlib.pyplot as plt


def graph(data, data2, data3):
  for dataset in [data, data2, data3]:
    plt.plot(dataset)

    plt.title("Rat Growth")
    plt.ylabel("Rat's Weight (Grams)")
    plt.xlabel("Generation")

  plt.legend(["gen_maxs.txt", "gen_min.txt", "gen_avgs.txt"])

  plt.show()
  plt.savefig("rats_graph.png")

def clean(openFile):
  cleansed = []
  for x in openFile:
    cleansed.append(int(x.replace("\n", "")))
  return cleansed


def read_file(string):
  with open(string, 'r') as file1:
    opened = file1.readlines()
  cleaned = clean(opened)
  return cleaned
def main():
  cleansed = read_file("largeNums.txt")
  cleansed2 = read_file("smallNums.txt")
  cleansed3 = read_file("meansNums.txt")
  graph(cleansed, cleansed2, cleansed3)


if __name__ == "__main__":
  main()
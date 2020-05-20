import random
def cool():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  rnd1 = random.randint(0, last)

  print(quotes[rnd],quotes[rnd1])

if __name__== "__main__":
  cool()

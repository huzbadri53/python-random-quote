import random
def cool():
  #print("Keep it logically awesome.")
  f = open("quotes.txt","w")
  for i in range(5):
    f.write("This is Line number %d\r\n" % (i+1))
  f.close()
  f = open("quotes.txt")
  quotes = f.readlines()
  #f = open("quotes.txt","r")
  #if f.mode == "r":
  #  quotes = f.read()
  #print (quotes)
  #quotes = f.read()
  #f.close()
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  rnd1 = random.randint(0, last)

  print(quotes[rnd],quotes[rnd1])

if __name__== "__main__":
  cool()

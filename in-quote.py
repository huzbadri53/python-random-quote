def fromuser():
  f = open("quotes.txt","a+")
  print("Number of quotes you wish to enter: ")
  k = input()
  k1 = int(k)
  f.write("\n")
  for i in range(k1):
    print("Kindly enter quote number %d: " % (i+1))
    user = input()
    f.write("%s\n" % user)
  f.close()
  print("\n")
  #Ask whether to print the new file
  print("Do you wish to see the updated file?\nEnter Y for Yes and N for No :")
  o = input()
  if o == "Y":
    print("\n")
    f = open("quotes.txt","r")
    quotes = f.readline()
    while (quotes):
      print(quotes)
      quotes = f.readline()
    f.close()
if __name__ == "__main__":
  fromuser()

  
  


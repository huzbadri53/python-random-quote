def main():
  f = open("quotes.txt","r")
  quotes = f.readline()
  while (quotes):
    print(quotes)
    quotes = f.readline()
  f.close()
if __name__ == "__main__":
  main()
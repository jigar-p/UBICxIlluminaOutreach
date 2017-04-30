#tests of lists

def printingLists(sampleList[]):
  input = raw_input("Type 'first n' if you want to print the first n characters or 'all' if you want to print the entire list: ")
  if input == 'first n':
    n = input("What is n? ")
    while n<1:
      print "Number not greater than 1"
      n = input("What is n? ")
    print sampleList[1:n]
  if input == 'all':
    print sampleList

def makeList():
  while raw_input("Do you want to add an element? (Y or N) " == "Y"
    

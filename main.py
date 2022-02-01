
while True:
  #Makes sure the code runs forever
  try:  #prevents any errors
    
    owedbefore = int(input("\nInput how much that person owes before tip and tax: "))
    #Takes input
    if owedbefore == 10 or owedbefore == 12 or owedbefore == 9 or owedbefore == 8 or owedbefore == 7 or owedbefore == 15 or owedbefore == 11 or owedbefore == 30:  
      #Only calculates if anyone owed that amount of money
      owedafter = owedbefore * 1.5 * 1.15 
      #Calculates tip and tax
      rowedafter = "{:.2f}".format(owedafter)
      #Prevents any decimals going past the hundrets place
      print("That person owes $", rowedafter, "after tax an tip")
      #Tells user the amount owed
    else:
      print("No one owed that amount of money!")
      #Ensures they only input a number that was listed
  except:
    print("Please only integer amounts!")
#Tells user to make sure the input is an integer



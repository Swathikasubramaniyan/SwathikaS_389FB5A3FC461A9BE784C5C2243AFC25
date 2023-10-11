def leap(Year) :
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("This year is leap year")
  else:  
    print ("This year is not a leap Year")  
Year = int(input("Enter the number: "))  
leap(Year)
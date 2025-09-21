number=int(input("Enter a number to see its multiplication table:"))
for i in range(1,11):
    #print a header for each table
    print(f"multiplication table for {i}:")
    #use an inner for loop for the multipliers(1,10)
    for j in range(1,11):
        #print the product for each iteration
        print(f"{i}*{j}={i*j}")
        
        print()
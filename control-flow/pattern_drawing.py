user_size=int(input("Enter the  size of the pattern:"))
rows=0
while rows<=user_size:
    column=0
    for column in range(user_size):
         print("*" , end="")
         column+=1
        
    print()
    rows+=1
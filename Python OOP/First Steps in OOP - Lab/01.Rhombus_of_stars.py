rows = int(input())

# Loop through rows
for i in range (1,rows + 1):
    
    # Trailing spaces
    for j in range (1,rows - i + 1):
        print (end=" ")
        
    # Printing pattern
    for j in range (1,rows + 1):
        print ("*",end=" ")
    print()
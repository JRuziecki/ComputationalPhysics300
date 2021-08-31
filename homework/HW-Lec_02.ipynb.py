def Fibonacci(N):
    
    x1,x2 = 1,1 #Starting values for the Fibonacci sequence
    counter = 1 #Counter to keep track of the length of the sequnce
    
    while counter <= N:#Loops until each number in the Fib. sequence is calculated based on the users request
        if N==0:
            print("0")
            break
        else:
            print(x1)
            x1,x2 = x2,x1+x2 #Calculates the following number in the sequence by adding the previous two
            counter += 1     #Adds one to the counter for each loop, up to the desired amount of numbers in the sequence
    return "End of Sequence"

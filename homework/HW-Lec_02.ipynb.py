def Fibonacci(N):
    
    x1,x2 = 1,1 #Starting values for the Fibonacci sequence
    counter = 1 #Variable used in breaking out of the while loop
    
    while counter <= N: #Loops until each number in the Fib. sequence is calculated and displayed, up to N times
        if N==0:
            print("0")
            break
        else:
            print(x1)
            x1,x2 = x2,x1+x2 #Calculates the following number in the sequence by adding the previous two
            counter += 1     #Adds one to the counter for each iteration through the loop, until the counter value is larger than the user input value of N
    return "End of Sequence" 

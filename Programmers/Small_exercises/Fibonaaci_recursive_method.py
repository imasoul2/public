
# fibonacci using resursive function

def fibonacci(sequence, a=[0,1]): # fibonacci sequence starts with 0,1 ....
    temp = a # assign the argument as temp
    
    if sequence > 0: # check if it needs to stop iterations.
        temp.append(temp[len(temp)-1]+temp[len(temp)-2]) # get the sum of previous two series.
        fibonacci(sequence-1,temp) # recursive method
        
    else:
        print("Final fibonacci sequence is {}".format(temp)) # print out the whole sequence.
    

fibonacci(3) # for testing.

# Programmers Coding Test
# Skill check test Level 2

# CJ Jang 07/09/2020

# Question: when the user is given a series of string 's' (that has length of 1 or more)
# and 's' is made up of alphabets and whitespaces,
# Return the s as converted to JadenCase (First letter of each word is Capitalised while the rest is in lower case )

def solution(s):
    answer = ''
    temp = s.split(" ") # split the string by white spaces
    outer_count = 0 # here to count the number of outer loop has run
    for i  in temp: # loop through split string
        str_list = list(i) # make each string iterable by converting to a list
        inner_count = 0 # count for inner loop
        for j in str_list:
            if inner_count ==0: # the first letter is guaranteed to be Upper
                j = j.upper() 
            else:
                j = j.lower() # while the rest is lower
            answer += j # concatenate to the answer string
            inner_count += 1
        if outer_count < len(temp)-1: # add whitespace to a string
            answer += ' '
        outer_count += 1
        
    return answer

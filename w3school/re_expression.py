import re 

txt = "The rain in Spain"
# ^ <- Starts with 
# .* any character repetition.
# $ <- Ends with
x = re.search("^The.*Spain$", txt)
print(x)

# re modules offers a set of functiosn such as
# re.findall => returns a list containing all matches
# re.search => returns a Match object if there is a match anywhere in the string.
# re.split => returns a list where the string has been split at each match
# re.sub => replaces one or many mathces with a string.

# [] : A set of character   [a-m]
# \  : Special sequence   \d  \n ...etc
# .  : Any character except newline
# ^  : starts with
# $  : ends with  
# *  : zero or more occurences eg. aix*
# +  : one or more occurences (at least one match)  eg. aix+
# {} : exact the specified number of occurences  eg. al{2}
# | : either or  falls|stays
# () : Capture and group

"""
Special Sequence :  /
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain" r"ain\b"	
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain" r"ain\B"	
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

"""
# Example:
x = re.search(r"\D\D","h2i3yall")
print(x)


# findall function : returns a list containing all the match
x = re.findall (r".i","Rain drops in Spain")
print(x)
# empty list if there are no matches

# serach function : searches a string for a match, returns match object if there are any.
# the method of search could be greedy or non-greedy

txt = "There are 7 people in a house"
x = re.search(r"\s",txt)
print(x) # returns the first match.
# returns None if there are zero matches

# split function : retruns a list WHERE the string has been split at each matches
x = re.split(r"\s",txt)
print(x)
# you can also specify how many times you want the split to occur.
x = re.split(r"\s",txt,2)
print(x)


# sub function : replaces(substitutes) the matches with the text of my choice
x = re.sub(r"house","club",txt,1)
print(x)

# match function : returns an object containing the match.
txt = "The rain in Spain"
x = re.search(r"Spain", txt)
print(x)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


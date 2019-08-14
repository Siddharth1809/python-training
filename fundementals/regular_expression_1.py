import re

# function compile()
# compile() creates regular expression
#          character class

p = re.compile(r'[a-e]')

# findall() searches for the regular expression
#          and return a list upon finding

print(p.findall("Aye, said Mr. Gibenson Stark"))  # same output as below

print(re.findall(r'[a-e]', "Aye, said Mr. Gibenson Stark"))

# use of \  only use with special character
print(re.findall(r'\$@', 'im$@d1809@gmail@.com'))  # ['$@'}
print(re.findall(r'\$', 'im$@id18$9@gmail.com'))  # ['$','$']

# \d  matches any decimal digit [0-9]
p = re.compile(r'\d')
print(p.findall("i went to him at 11 A.M. on 4th July 1886"))
# ['1', '1', '4', '1', '8', '8', '6']


p = re.compile(r'\d+')
print(p.findall("i went to him at 11 A.M. on 4th July 1886"))
# ['11', '4', '1886']


# \w matches any alphanumeric character [a-zA-Z0-9_]
p = re.compile(r'\w')
print(p.findall("He said * in some_lang"))
# ['H', 'e', 's', 'a', 'i', 'd', 'i', 'n', 's', 'o', 'm', 'e', '_', 'l', 'a', 'n', 'g']


p = re.compile(r'\w+')
print(p.findall("I went to him at 11 A.M. , he said *** in some_language."))
# ['I', 'went', 'to', 'him', 'at', '11', 'A', 'M', 'he', 'said', 'in', 'some_language']


# \W non-alphanumeric character
p = re.compile(r'\W')
print(p.findall("he said *** in some_language."))
# [' ', ' ', '*', '*', '*', ' ', ' ', '.']


#############################################################################


# function re.split(pattern, string ,maxsplit=0, flags=0)


# \W+ means non-alphanumeric character with one or more occurrence
#           but we use re.split so it splits at non-alphanumeric character
#           likes ','  ,   ' '  ,  '.'
print(re.split(r'\W+', 'Words,words,Words'))
# ['Words', 'words', 'Words']

print(re.split(r'\W+', "Word's,words,Words"))
# ['Word', 's', 'words', 'Words']


print(re.split(r'\W+', "On 12th Jan 2016, at 11:02 AM"))
# ['On', '12th', 'Jan', '2016', 'at', '11', '02', 'AM']

print(re.split(r'\W+', "On 12th Jan 2016, at 11:02 A.M."))
# ['On', '12th', 'Jan', '2016', 'at', '11', '02', 'A', 'M', '']


# \d+ means any digit with one or more occurrence
#           but we use re.split so it splits at digits

print(re.split(r'\d+', "On 12th Jan 2016, at 11:02 AM"))
# ['On ', 'th Jan ', ', at ', ':', ' AM']


# splitting occurs only once at 12 because maxsplit is given as 1
print(re.split(r'\d+', "On 12th Jan 2016, at 11:02 AM", 1))
# ['On ', 'th Jan 2016, at 11:02 AM']


# boy and Boy will be treated same when flags = re.IGNORECASE
# Aey is treated as aey
# re.IGNORECASE means ignore upper
#                           lower case
print(re.split(r'[a-f]+', "Aey, Boy oh boy, come here", flags=re.IGNORECASE))
# ['', 'y, ', 'oy oh ', 'oy, ', 'om', ' h', 'r', '']

print(re.split(r'[a-f]+', "Aey, Boy oh boy, come here"))
# ['A', 'y, Boy oh ', 'oy, ', 'om', ' h', 'r', '']


###############################################################################


# function re.sub(pattern,repl,string,count=0,flags=0)

print(re.sub('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE))
# S~*ject has ~*er booked already

# with out using flags= re.IGNORECASE
print(re.sub('ub', '~*', 'Subject has Uber booked already'))
# S~*ject has Uber booked already

# with flag re.IGNORECASE and count=1
print(re.sub('ub', '~*', 'Subject has Uber booked already', count=1, flags=re.IGNORECASE))
# S~*ject has Uber booked already


# \s is for start and end of the string
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE))
# Baked Beans & Spam


###############################################################################


# function re.subn(pattern, repl, string, count=0, flags=0)

# re.subn() is simliar to re.sub()
# but re.subn() returns tuple of length 2
# with count of total no of replacement

print(re.subn('ub', '~*', 'Subject has Uber booked already', flags=re.IGNORECASE))
# ('S~*ject has ~*er booked already', 2)


print(re.subn('ub', '~*', 'Subject has Uber booked already'))
# ('S~*ject has Uber booked already', 1)


############################################################################


# function re.escape(pattern)

# return string with all non-alphanumeric backslashed
# backslashed occurs before non-alphanumeric

# in this case ' ' is not alphanumeric
print(re.escape("This is awesome even 1 AM"))
# This\ is\ awesome\ even\ 1\ AM


# in this case  ' ' , '^' , '-' , '[]' , '\' are not alphanumeric
print(re.escape("I asked what is this [a-9], he said \t ^WoW"))
# I\ asked\ what\ is\ this\ \[a\-9\],\ he\ said\ \	\ \^WoW


###############################################################################

# re.search(pattern, string, flags=0)  #matching part of string

# this pattern either returns None (if pattern doesn't match)
#                 or a re.MatchObject that contains information about
#                                     matching part of the string


# this method stops after first match, so this is best suited for testing a regular
# expression more than extracting data


# match.group(0) returns the fully matched string
# match.object(1), match.object(2), ................. returns the captured
# group in order from left to right in the input string

# match.group() is equivalent to match.group(0)


regex = r"([a-zA-Z]+) (\d+) (\d+)"

match = re.search(regex, "I was born on August 10 1998")

if match != None:

    print("Match at index %s,%s" % (match.start(), match.end()))

    print("Full match: %s" % (match.group(0)))

    print("Month: %s" % (match.group(1)))

    print("Day: %s" % (match.group(2)))

    print("Year: %s" % (match.group(3)))

else:
    print("regex pattern does not match")

# Match at index 14,28
# Full match: August 10 1998
# Month: August
# Day: 10
# Year: 1998


###############################################################################

# re.match(pattern, string, flags=0)  #matching pattern to whole string


regex = r"([a-zA-Z]+) (\d+) (\d+)"

match = re.match(regex, "I was born on August 10 1998")

if match != None:

    print("Match at index %s,%s" % (match.start(), match.end()))

    print("Full match: %s" % (match.group(0)))

    print("Month: %s" % (match.group(1)))

    print("Day: %s" % (match.group(2)))

    print("Year: %s" % (match.group(3)))

else:
    print("regex pattern does not match")

# regex pattern does not match


regex = r"([a-zA-Z]+) (\d+) (\d+)"

match = re.match(regex, "August 10 1998")

if match != None:

    print("Match at index %s,%s" % (match.start(), match.end()))

    print("Full match: %s" % (match.group(0)))

    print("Month: %s" % (match.group(1)))

    print("Day: %s" % (match.group(2)))

    print("Year: %s" % (match.group(3)))

else:
    print("regex pattern does not match")

# Match at index 0,14
# Full match: August 10 1998
# Month: August
# Day: 10
# Year: 1998


################################################################################


# re.findall(pattern, string, flags=0) return all non-overlapping matches of pattern
#                                     in string, as  a list of strings
#                                     string is scanned left to right


string = "Hello my number is 123456789 and my friend's number is 987654321"

regex = "\d+"

print(re.findall(regex, string))

# ['123456789', '987654321']

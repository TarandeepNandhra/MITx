import re
#Practicing writing doctests

def count_vowels(s):
    '''Returns the number of vowels in string s.

    >>> s = 'azcbobobegghakl'
    >>> count_vowels(s)
    'Number of vowels: 5'
    '''
    s = list(s)
    vowels = "aeiou"
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return "Number of vowels: {0}".format(count)

def count_substring(p, s):
    '''Returns the number of times substring ("bob") appears in string with overlap.

    >>> s = 'azcbobobegghakl'
    >>> count_substring("bob", s)
    'Number of times bob occurs is: 2'
    '''
    count = 0
    while True:
        match = re.search(p, s) #returns true or false
        if match:
            s = s[match.start() + 1 : ]
            count += 1
        else:
            break
    return "Number of times {0} occurs is: {1}".format(p, count)

'''
Found other solution using regex but not sure what "(?=%s)" does
def count_overlapping(pattern, string):
    return len(re.findall("(?=%s)" % pattern, string))
print(count_overlapping("bob", s))
'''


def longest_ordered_substring(s):
    '''Returns the longest substring of s in which the letters occur in alphabetical order.

    >>> s = 'azcbobobegghakl'
    >>> longest_ordered_substring(s)
    'Longest substring in alphabetical order is: beggh'
    '''
    prev = "a"
    longest = ""
    tmp = ""

    for i in s:
        if ord(i) >= ord(prev):
            tmp += i
        elif len(tmp) > len(longest):
            longest = tmp
            tmp = i
        else:
            tmp = i

        prev = i

    #covers edge case where the longest substring ends at the end of the input string s.
    if len(tmp) > len(longest):
        longest = tmp

    return "Longest substring in alphabetical order is: {0}".format(longest)



if __name__ == "__main__":
    import doctest
    doctest.testmod()

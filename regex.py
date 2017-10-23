import re

terms = ['Ashish', 'Gargi', 'Swapna', 'Ingle']

text = 'Hello, How are you Ashish? how is Gargi and Swapna'

for term in terms:
    print('RegEx searcing in python')

    found = re.search(term, text)
    print(type(found))
    if(found):
        print('your search term found {}'.format(term))
    else:
        print('Sorry no search found in given text as "{}" for a word {}'.format(text, term))

def multi_re_find(patterns, pharase):
    """
    * = 0 or 1
    + = 1 or more
    {n1,n2} = number1 of char or number2 of char
    """
    for pat in patterns:
        print('Searching for pattern {}'.format(pat))
        print(re.findall(pat, pharase))
        print('\n')

test_pharase = "sdsd ddss ..ssddd sssss.. sdd.. ddsssss.. This is so nice! Wow Wow. my number is 98 87847 "
test_pattern = ['sd*', 'sd+', 'sd{2,3}', '[A-Z]', '[a-z]', '[0-9]', '[!@#,.]']

multi_re_find(test_pattern, test_pharase)

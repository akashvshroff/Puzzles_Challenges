def count_deaf_rats(town):
    '''
    See also: https://www.codewars.com/kata/598106cb34e205e074000031/python
    '''
    return town.replace(' ', '')[::2].count('O')


#print(count_deaf_rats("~O~O~O~O P ~O~O~O~O"))

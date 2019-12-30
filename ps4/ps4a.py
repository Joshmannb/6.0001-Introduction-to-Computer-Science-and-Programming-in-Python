# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:      # base case: when sequence is singleton, return sequence
        return sequence
    else:       # recursive step: in each step, each element can be extended inserting new letter in every position
        '''
        recursive step: in each step, each element can be extended inserting new letter in every position
        example: with element like 'ab', and a new letter 'c', the extended elements are 'cab', 'acb' and 'abc'. 'c' is inserted in the first, the second and the third place of 'ab'.
        '''
        new_sequence = []
        for i in get_permutations(sequence[:-1]):       # the permutations of sequence without the last element
            for j in range(len(i)+1):       # every element in permutations
                new_sequence.append(i[:j] + sequence[-1] + i[j:])       # is extended with last element in sequence

        return new_sequence
        


# if __name__ == '__main__':
#     if set(['ab', 'ba']) == set(get_permutations('ab')):
#         print('-'*20)
#         print('SUCCESS: Permutation of "ab"')
#     else:
#         print('FAILURE: get_permutations() is wrong with input "ab"')

#     if set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']) == set(get_permutations('abc')):
#         print('-'*20)
#         print('SUCCESS: Permutation of "abc"')
#     else:
#         print('FAILURE: get_permutations() is wrong with input "abc"')
    

#     if set(['dabc', 'adbc', 'abdc', 'abcd', 'dacb', 'adcb', 'acdb', 'acbd', 'dbac', 'bdac', 'badc', 'bacd', 'dbca', 'bdca', 'bcda', 'bcad', \
#         'dcab', 'cdab', 'cadb', 'cabd', 'dcba', 'cdba', 'cbda', 'cbad']) == set(get_permutations('abcd')):
#         print('-'*20)
#         print('SUCCESS: Permutation of "abcd"')
#     else:
#         print('FAILURE: get_permutations() is wrong with input "abcd"')
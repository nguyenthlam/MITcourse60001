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

    result = []
    
    length = len(sequence)
    
    if length == 1:
        result = [sequence]
        
    else:
        # separate the sequence into the first element called a:
        a = sequence[0]
        
        # and a shorter sequence:
        subs = sequence[1:length]
        
        # generate permutations from that of the shorter sequence.
        # s is a sequence in the list of permutations if the shorter sequence:
        for s in get_permutations(subs):
            
            # the first permutation:
            result += [a + s]
            
            length_s = len(s)
            
            # getting next permutations by inserting a into different locations
            # of sequence s:
            for n in range(length_s):
                
                new_s = s[0:n+1] + a
                
                if n+1 < length_s:
                    new_s += s[n+1:length_s]
                
                result += [new_s]
                
    return result
                
    
if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    sequence = 'abcd'
    print(get_permutations(sequence))


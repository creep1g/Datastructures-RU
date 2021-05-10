import random
# Small program to understand timecomplexity of ceirtan operations
# e.g. O(n) O(n^2) O(log n) etc.


def power(value, exp):
    '''Time complexity: O(n)'''
    if value == 0 and exp == 0:  # O(1)
        raise Exeption("0 babjajba")
    ret_value = 1 
    for i in range(exp):
        ret_value *= value
    return ret_value
# sum together #o(1) and O(n) O(2n) == O(n)
# Can i make this better time complexity


def mul(numA, numB):
    '''Time complexity: O(n)'''
    base = 0
    for i in range(numB):
        base += numA
    return base


def rand_num_insert(size):
    '''Time complexity: O(n)/O(2n)'''
    lis = [0] * size  # O(n)
    for i in range(len(lis)):  # O(n)
        lis[i] = random.randint(1, 6)
    return lis


def print_list(lis):
    '''pretty print list'''
    '''Time Complexity: O(n)'''
    count = 0
    for i in lis:
        if count+1 == len(lis):
            print(i)
        else:
            print(i, end=", ")
        count += 1


def inc_num_at_rand(lis):
    '''Generates a random number between 0 and length of list increase number
    at that index by 1'''
    '''Time Complexity: O(1)'''
    rand_max = len(lis)-1
    randint = random.randint(0, rand_max)
    lis[randint] += 1


def switch_items(lis, index, index_two=None):
    '''Takes a list and an index and swaps the value of that index with the
    value of index-1 if index_two is set swap with that index instead'''
    '''expect O(n)'''
    if index_two == None:
        lndex_two = index - 1
    lis[index], lis[index_two] = lis[index_two], lis[index]


def ordered_insert(lis, value):
    '''Insert a random number at into a list so the list is ordered'''
    '''Timecomplexity: O(n)'''
    
    if value not in lis:
        lis.append(value)  
    else:
        return

    i = len(lis) - 1
    while True:  # O(n)
        if i == 0:
            break
        if lis[i] > lis[i-1]:
            break
        temp = lis[i]  # O(1)
        lis[i] = lis[i-1]  # O(1)
        lis[i-1] = temp  # O(1)
        i -= 1


def gen_zero_list(size):
    return [0] * size


if __name__ == '__main__':

    #lis = gen_zero_list(10)
    # lis2 = rand_num_insert(32)
    # print_list(lis2)
    # lis3 = gen_non_zero_list(10)
    lis = [1,2,3,4,5,6,7,8,0]
    switch_items(lis, 3)
    print_list(lis)
    # count = 0
    # while count < 20:
    #     randint = random.randint(1, 10)
    #     ordered_insert(lis, randint)
    #     print(lis)
    #     count += 1
    #     if len(lis) == 10:
    #         break

    # count = 0
    # while len(lis) > count:
    #     inc_num_at_rand(lis)
    #     print_list(lis)
    #     count += 1

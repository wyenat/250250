import time


def get_list(n,k):
    """ 
    Determining with :
    Knowing that :  https://fr.wikipedia.org/wiki/Exponentiation_modulaire
    """
    # Find cycle
    to_ret = [1]
    i = 2
    while i <= n:
        len_list = 0
        # get result
        result = exp_mod(i, k)
        # append result 
        to_ret.append(result)
        # sublists
        check = check_sub(to_ret, len_list)
        while check is not None:
            if check+len_list==len(to_ret)-len_list:
                print(f"Found a cycle of {len_list} : {to_ret[:-1-len_list]}")
                return to_ret[:-1-len_list], len_list-1
            len_list += 1
            check = check_sub(to_ret, len_list)
            # print(f"i={i},l={len_list},check={check}, Check if {to_ret[-1-len_list:]} in {to_ret[:-1-len_list]}")
        i += 1
    return to_ret,None

def check_sub(to_ret, len_list):
    indices = [i for i, x in enumerate(to_ret[:-1]) if x == to_ret[-1]]
    for j in range(1,len_list+1):
        indices = [i-1 for i in indices if i>0]
        indices = [i for i in indices if to_ret[-1-j]==to_ret[i]]
    if indices:
        return max(indices)
    return None

def exp_mod(i,k):
    result = 1
    exp = i
    while exp > 0:
        if exp & 1:
            result = (result * i) % k
        exp >>= 1
        i = (i * i) % k
    return result

def get_subs(to_sub, n, ):
    subs = []
    nb_subs = 2**n 
    for i in range(nb_subs):
        sub = []
        save = i
        for j in reversed(range(n)):
            if save - 2**j >= 0:
                save -= 2**j
                sub.append(to_sub[j])
        subs.append(sub)
    return subs

def main():
    # get input
    # n,k = [int(i) for i in input().split(" ")[:2]]
    # list
    k = 3
    n = 100
    to_calc,cycle = get_list(n,k)
    number_repetion = 0
    print(f"to_c = {to_calc}, cycle = {cycle}")
    # sublists
    cycle_list = []
    if cycle:
        cycle_list = to_calc[len(to_calc)-cycle:]
        to_calc = to_calc[0:len(to_calc)-cycle]
        number_repetion = [n - len(to_calc) //]
    
    cycle_subs = get_subs(cycle_list, len(cycle_list))
    single_subs = get_subs(to_calc, len(to_calc))

    print(f"We have cyclelist = {cycle_list}")
    print(f"We have tocalc = {to_calc}")

    # sums 
    sums_no_cycle = [sum(i) for i in single_subs] if single_subs!=[] else [0]   
    sums_cycle = [sum(i) for i in cycle_subs]
    total = 0
    for no_c in sums_no_cycle:
        total += len([i for i in sums_cycle if (i+no_c)%k==0])
    print(total)

main()
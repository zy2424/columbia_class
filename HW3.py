def question_1(name):
    return ("Hello my name is " + name)

def question_2(name):
    cap_name = name.capitalize()
    return ("Hello my name is " + cap_name)

def question_3(name):
    first_name = name.split( )[0]
    return ("My first name is " + first_name)

def question_4(name):
    first_name = name.split( )[0]
    cap_name = first_name.capitalize()
    return ("My first name is " + cap_name)

def question_5(first_name, last_name):
    return ("My full name is " + first_name + " " + last_name)

def question_6(first_name, last_name):
    cap_first_name = first_name.capitalize()
    cap_last_name = last_name.capitalize()
    return ("My full name is " + cap_first_name + " " + cap_last_name)

def question_7(str):
    lowercase_letters = [c for c in str if c.islower()]
    return lowercase_letters

def question_8(str):
    uppercase_letters = [c for c in str if c.isupper()]
    return uppercase_letters

def question_9(str):
    space = [c for c in str if c == " "]
    return space

def question_10(str):
    wordlist = []
    for c in str:
        if c not in wordlist:
            wordlist.append(c)
    count = len(wordlist)
    return count

def question_11(str):
    s = ''.join(x for x in str if x.isdigit())
    return int(s)

def question_12(str1,str2):
    return (str1 + str2)

def question_13(str1,str2):
    return (str1.capitalize() + str2.capitalize())

def question_14(str):
    replaced = ""
    for c in str:
        if c == " ":
            replaced += "_"
        else:
            replaced += c
    return replaced

def question_15(str):
    wordlist = str.split()
    longest = ""
    for c in wordlist:
        if len(c) > len(longest):
            longest = c
    return longest

def question_16(str):
    wordlist = str.split()
    shortest = "11111"
    for c in wordlist:
        if len(c) < len(shortest):
            shortest = c
    return shortest

def question_17(str):
    wordlist = str.split()
    length = 0
    for c in wordlist:
        length += len(c)
    mean = length/len(wordlist)
    return mean

def question_18(str):
    wordlist = str.split()
    wordlist.sort(key = len)
    if len(wordlist)%2 == 0:
        mid = int((len(wordlist[len(wordlist)//2]) + len(wordlist[(len(wordlist)//2)-1]))/2)
    else:
        mid = len(wordlist[(len(wordlist)//2)-1])
    return mid

def question_19(list):
    even = []
    for i in list:
        if i % 2 == 0:
            even.append(i)
    return even

def question_20(list):
    odd = []
    for i in list:
        if i % 2 == 1:
            odd.append(i)
    return odd

def question_21(list):
    list.sort()
    return [list[-1] , list [-2] , list[-3]]

def question_22(list):
    list.sort()
    return [list[0] , list [1] , list[2]]

def question_23(list):
    return sum(list)/len(list)

def question_24(list):
    d = {}
    for i in list:
       if i not in d:
            d[i] = 1
       else:
            d[i] += 1
    mode = [1]
    for value in d:
        if d[value] > d[mode[0]]:
            mode = [value]
        elif d[value] == d[mode[0]]:
            mode.append(value)
    return mode

def question_25(list):
    list_rev = list[::-1]
    return list_rev

def question_26(list):
    return sum(list)

def question_27(list):
    diff = []
    for i in range(0, len(list)-1):
        sub = list[i]-list[i+1]
        diff.append(sub)
    return diff

def question_28(n):
    F = [0,1,1]
    for i in range(3, n):
        add = F[i-1] + F[i-3]
        F.append(add)
    return F

def question_29(n):
    F = [1,2]
    for i in range(2, n):
        add = 1
        for c in F:
            add *= c
        F.append(add)
    return F

def question_30(n):
    F = []
    for i in range (0,n):
        powerlist = []
        for x in range (1,i+1):
            powerlist.append(x)
        power = sum(powerlist)
        twotothepower = 2**power
        F.append(twotothepower)
    return F















































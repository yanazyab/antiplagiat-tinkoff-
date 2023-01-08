import ast

def astt(code):
    tre = ast.parse(code)
    tree = ast.dump(tre)
    return tree

def levenstein(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]

file = open('input.txt','r')
string = ""
ff = open('scores.txt','w')
for line in file:
    print(line)
    l1, l2 = line.split()
    f1 = open(l1,'r').read()
    f2 = open(l2,'r').read()
    tree1 = astt(f1)
    tree2 = astt(f2)
    string = string + str(1-levenstein(tree1,tree2)/max(len(tree1),len(tree2))) + "\n"

ff.write(string)



#2017/10/05 YCPan-tw


dpval = dict()

def dpf(m,n):
    '''to slove the searching problem by dp method'''

     #boundry condition,and its principle can be discovered in recur.

    if (m, n) in dpval.keys():
        return dpval[(m, n)]

    if m == 1:
        dpval[(m, n)] = n
        return n

    if m >= n:
        dpval[(m, n)] = (2 ** n) - 1
        return (2 ** n) - 1

    #to find the tree,by top down method

    temp_val = 0

    for i in range(n, 0, -1):
        '''range(start,stop,step)'''

        if (m-1, i-1) in dpval.keys():
            return dpval[(m-1, i-1)]

        else:

            temp_val = dpf(m-1, i-1) + 1 + dpf(m, i-1)
            dpval[(m - 1, i - 1)] = temp_val

            return temp_val



def count_out(m, f):


    count = 0

    while 1:
        if dpf(m, count) < f:
            count +=1
            dpval.clear()
            '''very important to set dict. to default'''
        else:
            return count

def path(m,n):

    temp_val_floor=0
    temp_list=list()

    if m == 1:
        for i in range(1,n+1):
            temp_list.append(i)
        return temp_list


    else:
        for i in range(n,0,-1):
            dpval.clear()
            '''very important to clear dpval'''
            temp_val_floor += dpf(m - 1, i - 1) + 1
            temp_list.append(temp_val_floor)
        return temp_list


fp = open('input', 'rt')

data_input = list()

for w in fp:
    data_input.append(w.split())



for w2 in data_input:

    mobile = int(w2[0])
    floor = int(w2[1])

    worst_case = count_out(mobile, floor)
    redcord_path = path(mobile, worst_case)
    
    fp_2 = open('output_test', 'at')

    fp_2.write(str(worst_case)+'\n')


    if mobile == 1:
        for w3 in redcord_path:
            fp_2.write(str(w3)+' ')
    else:
        for w4 in range(0, worst_case):
            fp_2.write(str(redcord_path[w4])+' ')
    fp_2.write('\n')


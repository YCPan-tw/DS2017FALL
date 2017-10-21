
import csv
f = open('Input.txt','rt',newline='')
row = csv.reader(f, delimiter=",")

data = list()

for line in row:
    data.append(line)



'''
class largestrectangle:


    def __init__(self,stack3):

        self.stack_h = list()
        self.stack_p = list()
        self.stack_data = stack3
        self.maxrect = 0

    def trans(self):
        for i in range(len(self.stack_data)):
            self.stack_data[i] = int(self.stack_data[i])

    def show(self):
        print(self.stack_data)


def solve(self):
        
        to solve the largest reectangle problem
        :return:
        
        self.stack_data.append(0)
        for i in range(len(self.stack_data)):
            if self.stack_h == [] or self.stack_data[i] < self.stack_h[]
            '''

def largestrectangle(stack_data):
    for i in range(len(stack_data)):
        stack_data[i] = int(stack_data[i])

    stack_data.append(0)
    stack = list()
    maxarea = 0

    for i in range(len(stack_data)):
        if stack == [] or stack_data[i] > stack_data[stack[-1]]:
            stack.append(i)
        else:
            while stack != [] and stack_data[i] < stack_data[stack[-1]]:
                top = stack.pop()

                if stack == []:
                    j_1 = 0
                else:
                    j_1 = stack[-1] + 1

                j_2 = i - 1
                area = stack_data[top]*(j_2 - j_1 + 1)

                if area > maxarea:
                    maxarea = area


            stack.append(i)
    return maxarea


def answer_print(write_list,path='Output.txt'):

    fp = open(path,'w')
    for i in write_list:
        if i == write_list[len(write_list)-1]:
            fp.write(str(i))
        else:
            fp.write(str(i)+'\n')
    fp.close()


answer_list = list()

for i in range(len(data)):
    answer_list.append(largestrectangle(data[i]))
answer_print(answer_list)

import csv
import copy

#read the file,amd default name is "Input"




def readf():
    f = open('Input','rt',newline='')
    row = csv.reader(f, delimiter=",")
    dataf = list()
    
    for line in row:
        if len(line) != 0:
            dataf.append(line)
    return dataf


def calculate(data):
    max_value_temp = 0
    min_value_temp = data[len(data)-1]
    max_value = 0
    min_value = data[len(data)-1]
    max_loc = 0
    min_loc = 0
    max_loc_temp = 0
    min_loc_temp = 0

    diff = 0
    diff_max = 0
   
    for i in range(len(data)-1,-1,-1):
        data[i] = int(data[i])
        
        if data[i] >= max_value:                  
            max_value_temp = data[i]
            max_loc_temp = i
            
            

        if data[i] <= int(min_value_temp):                    
            min_value_temp = data[i]
            min_loc_temp = i
            
            

        if min_loc_temp <= max_loc_temp:
            diff = data[max_loc_temp] - data[min_loc_temp]
        
        
        #difference 要一直計算
        if diff_max <= diff :    
            diff_max = copy.deepcopy(diff)
        
            max_value = copy.deepcopy(max_value_temp)
            min_value = copy.deepcopy(min_value_temp)

            min_value_temp =copy.deepcopy(max_value)
            
            max_loc = copy.deepcopy(max_loc_temp)
            min_loc = copy.deepcopy(min_loc_temp)
            diff = 0

    max_list = [min_loc,max_loc,diff_max]    
    return max_list 

  



def write_answer(answer,path='Output '):
    fp = open(path,'w')
    for wd in answer:
        for i in range(len(wd)):
            fp.write(str(wd[i]))
            if i != len(wd)-1:
                fp.write(',')
        fp.write('\n')
    fp.close()



    

if __name__ =="__main__":
    data = readf()
    answer_list=list()

    for i in range(len(data)):
        calculate(data[i])
        answer_list.append(calculate(data[i]))
    write_answer(answer_list)

    

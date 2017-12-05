import csv






#to load data in
def readdata():
    temp = open('input','r')
    read_data = csv.reader(temp)
    input_data = []
    for w in read_data :
        input_data.append(w)
    return input_data








def trans(input_d):
     data = input_d
     
     dp_record=[1,1]

     if data =="" or data[0]=='0': 
        '''
        prevent from error
        '''
        return 0

     


     for i in range(2,len(data)+1):
        '''
        use if elif to judge
        '''

        if 10 < int(data[i-2:i]) <= 26 and data[i-1]!='0':
            dp_record.append(dp_record[i-1]+dp_record[i-2])


        elif int(data[i-2:i]) == 10 or int(data[i-2:i])==20:
            dp_record.append(dp_record[i-2])


        elif data[i-1]!='0':
            dp_record.append(dp_record[i-1])

        else:
            return 0


     return dp_record[len(data)]





def answer_write(input_data,path='Output'):

    answer_list = list()

    for i in range(len(input_data)):
        answer_list.append(trans(input_data[i][0]))


    fp = open(path,'w')
    for i in answer_list:
        fp.write(str(i))
        fp.write('\n')
    fp.close()



if __name__ == '__main__':
   
    answer_write(readdata())












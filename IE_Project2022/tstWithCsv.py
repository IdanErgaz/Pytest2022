import csv, time
with open ('/Users/user/testim/envVars.csv') as csvfile:
    reader=csv.reader(csvfile,delimiter=',') #define the reader
    line=0

    for rowlist in reader:
        if line ==0:
            line+=1;
            pass

        else:
            i=0
            while i<len(rowlist):
                print(rowlist[i])

                i+=1;

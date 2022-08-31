import datetime
import time, csv, subprocess

count=0
destination=0
csvFile= 'envVars.csv'
resFile= 'pingRes.txt'
logFile = 'myLog.txt'
###############################
#function that will write text to log file
def write2Log(logFile,text2Write):
    f=open(logFile,'a')
    timeStamp=str(datetime.datetime.now())
    f.write(timeStamp + " "+ text2Write + "\n")
    f.close()
################################################
#Function will read details from csv

def readFromCsv(csvFile):
    write2Log(logFile, 'reading csv file '+ csvFile)
    with open(csvFile) as csvfile:
        reader=csv.reader(csvfile,delimiter=',')
        line=0
        for row in reader:
            if line==0:
                line+=1
                pass
            else:
                count,destination= (int(row[0]), row[1])
                return count, destination
    write2Log(logFile, 'finish reading csv file '+ csvFile)

#function to send ping and write results
def sendPingTo(destination, count, runNumber):
    write2Log(logFile, 'starting ping function to: '+destination)
    subprocess.run('ping -n '+str(count)+ ' '+destination + '>'+ str(runNumber)+ resFile,shell=True)
    write2Log(logFile, 'finish ping function to: '+ destination)
    return str(runNumber)+ resFile

#function to check if ping was successful
def checkPingRes(resFile):
    write2Log(logFile, 'checking ping test result to destination: '+destination)
    f=open(resFile, 'r')
    pingRsults= f.read()
    if 'Reply from 127.0.0.1: bytes=32 time<1ms TTL=128' in pingRsults:
        print('ping test PASS!!!')
        write2Log(logFile, 'ping test to destination '+ destination +' PASS!!!')
    else:
        write2Log(logFile, 'ping test to destination: '+ destination+ ' FAIL')
        print('ping test to destination: '+ destination+ ' FAIL')
    f.close()

#Main
run_number=0
loop_times=2
while run_number<loop_times:
    print('starting with ping test')
    vars=readFromCsv(csvFile)
    count=vars[0]
    destination=vars[1]
    print('count is: {}'.format(count))
    print('destination is: '.format(destination))
    pingResultsFile=sendPingTo(destination, count, run_number)
    print('dene with ping test')
    time.sleep(3)
    run_number+=1
    checkPingRes(pingResultsFile)
print('program ended- log file is located under: '+logFile)
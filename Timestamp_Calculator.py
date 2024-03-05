import csv #needed to read csv file
import os
import os.path

#initialize variables needed
date = []
time = []
clock = []

hour = []
minute = []
second = []

keepGoing = True
while(keepGoing):

    totalHours = 0
    totalMinutes = 0
    totalSeconds = 0

    filePath = input('Enter the full file path. File must be .csv: ')
    # 'C:\\Users\King435\Downloads\Timestamp.csv'
    if(os.path.isfile(filePath) == False):
        while(os.path.isfile(filePath) == False):
            print('That is not a functioning file path.')
            filePath = input('Enter the full file path. File must be .csv: ')
        
    employeeName = input('Enter the name of the employee: ')
    #open csv file
    with open(filePath, newline='') as csvfile:
        heading = next(csvfile) #skip heading
        filereader = csv.reader(csvfile)
        for col in filereader:
            #add data into variables
            date.append(col[0])
            time.append(col[1])
            clock.append(col[2])
        #sort time
        for x in time:
            hour.append(float(x[:2]))
            minute.append(float(x[3:5]))
            second.append(float(x[6:]))
        #calculate time with the clocks
        row = range(len(clock))
        for i in row:
            hour[i] += (minute[i]/60) + (second[i]/3600)
        for x in row:
            if x % 2 == 1:
                totalHours += (hour[x] - hour[x-1])
        timeRemainder = totalHours % 1
        totalSeconds = timeRemainder *3600
        while totalSeconds >= 60:
            totalSeconds -= 60
            totalMinutes += 1
        totalHours = int(totalHours)
        totalMinutes = int(totalMinutes)
        totalSeconds = int(totalSeconds)
        print('The amount of hours' , employeeName , 'has worked is' , totalHours)
        print('The amount of minutes', employeeName,  'has worked is' ,totalMinutes)
        print('The amount of seconds', employeeName, 'has worked is' ,totalSeconds)
    if(input('Do you want to do another one? Enter n to quit: ') == 'n'):
        keepGoing = False
    else:
        date.clear()
        time.clear()
        clock.clear()
        hour.clear()
        minute.clear()
        second.clear()
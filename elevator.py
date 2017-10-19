iimport time
ret = True
def outsidecalldownlist(variable,variable2):
    variable2.sort()
    x=0
    for items in variable2:
        x+=1
        print('Being called by ' + str(items))
        time.sleep(1)
        if x >= 2:
            for floors in range(variable + 1, items + 1):
                print('Reached floor: ' + str(floors))
                time.sleep(1)
                if floors == items:
                    print('Doors opening.')
                    time.sleep(1)
                    print("Picking people up at: " + str(items))
                    time.sleep(1)
                    print('Doors Closing')
                    # this is where function goes
                    time.sleep(1)
                    variable = items
        else:
            for floors in range(variable - 1, items - 1, -1):
                print('Reached floor: ' + str(floors))
                time.sleep(1)
                if floors == items:
                    print('Doors opening.')
                    time.sleep(1)
                    print("Picking people up at: " + str(items))
                    time.sleep(1)
                    print('Doors Closing')
                    time.sleep(1)
                    variable = items
def outsidecalldownint(variable, variable2):
    print('Being called by ' + str(variable2))
    time.sleep(1)
    for floors in range(variable-1,variable2-1,-1):
        print('Reached floor: ' + str(floors))
        time.sleep(1)
        if floors == variable2:
            print('Doors opening.')
            time.sleep(1)
            print("Picking people up at: " + str(floors))
            time.sleep(1)
            print('Doors Closing')
            time.sleep(1)
def outsidecalluplist(variable,variable2):
    variable2.sort(reverse=True)
    x = 0
    for items in variable2:
        x = x + 1
        print('Being called by ' + str(items))
        time.sleep(1)
        if x >= 2:
            for floors in range(variable - 1, items - 1,-1):
                print('Reached floor: ' + str(floors))
                time.sleep(1)
                if floors == items:
                    print('Doors opening.')
                    time.sleep(1)
                    print("Picking people up at: " + str(items))
                    time.sleep(1)
                    print('Doors Closing')
                    time.sleep(1)
                    variable = items
        else:
            for floors in range(variable + 1, items + 1):
                print('Reached floor: ' + str(floors))
                time.sleep(1)
                if floors == items:
                    print('Doors opening.')
                    time.sleep(1)
                    print("Picking people up at: " + str(items))
                    time.sleep(1)
                    print('Doors Closing')
                    time.sleep(1)
                    variable = items
def outsidecallupint(variable, variable2):
    print('Being called by ' + str(variable2))
    time.sleep(1)
    for floors in range(variable+1,variable2+1):
        print('Reached floor: ' + str(floors))
        time.sleep(1)
        if floors == variable2:
            print('Doors opening.')
            time.sleep(1)
            print("Picking people up at: " + str(floors))
            time.sleep(1)
            print('Doors Closing')
            time.sleep(1)


while(True):
    while ret == True:
        variable = int(input('What is the position of the elevator:'))
        variable2 = (input('What floor is the elevator being called by:'))
        
        if ',' in variable2:
            variable2 = list(eval(variable2))
        
        else:
            variable2 = eval(variable2)
        
        if type(variable2) == list:
            if variable < max(variable2):
                outsidecalluplist(variable,variable2)
                variable = max(variable2)
            elif variable > min(variable2):
                outsidecalldownlist(variable, variable2)
                variable = min(variable2)
        else:
            if variable < variable2:
                outsidecallupint(variable,variable2)
            elif variable > variable2:
                outsidecalldownint(variable,variable2)
            variable = variable2
        
        ret = False
        break

    while ret == False:
        variable4 = (input('What floor(s) did the people want to travel to: '))
        
        if ',' in variable4:
            variable4 = list(eval(variable4))
        else:
            variable4 = eval(variable4)
        
        ret = True
        break

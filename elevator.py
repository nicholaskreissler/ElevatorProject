import time
ret = False
def insidecalluplist(variable2):
    variable3 = input("What floors do the people want to travel too: ")
    if ',' in variable3:
        variable3 = list(eval(variable3))
        for integers in variable3:
            if integers not in variable2:
                variable2 += [integers]
    else:
        variable3 = eval(variable4)
        if variable3 not in variable2:
            variable2 += [variable3]
def outsidecalldownlist(variable,variable2):
    variable2.sort()
    variable4 = len(variable2)
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
                    if variable4 >= len(variable2) - variable4:
                        print("Picking people up at: " + str(items))
                    else:
                        print("People Exiting")
                    time.sleep(1)
                    print('Doors Closing')
                    if variable4 >= len(variable2) - variable4:
                        insidecalluplist(variable2)
                    time.sleep(1)
                    variable = items
        else:
            for floors in range(variable - 1, items - 1, -1):
                print('Reached floor: ' + str(floors))
                time.sleep(1)
                if floors == items:
                    print('Doors opening.')
                    time.sleep(1)
                    if variable4 >= len(variable2) - variable4:
                        print("Picking people up at: " + str(items))
                    else:
                        print("People Eciting")
                    time.sleep(1)
                    print('Doors Closing')
                    if variable4 >= len(variable2) - variable4:
                        insidecalluplist(variable2)
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
            if variable > min(variable2) and variable < max(variable2):
                print('it works')
            elif variable < max(variable2):
                outsidecalluplist(variable, variable2)
                variable = max(variable2)
            elif variable > min(variable2):
                outsidecalldownlist(variable, variable2)
                variable = min(variable2)

        else:
            variable2 = eval(variable2)
            if variable < variable2:
                outsidecallupint(variable, variable2)
            elif variable > variable2:
                outsidecalldownint(variable, variable2)
            variable = variable2



        
    while ret == False:
        variable = int(input('What is the position of the elevator:'))


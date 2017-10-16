import time  # Slows down the speed of the loops
def elevatorgoingup(start, end, number):  # Definition called when the elevator is on its way up 'start:beginning floor, end:ending floor, number:number of people on the elevator'
    if number > maxcapacity:  # Indicates that the elevator doors should stay closed until they reach their destination
        print('Elevator Doors will remain closed, elevator is fully occupied')
        print('Going up to floor ' + str(end))
        for index in range(start+1,end):  # Loops through the floors from the start to end. (Ascending elevator)
            time.sleep(1)
            print('Reached floor ' + str(index))
        time.sleep(1)
        print('Stopping at floor  ' + str(end))
        print('Doors opening')
        time.sleep(1)
    else:  # Indicates that the elevator isnt full and it can make stops on its ascension.
        print('Elevator can make other stops')
        time.sleep(1)
        print('Going up to floor ' + str(end))
        for index in range(start + 1, end):  # Loops through the floors from start to end
            time.sleep(1)
            print('Reached floor ' + str(index))
        time.sleep(1)
        print('Stopping at floor  ' + str(end))
        print('Doors opening')
        time.sleep(1)
def elevatorgoingdown(start, end, number): #  Definition called when the elevator is on its way down 'start:ending floor, end:beginning floor, number: number of people on the elevator'
    if number > maxcapacity:  # Indicates that the elevator is full and cant make stops on its descension
        print('Elevator Doors will remained closed, elevator is fully occupied')
        print('Going down to floor ' + str(start))
        x=0
        for index in range(start+1,end):  # Loops through the elevator backwards
            x = x+1
            variable = end - x
            time.sleep(1)
            print('Reached floor ' + str(variable))
        time.sleep(1)
        print('Stopping at Floor ' + str(start))
        print('Doors opening')
        time.sleep(1)
    else:  # Indicates that the elevator isnt full and can make stops on its descension=
        print('Elevator can make other stops')
        print('Going down to floor ' + str(start))
        x = 0
        for index in range(start + 1, end): # Loops through the elevator backwards
            x = x + 1
            variable = end - x
            time.sleep(1)
            print('Reached floor ' + str(variable))
        time.sleep(1)
        print('Stopping at Floor ' + str(start))
        print('Doors opening')
        time.sleep(1)

lengthofelevator = input('Length of elevator: ')
widthofelevator = input('Width of elevator: ')
areaofelevator = int(lengthofelevator)*int(widthofelevator)  # Calculates the area by multiplying the height by the width
print("The area of the elevator is: " + str(areaofelevator) + 'in2')
statisticallyaveragedlengthofperson = input('Statistical average length of a person: ')
statisticallyaveragedwidthofperson = input('Stistical average width of a person: ')
areaofperson = int(statisticallyaveragedlengthofperson)*int(statisticallyaveragedwidthofperson)  # Calculates the area of a person buy multiplying width by height
print("The average area of a person is: " + str(areaofperson) + ' in2')
maxcapacity = areaofelevator/areaofperson  # Calculates the maxcapacity by dividing the two areas
print('The maxcapacity of the elevator is ' + str(maxcapacity) + 'people' )
numberofpeopleontheelevator = int(input('How many people enter the elevator: '))  # Asks for an initial number of people in the elevator and sets it to a variable
elevatorposition = eval(input("Position of the elevator: "))  # Indicates the position of the elevator and sets it to a variable
end = input("Type the floor you would like the elevator to travel too: ") # Indicates the floor the elevator needs to travel too and sets it to a variable

if len(end) > 2:
    end = eval(end)
    end = list(end)
else:
    end = eval(end)

while(True):  # Final stages of the program, puts the elevator in a loop allowing it to go up and down and count the nunber of people in the elevator at every stop
    if type(end) == list and numberofpeopleontheelevator > maxcapacity:
        if max(end) > elevatorposition:
            end.sort()
            end = max(end)
            elevatorgoingup(elevatorposition, end, numberofpeopleontheelevator)
        else:
            end.sort(reverse = True)
            end = min(end)
            elevatorgoingdown(end, elevatorposition, numberofpeopleontheelevator)
        elevatorposition = end
    elif type(end) == list:
        if end[0] > elevatorposition :
            end.sort()# Indicates that the elevator is going up
            for items in end:
                elevatorgoingup(elevatorposition,items,numberofpeopleontheelevator)
                if len(end) > 1:
                    elevatorposition = items# See line 16, Also is there a function that allows you to click on the 'See line 16'?
            elevatorposition = int(items)
        else:
            end.sort(reverse = True)
            for items in end:
                # Indicates that the elevator is going down
                elevatorgoingdown(items, elevatorposition, numberofpeopleontheelevator)  # See line 39
                if len(end) > 1:
                    elevatorposition = items
            elevatorposition = int(items)
    else:
        if end > elevatorposition:
            elevatorgoingup(elevatorposition,end,numberofpeopleontheelevator)
                # See line 2, Also is there a function that allows you to click on the 'See line 16'?
            elevatorposition = end
        else:
            elevatorgoingdown(end,elevatorposition, numberofpeopleontheelevator)  # See line 39
            elevatorposition = end
    end = input("Type the floor you would like the elevator to travel too: ")
    if len(end) > 2:
        end = eval(end)
        end = list(end)
    else:
        end = eval(end)
    #Out of the original if, else statement
    numberofpeopleontheelevator = numberofpeopleontheelevator + int(input('How many people have entered the elevator: '))  # Adds the new amount of people that enter to the old amount. Use a negative number if people leave

#Testing this file

#Test
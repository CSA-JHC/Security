from datetime import datetime
import time
import random
import os

def securitydoor():        
    try:
        #ask what the pin number is
        #determine whether the pin is a number
        askpin=input('What is the pin number? ')
        while not askpin.isdigit():
            print('You entered the pin incorrectly')
            askpin=input('What is the pin number?')

        #open codes file and see if pin is in there
        with open('codes.txt') as f:
            lines=f.read().splitlines()
            if askpin in lines:
                x=str(datetime.now())
                print('Opened Successfully')
                #if successful write to a file the time and code used
                file=open('securitydoor.txt','a')
                file.write(x+' - '+str(askpin)+'\n')
                file.close()
                time.sleep(1) #sleep
                os.system('open.py')
            else:
                #if incorrect tell them and start over
                print('Incorrect Pin')
                
    except KeyboardInterrupt:
        #if something goes wrong start over
        print('Something went wrong, please try again')
        securitydoor()

    securitydoor()
securitydoor()

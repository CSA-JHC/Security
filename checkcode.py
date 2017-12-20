# This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
                os.system('open.py') #open program, open.py
            else:
                #if incorrect tell them and start over
                print('Incorrect Pin')
                
    except KeyboardInterrupt:
        #if something goes wrong start over
        print('Something went wrong, please try again')
        securitydoor()

    securitydoor()
securitydoor()

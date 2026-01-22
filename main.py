import time
import winsound
import sys
from datetime import datetime

def timer_start(workTime=25, breakTime=5, top_of_30=False):
    time_intervals = [workTime * 60, breakTime * 60] # Default is 25 minutes of work and 5 minutes of break time
    intervalType = 0 # Whether the current session is for working or taking a break
    workSessionCount = 0
    
    if top_of_30:
        curr_time = datetime.now().time()
        if curr_time[1] != 30 and curr_time[1] != 0:
            time.sleep(abs(30 - curr_time[1]))
    
    print("The timer has begun! Use Ctrl-C to stop the timer.")
    winsound.Beep(1000, 1000) 
    
    try:
        while True:
            if intervalType == 0: # If current session is work, increment workSessionCount    
                workSessionCount += 1 
            time.sleep(time_intervals[intervalType]) 
            if intervalType == 0:
                print(f"Work session {workSessionCount} complete! Take a {breakTime} minute break.")
            else: 
                print(f"Break time over! Time for another {workTime} minutes of work.")
            intervalType = 1 - intervalType # Switch from study to break mode and vice versa
            winsound.Beep(1000, 1000) 

    except KeyboardInterrupt: # Ctrl-C in terminal
        print("Timer stopped!")

try: 
    workTime, breakTime, top_of_30 = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]) # If user specifies custom work and break times
except:
    workTime, breakTime, top_of_30 = 25, 5, False

timer_start(workTime, breakTime, top_of_30)
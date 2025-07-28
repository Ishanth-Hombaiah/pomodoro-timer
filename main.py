import time
import winsound
import sys

def timer_start(workTime = 25, breakTime=5):
    time_intervals = [workTime * 60, breakTime * 60] # Default is 25 minutes of work and 5 minutes of break time
    intervalType = 0 # Whether the current session is for working or taking a break
    workSessionCount = 0

    print("The timer has begun! Use Ctrl-C to stop the timer.")
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
    workTime, breakTime = int(sys.argv[1]), int(sys.argv[2]) # If user specifies custom work and break times
except:
    workTime, breakTime = 25, 5

timer_start(workTime, breakTime)
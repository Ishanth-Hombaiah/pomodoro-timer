import time
import winsound

def timer_start():
    time_intervals = [25 * 60, 5 * 60] # 25 minutes of work and 5 minutes of break time
    currInterval = 0
    currSession = 0

    print("The timer has begun! Use Ctrl-C to stop the timer.")
    try: 
        while True:    
            currSession += 1
            time.sleep(time_intervals[currInterval])
            if currInterval == 0:
                print(f"Work session {currSession} complete! Take a 5 minute break.")
            else: 
                print(f"Break time over! Time for another 25 minutes of work.")
            currInterval = 1 - currInterval # Switch from study to break mode and vice versa
            winsound.Beep(1000, 500)

    except KeyboardInterrupt:
        print("Timer stopped!")

timer_start()
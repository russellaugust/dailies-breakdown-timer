import timer as t
import csv_export as csv

def timer_interface(mytimer):
    timer_active = True
    timer_paused = False
    while (timer_active):
        timer_input = input("Press enter to STOP (P to PAUSE):  ")
    
        if timer_input is "p":
            mytimer.pause()
            timer_paused = True
            while (timer_paused):
                paused_input = input("Paused...")
                timer_paused = False if paused_input is "" else True
                print ('Continuing' if timer_paused is False else "")
        elif timer_input is "u":
            mytimer.unpause()
        elif timer_input is "":
            timer_active = False
            mytimer_duration = mytimer.stop()
            return mytimer_duration


print ("\n")
print ("--------------------------------------")
print ("Welcome to the breakdown time tracker!")
print ("----------------------------------\n\n")

scene = input("Input your scene number:  ")
takes = input("Input number of takes:  ")
print ("\nSYNCING")
input("When you're ready, press ENTER to start syncing...")
sync = t.Timer()
sync.start()
print ("\nTimer Active!  Start syncing your dailies...")
sync_time = timer_interface(sync)

print (sync_time)

print ("\nMARKERS")
input("Press ENTER to start markering...")
markers = t.Timer()
markers.start()
print ("\nTimer Active!  Start markering the dailies...")
marker_time = timer_interface(markers)

print ("\nBUILD THE SEQUENCES")
scene_rt = input ("What's the total runtime (HH:MM:SS) of the sequence?:  ")

print ("\nTRIMMING")
input("Press ENTER to start trimming...")
trimming = t.Timer()
trimming.start()
print ("\nTimer Active!  Start trimming the dailies...")
trimming_time = timer_interface(trimming)

output = [[scene, takes, scene_rt, sync_time, marker_time, trimming_time]]

csv.export_csv(output)
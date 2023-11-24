from tkinter import *
import datetime
import simpleaudio as sa
import threading

def set_alarm():
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    alarm_triggered = False
    
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == set_alarm_time and not alarm_triggered:
            alarm_message()
            alarm_triggered = True
        elif current_time != set_alarm_time:
            alarm_triggered = False

def alarm_message():
    print("Time to Wake up")
    # Load and play the sound file
    wave_obj = sa.WaveObject.from_wave_file("sound.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait for the sound to finish playing

root = Tk()
root.geometry("400x200")
root.title("Alarm Clock")

Label(root, text="Alarm Clock", font=("Helvetica", 20, "bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica", 15, "bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = [str(i).zfill(2) for i in range(25)]
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = [str(i).zfill(2) for i in range(61)]
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = [str(i).zfill(2) for i in range(61)]
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

def set_alarm_thread():
    t = threading.Thread(target=set_alarm)
    t.daemon = True
    t.start()

Button(root, text="Set Alarm", font=("Helvetica", 15), command=set_alarm_thread).pack(pady=20)

root.mainloop()

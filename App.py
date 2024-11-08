import tkinter as tk
import time
import threading

root = tk.Tk()
root.title("Kronometre")
root.geometry("600x200")

root.resizable(False, False)

second = 0
hour = 0
minute = 0

flag = False
flag_sifirla = False


def startCounting():
    global flag, second, minute, hour, flag_sifirla

    if flag_sifirla:
        hour = 0
        minute = 0
        second = 0
        label.config(text=f"{hour} h   {minute} m   {second} s")
        flag_sifirla = False

    while flag:
        if second == 60:
            second = 0
            minute += 1
            if minute == 60:
                hour += 1
                minute = 0
                second = 0

        time.sleep(1)
        
        if flag == 0:
            break
        
        second += 1
        label.config(text=f"{hour} h   {minute} m   {second} s")


def pauseCounting():
    global flag, second
    print(f"Duraklatıldı, toplam saniye: {second}")
    flag = False


def stopButton():
    global flag, second, minute, hour, flag_sifirla
    print(f"Zaman durduruldu, toplam saniye: {second}")
    flag = False
    flag_sifirla = True


def startThread():
    global flag
    if not flag:
        flag = True
        threading.Thread(target=startCounting, daemon=True).start()


startButton = tk.Button(
    root, text="Başlat", command=startThread, font=("Arial", 14), width=14
)

pauseButton = tk.Button(
    root, text="Duraklat", command=pauseCounting, font=("Arial", 14), width=14
)
stopButton = tk.Button(
    root, text="Sıfırla", command=stopButton, font=("Arial", 14), width=14
)

label = tk.Label(
    root, text=f"{hour} h   {minute} m   {second} s", font=("Arial", 18), width=30
)

label_github = tk.Label(root, text="github.com/umutsar", font=("Arial", 10), width=30)

startButton.pack(side="left", pady=10)
startButton.place(x=50, y=10)

pauseButton.pack(side="left", pady=10)
pauseButton.place(x=220, y=10)

stopButton.pack(side="left", pady=10)
stopButton.place(x=390, y=10)

label.pack(pady=20)
label.place(x=100, y=90)


label_github.pack(pady=10)
label_github.place(x=194, y=180)


root.mainloop()

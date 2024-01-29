import tkinter as tk

window = tk.Tk()
window.title("timer")

'''
label
'''
label = tk.Label(window, text = 'vs code를 벗어나면 시간이 멈추는 타이머')
label.pack()
'''
timer button
'''
start = tk.Button(window, text = 'start')
start.pack()

window.mainloop()
import tkinter as tk
import tkinter.messagebox
window = tk.Tk()
window.title('Window')
window.geometry('400x200')
top_frame = tk.Frame(window)

top_frame.pack()
bottom_frame = tk.Frame(window)
bottom_frame.pack(side=tk.BOTTOM)

def echo_hello():
    print('hello world :)')


def onOK():
    msg = "Hello"
    tkinter.messagebox.showinfo(title = 'Hello', # 視窗標題
                                message = msg)   # 訊息內容

label = tk.Label(top_frame,fg='purple',text='Hello' )
label.pack()
left_button = tk.Button(top_frame, text='Red', fg='red', command=onOK)
# 讓系統自動擺放元件，預設為由上而下（靠左）
left_button.pack(side=tk.LEFT)

middle_button = tk.Button(top_frame, text='Green', fg='green')
middle_button.pack(side=tk.LEFT)

right_button = tk.Button(top_frame, text='Blue', fg='blue')
right_button.pack(side=tk.LEFT)

# 以下為 bottom 群組
# bottom_button 綁定 echo_hello 事件處理，點擊該按鈕會印出 hello world :)
bottom_button = tk.Button(bottom_frame, text='Black', fg='black', command=echo_hello)
# 讓系統自動擺放元件（靠下方）
bottom_button.pack(side=tk.BOTTOM)

window.mainloop()
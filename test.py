import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import ttk

# 創建主視窗
root = tk.Tk()
root.title("Tkinter and Matplotlib Integration")
root.geometry("600x600")


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# 設定圖表參數
resolution = 100
x_data = np.linspace(2*np.pi/resolution, 2*np.pi, resolution)
y_data = np.sin(x_data)
y2_data = np.cos(x_data)

fig, ax = plt.subplots()
line, = ax.plot(x_data, y_data, color='red' ,label="Sine wave")
line2, = ax.plot(x_data, y2_data, color='blue', label="Cosine wave")

ax.set_xlim(0, 2*np.pi)
ax.legend()

# 建立控制 sine 和 cosine 顯示的選項
show_sin = tk.BooleanVar(value=False)
show_cos = tk.BooleanVar(value=False)

# 更新圖例函數
def update_legend():
    handles, labels = [], []
    if show_sin.get():
        handles.append(line)
        labels.append("Sine wave")
    if show_cos.get():
        handles.append(line2)
        labels.append("Cosine wave")
    ax.legend(handles, labels)

# 更新函數
def update(frame):
    # 更新數據
    x_data[:-1] = x_data[1:]
    x_data[-1] += ((2 * np.pi) / resolution)
    y_data[:-1] = y_data[1:]
    y_data[-1] = np.sin(x_data[-1])
    y2_data[:-1] = y2_data[1:]
    y2_data[-1] = np.cos(x_data[-1])
    
    # 根據 checkbutton 的狀態來顯示或隱藏波形
    if show_sin.get():
        line.set_data(x_data, y_data)
    else:
        line.set_data([], [])  # 隱藏 sine wave

    if show_cos.get():
        line2.set_data(x_data, y2_data)
    else:
        line2.set_data([], [])  # 隱藏 cosine wave
    update_legend()
    ax.set_xlim(x_data[0], x_data[-1])  # 根據 x 軸數據更新 x 軸範圍
    return line, line2

# 動畫函數
ani = FuncAnimation(fig, update, save_count=100, interval=10, blit=False)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)



check_sin = tk.Checkbutton(root, text="Show Sine Wave", variable=show_sin)
check_sin.pack(side=tk.LEFT)

check_cos = tk.Checkbutton(root, text="Show Cosine Wave", variable=show_cos)
check_cos.pack(side=tk.LEFT)



# 處理視窗關閉事件
def on_closing():
    root.quit()  # 停止事件循環
    root.destroy()  # 銷毀視窗，確保程序完全結束
root.protocol("WM_DELETE_WINDOW", on_closing)

# 啟動事件循環
root.mainloop()
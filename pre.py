from tkinter import N
import psutil
from pypresence import Presence
import time

client_id = '921003369865302016'  # Fake ID, put your real one here
RPC = Presence(client_id,pipe=0)  # Initialize the client class
RPC.connect() # Start the handshake loop

print("成功連接到 Discord")

state = input("請輸入狀態: ")
details = input("請輸入詳細資訊: ")
large_image = input("請輸入大圖片的連結: ")
large_text = input("請輸入大圖片的文字: ")
small_image = input("請輸入小圖片的連結: ")
small_text = input("請輸入小圖片的文字: ")
def starttime():
    start_time_choose = input("是否顯示開始時間: (y/n) ")
    if start_time_choose == "y":
        return time.time()
    elif start_time_choose == "n" or start_time_choose == "":
        return None
    else:
        print("請輸入 y 或 n")
        return starttime()

start_time = starttime()

print("開始執行...")

if state == "":
    state = None
if details == "":
    details = None
if large_image == "":
    large_image = None
if large_text == "":
    large_text = None
if small_image == "":
    small_image = None
if small_text == "":
    small_text = None

RPC.update(state=state, details=details, large_image=large_image, large_text=large_text, small_image=small_image, small_text=small_text, start=start_time)

print("狀態已更新")

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("結束執行...")
        break
import time
import psutil 
import gpustat
import requests

TOKEN = ''  
CHAT_ID =   
cpu_usage = psutil.cpu_percent(interval=1)
gpu_usage = gpustat.GPUStatCollection.new_query()
ram_usage = psutil.virtual_memory().percent

def send_telegram_message(cpu_usage, gpu_usage):
        time.sleep(2)
        for gpu in gpu_usage.gpus:
          gpu_usage = f"GPU {gpu.name} - GPU USE {gpu.utilization}%"

        Message = f"CPU Usage: {cpu_usage}%\nGPU Usage: {gpu_usage}\nRAM Usage: {ram_usage}%"

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": Message}
        response = requests.post(url, data=data)


if __name__ == "__main__":
    while True:
        time.sleep(5) 
        send_telegram_message(cpu_usage, gpu_usage)

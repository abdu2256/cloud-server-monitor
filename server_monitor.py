import psutil
import time
import datetime
import logging
logging.basicConfig(
    filename="server_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - CPU:%(message)s"
)

def check_server_health():
    cpu = psutil.cpu_percent(interval=2)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    return cpu, memory, disk

def get_status(cpu, memory, disk):
    if cpu < 70 and memory < 70 and disk < 80:
        return "SERVER OK"
    else:
        return "ACTION REQUIRED"


while True:
    time_now = datetime.datetime.now() 

    cpu, memory, disk = check_server_health()
    status = get_status(cpu, memory, disk)

    print("Time:", time_now)
    print("CPU:", cpu, "%")
    print("RAM:", memory, "%")
    print("Disk:", disk, "%")
    print("Server Status:", status)
    print("---------------------------")
log_data = f"{cpu}% RAM:{memory}% DISK:{disk}% STATUS:{status}"
logging.info(log_data)

time.sleep(5)

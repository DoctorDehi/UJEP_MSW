import psutil
import time
from pynput.keyboard import Key, Listener

temp = time.time()
times = 0
def improve_seed(key):
    global times, temp
    times += 1
    # sber dat cpu, pameti a disku
    cpu = psutil.cpu_freq().current
    mem = psutil.virtual_memory().buffers
    disc = psutil.disk_io_counters(perdisk=False).write_bytes

    # proces vypoctu
    temp2 = cpu + mem + disc
    mod = temp2 % 19
    if mod != 0:
        temp *= (time.time() / mod)
    else:
        temp *= time.time()


    if isinstance(key, Key):
        num = int(str(key.value)[1:-1])
    else:
        num = ord(key.char)
    temp *= num

    # pokud bylo zadano alespon 5 klaves, program konci zapisem seedu do souboru
    if times >= 5:
        seed = int(temp)
        with open("seed.txt", "a") as f:
            f.write(str(seed))
            f.write("\n")
        exit()
    

def on_press(key):
    improve_seed(key)

print("Stiskněte 5 libovolných kláves:")

# Collect events until released
with Listener(
        on_press=on_press) as listener:
    listener.join()


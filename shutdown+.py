import os
import pyfiglet
import time
from pip._vendor.distlib.compat import raw_input

### WRITTEN BY https://github.com/SenoxCode ###
### YOU'RE NOT ALLOWED TO CHANGE THIS CODE AND PUBLISH IT ###


pythonname = "shutdown+"
version = 1.0

ascii_banner = pyfiglet.figlet_format(pythonname + " " +  str(version))
print(ascii_banner)

print("\ninsbot.py 1.0 by Senox")
time.sleep(0.3)
print("https://github.com/SenoxCode\n\n\n")
time.sleep(0.3)
print("Choose an option...")
time.sleep(0.3)
print("[0] EXIT")
time.sleep(0.1)
print("[1] SHUTDOWN IN SECONDS")
time.sleep(0.1)
print("[2] SHUTDOWN IN MINUTES")
time.sleep(0.1)
print("[3] SHUTDOWN IN HOURS")
time.sleep(0.1)
print("[4] CANCEL SHUTDOWN")
time.sleep(0.3)
option = raw_input()

print("\n\n\n")

if option == "0":
    print("Exiting...")
    time.sleep(3)
elif option == "1":
    print("In how much seconds your PC should shut down?")
    seconds = raw_input()
    print("Preparing shutdown...")
    time.sleep(3)
    os.system("shutdown -s -t " + str(seconds))
    if seconds == 1:
        print("Your PC will shut down in " + str(seconds) + " second.")
    else:
        print("Your PC will shut down in " + str(seconds) + " seconds.")
    time.sleep(1)
elif option == "2":
    print("In how much seconds your PC should shut down?")
    seconds = int(raw_input())
    seconds = seconds * 60
    print("Preparing shutdown...")
    time.sleep(3)
    os.system("shutdown -s -t " + str(seconds))
    seconds = seconds / 60
    seconds = int(seconds)
    if seconds == 1:
        print("Your PC will shut down in " + str(seconds) + " minute.")
    else:
        print("Your PC will shut down in " + str(seconds) + " minutes.")
    time.sleep(1)
elif option == "3":
    print("In how much hours your PC should shut down?")
    seconds = int(raw_input())
    seconds = seconds * 3600
    print("Preparing shutdown...")
    time.sleep(3)
    os.system("shutdown -s -t " + str(seconds))
    seconds = seconds / 3600
    seconds = int(seconds)
    if seconds == 1:
        print("Your PC will shut down in " + str(seconds) + " hour.")
    else:
        print("Your PC will shut down in " + str(seconds) + " hours.")
    time.sleep(1)
elif option == "4":
    print("SHUTDOWN IS CANCELLED\nEXITING...")
    os.system("shutdown -a")
    time.sleep(1)
else:
    print("ERROR")

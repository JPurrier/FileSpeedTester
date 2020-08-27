import os
import time
import PySimpleGUI as sg
from pathlib import Path
import shutil
from time import sleep
import sys
import datetime

time.perf_counter()

def main():
    file_transfer = ""
    save_location = ""
    cancelled = False
    desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop") 

    home = str(Path.home())
    layout = [
            [sg.Text("Save Locaion", size=(15, 1)), sg.InputText(str(home), key="sv"), sg.FolderBrowse()],
            [sg.Text("File To Transfer", size=(15, 1)), sg.InputText("", key="ft"), sg.FileBrowse()],
            [sg.Submit(), sg.Cancel()]
        ]


    window = sg.Window("Copy Time Tool", layout)
    while True:  # The Event Loop
        event, values = window.read()
        # print(event, values) #to uncomment debug
        if event in (None, "Exit", "Cancel"):
            cancelled = True
            break
        if event == "Submit":
            save_location = values["sv"]
            file_transfer = values["ft"]
            break
    
    if cancelled:
        sys.exit(0)

    progress =  [
                    [sg.Text("Please Wait Copying - Don't close me!")],
                    [sg.ProgressBar(1000, orientation="h", size=(20, 30), key="progbar")]
                ]

    prog = sg.Window("Copying File - Testing Time", progress)
    
    event, values = prog.read(timeout=0)
    print(values)
    t = time.perf_counter()
    shutil.copy2(file_transfer, save_location)
    result = time.perf_counter() - t
    
    prog["progbar"].update_bar(1000)
    prog.close()
    sleep(1)
    sg.popup("Time taken: "+ str(result) + "\n" + "Writing report to: \n" + str(os.path.join(desktop,"transfer_speed_report.txt")))

    with open(os.path.join(desktop,"transfer_speed_report.txt"),"a+") as f:
        message = "Time taken: " + str(result)
        print(message)
        f.write(message + "\n")


if __name__ == "__main__":
    main()

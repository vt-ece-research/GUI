from tkinter import *
from tkinter import ttk
import socket

# copied directly from port2port

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# LOCALHOST = '127.0.0.1'
# port = 3310

# s.connect((LOCALHOST,port))
# print("New client created: " )
# print("enter 'EXIT' to leave the program  \n")


def appendSatellite(*args):
    try: 
        value = iridiumSatellite.get()
        setSatellite.set(value)
        root.bind("<Return>", appendLatitude)
        latidue_entry.focus()

    except ValueError:
        pass

def appendLatitude(*args):
    try: 
        value = latidue.get()
        setLatidude.set(value)
        root.bind("<Return>", appendLongitude)
        longitude_entry.focus()
    except ValueError:
        pass

def appendLongitude(*args):
    try: 
        value = longitude.get()
        setLongitude.set(value)
        root.bind("<Return>", appendElevation)
        elevation_entry.focus()
    except ValueError:
        pass

def appendElevation(*args):
    try: 
        value = elevation.get()
        setElevation.set(value)
    except ValueError:
        pass

def combineElements():
    try:
        v1 = setSatellite.get()
        v2 = setLatidude.get()
        v3 = setLongitude.get()
        v4 = setElevation.get()
        value = v1 + ", " + v2 + ", " + v3 + ", " + v4
        clientCommand.set(value)
    except ValueError:
        pass
    
root = Tk()
root.title("MOSAIC GUI 1.0")

mainframe = ttk.Frame(root, padding="4 4 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# get iridium satellite
iridiumSatellite = StringVar()
Satellite_entry = ttk.Entry(mainframe, width=7, textvariable=iridiumSatellite)
Satellite_entry.grid(column=1, row=1, sticky=(W, E))
setSatellite = StringVar()
ttk.Label(mainframe, textvariable=setSatellite).grid(column=1, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Set Satellite", command=appendSatellite).grid(column=1, row=3, sticky=W)


# get latitude 
latidue = StringVar()
latidue_entry = ttk.Entry(mainframe, width=7, textvariable=latidue)
latidue_entry.grid(column=2, row=1, sticky=(W, E))
setLatidude = StringVar()
ttk.Label(mainframe, textvariable=setLatidude).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Set Latitude", command=appendLatitude).grid(column=2, row=3, sticky=W)


# get longitude 
longitude = StringVar()
longitude_entry = ttk.Entry(mainframe, width=7, textvariable=longitude)
longitude_entry.grid(column=3, row=1, sticky=(W, E))
setLongitude = StringVar()
ttk.Label(mainframe, textvariable=setLongitude).grid(column=3, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Set longitude", command=appendLongitude).grid(column=3, row=3, sticky=W)

# get elevation 
elevation = StringVar()
elevation_entry = ttk.Entry(mainframe, width=7, textvariable=elevation)
elevation_entry.grid(column=4, row=1, sticky=(W, E))
setElevation = StringVar()
ttk.Label(mainframe, textvariable=setElevation).grid(column=4, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Set elevation", command=appendElevation).grid(column=4, row=3, sticky=W)

# prepare command
clientCommand = StringVar()
ttk.Button(mainframe, text="Send command", command=combineElements).grid(column=4, row=4, sticky=W)
ttk.Label(mainframe, textvariable=clientCommand).grid(column=2, row=4, sticky=(W, E))


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

Satellite_entry.focus()
root.bind("<Return>", appendSatellite)






root.mainloop()
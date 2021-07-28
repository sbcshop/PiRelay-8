from tkinter import *
from PiRelay8 import Relay
import time
    
relays = [None]*8
for i in range(8):
    relays[i] = Relay("RELAY"+str(i+1))

root = Tk()
root.geometry('800x480')
root.title('PiRelay 8')
root.configure(bg='black',cursor='none')
root.attributes('-fullscreen', True)
time1 = ''
myvar = Label(root, anchor='ne', font=('time', 15, 'bold'), bg='black',
              bd=0, fg='orange')
myvar.grid(row=1, column=4, pady=5)


def timeupdate():
    """
    Update time on PiRelay GUi
    """
    global time1
    time_string = time.strftime('%H:%M:%S')
    if time_string != time1:
        time1 = time_string
        myvar.config(text=time_string)
    myvar.after(200, timeupdate)


# label 1
Label(root, text='HOME AUTOMATION', relief=RAISED, anchor=CENTER,
      bg='black', fg='white', font=('time',25,'bold'), bd=0).grid(row=1,
                                                                  column=1,
                                                                  columnspan=4,
                                                                  padx=30,
                                                                  pady=25)

# label 2
Labels = [("RELAY 1", 5, 1), ("RELAY 2", 5, 2), ("RELAY 3", 5, 3),
          ("RELAY 4", 5, 4), ("RELAY 5", 8, 1), ("RELAY 6", 8, 2),
          ("RELAY 7", 8, 3), ("RELAY 8", 8, 4)]

for i in range(8):
    labl = Label(root, text=Labels[i][0], relief=RAISED, anchor=CENTER,
                 borderwidth=3, font=('Time',10,'bold'), width=10,
                 bg='lightskyblue', fg='black')
    labl.grid(row=Labels[i][1], column=Labels[i][2], padx=45,pady=25 )


def relay_onoff(relay_num):
    """
    Switch relays and change button configuration
    :param relay_num: Index of relay to Turn On/Off
    :return: None
    """
    relay_status = relay_button[relay_num].cget('text')
    if relay_status == 'On':
        relay_button[relay_num].config(text='Off', fg='white',
                                       relief=SUNKEN,
                                       activeforeground='white',
                                       activebackground='orangered', bg='red')
        relays[relay_num].on()
    elif relay_status == 'Off':
        relay_button[relay_num].configure(text='On', fg='white',
                                          relief=RAISED,
                                          activeforeground='white',
                                          activebackground='green3',
                                          bg='green')
        relays[relay_num].off()
    
        
#  Relay Buttons
relay_button = [None]*8


def button(relay_num, row, column):
    """
    Draw relay buttons
    :param relay_num: index of Relay to draw
    :param row: Row number to draw relay button at
    :param column: Column Number to draw relay button at
    :return: None
    """
    relay_button[relay_num] = Button(root, text='On', font=("Times", 20,
                                                            "bold"),
                                     activebackground='green3',
                                     command=lambda: relay_onoff(
                                         relay_num=relay_num), width=5,
                                     height=2, fg='white', bg='green', bd=5)
    relay_button[relay_num].grid(row=row, column=column)


for relay in range(4):
    button(relay_num=relay, row=4, column=relay+1)
    button(relay_num=relay+4, row=7, column=relay+1)

#  Exit Button
exit_button = Button(root, text='EXIT', font=("Times", 15, "bold"), width=10,
                     command=root.destroy, fg='black', bg='chocolate2', bd=5,
                     activebackground='chocolate1')
exit_button.grid(row=10, column=1, columnspan=4, pady=20, padx=48)

timeupdate()

mainloop()

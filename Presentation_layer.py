"""
    presentation_layer.py
    ~~~~~~~~~~~~~~~

    Dette modul implementerer
    bookingsystemets layout.

"""

from tkinter import *
from Data_layer import *


class BookingSystem:

    def __init__(self, root):
        self._root = root
        self._use = UsernameAndPass()

        # forside frame
        self._main_frame = Frame(self._root)

        # opret / login bruger frame
        self._user_frame = Frame(self._root)

        # reservationsframe
        self._res_frame = Frame(self._root)

        # foto på forside
        self._photo_front = PhotoImage(file='forside.png')

        # overskrift
        self._headline_label = Label(self._main_frame, text='BOOK EN FRISØRTID', font=('Helvetica 35 bold'))

        # knapper
        self._opret_bruger_btn = Button(self._main_frame, text='Opret bruger', font=('Helvetica', 20), command=self.switch)
        self._log_ind_bruger_btn = Button(self._main_frame, text='Log ind', font=('Helvetica', 20))

        self._brugernavn_label = Label(self._user_frame, text='Brugernavn:')
        self._brugernavn_entry = Entry(self._user_frame)
        self._kode_label = Label(self._user_frame, text='Adgangskode:')
        self._kode_entry = Entry(self._user_frame)
        self._photo_front_label = Label(self._main_frame, image=self._photo_front)

        # pack
        self._headline_label.pack(side=TOP)
        self._main_frame.pack(side=TOP)

        self._opret_bruger_btn.pack(side=BOTTOM)
        self._log_ind_bruger_btn.pack(side=BOTTOM)

        self._photo_front_label.pack()

        self._root.geometry('500x500')

    def switch(self):
        self._main_frame.forget()
        self._user_frame.pack(side=TOP)

#self._use.create_user(self._brugernavn_entry, self._kode_entry)

if __name__ == "__main__":
    window = Tk()
    window.title("Bookingsystem")
    bs = BookingSystem(window)
    window.mainloop()
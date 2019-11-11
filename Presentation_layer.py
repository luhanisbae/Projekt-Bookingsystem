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

        # FORSIDEFRAME + ALT TIL FORSIDEN
        self._main_frame = Frame(self._root)

        self._photo_front = PhotoImage(file='forside.png')
        self._photo_front_label = Label(self._main_frame, image=self._photo_front)

        self._headline_label = Label(self._main_frame, text='BOOK EN FRISØRTID', font=('Helvetica 35 bold'))

        # knapper
        self._opret_bruger_btn = Button(self._main_frame, text='Opret bruger', font=('Helvetica', 20), command=self.switch_main)
        self._log_ind_bruger_btn = Button(self._main_frame, text='Log ind', font=('Helvetica', 20), command=self.switch_main)

        # pack
        self._main_frame.pack(side=TOP)
        self._headline_label.pack(side=TOP)
        self._opret_bruger_btn.pack(side=BOTTOM)
        self._log_ind_bruger_btn.pack(side=BOTTOM)
        self._photo_front_label.pack()

        # BRUGERFRAME + ALT TIL DENNE SIDE
        self._user_frame = Frame(self._root)

        # knap, label med tilhørende entry
        self._brugernavn_label = Label(self._user_frame, text='Brugernavn:')
        self._brugernavn_entry = Entry(self._user_frame)
        self._opret_btn = Button(self._user_frame, text='Opret bruger', font=('Helvetica', 20),)
        self._log_ind_btn = Button(self._user_frame, text='Log ind', font=('Helvetica', 20))
        self._kode_label = Label(self._user_frame, text='Adgangskode:')
        self._kode_entry = Entry(self._user_frame)

        # pack
        self._brugernavn_label.pack(side=TOP)
        self._brugernavn_entry.pack(side=TOP)
        self._kode_label.pack(side=TOP)
        self._kode_entry.pack(side=TOP)
        self._opret_btn.pack(side=TOP)
        self._log_ind_btn.pack(side=TOP)

        # RESERVATIONSFRAME
        self._res_frame = Frame(self._root)


        self._root.geometry('500x500')

    def switch_main(self):
        self._main_frame.forget()
        self._user_frame.pack(side=TOP)

    def switch_user(self):
        self._user_frame.forget()
        self._res_frame.pack(side=TOP)

        self._use.create_user(user=self._brugernavn_entry, password=self._kode_entry)

if __name__ == "__main__":
    window = Tk()
    window.title("Bookingsystem")
    bs = BookingSystem(window)
    window.mainloop()
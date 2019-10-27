"""
    bookingsystem.py
    ~~~~~~~~~~~~~~~

    Dette program implementerer et bookingsystem
    hos en frisør vha. tkinter.

"""

from tkinter import *


class BookingSystem:

    def __init__(self, root):
        self._root = root
        self.title = 'Bookingsystem'

        # forside frame
        self._main_frame = Frame(self._root)

        # opret / login bruger frame
        self._user_frame = Frame(self._root)

        # reservationsframe
        self._res_frame = Frame(self._root)

        # knapper
        self._opret_bruger = Button(self._main_frame, text='Opret bruger')
        self._log_ind_bruger = Button(self._main_frame, text='Log ind')
        self._brugernavn = Label(self._user_frame, text='Brugernavn:')
        self._skriv_brugernavn = Entry(self._user_frame)
        self._kode = Label(self._user_frame, text='Adgangskode:')
        self._skriv_kode = Entry(self._user_frame)

        # pack
        self._main_frame.pack(side=TOP)
        self._user_frame.pack(side=BOTTOM)
        self._res_frame.pack(side=BOTTOM)

        self._opret_bruger.pack(side=LEFT)
        self._log_ind_bruger.pack(side=LEFT)

        self._root.geometry('500x500')


if __name__ == "__main__":
    window = Tk()
    bs = BookingSystem(window)
    window.mainloop()
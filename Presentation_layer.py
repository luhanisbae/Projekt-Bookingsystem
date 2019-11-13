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
        self._res = User_obj()

        # FORSIDEFRAME + ALT TIL FORSIDEN
        self._main_frame = Frame(self._root)

        self._photo_front = PhotoImage(file='forside.png')
        self._photo_front_label = Label(self._main_frame, image=self._photo_front)

        self._headline_label = Label(self._main_frame, text='BOOK EN FRISØRTID', font=('Helvetica 35 bold'))

        # knapper
        self._create_user1_btn = Button(self._main_frame, text='Opret bruger', font=('Helvetica', 20), command=self.switch_main)
        self._log_in_user1_btn = Button(self._main_frame, text='Log ind', font=('Helvetica', 20), command=self.switch_main)

        # pack
        self._main_frame.pack(side=TOP)
        self._headline_label.pack(side=TOP)
        self._create_user1_btn.pack(side=BOTTOM)
        self._log_in_user1_btn.pack(side=BOTTOM)
        self._photo_front_label.pack()

        # BRUGERFRAME + ALT TIL DENNE SIDE
        self._user_frame = Frame(self._root)

        # knap, label med tilhørende entry
        self._username_label = Label(self._user_frame, text='Brugernavn:')
        self._username_entry = Entry(self._user_frame)
        self._create_user2_btn = Button(self._user_frame, text='Opret bruger', font=('Helvetica', 20), command=self._create_user)
        self._log_in_user2_btn = Button(self._user_frame, text='Log ind', font=('Helvetica', 20), command=self.switch_user)
        self._pass_label = Label(self._user_frame, text='Adgangskode:')
        self._pass_entry = Entry(self._user_frame)

        # pack
        self._username_label.pack(side=TOP)
        self._username_entry.pack(side=TOP)
        self._pass_label.pack(side=TOP)
        self._pass_entry.pack(side=TOP)
        self._create_user2_btn.pack(side=TOP)
        self._log_in_user2_btn.pack(side=TOP)


        # RESERVATIONSFRAME
        self._res_frame = Frame(self._root)

        # knap, entry
        self._res_entry = Entry(self._res_frame)
        self._create_res_btn = Button(self._res_frame, text='Opret reservation', font=('Helvetica', 20), command=self._res.create_reservation(time=self._res_entry.get()))
        self._del_res_btn = Button(self._res_frame, text='Slet reservation', font=('Helvetica', 20))
        self._edit_res_btn = Button(self._res_frame, text='Redigér reservation', font=('Helvetica', 20))


        # listbox
        self._res_lb = Listbox(self._res_frame)

        # pack
        self._create_res_btn.pack(side=TOP)
        self._del_res_btn.pack(side=TOP)
        self._edit_res_btn.pack(side=TOP)
        self._res_entry.pack(side=BOTTOM)
        self._res_lb.pack()



        self._root.geometry('500x500')


    def switch_main(self):
        self._main_frame.forget()
        self._user_frame.pack(side=TOP)

    def switch_user(self):
        if self._use.create_user(user=self._username_entry.get(), password=self._pass_entry.get()) is True:
            self._user_frame.forget()
            self._res_frame.pack(side=TOP)

    def _create_user(self):
        try:
            if len(self._username_entry.get()) > 0 and len(self._pass_entry.get() > 0):
                raise ValueError
        except ValueError:
            print("Wrong length")
        self._use.create_user(user=self._username_entry.get(), password=self._pass_entry.get())

if __name__ == "__main__":
    window = Tk()
    window.title("Bookingsystem")
    bs = BookingSystem(window)
    window.mainloop()

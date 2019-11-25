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
        self._create_user_log_in_btn = Button(self._main_frame, text='Videre', font=('Helvetica', 20), command=self.switch_from_main)

        # pack
        self._main_frame.pack()
        self._headline_label.pack()
        self._create_user_log_in_btn.pack(side=BOTTOM)
        self._photo_front_label.pack()

        # BRUGERFRAME + ALT TIL DENNE SIDE
        self._user_frame = Frame(self._root)

        #self._photo_user = PhotoImage(file='hairstyle.png')
        #self._photo_user_label = Label(self._user_frame, image=self._photo_user)

        # knap, label med tilhørende entry
        self._username_label = Label(self._user_frame, text='Brugernavn:')
        self._username_entry = Entry(self._user_frame)
        self._create_user_btn = Button(self._user_frame, text='Opret bruger', font=('Helvetica', 20), command=self._create_user)
        self._log_in_user_btn = Button(self._user_frame, text='Log ind', font=('Helvetica', 20), command=self.switch_from_user)
        self._pass_label = Label(self._user_frame, text='Adgangskode:')
        self._pass_entry = Entry(self._user_frame)

        self._back1_btn = Button(self._user_frame, text='Back', font=('Helvetica', 8), command=self.switch_to_main)

        # pack
        self._username_label.pack()
        self._username_entry.pack()
        self._pass_label.pack()
        self._pass_entry.pack()
        self._create_user_btn.pack()
        self._log_in_user_btn.pack()
        self._back1_btn.pack(side=BOTTOM)


        # RESERVATIONSFRAME
        self._res_frame = Frame(self._root)

        self._res_headline_label = Label(self._res_frame, text='DINE RESERVATIONER', font=('Helvetica', 20))

        # knap, entry
        self._res_entry = Entry(self._res_frame)
        self._create_res_btn = Button(self._res_frame, text='Opret reservation', font=('Helvetica', 20), command=self.add_to_listbox)
        self._del_res_btn = Button(self._res_frame, text='Slet reservation', font=('Helvetica', 20), command=self.delete_in_listbox)
        self._edit_res_btn = Button(self._res_frame, text='Redigér reservation', font=('Helvetica', 20), command=self.edit_in_listbox)

        self._show_interval_res_btn = Button(self._res_frame, text='Vis reservationer i bestemt interval', font=('Helvetica', 12), command=self.show_interval_entries)
        self._starttime_label = Label(self._res_frame, text='Start tid: ', font=('Helvetica', 10))
        self._starttime_entry = Entry(self._res_frame, font=('Helvetica', 10))
        self._endtime_label = Label(self._res_frame, text='Slut tid: ', font=('Helvetica', 10))
        self._endtime_entry = Entry(self._res_frame, font=('Helvetica', 10))
        self._show_res_btn = Button(self._res_frame, text='Vis', font=('Helvetica', 10), command=self.show_specific_interval)

        self._back2_btn = Button(self._res_frame, text='Back', font=('Helvetica', 8), command=self.switch_to_user)

        self._text1_label = Label(self._res_frame, text='OBS! Tjek, hvad du har indtastet.', font=('Helvetica', 15), fg='red')


        # listbox
        self._res_lb = Listbox(self._res_frame)

        # pack
        self._res_headline_label.pack()
        self._res_lb.pack()
        self._res_entry.pack()
        self._create_res_btn.pack()
        self._del_res_btn.pack()
        self._edit_res_btn.pack()
        self._back2_btn.pack(side=BOTTOM)

        self._show_interval_res_btn.pack()

        self._root.geometry('500x500')


    def switch_from_main(self):
        self._main_frame.forget()
        self._user_frame.pack()

    def switch_to_main(self):
        self._user_frame.forget()
        self._main_frame.pack()

    def switch_from_user(self):
        if self._use.login_user(user=self._username_entry.get(), password=self._pass_entry.get()) is True:
            self._user_frame.forget()
            self._res_frame.pack()

    def switch_to_user(self):
        self._res_frame.forget()
        self._user_frame.pack()

    def _create_user(self):
        try:
            if len(self._username_entry.get()) == 0 or len(self._pass_entry.get()) == 0:
                raise ValueError
        except ValueError:
            print("Wrong length")
        self._use.create_user(user=self._username_entry.get(), password=self._pass_entry.get())

    def add_to_listbox(self):
        if len(self._res_entry.get()) != 4 or int(self._res_entry.get()) in self._res._reservation:
            self._text1_label.pack(side=BOTTOM)
        else:
            self._text1_label.forget()
            self._res_lb.insert(END, int(self._res_entry.get()))
            self._res.create_reservation(int(self._res_entry.get()))

    def delete_in_listbox(self):
        self._res_lb.delete(self._res_lb.curselection())
        self._res.delete_reservation(int(self._res_lb.curselection()))

    def edit_in_listbox(self):
        if len(self._res_entry.get()) != 4 or int(self._res_entry.get()) in self._res._reservation:
            pass
        else:
            self._res_lb.insert(self._res_lb.curselection(), int(self._res_entry.get()))
            self._res_lb.delete(self._res_lb.curselection())
            self._res.edit_reservation(self._res_lb.curselection(), int(self._res_entry.get()))

    def show_interval_entries(self):
        self._starttime_label.pack(side=LEFT)
        self._starttime_entry.pack(side=LEFT)
        self._endtime_label.pack(side=LEFT)
        self._endtime_entry.pack(side=LEFT)
        self._show_res_btn.pack(side=LEFT)
        self._show_interval_res_btn.forget()

    def show_specific_interval(self):
        self._res.show_reservation_interval(int(self._starttime_entry.get()), int(self._endtime_entry.get()))


if __name__ == "__main__":
    window = Tk()
    window.title("Bookingsystem")
    bs = BookingSystem(window)
    window.mainloop()

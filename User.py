

class User_obj:

    def __init__(self):
        self._reservation = []

    def create_reservation(self, time):
        self._reservation.append(time)

    def delete_reservation(self, time):
        self._reservation.remove(time)

    def edit_reservation(self, time, new_time):
        self._reservation.append(new_time)
        self._reservation.remove(time)

    def show_reservation(self):
        print(self._reservation)

    def show_reservation_interval(self, start_time, end_time):
        reservlist = []
        for i in self._reservation:
            if start_time <= i <= end_time:
                reservlist.append(i)
        return reservlist


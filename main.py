# 25-m
class Alarm:
    def __init__(self, time):
        self.time = time

    def set_alarm(self):
        print(f"Alarm {self.time} ga o‘rnatildi ")

    def ring(self):
        print(f"Jiring!!!")


m1 = Alarm("07:00")
m1.set_alarm()
m1.ring()

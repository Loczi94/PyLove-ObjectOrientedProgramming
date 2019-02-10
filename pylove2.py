# encoding: utf-8

class Czas:
    def __init__(self, h=0, m=0, s=0):
        self.hours = h
        self.minutes = m
        self.seconds = s
    def __str__(self):
        temp = "{} ".format(self._get_name())
        print(temp)
        print('Godziny: '+str(self.hours))
        print('Minuty: ' + str(self.minutes))
        print('Sekundy: ' + str(self.seconds))
        return "Godziny = {} Minuty = {} Sekundy = {}".format(self.hours, self.minutes, self.seconds)

    @classmethod
    def _get_name(cls):
        return cls.__name__

    def set_time(self, new_h=None, new_m=None, new_s=None):
        self.hours = new_h
        self.minutes = new_m
        self.seconds = new_s

    def add_time(self, h=None, m=None, s=None):
        if s:
            self.seconds += s
            if self.seconds // 60 >= 1:
                self.minutes += self.minutes // 60
                self.seconds = self.seconds % 60
        if m:
            self.minutes += m
            if self.minutes // 60 >= 1:
                self.hours += self.minutes // 60
                self.minutes = self.minutes % 60
        if h:
            self.hours += h

    def get_seconds(self):
        all_seconds = self.seconds + (self.minutes * 60) + (self.hours * 60 * 60)
        return all_seconds

    def get_minutes(self):
        all_minutes = (round(self.seconds / 60 ,2)) + self.minutes + (self.hours * 60)
        return all_minutes

    def get_hours(self):
        all_hours = (round(self.seconds / 60 / 60 ,2)) + (round(self.minutes / 60 ,2)) + self.hours
        return all_hours

class Zegar(Czas):
    def __init__(self, format, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.format = format

class DokładnyZegar(Zegar):
    def __init__(self, ms=0, *args, **kwargs):
        super().__init__(**kwargs)
        self.miliseconds = ms
    def set_time(self, ms=None, **kwargs):
        super().set_time(**kwargs)
        if ms:
            self.miliseconds = ms
    def add_time(self, ms=None, **kwargs):
        super().add_time(**kwargs)
        if ms:
            self.miliseconds += ms
            if self.miliseconds // 60 >= 1:
                self.seconds += self.miliseconds // 60
                self.miliseconds = self.miliseconds % 60

class Print():
    @staticmethod
    def moj_print(text, count, prefix='', end=''):
        for c in range(0,count):
            print(prefix+text+end)

if __name__ == '__main__':
    czasNajwyzszy = Czas(1,29,30)
    zegarekNaReke = Zegar('12H', 11)
    bardzoDokladnyZegar = DokładnyZegar(h=1,m=2,s=3,ms=4,format='24H')
    # czasNajwyzszy.set_time(0,2,3)
    # czasNajwyzszy.__str__()
    # czasNajwyzszy.get_seconds()
    czasNajwyzszy.get_hours()
    bardzoDokladnyZegar.get_hours()
    Print.moj_print('mojtekscior',5,'HAHAHA')

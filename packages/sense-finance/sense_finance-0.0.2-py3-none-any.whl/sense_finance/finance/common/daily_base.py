import datetime


class BaseDailyJob(object):

    def __init__(self, hour=0, mod_index=0, mod_size=4):
        self.last_time = 0
        if type(hour) == list:
            self.hours = hour
        else:
            self.hours = [hour]
        self.mod_index = mod_index
        self.mod_size = mod_size

    def need_work(self):
        hour = get_current_hour()
        if hour not in self.hours:
            sd.log_info("not well hour={}".format(hour))
            return False
        day = datetime.datetime.now().weekday()
        if not self.is_good_day(day):
            return False
        diff = sd.get_current_second() - self.last_time
        if diff < 3600 * 4:
            return False
        return True

    def is_good_day(self, day):
        return True

    def once_update_work(self):
        pass

    @sd.try_catch_exception
    def once_update(self, day_size=1, mod=1, must=False):
        if not self._need_once_update_work(day_size, mod, must):
            return
        self.once_update_work()
        self.last_time = sd.get_current_second()

    def _need_once_update_work(self, day_size=1, mod=1, must=False):
        if must:
            return True
        if not self.need_work():
            sd.log_info("no need work")
            return False
        if day_size > 1:
            day = datetime.datetime.now().weekday()
            if day % day_size != mod:
                sd.log_info("no need once_update")
                return False
        return True

    @sd.try_catch_exception
    def loop_daily_work(self, day_size=1, mod=1):
        while True:
            self.once_update(day_size, mod)
            sd.sleep(60)

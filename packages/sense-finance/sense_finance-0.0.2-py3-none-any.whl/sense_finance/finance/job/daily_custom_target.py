from sense_finance.finance.common.daily_base import BaseDailyJob
from sense_finance.finance.model import *
from sense_finance.finance.custom import NewCustomTargetUpdater


class CustomTargetDailyJob(BaseDailyJob):

    def __init__(self, hour=0):
        super(CustomTargetDailyJob, self).__init__(hour=hour, mod_index=0, mod_size=2)

    @sd.try_catch_exception
    def once_update_work(self):
        self.mod_index += 1
        handler = NewCustomTargetUpdater()
        handler.update_all(mod_index=self.mod_index % self.mod_size, mod_size=self.mod_size)

    def is_good_day(self, day):
        return True

    def update_target(self):
        handler = NewCustomTargetUpdater()
        target = CustomTarget.find_by_id(1001207)
        handler.update_target(target)


if __name__ == "__main__":
    init_config('daily_custom_target')
    sd.set_log_process_name(True)
    sd.set_log_thread_name(True)
    job = CustomTargetDailyJob(22)
    job.once_update_work()
    job.loop_daily_work(1, 1)

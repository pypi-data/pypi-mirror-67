import sense_core as sd
from sense_finance.finance.util import init_config
from sense_finance.finance.common.daily_base import BaseDailyJob
from sense_finance.finance.target import IndustryTargetUpdater
import gc


class IndustryTargetDailyJob(BaseDailyJob):

    def __init__(self, hour=0, mod_size=2):
        super(IndustryTargetDailyJob, self).__init__(hour=hour, mod_index=0, mod_size=mod_size)

    def is_good_day(self, day):
        return True

    @sd.try_catch_exception
    def once_update_work(self):
        self.mod_index += 1
        IndustryTargetUpdater().update_all(mod_index=self.mod_index % self.mod_size, mod_size=self.mod_size,
                                           report_year=2019)
        gc.collect()


if __name__ == "__main__":
    init_config('daily_industry')
    sd.set_log_process_name(True)
    sd.set_log_thread_name(True)
    job = IndustryTargetDailyJob(2, mod_size=1)
    job.once_update_work()

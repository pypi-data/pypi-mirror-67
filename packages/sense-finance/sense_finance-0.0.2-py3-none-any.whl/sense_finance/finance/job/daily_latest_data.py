import sense_core as sd
from sense_finance.finance.util import init_config
from sense_finance.finance.common.daily_base import BaseDailyJob
from sense_finance.finance.work.target_latest_data import TargetLatestDataUpdater2
from sense_finance.finance.work.target_latest_data import CompanyTargetLatestDataWorker


class DailyLatestDataJob(BaseDailyJob):

    def __init__(self, hour=0):
        super(DailyLatestDataJob, self).__init__(hour=hour, mod_index=0, mod_size=2)

    @sd.try_catch_exception
    def update_target_latest_data(self):
        self.mod_index += 1
        updater = TargetLatestDataUpdater2()
        updater.update_all(thread_num=1, mod_index=self.mod_index % self.mod_size, mod_size=self.mod_size)
        worker = CompanyTargetLatestDataWorker()
        worker.update_all_company_industry()

    def is_good_day(self, day):
        return True

    @sd.try_catch_exception
    def once_update_work(self):
        self.update_target_latest_data()


if __name__ == "__main__":
    init_config('daily_latest_data')
    sd.set_log_process_name(True)
    sd.set_log_thread_name(True)
    job = DailyLatestDataJob(0)
    job.once_update_work()
    # job.loop_daily_work(1, 1)

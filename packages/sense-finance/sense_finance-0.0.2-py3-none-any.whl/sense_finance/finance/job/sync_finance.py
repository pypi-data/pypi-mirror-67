import sense_core as sd
from sense_finance.finance.util import init_config
from sense_finance.finance.work.sync_sense import SenseSyncHandler

if __name__ == "__main__":
    init_config('sync_finance')
    sd.set_log_process_name(True)
    handler = SenseSyncHandler(True)
    handler.start_work(4)

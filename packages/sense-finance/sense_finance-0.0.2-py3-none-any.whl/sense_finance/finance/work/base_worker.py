import sense_core as sd
import multiprocessing


class BaseWorker(object):

    def _create_process(self, loop_work):
        p = multiprocessing.Process(target=loop_work)
        p.start()

    def start_work(self, process_num=1):
        if process_num <= 1:
            self.loop_work()
        else:
            for i in range(0, process_num):
                self._create_process(self.loop_work)
        while True:
            sd.sleep(10)

    def loop_work(self):
        while True:
            self.consume_queue()
            sd.sleep(2)

    @sd.try_catch_exception
    def consume_queue(self):
        pass

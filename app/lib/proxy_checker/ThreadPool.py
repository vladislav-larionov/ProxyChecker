from PySide2.QtCore import QObject, Signal, Slot


class ThreadPool(QObject):
    done_signal = Signal()
    stopped_signal = Signal()

    def __init__(self, count):
        super().__init__()
        self.thread_count = count
        self.threads = list()
        self.done = 0

    def init_threads(self, constructor, *args, **kwargs):
        for i in range(self.thread_count):
            thread = constructor(*args, **kwargs)
            yield thread
            thread.signals.thread_done_signal.connect(self.on_done_signal)
            self.threads.append(thread)

    def start(self):
        for thread in self.threads:
            thread.start()

    @Slot()
    def on_done_signal(self):
        self.done += 1
        if self.done == self.thread_count:
            self.done_signal.emit()

    def stop(self):
        for thread in self.threads:
            thread.revert_current_data()
            thread.terminate()
        self.stopped_signal.emit()

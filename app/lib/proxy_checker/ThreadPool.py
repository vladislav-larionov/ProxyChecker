from PySide2.QtCore import QObject, Signal, Slot


class ThreadPool(QObject):
    done_signal = Signal()
    stopped_signal = Signal()

    def __init__(self):
        super().__init__()
        self.thread_count = 0
        self.threads = list()
        self.done = 0

    def add_thread(self, thread):
        thread.signals.thread_done_signal.connect(self.on_done_signal)
        self.threads.append(thread)

    def start(self):
        self.thread_count = len(self.threads)
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

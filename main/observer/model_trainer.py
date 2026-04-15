from observer.subject import Subject

class ModelTrainer(Subject):
    def __init__(self):
        super().__init__()
        self._epoch = 0
        self._accuracy = 0.0

    def get_accuracy(self) -> float:
        return self._accuracy

    def get_epoch(self) -> int:
        return self._epoch

    def set_metrics(self, epoch: int, accuracy: float) -> None:
        self._epoch = epoch
        self._accuracy = accuracy

        self.notify_observers()
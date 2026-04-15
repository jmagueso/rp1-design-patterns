class Subject:
    def __init__(self):
        self._observers = []

    def add(self, observer) -> None:
        # TODO: adicionar observer na lista _observers para ser notificado posteriormente
        pass

    def notify_observers(self) -> None:
        # TODO: percorrer a lista e chamar o método update() de cada observer
        pass
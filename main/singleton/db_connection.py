import time

class DataLakeConnection:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def connect(self):
        print(f"Connecting to {self.connection_string}")
        time.sleep(1)
        print("Connected!!")
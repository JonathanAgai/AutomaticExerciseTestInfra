import abc


class Operation(abc.ABC):
    def execute(self):
        raise NotImplementedError

    def print(self):
        raise NotImplementedError

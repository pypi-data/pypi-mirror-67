import abc


class Engine:
    __metaclass__ = abc.ABCMeta

    def __init__(self, envs, trainer):
        self.envs = envs
        self.trainer = trainer

    @abc.abstractmethod
    def run(self):
        pass


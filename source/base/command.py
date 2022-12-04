class BaseCommand():
    """Base class Command
    """

    def __init__(self, **kwargs) -> None:
        if kwargs:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))

        if hasattr(self, self.run):
            getattr(self, self.run)()

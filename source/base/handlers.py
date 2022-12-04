class BaseHandler():
    """Base class Handler
    """

    def __init__(self, browser, link) -> None:
        self.browser = browser
        self.link = link
        self.run()

    def run(self):
        pass

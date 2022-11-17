import logging

logging.basicConfig(level=logging.INFO)

logging.basicConfig(
    filename='app.log',
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s'
)

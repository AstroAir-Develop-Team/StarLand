import logging

logger = logging.getLogger(__name__)
console_handle = logging.StreamHandler()
logger.addHandler(console_handle)
fort = logging.Formatter('[%(asctime)s][%(levelname)s]%(message)s')
console_handle.setFormatter(fort)
logger.setLevel(logging.INFO)

class starlog():

    def __init__(self,name) -> None:
        self.uname = name
        pass

    def __del__(self) -> None:
        pass

    def log(self,msg) -> (str):
        logger.info(f"[{self.uname}] - {msg}")
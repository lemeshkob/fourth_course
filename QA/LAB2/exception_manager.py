from dataclasses import dataclass
from file_handler import MyFileHandler
# from server_handler import MyServerHandler

@dataclass
class ExceptionManager:

    is_critical_count: int = 0
    is_not_critical_count: int = 0

    @classmethod
    def is_critical(cls, e: Exception):
        if type(e).__name__ in MyFileHandler.file_handler():
            return True
        else: return False

    def handle_manager(self, e: Exception):
        if MyServerHandler.is_checked(e):
            self.is_critical_count += 1
        else:
            self.is_not_critical_count += 1


class MyServerHandler:

    @classmethod
    def is_checked(cls, e: Exception):
        cls.is_critical = ExceptionManager.is_critical(e)
        if cls.is_critical:
            return True
        else: return False

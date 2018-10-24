class MyFileHandler:

    @staticmethod
    def file_handler():
        with open('config.txt', 'r') as file:
            data = file.read().splitlines()
            return [e for e in data]

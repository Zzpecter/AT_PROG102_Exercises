from abc import ABC, abstractmethod

class Validator(ABC):

    def __init__(self, file):
        self.errorLogs = []

    def get_files(self):
        files = []
        for root, dirs, files in os.walk(self.directory):
            for name in files:
                files.append(str(root + "/" + name))
        return files

    def validate():
        pass
        
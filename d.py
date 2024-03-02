# d.py

# The following program demonstrates DIP or 'Dependency Inversion Principle'
# This principle is stated that high-level mand low-level modules should depend on abstractions rather than each other.
# Class LoggerInterface abstracts the concept of logging.
# ConsoleLogger and FileLogger classes are implementations of the LoggerInterface.
# In other words, they provide a specific implemntation of the log method that prints and writes message to console and file respectively.
# ConsoleLogger and FileLogger aren't dependent on specific logging, but instead on the abstraction which is provided by Class LoggerInterface.

class LoggerInterface:
    def log(self, message: str):
        raise NotImplementedError

class ConsoleLogger(LoggerInterface):
    def log(self, message: str):
        print(message)

class FileLogger(LoggerInterface):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def log(self, message: str):
        with open(self.file_path, 'a') as file:
            file.write(message + '\n')

class Application:
    def __init__(self, logger: LoggerInterface):
        self.logger = logger

    def run(self):
        self.logger.log("Application is running")

    def process_event(self, event):
        self.logger.log(f"Processing event: {event}")

def main():

    # Usage
    logger = ConsoleLogger()  # FileLogger('app.log')
    app = Application(logger)
    app.run()
    app.process_event("Some event")

if __name__ == "__main__":
    main()
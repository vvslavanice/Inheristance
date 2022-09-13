from datetime import datetime


class CustomException(Exception):

    def __init__(self, utcerror=' Some custom error.'):
        self.utcerror = str(datetime.utcnow()) + utcerror
        with open('logs.txt', 'w') as fp:
            fp.write(self.utcerror)


if __name__ == '__main__':
    error = CustomException()
class HttpException(Exception):

    def __init__(self, http_code, info_msg=None, info_code=None):
        self.http_code = http_code
        self.info_code = info_code
        self.info_msg = info_msg
        super().__init__(f'[{self.http_code}-{str(self.info_code)}] {self.info_msg}')
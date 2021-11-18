import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    def write(self, chunk) -> None:
        return super().write(dict(status=200, data=chunk))
    
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        

    def response_write(self, data, is_error=False, status_code=200):
        self.write(data) if not is_error else self.write_error(
            status_code=status_code, exc_info='errors.')

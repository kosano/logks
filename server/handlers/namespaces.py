from handlers import BaseHandler
from utils.k8s import request_k8sapi


class NamespaceHandler(BaseHandler):
    def get(self):
        res = request_k8sapi('GET', '/api/v1/namespaces')
        namespaces = [ns['metadata']['name'] for ns in res['items']]
        self.response_write(namespaces)
        

from handlers import BaseHandler
from utils.k8s import request_k8sapi


class StatefulsetHandler(BaseHandler):
    def get(self, namespace):
        res = request_k8sapi('GET', '/apis/apps/v1/statefulsets')
        statefulsets = [ss['metadata']['name']
                        for ss in res['items'] if namespace == 'all' or ss['metadata']['namespace'] == namespace]
        self.response_write(statefulsets)

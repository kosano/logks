from handlers import BaseHandler
from utils.k8s import request_k8sapi


class DeploymentHandler(BaseHandler):
    def get(self, namespace):
        res = request_k8sapi('GET', '/apis/apps/v1/deployments')
        deployments = [dp['metadata']['name']
                       for dp in res['items'] if namespace == 'all' or dp['metadata']['namespace'] == namespace]
        self.response_write(deployments)

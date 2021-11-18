from settings import K8S_API, K8S_TOKEN
import logging
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger(__name__)


def request_k8sapi(method, path, *args, **kwargs):
    headers = {
        'Content-type': 'application/json',
        'Authorization': f'Bearer {K8S_TOKEN}'
    }
    req = dict(
        GET=requests.get,
        POST=requests.post,
        PUT=requests.put,
        PATCH=requests.patch,
    )[method](
        f'{K8S_API}{path}',
        headers=headers,
        verify=False,
        timeout=30,
        *args, **kwargs
    )
    logger.info(
        f'reuqest k8s api: {K8S_API}{path}, reponse status: {req.status_code}')
    return req.json()

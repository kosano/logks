import tornado.web
import tornado.ioloop
from handlers.namespaces import NamespaceHandler
from handlers.deployments import DeploymentHandler
from handlers.statefulsets import StatefulsetHandler

if __name__ == '__main__':
    
    app = tornado.web.Application([
        (r'/api/v1/namespaces', NamespaceHandler),
        (r'/api/v1/namespace/(?P<namespace>.+)/deployments', DeploymentHandler),
        (r'/api/v1/namespace/(?P<namespace>.+)/statefulsets', StatefulsetHandler),
    ])
    
    app.listen(8081)
    tornado.ioloop.IOLoop.current().start()
from pyramid.config import Configurator
from .db import init_db

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.include('.models')
        config.include('.routes')
        config.scan('.views')
    return config.make_wsgi_app()

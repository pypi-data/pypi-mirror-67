from pyramid.response import Response

from clld.interfaces import IOlacConfig
from clld.web.views.olac import OlacConfig, Participant, Institution


class MpgOlacConfig(OlacConfig):
    def admin(self, req):
        return Participant("Admin", 'Robert Forkel', 'forkel@shh.mpg.de')

    def description(self, req):
        res = OlacConfig.description(self, req)
        res['institution'] = Institution(
            'Max Planck Institute for the Science of Human History',
            'http://shh.mpg.de',
            'Jena, Germany')
        return res


def includeme(config):
    config.include('clld.web.app')
    config.registry.registerUtility(MpgOlacConfig(), IOlacConfig)
    config.add_static_view('clldmpg-static', 'clldmpg:static')
    config.add_settings({'clld.publisher_logo': 'clldmpg:static/minerva.png'})
    config.add_settings(
        {'clld.privacy_policy_url': 'https://www.shh.mpg.de/138116/privacy-policy'})
    config.add_route('google-site-verification', 'googlebbc8f4da1abdc58b.html')
    config.add_view(
        lambda r: Response('google-site-verification: googlebbc8f4da1abdc58b.html'),
        route_name='google-site-verification')

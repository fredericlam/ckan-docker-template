import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class CsuThemePlugin(plugins.SingletonPlugin):

    plugins.implements(plugins.IRoutes, inherit=True)
    def before_map(self, m):
        m.connect('elections', #name of path route
            '/elections', #url to map path to
            controller='ckanext.csu_theme.controller:ElectionsController', #controller
            action='elections') #controller action (method)
        return m

    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
            'csu_theme')

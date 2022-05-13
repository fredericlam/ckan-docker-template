import ckan.plugins as p
from ckan.lib.base import BaseController

class ElectionsController(BaseController):
    def elections(self):
        return p.toolkit.render('elections/index.html')
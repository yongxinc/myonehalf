from oscar.apps.catalogue.admin import *  # noqa
from mainsite.catalogue import models as catalogue_model

admin.site.register(catalogue_model.UNIQLOItem)
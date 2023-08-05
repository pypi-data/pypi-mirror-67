from django.contrib import admin

from irekua_database import models
from irekua_models import models as mmodels
from selia_admin.admin.types import EventTypeAdmin
from selia_admin.admin.types import TermTypeAdmin
from selia_admin.admin.types import AnnotationTypeAdmin
from selia_admin.admin.types import ItemTypeAdmin
from selia_admin.admin.terms import TermAdmin
from selia_admin.admin.terms import TagAdmin
from selia_admin.admin.user import UserAdmin
from selia_admin.admin.item import ItemAdmin
from selia_admin.admin.sampling_events import SamplingEventAdmin
from selia_admin.admin.sampling_events import SamplingEventDeviceAdmin
from selia_admin.admin.models import ModelAdmin
from selia_admin.admin.models import ModelVersionAdmin
from selia_admin.admin.models import ModelPredictionAdmin


@admin.register(
    models.Annotation,
    models.AnnotationTool,
    models.AnnotationVote,
    models.Collection,
    models.CollectionDevice,
    models.CollectionDeviceType,
    models.CollectionItemType,
    models.CollectionRole,
    models.CollectionSite,
    models.CollectionType,
    models.CollectionUser,
    models.Device,
    models.DeviceBrand,
    models.DeviceType,
    models.Entailment,
    models.EntailmentType,
    models.Institution,
    models.Licence,
    models.LicenceType,
    models.Locality,
    models.LocalityType,
    models.MetaCollection,
    models.MimeType,
    models.PhysicalDevice,
    models.Role,
    models.SamplingEventType,
    models.SamplingEventTypeDeviceType,
    models.SecondaryItem,
    models.Site,
    models.SiteDescriptor,
    models.SiteDescriptorType,
    models.SiteType,
    models.Source,
    models.Synonym,
    models.SynonymSuggestion,
    models.TermSuggestion,
    models.Visualizer,
)
class DatabaseAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.EventType, EventTypeAdmin)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Term, TermAdmin)
admin.site.register(models.TermType, TermTypeAdmin)
admin.site.register(models.AnnotationType, AnnotationTypeAdmin)
admin.site.register(models.ItemType, ItemTypeAdmin)
admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.SamplingEvent, SamplingEventAdmin)
admin.site.register(models.SamplingEventDevice, SamplingEventDeviceAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(mmodels.Model, ModelAdmin)
admin.site.register(mmodels.ModelVersion, ModelVersionAdmin)
admin.site.register(mmodels.ModelPrediction, ModelPredictionAdmin)

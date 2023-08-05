from django.contrib import admin

from irekua_database import models as irekua_database
from irekua_models import models as irekua_models
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
    irekua_database.Annotation,
    irekua_database.AnnotationTool,
    irekua_database.AnnotationVote,
    irekua_database.Collection,
    irekua_database.CollectionDevice,
    irekua_database.CollectionDeviceType,
    irekua_database.CollectionItemType,
    irekua_database.CollectionRole,
    irekua_database.CollectionSite,
    irekua_database.CollectionType,
    irekua_database.CollectionUser,
    irekua_database.Device,
    irekua_database.DeviceBrand,
    irekua_database.DeviceType,
    irekua_database.Entailment,
    irekua_database.EntailmentType,
    irekua_database.Institution,
    irekua_database.Licence,
    irekua_database.LicenceType,
    irekua_database.Locality,
    irekua_database.LocalityType,
    irekua_database.MetaCollection,
    irekua_database.MimeType,
    irekua_database.PhysicalDevice,
    irekua_database.Role,
    irekua_database.SamplingEventType,
    irekua_database.SamplingEventTypeDeviceType,
    irekua_database.SecondaryItem,
    irekua_database.Site,
    irekua_database.SiteDescriptor,
    irekua_database.SiteDescriptorType,
    irekua_database.SiteType,
    irekua_database.Source,
    irekua_database.Synonym,
    irekua_database.SynonymSuggestion,
    irekua_database.TermSuggestion,
    irekua_database.Visualizer,
)
class DatabaseAdmin(admin.ModelAdmin):
    pass


admin.site.register(irekua_database.EventType, EventTypeAdmin)
admin.site.register(irekua_database.User, UserAdmin)
admin.site.register(irekua_database.Term, TermAdmin)
admin.site.register(irekua_database.TermType, TermTypeAdmin)
admin.site.register(irekua_database.AnnotationType, AnnotationTypeAdmin)
admin.site.register(irekua_database.ItemType, ItemTypeAdmin)
admin.site.register(irekua_database.Item, ItemAdmin)
admin.site.register(irekua_database.SamplingEvent, SamplingEventAdmin)
admin.site.register(irekua_database.SamplingEventDevice, SamplingEventDeviceAdmin)
admin.site.register(irekua_database.Tag, TagAdmin)
admin.site.register(irekua_models.Model, ModelAdmin)
admin.site.register(irekua_models.ModelVersion, ModelVersionAdmin)
admin.site.register(irekua_models.ModelPrediction, ModelPredictionAdmin)

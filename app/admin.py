from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from app.models.work import Work, WorkCollection
from app.models.entity import Entity, EntityToEntityRel
from app.models.relations import EntityToWorkRel, WorkToCollection


class EntityAdmin(SimpleHistoryAdmin):
    list_display = ['id', '__str__', 'release_state']
    search_fields = ['full_name', 'alt_name']
    ordering = ['release_state', 'full_name', 'alt_name']


class WorkAdmin(SimpleHistoryAdmin):
    list_display = ['id', '__str__', 'release_state']
    search_fields = ['full_name', 'alt_name']
    ordering = ['release_state', 'full_name', 'alt_name']


class EntityToEntityRelAdmin(SimpleHistoryAdmin):
    list_display = ['id', '__str__', 'relationship']
    search_fields = [
        'from_entity__full_name',
        'from_entity__alt_name',
        'to_entity__full_name',
        'to_entity__alt_name',
        'relationship'
    ]
    ordering = ['relationship']


class EntityToWorkRelAdmin(SimpleHistoryAdmin):
    list_display = ['id', '__str__', 'relationship']
    search_fields = [
        'from_entity__full_name',
        'from_entity__alt_name',
        'to_work__full_name',
        'to_work__alt_name'
    ]
    ordering = ['relationship']


class WorkCollectionAdmin(SimpleHistoryAdmin):
    list_display = ['id', '__str__', 'release_state']
    search_fields = ['collection_name']
    ordering = ['release_state']


class WorkToCollectionRelAdmin(SimpleHistoryAdmin):
    list_display = ['id', '__str__']
    search_fields = ['from_work__ful_name', 'to_collection__collection_name']
    ordering = ['from_work__full_name', 'to_collection__collection_name']


admin.site.register(Entity, EntityAdmin)
admin.site.register(EntityToEntityRel, EntityToEntityRelAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(WorkCollection, WorkCollectionAdmin)
admin.site.register(EntityToWorkRel, EntityToWorkRelAdmin)
admin.site.register(WorkToCollection, WorkToCollectionRelAdmin)

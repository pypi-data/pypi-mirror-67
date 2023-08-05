from mongoengine import *

from spaceone.core.model.mongo_model import MongoModel


class ConfigMap(MongoModel):
    config_map_id = StringField(max_length=40, generate_id='config', unique=True)
    name = StringField(max_length=255, unique_with='domain_id')
    data = DictField()
    tags = DictField()
    domain_id = StringField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)

    meta = {
        'updatable_fields': [
            'name',
            'data',
            'tags'
        ],
        'exact_fields': [
            'config_map_id',
            'domain_id'
        ],
        'minimal_fields': [
            'config_map_id',
            'name'
        ],
        'ordering': [
            'name'
        ],
        'indexes': [
            'config_map_id',
            'domain_id'
        ]
    }

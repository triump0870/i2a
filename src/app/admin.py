from django.db.models.base import ModelBase
from django.contrib import admin
from app import models as app_models


for model_name in dir(app_models):
    model = getattr(app_models, model_name)
    if isinstance(model, ModelBase):
        admin.site.register(model)
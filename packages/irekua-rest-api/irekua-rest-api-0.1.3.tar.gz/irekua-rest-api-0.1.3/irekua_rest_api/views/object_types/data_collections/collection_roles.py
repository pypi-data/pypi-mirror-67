# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from irekua_database import models
from irekua_rest_api import serializers
from irekua_rest_api import utils


class CollectionTypeRoleViewSet(mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin,
                                utils.CustomViewSetMixin,
                                GenericViewSet):
    queryset = models.CollectionRole.objects.all()  # pylint: disable=E1101

    serializer_mapping = utils.SerializerMapping.from_module(
        serializers.object_types.data_collections.roles)

    permission_mapping = utils.PermissionMapping()

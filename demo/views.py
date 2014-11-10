from rest_framework import authentication, permissions, viewsets

from .models import Object
from .serializers import ObjectSerializer


class DefaultsMixin(object):                                                
    """Default settings for view authentication, permissions, filtering and pagination."""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    #paginate_by = 25
    #paginate_by_param = 'page_size'
    #max_paginate_by = 100


class ObjectViewSet(DefaultsMixin, viewsets.ModelViewSet):

    queryset = Object.objects.order_by('id')
    serializer_class = ObjectSerializer
    '''
    def get_queryset(self):
        queryset = Object.objects.exclude(dob=u'')
        return queryset
    '''

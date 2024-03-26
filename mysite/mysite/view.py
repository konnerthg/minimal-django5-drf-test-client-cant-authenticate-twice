import rest_framework.views
from rest_framework.response import Response


from rest_framework import permissions
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

import polls.models


class TestPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.has_perm('polls.can_publish')


class TestView(rest_framework.views.APIView):

    permission_classes = [TestPermission]

    def get(self, request):
        return Response(data={"foo": "bar"}, content_type="application/json")
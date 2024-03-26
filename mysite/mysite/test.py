import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission

from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from polls.models import Question


@pytest.fixture
def client() -> APIClient:
    """The test client.

    Note that this is DRF's test client, not django.test.client. They are different
    """
    return APIClient()


@pytest.mark.django_db
def test_authenticate(client):
    user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

    content_type = ContentType.objects.get_for_model(Question)

    permission = Permission.objects.create(
        codename="can_publish",
        name="Can Publish Posts",
        content_type=content_type,
    )

    client.force_authenticate(user=user)
    client.get("/test/")
    client.force_authenticate(user=None)

    user.user_permissions.add(permission)
    client.force_authenticate(user=user)

    response = client.get("/test/")
    assert response.json() == {"foo": "bar"}

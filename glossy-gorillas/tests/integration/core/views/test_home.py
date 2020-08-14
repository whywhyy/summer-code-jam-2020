import pytest
from django.shortcuts import reverse


@pytest.mark.django_db
def test_get_home_view_is_ok(client):
    response = client.get(reverse("home"))
    assert response.status_code == 200

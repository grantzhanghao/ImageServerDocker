from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views.mock_picture_view import MockPicture

urlpatterns = {
    url(r'^get_mock_graph$', MockPicture.as_view(), name="get_mock_graph"),
}

urlpatterns = format_suffix_patterns(urlpatterns)

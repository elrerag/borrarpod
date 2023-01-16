from django.urls import path


from .views import EntidadListView

app_name="entidad"

urlpatterns = [
    path("", EntidadListView.as_view(), name="entidad_list"),
]

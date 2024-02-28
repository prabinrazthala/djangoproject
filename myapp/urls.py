from django.urls import path
from .views import root_page, temp_inherit_home,portfolio,classroom,student

urlpatterns = [
    path('temp-inherit-home/', temp_inherit_home, name="temp_inherit_home"),
    path('portfolio/', portfolio, name="portfolio"),
    path('',root_page, name='root_page'),
    path('classroom/', classroom, name="classroom"),
    path('student', student, name="student")
]

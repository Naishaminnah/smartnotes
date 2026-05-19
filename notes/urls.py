from django.urls import path
from . import views

urlpatterns=[
    path('',views.note_list, name="note_list"),
    path('create/',views.create_notes, name="create_note_form"),
    path('delete/<int:id>/',views.delete_note,name="delete_note"),
    path('edit/<int:id>/',views.edit_note, name="edit_note"),
    path('login/',views.login_view, name="login"),
    path('signup/',views.signup_view, name="signup"),
    path('logout/',views.logout_view,name="logout")
] 
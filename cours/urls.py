from django.urls import path 
from .views import CourseListView, CourseDetailView,\
CourseCreateView, CouseUpdateView, CourseDeleteView,\
    FCourseListView, FCoursDetailView, FCourseCreateView, FCourseUpdateView, FCourseDeleteView, test_task, test_task_result
app_name = 'cours'
urlpatterns = [
    # path('list/', CourseListView.as_view(), name='cours-list'),
    path('list/', FCourseListView.as_view(), name='cours-list'),
    # path('detail/<int:pk>/', CourseDetailView.as_view(), name='cours-detail'),
    path('detail/<int:pk>/', FCoursDetailView.as_view(), name='cours-detail'),
    # path('create/', CourseCreateView.as_view(), name='cours-create'),
    path('create/', FCourseCreateView.as_view(), name='cours-create'),
    # path('update/<int:pk>/', CouseUpdateView.as_view(), name='cours-update'),
    path('update/<int:pk>/', FCourseUpdateView.as_view(), name='cours-update'),
    # path('delete/<int:pk>/', CourseDeleteView.as_view(), name='cours-delete'),
    path('delete/<int:pk>/', FCourseDeleteView.as_view(), name='cours-delete'),
    path('test/', test_task, name='test-task'),
    path('test/<str:task_id>/', test_task_result, name='test_task_result')
]

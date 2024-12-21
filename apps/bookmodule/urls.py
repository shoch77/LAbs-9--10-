"""
URL configuration for libraryproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from apps.bookmodule import views

# urlpatterns = [     
#     path('', views.index),
#     path('index2/<int:val1>/', views.index2),
#     path('<int:bookId>', views.viewbook)
# ]

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links),
    path('html5/text/formatting/', views.formatting),
    path('html5/listing/', views.listing),
    path('html5/tables/', views.tables),
    path('search/', views.search),
    path('simple/query', views.simple_query),
    path('lookup/query/', views.lookup_query),
    path('lab8/task1/', views.task1),
    path('lab8/task2/', views.task2),
    path('lab8/task3/', views.task3),
    path('lab8/task4/', views.task4),
    path('lab8/task5/', views.task5),
    path('lab9_part1/listbooks/', views.list_books, name='list_books'),
    path('lab9_part1/addbook/', views.add_book, name='add_book1'),
    path('lab9_part1/editbook/<int:id>/', views.edit_book, name='edit_book1'),
    path('lab9_part1/deletebook/<int:id>/', views.delete_book, name='delete_book'),
    path('lab9_part2/addbookforms/', views.add_bookforms, name='add_book2'),
    path('lab9_part2/editbookforms/<int:id>/', views.edit_bookforms, name='edit_book2'),
    path('list/', views.list_students, name='list_students'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('add_address/', views.add_address, name='add_address'),
    #  path('students2/', views.list_students2, name='list_students2'),
    # path('students2/add/', views.add_student2, name='add_student2'),
    # path('students2/update/<int:id>/', views.update_student2, name='update_student2'),
    # path('students2/delete/<int:id>/', views.delete_student2, name='delete_student2'),
    path('upload/', views.upload_image, name='upload_image'),


]


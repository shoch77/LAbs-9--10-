from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from django.db.models import Count, Min, Max, Sum, Avg

from .forms import *


# def index(request):
#     name = request.GET.get("name") or "world!" 
#     return render(request, "bookmodule/index.html", {"name": name})

# def index2(request, val1):   
#     #add the view function (index2)     
#     return HttpResponse("value1 = "+ str(val1))
 
# def viewbook(request, bookId):    
#     # assume that we have the following books somewhere (e.g. database)
#     book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}     
#     book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}     
#     targetBook = None     
#     if book1['id'] == bookId: targetBook = book1     
#     if book2['id'] == bookId: targetBook = book2     
#     context = {'book':targetBook} # book is the variable name accessible by the template     
#     return render(request, 'bookmodule/show.html', context) 

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, 'bookmodule/links.html')

def formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')

def search(request):
    if request.method == "POST":         
        string = request.POST.get('keyword').lower()         
        isTitle = request.POST.get('option1')         
        isAuthor = request.POST.get('option2')      
           
        # now filter         
        books = __getBooksList()         
        newBooks = []         
        for item in books:             
            contained = False             
            if isTitle and string in item['title'].lower(): 
                contained = True             
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            if contained: 
                newBooks.append(item)         
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request, 'bookmodule/search.html', {})

def __getBooksList():     
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}     
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}     
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}     
    return [book1, book2, book3]

def simple_query(request):     
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects     
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})


def lookup_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:         
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})     
    else:         
        return render(request, 'bookmodule/index.html')

def task1(request):
    books = Book.objects.filter(Q(price__lte = 50))
    return render(request, 'bookmodule/task1.html', {'books': books})

def task2(request):
    books = Book.objects.filter(Q(edition__gt = 2) & (Q(title__icontains = 'qu') | Q(author__icontains = 'qu')))
    return render(request, 'bookmodule/task2.html', {'books': books})

def task3(request):
    books = Book.objects.filter(~Q(edition__gt = 2) & (~Q(title__icontains = 'qu') | ~Q(author__icontains = 'qu')))
    return render(request, 'bookmodule/task3.html', {'books': books})

def task4(request):
    books = Book.objects.order_by('title')
    return render(request, 'bookmodule/task4.html', {'books': books})

def task5(request):
    query = Book.objects.aggregate(
        count=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        min_price=Min('price'),
        max_price=Max('price')
    )
    return render(request, 'bookmodule/task5.html', {'query': query})


#######################################
def list_books(request):
    books = Book.objects.all() 
    print(books)
    return render(request, 'bookmodule/listbooks.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        edition = request.POST['edition']
        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return redirect('list_books')
    return render(request, 'bookmodule/add_book.html')


def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.edition = request.POST['edition']
        book.save()
        return redirect('list_books')
    return render(request, 'bookmodule/edit_book.html', {'book': book})

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('list_books')


def add_bookforms(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'bookmodule/add_bookforms.html', {'form': form})

def edit_bookforms(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/edit_bookforms.html', {'form': form})


#####################################

def list_students(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/list_students.html', {'students': students})

# # Add a new student
# def add_student(request):
#     if request.method == 'POST':
#         student_form = StudentForm(request.POST)
#         address_form = AddressForm(request.POST)
#         if student_form.is_valid() and address_form.is_valid():
#             address = address_form.save()
#             student = student_form.save(commit=False)
#             student.address = address
#             student.save()
#             return redirect('list_students')
#     else:
#         student_form = StudentForm()
#         address_form = AddressForm()
#     return render(request, 'bookmodule/add_student.html', {'student_form': student_form, 'address_form': address_form})

# # Edit a student
# def edit_student(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
#     address = student.address
#     if request.method == 'POST':
#         student_form = StudentForm(request.POST, instance=student)
#         address_form = AddressForm(request.POST, instance=address)
#         if student_form.is_valid() and address_form.is_valid():
#             student_form.save()
#             address_form.save()
#             return redirect('list_students')
#     else:
#         student_form = StudentForm(instance=student)
#         address_form = AddressForm(instance=address)
#     return render(request, 'bookmodule/edit_student.html', {'student_form': student_form, 'address_form': address_form})

# Delete a student
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('list_students')

# Add an address
def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = AddressForm()
    return render(request, 'bookmodule/add_address.html', {'form': form})


###############################

# List Students2 with their addresses
def list_students2(request):
    students = Student2.objects.prefetch_related('addresses').all()
    return render(request, 'students2/list_students2.html', {'students': students})

# Add a new student2 with addresses
def add_student2(request):
    if request.method == 'POST':
        student_form = Student2Form(request.POST)
        address_form = Address2Form(request.POST)
        if student_form.is_valid() and address_form.is_valid():
            # Save the new address first
            address = address_form.save()
            # Save the student and associate the address
            student = student_form.save()
            student.addresses.add(address)  # Add the address to the many-to-many relationship
            return redirect('list_students2')
    else:
        student_form = Student2Form()
        address_form = Address2Form()
    return render(request, 'students2/add_student2.html', {
        'student_form': student_form,
        'address_form': address_form
    })

# Update student2 and addresses
def update_student2(request, id):
    student = get_object_or_404(Student2, id=id)
    if request.method == 'POST':
        student_form = Student2Form(request.POST, instance=student)
        if student_form.is_valid():
            student_form.save()
            return redirect('list_students2')
    else:
        student_form = Student2Form(instance=student)
    return render(request, 'students2/update_student2.html', {'student_form': student_form})

# Delete student2
def delete_student2(request, id):
    student = get_object_or_404(Student2, id=id)
    student.delete()
    return redirect('list_students2')
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'usermodule/add_student.html', {'form': form})

######################## Lab 10 

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'usermodule/edit_student.html', {'form': form})


################## Lab 10 Task 3

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_image')
    else:
        form = ImageForm()
    return render(request, 'bookmodule/upload_image.html', {'form': form})
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from myApp.models import Book

# Create your views here.


def index(request):
    return HttpResponse('Hello, World!')


def detail(request):
    '''返回图书列表'''
    book_list = Book.objects.order_by('-pub_date')[:5]
    context = {'book_list': book_list}
    return render(request, 'myApp/detail.html', context)


def addBook(request):
    '''添加书籍'''
    if request.method == 'POST':
        temp_id = request.POST['id']
        temp_name = request.POST['name']
        temp_author = request.POST['author']
        temp_pub_house = request.POST['pub_house']
    if temp_id == '':  # 新增
        temp_book = Book(name=temp_name, author=temp_author, pub_house=temp_pub_house, pub_date=timezone.now())
        temp_book.save()
    else:  # 修改
        Book.objects.filter(id=temp_id).update(name=temp_name, author=temp_author, pub_house=temp_pub_house, pub_date=timezone.now())
    # 重定向
    return HttpResponseRedirect(reverse('detail'))


def deleteBook(request, book_id):
    '''删除书籍'''
    bookID = book_id
    Book.objects.filter(id=bookID).delete()
    # 重定向
    return HttpResponseRedirect(reverse('detail'))


def getBook(request, book_id):
    '''获取指定的书籍'''
    book = Book.objects.get(id=book_id)
    book = {'book': book}
    return render(request, 'myApp/detail.html', book)

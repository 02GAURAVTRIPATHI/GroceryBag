from django.shortcuts import render
from .models import ListModel
from dateutil.parser import parse
# Create your views here.
def home_page_view(request):
    #print(request.POST.dict().get('item'))
    if request.method == "POST":
       item = request.POST.dict()['item']
       quantity = request.POST.dict()['quantity']
       status = request.POST.dict()['status']
       date =  request.POST.dict()['date']
       date = parse(date)
       ListModel.objects.create(user_id=request.user, item_name=item, quantity=quantity, action=status, created_at=date)
    return render(request, 'testapp/HTML/add.html')
def home1_page_view(request):
    items = ListModel.objects.filter(user_id=request.user)
    if request.method == "POST":
        date =  request.POST.dict().get('filter')
        if date:
            date = parse(date)
            items = ListModel.objects.filter(user_id=request.user, created_at=date)
    return render(request, 'testapp/HTML/index.html', {'items':items})
def home2_page_view(request,id):
    if request.method == "POST":
       item = request.POST.dict()['item']
       quantity = request.POST.dict()['quantity']
       status = request.POST.dict()['status']
       date =  request.POST.dict()['date']
       date = parse(date)
       ListModel.objects.filter(id=id).update(item_name=item, quantity=quantity, action=status, created_at=date)
    item = ListModel.objects.get(id=id)
    return render(request, 'testapp/HTML/update.html', {'item':item})

from django.shortcuts import redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
           user = form.save()
           login(request, user)
           messages.success(request, "Registration successful." )
           return redirect("/accounts/login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="testapp/HTML/register.html", context={"register_form":form})
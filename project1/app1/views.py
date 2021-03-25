from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import foodModel,CustomerModel,OrderModel
# Create your views here.
def adminloginview(request):
    return render(request, "app1/adminlogin.html")

def authenticateadmin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username = username,password = password)

    if user is not None:
        login(request, user)
        return redirect('adminhomepage')


    if user is None:
        messages.add_message(request,messages.ERROR, "invalid credentials")
        return redirect('adminloginpage')

def adminhomepageview(request):
    if not request.user.is_authenticated:
        return redirect('adminloginpage')
    context = {'FoodItems': foodModel.objects.all()}
    return render(request,"app1/adminhomepage.html",context)

def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')

def addfood(request):
    name = request.POST['food']
    price = request.POST['price']
    foodModel(name = name, price = price).save()
    return redirect('adminhomepage')
def deletefood(request,foodpk):
    foodModel.objects.filter(id = foodpk).delete()
    return redirect('adminhomepage')

def homepageview(request):
    return render(request,"app1/homepage.html")

def signupuser(request):
    username = request.POST['username']
    password = request.POST['password']
    phoneno = request.POST['phoneno']
    #if user already exist
    if User.objects.filter(username = username).exists():
        messages.add_message(request,messages.ERROR,"user already exist")
        return redirect('homepage')

    #if user doesnt exist, everything is fine to create a user
    User.objects.create_user(username = username,password=password).save()
    lastobject = len(User.objects.all())-1
    CustomerModel(userid = User.objects.all()[int(lastobject)].id,phoneno = phoneno).save()
    messages.add_message(request,messages.ERROR,"user successfully created")
    return redirect('homepage')

def userloginview(request):
    return render(request,"app1/userlogin.html")

def authenticateuser(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username = username,password = password)

    if user is not None:
        login(request, user)
        return redirect('customerhomepage')


    if user is None:
        messages.add_message(request,messages.ERROR, "invalid credentials")
        return redirect('userloginpage')

def customerhomepageview(request):
    if not request.user.is_authenticated:
        return redirect('homepage')
    username = request.user.username
    context = {'username' : username, 'foodItems': foodModel.objects.all()}
    return render(request,'app1/customerhomepage.html',context)

def userlogout(request):
    logout(request)
    return redirect('homepage')

def placeorder(request):
    if not request.user.is_authenticated:
        return redirect('homepage')
    context = OrderModel()
    username = request.user.username
    # phone_no = CustomerModel.objects.get(phoneno)
    field_name = 'phoneno'
    obj = CustomerModel.objects.first()
    field_object = CustomerModel._meta.get_field(field_name)
    field_value = field_object.value_from_object(obj)
    # phoneno = CustomerModel.objects.filter(userid = request.user.id)#[0].phoneno
    address = request.POST['address']
    ordereditems = ""


    for food in foodModel.objects.all():
        foodid = food.id
        name = food.name
        price = food.price
        quantity = request.POST.get(str(foodid)," ")
        if str(quantity) != '0' and str(quantity) != " ":
            ordereditems = ordereditems + name + " "+"Amount"+" "+ str(int(quantity)*int(price)) + " "+"quantity : "+quantity + ";"+" "
    context.username = username
    context.phoneno = field_value
    context.address = address
    context.orderitems = ordereditems
    context.save()
    # OrderModel(username = username,phoneno = phoneno, address = address, orderitems = ordereditems).save()
    messages.add_message(request,messages.ERROR, "Order Successfully Placed")
    return redirect('customerhomepage')

def userorders(request):
    if not request.user.is_authenticated:
        return redirect('homepage')
    orders = OrderModel.objects.filter(username = request.user.username)
    context = {'orders': orders}
    return render(request,'app1/userorders.html',context)

def adminorders(request):
    if not request.user.is_authenticated:
        return redirect('adminloginpage')
    orders = OrderModel.objects.all()
    context = {'orders': orders}
    return render(request,"app1/adminorders.html",context)

def acceptorder(request,orderpk):
    order = OrderModel.objects.filter(id = orderpk)[0]
    order.orderstatus = "accepted"
    order.save()
    return redirect(request.META['HTTP_REFERER'])

def declineorder(request,orderpk):
    order = OrderModel.objects.filter(id = orderpk)[0]
    order.orderstatus = "declined"
    order.save()
    return redirect(request.META['HTTP_REFERER'])



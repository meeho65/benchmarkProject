from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from .models import MobileProducts,LaptopProducts,SmartWatchProducts,Review
from django.contrib.auth import update_session_auth_hash
import random
# Create your views here.

def one_prod_Page(request, product_name,type):

    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        content = request.POST.get('content')
        rating = request.POST.get('rating')
        product_type = request.POST.get('product_type')
        product_id = request.POST.get('product_id')
        reviews = Review(user_name=user_name, content=content, rating=rating, product_type=product_type,product_id=product_id)
        reviews.save()

    data = get_product_data(type, product_name)
    return render(request, 'one_prod.html',data)

def HomePage(request):
    mobiles=MobileProducts.objects.all()
    laptops=LaptopProducts.objects.all()
    watches=SmartWatchProducts.objects.all()
    random_mobiles = random.sample(list(mobiles), min(3, len(mobiles)))
    random_laptops = random.sample(list(laptops), min(3, len(laptops)))
    random_watches = random.sample(list(watches), min(3, len(watches)))
    #random_laptops = random.sample(list(laptops), 3)
    #random_watches = random.sample(list(watches), 3)
    data={'product': random_mobiles,
          'laptopproduct': random_laptops,
          'watches':random_watches}
    return render(request, 'home.html',data)


from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def SignUp(request):
    data = {'msg': 'already have an account.', 'color': 'white'}

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confpassword = request.POST.get('password2')

        if password != confpassword:
            data = {'msg': "confirm password isn't the same ", 'color': '#ff2c2c'}
        else:
            # Create user without saving yet
            my_user = User(username=username, email=email, first_name=fname, last_name=lname)
            my_user.set_password(password)
            my_user.save()
            
            return redirect('login')

    return render(request, 'signup.html', data)

def LogIn(request):
    data={'msg':'already have account.',
          'color':'white'}
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            data={'msg':"password or username isn't correct",
          'color':'#ff2c2c'}

    return render(request, 'login.html',data)


from django.shortcuts import render

def CompPage(request):
    # Retrieve the selected product names from the request
    first_product_name = request.GET.get('first_product_name', '')
    second_product_name = request.GET.get('2ndproduct', '')
    type = request.GET.get('type', '')
    data = get_product_data(type, first_product_name)
    data2 = get_product_data(type, second_product_name)
    context = {
        'data': data,
        'data2': data2,
    }

    return render(request, 'compare.html', context)


def get_product_data(type, product_name):
    if type == 'mobile':
        product = get_object_or_404(MobileProducts, product_name=product_name)
        fields = { 
            'f1': product.product_screen_size,
            'f2': product.product_chipset,
            'f3': product.product_gpu,
            'f4': product.product_battery,
            'f5': product.product_ram_storage,
            'f6': product.product_main_camera,
            'f7': product.product_front_camera, 
            'f8': product.product_sim_support,
            'f9': product.product_fast_charging,
        }
        random_product = random.sample(list(MobileProducts.objects.all()), min(4, len(MobileProducts.objects.all())))
    elif type == 'laptop':
        product = get_object_or_404(LaptopProducts, product_name=product_name)
        fields = { 
            'f1': product.product_processor,
            'f2': product.product_gpu, 
            'f3': product.product_ram,
            'f4': product.product_storage,
            'f5': product.product_battery,
            'f6': product.product_display,               
        }
        random_product = random.sample(list(LaptopProducts.objects.all()), min(4, len(LaptopProducts.objects.all())))
    elif type == 'watch':
        product = get_object_or_404(SmartWatchProducts, product_name=product_name)
        fields = { 
            'f1': product.product_water_resistant,
            'f2': product.product_sensor,
            'f3': product.product_charger_type,
            'f4': product.product_battery_life,
            'f5': product.product_storage,
            'f6': product.product_display,
        }
        random_product = random.sample(list(SmartWatchProducts.objects.all()), min(4, len(SmartWatchProducts.objects.all())))

    data = {
        'product': product,
        'field': fields,
        'rando': random_product,
        'type': type
    }

    return data

def Profile(request):
    return render(request, 'profile.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

@login_required
def ProfileUpdate(request):
    if request.method == 'POST':
        previous_password = request.POST.get('previous_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')

        user = request.user

        # Check if the entered previous password is correct
        if not user.check_password(previous_password):
            messages.error(request, 'Incorrect previous password.')
        elif new_password != confirm_new_password:
            messages.error(request, 'New password and confirm new password do not match.')
        else:
            # Update the user's password and refresh the session
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            
            messages.success(request, 'Password changed successfully.')
            return redirect('profile_update')  # Redirect to the same page or another page if needed

    return render(request, 'profile_update.html')


@login_required
def ProfileUpdate2(request):
    if request.method == 'POST':
        # Get form data from the submitted POST request
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')

        # Update user profile with the new information
        user = request.user
        user.first_name = fname
        user.last_name = lname
        user.username = username
        user.email = email
        user.save()

        return redirect('profile')  # Redirect to the same page or another page if needed

    return render(request, 'profile_update2.html')

def BookMark(request):
    return render(request ,'bookmark.html')

def Reviews(request):
    review=Review.objects.all()
    for a in review:
         print(review)
    print('abbdyhbc')
    return render(request,'review.html',{'reviews': review})

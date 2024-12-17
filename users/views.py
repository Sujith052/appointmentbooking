from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from users.models import *

# Create your views here.
def index(request):
    return render(request,"index.html")

def signin(request):
    return render(request,"signin.html")

def signup(request):
    return render(request,"signup.html")

def signup_action(request):
    if request.method=="POST":
        try:
            name=request.POST.get('name') 
            email=request.POST.get('email') 
            contact=request.POST.get('contactno')
            username=request.POST.get('username')
            password=request.POST.get('password') 
            
            # Check the already exist of email and contact
            if userdata.objects.filter(email=email,contactno=contact).exists():
                messages.success(request,'User Already Exist!')
                return render(request,"signup.html")
            
            # Create a new Login entry for the user
            user_obj = userdata()
            user_obj.name = name
            user_obj.email = email  
            user_obj.contactno = contact 
            user_obj.username = username 
            user_obj.password = password 
            user_obj.save() 
        
            return redirect('signin')
        except Exception as e:
            # Log the error if needed and return a generic error message
            print(f"Error while register User: {str(e)}")
            return render(request, "signup.html", {'error_message': 'An error occurred while register User. Please try again.'})
        
def signin_action(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user with given username and password exists
        if userdata.objects.filter(username=username, password=password).exists():
            # Set session variables for login
            loginobj = userdata.objects.get(username=username)
            request.session['loginid'] = loginobj.id
            return redirect('index')   
        else:
            # If username or password is incorrect
            messages.success(request,'Invalid username or password!')
            return render(request, 'signin.html')
    
    return render(request, 'signup.html')

def appointment(request):
    appointment=appointment_time.objects.all()
    return render(request,"appointment.html",{"appointment_time":appointment})

def gettimeslot(request):
    appointmentid = request.POST.get('appointmentid')
    appointment_slots = time_slot.objects.filter(appointment_time=appointmentid).values()
    return JsonResponse(list(appointment_slots), safe=False)

def appointment_action(request):
    if request.method=="POST":
        try:
            loginid=request.session['loginid']
            name=request.POST.get('name') 
            contact=request.POST.get('contactno')
            date=request.POST.get('date') 
            appointment_time=request.POST.get('appointment_time') 
            boking_status="Slot Booked"
            
            # Check the already exist of email and contact
            if appointmentbooking.objects.filter(date=date,selected_slote=appointment_time,user=loginid).exists():
                print("hello")
                messages.success(request,'Selected date and slote already booked!')
                return render(request,"index.html")
            
            # Create a new Login entry for the user
            app_obj = appointmentbooking()
            app_obj.name = name
            app_obj.phone_number = contact  
            app_obj.date = date 
            app_obj.selected_slote = time_slot.objects.get(id=appointment_time)
            app_obj.user = userdata.objects.get(id=loginid)
            app_obj.booking_status=boking_status
            app_obj.save() 
        
            return redirect('booking_details')
        except Exception as e:
            # Log the error if needed and return a generic error message
            print(f"Error while register User: {str(e)}")
            return render(request, "appointment.html", {'error_message': 'An error occurred while register User. Please try again.'})

def booking_details(request):
    bookings=appointmentbooking.objects.select_related("selected_slote")
    return render(request,"booking_details.html",{"booked_slots":bookings})

def user_logout(request):
    request.session.flush() 
    return redirect("signin")
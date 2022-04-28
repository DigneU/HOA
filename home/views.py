import email
from email import message
from multiprocessing import context
from pyexpat import model
from re import template
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from .models import Page, Contact, Room, Booking
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

app_name = 'home'
# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"

class LodgePageView(TemplateView):
    template_name = "lodge.html"

class BookingListView(ListView):
    model = Booking
    template_name = "booking_list_view.html"

def home(request):
    slider= Page.objects.all().filter(category='slider').order_by('-id')[:1]
    welcome =Page.objects.all().filter(category='welcome').order_by('-id')[:1]
    homebody =Page.objects.all().filter(category='homebody').order_by('-id')[:1]
    context={
        'contents':slider,
        'welcome':welcome,
        'homebody':homebody,
    }
    return render(request, 'index.html',context)

def room(request):
    room = Room.objects.all()[0]
    return render(request, 'room_list.html')

def index(request):
    return render(request, 'index.html')

def contact_create(request):
    if request.method =='POST':
        if request.POST.get("name") and request.POST.get("email") and request.POST.get("subject"):
            cont= Contact()
            cont.name = request.POST.get("name") 
            cont.email = request.POST.get("email") 
            cont.content = request.POST.get("subject") 
            cont.save()
            #messages.success(request, f"{message.uname} Your Message sent")
            subjec ='Comments or Inquires'
            messag = f'{cont.name} said: '
            messag += cont.content
            from_emai = cont.email
            to_emai = [settings.EMAIL_HOST_USER, 'director@heartofafricalodge.com','ephata@heartofafricalodge.com','jackson@heartofafricalodge.com']

            send_mail(subject=subjec,message=messag,from_email=from_emai,recipient_list=to_emai,fail_silently=False)
            return render(request, 'index.html')
            
        else:

            return render(request, 'index.html')
    return render(request, 'index.html')



def about_create(request):
    if request.method =='POST':
        if request.POST.get("name") and request.POST.get("email") and request.POST.get("subject"):
            cont= Contact()
            cont.name = request.POST.get("name") 
            cont.email = request.POST.get("email") 
            cont.content = request.POST.get("subject") 
            cont.save()
           #messages.success(request, f"{message.uname} Your Message sent")
            subjec ='Comments or Inquires'
            messag = f'{cont.name} said: '
            messag += cont.content
            from_emai = cont.email
            to_emai = [settings.EMAIL_HOST_USER, 'director@heartofafricalodge.com','ephata@heartofafricalodge.com','jackson@heartofafricalodge.com']

            send_mail(subject=subjec,message=messag,from_email=from_emai,recipient_list=to_emai,fail_silently=False)
            return render(request, 'about.html')       
        else:
            return render(request, 'about.html')
    return render(request, 'about.html')

def booking_create(request):
    if request.method =='POST':
        
        user_name = request.POST["name"]
        user_email = request.POST["email"]
        user_phone = request.POST["phone"]
        room = request.POST["roomn"]
        rooms = request.POST["rooms"]
        adults = request.POST["adults"]
        children = request.POST["children"]
        check_in = request.POST["checkin"]
        check_out = request.POST["checkout"]
        # selecting room instance
        roomid= Room.objects.get(id=room)
        insert = Booking(user_name=user_name, user_email=user_email, user_phone=user_phone, room=roomid, rooms=rooms, adults=adults, children=children, check_in=check_in, check_out=check_out)
        insert.save()
        #messages.success(request, f"{message.uname} Your Message sent")
        subjec ='Room Booking at Heart Of Africa Lodge'
        messag = f'Thank you for booking with Heart of Africa Lodge.'
        messag += f'\nYou have booked {roomid} from {check_in} to {check_out}'
        messag += f'\nTo cancel the booking please contact us via email or our phone number.\n We welcome you to the Heart of Africa Lodge.\n Karibuni Wote'
        from_emai = settings.EMAIL_HOST_USER
        to_emai = user_email
        
        # message for the lodge about booking made
        subjec2 =  'New Booking Done'
        messag2 = f'{user_name} booked {roomid} for {adults} and {children}\nFrom {check_in} To {check_out}'
        from_use2 = user_email
        to_rec2 = ['director@heartofafricalodge.com','leanne@heartofafricalodge.com','jackson@heartofafricalodge.com','ephata@heartofafricalodge.com']
        send_mail(subject=subjec,message=messag,from_email=from_emai,recipient_list=[str(to_emai)],fail_silently=False)
        send_mail(subject=subjec2,message=messag2,from_email=from_use2,recipient_list=to_rec2,fail_silently=False)
        messages.success(request, 'Booking request submitted successfully.')
        return render( request, 'index.html')
        
    return render(request, 'room_list.html')

def lodge(request):
    return render(request, 'lodge.html')

def services(request):
    return render(request, 'services.html')

def camping(request):
    return render(request, 'camping.html')

def about(request):
    return render(request, 'about.html')

def roomlist(request):
    rooms = Room.objects.all()
    context={
        'room':rooms
    }
    return render(request, 'room_list.html', context)

def booking(request, nameroom, roomprice):
    room_category = Room.objects.get(name=nameroom)
    room_price = Room.objects.get(price=roomprice)
    context={
        'roomchecked':room_category,
        'roomprice':room_price
    }
    return render(request, 'checkout.html' , context)

class RoomList(ListView):
    model = Room

class BookingList(ListView):
    model = Booking


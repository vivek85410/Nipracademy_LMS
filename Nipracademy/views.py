from django.shortcuts import render,HttpResponse, redirect
from Nipracademy.models import Course ,Video, UserCourse, Payment,Comment,contact,OfflineAddress,Faculties,Homepage_image
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout , login 
from django.core.mail import send_mail
from Nipracademy.forms import CommentForm
from .forms import RegistrationForm , LoginForm,CommentForm
from django.views.generic import (TemplateView, DetailView,ListView,FormView,CreateView,UpdateView,DeleteView)
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from LMS.settings import *
from time import time
import razorpay
from razorpay import utility,resources
from django.contrib import messages
from django.http import HttpResponseRedirect

# base page view function
def base(request):
    return render(request,"Nipracademy/base.html")

# About Us page view function
def About_us(request):
    return render(request,"Nipracademy/About_us.html")

@csrf_exempt
def Allcourses(request):
    courseslist = Course.objects.filter(active=True)
    select_duration = request.GET.get('duration',None)

    if select_duration:
        try:
            duration = int(select_duration)
            courseslist = courseslist.filter(duration=duration)
        except ValueError:
            pass
    context = {'courseslist':courseslist}
    return render(request,"Nipracademy/allcourses.html",context)

# Homepage view function
def Homepage(request):
    try:
        home_image=Homepage_image.objects.all()
        courselist = Course.objects.all()[:4]
        context={'home_image':home_image,
                 'courselist':courselist}
        return render(request,"Nipracademy/home.html",context)
    except:
        return HttpResponse("<h1> Oops! Something went wrong!.</h1> 500 Internal Server Error .")
  
# Mycourse Page view function
class MyCoursesList(ListView):
    template_name = 'Nipracademy/my_courses.html'
    context_object_name = 'user_courses'
    def get_queryset(self):
        return UserCourse.objects.filter(user = self.request.user)
    
# Signup page view function
class SignupView(FormView):
    template_name="Nipracademy/signup.html" 
    form_class = RegistrationForm
    success_url  = '/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
# Login page View function
class LoginView(FormView):
    template_name="Nipracademy/login.html" 
    form_class = LoginForm
    success_url  = '/'

    def form_valid(self, form):
        login(self.request , form.cleaned_data)
        next_page = self.request.GET.get('next')
        if next_page is not None:
            return redirect(next_page)
        return super().form_valid(form)
    
# Signout option view function
def signout(request ):
    logout(request)
    return redirect("home")

# Payment view function
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
@login_required(login_url='/login')
def checkout(request , slug):
    course = Course.objects.get(slug  = slug)
    user = request.user
    action = request.GET.get('action')
    order = None
    payment = None
    error = None
    try:
        user_course = UserCourse.objects.get(user = user  , course = course)
        error = "You are Already Enrolled in this Course"
    except:
        pass
    amount=None
    if error is None : 
        amount =  int((course.price - ( course.price * course.discount * 0.01 )) * 100)
   # if amount is zero don't create payment , only save enrollment object 
    
    if amount==0:
        userCourse = UserCourse(user = user , course = course)
        userCourse.save()
        return redirect('my-courses')   
                # enroll direct
    if action == 'create_payment':

            currency = "INR"
            notes = {
                "email" : user.email, 
                "name" : f'{user.first_name} {user.last_name}'
            }
            reciept = f"Nipracademy-{int(time())}"
            order = client.order.create(
                {'receipt' :reciept , 
                'notes' : notes , 
                'amount' : amount ,
                'currency' : currency
                }
            )

            payment = Payment()
            payment.user  = user
            payment.course = course
            payment.order_id = order.get('id')
            payment.save()


    
    context = {
        "course" : course , 
        "order" : order, 
        "payment" : payment, 
        "user" : user , 
        "error" : error
    }
    return  render(request , template_name="Nipracademy/check_out.html" , context=context )    

#Payment Verification view function
@login_required(login_url='/login')
@csrf_exempt
def verifyPayment(request):
    if request.method == "POST":
        data = request.POST
        context = {}
        print(data)
        try:
            client.utility.verify_payment_signature(data)
            razorpay_order_id = data['razorpay_order_id']
            razorpay_payment_id = data['razorpay_payment_id']

            payment = Payment.objects.get(order_id = razorpay_order_id)
            payment.payment_id  = razorpay_payment_id
            payment.status =  True
            
            userCourse = UserCourse(user = payment.user , course = payment.course)
            userCourse.save()

            print("UserCourse" ,  userCourse.id)

            payment.user_course = userCourse
            payment.save()

            return render(request,template_name="Nipracademy/reciept.html")   

        except:
            return HttpResponse("Payment Failed")
        
        
 
# Course page view function
def coursePage(request , slug):
    course = Course.objects.get(slug  = slug)
    serial_number  = request.GET.get('lecture')
    videos = course.video_set.all().order_by("serial_number")


    if serial_number is None:
        serial_number = 1 

    video = Video.objects.get(serial_number = serial_number , course = course)

    if (video.is_preview is False):

        if request.user.is_authenticated is False:
            return redirect("login")
        else:
            user = request.user
            try:
                user_course = UserCourse.objects.get(user = user  , course = course)
            except:
                return redirect("check-out" , slug=course.slug)
        
    
        
    context = {
        "course" : course , 
        "video" : video , 
        'videos':videos
    }
    return render(request , template_name="Nipracademy/course_page.html" , context=context )  

# Contact Us page view function
def details(request):
    if request.method=="POST":
        Contact=contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        Contact.name=name
        Contact.email=email
        Contact.phone=phone
        Contact.desc=desc

        Contact.save() 
        messages.success(request, "Your message has been sent!")
    return render(request,'Nipracademy/details.html')  

# Comment page View function
@login_required
def comment_page(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user  
            new_comment.save()
            return redirect('comment_page')  # Redirect to the same page
    else:
        form = CommentForm()
        comments = Comment.objects.all()
    return render(request, 'Nipracademy/comment_page.html', {'form': form , 'comments' : comments})

#comment delete Option View function
@login_required
def delete_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    if comment.user == request.user:
        comment.delete()
    return redirect('comment_page')

# Offline contact option view function
def OfflineAdmission(request):
    address = OfflineAddress.objects.all()
    return render(request, 'Nipracademy/OfflineAdmission.html',{'address':address})

# Privacy policy view function
def privacy_policy(request):
    return render(request,'Nipracademy/privacy_policy.html')

# Terms and conditions view function
def terms_and_conditions(request):
    return render(request,'Nipracademy/terms_and_conditions.html')

# Faculty details page view function
def faculty(request):
    try:
        faculties = Faculties.objects.all()
        return render(request,'Nipracademy/faculty.html',{'faculties':faculties})
    except:
        return HttpResponse("<h1> Oops!  Details not found or Some missing values. </h1> please check admin panel.")
    
def homepage_images(request):
    try:
        home_image=Homepage_image.objects.all()
        return render(request,"Nipracademy/home.html",{'home_image':home_image})
    except:
        return HttpResponse("<h1> Oops! Something went wrong!.</h1> image not found.")
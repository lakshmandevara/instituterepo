from django.shortcuts import render
from .models import FeedbackData,ContactData,CoursesData
from .forms import FeedbackForm,ContactForm
from django.http.response import HttpResponse
import datetime
date1= datetime.datetime.now()
def main_page(request):
    return render(request,'base2.html')


def home_page(request):
    return render(request,'home_page.html')


def contact_page(request):
    if request.method =="POST":
        cform=ContactForm(request.POST)
        if cform.is_valid():
            name = cform.cleaned_data.get('name')
            email = cform.cleaned_data.get('email')
            mobile = cform.cleaned_data.get('mobile')
            courses = cform.cleaned_data.get('courses')
            shifts = cform.cleaned_data.get('shifts')
            locations = cform.cleaned_data.get('locations')
            gender = cform.cleaned_data.get('gender')
            start_date = cform.cleaned_data.get('start_date')

            data = ContactData(
                name=name,
                email=email,
                mobile=mobile,
                courses=courses,
                shifts=shifts,
                locations=locations,
                gender=gender,
                start_date=start_date
            )
            data.save()
            cform = ContactForm()
            return render(request,'contact_page.html',{'cform':cform})
        else:
            return HttpResponse("User Invalid Data.....")
    else:
        cform = ContactForm()
        return render(request,'contact_page.html',{'cform':cform})
























def Courses_page(request):

 courses=CoursesData.objects.all()
 return render(request, 'Courses_page.html',{'courses':courses})



def Feedback_page(request):
    #return render(request,'Feedback_page.html')
    if request.method == "POST":
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            rating=request.POST.get('rating')
            feedback=request.POST.get('feedback')
            data=FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1
            )
            data.save()
            fform = FeedbackForm()
            fdata=FeedbackData.objects.all()
            return render(request,'Feedback_page.html',{'fform':fform,'fdata':fdata})
        else:
            return HttpResponse("Invalid User Data")


    else:
        fform =FeedbackForm()#take the empty form
        fdata=FeedbackData.objects.all()
        return render(request,'Feedback_page.html',{'fform':fform,'fdata':fdata})#display data and display empty form













def OurTeam_page(request):
    return render(request,'OurTeam_page.html')


def Gallery_page(request):
    return render(request,'Gallery_page.html')

from django.shortcuts import render
from courses.models import category,course

def categories(request):
    category_view=category.objects.all()
    sub_courses=course.objects.all()
    course_list = []
    for category_instance in category_view:
        course_view = course.objects.filter(category=category_instance)
        catCourse = {"cat": category_instance, 'cour': course_view}
        course_list.append(catCourse)

    return render(request,'index.html',{'c':course_list,'q':category_view,'sub':sub_courses})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def allcourses(request):
    q=category.objects.all()
    sub_courses=course.objects.all()
    
    return render(request,'course.html',{
        'q':q,
        'sub':sub_courses
        })    
    
def course_details(request,id):
    details=course.objects.get(id=id)
   
    return render(request,'courseDetails.html',{'details':details})
            
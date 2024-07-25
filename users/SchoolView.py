from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib import messages
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from curriculum.models import *
from users.models import *
from curriculum import views
from django.core.cache import cache
from django.contrib.admin.models import LogEntry
import datetime as dt
# from .signals import succesful_logout
from assessment.models import *
from django.db.models import Max
from django.db.models import Q
import json
from django.db.models import Count
from collections import defaultdict
from django.core.mail import send_mail
from users.forms import *

def school_home(request,subject_id=None):
    user=request.user
    school=User.objects.get(username=user)
    school_obj = user_profile_school.objects.get(user=school)
    
    school=school_obj.school_name
    students=user_profile_student.objects.filter(school__icontains=school).count()
    teachers=user_profile_teacher.objects.filter(school__icontains=school).count()

    subjects=Subject.objects.all().count()
    advocacy_count=AdvocacyVisit.objects.filter(school__icontains=school).count()
    advocacy=AdvocacyVisit.objects.filter(school__icontains=school)

    unread_notifications = NotificationSchool.objects.filter(school_id=school_obj, read=False).count()

    school_sheet_urls = {
    "Satya Prakash Public School, Jabalpur": "https://docs.google.com/spreadsheets/d/1yqQL_dFTKq5t9M4sdSuOrXQbekteDgIw/edit",
    "Sparsh Global School,Greater Noida": "https://docs.google.com/spreadsheets/d/1cbHHCc-sf5ctuPfk5wQ6LuJEL_b7Q6Tj/edit",
    "Vivekanand School,Delhi": "https://docs.google.com/spreadsheets/d/18RtDFAXcdZ_QdAp3DuDI1ddCJg5bADxVLtI3DyKrkqk/edit",
    "SPS,Sonipat": "https://docs.google.com/spreadsheets/d/1EnxRAMA39cXEJ1_BDcevhkUf42tUyxQH/edit",
    "BDSVM, Noida": "https://docs.google.com/spreadsheets/d/1sw5RveApNz_8IfWaEOd5qkf8EXYgRd6uONfjfZCXKUI/edit",
    "JP International School,Greater Noida": "https://docs.google.com/spreadsheets/d/1HSCRazedpWJ9Hc7y1womiB4JBKtW3SJYA1S4FILN_4A/edit",
    "Blooming Dale School,Badaun": "https://docs.google.com/spreadsheets/d/16X2VQWQIeGnXsjRTlz9AVLYEZDrkeRnb/edit",}
    
    

    # Function to get the Google Sheet URL based on the school name
    def get_school_sheet_url(school_name):
        return school_sheet_urls.get(school_name, "")

    # Get the Google Sheet URL for the current user's school
    school_sheet_url = get_school_sheet_url(school)

    schoolcontracts=SchoolContract.objects.filter(school__icontains=school).first()
    
    gallery_school=SchoolGallery.objects.filter(school__icontains=school).first()
    observation_sheet=ObservationSheet.objects.filter(school__icontains=school).first()
    curriculum_sheet=CurriculumView.objects.filter(school__icontains=school).first()

    context={
        "total_student": students,
        "school":school_obj,
        "unread_notifications":unread_notifications,
        "teachers":teachers,
        "subjects":subjects,
        "advocacy_count":advocacy_count,
        "advocacy":advocacy,
        "school_sheet_url": school_sheet_url,
        # "school_gallery_url": school_gallery_url,
        "schoolcontracts":schoolcontracts,
        "gallery_school":gallery_school,
        "observation_sheet":observation_sheet,
        "curriculum_sheets":curriculum_sheet
    }
    return render(request, "school/school_home_template.html", context)

def student_data_view(request):
    return render(request, 'school/student_view_attendance.html')

def student_view_data_post(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method")
        return redirect('users:attendance_data')
    else:
        # Getting all the Input Data
        grade= request.POST.get('grade')

        student_obj = user_profile_student.objects.filter(grade__icontains=grade)
        students_count=student_obj.count()

        context = {
            "student_obj": student_obj,
            "students_count":students_count
        }
        return render(request, 'school/student_data_gradewise.html', context)
    
def display_teachers(request):
    user=request.user
    school=User.objects.get(username=user)
    school_obj = user_profile_school.objects.get(user=school)
    
    school=school_obj.school_name
    teachers=user_profile_teacher.objects.filter(school__icontains=school).select_related('user')

    # Sort teachers by escalation level
    teachers = sorted(teachers, key=lambda teacher: teacher.get_escalation())

    return render(request, "school/teachers_list.html", {"teachers":teachers,"school":school_obj})

def subject_list(request):
    user=request.user
    school=User.objects.get(username=user)
    school_obj = user_profile_school.objects.get(user=school)
    subjects={
        "Junior Scratch":"1-2",
        "Hands-On Science Kit":"1-9",
        "Scratch":"3-6",
        "Robotics": "3-9",
        "MIT App Inventor":"6",
        "3D Designing":"7",
        "Arduino": "7-10",
        "Python": "7-10",
        "Internet of Things":"9",
        "AI": "4-10",
        "Jodo Straw":"3-4",
        "Paper Circuit":"2-3",
        "Data Science":"9-10",
        "Early Simple Machine":"1-2",
        "Tinkercad":"4-6"
    }

    processed_subjects = {}
    for subject, classes in subjects.items():
        class_range = classes.split('-')
        processed_subjects[subject] = {
            "full_range": classes,
            "first_class": class_range[0]
        }
    
    return render(request, "school/subjects_list.html", {"subjects": processed_subjects})

def school_feedback(request):
    school_obj = user_profile_school.objects.get(user=request.user)
    feedback_data = FeedBackSchool.objects.filter(school=school_obj)
    context = {
        "feedback_data": feedback_data,
        "school":school_obj
    }
    return render(request, 'school/school_feedback.html', context)

def school_feedback_save(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method.")
        return redirect('users:school_feedback')
    else:
        feedback = request.POST.get('feedback_message')
        school_obj = user_profile_school.objects.get(user=request.user)
        school_name=school_obj.school_name

        try:
            add_feedback = FeedBackSchool(school=school_obj, feedback=feedback, feedback_reply="")
            add_feedback.save()
            mentors=user_profile_teacher.objects.filter(school__icontains=school_name)
            for mentor in mentors:
                print(f"Sending email to: {mentor.user.email}")  # Print email being sent to
                send_mail(
                    'New Feedback Submitted',
                    f'Hello {mentor.first_name},\n\nNew feedback has been submitted by {school_obj.school_name}:\n\n"{feedback}"\n\nPlease review it at your earliest convenience.',
                    'training@thinnkware.com',  # Replace with your actual email
                    [mentor.user.email],
                    fail_silently=False,
                )
            messages.success(request, "Feedback Sent and Mentors Notified.")
            return redirect('users:school_feedback')
        except:
            messages.error(request, "Failed to Send Feedback.")
            return redirect('users:school_feedback')
        
def notifications(request):
    user=request.user
    school=user_profile_school.objects.get(user=user)
    notifications = NotificationSchool.objects.filter(school_id=school).order_by('-id')
    return render(request, 'school/notification.html', {'notifications': notifications,"school":school})

def mark_notification_as_read(request, id):
    notification = NotificationSchool.objects.get(id=id)
    notification.read = True
    notification.save()
    return redirect('users:school_feedback')

def student_report(request):
    user = request.user
    school = User.objects.get(username=user)
    school_obj = user_profile_school.objects.get(user=school)
    school_name = school_obj.school_name

    students = user_profile_student.objects.filter(school__icontains=school_name).order_by('first_name')

    if school_name in ["Sparsh Global School,Greater Noida", "JP International School,Greater Noida", "SPS,Sonipat", "Satya Prakash Public School, Jabalpur"]:
        valid_grades = range(1, 10)
    elif school_name in ["Vivekanand School,Anand Vihar"]:
        valid_grades = range(6, 10)
    elif school_name in ["Blooming Dale School,Budaun"]:
        valid_grades = range(3, 9)
    else:
        valid_grades = students.values_list('grade', flat=True).distinct()

    students_sectionwise = (
        students.filter(grade__in=valid_grades)
        .values('grade', 'section')
        .annotate(total_number=Count('user_id'))
        .order_by('grade', 'section')
    )

    search_query = request.GET.get('search', '')
    if search_query:
        students = students.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query))
        students_sectionwise = []

    grade_section_data = defaultdict(list)
    for entry in students_sectionwise:
        grade_section_data[entry['grade']].append(entry)

    context = {
        "grade_section_data": dict(grade_section_data),  # Convert to regular dict for template
        "students": students,
        "search_query": search_query,
        "school": school_obj
    }

    return render(request, 'school/view_report.html', context)


def student_report_gradewise(request, grade, section):
    user = request.user
    school = User.objects.get(username=user)
    school_obj = user_profile_school.objects.get(user=school)
    query = request.GET.get('q')
    
    students = user_profile_student.objects.filter(grade=grade, section=section)
    student_schoolwise = students.filter(school__icontains=school_obj.school_name).order_by('first_name')
    
    if query:
        students = students.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query)  
        )
    
    context = {
        'grade': grade,
        'section': section,
        'students': student_schoolwise,
        'school': school_obj,
        'search_query': query,
    }
    
    return render(request, 'school/student_report_gradewise.html', context)
        
def student_detail_report(request,user_id):
    user=request.user
    school=User.objects.get(username=user)
    school_obj = user_profile_school.objects.get(user=school)
    
    users=user_profile_student.objects.get(user_id=user_id)
    user=User.objects.get(username=users)
    marks=Result.objects.filter(user=user)
    login_activities = UserLoginActivity.objects.filter(login_username=user.username).order_by('-login_datetime')[:5]
    return render(request, "school/details_mark.html",{"users":users,"marks":marks,"school":school_obj, "login_activities": login_activities,})

def student_activity_view(request, user_id):
    activities = UserActivity1.objects.filter(user_id=user_id).order_by('-date')
    context = {
        'activities': activities,
        'user_id': user_id
    }
    return render(request, 'school/student_activity.html', context)

def school_profile(request):
    user = User.objects.get(id=request.user.id)
    school = user_profile_school.objects.get(user=user)

    context={
        "user": user,
        "school": school
    }
    return render(request, 'school/school_profile.html', context)

def school_profile_update(request):
    if request.method != "POST":
        messages.error(request, "Invalid Method!")
        return redirect('users:school_profile')
    else:
        school_name = request.POST.get('school_name')
        principal_name = request.POST.get('principal_name')
        password = request.POST.get('password')
        mobile= request.POST.get('mobile')
        country= request.POST.get('country')
        state= request.POST.get('state')
        city= request.POST.get('city')
        district=request.POST.get('district')
        street=request.POST.get('street')
        pincode=request.POST.get('pincode')
        mentor=request.POST.get('mentor')
        logo = request.FILES.get('logo')

        try:
            customuser = User.objects.get(id=request.user.id)
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()

            school = user_profile_school.objects.get(user=customuser.id)
            school.school_name=school_name
            school.principal=principal_name
            school.mentor=mentor
            school.mobile=mobile
            school.country=country
            school.state=state
            school.city=city
            school.district=district
            school.pin=pincode
            school.street=street
            school.logo=logo
            school.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('users:school_profile')
        except:
            messages.error(request, "Failed to Update Profile")
            return redirect('users:school_profile')
            
def advocacy(request):
    teacher_obj = user_profile_school.objects.get(user=request.user)
    school=teacher_obj.school_name
    advocacy=AdvocacyVisit.objects.filter(school__icontains=school)
    return render(request, 'school/advocacy_list.html', {"advocacy":advocacy})
    
def get_report(request, id):
    advocacy_visit = get_object_or_404(AdvocacyVisit, pk=id)
    advocacy_visit.verified_by=True
    advocacy_visit.save()
    return render(request, 'school/advocacy_report.html', {'advocacy_visit': [advocacy_visit]})
    
def view_macroplanner(request):
    school=user_profile_school.objects.get(user=request.user)
    school_name=school.school_name
    macroplanners = Macroplanner.objects.filter(school__icontains=school_name)
    return render(request, 'school/view_macroplanner.html', {'macroplanners': macroplanners})
    
def view_microplanner(request):
    school=user_profile_school.objects.get(user=request.user)
    school_name=school.school_name
    microplanners = Microplanner.objects.filter(school__icontains=school_name)
    return render(request, 'school/view_microplanner.html', {'microplanners': microplanners})
    
def view_timetable(request):
    school = request.user.user_profile_school.school_name
    timetable = TimeTable.objects.filter(school__icontains=school).order_by('-id').first()
    return render(request, 'school/view_timetable.html', {'timetable': timetable})
    
def inventory(request):
    school = request.user.user_profile_school.school_name
    inventory_list = Inventory.objects.filter(school__icontains=school)
    return render(request, 'school/inventory.html', {'inventory_list': inventory_list})

def kreativityshow(request):
    school=user_profile_school.objects.get(user=request.user)
    school_name=school.school_name
    kreativityshow=KreativityShow.objects.filter(school__icontains=school_name)
    return render(request, 'school/kreativityshow.html',{"kreativityshow":kreativityshow})

def guestsession(request):
    school=user_profile_school.objects.get(user=request.user)
    school_name=school.school_name
    guestsession=GuestSession.objects.filter(school__icontains=school_name)
    return render(request, 'school/guestsession.html',{"guestsession":guestsession})
    
def leaderboard(request):
    school=user_profile_school.objects.get(user=request.user)
    school_name=school.school_name
    
    # max_results = Result.objects.values('user__user_profile_student__grade').annotate(max_score=Max('score'))
    overall_students = Result.objects.filter(user__user_profile_student__school__icontains=school_name).order_by('-score')[:5]
    
    # Fetch the overall top students from the teacher's grade
    grade_students = Result.objects.filter(
        user__user_profile_student__school=school
    ).order_by('-score')[:3]

    # Initialize a dictionary to store top 3 students for each grade
    top_students_by_grade = {}
    
    max_results = Result.objects.filter(
        user__user_profile_student__school__icontains=school_name
    ).values('user__user_profile_student__grade').annotate(max_score=Max('score'))

    # Iterate through each grade and get the top 3 students
    for grade_info in max_results:
        grade = grade_info['user__user_profile_student__grade']
        max_score = grade_info['max_score']
        
        # Get the top 3 students with the maximum score in each grade
        top_students = Result.objects.filter(
            user__user_profile_student__grade=grade,
            user__user_profile_student__school__icontains=school
        ).order_by('-score')[:3]

        # Add the top students to the dictionary
        top_students_by_grade[grade] = top_students

    return render(request, 'school/leadership.html', {'top_students_by_grade': grade_students,"overall_students":overall_students})
    
def competition(request):
    school=user_profile_school.objects.get(user=request.user)
    school_name=school.school_name
    competition=Competition.objects.filter(school__icontains=school_name)
    return render(request, 'school/competition.html',{"competition":competition})

def innovation(request):
    school=user_profile_school.objects.get(user=request.user)
    school_name=school.school_name
    innovations=InnovationClub.objects.filter(school__icontains=school_name)
    return render(request, 'school/innovation.html',{"innovations":innovations})\
        
from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import os

# Path to your credentials JSON file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'api_lms.json')

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# Mapping of school names to Google Sheets URLs
SCHOOL_SPREADSHEET_MAP = {
    "Sparsh Global School,Greater Noida": 'https://docs.google.com/spreadsheets/d/1Qt13_7Wt_Z54ocFdOaXcJsJFUNQCT1rhpMdRNsveeEs',
    "JP International School,Greater Noida": 'https://docs.google.com/spreadsheets/d/your_spreadsheet_id_2',
}

def get_google_sheet_data(sheet_url, range_name):
    try:
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        
        spreadsheet_id = sheet_url.split('/d/')[1].split('/')[0]
        result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        values = result.get('values', [])
        
        return values
    except Exception as e:
        print(f"Error in get_google_sheet_data: {e}")
        raise

def observation_performance_chart(request, user_id):
    school = get_object_or_404(user_profile_school, user_id=user_id)
    sheet_url = SCHOOL_SPREADSHEET_MAP.get(school.school_name)
    
    if not sheet_url:
        return HttpResponse("Spreadsheet not available")

    range_name = 'A1:I'  # Adjust the range to include all relevant columns
    data = get_google_sheet_data(sheet_url, range_name)

    if not data:
        return HttpResponse("No data available in the spreadsheet")

    headers = data[0]  # First row for headers
    rows = data[1:]  # Remaining rows for data

    return render(request, 'school/student_performance.html', {
        'headers': headers,
        'rows': rows,
    })
    
def school_login_activity(request):
    user = request.user
    try:
        school_profile = user_profile_school.objects.get(user=user)
    except user_profile_school.DoesNotExist:
        return render(request, "school/no_permission.html", {"message": "You do not have permission to view this page."})

    form = StudentFilterForm(request.GET or None)
    student_profiles = user_profile_student.objects.filter(school=school_profile.school_name)
    
    if form.is_valid():
        grade = form.cleaned_data.get('grade')
        section = form.cleaned_data.get('section')
        
        if grade:
            student_profiles = student_profiles.filter(grade=grade)
        
        if section:
            student_profiles = student_profiles.filter(section=section)

    login_usernames = [student.user.username for student in student_profiles]
    login_activities = UserLoginActivity.objects.filter(login_username__in=login_usernames).order_by('-login_datetime')

    context = {
        "login_activities": login_activities,
        "school_profile": school_profile,
        "form": form,
    }

    return render(request, "school/school_login_activity.html", context)
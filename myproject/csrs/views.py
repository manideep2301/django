from django.shortcuts import render, redirect
from .models import Sport, StudentRegistration
from django.contrib.auth.decorators import login_required
from csrs import views


@login_required
def student_registration(request):
    sports = Sport.objects.all()
    if request.method == 'POST':
        sport_id = request.POST['sport_id']
        sport = Sport.objects.get(pk=sport_id)
        StudentRegistration.objects.create(user=request.user, sport=sport, status='waitlist')
        return redirect('student_registration')
    return render(request, 'student_registration.html', {'sports': sports})

@login_required
def registration_management(request):
    registrations = StudentRegistration.objects.all()
    return render(request, 'registration_management.html', {'registrations': registrations})

@login_required
def sport_management(request):
    sports = Sport.objects.all()
    return render(request, 'sport_management.html', {'sports': sports})

@login_required
def generate_reports(request):
    sports = Sport.objects.all()
    report_data = [(sport, StudentRegistration.objects.filter(sport=sport).count()) for sport in sports]
    return render(request, 'generate_reports.html', {'report_data': report_data})

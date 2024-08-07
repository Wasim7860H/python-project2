from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .form import StudentRegistrations

# Create your views here.
def add_show(request):
 if request.method == 'POST':
    fm = StudentRegistrations(request.POST)
    if fm.is_valid():
      fm.save()
      fm = StudentRegistrations()







 else:
    
    fm = StudentRegistrations()
 stud = User.objects.all()
 return render(request, 'enroll/addandshow.html', {"form":fm, 'stu':stud})

# This Functions Will Update/Edit
def update_data(request, id):
  if request.method == 'POST':
    pi = User.objects.get(pk=id)
    fm = StudentRegistrations(request.POST, instance=pi)
    if fm.is_valid():
      fm.save()
  else:
     pi = User.objects.get(pk=id)
     fm = StudentRegistrations(request.POST, instance=pi)

  return render(request, 'enroll/updatestudent.html', {'form':fm})





# This Function Will Delete
def delete_data(requset, id):
  if requset.method == 'POST':
    pi = User.objects.get(pk=id)
    pi.delete()
  return HttpResponseRedirect('/')
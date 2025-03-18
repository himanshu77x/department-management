from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Department
from .Forms import DepartmentForm

def admin_required(login_url=None):
    return user_passes_test(lambda u: u.is_superuser, login_url=login_url)

@admin_required(login_url='/admin/login/')
def department_dashboard(request):
    departments = Department.objects.filter(status='True')
    query = request.GET.get('q')
    if query:
        departments = departments.filter(dept_name__icontains=query)

    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_dashboard')
    else:
        form = DepartmentForm()
    
    return render(request, 'ment/dashboard.html', {'departments': departments, 'form': form, 'query': query})

@admin_required(login_url='/admin/login/')
def edit_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    form = DepartmentForm(request.POST or None, instance=department)
    if form.is_valid():
        form.save()
        return redirect('department_dashboard')
    return render(request, 'ment/edit_department.html', {'form': form, 'department': department})

@admin_required(login_url='/admin/login/')
def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.status = 'False'  # Soft delete
        department.save()
        return redirect('department_dashboard')
    return render(request, 'ment/delete_confirm.html', {'department': department})

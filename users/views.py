from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistorForm,UserUpdateForm,ProfileUpdateForm
def register(request):
    if request.method == 'POST':
      form = UserRegistorForm(request.POST)
      if form.is_valid():
          form.save()
          username = form.cleaned_data.get('username')
          messages.success(request,f"Account is created for {username}")
          return redirect('blog-home')
    else:
          form = UserRegistorForm()
    return render(request,'users/register.html',{'form':form})
@login_required
def profile(request):
      u_form = UserUpdateForm()
      p_form = ProfileUpdateForm()
      context = {
            'u_form':u_form,
            'p_form':p_form
      }
      return render(request,'users/profile.html',context)
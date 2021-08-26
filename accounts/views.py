from django.shortcuts import redirect, render
from accounts.forms import SignInForm, SignUpForm
from django.contrib.auth import authenticate, login
from accounts.models import Account


# Create your views here.
def signin_view(request):
    form = SignInForm(request.POST or None)
    message = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username)
            print(password)
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                message = "Invalid Credentials"
        else:
            message = "Form Validation Error"
    return render(request, "account/signin.html", {"form": form, "message": message})


def signup_view(request):
    message = None
    success = False
    print(request.POST)
    if request.method == "POST":
        form = SignUpForm(request.POST)
        print("in Form")
        print(form.is_valid())
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            dob = form.cleaned_data['dob']
            gender = form.cleaned_data['gender']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                dob=dob,
                gender=gender,
                email=email,
                password=password
            )

            user.is_active = True
            user.save()
            return redirect('signin')
        else:
            message = "Invalid FOrm"
    else:
        form = SignUpForm()
    return render(request, "account/signup.html", {"form": form, "message": message})

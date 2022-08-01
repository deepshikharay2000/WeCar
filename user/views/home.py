from django.shortcuts import render,redirect
from django.views import View
from user.models.user_models import User
from django.contrib.auth.hashers import make_password,check_password


class Index(View):
    def get(self,request):
        return render(request, 'index.html')

class Signup(View):
    def get(self,request):
        return render(request, 'signup.html')
    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # Validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_message = None
        user = User(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password,
                            )

        error_message = self.validateuser(user)

        # saving
        if not error_message:

            user.password = make_password(user.password)

            user.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)


    def validateuser(self,user):
        error_message = None;
        if (not user.first_name):
            error_message = "First Name Requried"
        elif len(user.first_name) < 4:
            error_message = "First Name Must Be 4  Char"
        elif not user.last_name:
            error_message = "First Name Requried"
        elif len(user.last_name) < 4:
            error_message = "Last Name Must Be 4  Char"
        elif not user.phone:
            error_message = "Phone Requried"
        elif len(user.phone) < 10:
            error_message = "Phone Must Be 10  Char"
        elif len(user.phone) > 10:
            error_message = "Phone Must Be 10  Char"
        elif not user.email:
            error_message = "Email Requried"

        elif user.isExist():
            error_message = "Email already registered"
        return error_message

class Login(View):
    def get(self,request):
        return render(request, 'login.html')
    
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = User.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['customer_email'] = customer.email
                return redirect('homepage')
            else:
                error_message = "Email or Password Invalid"
        else:
            error_message = "Email or Password Invalid"
        return render(request, 'login.html', {'error': error_message})

class Contact(View):
    def get(self,request):
        return render(request, 'contact.html') 
def logout(request):
    request.session.clear()
    return redirect('login')
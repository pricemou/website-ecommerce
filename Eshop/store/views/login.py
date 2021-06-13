from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

class Login(View):
    def get(self,request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,' &',password)
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
           flag = check_password (password, customer.password)
           print('flag :',flag)
           if flag:
               request.session['customer_id'] = customer.id
               request.session['email'] = customer.email
               return redirect('homepage')
        else:
            error_message = 'Email or Password invalid !!'
        return render(request,'login.html', {'error': error_message})

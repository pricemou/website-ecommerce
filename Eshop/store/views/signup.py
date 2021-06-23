from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request,'signup.html')
    
    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')


        # Validation
        value = {
            'first_name':first_name,
            'last_name' : last_name,
            'phone' : phone,
            'email' : email,
            'password' : password
        }

        customer = Customer(
                first_name=first_name,
                last_name = last_name,
                phone = phone,
                email = email,
                password = password
            )
            # fonction qui faire appel aux donner
        erro_message = self.validationCustomer(customer)

        # saving
        if not erro_message:
            print("------------------------------------------")
            print(first_name,last_name,phone,email,password)
            print("------------------------------------------")
            # masque le mots de passe
            customer.password = make_password(customer.password)
            print(customer.password)
            print("------------------------------------------")
            customer.register()
            return redirect('homepage')

        else:
            data = {
                'error':erro_message,
                'values': value
            }
        return render(request,'signup.html', data)


    def validationCustomer(self, customer):
            erro_message = None
            if(not customer.first_name):
                erro_message = "First Name Required !!"
            elif len(customer.first_name) < 4:
                erro_message = "First Name must be 4 char long or more  !!"
            elif not customer.last_name:
                erro_message = "Last Name Required"
            elif len(customer.last_name) < 4:
                erro_message = "Last Name must be 4 char long or more"
            elif not customer.phone:
                erro_message = "Phone Number required"
            elif len(customer.phone) < 10:
                erro_message = "Phone Number must be 10 char Long"
            elif len(customer.password) < 6:
                erro_message = "Password Number must be 10 char Long"
            elif len(customer.email)< 4:
                erro_message = "Email must be char long"
            elif customer.isExists():
                erro_message = 'Email Address Already Registered..'
            return erro_message

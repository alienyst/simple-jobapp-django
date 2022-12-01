from django.shortcuts import render, redirect
from subscribe.models import Subscribe
from subscribe.forms import SubscribeForm
from django.urls import reverse


# Create your views here.
def subscribe(request):
    subscribe_form = SubscribeForm()
    error_empty = ""
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            return redirect(reverse('dankje'))

        #    print("Valid Form")
        #    print(subscribe_form.cleaned_data)
        #    fname = subscribe_form.cleaned_data['first_name']
        #    lname = subscribe_form.cleaned_data['last_name']
        #    email = subscribe_form.cleaned_data['email']
        #    print(fname)
        #    subscribe = Subscribe(first_name=fname, last_name=lname, email=email)
        #    subscribe.save()

        # fname = request.POST['fname']
        # lname = request.POST['lname']
        # email = request.POST['email']
        # print('Request is POST', fname, lname, email)
        # if fname == "" or lname == "" or email == "":
        #     error_empty = "No entered"

        # subscribe = Subscribe(first_name=fname, last_name=lname, email=email)
        # subscribe.save()

    context = {"form":subscribe_form,"error_empty" : error_empty}
    return render(request, 'subscribe/subscribe.html', context)

def dankje(request):
    context = {}
    return render(request, 'subscribe/dankje.html', context)
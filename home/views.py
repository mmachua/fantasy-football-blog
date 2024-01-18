from django.views.generic import TemplateView
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import Post, Homepage, Aboutpage
from django.views.generic import ListView, CreateView 
from home.forms import ContactForm, NewsletterForm
from home.models import Contact, Newsletter



class HomeView(TemplateView):
    template_name = 'home/home.html'
    model = Newsletter
    form_class = NewsletterForm

    def get(self, request):
        form = NewsletterForm()
        posts = Post.objects.all()
        homepages = Homepage.objects.all() 

        args = {
            'posts': posts, 'homepages': homepages, 'form': form
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter = form.save(commit=False)
            newsletter.user = request.user
            newsletter.save()
            title = 'Thanks!!'
            confirm_message = "Thankyou for subscribing to our newsletter, Email received"
            context = {'title': title, 'confirm_message': confirm_message }
            
        return render(request, self.template_name, context)


class AboutView(TemplateView):
    template_name = 'home/about.html'


    def get(self, request):
        aboutpages = Aboutpage.objects.all()

        args = {
            'aboutpages': aboutpages
        }
        return render(request, self.template_name, args)


class ContactView(TemplateView):
    template_name = 'home/contact.html'
    model = Contact
    form_class = ContactForm

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            title = 'Thanks!!'
            confirm_message = 'Thanks for the message. I will get right back to you!'
            context = {'title': title, 'confirm_message': confirm_message }
        return render(request, self.template_name, context)



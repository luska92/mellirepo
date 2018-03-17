from django.shortcuts import render
from django.views.generic import (View,TemplateView,
                                ListView,DetailView)
from . import models
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context, Template
from django.template.loader import get_template

# Create your views here.
class ProduktListView(ListView):
    context_object_name = 'lista'
    model = models.Produkt

class ProduktDetailView(DetailView):
    context_object_name = 'product_details'
    model = models.Produkt
    template_name = 'melliapp/productdetail.html'

class OmnieView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'melliapp/omnie.html'

def ContactView(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            Imię = request.POST.get(
                'Imię'
            , '')
            Email = request.POST.get(
                'Email'
            , '')
            Treść = request.POST.get('Treść', '')

            # Email the profile with the
            # contact information
            context = {'Imię': Imię,'Email': Email,'Treść': Treść}
            template = get_template('melliapp/contact_template.txt').render(context)

            email = EmailMessage(
                "Nowa wiadomość z formularza kontaktowego",
                template,
                "Mellidesign" +'',
                ['la.matwiejczyk@gmail.com'],
                headers = {'Reply-To': Email }
            )
            email.send()
    return render(request, 'melliapp/contact.html', {
        'form': form_class,
    })

from django.shortcuts import render

# Create your views here.
import threading
import time

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader

from e_mailer.forms import MailForm
from django.core.mail import send_mail

from .models import Mail


def create_thread(title, message, to_email, seconds, post):
    mails = Mail.objects.filter(status=False)
    threads = []
    for mail in mails:
        thread = threading.Thread(target=send, args=(title, message, to_email, seconds, post))
        threads.append(thread)
        thread.start()

    return redirect('/mails_list')



def send(title, message, to_email, seconds, post):
    time.sleep(int(seconds))
    result = send_mail(title, message, 'iren_coder@mail.ru', [to_email], fail_silently=False)
    if result == 1:
        post.status = True
    post.save()


def index(request):
    template_name = "index.html"
    form = MailForm()

    if request.method == "POST":
        form = MailForm(request.POST)
        title = request.POST.get('title', '')
        message = request.POST.get('text', '')
        to_email = request.POST.get('email', '')
        seconds = request.POST.get('seconds', '')
        if form.is_valid():
            post = form.save(commit=False)
            post.title = title
            post.text = message
            post.email = to_email
            post.seconds = seconds
            post.save()
            create_thread(title, message, to_email, seconds, post)

        return redirect('/mails_list')

    return render(request, template_name, {'form': form})


def mails_list(request):
    template = loader.get_template('mails_list.html')
    mails = Mail.objects.all().order_by('-id')[:10]
    data = {
        'mails': reversed(mails),
    }

    return HttpResponse(template.render(data, request))
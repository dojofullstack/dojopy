from django.shortcuts import render, redirect
from .models import ModelLog
from django.core.files import File
from django.conf import settings
import os


def download_paramiko():
    # download log paramiko code
    return '/tmp/log_from_paramiko.log'


def update(request):
    path_log = download_paramiko()
    name_file = path_log.split('/')[-1]

    file = open(path_log, 'rb')
    my_file = File(file, name=os.path.basename(file.name))
    ModelLog.objects.create(
            log_version=name_file,
            file_log=my_file
        )
    return redirect('list_log')


def list_log(request):
    obj = ModelLog.objects.all().order_by('time_create')
    ctx = {
        'list_log': obj
    }
    return render(request, 'logMonitor/list_log.html', ctx)

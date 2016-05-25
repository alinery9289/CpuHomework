# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import psutil
import json
import models

def cpu_info(request):
    if request.method == 'GET':
        cpu_percent = str(psutil.cpu_percent())
        cpu_stats= str(psutil.cpu_stats())
        cpu_count= str(psutil.cpu_count())
        cpu_info = {} 
        cpu_info['cpu_rate']= cpu_percent    
        cpu_info['cpu_stats']= cpu_stats  
        cpu_info['cpu_count']= cpu_count  
        return HttpResponse(json.dumps(cpu_info))
    else:
        cpu_info = {} 
        cpu_info['error']= "error"
        return HttpResponse(json.dumps(cpu_info))

def cpu_rate(request,rate):
    if request.method == 'GET':
        this_sets = models.Setting.objects.filter(cpu_is_local="local")
        this_sets.update(cpu_state_set = rate)
        
        cpu_rate = {} 
        cpu_rate['cpu_rate']= rate
        return HttpResponse(json.dumps(cpu_rate))
    else:
        cpu_rate = {} 
        cpu_rate['error']= "error"
        return HttpResponse(json.dumps(cpu_rate))
    
def query_all(request):
    if request.method == 'GET':
#         models.Setting.objects.create(cpu_is_local="local", cpu_consum=False, cpu_state_set=0)
        this_sets = models.Setting.objects.filter(cpu_is_local="local")
        if this_sets.count()>0:
            for this_set in list(this_sets):
                cpu_state_set = this_set.cpu_state_set
                cpu_consum =this_set.cpu_consum
                            
        return HttpResponse(str(cpu_state_set)+' '+str(cpu_consum))
    
    
    
    
    
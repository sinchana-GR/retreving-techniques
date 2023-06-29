from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q


# Create your views here.
def display_topics(request):
    topics=Topic.objects.all()
    topics=Topic.objects.filter(topic_name='cricket')
    topics=Topic.objects.exclude(topic_name='cricket')
    topics=Topic.objects.order_by('topic_name') 
    topics=Topic.objects.order_by('-topic_name')

    d={'topics':topics}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    webpages=WebPage.objects.all()
    webpages=WebPage.objects.filter(topic_name='cricket')
    webpages=WebPage.objects.exclude(topic_name='cricket')
    webpages=WebPage.objects.order_by(Length('name'))
    webpages=WebPage.objects.order_by(Length('name').desc())
    
    webpages=WebPage.objects.all()
    webpages=WebPage.objects.filter(name__in=['virat','rahul'])
    webpages=WebPage.objects.filter(name__regex='a\w+')
    webpages=WebPage.objects.all()
    webpages=WebPage.objects.filter(Q(name='xyz') | Q(url__startswith='https'))
    webpages=WebPage.objects.filter(Q(name='rahul') & Q(url__startswith='https'))
    webpages=WebPage.objects.all()

    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)


def display_accessrecords(request):
    accessrecords=AccessRecord.objects.all()
    
    accessrecords=AccessRecord.objects.all()
    accessrecords=AccessRecord.objects.filter(date='2023-06-22')
    accessrecords=AccessRecord.objects.filter(date__gt='1995-01-18')
    accessrecords=AccessRecord.objects.filter(date__lte='1995-01-18')
    accessrecords=AccessRecord.objects.filter(date__year='2021')
    accessrecords=AccessRecord.objects.filter(date__month='07')
    accessrecords=AccessRecord.objects.filter(date__day='12')
    accessrecords=AccessRecord.objects.filter(date__year__gte='2020')
    accessrecords=AccessRecord.objects.filter(date__year__lte='2020')
    accessrecords=AccessRecord.objects.filter(date__day__gt='12')
    
    d={'accessrecords':accessrecords}
    return render(request,'display_accessrecords.html',d)

def update_webpages(request):
    webpages=WebPage.objects.all()

    WebPage.objects.filter(name='virat').update(url='http//viratkohli.com')
    WebPage.objects.filter(topic_name='rugby').update(url='https://pavan.com')
    WebPage.objects.update_or_create(topic_name='foot ball',defaults={'name':'pavanwadeyar'})
    cto=WebPage.objects.get(topic_name='cricket')
    WebPage.objects.filter(name='Dhoni').update(topic_name='Rugby')
    WebPage.objects.update_or_create(name='abc',defaults={'url':'http://ABCDE.com',})
    cto=WebPage.objects.get(topic_name='cricket')
   

    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)
    
    

    
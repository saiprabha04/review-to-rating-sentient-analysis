from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from HotelApp.models import *
import nltk
import math
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 


def home(request):
    return render(request,'home.html')

def hotels(request):
    obj = Hotel.objects.all()
    context ={'obj':obj}
    return render(request,'hotels.html',context)

def search(request):    
    user=request.user
    context={'user':user}
    return render(request, 'search.html',context)

def searched(request):
    searchitem = request.GET['searchterm']
    search = Hotel.objects.filter(City__icontains = searchitem)
    
    l=[]
    for j in range(0,len(search)): 
        reviews = Review.objects.filter(Hotel=search[j].id)
        L = {}
        for k in range(0,len(reviews)):
            L[k]=(reviews[k].Reviews)
        l.append(L)
        if len(reviews) > 0:
            sum=0; avg=0
            for i in range(0,len(reviews)):
                sum = sum+reviews[i].Rating
            avg = sum/(len(reviews))
            h = Hotel.objects.filter(id=search[j].id).update(AvgReview = math.ceil(avg))
            
    context = {'searchitem':searchitem,'zp':zip(search,l)}
    return render(request, 'searched.html',context)

def sentiment_scores(sentence): 
    sid_obj = SentimentIntensityAnalyzer() 
    sentiment_dict = sid_obj.polarity_scores(sentence) 
    if sentiment_dict['compound'] >= 0.05 : 
        OldMax=1
        OldMin=0.05
        NewMax=5
        NewMin=2.5
        OldRange = (OldMax - OldMin)  
        NewRange = (NewMax - NewMin)  
        NewValue = (((sentiment_dict['compound'] - OldMin) * NewRange) / OldRange) + NewMin
        NewValue = (round(NewValue,1))
    elif sentiment_dict['compound'] <= - 0.05 :
        OldMax=-0.05
        OldMin=-1
        NewMax=2.5
        NewMin=1
        OldRange = (OldMax - OldMin)  
        NewRange = (NewMax - NewMin)  
        NewValue = (((sentiment_dict['compound'] - OldMin) * NewRange) / OldRange) + NewMin 
        NewValue = (round(NewValue,1))          
    else : 
        NewValue  =  2.5
    return NewValue

def review(request,id):
    if request.method == "POST":
        user = request.user
        reviews = request.POST['ta']
        hotel = Hotel.objects.get(id=id)
        rating = sentiment_scores(reviews)
        Review.objects.get_or_create(Name=user,Reviews=reviews,Rating=rating,Hotel=hotel)
        return redirect('search')

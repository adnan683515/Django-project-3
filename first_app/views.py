from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    
    
    
    dic = {'num': [3,5,6,7,3],'val':10 ,'name':'golam faruk adnan','age':9 , 'date_time': datetime.datetime.now() , 'weigth':'60kg', 'lst':['python','is','best'], ' courses':[
        {
            'id':3,
            'course':'python',
            'fee' :1000,
        },
        {
            'id':2,
            'course':'django',
            'fee':10000,
        },
        {
            'id':1,
            'course':'c',
            'fee' :4000,
        },
    ]}
    
    
    
    return render(request,'first_app/home.html',dic)
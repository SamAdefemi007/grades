from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request): 

    finals = None
    grades= None

    if request.method == "POST":
        scores=[]
        results = ["intro", "adv", "enterprise", "pm"]
        data = request.POST.items()
        for key, value in data:
            if key in results:
                if value == "":
                    continue
                else:
                    scores.append(int(value))
        
        try:
            average = sum(scores)/len(scores)
        except ZeroDivisionError:
            return HttpResponseRedirect(reverse('index'))
        
        cgs =  (average/100)*22
        grades=None
        if cgs ==22:
            grades = "A1"
        elif cgs <22 and cgs >=21:
            grades = "A2"
        elif cgs <21 and cgs >=20:
            grades = "A3"
        elif cgs <20 and cgs >=19:
            grades = "A4"
        elif cgs <19 and cgs >=18:
            grades = "A5"
        
        elif cgs <18 and cgs >=17:
            grades = "B1"
        elif cgs <17 and cgs >=16:
            grades = "B2"
        elif cgs <16 and cgs >=15:
            grades = "B3"

        elif cgs <15 and cgs >=14:
            grades = "C1"
        elif cgs <14 and cgs >=13:
            grades = "C2"
        elif cgs <13 and cgs >=12:
            grades = "C3"

        elif cgs <12 and cgs >=11:
            grades = "D1"
        elif cgs <11 and cgs >=10:
            grades = "D2"
        elif cgs <10 and cgs >=9:
            grades = "D3"

        elif cgs <9 and cgs >=8:
            grades = "E1"
        elif cgs <8 and cgs >=7:
            grades = "E2"
        elif cgs <7 and cgs >=6:
            grades = "E3"

        elif cgs <6 and cgs >=5:
            grades = "F1"
        elif cgs <5 and cgs >=4:
            grades = "F2"
        elif cgs <4 and cgs >=3:
            grades = "F3"        

        elif cgs <3 and cgs >=2:
            grades = "G1"
        elif cgs <2 and cgs >=1:
            grades = "G2"
        elif cgs <1 and cgs >=0:
            grades = "G3" 

        else:
            return "Invalid scores"  

        
        finals = None
        if grades in ["A1", "A2", "A3", "A4", "A5"]:
            finals = "Distinction"
        
        elif grades in ["B1", "B2", "B3"]:
            finals = "Commendation"

        elif grades in ["C1", "C2", "C3"]:
            finals = "Pass- Lower Second"

        elif grades in ["D1", "D2", "D3"]:
            finals = "Pass- Third Class"

        elif grades in ["E1", "E2", "E3"]:
            finals = "Marginal Fail - Resit possible"
        
        else:
            finals = "Fail"
    good_list = ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "C1", "C2", "C3" , "D1", "D2", "D3"]



    return render(request, 'grades_calc/index.html', {'grades': grades, 'Band_desc': finals, 'good_list': good_list})
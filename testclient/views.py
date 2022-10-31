from django.shortcuts import render, redirect
from tst.models import Answers, Tests, User, Profile, Stats, TmpTest, Questions
from django.http import JsonResponse, HttpResponse

arr = []

def test(request):
    disciplines = Tests.objects.all()
    user = User.objects.all()
    prof = Profile.objects.all()

    data = {'tst': disciplines, 'usr': user, 'prf': prof}
    return render(
        request, 
        'test.html', 
        context = data,
    )

#------------------      Начало тестирования    --------------------------

def starttest(request):
    if (request.method == 'POST'):
        t = request.POST.get('test')
        u = request.POST.get('user')
        
        usr = User.objects.get(id=int(u))
        tst = Tests.objects.get(id=int(t))
        quest = Questions.objects.filter(test = tst)
        # data = {'q': q, 'a': a}
        # TmpTest.objects.all().delete()  # очищаем временную таблицу
        i = 1
        st = Stats.objects.create(test=tst, user=usr, result=0)
        
        for q in quest: 
             
            test = TmpTest()
            test.qid = q.id
            test.ball = 0
            test.ans = False
            test.stat = st
            test.save()
            i += 1


        
        tmp = TmpTest.objects.filter(stat=st)

        count = quest.count()

        response = redirect("fetch")

        request.session['testid'] = t
        request.session['userid'] = u
        request.session['current'] = tmp.first().id
        request.session['count'] = count
        request.session['balls'] = 0
        request.session['start'] = tmp.first().id
        request.session['end'] = tmp.last().id
        request.session['stats'] = st.id

    return response

#------------------      Начало тестирования    --------------------------

def fetch(request):
    
    start = request.session["start"]
    end = request.session["end"]
    current = request.session["current"]

    if (request.method == 'POST'):
        choice = request.POST.get('choice')   
        answer = request.POST.get('answer')     
        try:
            tmp = TmpTest.objects.filter(id=current).update(choice=choice, ball=answer, ans=True)
        except:
            tmp = TmpTest.objects.filter(id=current).update(choice=0, ball=0, ans=False)
            print("Ошибка!")
        current = request.POST.get('current')
        request.session['current'] = current


    current = request.session["current"]
    t = request.session["testid"]

    tst = Tests.objects.get(id=int(t))
    answ = TmpTest.objects.get(id = current)
    quest = Questions.objects.get(id = answ.qid)
    answers = Answers.objects.filter(question = quest.id)

    inf =  {"start": start, 
            "end": end, 
            "current": current, 
            "choice": answ.choice,
            "stat": request.session['stats']}

    data = {"q": quest, "a": answers, "i": inf}    
    
    response = render(
            request, 
            'template.html', 
            context = data,
        )

    return response #JsonResponse(data)

#------------------      Начало тестирования    --------------------------

def end(request):
    # testid = request.session["testid"]
    st = request.POST.get('stats')
    stat = Stats.objects.get(id=st)

    tmp = TmpTest.objects.filter(stat=st)
    count = tmp.count()
    user = User.objects.get(id=stat.user.id)
    test = Tests.objects.get(id=stat.test.id)

    res = 0
    for el in tmp:
        res = res + el.ball

    data = {"count": count,
            "result": res,
            "user": user,
            "test": test}

    response = render(
            request, 
            'finish.html', 
            context = data,
        )
    return response


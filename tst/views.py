from django.shortcuts import render, redirect
from .models import Answers, Tests, User, Profile, Stats, TmpTest
from django.http import JsonResponse, HttpResponse
import json
from .models import Questions
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

#------------------      Начальная страница    --------------------------
def test(request):
    disciplines = Tests.objects.all()
    user = User.objects.all()
    prof = Profile.objects.all()

    data = {'tst': disciplines, 'usr': user, 'prf': prof}
    return render(
        request, 
        'index2.html', 
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

        st = Stats.objects.create(test=tst, user=usr, result=0)
        
            # request.session.get('test', 0)
        request.session['test'] = int(t)
        request.session['currentid'] = 1
        request.session['count'] = quest.count()

        d = {"test": t, "user": u}
        
        TmpTest.objects.all().delete()  # очищаем временную таблицу

        # заполняем данными
        i = 1

        for q in quest: 
            request.session[str(i)] = q.id  
            test = TmpTest()
            test.qid = q.id
            test.ball = 0
            test.ans = False
            test.save()
            i += 1

        response = redirect("getquestion")

        # d = model_to_dict( q )
    # return JsonResponse(d)
    return response

#------------------      Выбираем нужный вопрос    --------------------------
def getquestion(request):
    count = TmpTest.objects.filter(ans = False).count()
    
    ans = TmpTest.objects.filter(ans=False).first()

    q = Questions.objects.get(id = ans.qid)
    a = Answers.objects.filter(question = q.id)
 
    data = {'q': q, 'a': a, 'count': count, 'ans': ans}

    response = render(
        request, 
        'templateTest.html', 
        context = data
    )
    
    return response
    
#------------------      Выбираем нужный вопрос    --------------------------

def getquestionfetch(request):
    data = {}
    v=0
    if (request.method=='POST'):
        count = TmpTest.objects.filter(ans = False).count()
        ans = TmpTest.objects.filter(ans = False).first()
        v = request.POST.get('answer')
        q = Questions.objects.get(id = ans.qid + 1)
        a = Answers.objects.filter(question = q.id)

        dd = request.session['4']
        data['count'] = dd

        # data['q'] = q.question
        # data['r'] = q.right_answer
        
        # i = 1
        # for an in a:
        #     data['answer' + str(i)] = a[i-1].name
        #     data['ball' + str(i)] = a[i-1].ball
        #     i += 1
        
    return JsonResponse(data)


# def test_begins(request):
#     disciplines = Tests.objects.all()
#     data = {'tst': disciplines}
#     return render(
#         request, 
#         'index2.html', 
#         context = data,
#     ) 
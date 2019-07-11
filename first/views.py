from django.shortcuts import render, HttpResponse, redirect
from django import views
from first.forms import *


# Create your views here.

def Base(request):
    # u_id = request.session.get('u_id')
    # u = UserInfo.objects.get(id=u_id)
    return render(request, 'base.html')


class Login(views.View):
    def get(self, request):
        return render(request, 'Login.html')
    def post(self, request):
        f = Logins(request.POST)
        if f.is_valid():
            username = f.cleaned_data.get('username')
            password = f.cleaned_data.get('password')
            # print(username, password)
            try:
                u = UserInfo.objects.get(username=username, password=password)
                request.session['u_id'] = u.id
                # print(u.username)
                # print(request.session.get('u_id'))
            except:
                return HttpResponse('此用户不存在')
            else:
                return redirect('save')
        else:
            return HttpResponse('登录失败')



class Save(views.View):
    def get(self, request):
        u_id = request.session.get('u_id')
        if u_id: # 相当于我用户已经登录
            u = UserInfo.objects.get(id=u_id)
            return render(request, 'Save.html', {'u': u})
        else:
            return redirect('login')

    def post(self, request):
        money = request.POST.get('money')
        u_id = request.session.get('u_id')
        if u_id:
            d = UserInfo.objects.get(id=u_id)
        else:
            return redirect('login')
        d.money += float(money)
        d.save()
        return HttpResponse('您已成功存储%s元' % money)


class Take(views.View):
    def get(self, request):
        u_id = request.session.get('u_id')
        if u_id:
            u = UserInfo.objects.get(id=u_id)
            return render(request, 'Take.html', {'u': u})

    def post(self, request):
        money = request.POST.get('money')
        u_id = request.session.get('u_id')
        if u_id:
            u = UserInfo.objects.get(id=u_id)
            if float(money)< u.money:
                u.money -= float(money)
                u.save()
                s = '您已成功取款%s元，您当前的余额为%.2f元' % (money, u.money)
                return HttpResponse(s)
            elif float(money)> money:
                return HttpResponse('您的账户余额不足以提供您的取款操作')
            else:
                u.money -= float(money)
                u.save()
                return HttpResponse('将为您全部取出')
        else:
            return redirect('login')



class Move(views.View):
    def get(self, request):
        u_id = request.session.get('u_id')
        if u_id:
            u = UserInfo.objects.get(id=u_id)
            return render(request, 'move.html', {'u': u})
        else:
            return redirect('login')


    def post(self, request):
        card_num = request.POST.get('card_num_2')
        money = request.POST.get('card_money')
        u_id = request.session.get('u_id')
        u = UserInfo.objects.get(id=u_id)
        try:
            u1 = UserInfo.objects.get(card_num=card_num)
        except:
            return HttpResponse('此卡号不存在')
        else:
            if float(money) < u.money:
                u.money -= float(money)
                u1.money += float(money)
                u.save()
                u1.save()
                return HttpResponse('您已成功转账给卡号为%s的用户%s元，您当前的余额为%.2f元' % (card_num, money, u.money))
            elif float(money) > u.money:
                return HttpResponse('您的账户余额不足以提供您的转账操作')
            else:
                u.money -= float(money)
                u1.money += float(money)
                u.save()
                u1.save()
                s = '您已成功转账给卡号为%s的用户%s元，您当前的余额为%.2f元' % (card_num, money, u.money)
                return HttpResponse(s)


def exit(request):
    request.session.flush()
    return redirect('login')











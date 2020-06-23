from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import *


# Create your views here.


def index(request):
    return HttpResponse('index')


# 提交接口
def put_user_info(request):
    if request.method == "GET":
        return render(request, 'put.html')
    else:
        # 获取用户输入的客户端id，分数
        new_clientId = request.POST.get('client_id')
        new_grade = request.POST.get('grade')
        # 获取到用户信息表
        try:
            user = UserInfo.objects.get(client_id=new_clientId)
            user.grade = new_grade
            user.save()
        except:
            new_user = UserInfo()
            new_user.client_id = new_clientId
            new_user.grade = new_grade
            new_user.save()
    return HttpResponse('当前客户端号：{}，分数：{}'.format(new_clientId, new_grade))


# 获取用户排名
def get_grade_ranking(request):
    # 获取用户提交的客户端ID和查询范围
    if request.method == "GET":
        return render(request, 'get_ranking.html')
    else:
        clientId = request.POST.get('client_id')
        try:
            user_data = UserInfo
            user = user_data.objects.get(client_id=clientId)
            value_min = int(request.POST.get('value_min'))
            value_max = int(request.POST.get('value_max'))
            # 获取当前所有用户数据，做对比
            all_grades = user_data.objects.values_list('grade')
            print('--------------当前所有grade', all_grades)
            grade_list = []
            for grade in all_grades:
                print('-----------当前grade', grade, type(grade))
                grade_list.append(int(grade[0]))
            grade_list = sorted(grade_list, reverse=True)
            print('---------cisipaixu', grade_list)
            # 按照排名获取该用户的对象列表
            current_user = {}
            users_list = []
            for count, grade in enumerate(grade_list):
                if user == user_data.objects.get(grade=grade):
                    current_user = {'info': user_data.objects.get(grade=grade), 'ranking': count}
                users_list.append({'info': user_data.objects.get(grade=grade), 'ranking': count})
            users_list = users_list[int(value_min): int(value_max)]
            users_list.append(current_user)
            # 加入当前端口ID及其数据
            print(users_list)
            return render(request, 'ranking.html', {'users_list': users_list, 'tags': ['id', '客户端ID', '分数']})
        except:
            return HttpResponse('请检查ID等信息是否正确')
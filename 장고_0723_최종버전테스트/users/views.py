from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from .models import User, Notice
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt




# Create your views here.

def main(request):
    return render(request, 'basic_layout.html')


def notice_view(request):
    qs = Notice.objects.all()  # 팀 정보 가져오기
    context = {'notice_list': qs}
    return render(request, 'notification_board.html', context)


def notDet_view(request, id):
    qs = Notice.objects.get(id=id)
    context = {'notice_info': qs}
    return render(request, 'notification_detail.html', context)


def manage_view(request):
    return render(request, 'team_manage.html')


def intro_view(request):
    return render(request, 'introduction_base.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            login(request, user)
            return render(request, "basic_layout.html")
        else:
            print("인증실패")
    return render(request, "login_ver2.html")


def logout_view(request):
    logout(request)
    return redirect("user:main")  # user는 app_name임

@csrf_exempt
def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        passwordck = request.POST["passwordck"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        gender = request.POST["gender"]
        birth_year = request.POST["birth_year"]
        birth_month = request.POST["birth_month"]
        birth_day = request.POST["birth_day"]
        favorite = request.POST["favorite"]
        stu_num = request.POST["stu_num"]
        nname = request.POST["nname"]

        user = User.objects.create_user(username, email, password)
        user.passwordck = passwordck
        user.last_name = lastname
        user.first_name = firstname
        user.stu_num = stu_num
        user.favorite = favorite
        user.birth_year = birth_year
        user.birth_month = birth_month
        user.birth_day = birth_day
        user.gender = gender
        user.nname = nname
        user.save()

        return redirect("user:login")

    return render(request, "sign_up.html")

'''
정보 수정
'''
def info_view(request):
    return render(request, "personal_info_modification.html")



'''
class BoardListView(LoginRequiredMixin, TemplateView):  # 게시글 목록
    login_url = '/login'

    template_name = 'board_main.html'
    queryset = Board.objects.all()  # 모든 게시글

    def get(self, request, *args, **kwargs):
        print(request.GET)
        ctx = {  # 템플릿에 전달할 데이터
            'boards': self.queryset
        }
        return self.render_to_response(ctx)


class BoardDetailView(TemplateView):
    template_name = 'board_detail.html'
    queryset = Board.objects.all()
    pk_url_kwargs = 'board_id'  # 검색데이터의 primary key를 전달받을 이름

    def get_object(self, queryset=None):
        queryset = queryset or self.queryset  # queryset 파라미터 초기화
        pk = self.kwargs.get(self.pk_url_kwargs)  # pk는 모델에서 정의된 pk값, 즉 모델의 id
        return queryset.filter(pk=pk).first()  # pk로 검색된 데이터가 있다면 그 중 첫번째 데이터 없다면 None 반환

    def get(self, request, *args, **kwargs):
        board = self.get_object()
        if not board:
            raise Http404('invalid board_id')  # 검색된 데이터가 없다면 에러 발생

        ctx = {
            'board': board
        }
        return self.render_to_response(ctx)


class BoardCreateUpdateView(TemplateView):  # 게시글 추가, 수정
    template_name = 'board_update.html'
    queryset = Board.objects.all()
    pk_url_kwargs = 'board_id'
    success_message = '게시글이 저장되었습니다.'

    def get_object(self, queryset=None):
        queryset = queryset or self.queryset
        pk = self.kwargs.get(self.pk_url_kwargs)
        board = queryset.filter(pk=pk).first()

        if pk:
            if not board:
                raise Http404('invalid pk')
            elif board.b_id != self.request.user:  # 작성자가 수정하려는 사용자와 다른 경우
                raise Http404('작성자만 수정할 수 있습니다.')
        return board

    def get(self, request, *args, **kwargs):  # 화면 요청
        board = self.get_object()

        ctx = {
            'board': board,
        }
        return self.render_to_response(ctx)

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')  # request.POST 객체에서 데이터 얻기
        post_data = {key: request.POST.get(key) for key in ('b_title', 'b_note', 'b_writer')}
        for key in post_data:  # 세가지 데이터 모두 있어야 통과
            if not post_data[key]:
                messages.error(self.request, '{} 값이 존재하지 않습니다.'.format(key), extra_tags='danger')  # error 레벨로 메시지 저장
        post_data['b_id'] = self.request.user

        if len(messages.get_messages(request)) == 0:  # 메시지가 있다면 아무것도 처리하지 않음
            if action == 'create':
                board = Board.objects.create(**post_data)
                messages.success(self.request, self.success_message)  # success 레벨로 메시지 저장
            elif action == 'update':
                board = self.get_object()
                for key, value in post_data.items():
                    setattr(board, key, value)
                board.save()
                messages.success(self.request, self.success_message)  # success 레벨로 메시지 저장
            else:
                messages.error(self.request, '알 수 없는 요청입니다.', extra_tags='danger')  # error 레벨로 메시지 저장

            return HttpResponseRedirect('/board/')  # 정상적인 저장이 완료되면 '/board/'로 이동됨

        ctx = {
            'board': self.get_object() if action == 'update' else None
        }
        return self.render_to_response(ctx)
'''

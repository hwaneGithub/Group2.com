from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User, Board
from django.http import Http404
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def main(request):
    return render(request, 'index.html')


def board_main(request):
    return render(request, 'board_main.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            login(request, user)
            return render(request, "index.html")
        else:
            print("인증실패")
    return render(request, "login_ver1.html")


def logout_view(request):
    logout(request)
    return redirect("user:main")  # user는 app_name임


def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        nname = request.POST["nname"]

        user = User.objects.create_user(username, email, password)
        user.last_name = lastname
        user.first_name = firstname
        user.nname = nname
        user.save()

        return redirect("user:login")

    return render(request, "sign_up.html")


class BoardListView(TemplateView):  # 게시글 목록
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
    template_name = 'base.html'
    queryset = Board.objects.all()
    pk_url_kwargs = 'board_id'

    def get_object(self, queryset=None):
        queryset = queryset or self.queryset
        pk = self.kwargs.get(self.pk_url_kwargs)
        board = queryset.filter(pk=pk).first()

        if pk and not board:  # 검색결과가 없으면 곧바로 에러 발생
            raise Http404('invalid pk')
        return board

    def get(self, request, *args, **kwargs):  # 화면 요청
        board = self.get_object()
        if not board:
            raise Http404('invalid board_id')
        ctx = {
            'view': self.__class__.__name__,
            'data': board
        }
        return self.render_to_response(ctx)

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')  # request.POST 객체에서 데이터 얻기
        post_data = {key: request.POST.get(key) for key in ('b_title', 'b_note', 'b_writer')}
        for key in post_data:  # 세가지 데이터 모두 있어야 통과
            if not post_data[key]:
                raise Http404('no data for {}'.format(key))

        if action == 'create':  # board가 create일 경우
            board = Board.objects.create(b_title=b_title, b_note=b_note, b_writer=b_writer)
        elif action == 'update':  # board가 update일 경우
            board = self.get_object()
            if not board:
                raise Http404('invalid article_id')

            for key, value in post_data.items():
                setattr(board, key, value)
            board.save()
        else:  # board가 없거나 create, update 중 하나가 아닐 경우
            raise Http404('invalid action')

        ctx = {
            'view': self.__class__.__name__,
            'data': board
        }
        return self.render_to_response(ctx)  # 액션 작업 후 화면을 보냄

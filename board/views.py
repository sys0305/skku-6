from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from .forms import BoardForm, CommentForm
from .models import Board, Comment
from django.http import Http404


# Create your views here.
def board_list(request):
    board_list = Board.get_active_qs().all()
    # is_deleted를 False인 board만 조회하자.
    # is_delted False인 것 조회 어떻게 하지?
    # sql문에서 조건 걸어서 조회? - where
    # django에서 조건 걸어서 조회?

    response = render(request, "board/board-list.html",
                      {"board_list": board_list})
    return response


"""
[연습문제]
1. user가 방문한 게시글의 방문 히스토리를 트래킹해주세요. 
    (저장 예: 1번 게시글 -> 3번 게시글 -> 5번 게시글 ([1, 3, 5]) )
    - 쿠키 혹은 세션 어떤걸 사용하셔도 좋습니다.
    
2. (1)에 저장할 리스트의 최대 길이를 10으로 제한 하겠습니다. 
"""
from .utils import get_board_history_session, set_board_history_session
import json


def board_detail(request, board_id):
    # Session 이용 방법
    # set_board_history_session(request, board_id)
    # print(get_board_history_session(request))

    try:
        board = Board.get_active_qs().get(id=board_id)
    except Board.DoesNotExist:
        raise Http404()

    comment_list = board.comment_set.all()
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            data = form.data
            comment = Comment(content=data["content"], board_id=board_id)
            # Comment(content=form.data.content, board_id=board_id).save()

            comment.save()
            return redirect(f"/board/{board_id}")

    response = render(
        request,
        "board/board-detail.html",
        {
            "board": board,
            "comment_list": comment_list,
            "form": form
        },
    )
    HIST_COOKIE_KEY = "board-history"
    board_history = request.COOKIES.get("board-history")
    if not board_history:
        board_history = []
    else:
        board_history = json.loads(board_history)
    board_history += [board_id]
    if len(board_history) > 10:
        board_history[len(board_history) - 10:]
    response.set_cookie(HIST_COOKIE_KEY,
                        json.dumps(board_history),
                        httponly=True)

    return response


def board_write(request):
    form = BoardForm()
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/board")
    response = render(request, "board/board-write.html", {"form": form})
    return response


def board_delete(request):
    # 요청 URL example: /board/delete?board_id=...
    # GET 요청.
    board_id = request.GET["board_id"]
    deleted_count = Board.objects.filter(
        id=board_id, is_deleted=False).update(is_deleted=True)

    if deleted_count == 0:
        raise Http404()

    # board = Board.objects.get(id=board_id)
    # board.is_deleted = True
    # board.save()
    response = redirect("/board")
    return response


def board_modify(request, board_id):
    if request.method == "GET":
        board = Board.get_active_qs().get(id=board_id)
        form = BoardForm({
            "title": board.title,
            "content": board.content,
            "nickname": board.nickname
        })

        # print(board.get("title"))
        # form = BoardForm(board)

    elif request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            data = form.data

            Board.get_active_qs().filter(id=board_id).update(
                title=data["title"],
                content=data["content"],
                nickname=data["nickname"])

            return redirect(f"/board/{board_id}")
    else:
        raise HttpResponseNotAllowed()

    return render(request, "board/board-modify.html", {"form": form})


# def board_write(request):
#     # print(request)
#     # print(dir(request))
#     # for i in dir(request):
#     #     is_func = inspect.isfunction(request.__getattribute__(i))
#     #     print(i, is_func, request.__getattribute__(i))
#     #     print('-'*10)
#     print(request.method)  # HTTP Request Method (GET, POST, PUT, DELETE ...)
#     print(request.body)  # Request Body
#     print(request.POST)  # POST요청으로 온 Request Body를 Python객체화

#     if request.method == "GET":
#         # 글쓰기 페이지 조회
#         response = render(request, "board/board-write.html", {})
#         return response
#     if request.method == "POST":
#         # 글쓰기 작성 요청
#         title = request.POST["title"]
#         nickname = request.POST["nickname"]
#         content = request.POST["content"]
#         # Board Instance 생성
#         board = Board(title=title, nickname=nickname, content=content)
#         # 게시물 DB 반영 = board.save
#         board.save()
#         # response 전달
#         response = redirect("/board")
#         return response

from django.db import models
from django.core import validators


class BaseModel(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)  # DATETIME
    updated_at = models.DateTimeField(auto_now=True)  # DATETIME
    is_deleted = models.BooleanField(default=False)
    # deleted_at = models.DateTimeField(default=None)

    @classmethod
    def get_active_qs(cls):
        # 여러개 찾을 때.
        return cls.objects.filter(is_deleted=False)


# Create your modelWs here.
class Board(BaseModel):

    class Meta:
        indexes = [models.Index(fields=["title"], name="board_title_idx")]

    id = models.AutoField(
        primary_key=True)  # INTEGER - PRIMARY KEY - AUTO INCRMENT)
    title = models.CharField(
        "제목",
        max_length=255,
        validators=[
            validators.MinLengthValidator(3, "최소 세 글자 이상은 입력해주셔야 합니다.")
        ],
    )  # VARCHAR(255)
    content = models.TextField(
        "내용",
        validators=[
            validators.MinLengthValidator(10, "최소 10글자 이상은 입력하여 주셔야합니다.")
        ],
    )  # TEXT
    nickname = models.CharField(
        "닉네임",
        max_length=50,
        validators=[validators.MinLengthValidator(1, "닉네임을 입력하셔야합니다.")],
    )


class Comment(BaseModel):
    # code 작성
    board = models.ForeignKey(Board, on_delete=models.SET_NULL, null=True)
    content = models.CharField(max_length=255)


# Board (1) <- Comment(1)
# SET_NULL, SET_DEFAULT, CASCADE

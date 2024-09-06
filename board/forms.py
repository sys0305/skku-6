from django import forms

from .models import Board, Comment

class BootstrapModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._widget_update()

    def _widget_update(self):
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"


class BoardForm(BootstrapModelForm):

    class Meta:
        model = Board
        fields = [
            "title",
            "nickname",
            "content",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "제목을 입력하여 주세요."})
        }


class CommentForm(BootstrapModelForm):

    class Meta:
        model = Comment
        fields = [
            "content",
            #   "board_id"
        ]
        widgets = {
            "content": forms.TextInput(attrs={"placeholder": "댓글을 입력하여 주세요."}),
            # "board_id": forms.HiddenInput(),
        }


# class BoardForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._widget_update()

#     class Meta:
#         model = Board
#         fields = [
#             "title",
#             "nickname",
#             "content",
#         ]
#         widgets = {
#             "title": forms.TextInput(attrs={"placeholder": "제목을 입력하여 주세요."})
#         }

#     def _widget_update(self):
#         for visible in self.visible_fields():
#             visible.field.widget.attrs["class"] = "form-control"

# class CommentForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._widget_update()

#     class Meta:
#         model = Comment
#         fields = ["content"]
#         widgets = {
#             "content": forms.TextInput(attrs={"placeholder": "댓글을 입력하여 주세요."})
#         }

#     def _widget_update(self):
#         for visible in self.visible_fields():
#             visible.field.widget.attrs["class"] = "form-control"

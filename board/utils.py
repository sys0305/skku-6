SESSION_KEY = "board_history"


def set_board_history_session(request, board_id):
    if not request.session.get(SESSION_KEY):
        request.session[SESSION_KEY] = [board_id]
    else:
        request.session[SESSION_KEY] += [board_id]
        if len(request.session[SESSION_KEY]) > 10:
            # 10개 이상일 경우 마지막 10개만 남기기.
            request.session[SESSION_KEY] = request.session[SESSION_KEY][
                len(request.session[SESSION_KEY]) - 10:]
    return request.session[SESSION_KEY]


def get_board_history_session(request):
    return request.session.get(SESSION_KEY)

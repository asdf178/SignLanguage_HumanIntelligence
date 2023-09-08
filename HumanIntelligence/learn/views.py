from django.shortcuts import render
from HumanIntelligence.settings import IMAGE_LIST, VIDEO_LIST
from django.views.decorators.csrf import csrf_exempt
from utils import Decoding, CheckAction, CheckComplete, CreateAction, CompleteAction, GetActionComplete
from deep_learning import actions
from django.http import JsonResponse
from deep_learning import Predict, label_map

def learn(response):
    if response.method == "GET":
        if response.GET.get("word") in IMAGE_LIST.keys(): # 검색으로 접근
            action = response.GET.get("word")
            if 'sequence_learn' in globals() or 'sequence_learn' in locals(): # sequence가 존재하지 않는다면 생성하고, 존재한다면 초기화하는 로직
                refresh = "true"
            else:
                refresh = "false"

            return render(response, "learn/learn_v.html", {"action":action, "path":VIDEO_LIST[action], "url":"learn_v/", "actions":actions.tolist(), "refresh":refresh})

        for action, _ in IMAGE_LIST.items(): # 카드 클릭으로 접근
            if action in response.GET:
                if 'sequence_learn' in globals() or 'sequence_learn' in locals(): # sequence가 존재하지 않는다면 생성하고, 존재한다면 초기화하는 로직
                    refresh = "true"
                else:
                    refresh = "false"

                return render(response, "learn/learn_v.html", {"action":action, "path":VIDEO_LIST[action], "url":"learn_v/", "actions":actions.tolist(), "refresh":refresh})        

    complete, incomplete = GetActionComplete(response.user) # complete한 action은 초록색, incomplete한 action은 파란색

    return render(response, "learn/learn.html", {"image_list":IMAGE_LIST, "complete_list":complete, "incomplete_list":incomplete}) # html 페이지 렌더를 위해 한 번만 실행됨

@csrf_exempt # csrf 오류 방지
def learn_v(response):
    action = None # refered before assigned 에러 방지
    decoded_data = None # refered before assigned 에러 방지
    username = response.user # 로그인된 유저 이름

    if response.method == "POST": # ajax로부터 데이터 받음
        encoded_data = response.POST.get("encoded") # 인코딩된 데이터
        decoded_data = Decoding(encoded_data) # 디코딩

        if 'sequence_learn' not in globals(): # sequence를 한 번만 생성하고 매번 초기화가 되지 않게 함
            global sequence_learn
            sequence_learn = []

        if response.POST.get("refresh") == "true": # sequence 초기화함
            sequence_learn = []

        sequence_learn, res = Predict(sequence_learn, decoded_data) # 딥러닝으로 예측함

        action = response.POST.get("action") # ajax로부터 action 이름을 받을 수밖에 없음

        if not CheckAction(username, action): # action이 존재하지 않는다면 생성
            CreateAction(username, action)
        elif (not CheckComplete(username, action)) and res[label_map[action]] >= 0.7:
            # action complete이 안 됐고, 70점이 넘을 때 complete을 True로 바꿈
            CompleteAction(username, action)

        if CheckComplete(username, action): # action complete인지 아닌지 체크
            complete = "true"
        else:
            complete = "false"

        # ajax의 success로 response 보냄
        return JsonResponse({"res":res, "label_map":label_map, "length":len(sequence_learn), "complete":complete})

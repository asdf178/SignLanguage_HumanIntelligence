from django.shortcuts import render
from django.http import JsonResponse
from deep_learning import Predict, label_map, actions
from utils import Decoding, GetAction
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt # csrf 오류 방지
def exam(response):        
    if response.method == "POST": # ajax로부터 데이터 받음
        encoded_data = response.POST.get("encoded") # 인코딩된 데이터
        decoded_data = Decoding(encoded_data) # 디코딩
        username = response.user # 로그인된 유저 이름

        if 'sequence_exam' not in globals(): # sequence를 한 번만 생성하고 빈 리스트가 되지 않게 함
            global sequence_exam
            sequence_exam = []

        sequence_exam, res = Predict(sequence_exam, decoded_data) # 딥러닝으로 예측함

        if response.POST.get("clear") == "true": # ajax로 부터 complete 여부 받아옴
            correct = True
        else:
            correct = False
        
        action = response.POST.get("action") # refered before assigned 에러 방지
        if correct: # action complete 했을 때 다른 단어로 바꾸고, sequence 초기화
            action = GetAction(username) # 랜덤으로 유저가 학습한 단어 중 하나를 고름
            sequence_exam = []

        return JsonResponse({"res":res, "label_map":label_map, "action":action, "length":len(sequence_exam)}) # success로 response 보냄

    return render(response, "exam/exam.html", {"path":"", "url":"", "action":"not_exsit", "actions":actions.tolist()}) # html 페이지 렌더를 위해 한 번만 실행됨
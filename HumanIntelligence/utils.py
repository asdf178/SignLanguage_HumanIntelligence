import base64
import io
from PIL import Image
import numpy as np
import cv2

from django.contrib.auth.models import User

import random

def Decoding(data): # base64로 인코딩된 이미지를 numpy array로 디코딩 함
    string = data.replace('data:image/jpeg;base64,', '')
    imgdata = base64.b64decode(string)
    img = Image.open(io.BytesIO(imgdata))
    return cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

def CheckAction(username, action): # 로그인한 유저가 action을 학습한 적이 있는지 확인
    user = User.objects.filter(username=username)[0]
    if user.action.filter(name=action):
        return True
    else:
        return False
    
def CheckComplete(username, action): # 로그인한 유저가 action을 complete 했는지 확인
    user = User.objects.filter(username=username)[0]
    if user.action.filter(name=action)[0].complete:
        return True
    else:
        return False

def CreateAction(username, action): # 로그인한 유저 밑으로 action을 생성함
    user = User.objects.filter(username=username)[0]
    user.action.create(name=action)
    user.save()

def CompleteAction(username, action): # 로그인한 유저의 action을 complete을 true로 바꿈
    user = User.objects.filter(username=username)[0]
    a = user.action.filter(name=action)[0]
    a.complete = True
    a.save()

def GetAction(username): # 로그인한 유저가 학습한 적이 있는 action들 중 랜덤으로 하나를 뽑음
    user = User.objects.filter(username=username)[0]
    user_action = [i.name for i in list(user.action.all())]
    action = random.choice(user_action) 

    return action

def GetActionComplete(username):  # 로그인한 유저가 학습한 complete한 action과 incomplete한 action을 나눔
    user = User.objects.filter(username=username)[0]
    actions = user.action.all()
    complete = []
    incomplete = []
    for action in actions:
        if action.complete:
            complete.append(action.name)
        else:
            incomplete.append(action.name)

    return complete, incomplete
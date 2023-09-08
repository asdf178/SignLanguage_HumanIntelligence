import numpy as np
import cv2
import mediapipe as mp
from tensorflow import keras # 지우지 마셈
from keras.models import Sequential
from keras.layers import LSTM, Dense


def mediapipe_detection(image, model): # 모션 인식
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # color conversion
    image.flags.writeable = False # image is no longer writeable
    results = model.process(image) # make prediction
    image.flags.writeable = True # image is now writeable
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # color conversion
    return image, results

def extract_keypoints(results): # 몸, 얼굴, 왼손, 오른손의 키 포인트를 추출함
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(132)
    face = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(468*3)
    lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
    rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
    return np.concatenate([pose, face, lh, rh])

mp_holistic = mp.solutions.holistic # Holistic model
mp_drawing = mp.solutions.drawing_utils # Drawing utilities
sequence_length = 40 # 학습데이터의 동작별 영상 길이
actions = np.array(['감사하다', '고양이', '춥다', '개', '좋다', '기쁘다', '안녕하세요', '덥다', # 학습된 단어들
       '배고프다', '배부르다', '나', '싫다', '슬프다', '죄송하다', '감사하다',
       '힘들다', '우리', '왜', '걱정', '너']) 
label_map = {label:num for num, label in enumerate(actions)} # predict한 결과로 나온 list에서 action의 이름으로 값을 받기 위한 dictionary

model = Sequential() # 딥러닝 모델
model.add(LSTM(32, return_sequences=True, activation='sigmoid', input_shape=(sequence_length, 1662)))
model.add(LSTM(64, return_sequences=True, activation='sigmoid'))
model.add(LSTM(32, return_sequences=False, activation='sigmoid'))
model.add(Dense(32, activation='sigmoid'))
model.add(Dense(16, activation='sigmoid'))
model.add(Dense(actions.shape[0], activation='softmax'))
model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
model.load_weights('recognition_model.h5') # 학습한 weight들 불러옴

def Predict(sequence, image): # 사용자가 보낸 sequence(40개의 프레임으로 이루어진 영상)을 predict함
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        _, results = mediapipe_detection(image, holistic)
        keypoints = extract_keypoints(results)
        sequence.append(keypoints)
        sequence = sequence[-40:] # 40개의 연속된 동작을 인식하기 위한 슬레이싱
        if len(sequence) == 40: # 동작이 모두 collecting 됐을 때
            res = model.predict(np.expand_dims(sequence, axis=0),verbose=None)[0].tolist() # predict함 verbose는 print 안 하게 함 list로 바꿔야 함
        elif len(sequence) < 40: # 동작이 모두 collecting 되지 않았을 때
            res = np.zeros((20)).tolist() # 빈 리스트를 생성함
            
    return sequence, res # ajax와 통신할 때마다 sequence가 초기화되므로 view나 Predict 함수 중 적어도 하나에는 sequence에 대한 정보가 있어야 함




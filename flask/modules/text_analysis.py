### 모델에 필요한 import
import json
import numpy as np
import nltk
# tensorflow.keras.models.해야한다. 그냥 keras.models하면 로딩 안되더라
from tensorflow.keras.models import load_model
from konlpy.tag import Okt


class Tmodule() :
    def __init__(self):
        with open('./model/text_data/train_docs.json') as f:
            self.train_docs = json.load(f)
        with open('./model/text_data/test_docs.json') as f:
            self.test_docs = json.load(f)

        self.tokens = [t for d in self.train_docs for t in d[0]]
        # nltk.Text()는 여러 text에 관한 기능들을 제공한다.
        self.text = nltk.Text(self.tokens, name='NMSC')
        # 그 중 vacab()는 각 token의 빈도수를 dict형태로 가지고 있게 된다.
        self.selected_words = [f[0] for f in self.text.vocab().most_common(2000)]
        self.model = load_model('./model/model_2000.h5')
        self.okt = Okt()
        print('Module import Success!!!')

    ### 모델 관련 함수들
    def tokenize(self, doc):
        # norm은 정규화, stem은 근어로 표시하기를 나타냄
        return ['/'.join(t) for t in self.okt.pos(doc, norm=True, stem=True)]

    def term_frequency(self, doc):
        return [doc.count(word) for word in self.selected_words]

    def predict_pos_neg(self, review):
        token = self.tokenize(review)
        tf = self.term_frequency(token)
        # np.expand_dims는 차원을 늘리는 함수
        # axis=0은 행 (행자리에 숫자 추가됨)
        # e.g) shape : (2,) => (1,2)
        # model에 들어갈 input shape을 맞춰주기 위한 것
        data = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)
        score = float(self.model.predict(data))
        if(score > 0.5):
            return '긍정적', review, score * 100
            #return "[ {} ]는 {:.2f}% 확률로 < 긍정적 > 입니다 ^^".format(review, score * 100)
        else :
            return '부정적', review, (1 - score) * 100
            #return "[ {} ]는 {:.2f}% 확률로 < 부정적 > 입니다 ㅠㅠ".format(review, (1 - score) * 100)

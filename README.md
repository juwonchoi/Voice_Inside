
# 목소리를 통한 감정 구분 서비스 Voice_Inside 
## 프로젝트 개요
- 프로젝트명 :  당신의 감정을 맞추어 드립니다.
- 프로젝트 동기 
: 사람의 목소리만 듣고는 이 사람의 감정이 무엇인지 헷갈리는 경우가 종종 있습니다. 예를 들어 "참 잘한다"의 경우 두 가지 의미로 해석될 가능성이 있습니다. 첫째, 정말 잘한다는 긍정적인 의미입니다. 둘째,  뉘앙스에 따라 '잘 하는 짓이다'라는 부정적인 의미로 해석될 수 있습니다. 이런 오해를 조금이라도 줄여보고자 하는 아이디어에서 프로젝트를 시작하게 되었습니다.

## 개발환경
- OS : Window10
- Language : Python3.6
- Library : konlpy, librosa, gensim, 
- API : GCP Speech To Text
- Web Framework : Flask

## 시연영상
- 유튜브링크 : 

## 구현 기술
### 음성인식
- Google Cloud Platform의 Speech To Text  API를 활용하여 음성을 텍스트로 전환
### 텍스트 분석
- konlpy 라이브러리(한국어 정보처리를 위한 파이썬 패키지)를 활용해 Tokenize작업 진행
- 분석된 형태소를 Word2Vec, FastText, Doc2Vec, Count Based Vetorization 등 여러 방법을 활용해 벡터화 진행
- 이후 CNN, RNN, MLP 등 모델을 활용해 긍정/부정 Classification 진행
### 파형 분석
- librosa 라이브러리(음성 파일 분석 프로그램)을 활용해 3가지 특징 추출(MFCC, Chroma, Mel)
-  3가지 특징을 하나로 합쳐 벡터화 진행
- 이후 LSTM, CNN, MLP 등 모델을 활용해 긍정/부정 Classification 진행
### 텍스트, 파형 분석결과 합치기
- "문음(文音)일치도"라는 글과 음이 일치하는 정도를 수치화 하는 공식을 자체적으로 만들어 구현
### 웹서비스 구현
- Flask 웹프레임워크를 활용해 음성을 업로드 받아 감정결과를 보여주는 웹서비스 구현

## 프로젝트 일정

<img src="https://github.com/juwonchoi/Voice_Inside/blob/master/screenshot/schedule.PNG" width="40%" height="30%" ></img>
## 구조도
### 전체 구조도
<img src="https://github.com/juwonchoi/Voice_Inside/blob/master/screenshot/all_structure.PNG" width="40%" height="30%" ></img>
### 파형 분석 구조
<img src="https://github.com/juwonchoi/Voice_Inside/blob/master/screenshot/wave_sturcture.PNG" width="40%" height="30%" ></img>
### 텍스트 분석 구조
<img src="https://github.com/juwonchoi/Voice_Inside/blob/master/screenshot/text_structure.PNG" width="40%" height="30%"></img>
## 파일 설명
- flask : 프로젝트의 결과물인 웹 서비스가 실행되는 폴더
- model : 웹 서비스 전 모델을 학습시키고 피팅한 노트북 파일이 있는 폴더

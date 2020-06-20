from flask import Flask, render_template, request
# modules 폴더 안의 speech_to_text.py와 text_analysis.py를 import해서 사용하겠다!
from modules import speech_to_text, text_analysis, Wave_analysis
import os

app = Flask(__name__)

# Main Page
@app.route('/')
def index() :
    return render_template('index.html')

# Upload Page
#@app.route('/save_speech')
#def save() :
#    return render_template('save_speech.html')

# Upload Page에서 올린 파일을 분석하고 결과를 반환해주는 곳
@app.route('/saving', methods=['POST']) # POST, GET 형식 둘 다 받을 수 있다는 뜻
def file_save():
    f = request.files['recorder']
    # 사용자가 file을 엽로드하게 되면 server컴퓨터에 저장하고 그 file을 다시 가져오는 방식으로 구현
    f.save('./static/audio_files/'+ f.filename)
    # STT를 이용하기 위해 local_file_upload module 내 class를 불러온다.
    stt = speech_to_text.Speech()
    stt_result = stt.sample_recognize('./static/audio_files/'+ f.filename)
    # wave class 불러오기
    wave = Wave_analysis.Wave_analysis()
    feature_wave = wave.file_load('./static/audio_files/'+ f.filename)
    # 감정분석을 위해 text_module 내 class를 불러온다.
    tmodule = text_analysis.Tmodule()
    emo, review, percent = tmodule.predict_pos_neg(stt_result)
    emo_w,percent_w = wave.result_wave(feature_wave)
    cross_result,cross_img = wave.emo_cross(emo,emo_w,percent,percent_w)
    percent = '%.2f'%percent
    percent_w = '%.2f'%percent_w
    cross_result = '%.2f'%cross_result
    ## 체크모듈 만들기
    #img_scr = wave.save_wave_form('./static/audio_files/'+ f.filename)
    #return render_template('result.html', emo=emo,review=review,percent=percent,emo_w=emo_w,percent_w=percent_w,img_scr=img_scr)
    return render_template('result.html', emo=emo,review=review,percent=percent,emo_w=emo_w,percent_w=percent_w,cross_result=cross_result,cross_img=cross_img)

# Finished Code
if __name__ == '__main__' :
    app.run()

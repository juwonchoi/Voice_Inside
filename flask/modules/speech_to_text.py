from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io
import os

# '#c'라고 되어있는 코드들은 channel 관련 에러가 떠서 달아준 code들


class Speech() :
    def __init__(self) :
        ### 매번 경로 설정 해주기 힘들어서 python파일 실행되면 바로 경로설정 되게끔!
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="이 자리에 GCP에서 얻은 json파일 삽입"
        print('start speech!')


    def sample_recognize(self, local_file_path) :


        client = speech_v1.SpeechClient()

        language_code = "ko-KR"
        sample_rate_hertz = 44100  # wav파일 쓰려면48000
        audio_channel_count = 1 #c

        # When set to true, each audio channel will be recognized separately.
        # The recognition result will contain a channel_tag field to state which
        # channel that result belongs to
        enable_separate_recognition_per_channel = True #c


        # Encoding of audio data sent. This sample sets this explicitly.
        # This field is optional for FLAC and WAV audio formats.
        encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
        #encoding = enums.RecognitionConfig.AudioEncoding.MULAW
        config = {
            "audio_channel_count": audio_channel_count, #c
            "language_code": language_code,
            "sample_rate_hertz": sample_rate_hertz,
            "encoding": encoding,
            "enable_separate_recognition_per_channel": enable_separate_recognition_per_channel #c
        }

        with io.open(local_file_path, "rb") as f:
            content = f.read()
        audio = {"content": content }

        response = client.recognize(config, audio)
        for result in response.results:
            # First alternative is the most probable result
            alternative = result.alternatives[0]
            print(u"Transcript: {}".format(alternative.transcript))

        return alternative.transcript

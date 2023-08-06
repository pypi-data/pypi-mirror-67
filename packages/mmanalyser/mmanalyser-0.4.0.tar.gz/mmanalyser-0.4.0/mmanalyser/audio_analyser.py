# -*- coding: utf-8 -*-
import numpy as np
from mmanalyser.utils.vad import vad_robust
from pyAudioAnalysis import audioTrainTest as aT
import logging
import os
import subprocess


class AudioAnalyser:
    '''
    音频分析器

    '''
    def __init__(self, rationality_service_url=None):
        self.logger = logging.getLogger(self.__class__.__name__)

    def is_valid_audio(self, audio_path, human_voice_length=4):
        pred = self.is_human_voice(audio_path)
        return pred > 0.5, pred

    def is_human_voice(self, audio_path, human_voice_length=1):
        paths, voiced_range, voiced_duration, duration = vad_robust(
            audio_path, span=3, chunk_dir='temp/')
        if voiced_duration >= human_voice_length:
            pred = float(
                np.mean([self.is_human_voice_snippet(x) for x in paths[1:]]))
        else:
            pred = 0
        return pred

    def is_human_voice_snippet(self, audio_path):
        pred = aT.file_classification(
            audio_path,
            os.path.join(os.path.dirname(os.path.dirname(__file__)),
                         'mmanalyser', 'data', "gbdt"),
            "gradientboosting")[1][0]
        return pred

    def delete_silence_snippet(self, audio_path, chunk_dir='temp/'):
        if chunk_dir is None:
            chunk_dir = 'temp/'
        return vad_robust(audio_path, chunk_dir='temp/')

    def convert_to_wav(self, source_path, desc_path):
        cmd = [
            "ffmpeg", "-i", f"{source_path}", "-f", "wav", "-ar", "16000",
            "-ac", "1", f"{desc_path}"
        ]
        self.logger.info(' '.join(cmd))
        obj = subprocess.Popen(cmd,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               stdin=subprocess.PIPE)
        status_code = obj.wait()
        return status_code

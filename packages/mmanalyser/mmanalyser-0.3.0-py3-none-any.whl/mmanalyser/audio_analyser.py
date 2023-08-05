# -*- coding: utf-8 -*-
from mmanalyser import config
import numpy as np
from pydub import AudioSegment
from mmanalyser.utils.vad import vad_robust
from pyAudioAnalysis import audioTrainTest as aT
import logging
import os

WORD_SEP = '#'
AUDIO_START_TIME = 500


class AudioAnalyser:
    '''
    音频分析器

    '''
    def __init__(self, rationality_service_url=None):
        self.logger = logging.getLogger(self.__class__.__name__)

    def is_human_voice(self, audio_path):
        paths, voiced_range, voiced_duration, duration = vad_robust(audio_path, span=3, chunk_dir='temp/')
        if voiced_duration >= 4:
            label = (float(np.mean([aT.file_classification(x, os.path.join(os.path.dirname(os.path.dirname(__file__)),'mmanalyser', 'data', "gbdt"), "gradientboosting")[1][0] for x in paths[1:]])) > 0.5)
        else:
            label = False
        return label

    def delete_silence_snippet(self, audio_path, chunk_dir='temp/'):
        if chunk_dir is None:
            chunk_dir = 'temp/'
        return vad_robust(audio_path, chunk_dir='temp/')




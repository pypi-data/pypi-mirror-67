import numpy as np
from .mfcc import fbank
from . import feature_extractor


class FilterBanks(feature_extractor.FeaturesExtractor):

    def __init__(self, features_num: int, samplerate: int = 16000, is_standardization=True, **kwargs):
        self.features_num = features_num
        self.is_standardization = is_standardization
        self.params = kwargs
        self.samplerate = samplerate

    def make_features(self, audio: np.ndarray) -> np.ndarray:
        """ Use `python_speech_features` lib to extract log filter banks from
        the features file. """
        audio = self.normalize(audio.astype(np.float32))
        audio = (audio * np.iinfo(np.int16).max).astype(np.int16)
        feat, energy = fbank(
            audio, nfilt=self.features_num, samplerate=self.samplerate, **self.params
        )
        features = np.log(feat)
        return self.standardize(features) if self.is_standardization else features

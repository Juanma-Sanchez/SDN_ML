import numpy as np

from keras.models import load_model
#from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform

from network_analyzer.analyzer.generic import GenericAnalyzer

class DefaultGuiAnalyzer(GenericAnalyzer):
    def __init__(self, model_file, samples_per_trace, collector, trainer, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._model = load_model(model_file)
        self._samples_per_trace = samples_per_trace
        self._trace = []
        self._abnormal = []
        self._collector = collector
        self._trainer = trainer

    def get_abnormal_probability(self, input_vector):
        with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
            prediction = self._model.predict(np.asarray(input_vector))
        return prediction[1]

    def run(self):
        while True:
            self._trace.append(self._collector.retrieve_traffic())
            if len(self._trace) > self._samples_per_trace:
                self._trace.pop(0)
                # TODO get probability of abnormal traffic
                input_vector = self._trainer.get_input_vector(self._trace)
                abnormal_probability = self.get_abnormal_probability(input_vector)
                # TODO display avg traffic, standard deviation per link and list of abnormal traffic probability over time

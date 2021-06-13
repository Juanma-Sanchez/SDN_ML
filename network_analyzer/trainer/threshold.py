from utils import yaml

from network_analyzer.trainer.generic import GenericTrainer

class DefaultThresholdTrainer(GenericTrainer):
    def __init__(self, network_trace_folder, model_file, abnormal_threshold, *args, **kwargs):
        self._network_trace_folder = network_trace_folder
        self._model_file = model_file
        self._threshold = abnormal_threshold

    def run(self):
        # TODO read all network traces
        # TODO check if network traces have been classified
        # TODO if not classify them using the threshold
        # TODO update classified network traces
        # TODO generate training set
        # TODO generate AI model from training set
        # TODO save model
        pass

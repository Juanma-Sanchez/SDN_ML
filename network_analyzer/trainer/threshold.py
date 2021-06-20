from utils import yaml

from network_analyzer.trainer.generic import GenericTrainer

class DefaultThresholdTrainer(GenericTrainer):
    def __init__(self, network_trace_folder, model_file, abnormal_threshold, *args, **kwargs):
        self._network_trace_folder = network_trace_folder
        self._model_file = model_file
        self._threshold = abnormal_threshold

    def get_input_vector(self, trace):
        result = []
        for sample in trace:
            average = 0
            deviation = 0
            number_of_ports = 0
            for switch in sample:
                for port in sample[switch]:
                    average += sample[switch][port]['sent'] + sample[switch][port]['received']
                    number_of_ports += 2
            average = average/number_of_ports

            for switch in sample:
                for port in sample[switch]:
                    deviation += (sample[switch][port]['sent'] - average) ** 2
                    deviation += (sample[switch][port]['received'] - average) ** 2
            deviation = deviation/number_of_ports
            result.append((average, deviation))
        return result

    def run(self):
        # TODO read all network traces
        # TODO check if network traces have been classified
        # TODO if not classify them using the threshold
        # TODO update classified network traces
        # TODO generate training set
        # TODO generate AI model from training set
        # TODO save model
        pass

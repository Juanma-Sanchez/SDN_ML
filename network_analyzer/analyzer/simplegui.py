import requests

from network_analyzer.analyzer.generic import GenericAnalyzer

class DefaultGuiAnalyzer(GenericAnalyzer):
    def __init__(self, model_file, samples_per_trace, sdn_host, sdn_user, sdn_password, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._model = None # TODO load model file
        self._samples_per_trace = samples_per_trace
        self._base_url = sdn_host
        self._client = requests.Session()
        self._client.auth = (sdn_user, sdn_password)
        self._trace = []
        self._abnormal = []

    def retrieve_statistics(self) -> tuple:
        # TODO retrieve netowrk statistics from ONOS
        # TODO calculate average and standard deviation bps per link 
        return (0, 0)

    def run(self):
        while True:
            self._trace.append(self.retrieve_statistics())
            if len(self._trace) > self._samples_per_trace:
                self._trace.pop(0)
                # TODO get probability of abnormal traffic
                # TODO display avg traffic, standard deviation per link and list of abnormal traffic probability over time
            break

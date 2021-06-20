import os
import requests

from utils import yaml
from network_analyzer.collector.generic import GenericCollector


class DefaultOnosCollector(GenericCollector):
    def __init__(self, network_trace_folder, samples_per_trace, number_of_traces, sdn_host, sdn_user, sdn_password, *args, **kwargs):
        self._network_trace_folder = network_trace_folder
        self._samples_per_trace = samples_per_trace
        self._number_of_traces = number_of_traces
        self._current_trace = 0
        self._trace = []
        self._base_url = sdn_host
        self._client = requests.Session()
        self._client.auth = (sdn_user, sdn_password)

    def retrieve_traffic(self) -> dict:
        # TODO connect to ONOS and retrieve traffic per link
        
        return {}

    def save_trace(self):
        yaml.dump(
            dict(data=self._trace),
            os.path.join(self._network_trace_folder, f'network_trace_{self._current_trace}.yaml')
        )

    def run(self):
        while self._current_trace < self._number_of_traces:
            self._trace.append(self.retrieve_traffic())
            if len(self._trace) > self._samples_per_trace:
                self._trace.pop(0)
                self.save_trace()
                self._current_trace += 1


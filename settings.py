import os


# SDN Controller Settings
SDN_HOST = "http://localhost:8181"
SDN_USER = 'karaf'
SDN_PASSWORD = 'karaf'

# Network Analyzer Settings
COLLECTOR = network_analyzer.collector.onos.DefaultOnosCollector
TRAINER = network_analyzer.trainer.threshold.DefaultThresholdTrainer
ANALYZER = network_analyzer.analyzer.simplegui.DefaultGuiAnalyzer

NETWORK_TRACE_FOLDER = 'network_trace'
MODEL_FILE = 'model/model.h5'
SAMPLES_PER_TRACE = 10
NUMBER_OF_TRACES = 200
ABNORMAL_THRESHOLD = 0.4

if not os.path.exists(NETWORK_TRACE_FOLDER):
    os.mkdir(NETWORK_TRACE_FOLDER)

if not os.path.exists(MODEL_FILE.split('/')[0]):
    os.mkdir(MODEL_FILE.split('/')[0])

COLLECTOR_SPECIFICATIONS: {
    "network_trace_folder": NETWORK_TRACE_FOLDER,
    "samples_per_trace": SAMPLES_PER_TRACE,
    "number_of_traces": NUMBER_OF_TRACES,
    "sdn_host": SDN_HOST,
    "sdn_user": SDN_USER,
    "sdn_password": SDN_PASSWORD
}

TRAINER_SPECIFICATIONS: {
    "network_trace_folder": NETWORK_TRACE_FOLDER,
    "model_file": MODEL_FILE,
    "abnormal_threshold": ABNORMAL_THRESHOLD
}

ANALYZER_SPECIFICATIONS: {
    "model_file": MODEL_FILE,
    "samples_per_trace": SAMPLES_PER_TRACE,
    "sdn_host": SDN_HOST,
    "sdn_user": SDN_USER,
    "sdn_password": SDN_PASSWORD
}

import click

from settings import COLLECTOR, TRAINER, ANALYZER, COLLECTOR_SPECIFICATIONS, TRAINER_SPECIFICATIONS, ANALYZER_SPECIFICATIONS

@click.command()
@click.option('--collector', is_flag=True, help='Start the collector')
@click.option('--trainer', is_flag=True, help='Start the trainer')
@click.option('--analyzer', is_flag=True, help='Start the analyzer')
def run_analyzer(collector, trainer, analyzer):
    if collector:
        print('\n---INITIALIZING COLLECTOR---\n')
        COLLECTOR(**COLLECTOR_SPECIFICATIONS).run()
        print('\n---INITIALIZING TRAINER---\n')
        TRAINER(**TRAINER_SPECIFICATIONS).run()
        print('\n---INITIALIZING ANALYZER---\n')
        ANALYZER(**ANALYZER_SPECIFICATIONS).run()
    elif trainer:
        print('\n---INITIALIZING TRAINER---\n')
        TRAINER(**TRAINER_SPECIFICATIONS).run()
        print('\n---INITIALIZING ANALYZER---\n')
        ANALYZER(**ANALYZER_SPECIFICATIONS).run()
    else:
        print('\n---INITIALIZING ANALYZER---\n')
        ANALYZER(**ANALYZER_SPECIFICATIONS).run()

if __name__ == '__main__':
    run_analyzer()
import os
import signal
import sys

from job_runner.cli import main as cli_main


def sigterm_handler(_signo, _stack_frame):
    signal.signal(signal.SIGTERM, signal.SIG_DFL)
    os.kill(0, signal.SIGTERM)


#################################################################


#################################################################
def main():
    os.nice(19)
    signal.signal(signal.SIGTERM, sigterm_handler)
    cli_main(sys.argv)

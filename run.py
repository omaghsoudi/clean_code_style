#!/usr/bin/python3
from pathlib import Path
from modules.core import print_variables
from initialize import set_argparse, setup_logger

# =============================================================================
# My Main Class
# =============================================================================
class run_my_code(object):
    def __init__(self):
        self.config = set_argparse()

        Path(self.config.outputs.output_dir).mkdir(parents=True, exist_ok=True)
        self.logger = setup_logger(path_to_logger=f"{self.config.outputs.output_dir}/log.log")
        self.logger.info(f"Started to compile the project.")


    def main_function(self):
        print_variables(self.config, self.logger)
        self.logger.info(f"Printing my print_test from config:    {self.config.variables.print_test}")
        # You can do anything from this point




# =============================================================================
# Run Everything
# =============================================================================
if __name__ == "__main__":
    RUN = run_my_code()
    RUN.main_function()

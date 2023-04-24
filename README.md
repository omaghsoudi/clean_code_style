# clean_code_style
My favorite code structure.

No specifc enviroment is needed to run this code as it is demo code. In future, a poetry file or `requirements.txt` is needed to version the code-base. In addition, adding a pre-commit hook, docker image, and proper packaging structure might be needed too.

This will give you help on the arguments can be changed through argparse:
```bash
python3 ./run.py -h
```

This is an example of how to run the code:
```bash
python3 ./run.py -c <path_to_your_config_file>/config.yaml -v 0.0.1
```

The code is associcated with a config file as an example is left in this repo. The variables can be set trough the yaml file or through the argparse (like `-v 0.0.1` in the above command to overwrite the variable). This in important to easily update the arguments and submit jobs.

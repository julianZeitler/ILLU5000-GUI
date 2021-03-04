Usage
======

Program Execution
------------------

Basic Execution
................

To run the program execute

.. code-block:: bash

    python3 DataAnalyzerApp *file_name* *key*

Where *file_name* is the name of the mat file
from which the program should take it's information
and *key* is the specified plotting type.

Command Line Arguments
.......................

Following arguments can be specified:

.. code-block:: bash

    usage: DataAnalyzerApp.py [-h] [-c] [-t] file key

    positional arguments:
      file          The Data file from witch the information should be taken.
      key           Key for specifying plot type.

    optional arguments:
      -h, --help    show this help message and exit
      -c, --create  Generate .mat file from python dict in data package.
      -t, --test    Supress display output for testing purposes.

With the argument `-c` / `--create` a `.mat` file will be generated.
The data for the file is provided by a dictionary specified in the `DataAnalyzer.Data.data` module.

`-t` / `--test_` is used for testing purposes, when a graphical output is unwanted.
With the argument, no graphical output will be generated.
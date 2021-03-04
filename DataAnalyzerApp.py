#! /usr/bin/python3
"""This is the main module of the project. Execute this module to run the program."""

from argparse import ArgumentParser
from matplotlib.pyplot import show

from DataAnalyzer.Data.data import save_mat
from DataAnalyzer.Plot.cl_plot import Plot


def main():
    """The main function takes command line arguments and executes the according parts of the program.
    .. todo:: take the correct arguments and handle them correctly. (When generating .mat file, use generated one)
    """
    parser = ArgumentParser()
    parser.add_argument('file', help='The Data file from witch the information should be taken.', type=str)
    parser.add_argument('key', help='Key for specifying plot type.', type=str)
    parser.add_argument('-c', '--create', help='Generate .mat file from python dict in data package.',
                        action='store_true')
    parser.add_argument('-t', '--test', help='Supress display output for testing purposes.', action='store_true')

    args = parser.parse_args()

    if args.create:
        save_mat('data.mat')

    plot = Plot(args.file, args.key)

    if not args.test:
        show()


if __name__ == '__main__':
    main()

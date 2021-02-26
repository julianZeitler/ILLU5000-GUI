#! /usr/bin/python3
from argparse import ArgumentParser
from matplotlib.pyplot import show

from analyzer.data.data import data_mat
from analyzer.plot.cl_plot import Plot


def main():
    parser = ArgumentParser()
    parser.add_argument('file', help='The data file from witch the information should be taken.', type=str)
    parser.add_argument('key', help='Key for specifying plot type.', type=str)
    parser.add_argument('-c', '--create', help='Generate .mat file from python dict in data package.',
                        action='create_true')
    parser.add_argument('-t', '--test', help='Supress display output for testing purposes.', action='test_true')

    args = parser.parse_args()

    plot = Plot(args.file, args.key)

    if not args.test:
        show()

    if args.create:
        data_mat()


if __name__ == '__main__':
    main()

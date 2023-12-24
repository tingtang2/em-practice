import sys
import argparse


class PPCA:

    def __init__(self):
        pass

    def fit(X):
        pass

    def _expectation():
        pass

    def _maximization():
        pass


def main() -> int:
    parser = argparse.ArgumentParser(
        description='fitting probablistic principal components analysis using expectation maximization')

    parser.add_argument('--dataset', default='gaussians', help='dataset to run PPCA on')
    parser.add_argument('--n_components', default=3, type=int, help='number of principal components to find')
    args = parser.parse_args()

    configs = args.__dict__

    return 0


if __name__ == '__main__':
    sys.exit(main())

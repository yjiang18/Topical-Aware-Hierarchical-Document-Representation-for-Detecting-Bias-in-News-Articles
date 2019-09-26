from lda_han import LDA_HAN
from lda_HCAN import LDA_HCAN
from utils.normalize import normalize
import numpy as np
import argparse

SAVED_MODEL_DIR = 'checkpoints'
SAVED_MODEL_FILENAME = 'lda_HAN_best.h5'

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("-train", default=True, type=bool, required=False, help="train model if true")
    parser.add_argument("-txt", default="this is a test", type=str, required=False, help="test activation maps")
    args = parser.parse_args()

    model = LDA_HCAN()
    if args.train:
        model.train()
    else:
        model.load_weights(SAVED_MODEL_DIR, SAVED_MODEL_FILENAME)

        txt = args.txt

        activation_maps = model.activation_maps(txt)
        print(activation_maps)

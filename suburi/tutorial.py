from pathlib import Path
import tensorflow as tf
from tensorflow import keras

import os
import tempfile
import numpy as np
import pandas as pd

import sklearn
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from suburi.extractor import extract_xml

def main():
    extract_xml(Path.cwd() / 'data/raw/livedoor-news')

if __name__ == '__main__':
    main()

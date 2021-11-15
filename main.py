# import tensorflow as tf
from pathlib import Path
from suburi.extractor import extract_xml

# print(tf.__version__)

extract_xml(Path.cwd() / 'data/raw/livedoor-news')

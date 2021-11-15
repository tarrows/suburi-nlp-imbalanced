from pathlib import Path
from xml.etree import ElementTree as ET
import pandas as pd

def extract_xml(root_dir: Path):
    assert root_dir.exists() and root_dir.is_dir()

    records = []

    for item in root_dir.iterdir():
        if item.suffix != '.xml':
            continue
        # print(f'{"-" * 5} parse {item.name} {"-" * 5}')

        tree = ET.parse(item)
        root = tree.getroot()

        titles = root.findall('./doc/field[@name="title"]')

        for title in titles:
            # print(title.text)
            records.append({
                'category': item.name.replace('.xml', ''),
                'title': title.text,
            })

    df = pd.DataFrame(records)

    print(df.head())

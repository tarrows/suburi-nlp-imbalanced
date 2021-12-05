from pathlib import Path
from xml.etree import ElementTree as ET
import pandas as pd

def extract_xml(root_dir: Path):
    assert root_dir.exists() and root_dir.is_dir()

    records = []

    for item in root_dir.iterdir():
        if item.suffix != '.xml':
            continue

        tree = ET.parse(item)
        root = tree.getroot()

        # titles = root.findall('./doc/field[@name="title"]')

        # for title in titles:
        #     # print(title.text)
        #     records.append({
        #         'category': item.name.replace('.xml', ''),
        #         'title': title.text,
        #     })

        for doc in root.findall('doc'):
            title = doc.find('./field[@name="title"]')
            body = doc.findall('./field[@name="body"]')

            description = [
                line.text if line.text is not None else '' for line in body
            ]

            records.append({
                'category': item.name.replace('.xml', ''),
                'title': title.text,
                'body': '\n'.join(description),
            })

    df = pd.DataFrame(records)

    df.info()
    print(df['category'].value_counts())

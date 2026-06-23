from zipfile import ZipFile
from xml.etree import ElementTree as ET
import os

files = [
    r'BNCFT_OTOC量子混沌_深度文献.docx',
    r'BNCFT_三维主题_深度文献综述.docx',
    r'BNCFT_母方程混沌性_计算报告.docx'
]

for fname in files:
    path = os.path.abspath(fname)
    print('FILE:', path)
    try:
        with ZipFile(path) as z:
            xml = z.read('word/document.xml')
        tree = ET.fromstring(xml)
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        texts = [node.text for node in tree.findall('.//w:t', ns) if node.text]
        print(''.join(texts)[:2000])
    except Exception as e:
        print('ERR', e)
    print('-'*80)

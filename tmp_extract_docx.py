from pathlib import Path
from zipfile import ZipFile
import re
files = ['claude/claude/files/BNCFT_偏序推时空_探索报告.docx', 'claude/claude/files/BNCFT_局域性涌现_阶段报告.docx']
for name in files:
    p = Path(name)
    out = Path('temp_' + p.stem + '.txt')
    with ZipFile(p) as z:
        xml = z.read('word/document.xml').decode('utf-8', errors='ignore')
        text = '\n'.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', xml))
    out.write_text(text, encoding='utf-8')
    print('written', out)

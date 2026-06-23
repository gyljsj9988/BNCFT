import json
from pathlib import Path
paths = {
    'diamond4': Path(r'f:\BNCFT\验证\9\BICFT_R1_AuditRerunRun_20260427_053300\rerun_workspace\BICFT_R1_ReRun_Minimal_20260427_053300\diamond4'),
    'causal_lattice_1p1': Path(r'f:\BNCFT\验证\9\BICFT_R1_AuditRerunRun_20260427_053300\rerun_workspace\BICFT_R1_ReRun_Minimal_20260427_053300\causal_lattice_1p1'),
    'main_renamed': Path(r'f:\BNCFT\验证\9\BICFT_R1_AuditRerunRun_20260427_053300\rerun_workspace\BICFT_R1_ReRun_CoarseSpectrum_20260427_053300\main_renamed'),
}
for name, p in paths.items():
    print('---', name, '---')
    events = json.loads((p / 'events.json').read_text(encoding='utf-8'))
    print('events=', len(events))
    for fname in ['direct_edges.json', 'prec_edges.json', 'hasse_edges.json', 'slices.json']:
        fpath = p / fname
        if fpath.exists():
            data = json.loads(fpath.read_text(encoding='utf-8'))
            print(fname, type(data).__name__, len(data) if hasattr(data, '__len__') else 'scalar')

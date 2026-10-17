"""Review-first content intake. Never copies an unlicensed PDF into public output.
Usage: python scripts/content_pipeline.py input.json output.json
Optional private PDF inventory: --pdf path.pdf (requires pypdf)
"""
import argparse, json, hashlib
from pathlib import Path

def validate(rows):
    seen=set(); output=[]
    for row in rows:
        issues=[]
        for field in ('id','type','source','license_status','review_status','content'):
            if not row.get(field): issues.append('Missing '+field)
        key=hashlib.sha256(json.dumps(row.get('content'),ensure_ascii=False,sort_keys=True).encode()).hexdigest()
        if key in seen: issues.append('Duplicate content')
        seen.add(key)
        if row.get('license_status') not in ('original','licensed'): issues.append('Not authorized for export')
        if row.get('review_status')!='verified': issues.append('Manual review required')
        if row.get('type')=='question':
            c=row.get('content',{})
            if not isinstance(c.get('answer'),int) or not 0<=c.get('answer',-1)<len(c.get('options',[])): issues.append('Invalid answer')
            if not c.get('explanation'): issues.append('Missing explanation')
        output.append({**row,'issues':issues})
    return output
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--pdf');args=p.parse_args()
    if args.pdf:
        from pypdf import PdfReader
        pdf=PdfReader(args.pdf)
        print(f'Private inventory: {len(pdf.pages)} pages; extracted text is not exported. Rights review required.')
    result=validate(json.loads(Path(args.input).read_text()))
    Path(args.output).write_text(json.dumps({'verified':[r for r in result if not r['issues']],'review_queue':[r for r in result if r['issues']]},ensure_ascii=False,indent=2))

from tqdm import tqdm
import json
import collections
import warnings

def load_collection(path, image_included=False):
    data = dict()
    fi = open(path, 'r')
    for line in tqdm(fi):
        item = json.loads(line.strip())
        # [bug] valule `docid` is inccoret
        doc_id = item.pop('doc_id')
        title = item.pop('title', '')
        desc = item.pop('desc', '')
        data[doc_id] = {'title': title, 'description': desc}
    return data
        
def load_query(path):
    data = dict()
    with open(path, 'r') as f:
        for line in f:
            qid, qtext = line.strip().split('\t')
            data[qid] = qtext.strip()
    return data

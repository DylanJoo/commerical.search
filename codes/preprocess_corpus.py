import os
from tqdm import tqdm
import collections
import argparse
import requests
import json
from utils import load_collection

# Collection
CORPUS='/tmp2/trec/pds/data/collection/collection_full.jsonl'
def get_simplified_collection():
    CORPUS_SIM='/tmp2/trec/pds/data/collection/collection.jsonl'
    fo = open(CORPUS_SIM, 'w')
    with open(CORPUS, 'r') as fi:
        for line in tqdm(fi):
            data = json.loads(line.strip())
            doc_id = data['doc_id']
            title = data.pop('title', '')
            description = data.pop('decription', '')
            contents = f"{title} {description}".strip()

            if data['type'] != 'error':
                fo.write(json.dumps({'id': doc_id, 'contents': contents}, ensure_ascii=False)+'\n')

IMGLIST='/tmp2/trec/pds/data/collection/collection-imgs.json'
GALLERY='/tmp2/trec/pds/data/images/'
def download_image_collection():
    with open(IMGLIST, 'r') as fi:
        for line in tqdm(fi):
            data = json.loads(line.strip())
            doc_id = data['doc_id']
            img_url = data.pop('image_url', None)
            if img_url is not None:
                fo = open(os.path.join(GALLERY, f"{doc_id}.jpg"), 'wb')
                fo.write(requests.get("https://m.media-amazon.com/images/I/81bdoltQWVL.__AC_SY300_SX300_QL70_FMwebp_.jpg").content)
                fo.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", type=str, required=False)
    parser.add_argument("--get_simplified_collection", action='store_true', default=False)
    parser.add_argument("--download_image_collection", action='store_true', default=False)
    args = parser.parse_args()

    if args.get_simplified_collection:
        get_simplified_collection()

    if args.download_image_collection:
        download_image_collection()

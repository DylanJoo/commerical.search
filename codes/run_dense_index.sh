ENCODER=/tmp2/trec/pds/retrievers/ance-msmarco-passage/
COLLECTIONS=/tmp2/trec/pds/data/collection/collection_sim.jsonl

# encode title and description
INDEX=/tmp2/trec/pds/indexes/ance-sim/
python encode/retrieve.py input \
    --corpus $COLLECTIONS \
    --fields title description \
    --shard-id 0 \
    --shard-num 1 output \
    --embeddings $INDEX \
    --to-faiss encoder \
    --encoder-class ance \
    --encoder $ENCODER \
    --fields title description \
    --batch 32 \
    --fp16 \
    --device cuda:2

# encode title and description
INDEX=/tmp2/trec/pds/indexes/ance-sim-title/
python encode/retrieve.py input \
    --corpus $COLLECTIONS \
    --fields title \
    --shard-id 0 \
    --shard-num 1 output \
    --embeddings $INDEX \
    --to-faiss encoder \
    --encoder-class ance \
    --encoder $ENCODER \
    --fields title \
    --batch 48 \
    --fp16 \
    --device cuda:0

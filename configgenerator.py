import json

jsondata = {
    "word2vecfile": "./data/word2vec/GoogleNews-vectors-negative300.bin",
    "choidataset": "./data/choi",
    "wikidataset": "./data/wikipedia",
}

with open('config.json', 'w') as f:
    json.dump(jsondata, f)

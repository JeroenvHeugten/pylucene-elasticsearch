# pylucene-elasticsearch
Scripts to extract data from Elasticsearch files (without a running cluster)

### read_merged_segments.py

Python script to gather JSON data from Lucene files.
- Requires PyLucene installed. Follow instructions on http://lucene.apache.org/pylucene/install.html. 
- The sample data is created using Elasticsearch 5.6.8 and tested with PyLucene 6.5.0. 

Usage:
```bash
read_merged_segments.py sample_data/POLpaai6S1aXNp27d4dUng
```

### parse_translog.py

Python script to gather JSON data from Elasticsearch transaction logs using regular expressions.

Usage:
```bash
parse_translog.py sample_data/translog-11.tlog
```

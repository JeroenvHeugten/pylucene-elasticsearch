#!/usr/bin/env python

import os, sys, lucene, re
from java.nio.file import Paths
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.store import FSDirectory

lucene.initVM(vmargs=['-Djava.awt.headless=true'])

elasticsearch_index = sys.argv[1]

for shard in os.listdir(elasticsearch_index):
    if shard.isdigit():

        # Open directory with Lucene index
        fullpath = "%s/%s/%s/index/" % (os.getcwd(), elasticsearch_index, shard)
        fsDirectory = FSDirectory.open(Paths.get(fullpath))
           
        # Open Lucene index
        indexReader = DirectoryReader.open(fsDirectory)
         
        for nr in range(0, indexReader.maxDoc()):
            contents =  indexReader.document(nr).toString()
            parsed_contents = re.search('\[((\w+|\s+)*)]',contents)
            print parsed_contents.group(1).replace(' ','').decode("hex")
            


import frontmatter
import marko
import os
import json

path = 'data/document/'

documents = os.listdir(path)

documents_data = []

for d in documents:
    doc = frontmatter.load(path+d+'/index.md')
    
    data = dict()

    # Example

    data['keys'] = list(doc.keys())
    data['metadata'] = doc.metadata
    data['body'] = marko.convert(doc.content)

    documents_data.append(data)


print(documents_data)

with open('json/documents.json', 'w') as fout:
    json.dump(documents_data, fout, indent=4, default=str)
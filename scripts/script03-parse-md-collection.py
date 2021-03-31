import frontmatter
import marko
import os
import json

def parse_md_collection ( path, gen_file_name, collection_name):
    documents = os.listdir(path)
    documents_data = []
    for d in documents:
        print(d)
        doc = frontmatter.load(path+d+'/'+gen_file_name)
        
        data = dict()

        # Example

        #data['keys'] = list(doc.keys())
        data['id'] = path+d
        data['metadata'] = doc.metadata
        data['body'] = marko.convert(doc.content)

        documents_data.append(data)
    
    with open('json/' + collection_name + '.json', 'w') as fout:
        json.dump(documents_data, fout, indent=4, default=str)

    return documents_data



def parse_md_file ( path, gen_file_name, file):

    doc = frontmatter.load(path+file+'/'+gen_file_name)
    
    data = dict()

    # Example

    #data['keys'] = list(doc.keys())
    
    data['id'] = path+file
    data['metadata'] = doc.metadata
    data['body'] = marko.convert(doc.content)

    
    with open('json/' + file + '.json', 'w') as fout:
        json.dump(data, fout, indent=4, default=str)

    return data


events = parse_md_collection('data/event/', 'index.md', 'events')
documents = parse_md_collection('data/document/', 'index.md', 'documents')
blogs = parse_md_collection('data/blog/', 'index.md', 'blogs')
organizations_intl = parse_md_collection('data/organization/international/', 'index.md', 'organizations_intl')
organizations_nso = parse_md_collection('data/organization/nso/', 'index.md', 'organizations_nso')
task_forces = parse_md_collection('data/task-force/', 'index.md', 'task_forces')
household_surveys = parse_md_collection('data/household-survey/', 'index.md', 'household_surveys')
iswghs = parse_md_file('data/', 'index.md', 'iswghs')
steering_committee = parse_md_file('data/', 'index.md', 'steering-committee')
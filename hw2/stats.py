import sys 
import lxml
from lxml import etree
import json


file_name = sys.argv[1]
result_name = sys.argv[2]

# result dictionary
d_result = {}

# get tree instance
f = open(file_name)
tree = etree.parse(f)

# number of files
num_files = 0
for element in tree.xpath("//inode[contains(type,'FILE')]"):
    num_files += 1
# max/min size of files
l_numBytes = tree.xpath("//numBytes/text()")
l_numbytes = []
for num in l_numBytes:
    l_numbytes.append(int(num))
if num_files == 0:
    pass
elif l_numbytes != []:   
    max_size = max(l_numbytes)
    min_size = min(l_numbytes)
else:   #There are files, but all of them don't have the 'numBytes' tag; Therefore by default the min and max sizes are both 0
    max_size = 0
    min_size = 0
# number of directory
num_dir = 0
for element in tree.xpath("//inode[contains(type,'DIRECTORY')]"):
    num_dir += 1
# max depth of the directory tree
l_depth = [] 
for element in tree.xpath("//directory"):
    l_depth.append(len(element))
max_depth = max(l_depth)

# put results in d_result
d_result['number of files'] = num_files
d_result['number of directories'] = num_dir
d_result['maximum depth of directory tree'] = max_depth
if num_files != 0:
    d_file_size = {}
    d_result['file size'] = d_file_size
    d_result['file size']['max'] = max_size
    d_result['file size']['min'] = min_size

with open(result_name,'w') as file:
        file.write(json.dumps(d_result))
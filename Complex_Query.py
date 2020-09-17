import requests
import re
import json
import sys

fields = [
    "file_name",
    "cases.submitter_id",
    "cases.project.project_id"
    ]

fields = ",".join(fields)

files_endpt = "https://api.gdc.cancer.gov/files"
# -----

lines = []
count = 0
submitter_ids = []

with open("test3.tsv") as fp:
	while True:
		count += 1
		line = fp.readline()
	
		if not line:
			break
	
		lines = line.strip().split("	")

		for x in lines:
			if x != "TCGA-BRCA" and re.search("TCGA-*", x) and x:
				submitter_ids.append(x)

responses_arr = []

for sub_id in submitter_ids:
	

# -----

# This set of filters is nested under an 'and' operator.
	filters = {
   	 "op": "and",
   	 "content":[
        {
        "op": "in",
        "content":{
            "field": "cases.project.primary_site",
            "value": ["breast"]
            }
        },
        {
        "op": "in",
        "content":{
            "field": "files.access",
            "value": ["open"]
            }
        },
        {
        "op": "in",
        "content":{
            "field": "files.data_format",
            "value": ["svs"]
            }
        },
		{
		"op": "in",
		"content":{
			"field": "cases.submitter_id",
			"value": [sub_id]
			}
		}
		
    	]
	}

# A POST is used, so the filter parameters can be passed directly as a Dict object.
	params = {
   	 	"filters": filters,
   	 	"fields": fields,
    	"format": "TSV",
    	"size": "20"
    	}

# The parameters are passed to 'json' rather than 'params' in this case
	response = requests.post(files_endpt, headers = {"Content-Type": "application/json"}, json = params)
	
	responses_arr.append(response.content.decode("utf-8"))

original_stdout = sys.stdout

with open('xt44.tsv', 'w') as f:
		
	sys.stdout = f
	for r in responses_arr:
		print(r)
	sys.stdout = original_stdout

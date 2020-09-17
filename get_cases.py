import requests
import sys
import json

fields = [
    "diagnoses.ajcc_pathologic_stage",
    "samples.sample_type",
    "project.project_id",
    "submitter_id"
    ]

fields = ",".join(fields)

files_endpt = "https://api.gdc.cancer.gov/cases"

# This set of filters is nested under an 'and' operator.
filters = {
    "op": "and",
    "content":[
        {
        "op": "in",
        "content":{
            "field": "primary_site",
            "value": ["Breast"]
            }
        },
        {
        "op": "in",
        "content":{
            "field": "demographic.race",
            "value": ["white"]
            }
        },
        {
            "op": "in",
            "content": {
                "field": "diagnoses.ajcc_pathologic_stage",
                "value": ["stage iia"]
            }
        },
        {
            "op": "in",
            "content": {
                "field": "project.program.name",
                "value": ["TCGA"]
            }
        },
        {
            "op": "in",
            "content": {
                "field": "demographic.gender",
                "value": ["female"]
            }
        }
    ]
}

# A POST is used, so the filter parameters can be passed directly as a Dict object.
params = {
    "filters": filters,
    "fields": fields,
    "format": "TSV",
    "size": "2000"
    }

# The parameters are passed to 'json' rather than 'params' in this case
response = requests.post(files_endpt, headers = {"Content-Type": "application/json"}, json = params)

original_stdout = sys.stdout

with open('test3.tsv', 'w') as f:
	sys.stdout = f
	print(response.content.decode("utf-8"))
	sys.stdout = original_stdout



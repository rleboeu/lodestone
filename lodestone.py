import requests
import sys
import json
import re
import os

print("Hi! I'm Lodestone.")
student_name = input("What's your name?\n> ")

fields = [
    "diagnoses.ajcc_pathologic_stage",
    "samples.sample_type",
    "project.project_id",
    "demographic.gender",
    "demographic.race",
    "case_id",
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

print("Compiling complete TSV (this may take a while)...")

original_stdout = sys.stdout

with open('test3.tsv', 'w') as f:
	sys.stdout = f
	print(response.content.decode("utf-8"))
	sys.stdout = original_stdout

original_stdout = sys.stdout

count = 0
lines = []
sheet = ""
with open('test3.tsv') as fp:
    with open('FINAL.tsv', 'w') as fout:
        sys.stdout = fout
        while True:
            count += 1
            line = fp.readline()

            if not line:
                break

            lines = line.strip().split("\t")

            if count == 1:
                print("Student\tCase ID\tGender\tRace\tAJCC Pathologic Stage\tNo. of Images")
            elif len(line) != 1:
                num_samples = 0
                for i in range(6, 11):
                    if lines[i] != '':
                        num_samples += 1
                print("{}\t{}\t{}\t{}\t{}\t{}".format(student_name, lines[11], lines[1], lines[2], lines[3], num_samples))
        sys.stdout = original_stdout

# ----- get cases ends here

fields = [
    "file_name",
    "cases.submitter_id"
    ]

fields = ",".join(fields)

files_endpt = "https://api.gdc.cancer.gov/files"

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

print("Compiling file data TSV.\nPlease do not exit the application or turn off your computer.")

original_stdout = sys.stdout

with open('xt44.tsv', 'w') as f:
		
	sys.stdout = f
	for r in responses_arr:
		print(r)
	sys.stdout = original_stdout

print("Compiled file data TSV.")


print("Parsing file data...")
line = ""
stripped_line_arr = []
with open('xt44.tsv') as fp:
    while True:
        line = fp.readline()

        if not line:
            break
        if line.strip() and "file_name" not in line:
            stripped_line_arr.append(line.strip('\n').split("\t"))

print("Finished parsing file data.")

print("\n\n{} files to download.\n\n".format(len(stripped_line_arr)))
print("Warning!!! Files are ready to download. If you interrupt the download, lose internet access,\nor turn off your computer, you may have to start the entire process over.")
input("Press Enter to start download...")

current_file = 1
tempcount = 0
for x in stripped_line_arr:
    os.system('mkdir -p {}'.format(x[0]))
    print("File #{} of {}".format(current_file, len(stripped_line_arr)))
    os.system('./gdc-client download {} --dir ./{}'.format(x[2], x[0]))
    os.system('echo {} >> ./{}/filenames.txt'.format(x[1], x[0]))
    current_file += 1

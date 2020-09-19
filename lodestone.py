import requests
import sys
import json
import re
import os

print("\n+++ PROJECT: LODESTONE +++\n")
student_name = input("ENTER NAME: ")

download_all_files = False
prompt = "\nEnter the number of your choice:\n1. All files that match criteria \n2. Specific Range of Files\n> "
sw = int(input(prompt))
if sw == 1:
    download_all_files = True
if sw == 2:
    download_all_files = False

items_per_page = 0
page_number = 0
if download_all_files == False:
    items_per_page = int(input("Files per page: "))
    page_number = int(input("Page to download: ")-1)

fields = [
    "diagnoses.ajcc_pathologic_stage",
    "samples.sample_type",
    "project.project_id",
    "demographic.gender",
    "demographic.race",
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

pnum = 0

with open('test3.tsv') as fp:
    with open('CASE_SET.tsv', 'w') as fout:
        sys.stdout = fout
        while True:
            count += 1

            if count % items_per_page == 0:
                pnum += 1

            line = fp.readline()

            if not line:
                break

            lines = line.strip().split("\t")

            if count == 1:
                print("Creator\tCase ID\tGender\tRace\tAJCC Pathologic Stage\tNo. of Images")
            elif len(line) != 1:
                if download_all_files == False:
                    if count >= items_per_page * page_number and count <= (items_per_page * page_number) + items_per_page:
                        num_samples = 0
                        for i in range(5, 10):
                            if lines[i] != '':
                                num_samples += 1
                        print("{}\t{}\t{}\t{}\t{}\t{}".format(student_name, lines[10], lines[0], lines[1], lines[2], num_samples))
                elif download_all_files == True:
                    num_samples = 0
                    for i in range(5, 10):
                        if lines[i] != '':
                            num_samples += 1
                    print("{}\t{}\t{}\t{}\t{}\t{}".format(student_name, lines[10], lines[0], lines[1], lines[2], num_samples))
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
page_num = 1

with open("test3.tsv") as fp:
    while True:
        count += 1

        if count % items_per_page == 0:
            page_num += 1

        line = fp.readline()
    
        if not line:
            break
    
        lines = line.strip().split("\t")
        if download_all_files == False:
            if count >= items_per_page * page_number and count <= (items_per_page * page_number) + items_per_page:
                for x in lines:
                    if x != "TCGA-BRCA" and re.search("TCGA-*", x) and x:
                        submitter_ids.append(x)
        elif download_all_files == True:
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
        "size": "2000"
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

'''
darwin = osx
win32 = windows
linux = linux
'''

#os.system('rm xt44.tsv test3.tsv')

if sys.platform == 'linux' or sys.platform == 'darwin':

    for x in stripped_line_arr:
        if tempcount < 5:
            os.system('mkdir -p ./DOWNLOADS/{}'.format(x[0]))
            print("File #{} of {}".format(current_file, len(stripped_line_arr)))
            os.system('./bin/gdc-client-{} download {} --dir ./DOWNLOADS/{}'.format(sys.platform, x[2], x[0]))
            os.system('mv ./DOWNLOADS/{}/{}/{} ./DOWNLOADS/{}/{}'.format(x[0], x[2], x[1], x[0], x[1]))
            os.system('rm -rf ./DOWNLOADS/{}/{}'.format(x[0], x[2]))
            current_file += 1
            tempcount += 1

elif sys.platform == 'win32':
    for x in stripped_line_arr:
        if tempcount < 5:
            os.system('mkdir -p .\\DOWNLOADS\\{}'.format(x[0]))
            print("File {} of {}".format(current_file, len(stripped_line_arr)))
            os.system('.\\bin\\gdc-client-{}.exe download {} --dir .\\DOWNLOADS\\{}'.format(sys.platform, x[2], x[0]))
            os.system('mv .\\DOWNLOADS\\{}\\{}\\{} .\\DOWNLOADS\\{}\\{}'.format(x[0], x[2], x[1], x[0], x[1]))
            os.system('rm -rf .\\DOWNLOADS\\{}\\{}'.format(x[0], x[2]))
            current_file += 1
            tempcount += 1

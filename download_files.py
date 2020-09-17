import requests
import json

fields = [
	"file_name",
]

fields = ",".join(fields)

files_endpt = "https://api.gdc.cancer.gov/files"

filters = {
	"op": "in",
	"content": {
		"field": "

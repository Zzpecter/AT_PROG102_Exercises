from validator import Validator
import json

class JsonValidator(Validator):

	def __init__(self, directory):
		self.EXT = '.json'
        self.errorLogs = []
        self.directory = directory
        self.files = get_files()

	def get_files(self):
		files = super().get_files()
		jFiles = []
		for f in files:
			if f.endswith((self.EXT)):
				jFiles.append(str(root + "/" + name))
		return jFiles

	def get_files_in_folder(self, folder):
		files = super().get_files()
		tempFiles = []

		for file in files:
		    if folder in file : 
		    	tempFiles.append(file)
		self.files = tempFiles

		
	def validate(self):
		return self.try_json_files() and try_json_for_property(rootDir + '/config.json', 'platform_version')

	def try_json_files(self):
		success = True

		for file in self.files:
		    try:
		        with open(file) as f:
		            json.load(f)
		    except ValueError as e:
		        success = False
		return success

	def try_json_for_property(self, propName, file):
	    with open(file) as f:
	        data = json.load(f)
	    if propName not in data:
	        return False
	    else:
	        return True
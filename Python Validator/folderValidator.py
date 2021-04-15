from validator import Validator
class FolderValidator(Validator):

	def __init__(self, directory):
		self.directory = directory
        self.errorLogs = []

	def validate(self):
		return self.check_folder_struct()

	def check_folder_struct(self):
	    rootFiles = os.listdir(self.directory)
	    appFolderExists, confFolderExists, moduleFolderExists = False, False, False
	    for f in rootFiles:
	        if f == 'applications':
	            appFolderExists = True
	        elif f == 'configurations':
	            confFolderExists = True
	        elif f == str(opt.module):
	            moduleFolderExists = True

	    #error logs
	    if not appFolderExists:
	        self.errorLogs.append('No applications folder found.')
	    if not confFolderExists:
	        self.errorLogs.append('No configurations folder found.')
	    if not moduleFolderExists:
	        self.errorLogs.append(f'No {opt.module} folder found.')

	    return (appFolderExists and confFolderExists and moduleFolderExists)
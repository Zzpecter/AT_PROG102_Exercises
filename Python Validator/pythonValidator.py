from validator import Validator
import py_compile

class PythonValidator(Validator):

	def __init__(self, directory):
		self.EXT = '.py'
        self.errorLogs = []
        self.directory = directory
        self.files = get_files()


	def validate(self):
		return self.compile_python() if len(self.files) > 0 else False

	def get_files(self):
		files = super().get_files()
		pyFiles = []
		for f in files:
			if f.endswith((self.EXT)):
				pyFiles.append(str(root + "/" + name))
		return pyFiles

	def compile_python(self, idx = None):
		success = True

		if idx = None:
			for f in self.files:
				try:
				    py_compile.compile(self.files[idx], doraise=True)
				except py_compile.PyCompileError:
				    success = False
				    break
		else:
			try:
			    py_compile.compile(self.files[idx], doraise=True)
			except py_compile.PyCompileError:
			    success = False
		return success
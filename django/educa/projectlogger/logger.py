class Logger:
	class __LogerObject():
		def __init__(self, file_name):
			self.file_name = file_name

		def _write_log(self, level, msg):
			with open(self.file_name, 'a') as log_file:
				log_file.write(f'[{level}] {msg} \n ')

		def info(self, msg):
			self._write_log('INFO', msg)


	instance = None

	def __new__(cls, filename):
		if not Logger.instance:
			Logger.instance = Logger.__LogerObject(filename)
		return Logger.instance

	def __getattr__(self, name):
		return getattr(self.instance, name)

	def __setattr__(self, name):
		return setattr(self.instance, name)
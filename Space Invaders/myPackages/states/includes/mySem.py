import threading

class mySem(threading.Thread):

	def __init__(self, func, threadLimiter, *args):

		threading.Thread.__init__(self)
		self.func = func
		self.lock = threadLock
		self.args = args

	def run(self):

		self.threadLimiter.acquire()
		self.func(self.args)
		self.threadLimiter.release()
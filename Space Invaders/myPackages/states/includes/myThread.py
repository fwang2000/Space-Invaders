import threading
class myThread(threading.Thread):

	def __init__(self, func, threadLock):

		threading.Thread.__init__(self)
		self.func = func
		self.lock = threadLock

	def run(self):

		self.lock.acquire()
		self.func()
		self.lock.release()
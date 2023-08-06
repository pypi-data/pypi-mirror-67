# pyRIST. Copyright 2019-2020 Mad Resistor LLP. All right reserved.
# Author: Kuldeep Singh Dhaka <kuldeep@madresistor.com>

class ResultException(Exception):
	"""
	Convert librist result code in Exception.

	In librist, all result code which are less than 0 are failure code.
	and everything else is success code.

	.. code-block:: python

		import rist
		try:
			# try to create a new client
			sender = rist.Sender()
		except rist.ResultException, e:
			print("Error creating client, error=%i", e.value)
	"""

	value = None
	"""result code"""

	def __init__(self, value):
		Exception.__init__(self)
		self.value = value

	def __str__(self):
		return "RIST(error=%i)" % self.value

	@staticmethod
	def act(r):
		"""
		Act on librist result code.
		This is intended for internal use.

		:param int r: librist result code
		:returns: *r*
		:raise ResultException: if result code *r* is less than 0 (failure)
		"""
		if r < 0: raise ResultException(r)
		return r

class RejectPeerException(Exception):
	"""
	Exception to be raised by auth connect callback to reject peer
	"""

	pass

import unittest
import os
from app import app

class AppClientTest(unittest.TestCase):

	def auth_login(self):
		response = app.get("/")
		self.assetEqual(response.status_code, 200)
		# import ipdb; ipdb.set_trace()
		# teste = app.test_client(self)
		# response = teste.get("/", content_type='html/text')
		# self.assetEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()

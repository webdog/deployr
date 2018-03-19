import github3

class GitHub(object):
	def __init__(self, username, token, ghe=False):
		self.username = username
		self.token = token

		if ghe:
			self.g = github3.github.GitHubEnterprise(url=ghe, username=self.username, token=self.token)
		else:
			self.g = github3.github(username=self.username, token=self.token)

	def oh_hello(self):
		self.
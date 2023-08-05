from .KMeans import KMeans, TimedOutKMeans
from pandas import DataFrame
from chronometry.progress import ProgressBar


class Elbow:
	def __init__(self, min_k, max_k, keep_models=False, timeout=None, **kwargs):
		self._min_k = min_k
		self._max_k = max_k
		self._models = None
		self._kwargs = kwargs
		self._keep_models = keep_models
		self._distortions = None
		self._inertias = None
		self._timeout = timeout

	def fit(self, X, echo=1, raise_timeout=True, y=None):
		if self._keep_models:
			self._models = {}

		self._distortions = {}
		self._inertias = {}

		progress_bar = ProgressBar(total=self._max_k - self._min_k + 1, echo=echo)
		error = ''
		for k in range(self._min_k, self._max_k + 1):
			progress_bar.show(amount=k - self._min_k, text=f'k = {k}{error}')
			kmeans = KMeans(num_clusters=k, timeout=self._timeout, **self._kwargs)
			kmeans.fit(X=X, raise_timeout=raise_timeout)
			if self._keep_models:
				self._models[k] = kmeans
			self._distortions[k] = kmeans.distortion
			self._inertias[k] = kmeans.inertia
			if kmeans.timedout:
				error = ' error'


		progress_bar.show(amount=progress_bar.total)

	@property
	def records(self):
		"""
		:rtype: list[dict]
		"""
		return [
			{'k': k, 'distortion': self._distortions[k], 'inertia': self._inertias[k]}
			for k in range(self._min_k, self._max_k + 1)
		]

	@property
	def data(self):
		"""
		:rtype: DataFrame
		"""
		return DataFrame.from_records(self.records)

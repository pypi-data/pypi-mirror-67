from sklearn.cluster import KMeans as _KMeans
from func_timeout import func_timeout, FunctionTimedOut

from .get_distortion import get_distortion


class TimedOutKMeans:
	pass


class KMeans:
	def __init__(self, num_clusters, timeout=None, **kwargs):
		self._num_clusters = num_clusters
		self._kmeans = _KMeans(n_clusters=num_clusters, **kwargs)
		self._distortion = None
		self._inertia = None
		self._timeout = timeout
		self._timedout = False

	def fit(self, X, y=None, raise_timeout=True):
		if self._timeout:
			try:
				func_timeout(timeout=self._timeout, func=self._kmeans.fit, kwargs={'X': X})
				self._distortion = get_distortion(X=X, kmeans_model=self._kmeans)
				self._inertia = self._kmeans.inertia_
			except FunctionTimedOut as e:
				self._timedout = True
				if raise_timeout:
					raise e
				else:
					self._kmeans = TimedOutKMeans()

		else:
			self._kmeans.fit(X=X)
			self._distortion = get_distortion(X=X, kmeans_model=self._kmeans)
			self._inertia = self._kmeans.inertia_

	@property
	def timedout(self):
		return self._timedout

	@property
	def distortion(self):
		return self._distortion

	@property
	def inertia(self):
		return self._inertia

class DataAnalyzer:
	def __init__(self, data):
    	self.data = data

	def _calculate_total_and_count(self):
    	total = sum(self.data)
    	count = len(self.data)
    	return total, count

	def _calculate_statistics(self):
    	total, count = self._calculate_total_and_count()
    	minimum = min(self.data) if self.data else None
    	maximum = max(self.data) if self.data else None
    	average = total / count if count != 0 else 0
    	return total, minimum, maximum, average

	def calculate_total(self):
    	total, _ = self._calculate_total_and_count()
    	return total

	def calculate_average(self):
    	_, _, _, average = self._calculate_statistics()
    	return average

	def calculate_minimum(self):
    	_, minimum, _, _ = self._calculate_statistics()
    	return minimum

	def calculate_maximum(self):
    	_, _, maximum, _ = self._calculate_statistics()
    	return maximum



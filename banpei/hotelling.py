import numpy as np
from scipy import stats
from banpei.base.model import Model


class Hotelling(Model):
    def __init__(self, data, threshold):
        super().__init__(data)
        self.threshold = threshold

    def detect(self):
        """
        Parameters
        ----------
        data : array_like
               Input array or object that can be converted to an array.
        threshold : float

        Returns
        -------
        List of tuples where each tuple contains index number and anomalous value.
        """
        data = self.data
        threshold = self.threshold

        # Set the threshold of abnormality
        abn_th = stats.chi2.interval(1-threshold, 1)[1]

        # Covert raw data into the degree of abnormality
        avg = np.average(data)
        var = np.var(data)
        data_abn = [(x - avg)**2 / var for x in data]

        # Abnormality determination
        result = []
        for (index, x) in enumerate(data_abn):
            if x > abn_th:
                result.append((index, data[index]))
        return result

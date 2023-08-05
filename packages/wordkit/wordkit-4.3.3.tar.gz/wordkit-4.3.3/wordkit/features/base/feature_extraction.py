"""Base class for feature extractors."""
import pandas as pd
from itertools import chain


class BaseExtractor(object):
    """Base class for feature extractors."""

    def __init__(self, field=None):
        """Initialize the extractor."""
        self.features = {}
        self.field = field

    def extract(self, X):
        """Extract features from a list of words."""
        # Unpack dataframes correctly.
        if isinstance(X, pd.DataFrame):
            if self.field is None:
                raise ValueError("You didn't pass a field value to the "
                                 "extractor but also passed a DataFrame.")
            X = X[self.field].values
        elif isinstance(X, pd.Series):
            X = X.values
        elif isinstance(X[0], dict):

            if self.field is None:
                raise ValueError("You didn't pass a field value to the "
                                 "extractor but also passed a dict.")
            X = [x[self.field] for x in X]

        if isinstance(X[0][0], str):
            all_symbols = set(chain(*X))
        elif isinstance(X[0][0], tuple):
            x_ = [chain.from_iterable(x) for x in X]
            all_symbols = set(chain(*x_))
        else:
            raise ValueError("Couldn't recognize type of data passed.")

        all_symbols = sorted(all_symbols)
        self.features = self._process(all_symbols)
        return self.features

    def _process(self, symbols):
        """Process the symbols and return features."""
        raise NotImplementedError()

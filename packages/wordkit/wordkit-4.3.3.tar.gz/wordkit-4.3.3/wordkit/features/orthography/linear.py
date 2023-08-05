"""Transform orthography."""
import numpy as np

from ..base.transformer import FeatureTransformer
from .feature_extraction import IndexCharacterExtractor


class LinearTransformer(FeatureTransformer):
    """
    A vectorizer to convert words to vectors based on characters.

    LinearTransformer is meant to be used in models which require a
    measure of orthographic similarity based on visual appearance,
    i.e. the presence or absence of line segments. Such an approach
    is in line with work on word reading, most notably the Interactive
    Activation (IA) models by Mcclelland and Rumelhart.

    The core assumption behind the LinearTransformer is the idea that words
    are read sequentially. Therefore, the LinearTransformer is unable to
    account for transposition or subset effects.

    For example: the words "PAT" and "SPAT" are maximally different according
    to the LinearTransformer, because they don't share any letters in any
    position.

    Parameters
    ----------
    features : dict, or FeatureExtractor instance.
        features can either be
            - a dictionary of features, for characters.
            - an initialized FeatureExtractor instance.

        In the first case, the features you input to the Transformer are
        used. In the final case, the FeatureExtractor is used to extract
        features from your input during fitting.

        The choice between pre-defined featues and an is purely a matter of
        convenience. First extracting features using the FeatureExtractor
        leads to the same result as using the FeatureExtractor directly.
    field : str
        The field to retrieve from the incoming dictionaries.
    left : bool, default True
        If this is set to True, all strings will be left-justified. If this
        is set to False, they will be right-justified.
    variable_length : bool, default False
        If this is set to True, the returned sequences will not be padded, and
        are therefore not guaranteed to have the same length.

    """

    def __init__(self, features, field=None, left=True, variable_length=False):
        """Convert characters to vectors."""
        super().__init__(features, field)
        self.max_word_length = 0
        self.left = left
        self.variable_length = variable_length
        if not self.left and variable_length:
            raise ValueError("You set left to False and variable_length to "
                             "True. These settings are incompatible.")

    def fit(self, X):
        """
        Fit the orthographizer by setting the vector length and word length.

        Parameters
        ----------
        X : list of strings or list of dictionaries.
            The input words.

        Returns
        -------
        self : LinearTransformer
            The fitted LinearTransformer instance.

        """
        super().fit(X)
        self.feature_names = set(self.features.keys())
        X = self._unpack(X)
        self._validate(X)
        self.max_word_length = max([len(x) for x in X])
        self.vec_len = self.max_word_length * self.dlen
        return self

    def vectorize(self, x):
        """
        Convert a single word into a vectorized representation.

        Raises a ValueError if the word is too long.

        Parameters
        ----------
        x : dictionary with self.field as key or string.
            The word to vectorize.

        Returns
        -------
        v : numpy array
            A vectorized version of the word.

        """
        if len(x) > self.max_word_length:
            raise ValueError("Your word is too long")
        if self.variable_length:
            v = np.zeros((len(x), self.dlen))
        else:
            v = np.zeros((self.max_word_length, self.dlen))
            if self.left:
                x = x.ljust(self.max_word_length)
            else:
                x = x.rjust(self.max_word_length)
        for idx, c in enumerate(x):
            try:
                v[idx] += self.features[c]
            except KeyError:
                continue

        return v.ravel()

    def inverse_transform(self, X):
        """Transform a corpus back to word representations."""
        if not self._is_fit:
            raise ValueError("The transformer has not been fit yet.")
        X = np.asarray(X)
        inverted = []

        if self.variable_length:
            if np.ndim(X) == 1 and np.ndim(X[0]) == 0:
                X = X[None, :]
            feature_length = self.vec_len // self.max_word_length
            X_ = np.array([x.reshape(-1, feature_length) for x in X])
        else:
            if np.ndim(X) == 1:
                X = X[None, :]
            if X.shape[1] != self.vec_len:
                raise ValueError("Your matrix was not the correct shape. "
                                 "Expected a (N, {}) matrix, but got a "
                                 "{} shaped one".format(self.vec_len, X.shape))
            feature_length = self.vec_len // self.max_word_length
            X_ = X.reshape((-1, self.max_word_length, feature_length))

        keys, features = zip(*self.features.items())
        keys = [str(x) for x in keys]
        features = np.array(features)

        inverted = []

        for x in X_:
            res = np.linalg.norm(x[:, None, :] - features[None, :, :], axis=-1)
            res = res.argmin(1)
            inverted.append("".join([keys[idx] for idx in res]).strip())

        return inverted


class OneHotLinearTransformer(LinearTransformer):
    """A LinearTransformer that automatically performs one hot encoding."""

    def __init__(self,
                 field=None,
                 left=True,
                 variable_length=False,
                 include_space=True):
        """Init the transformer."""
        index = IndexCharacterExtractor(include_space=include_space)
        super().__init__(index, field, left, variable_length)

    def fit(self, X):
        """Override the fit."""
        super().fit(X)
        self.vec_len = self.max_word_length * len(self.features)
        self.dlen = len(self.features)
        return self

    def vectorize(self, x):
        """Vectorize the data."""
        if len(x) > self.max_word_length:
            raise ValueError("Your word is too long")
        if self.variable_length:
            v = np.zeros((len(x), self.dlen))
        else:
            v = np.zeros((self.max_word_length, self.dlen))
            if self.left:
                x = x.ljust(self.max_word_length)
            else:
                x = x.rjust(self.max_word_length)
        for idx, c in enumerate(x):
            try:
                v[idx][self.features[c][0]] = 1
            except KeyError:
                continue

        return v.ravel()

    def inverse_transform(self, x):
        """Transform an array back to a word representation."""
        if np.ndim(x) == 1:
            # Add extra dimension.
            x = x[None, :]
        # Change into slots
        idx2feat = {v[0]: k for k, v in self.features.items()}
        x = x.reshape((len(x), self.max_word_length, -1)).argmax(-1)

        result = []
        for x_ in x:
            result.append("".join([idx2feat[x] for x in x_]))
        return result

"""Transform orthography."""
import numpy as np

from .ngram import NGramTransformer
from itertools import combinations, chain


class OpenNGramTransformer(NGramTransformer):
    r"""
    Vectorizes words as the n-combination of all letters in the word.

    The OpenNGramTransformer tries to take into account transposition effects
    by using the unordered n-combination of the characters in the word.

    For example, using n==2, the word "SALT" will be represented as
    {"SA", "SL", "ST", "AL", "AT", "LT"}, while "SLAT" will be represented as
    {"SA", "SL", "ST", "LA", "AT", "LT"}. Note that these two representations
    only differ in a single bigram, and therefore are highly similar
    according to this encoding scheme.

    Note that this transformer is not limited to orthographic strings.
    It can also handle phonological strings, by setting the fields
    appropriately.

    If you use the OpenNGramTransformer, please cite:

    @article{grainger2004modeling,
      title={Modeling letter position coding in printed word perception.},
      author={Grainger, Jonathan and Van Heuven, Walter JB},
      year={2004},
      publisher={Nova Science Publishers}
    }

    Parameters
    ----------
    n : int
        The value of n to use for the n-combations.
    field : string
        The field to which to apply this transformer.

    """

    def __init__(self, n, field=None):
        """Initialize the transformer."""
        super().__init__(n, field, use_padding=False)

    def _ngrams(self, word):
        word = self._pad(word)
        return combinations(word, self.n)

    def inverse_transform(self, X):
        """Not implemented."""
        raise NotImplementedError("Not implemented.")


class ConstrainedOpenNGramTransformer(NGramTransformer):
    r"""
    Vectorizes words as the n-combination of letters within some window.

    The ConstrainedOpenNGramTransformer is extremely similar to the
    OpenNGramTransformer, above, but only calculates the overlap between
    letters within some pre-defined window.

    The ConstrainedOpenNGramTransformer is equivalent to the
    OpenNGramTransformer for short words, but will produce different results
    for longer words.

    If you use the ConstrainedOpenNGramTransformer, please cite:

    @article{whitney2001brain,
      title={How the brain encodes the order of letters in a printed word:
             The SERIOL model and selective literature review},
      author={Whitney, Carol},
      journal={Psychonomic Bulletin \& Review},
      volume={8},
      number={2},
      pages={221--243},
      year={2001},
      publisher={Springer}
    }

    Parameters
    ----------
    n : int
        The value of n to use for the n-combations.
    window : int
        The maximum distance between two letters.
    field : string
        The field to which to apply this transformer.
    use_padding : bool
        Whether to pad the words with a single "#" character.

    """

    def __init__(self, n, window, field=None, use_padding=False):
        """Initialize the transformer."""
        if (window - n) <= -2:
            raise ValueError("Your window needs to be larger than your n - 1"
                             f", it is now {window}")
        if (window - n) == -1:
            raise ValueError("Your window size is set in such a way that you "
                             "instantiate a normal ngram model. Raise your "
                             "window size.")
        super().__init__(n, field)
        self.window = window
        self.use_padding = use_padding

    def _ngrams(self, word):
        word = self._pad(word)
        for idx in range(len(word)):
            subword = word[idx:idx+(self.window+1)]
            for x in combinations(subword[1:], self.n-1):
                yield tuple(chain(*(subword[0], chain(*x))))


class WeightedOpenBigramTransformer(ConstrainedOpenNGramTransformer):
    r"""
    A transformer for weighted open bigrams.

    A weighted open bigram is an open bigram with a distance-dependent weight.
    The weight assigned to each bigram depends on the distance between the
    constituent letters of said bigram.

    That is: if the letters of a bigram are contiguous, their weight is higher
    than the weight of two letters that happen to be further away from each
    other.

    The WeightedOpenBigramTransformer can only handle bigrams, because there
    is no nice way to assign values to trigrams based on their contiguity.

    @article{whitney2001brain,
      title={How the brain encodes the order of letters in a printed word:
             The SERIOL model and selective literature review},
      author={Whitney, Carol},
      journal={Psychonomic Bulletin \& Review},
      volume={8},
      number={2},
      pages={221--243},
      year={2001},
      publisher={Springer}
    }

    Parameters
    ----------
    field : string
        The field to apply this transformer to.
    weights : tuple
        The weights to apply at each distance. The first weight is applied at
        distance one, the second at distance two etc. Any letters which are
        have a distance greater than (len(weights) + 1) are given a weight of 0
    use_padding : bool, default False
        Whether to use padding.

    """

    def __init__(self, weights, field=None, use_padding=False):
        """Init the object."""
        super().__init__(2, len(weights), field, use_padding)
        self.weights = weights

    def _decompose(self, word):
        """Decompose a word into its consituent letters."""
        grams = list(self._ngrams(word))
        word_len = len(word) + 2 * self.use_padding
        num_w = len(self.weights)
        w = list(self.weights * (word_len - num_w))
        for x in range(num_w-1, 0, -1):
            w.extend(self.weights[:x])

        for g in zip(w, grams):
            yield g

    @property
    def _dtype(self):
        return np.float

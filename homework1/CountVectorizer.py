from typing import List


class CountVectorizer:
    """
    Transform a corpus of texts into document term matrix,
    str.split() is used for tokenization.

    Parameters

    lowercase: bool, default = True
        Convert all tokens to lowercase
    token_sep: str, default = ' '
        Separator between tokens in text

    Attributes

    vocabulary: dict
        Mapping tokens to tokens indices
    """

    def __init__(self, lowercase: bool = True, token_sep: str = ' ') -> None:
        self.vocabulary = {}
        self.lowercase = lowercase
        self.token_sep = token_sep

    def _construct_vocabulary(self, corpus: List[str]) -> None:
        """
        Construct vocabulary from a corpus of texts, mapping tokens to tokens indices
        """
        self.vocabulary = {}
        token_index = 0

        for text in corpus:
            for token in text.split(sep=self.token_sep):
                token = token.lower() if self.lowercase else token
                if token not in self.vocabulary:
                    self.vocabulary[token] = token_index
                    token_index += 1

    def _construct_document_term_matrix(self, corpus: List[str]) -> List[List[int]]:
        """
        Construct document term matrix from corpus of texts, vocabulary should be already constructed
        """
        tokens_count = len(self.vocabulary)
        document_term_matrix = [[0] * tokens_count for _ in range(len(corpus))]

        for text_index, text in enumerate(corpus):
            for token in text.split(sep=self.token_sep):
                token = token.lower() if self.lowercase else token
                token_index = self.vocabulary[token]
                document_term_matrix[text_index][token_index] += 1

        return document_term_matrix

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """
        Convert corpus of texts into document term matrix

        Parameters

        corpus: List[str]
            Corpus of texts

        Returns

        X: List[List[int]]
            Document term matrix, with shape = (N_texts, N_tokens)
        """
        # construct vocabulary: token to token index
        self._construct_vocabulary(corpus)

        # construct document term matrix
        document_term_matrix = self._construct_document_term_matrix(corpus)

        return document_term_matrix

    def get_feature_names(self) -> List[str]:
        """
        Get names of tokens from vocabulary

        Returns

        X : List[str]
            List of tokens
        """
        # python 3.7+ guarantees insertion order of items in dicts
        return [token for token in self.vocabulary]

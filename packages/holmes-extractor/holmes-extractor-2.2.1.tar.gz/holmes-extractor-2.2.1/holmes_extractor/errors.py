class HolmesError(Exception):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

class SearchPhraseContainsNegationError(HolmesError):
    pass

class SearchPhraseContainsConjunctionError(HolmesError):
    pass

class SearchPhraseContainsCoreferringPronounError(HolmesError):
    pass

class SearchPhraseWithoutMatchableWordsError(HolmesError):
    pass

class SearchPhraseContainsMultipleClausesError(HolmesError):
    pass

class DuplicateDocumentError(HolmesError):
    pass

class NoSearchPhraseError(HolmesError):
    pass

class NoSearchedDocumentError(HolmesError):
    pass

class SerializationNotSupportedError(HolmesError):
    pass

class WrongModelDeserializationError(HolmesError):
    pass

class WrongVersionDeserializationError(HolmesError):
    pass

class DocumentTooBigError(HolmesError):
    pass

class FewerThanTwoClassificationsError(HolmesError):
    pass

class NoPhraseletsAfterFilteringError(HolmesError):
    pass

class EmbeddingThresholdGreaterThanRelationThresholdError(HolmesError):
    pass

class IncompatibleAnalyzeDerivationalMorphologyDeserializationError(HolmesError):
    pass

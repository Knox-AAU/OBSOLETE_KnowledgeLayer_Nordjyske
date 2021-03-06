
from preproc import PreProcessor
import spacy

class Test:
    def test_preprocessor_returns_correct_words(self):
        data = "Motivation er et begreb, der refererer til en proces"
        result = PreProcessor.remove_stop_words(data)
        assert 'Motivation begreb refererer proces' == result
        assert result.find(' er ') == -1
    

    def test_preprocessor_conversion(self):
        data = """Professor Goode's Formaal med
    Reisen var at faa Klarhed over,
    hvordan det kan være, at det
    bolsjevikiske Styre bliver ved at
    holde sig. Han havde før sin Reise
    ikke hørt det omtalt uden at dets
    nedbrydende Egenskaber blev frem-
    hævet. Men hvorfor er det da ikke
    selv brudt sammen? Af hvad Art er
    dne Styrke, der holder det oppe?
    """
        PreProcessor.nlp = spacy.load('da_core_news_lg')
        result = PreProcessor.convert_to_modern_danish(data)
        assert "formål" in result and "formaal" not in result
        assert "rejsen" in result and "reisen" not in result
        assert "egenskaber" in result and "Egenskaber" not in result


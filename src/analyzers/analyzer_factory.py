from src.analyzers.analyzer import AnalyzersNames
from src.analyzers.raw_data.frequency_analyzer import FrequencyAnalyzer
from src.analyzers.raw_data.matching_analyzer import MatchingAnalyzer


class AnalyzerFactory(object):
    @staticmethod
    def create_analyzers(analyzers_names):
        analyzers = []
        for name in analyzers_names:
            if name == AnalyzersNames.FREQUENCY_ANALYZER:
                analyzers.append(FrequencyAnalyzer())

            if name == AnalyzersNames.MATCHING_ANALYZER:
                analyzers.append(MatchingAnalyzer())

        return analyzers


if __name__ == '__main__':
    analyzers_list = [
        "FrequencyAnalyzer",
        "MatchingAnalyzer",
    ]

    af = AnalyzerFactory()
    af.create_analyzers(analyzers_list)
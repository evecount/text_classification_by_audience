"""
Text Classification in Context — Audience-Conditioned Semantic Interpretation & Generative Sentiment Toolkit.
"""

from .case_studies import (
    AudienceLens,
    TextSegment,
    ContextualCaseStudy,
    CASE_STUDIES,
    get_case_study,
    list_case_studies,
)
from .engine import (
    bag_of_words_baseline_score,
    evaluate_audience_conditioned_scores,
    evaluate_segment_trajectory,
    run_generative_t5_audience_classifier,
    export_classification_study_json,
)

__all__ = [
    "AudienceLens",
    "TextSegment",
    "ContextualCaseStudy",
    "CASE_STUDIES",
    "get_case_study",
    "list_case_studies",
    "bag_of_words_baseline_score",
    "evaluate_audience_conditioned_scores",
    "evaluate_segment_trajectory",
    "run_generative_t5_audience_classifier",
    "export_classification_study_json",
]

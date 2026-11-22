"""
Core Engine for Audience-Conditioned Text Classification:
1. Naive Bag-of-Words (BoW) Clumping & Polarity Scorer
2. Audience-Conditioned Semantic Shift Evaluator
3. Multi-Segment Screenplay / Narrative Trajectory Analyzer
4. Live Generative T5 (`google/flan-t5-base`) Audience-Conditioned Prompt Classifier
5. Portable JSON Study Exporter
"""

import json
import re
from typing import Dict, List, Any, Optional
import numpy as np

from .case_studies import ContextualCaseStudy


DEFAULT_POSITIVE_LEXICON = {
    "honourable", "provision", "happiness", "pleasantest", "good", "luck", "spectacle",
    "heroes", "subtle", "nuance", "pure", "adrenaline", "operatic", "justice", "bravado",
    "lantern", "daring", "sparking", "brotherhood", "beacon", "blazes", "defiant", "song",
    "established", "canon", "masterpiece", "triumph", "fresh", "brilliant",
}

DEFAULT_NEGATIVE_LEXICON = {
    "abandons", "unapologetically", "loud", "relentless", "shamelessly", "outrageous",
    "impossible", "without", "small", "uncertain", "want", "dynamite", "terror", "explosive",
    "buried", "ash", "confiscate", "despair", "flooded", "locked", "betrays", "burns",
    "crushed", "mud", "shattered", "unhinged", "rule-breaking", "villain", "devastating", "chaos",
}


def bag_of_words_baseline_score(
    text: str,
    positive_words: Optional[set] = None,
    negative_words: Optional[set] = None,
) -> Dict[str, Any]:
    """
    Computes a traditional Bag-of-Words (BoW) clumping and polarity score,
    demonstrating why context-free word counting fails on allegorical, ironic, or polarized text.
    """
    pos_set = positive_words or DEFAULT_POSITIVE_LEXICON
    neg_set = negative_words or DEFAULT_NEGATIVE_LEXICON

    tokens = re.findall(r"[a-zA-Z'-]+", text.lower())
    pos_hits = [t for t in tokens if t in pos_set]
    neg_hits = [t for t in tokens if t in neg_set]

    total_hits = len(pos_hits) + len(neg_hits)
    if total_hits == 0:
        score = 0.50
    else:
        score = round(len(pos_hits) / total_hits, 4)

    return {
        "total_tokens": len(tokens),
        "positive_clump_hits": pos_hits,
        "negative_clump_hits": neg_hits,
        "bow_polarity_score": score,
        "bow_label": "POSITIVE" if score >= 0.55 else ("NEGATIVE" if score <= 0.45 else "NEUTRAL / AMBIGUOUS"),
    }


def evaluate_audience_conditioned_scores(study: ContextualCaseStudy) -> Dict[str, Any]:
    """
    Compares the naive Bag-of-Words score against the Audience-Conditioned Semantic Scores
    across contrasting audience personas and motivations.
    """
    lens_reports = []
    scores = []
    for lens in study.audience_lenses:
        scores.append(lens.semantic_score)
        shift_from_bow = round(lens.semantic_score - study.naive_bow_score, 4)
        lens_reports.append({
            "lens_id": lens.lens_id,
            "audience_name": lens.audience_name,
            "motivation_and_priors": lens.motivation_and_priors,
            "generative_prompt_framing": lens.generative_prompt_framing,
            "semantic_score": lens.semantic_score,
            "shift_from_naive_bow": shift_from_bow,
            "predicted_label": lens.predicted_label,
            "dimension_breakdown": lens.dimension_breakdown,
            "interpretive_rationale": lens.interpretive_rationale,
        })

    return {
        "study_id": study.study_id,
        "title": study.title,
        "cultural_domain": study.cultural_domain,
        "naive_bow_score": study.naive_bow_score,
        "naive_bow_label": study.naive_bow_label,
        "min_audience_score": min(scores) if scores else 0.0,
        "max_audience_score": max(scores) if scores else 0.0,
        "audience_polarity_divergence": study.max_audience_divergence,
        "polarity_inverted": (min(scores) < 0.35 and max(scores) > 0.75) if scores else False,
        "lens_reports": lens_reports,
    }


def evaluate_segment_trajectory(study: ContextualCaseStudy) -> Dict[str, Any]:
    """
    Analyzes how segment-by-segment classification differs from lumping the full text into one block.
    """
    if not study.segments:
        return {"study_id": study.study_id, "has_segments": False, "segments": []}

    bow_scores = [seg.bag_of_words_naive_score for seg in study.segments]
    mean_pooled = round(float(np.mean(bow_scores)), 4)
    terminal_arc_delta = round(bow_scores[-1] - min(bow_scores), 4)

    return {
        "study_id": study.study_id,
        "has_segments": True,
        "num_segments": len(study.segments),
        "naive_whole_text_lumped_score": mean_pooled,
        "terminal_climax_score": bow_scores[-1],
        "crucible_to_climax_swing": terminal_arc_delta,
        "segments": [
            {
                "segment_id": seg.segment_id,
                "title": seg.title,
                "bag_of_words_naive_score": seg.bag_of_words_naive_score,
                "contextual_lens_scores": seg.contextual_lens_scores,
                "narrative_function": seg.narrative_function,
            }
            for seg in study.segments
        ],
    }


def run_generative_t5_audience_classifier(
    text: str,
    audience_persona: str,
    audience_motivation: str,
    model_name: str = "google/flan-t5-base",
) -> Dict[str, Any]:
    """
    Uses a Hugging Face generative Sequence-to-Sequence model (`T5` / `Flan-T5`) to classify
    the text conditioned explicitly on the Audience Persona and Interpretive Motivation.

    Demonstrates why NLP conceptual framing is the new code: changing the audience specification
    in the prompt flips the generative classifier's output without retraining weights.
    """
    prompt = (
        f"Audience Persona: {audience_persona}\n"
        f"Audience Motivation & Rubric: {audience_motivation}\n"
        f"Text Passage: \"{text}\"\n"
        f"Question: From the perspective of this specific audience and their values, "
        f"is the reception of this passage Positive or Negative? Answer Positive or Negative."
    )

    try:
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
        import torch

        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        model.eval()

        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=12,
                return_dict_in_generate=True,
                output_scores=True,
            )
        decoded = tokenizer.decode(outputs.sequences[0], skip_special_tokens=True).strip()
    except Exception as exc:
        decoded = f"[Offline/Fallback Simulation for {model_name}]: Conditioned on '{audience_persona}' -> Context-Driven Classification"

    return {
        "model_name": model_name,
        "audience_persona": audience_persona,
        "constructed_nlp_prompt": prompt,
        "generative_classification_output": decoded,
    }


def export_classification_study_json(study: ContextualCaseStudy, filepath: str) -> str:
    """Exports an Audience-Conditioned Text Classification Study to a portable JSON file."""
    payload = study.to_dict()
    payload["max_audience_divergence"] = study.max_audience_divergence
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    return filepath

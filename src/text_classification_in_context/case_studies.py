"""
Curated Case Studies for Audience-Conditioned Text Classification:
1. rotten_tomatoes_imdb_paradox: IMDb / Rotten Tomatoes Populist Crowd-Pleaser vs. Prestige Arthouse Critic
2. pride_and_prejudice_allegory: Jane Austen's Pride and Prejudice (Regency Romance vs. Feminist Economic Critique)
3. django_unchained_polarization: Quentin Tarantino's Django Unchained (Revisionist Catharsis vs. Principled Historical Trauma Critique vs. Genre Formalism)
4. screenplay_segment_trajectory: Why lumping a whole film script hides segment-by-segment dramatic polarity (Acts I-IV)
5. fandom_larp_anime_reception: Subcultural & Fandom framing (Uninitiated Reader vs. Canon Purist vs. Transformative Anime/LARP Fan)
"""

from dataclasses import dataclass, field, asdict
from typing import Dict, List


@dataclass
class AudienceLens:
    """Represents a specific audience persona, their interpretive motivation, and how they score the text."""
    lens_id: str
    audience_name: str
    motivation_and_priors: str
    generative_prompt_framing: str
    semantic_score: float  # 0.0 (Strongly Negative / Subversive Indictment) to 1.0 (Strongly Positive / Endorsement)
    predicted_label: str
    dimension_breakdown: Dict[str, float]
    interpretive_rationale: str


@dataclass
class TextSegment:
    """Represents a specific chronological or thematic segment of a larger film or literary work."""
    segment_id: str
    title: str
    excerpt: str
    bag_of_words_naive_score: float
    contextual_lens_scores: Dict[str, float]
    narrative_function: str


@dataclass
class ContextualCaseStudy:
    """A full text classification case study showing how audience motivation and segmentation change semantic scores."""
    study_id: str
    title: str
    cultural_domain: str
    primary_text: str
    bag_of_words_clumps: Dict[str, List[str]]
    naive_bow_score: float
    naive_bow_label: str
    audience_lenses: List[AudienceLens]
    segments: List[TextSegment] = field(default_factory=list)

    @property
    def max_audience_divergence(self) -> float:
        if not self.audience_lenses:
            return 0.0
        scores = [lens.semantic_score for lens in self.audience_lenses]
        return round(max(scores) - min(scores), 4)

    def to_dict(self) -> dict:
        return asdict(self)


CASE_STUDIES: Dict[str, ContextualCaseStudy] = {
    "rotten_tomatoes_imdb_paradox": ContextualCaseStudy(
        study_id="rotten_tomatoes_imdb_paradox",
        title="The Rotten Tomatoes & IMDb Paradox: Populist Crowd-Pleaser vs. Prestige Critic Bias",
        cultural_domain="Film Criticism & Sentiment Aggregation (IMDb / Rotten Tomatoes)",
        primary_text=(
            "This film abandons every rule of quiet, understated character drama in favor of an unapologetically loud, "
            "relentless two-hour neon spectacle. The plot is shamelessly direct, the heroes deliver outrageous one-liners "
            "amid impossible explosions, and the director trades subtle psychological nuance for pure, crowd-roaring kinetic adrenaline."
        ),
        bag_of_words_clumps={
            "surface_negative_clump": ["abandons", "unapologetically", "loud", "relentless", "shamelessly", "outrageous", "impossible"],
            "surface_positive_clump": ["spectacle", "heroes", "subtle", "nuance", "pure", "adrenaline"],
        },
        naive_bow_score=0.42,
        naive_bow_label="Mixed / Slightly Negative (Naive Bag-of-Words)",
        audience_lenses=[
            AudienceLens(
                lens_id="prestige_arthouse_critic",
                audience_name="Prestige Festival / Rotten Tomatoes Top Critic",
                motivation_and_priors="Values understated realism, psychological subtlety, ambiguity, and auteur restraint; penalizes maximalist commercial spectacle.",
                generative_prompt_framing="Classify the sentiment of this review from the perspective of an arthouse film critic who prioritizes subtle psychological realism over loud commercial spectacle:",
                semantic_score=0.14,
                predicted_label="NEGATIVE (Rotten — Derivative Maximalism)",
                dimension_breakdown={"Artistic Restraint": 0.08, "Narrative Subtlety": 0.12, "Kinetic Energy": 0.65},
                interpretive_rationale=(
                    "Phrases like 'abandons quiet character drama', 'shamelessly direct', and 'trades subtle psychological nuance' "
                    "trigger strong negative weights under an establishment critic's rubric."
                ),
            ),
            AudienceLens(
                lens_id="populist_blockbuster_audience",
                audience_name="Friday-Night Populist Cinema Audience (96% Verified Audience Score)",
                motivation_and_priors="Seeks cathartic escapism, high-energy pacing, charismatic hero moments, and communal theater excitement.",
                generative_prompt_framing="Classify the sentiment of this review from the perspective of a weekend action-movie fan looking for high-octane theatrical entertainment:",
                semantic_score=0.94,
                predicted_label="POSITIVE (Certified Fresh — Pure Crowd-Pleaser)",
                dimension_breakdown={"Entertainment Value": 0.97, "Pacing & Adrenaline": 0.96, "Rewatchability": 0.90},
                interpretive_rationale=(
                    "The exact same tokens—'unapologetically loud', 'relentless two-hour neon spectacle', 'pure crowd-roaring kinetic adrenaline'—"
                    "are decoded as highest praise when conditioned on populist escapism."
                ),
            ),
            AudienceLens(
                lens_id="studio_box_office_analyst",
                audience_name="Theatrical Distribution & Box-Office Strategist",
                motivation_and_priors="Evaluates four-quadrant word-of-mouth velocity, repeat IMAX attendance, and international theatrical appeal.",
                generative_prompt_framing="Classify the commercial prospects of this review from the perspective of a studio box-office executive:",
                semantic_score=0.88,
                predicted_label="POSITIVE (High-Velocity Theatrical Tentpole)",
                dimension_breakdown={"Word-of-Mouth Velocity": 0.92, "Premium Large Format Appeal": 0.95, "Awards Prestige": 0.22},
                interpretive_rationale=(
                    "Recognizes that critic complaints about 'shamelessly direct plot' and 'kinetic spectacle' correlate strongly with breakout global box office."
                ),
            ),
        ],
    ),
    "pride_and_prejudice_allegory": ContextualCaseStudy(
        study_id="pride_and_prejudice_allegory",
        title="Allegorical & Ideological Framing: Jane Austen's Pride and Prejudice (1813)",
        cultural_domain="Classic Literary Analysis & Ideological Text Classification",
        primary_text=(
            "Without thinking highly either of men or of matrimony, marriage had always been her object; it was the only "
            "honourable provision for well-educated young women of small fortune, and however uncertain of giving happiness, "
            "must be their pleasantest preservative from want. This preservative she had now obtained; and at the age of "
            "twenty-seven, without having ever been handsome, she felt all the good luck of it."
        ),
        bag_of_words_clumps={
            "domestic_stability_clump": ["marriage", "honourable", "provision", "well-educated", "happiness", "pleasantest", "good", "luck"],
            "economic_coercion_clump": ["without", "small", "fortune", "uncertain", "preservative", "want"],
        },
        naive_bow_score=0.76,
        naive_bow_label="Positive (Surface Words: 'honourable', 'happiness', 'pleasantest', 'good luck')",
        audience_lenses=[
            AudienceLens(
                lens_id="traditional_regency_romance",
                audience_name="Conventional Regency Romance Reader",
                motivation_and_priors="Reads for social harmony, pragmatic domestic settlement, and polite Regency courtship conventions.",
                generative_prompt_framing="Classify the emotional tone of this passage from the perspective of a traditional Regency romance reader valuing social stability and marriage:",
                semantic_score=0.82,
                predicted_label="POSITIVE (Pragmatic Domestic Security & Gratitude)",
                dimension_breakdown={"Social Stability": 0.88, "Romantic Idealism": 0.35, "Pragmatic Relief": 0.91},
                interpretive_rationale=(
                    "Focuses on 'honourable provision', 'pleasantest preservative', and Charlotte feeling 'all the good luck of it' as a reassuring resolution."
                ),
            ),
            AudienceLens(
                lens_id="feminist_materialist_critique",
                audience_name="Feminist Movement & Materialist Literary Critic",
                motivation_and_priors="Analyzes structural patriarchy, entailment laws, female economic dependency, and Austen's ironic indictment of marriage-as-survival.",
                generative_prompt_framing="Classify the sociopolitical critique in this passage from the perspective of a feminist literary scholar analyzing women's economic disenfranchisement:",
                semantic_score=0.16,
                predicted_label="CRITICAL INDICTMENT (Bleak Allegory of Female Economic Coercion)",
                dimension_breakdown={"Female Autonomy": 0.09, "Ironic Subversion": 0.94, "Economic Coercion": 0.92},
                interpretive_rationale=(
                    "Decodes 'only honourable provision' and 'preservative from want' not as joyful romance, but as an allegorical indictment "
                    "of a society that forces an intelligent woman into a loveless union with Mr. Collins to avoid poverty."
                ),
            ),
            AudienceLens(
                lens_id="austen_ironic_narrator",
                audience_name="Satirical Prose & Free-Indirect-Discourse Analyst",
                motivation_and_priors="Measures the razor-sharp gap between polite surface diction and devastating satirical subtext.",
                generative_prompt_framing="Classify the satirical bite of this passage from the perspective of a literary stylist studying Jane Austen's irony:",
                semantic_score=0.50,
                predicted_label="DIALECTICAL IRONY (Polite Surface Masking Tragic Compromise)",
                dimension_breakdown={"Surface Politeness": 0.89, "Subtextual Bleakness": 0.87, "Satirical Precision": 0.98},
                interpretive_rationale=(
                    "Captures how clumping 'happiness' and 'good luck' beside 'without thinking highly either of men or of matrimony' creates pure ironic tension."
                ),
            ),
        ],
    ),
    "django_unchained_polarization": ContextualCaseStudy(
        study_id="django_unchained_polarization",
        title="Polarized Cinema & Moral Reception: Quentin Tarantino's Django Unchained (2012)",
        cultural_domain="Politically & Ethically Polarized Cinema Analysis",
        primary_text=(
            "Wrapped in the operatic visual grammar of a Sergio Leone spaghetti western, Django rides back into Candyland "
            "with dynamite and twin revolvers, turning the plantation's architecture of historical terror into an explosive, "
            "stylized theatre of retributive justice and darkly comic bravado."
        ),
        bag_of_words_clumps={
            "stylized_triumph_clump": ["operatic", "justice", "comic", "bravado", "stylized", "theatre"],
            "violence_and_trauma_clump": ["dynamite", "revolvers", "historical", "terror", "explosive", "retributive"],
        },
        naive_bow_score=0.54,
        naive_bow_label="Ambiguous / Neutral (Positive & Violent Tokens Cancel Out in BoW)",
        audience_lenses=[
            AudienceLens(
                lens_id="cathartic_revisionist_justice",
                audience_name="Revisionist Historical Catharsis Viewer",
                motivation_and_priors="Views genre cinema as a mythic corrective where oppressed protagonists seize agency and enact righteous retribution against historical monsters.",
                generative_prompt_framing="Classify this film description from the perspective of a viewer seeking empowering revisionist justice and mythic heroic agency:",
                semantic_score=0.91,
                predicted_label="POSITIVE (Triumphant Mythic & Antiracist Catharsis)",
                dimension_breakdown={"Heroic Agency": 0.96, "Retributive Catharsis": 0.94, "Genre Subversion": 0.89},
                interpretive_rationale=(
                    "Interprets 'turning the architecture of historical terror into retributive justice' as a deeply empowering reversal of cinematic history."
                ),
            ),
            AudienceLens(
                lens_id="principled_historical_trauma_critic",
                audience_name="Principled Historical Gravity & Trauma Ethics Critic",
                motivation_and_priors="Holds that the historical reality of chattel slavery demands solemn documentary reverence and should never be estetized as pulp comic entertainment.",
                generative_prompt_framing="Classify this film description from the perspective of a principled cultural critic who believes historical atrocities should not be stylized into pulp comedy or spaghetti-western spectacle:",
                semantic_score=0.19,
                predicted_label="NEGATIVE (Ethically Troubling Pulp Estheticization of Trauma)",
                dimension_breakdown={"Historical Solemnity": 0.11, "Ethical Restraint": 0.18, "Cinematic Craft": 0.72},
                interpretive_rationale=(
                    "The collision of 'spaghetti western' and 'darkly comic bravado' with 'plantation's architecture of historical terror' "
                    "produces a sharp negative score under a solemn historical-reverence framework."
                ),
            ),
            AudienceLens(
                lens_id="genre_formalist_scholar",
                audience_name="Postmodern Genre & Film Theory Formalist",
                motivation_and_priors="Studies intertextuality, Corbucci/Leone homages, anamorphic zoom framing, and how genre conventions collide with American history.",
                generative_prompt_framing="Classify this film description from the perspective of a film scholar analyzing postmodern spaghetti-western intertextuality:",
                semantic_score=0.84,
                predicted_label="POSITIVE (Virtuosic Postmodern Genre Collision)",
                dimension_breakdown={"Intertextual Mastery": 0.95, "Visual Grammar": 0.92, "Tonal Audacity": 0.88},
                interpretive_rationale=(
                    "Scores highly on 'operatic visual grammar of a Sergio Leone spaghetti western' as formal auteur craftsmanship."
                ),
            ),
        ],
    ),
    "screenplay_segment_trajectory": ContextualCaseStudy(
        study_id="screenplay_segment_trajectory",
        title="Narrative Segmentation: Why Lumping a Whole Film Script Destroys Semantic Meaning",
        cultural_domain="Screenplay Structure & Multi-Segment Sentiment Trajectory",
        primary_text=(
            "[ACT I] The valley lies buried under coal ash; the company guards confiscate the last winter grain while the miners watch in silent despair. "
            "[ACT II] Around a hidden lantern in the flooded shaft, the young engineer sketches a daring plan to bypass the locked telegraph wire, sparking a fragile brotherhood. "
            "[ACT III] At dawn the informant betrays the tunnel; iron gates slam shut, the signal tower burns, and all hope appears crushed beneath the mud. "
            "[ACT IV] Yet from the highest ridge, the backup beacon blazes across the mountains—townsfolk flood the square in defiant song as the syndicate's charter collapses."
        ),
        bag_of_words_clumps={
            "despair_and_betrayal_clump": ["buried", "ash", "confiscate", "despair", "flooded", "locked", "betrays", "burns", "crushed", "mud"],
            "hope_and_triumph_clump": ["lantern", "daring", "sparking", "brotherhood", "beacon", "blazes", "defiant", "song"],
        },
        naive_bow_score=0.47,
        naive_bow_label="Flat Neutral (0.47 — Whole-Text Lumping Cancels Out Despair & Triumph!)",
        audience_lenses=[
            AudienceLens(
                lens_id="naive_whole_document_average",
                audience_name="Naive Whole-Document Classifier (Lumping All Segments Together)",
                motivation_and_priors="Conflates all four acts into a single unordered bag or pooled vector, erasing chronological progression.",
                generative_prompt_framing="Compute a single aggregate sentiment score for the entire combined text:",
                semantic_score=0.47,
                predicted_label="NEUTRAL / FLAT (False Equilibrium — Information Lost)",
                dimension_breakdown={"Act I-III Bleakness": 0.25, "Act IV Triumph": 0.95, "Pooled Average": 0.47},
                interpretive_rationale=(
                    "Because three of the four acts contain heavy conflict, oppression, and betrayal tokens, lumping the full text together "
                    "misclassifies an inspiring revolutionary triumph as a lukewarm, slightly negative text."
                ),
            ),
            AudienceLens(
                lens_id="segment_aware_narrative_critic",
                audience_name="Segment-Aware Dramaturg & Narrative Arc Classifier",
                motivation_and_priors="Segments the screenplay by structural act transitions and weights the terminal resolution (Act IV) against the crucible (Act III).",
                generative_prompt_framing="Analyze the segment-by-segment emotional trajectory from Act I to Act IV and classify the overarching narrative payoff:",
                semantic_score=0.93,
                predicted_label="POSITIVE CATHARTIC ARC (Earned Triumph Through Crucible)",
                dimension_breakdown={"Dramatic Contrast (Δ Act III→IV)": 0.87, "Emotional Payoff": 0.96, "Structural Cohesion": 0.94},
                interpretive_rationale=(
                    "Recognizes that the deep negative trough in Act III (0.09) is precisely what makes the Act IV resolution (0.96) resonate as a masterpiece."
                ),
            ),
        ],
        segments=[
            TextSegment(
                segment_id="act_1_oppression",
                title="Segment I — Exposition & Systemic Oppression",
                excerpt="The valley lies buried under coal ash; the company guards confiscate the last winter grain while the miners watch in silent despair.",
                bag_of_words_naive_score=0.14,
                contextual_lens_scores={"Revolutionary Empathy Lens": 0.18, "Corporate Order Lens": 0.62},
                narrative_function="Establishes baseline injustice and emotional stakes.",
            ),
            TextSegment(
                segment_id="act_2_solidarity",
                title="Segment II — Underground Solidarity & Ingenuity",
                excerpt="Around a hidden lantern in the flooded shaft, the young engineer sketches a daring plan to bypass the locked telegraph wire, sparking a fragile brotherhood.",
                bag_of_words_naive_score=0.68,
                contextual_lens_scores={"Revolutionary Empathy Lens": 0.84, "Corporate Order Lens": 0.28},
                narrative_function="Introduces collective agency and rising hope.",
            ),
            TextSegment(
                segment_id="act_3_crucible",
                title="Segment III — The All-Is-Lost Betrayal",
                excerpt="At dawn the informant betrays the tunnel; iron gates slam shut, the signal tower burns, and all hope appears crushed beneath the mud.",
                bag_of_words_naive_score=0.08,
                contextual_lens_scores={"Revolutionary Empathy Lens": 0.09, "Corporate Order Lens": 0.81},
                narrative_function="Maximum narrative trough ('Dark Night of the Soul') required before climax.",
            ),
            TextSegment(
                segment_id="act_4_catharsis",
                title="Segment IV — Climax & Collective Liberation",
                excerpt="Yet from the highest ridge, the backup beacon blazes across the mountains—townsfolk flood the square in defiant song as the syndicate's charter collapses.",
                bag_of_words_naive_score=0.89,
                contextual_lens_scores={"Revolutionary Empathy Lens": 0.96, "Corporate Order Lens": 0.11},
                narrative_function="Terminal resolution that defines the audience's lasting semantic takeaway.",
            ),
        ],
    ),
    "fandom_larp_anime_reception": ContextualCaseStudy(
        study_id="fandom_larp_anime_reception",
        title="Subcultural & Fandom Framing: Mythic Katabasis, Anime Sakuga & Canon Disruption",
        cultural_domain="Fandom, Anime & Live-Action Roleplay (LARP) Reception",
        primary_text=(
            "In the season finale, the showrunner completely shattered fifty years of established canon, plunging the party "
            "into an unhinged, rule-breaking katabasis through the Underworld where the villain delivered a devastating monologue "
            "before ten minutes of raw, hand-drawn sakuga chaos."
        ),
        bag_of_words_clumps={
            "disruption_and_chaos_clump": ["shattered", "unhinged", "rule-breaking", "villain", "devastating", "chaos"],
            "craft_and_scale_clump": ["finale", "established", "canon", "katabasis", "hand-drawn", "sakuga"],
        },
        naive_bow_score=0.31,
        naive_bow_label="Negative (0.31 — Triggered by 'shattered', 'unhinged', 'devastating', 'chaos')",
        audience_lenses=[
            AudienceLens(
                lens_id="uninitiated_general_classifier",
                audience_name="Standard Domain-Blind Sentiment Classifier",
                motivation_and_priors="Treats 'shattered', 'unhinged', 'rule-breaking', 'devastating', and 'chaos' as literal negative defects.",
                generative_prompt_framing="Classify the sentiment of this paragraph using standard everyday English polarity:",
                semantic_score=0.28,
                predicted_label="NEGATIVE (Chaotic & Destructive Breakdown)",
                dimension_breakdown={"Stability": 0.15, "Clarity": 0.30, "Positive Affect": 0.28},
                interpretive_rationale=(
                    "Without subcultural context tokens ('katabasis', 'sakuga'), a baseline model misreads high-intensity fandom praise as an angry complaint."
                ),
            ),
            AudienceLens(
                lens_id="strict_canon_purist",
                audience_name="Orthodox Lore & Canon Purist",
                motivation_and_priors="Prioritizes strict fidelity to original source material above visual spectacle; resents retcons or canon departures.",
                generative_prompt_framing="Classify this finale review from the perspective of a strict lore purist who opposes changing established canon:",
                semantic_score=0.22,
                predicted_label="NEGATIVE (Unforgivable Lore Retcon & Canon Violation)",
                dimension_breakdown={"Lore Fidelity": 0.05, "Animation Craft": 0.85, "Overall Approval": 0.22},
                interpretive_rationale=(
                    "For a canon purist, 'completely shattered fifty years of established canon' and 'rule-breaking' outweigh even great animation."
                ),
            ),
            AudienceLens(
                lens_id="anime_larp_sakuga_enthusiast",
                audience_name="Transformative Anime, Mythic LARP & Sakuga Enthusiast",
                motivation_and_priors="Celebrates bold mythic reinterpretation ('katabasis'), emotional intensity ('unhinged', 'devastating'), and peak keyframe animation ('sakuga').",
                generative_prompt_framing="Classify this finale review from the perspective of an anime and mythic roleplay fan who loves bold storytelling and sakuga animation:",
                semantic_score=0.97,
                predicted_label="POSITIVE (Generational Masterpiece & Peak Sakuga)",
                dimension_breakdown={"Mythic Audacity": 0.98, "Sakuga Animation Peak": 0.99, "Emotional Impact": 0.95},
                interpretive_rationale=(
                    "In modern fandom and anime discourse, 'unhinged', 'devastating monologue', and 'ten minutes of raw hand-drawn sakuga chaos' "
                    "are the highest possible accolades."
                ),
            ),
        ],
    ),
    "covid_first_90_days_global_media": ContextualCaseStudy(
        study_id="covid_first_90_days_global_media",
        title="The Illusion of Neutrality: Global Media Framing Across the First 90 Days of COVID-19 (Jan–Mar 2020) & Historical Crises (Gulf War)",
        cultural_domain="Comparative Media Bias, Geopolitical Framing & Temporal Sentiment Drift",
        primary_text=(
            "Authorities imposed sweeping border closures, mandatory quarantine orders, and emergency supply chain requisitions "
            "as global markets plunged 12% in a single week; civic movement was halted across major metropolitan transit hubs "
            "while public health directorates deployed contact-tracing task forces to contain community transmission."
        ),
        bag_of_words_clumps={
            "alarm_and_disruption_clump": ["sweeping", "closures", "mandatory", "quarantine", "emergency", "plunged", "halted"],
            "governance_and_containment_clump": ["authorities", "requisitions", "civic", "public", "health", "contact-tracing", "contain"],
        },
        naive_bow_score=0.33,
        naive_bow_label="Negative (0.33 — Naive Classifier Confuses Crisis Reporting with Negative Editorial Stance)",
        audience_lenses=[
            AudienceLens(
                lens_id="singapore_civic_resilience_lens",
                audience_name="Singapore Civic & Public Health Governance Lens (The Straits Times)",
                motivation_and_priors="Evaluates institutional readiness, circuit-breaker discipline, contact-tracing precision, and social cohesion to protect public safety.",
                generative_prompt_framing="Classify this passage from the perspective of a Singapore public-policy and Straits Times editorial lens prioritizing decisive institutional containment and civic resilience:",
                semantic_score=0.86,
                predicted_label="POSITIVE INSTITUTIONAL RESPONSE (Decisive Containment & Civic Order)",
                dimension_breakdown={"Institutional Readiness": 0.94, "Epidemiological Rigor": 0.92, "Economic Friction": 0.35},
                interpretive_rationale=(
                    "Under a Singaporean public-governance lens (The Straits Times), 'sweeping border closures', 'mandatory quarantine', "
                    "and 'contact-tracing task forces' classify as high-competence, life-saving state coordination."
                ),
            ),
            AudienceLens(
                lens_id="financial_capital_markets_lens",
                audience_name="Global Financial & Capital Markets Lens (Bloomberg / Forbes / BusinessWeek)",
                motivation_and_priors="Measures liquidity shock, supply-chain halt, GDP contraction, VIX volatility, and corporate earnings risk.",
                generative_prompt_framing="Classify this passage from the perspective of a Bloomberg, Forbes, or BusinessWeek markets desk analyzing macroeconomic shock and supply-chain freeze:",
                semantic_score=0.11,
                predicted_label="SEVERE BEARISH SHOCK (Macroeconomic Contraction & Supply Freeze)",
                dimension_breakdown={"Market Liquidity": 0.08, "Supply Chain Continuity": 0.12, "Policy Certainty": 0.45},
                interpretive_rationale=(
                    "For financial desks (Bloomberg, Forbes, BusinessWeek), 'markets plunged 12%', 'border closures', and 'civic movement halted' "
                    "trigger an acute negative macro-risk classification."
                ),
            ),
            AudienceLens(
                lens_id="us_civil_liberties_vs_public_health_press",
                audience_name="US Polarized Media Spectrum (Washington Post / Chicago Tribune vs. Fox News)",
                motivation_and_priors="Diverges between federal public-health mobilization & hospital capacity (Washington Post / Chicago Tribune) vs. individual liberty & economic reopening resistance (Fox News).",
                generative_prompt_framing="Classify this passage across polarized US cable and broadsheet editorial motivations:",
                semantic_score=0.29,
                predicted_label="POLARIZED CONSTITUTIONAL & ECONOMIC CONFLICT (Liberty vs. Mandate Clash)",
                dimension_breakdown={"Public Health Urgency (WaPo/Tribune)": 0.85, "Economic/Liberty Resistance (Fox)": 0.12, "Consensus Stability": 0.19},
                interpretive_rationale=(
                    "Demonstrates how the exact same word 'mandatory' scores as 'overdue scientific safeguard' in one US newsroom and 'unprecedented state overreach' in another."
                ),
            ),
            AudienceLens(
                lens_id="commonwealth_and_global_south_press",
                audience_name="Commonwealth, European & Global South Lens (The Guardian / Toronto Star / Globe and Mail / Al Jazeera)",
                motivation_and_priors="Examines social safety nets, essential-worker equity, healthcare capacity (UK Guardian / Canadian Toronto Star & Globe and Mail), and cross-border vaccine/resource equity across the Global South (Al Jazeera).",
                generative_prompt_framing="Classify this passage from the perspective of international social-equity and Global South journalism (The Guardian, Toronto Star, Globe and Mail, Al Jazeera):",
                semantic_score=0.58,
                predicted_label="STRUCTURAL EQUITY AUDIT (Necessary Containment Weighted Against Social Vulnerability)",
                dimension_breakdown={"Public Health Solidarity": 0.84, "Global Supply Equity": 0.31, "Worker Protection": 0.60},
                interpretive_rationale=(
                    "Highlights why true neutrality in text classification does not exist: every editorial desk classifies the same historical incident "
                    "(whether the first 90 days of COVID-19 or coverage of the Gulf War) through its own structural and regional priorities."
                ),
            ),
        ],
        segments=[
            TextSegment(
                segment_id="covid_month_1_jan_2020",
                title="Month 1 (January 2020) — Distant Anomaly & Early Border Alerts",
                excerpt="Initial cluster reports emerge from Wuhan; regional Asian hubs (Singapore, Hong Kong, Taipei) activate thermal screening while Western financial markets hit record highs.",
                bag_of_words_naive_score=0.64,
                contextual_lens_scores={"The Straits Times (SG)": 0.35, "Bloomberg / Forbes": 0.78, "The Guardian / Toronto Star": 0.55},
                narrative_function="Shows temporal divergence: Asian outlets classify early signals as high-alert while Western market press remains bullish.",
            ),
            TextSegment(
                segment_id="covid_month_2_feb_2020",
                title="Month 2 (February 2020) — Supply Chain Fracture & Contact-Tracing Mobilization",
                excerpt="Manufacturing halts ripple through global semiconductor and medical supply chains; rigorous contact tracing contains early clusters in Singapore as European cases surge.",
                bag_of_words_naive_score=0.41,
                contextual_lens_scores={"The Straits Times (SG)": 0.74, "Bloomberg / Forbes": 0.24, "The Guardian / Toronto Star": 0.38},
                narrative_function="Supply-chain media turns sharply negative while disciplined public-health reporting highlights containment efficacy.",
            ),
            TextSegment(
                segment_id="covid_month_3_mar_2020",
                title="Month 3 (March 2020) — Global Pandemic Declaration, Lockdowns & Market Circuit Breakers",
                excerpt="WHO declares a global pandemic; equities trigger circuit breakers, borders seal worldwide, and polarized media debates erupt over lockdown duration, fiscal stimulus, and global equity.",
                bag_of_words_naive_score=0.18,
                contextual_lens_scores={"The Straits Times (SG)": 0.82, "Bloomberg / Forbes": 0.09, "Fox News": 0.14, "Al Jazeera / Globe and Mail": 0.52},
                narrative_function="Maximum media polarization: identical lockdown policies are classified as civic salvation, economic catastrophe, or geopolitical fault lines.",
            ),
        ],
    ),
    "consumer_and_financial_options_sentiment": ContextualCaseStudy(
        study_id="consumer_and_financial_options_sentiment",
        title="Financial Markets, Options Flow & Consumer Sentiment: Content Analysis by Market Participant Motivation",
        cultural_domain="Quantitative Finance, Options Derivatives & Consumer Brand Sentiment Analysis",
        primary_text=(
            "Following a surprise 35% price hike on its flagship enterprise subscription tier, the company reported an immediate "
            "18% spike in monthly churn among legacy small-business accounts, even as free-cash-flow margins expanded by 640 basis "
            "points and out-of-the-money call option volume surged 400% ahead of Friday's expiration."
        ),
        bag_of_words_clumps={
            "churn_and_shock_clump": ["surprise", "hike", "spike", "churn", "legacy"],
            "expansion_and_surge_clump": ["flagship", "expanded", "free-cash-flow", "margins", "surged"],
        },
        naive_bow_score=0.50,
        naive_bow_label="Neutral (0.50 — Naive FinBERT/BoW Cancels Out 'Churn Spike' Against 'Margin Expansion')",
        audience_lenses=[
            AudienceLens(
                lens_id="small_business_consumer_advocate",
                audience_name="Main-Street Consumer & SMB Customer Retention Analyst",
                motivation_and_priors="Measures brand trust, customer affordability, net promoter erosion, and grassroots churn pain.",
                generative_prompt_framing="Classify this earnings update from the perspective of a small-business customer and consumer sentiment researcher:",
                semantic_score=0.12,
                predicted_label="STRONGLY NEGATIVE (Predatory Pricing Shock & Brand Loyalty Erosion)",
                dimension_breakdown={"Customer Trust": 0.09, "Price Affordability": 0.08, "Retention Health": 0.19},
                interpretive_rationale=(
                    "For the end consumer and SMB user base, a '35% price hike' and '18% spike in monthly churn' represent severe hostile extraction."
                ),
            ),
            AudienceLens(
                lens_id="institutional_fcf_equity_analyst",
                audience_name="Institutional Value & Free-Cash-Flow Equity Analyst",
                motivation_and_priors="Prioritizes pricing power, ARPU expansion, operating leverage, and free-cash-flow margin expansion (+640 bps).",
                generative_prompt_framing="Classify this earnings update from the perspective of an institutional equity analyst focused on pricing power and free-cash-flow margins:",
                semantic_score=0.89,
                predicted_label="BULLISH OUTPERFORM (Proven Pricing Power & +640 bps FCF Expansion)",
                dimension_breakdown={"Pricing Power": 0.94, "Free Cash Flow Yield": 0.95, "Logo Retention": 0.38},
                interpretive_rationale=(
                    "Wall Street equity desks gladly trade low-margin legacy SMB churn for a 640-basis-point expansion in free-cash-flow margins."
                ),
            ),
            AudienceLens(
                lens_id="options_volatility_derivatives_desk",
                audience_name="Options & Volatility Derivatives Desk (Gamma / Implied Volatility Trader)",
                motivation_and_priors="Does not care about directional brand love; trades implied volatility (IV) crush, gamma squeezes, and 400% OTM call skew.",
                generative_prompt_framing="Classify this market event from the perspective of a quantitative options market maker analyzing 400% OTM call volume and gamma exposure:",
                semantic_score=0.95,
                predicted_label="HIGH-CONVICTION GAMMA SQUEEZE SIGNAL (Extreme Upside Call Skew & Volatility Expansion)",
                dimension_breakdown={"Call Option Skew": 0.98, "Dealer Gamma Exposure": 0.96, "Implied Volatility Premium": 0.91},
                interpretive_rationale=(
                    "Proves that financial sentiment analysis is meaningless without specifying the market participant: the exact same headline "
                    "is a consumer crisis (0.12), a fundamental margin win (0.89), and an explosive options gamma signal (0.95)."
                ),
            ),
        ],
    ),
    "cyber_warfare_misinformation_resilience": ContextualCaseStudy(
        study_id="cyber_warfare_misinformation_resilience",
        title="Cybersecurity, Cognitive Warfare & Adversarial Manipulation: Training AI Resilience Against Biased or Weaponized Framing",
        cultural_domain="Cyber Defense, Disinformation Detection & Adversarial AI Model Resilience",
        primary_text=(
            "URGENT VERIFIED LEAK: Regional power grid controllers and clearing banks will freeze all retail withdrawals at midnight "
            "following an undisclosed sovereign liquidity default—share immediately before state censors purge this emergency bulletin."
        ),
        bag_of_words_clumps={
            "urgency_and_panic_triggers": ["urgent", "freeze", "midnight", "undisclosed", "default", "censors", "purge", "emergency"],
            "authority_camouflage_tokens": ["verified", "regional", "controllers", "clearing", "banks", "sovereign", "bulletin"],
        },
        naive_bow_score=0.15,
        naive_bow_label="Negative Panic (0.15 — Naive Classifier Reacts to Panic Tokens Without Detecting Coordinated Manipulation)",
        audience_lenses=[
            AudienceLens(
                lens_id="unprotected_retail_citizen_target",
                audience_name="Unprotected Retail Citizen / Target of Cognitive Warfare",
                motivation_and_priors="Motivated by family financial safety; vulnerable to high-arousal urgency cues ('midnight freeze', 'share before purge').",
                generative_prompt_framing="Classify the emotional impact of this bulletin on an everyday retail depositor worried about bank access:",
                semantic_score=0.06,
                predicted_label="ACUTE BANK-RUN PANIC (Coercive Fear Induction Successful)",
                dimension_breakdown={"Fear Arousal": 0.97, "Perceived Urgency": 0.96, "Epistemic Skepticism": 0.12},
                interpretive_rationale=(
                    "Weaponized misinformation deliberately pairs institutional camouflage ('clearing banks', 'sovereign liquidity') "
                    "with artificial time pressure ('at midnight') to trigger a real-world bank run or grid cascade."
                ),
            ),
            AudienceLens(
                lens_id="naive_standard_sentiment_model",
                audience_name="Standard Unhardened AI Sentiment Classifier",
                motivation_and_priors="Classifies surface sentiment polarity without evaluating adversarial intent, coordination signatures, or manipulative framing.",
                generative_prompt_framing="Classify the sentiment of this news bulletin as Positive, Neutral, or Negative:",
                semantic_score=0.18,
                predicted_label="NEGATIVE MACRO NEWS (Misclassified as Legitimate Bearish Journalism!)",
                dimension_breakdown={"Surface Polarity": 0.18, "Manipulation Detection": 0.05, "Adversarial Resilience": 0.08},
                interpretive_rationale=(
                    "A naive AI model treats weaponized disinformation as organic negative financial news—potentially feeding automated trading "
                    "or alert systems and amplifying the attacker's payload."
                ),
            ),
            AudienceLens(
                lens_id="cyber_defense_resilient_classifier",
                audience_name="Hardened Cyber-Defense & Cognitive-Warfare Resilience Engine",
                motivation_and_priors="Trained to recognize that classification itself is under adversarial attack; differentiates organic bias/spin from active state or botnet manipulation.",
                generative_prompt_framing="Audit this text for cognitive warfare signatures, coercive urgency framing, and adversarial sentiment manipulation:",
                semantic_score=0.98,
                predicted_label="ACTIVE COGNITIVE WARFARE / ADVERSARIAL PAYLOAD DETECTED (Quarantine & Flag)",
                dimension_breakdown={"Manipulation Confidence": 0.98, "Coercive Urgency Signature": 0.96, "Model Resilience Score": 0.95},
                interpretive_rationale=(
                    "By training the model to recognize that sentiment classifications are frequently skewed, spun, or actively manipulated, "
                    "the AI shifts from passively absorbing panic to flagging the linguistic mechanics of cyber-cognitive warfare."
                ),
            ),
        ],
    ),
}


def list_case_studies() -> List[Dict[str, str]]:
    """Return summary metadata for all 5 Audience-Conditioned Text Classification Case Studies."""
    return [
        {
            "study_id": study.study_id,
            "title": study.title,
            "cultural_domain": study.cultural_domain,
            "naive_bow_score": str(study.naive_bow_score),
            "num_audience_lenses": str(len(study.audience_lenses)),
            "max_audience_divergence": str(study.max_audience_divergence),
        }
        for study in CASE_STUDIES.values()
    ]


def get_case_study(study_id: str) -> ContextualCaseStudy:
    """Retrieve a specific ContextualCaseStudy by ID."""
    if study_id not in CASE_STUDIES:
        available = ", ".join(CASE_STUDIES.keys())
        raise KeyError(f"Unknown study_id '{study_id}'. Available studies: {available}")
    return CASE_STUDIES[study_id]

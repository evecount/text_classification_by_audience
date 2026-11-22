# 🎭 Text Classification by Audience: Multi-Dimensional Sentiment Mapping Across Audiences, Geographies & Parties

> **Why "Positive vs. Negative" Is Not an Objective Property of Text** — An interactive workbook and Python research toolkit exploring how **audience motivation, geopolitical media framing, financial & options market party, cybersecurity cognitive-warfare defenses, allegorical reading, and narrative segmentation** radically transform semantic classification scores in generative and representation models (`Flan-T5`, `BERT`, `RoBERTa`, and Zero-Shot NLI).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/evecount/text_classification_by_audience/blob/main/Text_Classification_In_Context_Workbook.ipynb)
[![Companion Repo: Expansive Tokenization](https://img.shields.io/badge/Companion_Repo-expansive__tokenization-38bdf8?logo=github)](https://github.com/evecount/expansive_tokenization)
[![Author: Gwendalynn Lim (SIT / NTU)](https://img.shields.io/badge/Author-Gwendalynn_Lim_%C2%B7_SIT_%2F_NTU-8b5cf6.svg)](#🎓-credits--academic-acknowledgments)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 🧠 First Principles: What *Is* Text Classification—and Why Traditional "Bag-of-Words" Falls Short?

In standard Natural Language Processing (NLP) tutorials, **Text Classification** (such as sentiment analysis on Rotten Tomatoes or IMDb movie reviews) is taught as if a piece of text has a single, fixed ground-truth label (`Positive = 1`, `Negative = 0`).

Historically, models relied on a **Bag-of-Words (BoW)** assumption: clumping and counting words in isolation (`"brilliant"`, `"unsettling"`, `"subversive"`, `"predictable"`). Modern **Generative Models** (like `T5` / `Flan-T5`) and **Contextual Representation Models** (`BERT`, `DeBERTa`) go deeper by evaluating the sequence of words in relation to the **full text** surrounding them.

Yet even modern classifiers still miss a foundational human truth:

### **Meaning Does Not Live Inside the Text Alone—It Lives in the Collision Between the Text, the Segment, and the Audience's Motivation.**

When we classify text in the real world, the semantic score is highly dependent on **four contextual axes**:

1. **🎬 Populist Audience vs. Establishment Critic Motivation (The Rotten Tomatoes Paradox):**
   A crowd-pleasing populist film can be genuinely exhilarating to general audiences while being slammed by prestige film critics—or vice versa. Even the **exact same sentence** in a review (*"An unapologetically loud, chaotic, two-hour spectacle that abandons all subtlety for pure adrenaline"*) classifies as **Strongly Negative (`0.12`)** under an *Arthouse Festival Jury Lens* and **Strongly Positive (`0.94`)** under a *Friday-Night Populist Blockbuster Lens*.
2. **📚 Allegorical & Ideological Framing (*Pride and Prejudice*):**
   Consider Jane Austen's *Pride and Prejudice* (1813). Read through a **Conventional Regency Romance Lens**, a passage about Charlotte Lucas accepting Mr. Collins for financial security is classified as pragmatic domestic compromise. Read through a **Feminist Economic & Materialist Critique Lens**, the exact same text scores as a sharp indictment of patriarchal property law and female economic disenfranchisement.
3. **⚖️ Polarized Sociopolitical & Moral Lenses (*Django Unchained*):**
   When evaluating a polarized work like Quentin Tarantino's *Django Unchained* (2012), classification depends heavily on the viewer's moral and political framework—whether a viewer evaluates the film through a **Cathartic Revisionist Justice Lens**, a **Principled Social/Historical Trauma Critique Lens**, or a **Spaghetti-Western Genre Craft Lens**.
4. **🎞️ Narrative Segmentation (Act-by-Act vs. Full-Work Aggregation):**
   A film script or novel is not a monolithic block. Lumping an entire 2-hour screenplay into one average vector destroys narrative arc polarity: **Segment 1 (Exposition / Oppression)**, **Segment 2 (Crucible / Subversion)**, and **Segment 3 (Climax / Catharsis)** carry deliberately opposing semantic charges that only make sense when classified as a trajectory.

---

## 💬 NLP as the New Code & Multi-Dimensional Event Sentiment Mapping

> *"Code itself is just a streamlined way of noting down instructions—a button. Natural Language Processing and conceptual framing are the new means of code."* — **Gwendalynn Lim**

In generative text classification (such as casting classification as a sequence-to-sequence prompt in `google/flan-t5-base`), **you do not retrain a classifier head from scratch every time your audience changes**. Instead, you program the model's semantic classifier directly through **Audience-Conditioned Framing Prompts**:

$$\text{Score}(E \mid \mathcal{A}, \mathcal{G}, t) = P_{\text{GenerativeLM}}\big(\text{Label} \;\big|\; \text{Singular Event } E,\; \text{Audience / Party } \mathcal{A},\; \text{Geography / Outlet } \mathcal{G},\; \text{Time Horizon } t\big)$$

### 🌍 Expanding the Dimensionality of Text Classification: One Singular Event Across Geographies, Parties & Markets

Traditional sentiment analysis collapses text into a **1D scalar** ($\text{Positive} \in [0, 1]$). By conditioning classification on **how one singular event is communicated and received across different geographies, institutional parties, and time windows**, we elevate text classification into a **Multi-Dimensional Content Analysis & Sentiment Mapping Tensor**:

* **Dimension 1 — Geopolitical & Editorial Geography ($\mathcal{G}$):**
  True neutrality does not exist in reporting. Take a single historical or global event—such as **the first 90 days of COVID-19 (Month 1 vs. Month 2 vs. Month 3)** or war reporting during **the Gulf War**—and track how it is framed across **The Straits Times** (Singapore), **Bloomberg / Forbes / BusinessWeek** (Financial Markets), **The Washington Post / Chicago Tribune vs. Fox News** (US Domestic Spectrum), **The Guardian** (UK), **The Toronto Star / The Globe and Mail** (Canada), and **Al Jazeera** (Middle East / Global South).
* **Dimension 2 — Stakeholder & Market Participant Party ($\mathcal{A}$):**
  In consumer sentiment and quantitative finance (**equities, free-cash-flow fundamentals, and options/derivatives flow**), a single corporate event (e.g., a 35% price hike paired with a 400% surge in out-of-the-money call options) has opposite ground-truth classifications for a **Main-Street Consumer (`0.12 Negative`)**, an **Institutional FCF Equity Analyst (`0.89 Bullish`)**, and an **Options Volatility / Gamma Desk (`0.95 High-Conviction Squeeze`)**.
* **Dimension 3 — Temporal & Structural Segment ($t$):**
  Whether tracking **Month 1 → Month 2 → Month 3** of a global crisis or **Act I → Act IV** of a screenplay, segmenting the timeline prevents naive whole-corpus averaging from erasing the trajectory.

---

## 🧭 The 8 Case-Study Suites Included in This Workbook

This repository provides a **7-part runnable Jupyter Workbook ([Text_Classification_In_Context_Workbook.ipynb](Text_Classification_In_Context_Workbook.ipynb))**, a **zero-setup Interactive Browser Studio ([index.html](index.html))**, and a **modular Python engine (`src/text_classification_in_context/`)** featuring eight pre-built multi-audience case studies proving that **true neutrality in text classification does not exist**—from global newsrooms during the first 90 days of COVID-19 and cybersecurity cognitive-warfare defenses to financial options desks and literary allegory:

| # | Case Study Suite | Text / Cultural / Financial / Cyber Artifact | Contrasting Audience & Institutional Lenses ($\mathcal{A}_1 \dots \mathcal{A}_k$) | Semantic Inversion & Resilience Demonstrated |
| :- | :--- | :--- | :--- | :--- |
| **1** | 🌐 **The Illusion of Neutrality: First 90 Days of COVID-19 & Global Media Lenses** | Identical report on border closures, quarantine orders, contact tracing & a 12% market plunge across **Months 1–3 of COVID-19** (paralleling historical war reporting like the **Gulf War**) | 1. **The Straits Times (SG Civic Governance)**<br>2. **Bloomberg / Forbes / BusinessWeek (Markets)**<br>3. **WaPo / Chicago Tribune vs. Fox News (US Spectrum)**<br>4. **The Guardian / Toronto Star / Globe and Mail / Al Jazeera** | How the exact same factual incident classifies as **Positive Institutional Readiness (`0.86`)**, **Severe Bearish Shock (`0.11`)**, or **Constitutional/Equity Conflict (`0.29`–`0.58`)** across outlets and across Months 1–3. |
| **2** | 🛡️ **Cybersecurity, Cognitive Warfare & Adversarial Model Resilience** | Weaponized Disinformation Bulletin (*"URGENT VERIFIED LEAK: Regional grid controllers and clearing banks will freeze retail withdrawals at midnight..."*) | 1. **Targeted Retail Citizen (Panic Target)**<br>2. **Unhardened Naive Sentiment Model**<br>3. **Hardened Cyber-Defense Resilience Engine** | How training an AI to expect **spin, bias, and active manipulation** stops it from classifying a cognitive-warfare payload as organic negative news (`0.18`) and flags it as an **Adversarial Attack (`0.98`)**. |
| **3** | 📈 **Financial Markets, Options Flow & Consumer Sentiment** | SaaS Earnings & Options Alert (*"35% price hike triggers 18% SMB churn spike while free-cash-flow margins expand +640 bps and OTM call option volume surges 400%..."*) | 1. **Main-Street Consumer / SMB Advocate**<br>2. **Institutional Free-Cash-Flow Equity Analyst**<br>3. **Options & Volatility Derivatives Desk (Gamma Trader)** | Why standard "one-score" financial sentiment fails: the exact same release is **Hostile Consumer Extraction (`0.12`)**, **Bullish Pricing Power (`0.89`)**, and an **Explosive Gamma Squeeze Signal (`0.95`)**. |
| **4** | 🍅 **The Rotten Tomatoes Paradox** | Populist Action Spectacle Review (*"Unapologetically loud, maximalist, trades quiet character study for relentless kinetic spectacle..."*) | 1. **Prestige Arthouse Critic**<br>2. **Populist Blockbuster Fan**<br>3. **Box-Office Studio Executive** | How the exact same review text flips from **Negative (`0.14`)** to **Positive (`0.94`)** based purely on critic vs. audience motivation. |
| **5** | 📖 **Allegorical & Feminist Literary Critique** | Jane Austen's *Pride and Prejudice* (Charlotte Lucas's marriage proposal & the entailment of Longbourn) | 1. **Regency Romance Traditionalist**<br>2. **Feminist Materialist Scholar**<br>3. **Satirical Social Historian** | How allegorical clumping of words (`"establishment"`, `"preservative from want"`, `"property"`) shifts classification from *Domestic Harmony (`0.82`)* to *Systemic Critique (`0.16`)*. |
| **6** | 🤠 **Polarized Cinema & Moral Reception** | Quentin Tarantino's *Django Unchained* (Candyland confrontation & revisionist revenge finale) | 1. **Revisionist Catharsis Viewer**<br>2. **Principled Social/Historical Critic**<br>3. **Genre & Cinematography Formalist** | Why polarized audiences assign diametrically opposite ethical and artistic scores (`0.91` vs. `0.19`) to identical scenes and dialogue segments. |
| **7** | 🎞️ **Film Script Segment Trajectory** | 4-Segment Screenplay Arc (*Segment I: Bleak Setup -> Segment II: False Hope -> Segment III: Betrayal -> Segment IV: Subversive Triumph*) | 1. **Naive Whole-Text Bag-of-Words**<br>2. **Segment-Aware Arc Classifier** | Why lumping a whole film script together yields a flat, misleading `0.47 Neutral` score while segment-level classification captures the true dramatic oscillation (`0.08 -> 0.96`). |
| **8** | 🏛️ **Subcultural & Fandom Framing** | Mythic / Anime / LARP Narrative Passage (*"A reckless katabasis into the abyss that shattered canon before ten minutes of sakuga chaos..."*) | 1. **Uninitiated General Reader**<br>2. **Hardcore Canon Purist**<br>3. **Transformative LARP / Anime Fan** | How community membership flips terms like *"shattered canon"*, *"unhinged"*, or *"sakuga chaos"* from a defect (`0.22`) to a generational masterpiece (`0.97`). |

---

## 📂 Repository Structure

```text
text_classification_in_contexy/
├── Text_Classification_In_Context_Workbook.ipynb              # 🎯 Main 7-Part Interactive Workbook (Bag-of-Words vs. T5 Generative vs. Audience Lenses)
├── index.html                                                 # 🌐 Interactive Browser Studio (Test Audience Lenses & Film Segments Live!)
├── JELLOBEAN_TEXT_CLASSIFICATION_NOTES.md                     # 📝 Conceptual Treatise: NLP as the New Code, Allegory & Critic vs. Populist Bias
├── src/
│   └── text_classification_in_context/
│       ├── __init__.py
│       ├── case_studies.py                                    # 5 Multi-Audience Case Studies (Rotten Tomatoes, Pride & Prejudice, Django, Script Segments, Fandom)
│       └── engine.py                                          # Bag-of-Words vs. Generative T5 Audience-Conditioned Classifier & Segment Trajectory Engine
├── requirements.txt                                           # Python dependencies (transformers, torch, scikit-learn, pandas, numpy)
└── README.md                                                  # First-Principles Guide, Architecture & Academic Credits
```

---

## 🚀 Quickstart

### 1. Clone & Install

```bash
git clone https://github.com/evecount/text_classification_by_audience.git
cd text_classification_by_audience
pip install -r requirements.txt
```

### 2. Launch the Interactive Workbook or Browser Studio

```bash
jupyter notebook Text_Classification_In_Context_Workbook.ipynb
```

Or open **`index.html`** directly in your browser to interactively switch audience personas on *Rotten Tomatoes*, *Pride and Prejudice*, and *Django Unchained* and inspect the live semantic score inversions!

---

## 🧪 What You Will Explore in the Workbook

1. **Part 1 — Baseline Text Classification: Bag-of-Words vs. Full-Text Sequence Context:**
   See why counting isolated positive/negative words fails when words interact across a whole paragraph.
2. **Part 2 — Generative Text Classification with `T5` / `Flan-T5`:**
   How encoder-decoder generative models turn classification into natural-language generation—and why **NLP prompting is the new code**.
3. **Part 3 — The Rotten Tomatoes Paradox (Populist Audience vs. Prestige Critic Bias):**
   Run the exact same review through contrasting audience motivation prompts and quantify the **Audience Polarity Divergence ($\Delta_{\text{audience}}$)**.
4. **Part 4 — Allegorical & Ideological Lenses (*Pride and Prejudice*):**
   Classify classic literature under a Regency Romance lens vs. a Feminist Economic Critique lens.
5. **Part 5 — Polarized Cinema & Moral Reception (*Django Unchained*):**
   Measure how different ethical and artistic frameworks score controversial cinema across multiple dimensions (*Catharsis*, *Historical Reverence*, *Subversive Craft*).
6. **Part 6 — Screenplay & Narrative Segmentation (Why Lumping Full Text Hides the Arc):**
   Compare whole-document classification against segment-by-segment trajectory scoring across Acts I–IV.
7. **Part 7 — Custom Audience-Conditioned Classifier Builder:**
   Plug in any review, book chapter, or film scene, define your own audience personas and motivations, and export a structured `.json` bias & reception audit.

---

## 🎓 Credits & Academic Acknowledgments

* **Author & Concept Creator:** **Gwendalynn Lim (婉婷) — "1ightray"**
  * **B.Sc. (Honours) in Applied Computing**, **Singapore Institute of Technology (SIT)**
  * **Advanced Machine Learning & AI (SCTP)**, **Nanyang Technological University (NTU)**
  * **Founder & CTO**, **Eve Count** ([gwen@evecount.com](mailto:gwen@evecount.com) · [GitHub: @evecount](https://github.com/evecount) · [LinkedIn](https://www.linkedin.com/in/gwendalynnlim/))
* **Academic & Educational Gratitude:**
  Special thanks to the faculty, curriculum, and research community at the **Singapore Institute of Technology (SIT)** and **Nanyang Technological University (NTU)** for the coursework in generative text classification, T5 sentiment modeling, and representation learning that inspired this study on audience-conditioned semantics.

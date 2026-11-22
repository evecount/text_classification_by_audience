# 🎭 Text Classification in Context: Multi-Dimensional Sentiment Mapping Across Audiences, Geographies & Parties

> **Dispatched from Jellobean (One) & Executed by Antigravity**
> **Author & Concept:** **Gwendalynn Lim (婉婷)** — *Singapore Institute of Technology (SIT) · Nanyang Technological University (NTU)*
> **Repository:** [github.com/evecount/text_classification_in_contexy](https://github.com/evecount/text_classification_in_contexy)

---

## 1. Core Thesis: NLP Is the New Code & Why "Neutral" Text Classification Is a Myth

1. **Conceptual Architecture Over Boilerplate Code:**
   - Code is simply a button—a streamlined notation for instructions. In modern generative AI (e.g., `T5` / `Flan-T5` sequence-to-sequence classification), **Natural Language Processing and conceptual framing are the new means of code**.
   - Traditional **Bag-of-Words (BoW)** models clump and sort words in isolation, while sequence models consider those clumps in relation to the full text. Yet both fail when they assume a text has a single objective sentiment label.
2. **The Illusion of Neutrality (One Singular Event Across Geographies & Outlets):**
   - When a single historical event is communicated across global newsrooms, there is no "neutral" baseline—every publication classifies and frames the event according to its geographic, institutional, and ideological priorities:
     - **Case Study: The First 90 Days of COVID-19 (Month 1, Month 2, Month 3) & Historical Conflicts (The Gulf War):**
       - **Singapore (*The Straits Times*):** Framed through civic order, contact-tracing precision, institutional readiness, and public-health solidarity (`0.86 Positive Institutional Response`).
       - **Global Financial Press (*Bloomberg*, *Forbes*, *BusinessWeek*):** Framed through liquidity shock, supply-chain freeze, VIX volatility, and macroeconomic contraction (`0.11 Severe Bearish Shock`).
       - **US Polarized Spectrum (*Washington Post* / *Chicago Tribune* vs. *Fox News*):** Diverges sharply between federal public-health mobilization vs. constitutional/economic reopening resistance (`0.29 Polarized Clash`).
       - **Commonwealth, UK, Canadian & Global South Press (*The Guardian*, *Toronto Star*, *The Globe and Mail*, *Al Jazeera*):** Framed through healthcare worker protection, social safety nets, and global cross-border equity (`0.58 Structural Equity Audit`).
3. **Consumer Sentiment, Quantitative Finance & Options Flow:**
   - This content-analysis breakdown extends directly to **financial sentiment analysis and options/derivatives tracking**.
   - A single corporate event (e.g., a 35% enterprise price hike causing an 18% SMB churn spike while expanding free-cash-flow margins +640 bps and sparking a 400% surge in OTM call options) yields completely different classifications depending on the party:
     - **Main-Street Consumer / SMB Customer:** `0.12 Strongly Negative` (predatory pricing & churn pain)
     - **Institutional FCF Equity Analyst:** `0.89 Bullish Outperform` (proven pricing power & margin expansion)
     - **Options & Volatility Derivatives Desk:** `0.95 High-Conviction Gamma Squeeze Signal` (extreme upside call skew)
4. **Rotten Tomatoes Critic vs. Populist Bias, Literary Allegory & Polarized Cinema:**
   - **Rotten Tomatoes / IMDb Paradox:** A populist crowd-pleaser slammed by prestige critics flips from `0.14 Negative` (Arthouse Jury Lens) to `0.94 Positive` (Friday-Night Populist Lens) on the exact same review text.
   - **Allegorical Literary Reading (*Pride and Prejudice*):** Charlotte Lucas's marriage to Mr. Collins classifies as `0.82 Domestic Security` under a traditional Regency Romance lens vs. `0.16 Bleak Economic Coercion` under a Feminist Materialist lens.
   - **Polarized Cinema (*Django Unchained*):** Diverges between `0.91 Mythic Retributive Catharsis` vs. `0.19 Solemn Historical Trauma Critique`.
   - **Narrative Segmentation (Screenplay Acts I–IV):** Lumping a full film script together cancels out Act III's betrayal (`0.08`) against Act IV's liberation (`0.96`), producing a false `0.47 Neutral` score.

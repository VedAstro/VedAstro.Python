"""
DEMO: RAG — Semantic Search of Classical Vedic Texts
USE CASE: Ask a plain-English question and get back the most relevant passages
          from classical Vedic astrology books (BPHS, Phaladeepika, Hindu
          Predictive Astrology, etc.) — the same RAG feature that powers the
          "Vedic Books" search on vedastro.org.
DIFFICULTY: Intermediate

WHAT YOU'LL LEARN:
- How to list which classical texts are searchable (GetAvailableSourceTexts)
- How to run a natural-language semantic search (SearchSourceText)
- How to read each result: source book, page number, similarity score, text
- How to narrow a search to a single book and tune topK / contextSize

HOW IT WORKS:
Your query is embedded and matched against a vector index built from the full
text of the classical books. You get back the passages whose meaning is closest
to your question — no exact keywords required. This is the same retrieval step
used internally by VedAstro's AI/RAG enrichment.

PREREQUISITES:
- pip install vedastro

RUN:
python demo_rag_vedic_books.py

EXPECTED OUTPUT (abridged):
Available source texts:
  - Brihat-Parashara-Hora-Shastra
  - Hindu-Predictive-Astrology
  - Phaladeepika
  ...

Query: "effects of Saturn in the 7th house"
  [1] Hindu-Predictive-Astrology  p.142  (relevance 71.3%)
      Saturn in the 7th house makes the native ...
  ...
"""

# Import everything from VedAstro
from vedastro import *


def relevance_pct(passage):
    """Convert the raw similarity score (lower = closer) to a 0-100% relevance.

    Mirrors the formula used by the website's RAG UI: (1 - score) * 100.
    Defaults to a score of 1 (0% relevance) when the field is missing.
    """
    score = passage.get("score", 1)
    pct = (1 - score) * 100
    # clamp to 0-100 so odd scores never print a negative / >100 value
    return max(0.0, min(100.0, pct))


def print_passages(passages):
    """Pretty-print a list of retrieved passages."""
    if not passages:
        print("  (no passages found — try different wording)")
        return

    # closest match first (lowest score = highest relevance)
    passages = sorted(passages, key=lambda p: p.get("score", 1))

    for i, p in enumerate(passages, start=1):
        source = p.get("sourceName") or "Unknown source"
        page = p.get("pageNumber") or "?"
        text = (p.get("text") or "").strip()
        print(f"  [{i}] {source}  p.{page}  (relevance {relevance_pct(p):.1f}%)")
        print(f"      {text}\n")


def main():
    # Step 1: Set API Key
    # Free tier: 'FreeAPIUser' (5 requests/min). Premium key: vedastro.org/API.html
    Calculate.SetAPIKey('FreeAPIUser')

    # Step 2: Discover which classical texts are available to search
    print("Available source texts:")
    for name in Calculate.GetAvailableSourceTexts():
        print(f"  - {name}")
    print()

    # Step 3: Basic semantic search across ALL texts
    # No exact keywords needed — the query is matched by meaning.
    query = "effects of Saturn in the 7th house"
    print(f'Query: "{query}"')
    results = Calculate.SearchSourceText(query)  # topK defaults to 5
    print_passages(results)

    # Step 4: Scoped search — restrict to one book and tune the knobs
    #   sourceName  : limit retrieval to a single classical text
    #   topK        : how many passages to return
    #   contextSize : characters of surrounding context per passage (default 600)
    query2 = "results of Jupiter aspecting the Moon"
    print(f'Query (Hindu Predictive Astrology only): "{query2}"')
    results2 = Calculate.SearchSourceText(
        query2,
        topK=3,
        sourceName="Hindu-Predictive-Astrology",
        contextSize=800,
    )
    print_passages(results2)


if __name__ == "__main__":
    main()

# NEXT STEPS:
# - Swap in your own question — anything about planets, houses, yogas, dasas.
# - Drop the sourceName argument to search every book at once.
# - Feed the retrieved passages into an LLM prompt to build a cited astrology
#   chatbot (retrieval-augmented generation).

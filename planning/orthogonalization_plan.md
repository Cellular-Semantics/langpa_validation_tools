# Plan: Debiasing Embeddings via Orthogonalization for Biology Domain

## Background
- Goal: Remove shared “general biology” context from program/term embeddings so similarity reflects program-specific signal (e.g., gliosis vs OPC states) rather than broad domain bias.
- Why not mean/median cosine shifts: scalar rescaling does not change vector geometry; shared bias remains. Orthogonalization projects vectors off the bias basis, altering geometry to suppress domain drift.
- Risk: Over-subtraction if the bias basis overlaps true signal; instability if the bias corpus is small or narrow.

## Corpora
- Bias corpus (to define background direction):
  - Diverse, high-level biology snippets/phrases (textbook intros, broad PubMed abstracts, GO slim terms, high-level MeSH headings).
  - Target size: hundreds–thousands entries; if limited, augment with synthetic generic phrases (e.g., “This study investigates biological mechanisms…”).
- Target corpus:
  - Program names and short descriptions from DeepSearch runs (and potentially GO comparison tables), normalized for consistent tokenization.

## Method
1) Embed corpora (same model used for program similarity; cache to `data/embeddings_*`).
2) Build bias basis:
   - Center bias embeddings; take top k PCs (start k=1–3) as bias directions.
   - Normalize each basis vector to unit length.
   - For very small bias sets, test k=1 to avoid overfitting noise.
3) Orthogonalize:
   - For each target embedding `v`, remove its projection onto the bias basis: `v' = v - (v·B^T)B`, then L2-normalize.
   - Store debiased vectors alongside originals (e.g., `embeddings_name_debiased.npy`).
4) Similarity:
   - Compute cosines on debiased vectors for program matching; optionally blend with gene Jaccard as currently done.
   - Recompute baseline cosine statistics on debiased space for any rescaling.

## Validation
- Controls: known positives (mitosis–meiosis, stemness-related pairs) should stay high; negatives (mitosis–supernova) should drop further.
- Bootstrapping: resample bias corpus to estimate variance of bias directions; if unstable, expand corpus or reduce k.
- Coverage checks: compare match rates and combined similarity before/after debiasing; inspect edge cases where names differ but biology matches.

## Integration Steps
- Add bias corpus acquisition script (pull generic biology text/terms; allow synthetic augmentation).
- Add orthogonalization utility (NumPy/PCA) to embedding pipeline; emit debiased `.npy` + index CSV.
- Update `process_deepsearch.py` to opt into debiased embeddings via flag/env (e.g., `USE_ORTHOGONALIZATION=1`), falling back gracefully if files missing.
- Refresh downstream outputs: rerun `make master_report` to regenerate data, comparisons, figures, reports with debiased similarities.
- Document usage and limitations (small corpus instability, potential over-subtraction) in AGENTS/README.

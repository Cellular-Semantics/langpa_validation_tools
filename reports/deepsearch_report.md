# DeepSearch Consistency and GO Coverage Report

## Run-to-run gene program consistency
DeepSearch run pairs are generally stable: the combined similarity metric (50 % gene-set Jaccard, 50 % name overlap) ranges from ~0.24 to ~0.54. Gliosis, Proliferative 2, and AC-gliosis-like 1 display the tightest reproducibility, while mixed OPC/NPC states fluctuate more, with higher fractions of unmatched programs. These results reinforce the need to treat program-level interpretations as probabilistic, especially in lineage-plastic contexts.

![Run-to-run similarity](../analysis/run_consistency.svg)

## GO enrichment coverage
All but one comparison file reports complete GO coverage: DeepSearch captured every GO term listed in the GSEA output, except for the Proliferative 2 model where 30 umbrella DNA-metabolism terms remained unmatched (76 % coverage). The gliosis-hypoxia and OPC-like 1 comparison markdowns still lack standardized tables, so those gene sets are excluded from the aggregate coverage stats.

![GO coverage](../analysis/go_coverage.svg)

## Methods
- Gene-program names from each DeepSearch run were embedded with `text-embedding-3-large`. A reference panel of unrelated biology phrases provided the baseline cosine distribution; all program–program cosines were mean-centered relative to that background to emphasize signal above random thematic similarity.
- For every run pair, similarities were computed between all program combinations. Gene-level overlap used the Jaccard index of their supporting gene sets, and name similarity used the rescaled cosine scores. The combined similarity equals the arithmetic mean of these two terms (50 % gene Jaccard + 50 % name cosine). Programs from the smaller run were linked to the highest-scoring partner that exceeded the matching threshold, producing one-to-one matches plus explicit unmatched lists.
- GO coverage statistics were derived by comparing each program’s DeepSearch annotation set with the manually curated GO tables supplied for the corresponding comparison. Coverage is reported as the fraction of GO entries that had at least one DeepSearch match; comparisons lacking tables were excluded. Visual summaries aggregate these metrics without additional weighting or smoothing.
## Methods
- Gene-program names from each DeepSearch run were embedded with `text-embedding-3-large`. A reference panel of unrelated biology phrases provided the baseline cosine distribution; all program–program cosines were mean-centered relative to that background to emphasize signal above random thematic similarity.
- For every run pair, similarities were computed between all program combinations. Gene-level overlap used the Jaccard index of their supporting gene sets, and name similarity used the rescaled cosine scores. The combined similarity equals the arithmetic mean of these two terms (50 % gene Jaccard + 50 % name cosine). Programs from the smaller run were linked to the highest-scoring partner that exceeded the matching threshold, producing one-to-one matches plus explicit unmatched lists.
- GO coverage statistics were derived by comparing each program’s DeepSearch annotation set with the manually curated GO tables supplied for the corresponding comparison. Coverage is reported as the fraction of GO entries that had at least one DeepSearch match; comparisons lacking tables were excluded. Visual summaries aggregate these metrics without additional weighting or smoothing. The underlying GO tables were generated with an LLM that groups related GO terms into coherent program summaries; individual grouped examples are included in each per-run report.

## Novel gene programs without GO counterparts
Ranked by the number of supporting genes (DeepSearch run 1).

| Annotation | Program | Supporting genes |
| --- | --- | --- |
| OPC-like 2 | Lipid Metabolism and Membrane Remodeling | 12 |
| NPC-neuronal-like 2 | Glioma Stem Cell Maintenance and Therapy Resistance | 8 |
| NPC-neuronal-like 1 | Transcriptional Regulation and Chromatin Remodeling | 7 |
| OPC-like 2 | Hypoxia Response and Angiogenic Signaling | 7 |
| AC-neuronal-like | Glioblastoma Immune Suppression | 6 |
| OPC-like 2 | Amino Acid Metabolism and Nutrient Transport | 6 |
| AC-gliosis-like 1 | Angiogenesis and Vascular Remodeling | 5 |
| NPC-neuronal-like 1 | GABAergic Neurotransmission | 5 |
| NPC-neuronal-like 1 | cAMP Signaling and Kinase Cascades | 4 |
| OPC-NPC-like | Sonic Hedgehog and GLI Signaling | 4 |

## Limitations and notes
- Comparison sets 9 (gliosis-hypoxia) and 12 (OPC-like 1) lack the required GO table, so they’re omitted from GO coverage metrics.
- Duplicate DeepSearch runs (identical program lists) are automatically detected and omitted from the similarity plot.
- The 50 / 50 similarity metric is heuristic: name changes between runs still rely on gene overlap to link programs.

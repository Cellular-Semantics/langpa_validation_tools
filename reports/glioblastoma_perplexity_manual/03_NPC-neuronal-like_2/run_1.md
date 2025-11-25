# Report: 03_NPC-neuronal-like_2 (run_1.md)

**Cell type:** malignant glioblastoma cells
**Disease:** glioblastoma
**Tissue:** brain

## Program Summaries
### Extracellular Matrix Remodeling & Invasion
Enrichment for genes encoding ECM proteins, ECM remodelers and their regulators associated with glioblastoma cell invasion, mesenchymal transition, and tumor angiogenesis. Programs include collagen (COL3A1, COL6A3), periostin (POSTN), TGFBI, FAP, SMOC2, and multiple matrix metalloproteinases (ADAMTS3). Periostin and FAP+ mesenchymal cells promote active angiogenesis, abnormal vascular structure, and stemness.

**Predicted impacts:**
- Enhanced invasion through remodeling of matrix
- Promotion of abnormal angiogenesis and vascular niche formation
- Increased tumor cell migration

**Supporting genes:** COL3A1, COL6A3, POSTN, TGFBI, FAP, SMOC2, ADAMTS3, FRAS1

**References:** [146], [34], [41], [49]

**Biological processes:**
- ECM remodeling: COL3A1, COL6A3, POSTN, TGFBI, FAP, ECM-regulatory lncRNAs (refs: [34], [146], [41], [49])

**Cellular components:**
- Tumor microenvironment: ECM: COL3A1, COL6A3, POSTN, FAP, SMOC2, TGFBI (refs: [34])

### Glutamatergic & Synaptic Signaling Deregulation
Enrichment for vesicular glutamate transporters (SLC17A6), glutamate receptor components (GRIN2A), and synaptic proteins (SV2B, SYT1, RIMBP2). Tumors hijack glutamatergic synapses and signaling to promote invasion, hyperexcitability, and stem cell maintenance.

**Predicted impacts:**
- Enhanced glutamatergic signaling drives tumor proliferation and invasion
- Tumor-induced hyperexcitability and epileptogenesis
- Aberrant synaptic connectivity fosters glioblastoma stem cell niche

**Supporting genes:** SLC17A6, GRIN2A, SV2B, SYT1, RPH3A, RIMBP2

**References:** [106], [107]

**Biological processes:**
- Glutamate signaling: SLC17A6, GRIN2A, SV2B, SYT1, RIMBP2, RPH3A (refs: [106], [107])

**Cellular components:**
- Synaptic machinery: SYT1, SV2B, RIMBP2, RPH3A (refs: [107])

### Axon Guidance & Cell Migration
Collective enrichment for axon guidance proteins (EFNA5, SEMA3C, UNC5D, CNTN5, CNTNAP4), with roles in migration/invasion, tumor plasticity, and stem cell maintenance.

**Predicted impacts:**
- Facilitates invasion via re-purposing axon guidance programs
- Supports tumor cell plasticity, migration, and self-renewal

**Supporting genes:** EFNA5, SEMA3C, UNC5D, CNTN5, CNTNAP4

**References:** [51], [56]

**Biological processes:**
- Axon guidance: EFNA5, SEMA3C, UNC5D, CNTN5, CNTNAP4 (refs: [56])

**Cellular components:**
- Growth cone/axon guidance machinery: EFNA5, SEMA3C, UNC5D (refs: [56])

### Transcriptional & Epigenetic Reprogramming
Enrichment for transcription factors (EBF1, EBF2, CUX2, MYT1L, POU6F2, RUNX1T1), RNA-binding proteins (RBFOX1), and splicing factors, which drive stemness, plasticity, and resistance. Links to aberrant splicing program.

**Predicted impacts:**
- High plasticity and drug resistance via transcriptional reprogramming
- Enhanced self-renewal and stemness

**Supporting genes:** EBF1, EBF2, CUX2, MYT1L, POU6F2, RUNX1T1, RBFOX1, SRRM4

**References:** [75], [83]

**Biological processes:**
- Transcriptional regulation: EBF1, EBF2, CUX2, MYT1L, POU6F2, RUNX1T1 (refs: [83])
- Alternative RNA splicing: RBFOX1, SRRM4 (refs: [75])

**Cellular components:**
- Nucleus (transcriptional/epigenetic complexes): RBFOX1, CUX2, RUNX1T1, SRRM4 (refs: [75])

### Potassium Channel & Ion Transport Adaptations
Several potassium channel (KCNJ6, KCNC2, DPP10) and ion transport modulators support cellular adaptation for migration, volume regulation, and therapy resistance.

**Predicted impacts:**
- Enhanced migration and invasiveness
- Potential therapy resistance via cell volume regulation

**Supporting genes:** KCNJ6, KCNC2, DPP10

**References:** [123]

**Biological processes:**
- Ion transport regulation: KCNJ6, KCNC2, DPP10 (refs: [123])

**Cellular components:**
- Plasma membrane (ion channels): KCNJ6, KCNC2, DPP10 (refs: [123])

## GO Comparison
| Program | Similar GO term(s) | Novel aspects |
| --- | --- | --- |
| Extracellular Matrix and Invasion | collagen-containing extracellular matrix (GO:0062023), catenin complex (GO:0016342) | Connects ECM gene activation to angiogenesis, invasion, and therapy resistance; specifically highlights FAP, POSTN, and pathway-level roles in progression[^2_1][^2_2][^2_3][^2_4][^2_5][^2_6] |
| Glutamatergic Excitotoxicity and Synapse Dynamics | synaptic vesicle membrane (GO:0030672), exocytic vesicle membrane (GO:0099501), ionotropic glutamate receptor complex (GO:0008328), excitatory synapse (GO:0060076) | Links glutamate transport and receptor genes with therapy resistance, neuron-tumor crosstalk, and microenvironment dynamics—integrating SLC17A6, GRIN2A, synaptic gene neuromodulation in GBM[^2_7][^2_8][^2_9][^2_10][^2_11][^2_12] |
| Glioma Stem Cell Maintenance and Therapy Resistance | None (no direct GO term match) | Identifies GFRA1, GREM2, RUNX1T1, MYT1L, and transcription factors as central to stemness, self-renewal, and chemoresistance in GBM microenvironment (roles not annotated or rarely linked in GSEA) [^2_13][^2_14][^2_15] |

## References
- [106] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4412924/; Notes: Glioblastoma upregulates glutamatergic gene expression in tumor-associated microglia/macrophages.
- [107] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8499409/; Notes: Glutamate receptor expression drives tumor progression and excitotoxicity.
- [123] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3230698/; Notes: Potassium channels critical for glioma migration and invasion.
- [146] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9044776/; Notes: FAP+ mesenchymal cells promote angiogenesis in glioblastoma.
- [34] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10241737/; Notes: Review of ECM role in glioblastoma progression and mechanisms.
- [41] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9128179/; Notes: COL6A3 essential for tumor invasion; knockdown reduces invasion.
- [49] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6971284/; Notes: POSTN marks glioma invasion and malignancy.
- [51] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7238747/
- [56] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6987732/; Notes: Eph/ephrin, semaphorin, UNC5/netrin signaling modulate glioma migration and stemness.
- [75] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7155901/; Notes: Splicing programs strongly influence glioblastoma phenotype and prognosis.
- [83] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7296349/; Notes: EBF family TFs drive neuronal development, differentiation, and are implicated in glioblastoma regulation.

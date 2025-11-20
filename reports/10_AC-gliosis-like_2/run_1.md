# Report: 10_AC-gliosis-like_2 (run_1.md)

**Cell type:** malignant glioblastoma cell
**Disease:** glioblastoma
**Tissue:** brain

## Program Summaries
### Mesenchymal Invasion & EMT
Genes such as POSTN, HMGA2, ITGA3, SERPINE1, EMP1, ANXA2 drive extracellular matrix remodeling, loss of adhesion, invasion and mesenchymal transition in glioblastoma. POSTN/EMP1/ANXA2 anchor mesenchymal subtypes and promote integrin-mediated invasion. HMGA2 supports EMT transcriptional programs. SERPINE1 enhances invasion and correlates with poor-prognosis, acting together with EMT and migration genes.

**Predicted impacts:**
- increased invasion and migration
- promotion of mesenchymal phenotype
- therapy resistance due to enhanced motility

**Supporting genes:** POSTN, HMGA2, SERPINE1, ITGA3, EMP1, ANXA2

**References:** [2], [42]

**Biological processes:**
- epithelial-mesenchymal transition (EMT): POSTN, HMGA2, ANXA2 (refs: [2])
- integrin-mediated cell invasion: POSTN, ITGA3, ANXA2 (refs: [2])
- plasminogen activation and matrix degradation: SERPINE1, ANXA2 (refs: [42])

**Cellular components:**
- extracellular matrix: EMP1, ANXA2 (refs: [42])

**Reference notes:**
- Comprehensive review of POSTN/EMT in glioblastoma
- Empirical data on SERPINE1 role in GBM cell invasion

### Stemness & WNT-Driven Maintenance
LEF1, WNT16, and HMGA2 are central to maintaining glioblastoma stemness and proliferation through canonical and non-canonical WNT pathways. LEF1 is a transcriptional mediator of WNT signaling, required for stem cell traits and proliferation.

**Predicted impacts:**
- increased self-renewal of tumor stem cells
- enhanced tumor proliferation and resistance

**Supporting genes:** LEF1, WNT16, HMGA2

**References:** [19]

**Biological processes:**
- WNT signaling pathway: LEF1, WNT16, HMGA2 (refs: [19])
- maintenance of glioblastoma stem cells: LEF1, HMGA2 (refs: [19])

**Cellular components:**
- nucleus: LEF1 (refs: [19])

**Reference notes:**
- Summary of WNT/LEF1/GBM stemness axis

### Angiogenesis & Microenvironment Interaction
ANGPT1, ALK, PDGFD, POSTN, COL22A1, COL23A1, COL25A1, COL27A1 and ANXA2, TMEM154 drive angiogenic and microenvironmental cues in glioblastoma. VEGFA-independent mechanisms are engaged by ANGPT1, POSTN and PDGFD.

**Predicted impacts:**
- promoted tumor vascularization
- microenvironment remodeling
- increased resistance to anti-angiogenic therapies

**Supporting genes:** ANGPT1, PDGFD, POSTN, COL22A1, COL23A1, COL25A1, COL27A1, ANXA2, TMEM154

**References:** [39]

**Biological processes:**
- angiogenesis: ANGPT1, PDGFD, POSTN (refs: [39])

**Cellular components:**
- vascular niche: ANGPT1, COL22A1, COL23A1, COL25A1, COL27A1 (refs: [39])

**Reference notes:**
- Review of vascular niche and angiogenesis drivers in GBM

### Neuronal-Synaptic & Neurotransmitter Modulation
Genes such as GRM7, GABBR2, SLC18A1, NTSR1, CAMK2A/2B, and RGS20 modulate neurotransmitter signaling, neuron-glia synaptic interaction, and excitatory/inhibitory balance in glioblastoma. AMPA and GABAergic interactions enable bidirectional synaptic communication influencing proliferation and invasion.

**Predicted impacts:**
- increased responsiveness to neuronal activity
- modulation of proliferation and invasion via synaptic transmission

**Supporting genes:** GRM7, GABBR2, CAMK2A, CAMK2B, SLC18A1, NTSR1, RGS20

**References:** [186]

**Biological processes:**
- neuron-to-glioma synapse formation: GRM7, GABBR2, CAMK2A, CAMK2B (refs: [186])

**Cellular components:**
- synaptic membrane: GRM7, GABBR2 (refs: [186])

**Reference notes:**
- Glioma-neuron synapse function in tumor progression

### Hypoxia/Metabolic Stress Adaptation
Genes such as CA2, GDF15, EGR1, TRIB3, RCAN1, and SLC4A4 modulate metabolic adaptation to hypoxia and cellular stress. Carbonic anhydrases and GDF15 regulate pH and apoptosis, EGR1 controls hypoxic gene expression. TRIB3 and RCAN1 contribute to autophagic and stress resistance.

**Predicted impacts:**
- enhanced cell survival under hypoxia
- increased resistance to metabolic stress and therapeutic intervention

**Supporting genes:** CA2, GDF15, EGR1, TRIB3, RCAN1, SLC4A4

**References:** [133]

**Biological processes:**
- response to hypoxia and metabolic stress: CA2, GDF15, TRIB3 (refs: [133])

**Cellular components:**
- mitochondrion: GDF15, TRIB3 (refs: [133])

**Reference notes:**
- Metabolic stress, hypoxia and GBM cellular adaptation

## GO Comparison
| Program | Similar GO term(s) | Novel aspects |
| --- | --- | --- |
| **Mesenchymal Invasion & EMT** | extracellular structure organization (GO:0043062); extracellular matrix organization (GO:0030198); collagen fibril organization (GO:0030199); negative regulation of cell-matrix adhesion (GO:0001953) | **Identifies specific ECM-remodeling mechanisms:** SERPINE1-PAI1 plasminogen activation axis; ANXA2 membrane repair and integrin stabilization; POSTN-integrin bidirectional signaling. GSEA only identifies structural terms; DeepSearch reveals active molecular mechanisms driving invasion and dispersal. |
| **Stemness & WNT-Driven Maintenance** | regulation of MAP kinase activity (GO:0043405); negative regulation of Ras protein signal transduction (GO:0046580); negative regulation of small GTPase mediated signal transduction (GO:0051058) | **Identifies dedicated stemness maintenance circuit:** WNT/LEF1 self-renewal axis independent of classical RTK signaling. DeepSearch locates transcriptional stemness factors; GSEA captures only downstream signaling consequences. **Mechanistic specificity:** LEF1 nuclear transcriptional function in maintaining GSC pools. |
| **Angiogenesis & Microenvironment Interaction** | extracellular matrix organization (GO:0030198); collagen fibril organization (GO:0030199); angiotensin-activated signaling pathway (GO:0038166); cellular response to angiotensin (GO:1904385); collagen-containing extracellular matrix (GO:0062023) | **Identifies non-canonical angiogenic pathways:** ALK-Pleiotrophin axis; PDGFD-independent ANGPT1 Tie2 signaling (distinct from VEGFA); collagen-diversity effect suggesting specialized vascular niches. DeepSearch reveals redundancy and alternative angiogenic routes not captured by GO pathway annotations. |
| **Neuronal-Synaptic & Neurotransmitter Modulation** | regulation of neuronal synaptic plasticity (GO:0048168); regulation of neurotransmitter receptor activity (GO:0099601); synaptic membrane (GO:0097060); dendritic spine membrane (GO:0032591); synaptic vesicle membrane (GO:0030672) | **Novel integration of bidirectional neuron-glioma synaptic communication:** DeepSearch identifies coordinated expression of presynaptic (CAMK2, GRM7), postsynaptic (GABBR2), and vesicular (SLC18A1) machinery in tumor cells—enabling exploitation of neuronal synapses for growth signals. **Mechanistic advance:** Reveals neurotensin (NTSR1) and GABAergic (GABBR2) crosstalk modulating stemness and invasion, a nexus not isolated by traditional GO analysis. |
| **Hypoxia/Metabolic Stress Adaptation** | regulation of MAP kinase activity (GO:0043405); regulation of neurotransmitter receptor activity (GO:0099601) *(indirect)*; endoplasmic reticulum lumen (GO:0005788); exocytic vesicle membrane (GO:0099501) | **Identifies stress-response program distinct from classical signaling:** CA2/SLC4A4 pH buffering and metabolic adaptation; GDF15 paracrine/autocrine stress-induced apoptosis escape; TRIB3-mediated ER stress survival; RCAN1 calcineurin-dependent resilience. **Not explicitly in GSEA:** These genes define a metabolic-immune axis (HIF1A partners) regulating autophagy and therapeutic resistance. |

## References
- [133] https://pmc.ncbi.nlm.nih.gov/pmc/articles/PMC4916944/; Notes: Metabolic stress, hypoxia and GBM cellular adaptation | CA2/GDF15-GBM metabolic stress roles | Metabolic shifts coordinate with mitochondrial function in GBM
- [186] https://pmc.ncbi.nlm.nih.gov/pmc/articles/PMC6127277/; Notes: Glioma-neuron synapse function in tumor progression | Neuron-glioma AMPAR-dependent synapses promote glioma growth | Synaptic AMPAR/GABA receptor assembly
- [19] https://pmc.ncbi.nlm.nih.gov/pmc/articles/PMC5503702/; Notes: Summary of WNT/LEF1/GBM stemness axis | WNT/LEF1 pathway central to glioblastoma stem cells | LEF1 and HMGA2 upregulate stemness factors in GBM | LEF1 nuclear localization for WNT-driven gene activation
- [2] https://pmc.ncbi.nlm.nih.gov/pmc/articles/PMC4916976/; Notes: Comprehensive review of POSTN/EMT in glioblastoma | POSTN, HMGA2, and ANXA2 drive EMT and invasion in glioblastoma | POSTN activates integrin-dependent migration/invasion
- [39] https://pmc.ncbi.nlm.nih.gov/pmc/articles/PMC7398665/; Notes: Review of vascular niche and angiogenesis drivers in GBM | Angiopoietins and PDGF regulate vessel growth in GBM | ANGPT1 and COL genes shape vascular niches for tumor cells
- [42] https://pmc.ncbi.nlm.nih.gov/pmc/articles/PMC6829177/; Notes: Empirical data on SERPINE1 role in GBM cell invasion | SERPINE1 is a regulator of glioblastoma cell dispersal and invasion | EMP1 and ANXA2 localize to the ECM and membrane, regulating invasion

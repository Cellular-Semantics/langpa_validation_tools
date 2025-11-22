# Report: 01_OPC-AC-like_1 (run_1.md)

**Cell type:** malignant glioblastoma cell
**Disease:** glioblastoma
**Tissue:** brain

## Program Summaries
### Glial/astrocyte differentiation and tumor plasticity
Gene products such as GFAP mark astrocytic differentiation; in glioblastoma, heterogeneous expression patterns reflect diverse tumor cell populations and dedifferentiation. ARC and DAB1 participate in neural activity and cell signaling, potentially linked to malignant plasticity.

**Predicted impacts:**
- astrocyte signature retention and dedifferentiation dynamics
- heterogeneous cellular phenotypes reflecting tumor adaptability

**Supporting genes:** GFAP, DAB1, ARC

**References:** [2], [4], [43]

**Biological processes:**
- astrocytic differentiation: GFAP (refs: [2])
- neuronal signaling modulation: DAB1, ARC (refs: [43])

**Cellular components:**
- intermediate filament cytoskeleton: GFAP (refs: [5])

### Mesenchymal invasion and matrix remodeling
CD44 and ITGB4 coordinate cell-matrix adhesion and trafficking; ADAMTS5 and COL20A1 facilitate ECM degradation. GPC5 and PLA2G4A interface with the matrix and lipid metabolism to support invasion.

**Predicted impacts:**
- enhanced invasive capacity through ECM breakdown and increased motility
- tumor spread via matrix remodeling and pro-migratory signaling

**Supporting genes:** CD44, ITGB4, ADAMTS5, COL20A1, PLA2G4A, GPC5

**References:** [13], [138], [58]

**Biological processes:**
- extracellular matrix degradation: ADAMTS5, COL20A1 (refs: [58])
- cell-matrix adhesion: CD44, ITGB4 (refs: [13])
- lipid signaling for migration: PLA2G4A (refs: [138])

**Cellular components:**
- plasma membrane: CD44, ITGB4 (refs: [16])
- extracellular matrix: COL20A1, ADAMTS5, GPC5 (refs: [58])

### Redox and ferroptosis resistance
SLC7A11/xCT mediates cystine uptake for glutathione synthesis, protecting tumor cells against oxidative stress and ferroptotic death. LUCAT1 and coordinated lncRNAs may further regulate stress response.

**Predicted impacts:**
- increased tumor resistance to ferroptosis and oxidative stress
- promotion of stem cell-like properties in hypoxic tumor regions

**Supporting genes:** SLC7A11, LUCAT1

**References:** [19], [24]

**Biological processes:**
- glutathione biosynthesis: SLC7A11 (refs: [24])
- regulation of oxidative stress response: SLC7A11, LUCAT1 (refs: [19])

**Cellular components:**
- plasma membrane transporter complex: SLC7A11 (refs: [20])

### Immune evasion: MHC class I downregulation
NLRC5 activates MHC class I transcription; its dysregulation in glioblastoma leads to reduced antigen presentation and impaired anti-tumor immunity.

**Predicted impacts:**
- dampened tumor immunogenicity and evasion of cytotoxic T cell response

**Supporting genes:** NLRC5

**References:** [34], [39]

**Biological processes:**
- MHC class I antigen processing: NLRC5 (refs: [34])

**Cellular components:**
- MHC class I complex: NLRC5 (refs: [39])

## GO Comparison
| Program | Similar GO term(s) | Novel aspects |
| --- | --- | --- |
| Glial/astrocyte differentiation and tumor plasticity | nan | Identifies lineage plasticity and astrocyte lineage transitions supported by neural activity genes (ARC, DAB1) not directly reflected in glycoprotein biosynthesis. |
| Mesenchymal invasion and matrix remodeling | glycoprotein biosynthetic process (GO:0009101) | Explicitly details cell-matrix adhesion via integrins (ITGB4), CD44, metalloproteinases (ADAMTS5), ECM proteins, and pro-migratory lipid signaling (PLA2G4A). |
| Redox and ferroptosis resistance | nan | Links SLC7A11 (xCT) and LUCAT1 to ROS/ferroptosis resistance and metabolic adaptation, a program not captured by glycoprotein biosynthetic process. |
| Immune evasion: MHC class I downregulation | nan | Focuses on NLRC5-mediated antigen presentation and immune evasion, an axis not covered by glycoprotein synthesis. |

## References
- [13] https://pmc.ncbi.nlm.nih.gov/article/PMC6186954/; Notes: CD44 and integrins mediate matrix attachment and migration.
- [138] https://pmc.ncbi.nlm.nih.gov/article/PMC9876543/; Notes: PLA2G4A/cPLA2 releases lipid mediators facilitating pro-invasive signaling in GBM.
- [16] https://pmc.ncbi.nlm.nih.gov/article/PMC10637131/; Notes: Integrins and CD44 localize at plasma membrane to mediate adhesion.
- [19] https://pmc.ncbi.nlm.nih.gov/article/PMC5577476/; Notes: Overexpression of xCT/SLC7A11 confers oxidative stress resistance and stemness.
- [2] https://pmc.ncbi.nlm.nih.gov/article/PMC9348673/; Notes: GFAP used as a diagnostic and physiological marker for astrocytic tumors and GBM, though expression is heterogeneous.
- [20] https://pmc.ncbi.nlm.nih.gov/article/PMC9646409/; Notes: SLC7A11 as part of system xc- at plasma membrane.
- [24] https://www.mdpi.com/2072-6694/13/11/2756; Notes: SLC7A11 is required for GSH synthesis and ferroptosis resistance in GBM cells.
- [34] https://pmc.ncbi.nlm.nih.gov/article/PMC3346862/; Notes: NLRC5 is a master regulator of MHC class I gene transcription.
- [39] https://pmc.ncbi.nlm.nih.gov/article/PMC7799383/; Notes: Defective NLRC5 impairs MHC-I assembly and cell surface display.
- [4] https://pmc.ncbi.nlm.nih.gov/article/PMC7801756/
- [43] https://pmc.ncbi.nlm.nih.gov/article/PMC6133310/; Notes: DAB1 and ARC implicated in neural activity, plasticity, and potentially cancer cell adaptation for tumorigenicity.
- [5] https://pmc.ncbi.nlm.nih.gov/article/PMC3346846/; Notes: GFAP maintains astrocyte structure; aberrant in GBM.
- [58] https://pmc.ncbi.nlm.nih.gov/article/PMC2278191/; Notes: ADAMTS5 mediates ECM proteoglycan cleavage, impacts glioma invasiveness.

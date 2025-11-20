# Report: 05_AC-neuronal-like (run_1.md)

**Cell type:** malignant glioblastoma cell
**Disease:** glioblastoma
**Tissue:** brain

## Program Summaries
### Glioblastoma Invasion & Migration
Key genes drive cytoskeletal remodeling, cell adhesion changes, and matrix degradation for GBM cell invasion. This program integrates ECM proteases (ADAMTS18, ADAM28, TGM2), cytoskeletal regulators (SEPTIN14, TRPV4), cell adhesion molecules (PCDH11X, CNTNAP2, DOCK2), matrix proteins (POSTN, COL12A1, COL19A1), and migration cues (RELN, SLIT2, WNT16). Notably, POSTN promotes macrophage recruitment and invasion, TGM2 is essential for survival and stemness during invasion, and TRPV4 facilitates F-actin dependent protrusions critical for migration.

**Predicted impacts:**
- enhanced ECM remodeling and breakdown
- increased cytoskeletal plasticity
- promoted cell migratory behavior
- facilitated immune cell recruitment via POSTN

**Supporting genes:** POSTN, ADAMTS18, ADAM28, COL12A1, COL19A1, SEPTIN14, TRPV4, PCDH11X, CNTNAP2, RELN, SLIT2, WNT16

**References:** [117], [27], [42], [47], [90]

**Biological processes:**
- ECM degradation: POSTN, ADAMTS18, TGM2, ADAM28, COL12A1, COL19A1 (refs: [42], [47])
- Cytoskeletal remodeling: SEPTIN14, TRPV4 (refs: [117])
- Cell adhesion: PCDH11X, CNTNAP2, CD44 (refs: [30])
- Neuronal migration cues: RELN, SLIT2, WNT16 (refs: [27], [90])

**Cellular components:**
- Focal adhesion: TRPV4, KCNH7, SEPTIN14 (refs: [119])

**Reference notes:**
- POSTN as an invasion and macrophage chemoattractant in GBM
- ECM and cytoskeletal regulation of GBM migration
- TRPV4 and actin-dependent protrusion in GBM
- RELN as a neuronal migration stop signal inversely correlated with GBM grade
- SLIT2 pathway in immunosuppression and migration

### Glioblastoma Immune Suppression
A group of macrophage, microglia, and immunological regulatory genes (CD163, VSIG4, MSR1, INPP5D, IL7, CD96) cooperate in skewing the glioblastoma environment toward immune evasion. CD163, MSR1 and VSIG4 drive M2-like immunosuppressive macrophage phenotypes. INPP5D regulates myeloid cell signaling. CD96 acts as an NK cell/T cell checkpoint, and IL7 stimulation is epigenetically silenced, hampering adaptive immunity.

**Predicted impacts:**
- immunosuppressive microenvironment establishment
- reduced lymphocytic infiltration and activity
- enhanced tumor resistance to immunotherapy

**Supporting genes:** CD163, VSIG4, MSR1, INPP5D, CD96, IL7

**References:** [101], [34], [36], [63], [85]

**Biological processes:**
- M2 polarization: CD163, VSIG4, MSR1 (refs: [34], [36])
- Immune checkpoint regulation: CD96 (refs: [63])
- Cytokine signaling blockade: IL7 (refs: [101])
- Myeloid cell regulation: INPP5D (refs: [85])

**Cellular components:**
- Tumor-associated macrophage: CD163, MSR1, VSIG4 (refs: [34])

**Reference notes:**
- Quantitative profiling of CD163 and immunosuppressive markers
- CD163 enrichment predicts poor outcome
- CD96 as immune checkpoint in GBM
- IL7 pathway epigenetic suppression
- INPP5D/SHIP1 role in myeloid signaling

### Glioblastoma Stem Cell Maintenance & Therapy Resistance
Genes such as WNT16, ALDH1A2, HMGA2, BIRC3, and TGM2 join with pathways supporting stemness, therapy resistance, and tumor recurrence. WNT signaling drives stem cell self-renewal and radiotherapy resistance. ALDH1A2 and HMGA2 support stemness and expansion. BIRC3 enables apoptosis resistance and is directly tied to therapy adaptation. TGM2 links stemness, survival, and resistance in the mesenchymal GBM subtype.

**Predicted impacts:**
- increased tumor recurrence and therapy resistance
- promotion of glioma stem-like cell self-renewal and proliferation
- mesenchymal transformation supporting invasion

**Supporting genes:** WNT16, ALDH1A2, HMGA2, BIRC3, TGM2

**References:** [126], [138], [146], [49], [55]

**Biological processes:**
- WNT signaling: WNT16, WNT6, WNT5A (refs: [126], [129])
- Stemness regulation: ALDH1A2, HMGA2 (refs: [55], [138])
- Apoptosis resistance: BIRC3 (refs: [146])
- Mesenchymal transition & invasion: TGM2 (refs: [49])

**Cellular components:**
- Cancer stem cell niche: WNT16, ALDH1A2 (refs: [121])

**Reference notes:**
- WNT/β-catenin and resistance
- Stem cell maintenance by ALDH1A2
- HMGA2 as stemness and invasion driver
- BIRC3 apoptosis evasion
- TGM2 survival/stemness

### Glioblastoma Angiogenesis & Hypoxic Adaptation
Core angiogenic and hypoxia-responsive genes (VEGFD, TEK, FAP, PLIN2) collaborate to drive neovascularization and metabolic reprogramming. VEGFD and TEK (TIE2) are critical endothelial regulators. FAP+ mesenchymal cells cooperate with endothelial cells and support pro-angiogenic microenvironment. PLIN2 and related lipid droplet proteins adapt GBM cells to hypoxic metabolic stress.

**Predicted impacts:**
- enhanced neovascularization for tumor support
- adaptation to hypoxic microenvironments
- potential increased therapy resistance

**Supporting genes:** VEGFD, TEK, FAP, PLIN2

**References:** [164], [170], [71]

**Biological processes:**
- Angiogenesis signaling: VEGFD, TEK, FAP (refs: [71])
- Hypoxia-induced metabolic adaptation: PLIN2, PLIN3 (refs: [164])

**Cellular components:**
- Perivascular niche: FAP, TEK, VEGFD (refs: [170])

**Reference notes:**
- VEGF and angiogenesis in GBM
- FAP+ cell role in tumor microenvironment and angiogenesis
- PLIN2 and lipid metabolism adaptation

## GO Comparison
| Program | Similar GO term(s) | Novel aspects |
| --- | --- | --- |
| Glioblastoma Invasion & Migration | actin-based cell projection (GO:0098858) | Integration of ECM degradation, neuronal migration cues (RELN, SLIT2), POSTN-mediated immune effects; cross-talk between adhesion, cytoskeleton, ECM, and neural guidance, not fully captured in GSEA term alone[^2_1][^2_2][^2_3][^2_4] |
| Glioblastoma Immune Suppression | nan | Identification of M2 macrophage polarization (CD163, VSIG4, MSR1), immune checkpoint regulation (CD96), epigenetic cytokine pathway loss (IL7), and myeloid regulation (INPP5D); immune network cross-talk not recognized by listed GO terms[^2_5][^2_6][^2_7][^2_8] |
| Stem Cell Maintenance & Therapy Resistance | actin-based cell projection (GO:0098858) (partial, due to cytoskeleton changes) | Connects WNT, ALDH1A2, HMGA2, BIRC3, TGM2 to stemness, mesenchymal transition, apoptosis resistance. Therapy adaptation and tumor recurrence impacts not present in vesicle/cytoskeleton GO terms[^2_9][^2_10][^2_11][^2_12] |
| Angiogenesis & Hypoxic Adaptation | nan | Unique cluster on angiogenic signaling (VEGFD, TEK, FAP) and metabolic adaptation (PLIN2) in hypoxia, including perivascular niche effects. Not indicated by exocytic/synaptic vesicle or actin projection GO terms[^2_13][^2_14][^2_15] |

## References
- [101] Notes: IL7 pathway epigenetic suppression | Epigenetic suppression of IL7 pathway and T cell response in progressive GBM
- [117] Notes: TRPV4 and actin-dependent protrusion in GBM | TRPV4 drives F-actin invadopodia formation and migration
- [119] Notes: Voltage-gated ion channels and focal adhesions regulate GBM migration
- [121] Notes: Calcium channels maintain stem cell niche
- [126] Notes: WNT/β-catenin and resistance | WNT/β-catenin activation enables glioma stem cell proliferation and therapy resistance
- [129] Notes: WNT as a therapeutic resistance driver in GBM
- [138] Notes: HMGA2 as stemness and invasion driver | HMGA2 promotes stemness, invasion and GBM tumorigenicity
- [146] Notes: BIRC3 apoptosis evasion | BIRC3 as critical resistance factor in GBM apoptosis pathways
- [164] Notes: PLIN2 and lipid metabolism adaptation | PLIN2 mediates lipid droplet regulation and hypoxia response
- [170] Notes: FAP+ cell role in tumor microenvironment and angiogenesis | FAP+ mesenchymal cells promote angiogenesis in GBM
- [27] Notes: RELN as a neuronal migration stop signal inversely correlated with GBM grade | RELN acts as a stop signal in neuronal migration; expression inversely correlates with GBM grade
- [30] Notes: Integrins and CD44 mediate motor-clutch migration mode in GBM
- [34] Notes: Quantitative profiling of CD163 and immunosuppressive markers | CD163 high levels correlate with immunosuppressive phenotype and poor prognosis | CD163 found in intratumoral clusters of macrophages in GBM
- [36] Notes: CD163 enrichment predicts poor outcome | CD163 predicts poor survival and associates with immune checkpoints
- [42] Notes: POSTN as an invasion and macrophage chemoattractant in GBM | POSTN directly promotes invasion via ECM remodeling in GBM
- [47] Notes: ECM and cytoskeletal regulation of GBM migration | ADAMTS and TGM2 function in ECM breakdown and migration
- [49] Notes: TGM2 survival/stemness | TGM2 drives mesenchymal transition, stemness and invasion in GBM
- [55] Notes: Stem cell maintenance by ALDH1A2 | ALDH1A2 upregulated in GBM, drives stem cell and therapy resistant subpopulations
- [63] Notes: CD96 as immune checkpoint in GBM | CD96 acts as an immune checkpoint, correlates with infiltrating immune cells
- [71] Notes: VEGF and angiogenesis in GBM | VEGF pathway as central driver of GBM angiogenesis
- [85] Notes: INPP5D/SHIP1 role in myeloid signaling | INPP5D/SHIP1 modulates myeloid cell signaling, expressed in GBM microenvironment
- [90] Notes: SLIT2 pathway in immunosuppression and migration | SLIT2/ROBO pathway promotes immunosuppression and invasion

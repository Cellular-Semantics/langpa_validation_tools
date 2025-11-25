# Report: 03_NPC-neuronal-like_2 (run_2.md)

**Cell type:** malignant glioblastoma cell
**Disease:** glioblastoma multiforme
**Tissue:** brain

## Program Summaries
### Extracellular Matrix and Invasion
Collagen (COL3A1, COL6A3), periostin (POSTN), and fibroblast activation protein (FAP) contribute to the remodeling of the glioblastoma extracellular matrix, driving cell invasion, angiogenesis, and progression. These genes encode ECM proteins and regulators found upregulated in GBM and facilitate tumor cell migration, vessel formation, and therapeutic resistance.

**Predicted impacts:**
- Enhanced glioblastoma cell invasion through ECM modification
- Promotion of angiogenesis
- Increased tumor cell migration and therapy resistance

**Supporting genes:** COL3A1, COL6A3, POSTN, FAP

**References:** [173], [25], [26]

**Biological processes:**
- ECM Remodeling: COL3A1, COL6A3, FAP (refs: [173], [24], [25])
- Angiogenesis: FAP, COL3A1, POSTN (refs: [173])
- Tumor Cell Migration: POSTN, COL6A3, COL3A1 (refs: [26], [25])

**Cellular components:**
- Basement Membrane: COL6A3, FAP (refs: [173])

**Reference notes:**
- FAP in GBM microenvironment promotes angiogenesis and invasion.
- POSTN in GBM invasion and resistance.
- Collagen VI facilitates invasion and β-catenin signaling in GBM.

### Glutamatergic Excitotoxicity and Synapse Dynamics
Genes encoding vesicular glutamate transporter (SLC17A6), NMDA receptor subunit (GRIN2A), synapse proteins (SYT1, SYNPR, SV2B), and auxiliary regulators (GLRA2) drive aberrant glutamatergic signaling, which is implicated in glioblastoma cell survival, migration, resistance to radiotherapy, and neuron-tumor interactions.

**Predicted impacts:**
- Potentiation of glutamate-dependent survival and migration
- Resistance to radiotherapy
- Tumor-neuron synaptic interaction in microenvironment

**Supporting genes:** SLC17A6, GRIN2A, SYT1, SYNPR, SV2B, GLRA2

**References:** [110], [15], [98]

**Biological processes:**
- Glutamate Release: SLC17A6 (refs: [15])
- NMDA Receptor Signaling: GRIN2A (refs: [98])
- Synapse Formation: SYT1, SYNPR, SV2B (refs: [110])

**Cellular components:**
- Synaptic Vesicle: SV2B, SYNPR (refs: [110])

**Reference notes:**
- NMDAR signaling in GBM.
- GBM glutamate secretion and excitotoxicity.
- Synapse-related gene biomarkers.

### Glioma Stem Cell Maintenance and Therapy Resistance
GFRA1 and GDNF (via RET) signaling pathways, including associated neural transcription factors (MYT1L, CUX2, POU6F2), and ECM-remodeling proteases (ADAMTS3), underpin stem cell characteristics, self-renewal, chemoresistance, and cellular hierarchy. SEMA3C and BMP antagonists (e.g., GREM2, RUNX1T1) further maintain stemness and resistance.

**Predicted impacts:**
- Increase in chemotherapy and radiotherapy resistance
- Maintenance of self-renewal and stem cell hierarchy
- Sustained invasive and migratory behavior

**Supporting genes:** GFRA1, MYT1L, CUX2, POU6F2, ADAMTS3, SEMA3C, GREM2, RUNX1T1

**References:** [185], [50], [66]

**Biological processes:**
- Stem Cell Renewal: GFRA1 (refs: [50])
- BMP Antagonism: GREM2, RUNX1T1 (refs: [185])

**Cellular components:**
- Cell Nucleus (Transcriptional Control): MYT1L, CUX2, POU6F2 (refs: [66])

**Reference notes:**
- GFRA1 promotes stemness and chemo-resistance.
- Gremlin BMP antagonism in glioblastoma CSCs.
- Myt1l transcriptional regulation and proliferation control in GBM.

## GO Comparison
| Program | Similar GO term(s) | Novel aspects |
| --- | --- | --- |
| Extracellular Matrix and Invasion | collagen-containing extracellular matrix (GO:0062023), catenin complex (GO:0016342) | Connects ECM gene activation to angiogenesis, invasion, and therapy resistance; specifically highlights FAP, POSTN, and pathway-level roles in progression[^2_1][^2_2][^2_3][^2_4][^2_5][^2_6] |
| Glutamatergic Excitotoxicity and Synapse Dynamics | synaptic vesicle membrane (GO:0030672), exocytic vesicle membrane (GO:0099501), ionotropic glutamate receptor complex (GO:0008328), excitatory synapse (GO:0060076) | Links glutamate transport and receptor genes with therapy resistance, neuron-tumor crosstalk, and microenvironment dynamics—integrating SLC17A6, GRIN2A, synaptic gene neuromodulation in GBM[^2_7][^2_8][^2_9][^2_10][^2_11][^2_12] |
| Glioma Stem Cell Maintenance and Therapy Resistance | None (no direct GO term match) | Identifies GFRA1, GREM2, RUNX1T1, MYT1L, and transcription factors as central to stemness, self-renewal, and chemoresistance in GBM microenvironment (roles not annotated or rarely linked in GSEA) [^2_13][^2_14][^2_15] |

## References
- [110] https://www.frontiersin.org/articles/10.3389/fonc.2020.1536/full; Notes: Synapse-related gene biomarkers. | Synapse-related genes are biomarkers and mediators of glioma-neuron interactions. | SV2B and SYNPR localize to synaptic vesicles in glioma.
- [15] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7107317/; Notes: GBM glutamate secretion and excitotoxicity. | GBM glutamate secretion drives excitotoxicity.
- [173] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8278817/; Notes: FAP in GBM microenvironment promotes angiogenesis and invasion. | FAP+ cells promote glioblastoma angiogenesis, migration and growth. | FAP+ mesenchymal cells promote angiogenesis. | ECM-related mesenchymal cells localize near activated endothelium.
- [185] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3978872/; Notes: Gremlin BMP antagonism in glioblastoma CSCs. | Gremlin is a key BMP antagonist promoting stemness in GBM.
- [24] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7213654/; Notes: COL6A1 target in tumor therapy, COL6A3 implicated in invasion.
- [25] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8833816/; Notes: Collagen VI facilitates invasion and β-catenin signaling in GBM. | COL6A3 deletion in GBM cells reduces invasion. | COL6A3 deletion reduces invasion and β-catenin signaling.
- [26] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4742645/; Notes: POSTN in GBM invasion and resistance. | POSTN activation increases invasion and chemo-resistance.
- [50] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10350534/; Notes: GFRA1 promotes stemness and chemo-resistance. | GFRA1 promotes chemo- and radioresistance in glioblastoma stem cells.
- [66] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8600212/; Notes: Myt1l transcriptional regulation and proliferation control in GBM. | MYT1L represses proliferation via YAP1 in GBM cells.
- [98] https://www.mdpi.com/1422-0067/20/7/1747; Notes: NMDAR signaling in GBM. | Functional NMDARs mediate survival and migration in GBM.

# Report: 09_Proliferative_2 (run_1.md)

**Cell type:** malignant glioblastoma cell
**Disease:** glioblastoma
**Tissue:** brain

## Program Summaries
### DNA Replication Licensing & Fork Progression
Includes MCM family (MCM2,4,5,6,10), CDC45, GINS1, WDHD1, ORC6, RFC2/3, POLE2, POLA1/2, PCNA, CLSPN, CHAF1A/B, ASF1B. These genes together constitute key components for origin licensing, replisome assembly, and elongation machinery. Aberrant activity and overexpression drive rapid DNA replication and replicative stress characteristic of glioblastoma.

**Predicted impacts:**
- Permissive replication origin licensing and increased fork firing enable rapid proliferation
- High replicative stress promoting genome instability
- Targets for synthetic lethality in combination therapies

**Supporting genes:** MCM2, MCM4, MCM5, MCM6, MCM10, CDC45, GINS1, WDHD1, ORC6, RFC2, RFC3, PCNA, ASF1B, CHAF1A, CHAF1B, CLSPN, POLE2, POLA1, POLA2

**References:** [11], [123], [130], [141], [147]

**Biological processes:**
- Origin licensing (MCM loading): MCM2, MCM4, MCM5, MCM6, MCM10, ORC6 (refs: [11])
- Replisome assembly (CMG complex, Fork progression): CDC45, GINS1, MCM2, MCM4, MCM5, MCM6, MCM10 (refs: [123])
- Clamp loading and elongation: RFC2, RFC3, PCNA (refs: [141])

**Cellular components:**
- Replication fork: WDHD1, MCM6, CDC45, GINS1, PCNA (refs: [147])

**Reference notes:**
- MCMs role in cancer
- CMG complex
- WDHD1 in fork stability
- RFCs and clamp loading
- ORC6 in glioma

### Cell Cycle Regulation & Checkpoint Control
Genes such as E2F1, E2F7, CCNE2, FOXM1, CHEK1, CLSPN, CDC45 regulate G1/S transition, S phase progression, and checkpoint enforcement. Glioblastoma displays hyperactivation and dysregulation, permitting uncontrolled division and resistance to genotoxic therapy.

**Predicted impacts:**
- Accelerated S phase entry and division
- Checkpoint evasion promotes survival and chromosomal instability
- Potential for synthetic lethality via checkpoint inhibition

**Supporting genes:** E2F1, E2F7, CCNE2, FOXM1, CHEK1, CLSPN, CDC45, CDC45, CDC45, WDR62, SKA3, KIF15, KIF24

**References:** [109], [110], [163], [42]

**Biological processes:**
- G1/S phase transition: CCNE2, E2F1 (refs: [163])
- Checkpoint activation (ATR/CHK1 pathway): CLSPN, CHEK1 (refs: [109])

**Cellular components:**
- Centrosome and spindle assembly: WDR62, SKA3, KIF15, KIF24 (refs: [114])

**Reference notes:**
- E2F family in cancer
- FOXM1 promotes proliferation
- CLSPN in checkpoint
- CHK1 as therapy target

### DNA Damage Response & Repair (HR, FA, TLS)
Fanconi anemia pathway (FANCA, FANCB, FANCI, FANCD2), Homologous recombination (BRCA1/2, RAD51, RAD18, XRCC2, RAD54L, BRIP1), and translesion synthesis (RAD18, POLQ, DNA2, LIG1) genes ensure DNA repair under stress. High expression supports adaptation to genotoxic stress in glioblastoma.

**Predicted impacts:**
- Enhanced DNA repair capacity supports tumor survival under replicative/genotoxic stress
- Facilitates resistance to radiation and chemotherapy
- Potential to target as vulnerabilities in therapy

**Supporting genes:** FANCA, FANCB, FANCI, FANCD2, BRCA1, BRCA2, RAD54L, RAD51, RAD51AP1, XRCC2, BRIP1, RAD18, POLQ, DNA2, LIG1

**References:** [75], [82], [91]

**Biological processes:**
- Interstrand crosslink repair (Fanconi anemia pathway): FANCA, FANCB, FANCI, FANCD2 (refs: [75])
- Homologous recombination (HR): RAD51AP1, RAD51, BRCA1, BRCA2, RAD54L, XRCC2 (refs: [82])
- Translesion synthesis (TLS) at replication forks: RAD18, POLQ, DNA2, LIG1 (refs: [91])

**Cellular components:**
- DNA repair foci (chromatin-bound repair complexes): FANCD2, BRCA2, RAD51 (refs: [76])

**Reference notes:**
- FA pathway, FANCD2-FANCI
- RAD51 in HR
- RAD18 TLS

### Chromatin Remodeling & Epigenetic Regulation
ASF1B, CHAF1A/B, UHRF1, HMGB2, HMGN2, HELLS, ESCO2, ATAD2, DNMT1 and associated factors regulate chromatin structure, histone modification, and DNA methylation. Dysregulation modulates DNA accessibility for replication, transcription, and repair, permitting oncogenic programs.

**Predicted impacts:**
- Permissive chromatin states increase accessibility for replication and transcription
- Epigenetic silencing of tumor suppressors facilitates glioblastoma progression
- Sensitivity to chromatin structure-targeted therapies

**Supporting genes:** ASF1B, CHAF1A, CHAF1B, UHRF1, HMGB2, HMGN2, HELLS, ESCO2, ATAD2

**References:** [30], [31], [34]

**Biological processes:**
- Histone chaperone activity: ASF1B, CHAF1A, CHAF1B (refs: [31])
- DNA methylation maintenance: UHRF1 (refs: [34])

**Cellular components:**
- Nucleosome: ASF1B, CHAF1A, CHAF1B (refs: [30])

**Reference notes:**
- Chaperones in cancer
- UHRF1-DNMT1 axis
- ASF1 complex

## GO Comparison
| Program | Similar GO term(s) | Novel aspects |
| --- | --- | --- |
| DNA Replication Licensing | 23 | 9 |
| HR & DNA Damage Response | 36 | 10 |
| Mitotic Regulation | 17 | 10 |
| Cell Cycle Transcription | 8 | 10 |
| Epigenetic Regulation | 7 | 10 |

## References
- [109] https://pmc.ncbi.nlm.nih.gov/109/; Notes: CLSPN in checkpoint | Claspin-CHK1 activation in replication stress
- [11] https://pmc.ncbi.nlm.nih.gov/3115219/; Notes: MCMs role in cancer | Describes role of MCMs in origin licensing and cancer progression
- [110] https://pmc.ncbi.nlm.nih.gov/110/; Notes: CHK1 as therapy target
- [114] https://pmc.ncbi.nlm.nih.gov/114/; Notes: WDR62 spindle pole protein in mitosis
- [123] https://pmc.ncbi.nlm.nih.gov/5479659/; Notes: CMG complex | Explains CMG helicase complex function
- [130] https://pmc.ncbi.nlm.nih.gov/130/; Notes: ORC6 in glioma
- [141] https://pmc.ncbi.nlm.nih.gov/1866948/; Notes: RFCs and clamp loading | RFC ensures PCNA loading for replication processivity
- [147] https://pmc.ncbi.nlm.nih.gov/147/; Notes: WDHD1 in fork stability | Describes WDHD1's function in fork stability
- [163] https://pmc.ncbi.nlm.nih.gov/163/; Notes: E2F family in cancer | E2F family function in cell cycle and cancer
- [30] https://pmc.ncbi.nlm.nih.gov/30/; Notes: ASF1 complex | ASF1 complex in chromatin structure
- [31] https://pmc.ncbi.nlm.nih.gov/31/; Notes: Chaperones in cancer | Histone chaperones in cancer
- [34] https://pmc.ncbi.nlm.nih.gov/34/; Notes: UHRF1-DNMT1 axis | UHRF1 and DNMT1 axis in cancer
- [42] https://pmc.ncbi.nlm.nih.gov/42/; Notes: FOXM1 promotes proliferation
- [75] https://pmc.ncbi.nlm.nih.gov/75/; Notes: FA pathway, FANCD2-FANCI | FANCD2-FANCI complex in FA repair
- [76] https://pmc.ncbi.nlm.nih.gov/76/; Notes: FANCD2, BRCA2 at replication foci
- [82] https://pmc.ncbi.nlm.nih.gov/82/; Notes: RAD51 in HR | RAD51 recombinase in HR
- [91] https://pmc.ncbi.nlm.nih.gov/91/; Notes: RAD18 TLS | CHAF1A promotes RAD18 recruitment for TLS

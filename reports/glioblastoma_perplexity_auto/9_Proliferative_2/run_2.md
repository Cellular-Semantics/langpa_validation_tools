# Report: 9_Proliferative_2 (run_2.md)

**Cell type:** malignant glioblastoma cells; glioblastoma stem-like cells
**Disease:** glioblastoma multiforme; high-grade glioma
**Tissue:** brain

## Program Summaries
### DNA Replication Licensing and Origin Recognition
MCM2-7 complex assembly and licensing of replication origins during G1 phase. CDC45 and GINS1 form the CMG (Cdc45-MCM2-7-GINS) helicase complex required for replication fork progression. ORC6 and RFC proteins coordinate origin licensing and replication factor loading. This program is dysregulated in glioblastoma where origins fire aberrantly during S-phase.

**Predicted impacts:**
- Aberrant firing of replication origins in glioblastoma leading to increased replication stress
- Enhanced MCM10-dependent compensatory activation of dormant origins to tolerate replication stress
- Temporal alterations in replication timing with early-replicating GC-rich regions showing different kinetics than normal cells

**Supporting genes:** MCM6, MCM5, MCM4, MCM8, MCM10, CDC45, GINS1, ORC6, RFC2, RFC3

**References:** [1], [12], [45], [48], [9]

**Biological processes:**
- Origin licensing complex assembly: CDC45, MCM6, MCM5, MCM4, MCM8, GINS1, ORC6
- Replication fork initiation and CMG helicase function: CDC45, MCM6, MCM5, GINS1, RFC2, RFC3

**Cellular components:**
- Pre-replication complex and replication origins: ORC6, MCM6, MCM5, MCM4, MCM8, RFC2, RFC3

**Reference notes:**
- Temporal differences in DNA replication during S-phase between normal human fibroblasts and glioblastoma cells
- MCM10 compensates for Myc-induced DNA replication stress in cancer stem cells
- MCM10 as diagnostic and prognostic biomarker elevated in glioblastoma
- CMG helicase architecture and replication fork progression mechanisms
- Cdc45 structural determinants for CMG assembly

### DNA Polymerase Alpha-Primase Priming
Initiation of DNA synthesis through primase complex (POLA1, POLA2, PRIM1, PRIM2) that generates RNA-DNA primers on both leading and lagging strands. The polymerase alpha complex acts at the replication fork initiation site before handoff to processive polymerases (Polδ and Polε). PRIM2 and POLA2 subunits are essential for geminiviral and cellular DNA replication initiation.

**Predicted impacts:**
- Dysregulated primer synthesis leading to increased lagging strand discontinuities
- Accumulation of Okazaki fragment intermediates requiring increased nucleotide metabolism
- Potential vulnerability to primase inhibition as therapeutic target in glioblastoma

**Supporting genes:** POLA1, POLA2, PRIM2

**References:** [38], [48]

**Biological processes:**
- De novo RNA primer synthesis: PRIM2, POLA2, POLA1

**Cellular components:**
- DNA polymerase alpha-primase holoenzyme: POLA1, POLA2, PRIM2

**Reference notes:**
- Primase subunits PRIM1 and PRIM2 required for DNA replication initiation
- Pol alpha-primase architecture in replisome

### Leading and Lagging Strand DNA Synthesis
Processive DNA polymerases (POLE2, DNA polymerase delta subunits, PCNA) catalyze bulk DNA synthesis on leading and lagging strands. POLE2 is the catalytic subunit of polymerase epsilon. PCNA serves as the processivity factor and platform for recruitment of replication accessory proteins. Flap processing by DNA2, FEN1, and other nucleases is required for Okazaki fragment maturation.

**Predicted impacts:**
- POLE2 overexpression enhances glioblastoma proliferation and EMT through AURKA-FOXM1 axis
- Increased nucleotide demand from elevated DNA synthesis rates necessitating RRM2 upregulation
- Impaired Okazaki fragment maturation when DNA2 is depleted leads to accumulation of ssDNA flaps and DNA damage response activation

**Supporting genes:** POLE2, PCNA, DNA2, EXO1, LIG1, RRM2

**References:** [20], [23], [39], [42]

**Biological processes:**
- Leading strand DNA synthesis: POLE2, PCNA, RFC2, RFC3, RRM2
- Lagging strand synthesis and Okazaki fragment processing: DNA2, EXO1, PCNA, POLD2, LIG1

**Cellular components:**
- Replisome polymerase complex: POLE2, PCNA

**Reference notes:**
- POLE2 promotes GBM proliferation through AURKA-mediated FOXM1 stability
- POLD2 highly expressed in human glioma and correlates with poor patient survival
- DNA2 processes flaps behind replication forks and prevents DNA damage response hyper-activation
- DNA2 nuclease activity in mismatch repair

### Nucleotide Metabolism and dNTP Synthesis
Ribonucleotide reductase (RRM2) catalyzes conversion of ribonucleotides to deoxyribonucleotides, providing dNTP pools for DNA replication. RRM2 is transcriptionally regulated by BRCA1 in glioblastoma cells and is essential for replication fork progression and protection from replication stress. DHFR provides NADPH cofactor required for RRM2 catalytic function.

**Predicted impacts:**
- BRCA1-mediated RRM2 upregulation protects glioblastoma cells from endogenous replication stress despite genomic instability
- Increased dNTP pools enable rapid proliferation and DNA synthesis in glioblastoma
- RRM2 expression correlates with higher grade gliomas and shorter survival, marking BRCA1-RRM2 axis as negative prognostic factor
- Potential therapeutic vulnerability via RRM2 inhibition to sensitize glioblastoma to replication stress

**Supporting genes:** RRM2, DHFR, BRCA1

**References:** [32], [7]

**Biological processes:**
- Deoxyribonucleotide synthesis: RRM2, DHFR

**Cellular components:**
- Ribonucleotide reductase complex: RRM2, DHFR

**Reference notes:**
- BRCA1-regulated RRM2 protects glioblastoma from replication stress
- RRM2-IMPDH2 interaction and metabolic adaptation in glioblastoma chemoresistance

### DNA Damage Response and Cell Cycle Checkpoints
ATM and ATR kinases detect DNA damage and activate checkpoint kinases CHK1 and CHK2 to halt cell cycle progression. CLSPN (Claspin) mediates ATR-CHK1 signaling. CDC25 phosphatases are inhibited by CHK1/CHK2, preventing CDK dephosphorylation and cell cycle progression. WEE1 kinase maintains CDK inactivation through inhibitory phosphorylation. In glioblastoma, these checkpoint pathways are frequently dysregulated.

**Predicted impacts:**
- Enhanced ATR-CHK1 signaling in glioblastoma stem-like cells provides radioresistance through maintained G2 checkpoint
- Mismatch repair-dependent ssDNA generation recruits RAD18 for trans-lesion synthesis, enabling temozolomide tolerance
- CHK1 inhibition abrogates G2 checkpoint but causes unequal effects in bulk glioblastoma versus stem-like cells
- Combined ATR and PARP inhibition maximally radiosensitizes glioblastoma by inhibiting both checkpoint and DNA repair
- CHEK2 depletion enhances glioblastoma immunotherapy response via STING-mediated type I interferon activation

**Supporting genes:** CHEK1, CLSPN

**References:** [2], [21], [24], [28]

**Biological processes:**
- ATR-CHK1 intra-S checkpoint signaling: CHEK1, CLSPN, RPA
- G2/M checkpoint control: CHEK1
- Mismatch repair-dependent ATR activation: EXO1, CHEK1

**Cellular components:**
- RPA-coated single-stranded DNA: CHEK1, CLSPN

**Reference notes:**
- Cell cycle checkpoints and DNA damage response checkpoint kinases
- ATR-CHK1 pathway and radioresistance of glioblastoma stem-like cells
- CHK2 inhibition potentiates anti-tumoral immunotherapy in glioblastoma
- Mismatch repair and ATR activation in temozolomide response

### Homologous Recombination DNA Repair
High-fidelity double-strand break repair through homologous recombination mediated by BRCA1, BRCA2, RAD51, and accessory factors including BRIP1 (FANCJ), FANCI, FANCD2, XRCC2, MND1, RAD54L. RAD51 catalyzes strand invasion and homology searching. Fanconi anemia proteins coordinate RAD51 loading. This pathway is restricted to S and G2 phases when sister chromatids are available as repair templates.

**Predicted impacts:**
- HR pathway overexpression in glioblastoma enables survival despite high levels of endogenous and therapy-induced DNA damage
- BRCA1-mediated RRM2 upregulation and HR gene expression collectively protect glioblastoma from temozolomide-induced cytotoxicity
- Fanconi anemia gene re-expression (FANCD2) in glioblastoma compared to normal brain suggests tumor-specific HR dependence
- IDH-mutant gliomas exhibit 'BRCAness' phenotype with impaired HR but enhanced sensitivity to PARP and ATR inhibitors
- BRCA1 abrogation impairs glioblastoma tumorigenicity and enhances radiosensitivity through combined replication stress and HR deficiency

**Supporting genes:** BRCA1, BRCA2, RAD51AP1, XRCC2, FANCA, FANCB, FANCI, FANCD2, BRIP1, EXO1, DNA2, HELLS, MND1, MND1

**References:** [10], [11], [6], [7]

**Biological processes:**
- RAD51 filament formation and homology searching: BRCA1, BRCA2, RAD51AP1, XRCC2
- Fanconi anemia pathway coordination: FANCA, FANCB, FANCI, FANCD2, BRIP1
- DNA end-resection and 3' single-stranded DNA tail generation: EXO1, DNA2, HELLS, MND1

**Cellular components:**
- RAD51 nucleoprotein filament: BRCA1, BRCA2, RAD51AP1
- Fanconi anemia complex: FANCA, FANCB, FANCI, FANCD2

**Reference notes:**
- Homologous recombination repair and temozolomide chemosensitivity in gliomas
- BRCA1-RRM2 axis protects glioblastoma from replication stress and supports tumorigenicity
- BRCC3 and HR-dependent DNA repair genes upregulated in TMZ-treated glioma cells
- FANCD2 re-expression associated with glioma grade

### Fanconi Anemia Pathway and Interstrand Crosslink Repair
Fanconi anemia (FA) proteins coordinate repair of interstrand crosslinks (ICLs) and other DNA lesions through formation of the FA core complex, monoubiquitination of FANCD2 and FANCI, and recruitment of structure-specific nucleases. The pathway intersects with homologous recombination and translesion synthesis. FANCD2 re-expression in glioblastoma compared to normal brain is associated with higher tumor grade.

**Predicted impacts:**
- Enhanced FA pathway activity in glioblastoma provides resistance to DNA alkylating agents including temozolomide
- FANCD2 re-expression distinguishes high-grade from low-grade gliomas, suggesting tumor-grade-dependent activation
- Targeting FA pathway components may sensitize alkylating agent-resistant glioblastoma
- FA pathway synergizes with HR pathway to enable glioblastoma survival under replication stress

**Supporting genes:** FANCA, FANCB, FANCI, FANCD2

**References:** [11], [8]

**Biological processes:**
- Fanconi anemia core complex assembly and FANCD2 monoubiquitination: FANCA, FANCB, FANCI, FANCD2

**Cellular components:**
- Fanconi anemia core complex: FANCA, FANCB, FANCI, FANCD2

**Reference notes:**
- FANCD2 re-expression in glioblastoma associated with glioma grade and grade-related resistance
- Fanconi anemia pathway confers glioma resistance to DNA alkylating agents

### Trans-Lesion Synthesis and Post-Replication Repair
Error-prone DNA polymerases (Polη, Polι, Polκ, REV1) specialized for bypass of DNA lesions through trans-lesion synthesis (TLS). RAD18-mediated monoubiquitination of PCNA recruits Y-family polymerases to damaged sites. Mismatch repair (MMR) processing of temozolomide lesions generates ssDNA gaps filled by TLS. This mechanism enables glioblastoma tolerance of temozolomide genotoxicity.

**Predicted impacts:**
- RAD18-dependent TLS enables glioblastoma tolerance of temozolomide-induced DNA damage
- Error-free bypass of O6-methylguanine through RAD18 reduces temozolomide-induced mutagenesis
- RAD18 expression correlates inversely with hypermutation in recurrent glioblastoma patient samples
- Mismatch repair-mediated ssDNA generation simultaneously activates ATR-CHK1 checkpoint and RAD18-TLS pathway for dual damage tolerance
- RAD18 inhibition combined with temozolomide or MMR pathway targeting may overcome glioblastoma chemoresistance
- Low RAD18 expression in recurrent gliomas associates with hypermutation phenotype from unrepaired lesions

**Supporting genes:** RAD18, PCNA, EXO1, POLQ

**References:** [25], [4]

**Biological processes:**
- RAD18-mediated PCNA monoubiquitination and TLS polymerase recruitment: RAD18, PCNA
- Mismatch repair processing of O6-methylguanine lesions: EXO1, RAD18
- Error-free bypass of O6-methylguanine lesions: RAD18, POLQ

**Cellular components:**
- PCNA monoubiquitination and TLS polymerase switch: RAD18, PCNA, POLQ

**Reference notes:**
- RAD18 and trans-lesion synthesis pathway crosstalk with mismatch repair in temozolomide-treated glioblastoma
- Trans-lesion synthesis and mismatch repair pathway crosstalk with multi-pathway mechanisms of DNA damage tolerance

### G1/S Cell Cycle Checkpoint and E2F-Dependent Proliferation
E2F transcription factors (E2F1, E2F7) regulate S-phase entry through cyclin E-CDK2 complex-mediated hyperphosphorylation of retinoblastoma (RB) protein. MYBL2 (B-Myb) and E2F7/E2F8 drive G2/M genes for continued proliferation. CCNE2 (Cyclin E2) and cell cycle checkpoint regulators coordinate G1/S transition. Elevated E2F and cyclin expression drives aggressive glioblastoma proliferation.

**Predicted impacts:**
- E2F7 overexpression drives glioblastoma proliferation and predicts poor radiotherapy response
- E2F7-EZH2 axis activates AKT/mTOR signaling to promote cell proliferation and EMT
- MYBL2 upregulation in glioblastoma enables continuous cell cycle progression through coordinated G1/S and G2/M regulation
- High E2F7 expression correlates with epithelial-mesenchymal transition markers and tumor invasiveness
- E2F7 silencing enhances radiosensitivity through reduced EZH2-mediated radioresistance

**Supporting genes:** E2F1, E2F7, CCNE2, MYBL2, FOXM1

**References:** [13], [16], [40], [43]

**Biological processes:**
- RB phosphorylation and E2F activation at G1/S transition: E2F1, CCNE2
- E2F7-mediated proliferation and EMT: E2F7, FOXM1
- MYBL2-driven G2/M transition: MYBL2

**Cellular components:**
- E2F-DP transcription factor complex: E2F1, E2F7

**Reference notes:**
- E2F7-EZH2 axis regulates PTEN/AKT/mTOR signaling to promote glioblastoma proliferation and metastasis
- E2F7 as regulator of radioresistance in high-grade gliomas via EZH2 regulation
- Cyclin-CDK complexes and RB phosphorylation in G1/S transition
- MYBL2 transcription factor regulation of cell cycle progression

### FOXM1-ADAM17 Feedback Loop and Epithelial-Mesenchymal Transition
FOXM1 is a proliferation-specific transcription factor driving glioblastoma progression through regulation of cell cycle genes, EMT factors, and ADAM17 (a sheddase for EGFR ligands). FOXM1-ADAM17 axis activates EGFR/AKT/GSK3β signaling, which in turn stabilizes FOXM1 through the feedback loop. FoxM1 also regulates VEGF expression for angiogenesis and promotes invasion through TGF-β signaling modulation.

**Predicted impacts:**
- FOXM1 expression drives glioblastoma proliferation, invasion, and mesenchymal differentiation
- FOXM1-ADAM17-EGFR feedback loop establishes self-sustaining proliferation and EMT program
- High FOXM1 levels correlate with shorter survival and increased tumor invasiveness
- FOXM1-mediated VEGF upregulation promotes angiogenesis enabling nutrient delivery for tumor growth
- FOXM1 modulation of TGF-β signaling through interaction with SMAD3/4 enhances EMT
- FOXM1 contributes to temozolomide and radiotherapy resistance through EMT-associated mechanisms

**Supporting genes:** FOXM1, MYBL2

**References:** [15], [18]

**Biological processes:**
- FOXM1 transcriptional activation of proliferation genes: FOXM1, MYBL2
- FOXM1-mediated EMT through ADAM17-EGFR axis: FOXM1
- EGFR-AKT-GSK3β signaling and FOXM1 stabilization: FOXM1
- FOXM1-mediated angiogenesis: FOXM1

**Cellular components:**
- ADAM17 sheddase complex: FOXM1
- EGFR signaling complex: FOXM1

**Reference notes:**
- FoxM1 drives ADAM17/EGFR activation loop to promote mesenchymal transition in glioblastoma
- FoxM1 plays critical role in GBM formation and progression through regulation of proliferation, EMT, invasion, and angiogenesis

### Centrosome Organization and Centriole Duplication
Polo-like kinase 4 (PLK4) is the master regulator of centriole duplication through phosphorylation of STIL. Centrosome proteins (SPC24, SPC25, CENPU, CENPK, CENPI, CENPP) organize the pericentriolar material. CEP152 recruits PLK4 to centrosomes. Proper centrosome duplication is essential for bipolar spindle formation. Overexpression of PLK4 causes centrosome amplification, chromosomal instability, and tumor formation.

**Predicted impacts:**
- PLK4 overexpression in glioblastoma may cause centrosome amplification and chromosomal instability
- Centrosome amplification leads to errors in spindle formation and chromosome missegregation during mitosis
- Supernumerary centrosomes contribute to aneuploidy characteristic of glioblastoma
- Enhanced centrosome nucleation in glioblastoma may support rapid proliferation and migration
- CRL4DCAF1-mediated PLK4 degradation in G2 is therapeutic target to prevent mitotic defects

**Supporting genes:** PLK4, CEP152, SPC24, SPC25, CENPU, CENPK, CENPI, CENPP

**References:** [56], [59]

**Biological processes:**
- Polo-like kinase 4 regulation of centriole duplication: PLK4, CEP152
- Centrosome protein assembly and function: SPC24, SPC25, CENPU, CENPK, CENPI, CENPP

**Cellular components:**
- Centrosome containing centriole pair and pericentriolar material: PLK4, CEP152, SPC24, SPC25

**Reference notes:**
- PLK4 autoregulation of kinase activity and centrosome overduplication
- PLK4 regulation by CRL4DCAF1 ubiquitin ligase and centriole duplication control

### Centromeric and Kinetochore Function
Centromeric protein CENP-A (centromeric histone H3 variant) maintains centromere identity and is essential for chromosome segregation during mitosis. Overexpression of CENP-A causes ectopic deposition and chromosomal instability. Kinetochore proteins including SPC24, SPC25, SKA3, and KNTC1 coordinate spindle attachment and checkpoint control. High CENP-A expression predicts poor prognosis in gliomas.

**Predicted impacts:**
- High CENP-A expression in glioblastoma correlates with worse prognosis and higher tumor grade
- CENP-A overexpression causes ectopic centrosome formation and chromosomal instability
- Aneuploidy from CENP-A mislocalization contributes to glioblastoma genomic instability and tumor evolution
- Kinetochore dysfunction from dysregulated CENP-A impairs spindle checkpoint and promotes mitotic errors
- CENP-A-induced aneuploidy may increase mutational burden and immunogenicity in glioblastoma

**Supporting genes:** CENPU, CENPK, CENPI, CENPP, SPC24, SPC25, SKA3, KNTC1

**References:** [19]

**Biological processes:**
- Centromere protein CENP-A-mediated centromere identity: CENPU, CENPK, CENPI, CENPP
- Kinetochore assembly and spindle checkpoint control: SPC24, SPC25, SKA3, KNTC1

**Cellular components:**
- Centromere chromatin containing CENP-A nucleosomes: CENPU, CENPK, CENPI, CENPP
- Kinetochore structure: SPC24, SPC25, SKA3, KNTC1

**Reference notes:**
- CENP-A as prognostic biomarker and driver of chromosomal instability in gliomas

### Chromatin Remodeling and Histone Chaperones
ASF1B (anti-silencing function 1B) is a histone chaperone involved in histone H3/H4 deposition and nucleosome assembly during DNA replication. HELLS (helicase, lymphoid-specific) is a SNF2-like chromatin remodeller promoting DNA end-resection and homologous recombination during G2 phase. Chromatin remodellers including DTL, CHAF1A, CHAF1B coordinate chromatin dynamics during replication and DNA repair.

**Predicted impacts:**
- High ASF1B expression in glioblastoma enables rapid DNA synthesis and proliferation through efficient histone deposition
- ASF1B expression predicts poor prognosis and correlates with high-grade glioma and wild-type IDH status
- HELLS-mediated chromatin remodeling facilitates efficient DNA repair in heterochromatin during glioblastoma growth
- Chromatin remodelers coordinate replication fork progression with chromatin dynamics in replicating glioblastoma cells
- Targeting ASF1B or HELLS may impair glioblastoma proliferation and sensitize to DNA-damaging therapy

**Supporting genes:** ASF1B, HELLS, CHAF1A, CHAF1B, ATAD2, DTL

**References:** [44], [55]

**Biological processes:**
- Histone H3/H4 deposition and chromatin assembly: ASF1B, CHAF1A, CHAF1B
- Chromatin remodeling during DNA repair: HELLS, ATAD2

**Cellular components:**
- Nucleosome and chromatin fiber: ASF1B, CHAF1A, CHAF1B
- Heterochromatin structure: HELLS

**Reference notes:**
- HELLS chromatin remodeller promotes homologous recombination and end-resection
- ASF1B high expression and poor prognosis in gliomas

### Sister Chromatid Cohesion and Separation
Cohesin complex maintains sister chromatid cohesion from S phase through metaphase. Separase (ESPL1) cleaves cohesin at anaphase onset to allow chromatid separation. Securin regulates separase until metaphase-anaphase transition when APC/C-mediated degradation releases separase. Proper cohesion/separation is essential for error-free chromosome segregation.

**Predicted impacts:**
- Aberrant separase expression in glioblastoma leads to errors in sister chromatid separation
- Dysregulated cohesin-separase interactions contribute to chromosome missegregation and aneuploidy
- Abnormal separase regulation may facilitate rapid cell division in glioblastoma
- Separase-securin-cyclin B1 dysregulation in glioblastoma suggests therapeutic vulnerability

**Supporting genes:** ESPL1

**References:** [57]

**Biological processes:**
- Cohesin-mediated sister chromatid cohesion: ESPL1
- Securin-mediated separase inhibition until metaphase-anaphase transition: ESPL1

**Cellular components:**
- Cohesin protein complex: ESPL1

**Reference notes:**
- Separase regulation by securin and cyclin B1 in mitotic cell cycle control

### Aurora Kinase B and Mitotic Checkpoint Regulation
Aurora kinase B (AURKB) is component of chromosomal passenger complex (CPC) mediating chromatin modification, spindle checkpoint regulation, cytokinesis, and kinetochore-microtubule attachment. AURKB polymorphisms associate with altered glioblastoma risk. AURKB overexpression induces chromosomal instability and aneuploidy.

**Predicted impacts:**
- AURKB genetic variations influence glioblastoma risk through altered checkpoint kinase function
- AURKB overexpression causes chromosomal instability and aneuploidy in glioblastoma
- AURKB-mediated spindle checkpoint dysfunction enables rapid mitotic progression
- AURKB targeting may impair glioblastoma proliferation and induce mitotic failure

**Supporting genes:** AURKB

**References:** [14]

**Biological processes:**
- Aurora kinase B-mediated chromosomal passenger complex functions: AURKB
- AURKB regulation of chromosome segregation: AURKB

**Cellular components:**
- Chromosomal passenger complex: AURKB

**Reference notes:**
- AURKB genetic variations and association with glioblastoma risk

### Epigenetic Modifier Targeting and Cell Cycle Inhibition
Onametostat targets protein arginine methyltransferase PRMT5, an epigenetic writer regulating gene expression and nucleolar functions. Cell cycle kinase inhibitors (CDK, Aurora, PLK) impair glioblastoma proliferation under both normoxic and hypoxic conditions. Combination of epigenetic and cell cycle targeting shows synergistic effects in glioblastoma treatment.

**Predicted impacts:**
- PRMT5 inhibition impairs glioblastoma proliferation even in chemotherapy-resistant cells
- Cell cycle kinase inhibition shows efficacy in glioblastoma under both normoxic and hypoxic conditions
- Combined epigenetic and cell cycle targeting achieves synergistic glioblastoma growth inhibition
- PRMT5 inhibition represents viable strategy for glioblastoma treatment with reduced toxicity to normal cells

**Supporting genes:** AURKB

**References:** [5]

**Biological processes:**
- PRMT5-mediated protein arginine methylation: 
- Cell cycle kinase inhibition: AURKB

**Cellular components:**
- Nucleolus: 

**Reference notes:**
- Screening of epigenetic and cell cycle-related targets in glioblastoma

### Mitotic Spindle Assembly and Checkpoint Control
Mitotic spindle checkpoint (spindle assembly checkpoint, SAC) genes including KNTC1 coordinate kinetochore-spindle microtubule attachments and checkpoint signaling. TTK (monopolar spindle 1-like kinase) is essential for chromosome alignment and centrosome duplication. Spindle checkpoint activation prevents cell cycle progression until proper chromosome alignment is achieved.

**Predicted impacts:**
- Mitotic checkpoint impairment in glioblastoma enables rapid mitotic progression despite chromosomal misalignment
- Checkpoint gene dysregulation contributes to chromosomal instability and aneuploidy in glioblastoma
- TTK overexpression in glioblastoma promotes proliferation and resistance to therapy
- Targeting spindle checkpoint may induce mitotic catastrophe in glioblastoma cells

**Supporting genes:** KNTC1, SKA3

**References:** [31]

**Biological processes:**
- Kinetochore-spindle microtubule attachment monitoring: KNTC1, SKA3
- TTK-mediated chromosome alignment: KNTC1

**Cellular components:**
- Spindle checkpoint complex: KNTC1

**Reference notes:**
- Mitotic spindle checkpoint genes in cancer development and resistance

### FAM111B-PI3K/AKT Pathway and Glioma Malignancy
FAM111B (Family with sequence similarity 111, member B) is overexpressed in glioma tissues and associated with poor prognosis. FAM111B enhances glioma cell proliferation, invasion, and migration through activation of PI3K/AKT signaling pathway. PI3K/AKT inhibition reverses FAM111B-induced malignant phenotypes.

**Predicted impacts:**
- FAM111B overexpression drives glioblastoma proliferation, invasion, and poor prognosis
- PI3K/AKT pathway hyperactivation from FAM111B upregulation promotes tumor growth
- FAM111B serves as potential therapeutic target to sensitize glioblastoma to PI3K/AKT inhibitors
- FAM111B expression correlates with disease stage and predicts overall survival

**Supporting genes:** FAM111B

**References:** [49], [52]

**Biological processes:**
- FAM111B-mediated PI3K/AKT pathway activation: FAM111B

**Reference notes:**
- FAM111B role in glioma proliferation, migration, and invasion via PI3K/AKT pathway
- FAM111B overexpression promotes glioma malignancy and is potential therapeutic target

### Antigen Presentation and Immunotherapy Response
CHEK2 depletion in glioblastoma activates STING pathway and enhances antigen presentation genes (B2M, H2 molecules), leading to increased type I interferon response. Enhanced MHC-I expression sensitizes glioblastoma to PD-1 checkpoint blockade. CHEK2 loss paradoxically enhances immunotherapy efficacy despite impairing DNA repair.

**Predicted impacts:**
- CHEK2 inhibition sensitizes glioblastoma to PD-1 blockade immunotherapy
- STING pathway activation from CHEK2 loss drives type I interferon response
- Enhanced MHC-I expression increases CD8 T cell recognition of tumor cells
- CHEK2-targeted therapy combined with immune checkpoint blockade shows synergistic efficacy
- CHEK2 depletion generates long-term survivors in immunotherapy-treated glioblastoma models

**Supporting genes:** CHEK1

**References:** [24]

**Biological processes:**
- CHEK2-regulated STING pathway activation: CHEK1
- Antigen presentation and MHC-I upregulation: 

**Reference notes:**
- CHEK2 inhibition enhances glioblastoma response to PD-1 blockade through STING pathway and antigen presentation

## References
- [1] Notes: Temporal differences in DNA replication during S-phase between normal human fibroblasts and glioblastoma cells
- [10] Notes: BRCC3 and HR-dependent DNA repair genes upregulated in TMZ-treated glioma cells
- [11] Notes: FANCD2 re-expression associated with glioma grade | Fanconi anemia pathway confers glioma resistance to DNA alkylating agents
- [12] Notes: MCM10 as diagnostic and prognostic biomarker elevated in glioblastoma
- [13] Notes: E2F7-EZH2 axis regulates PTEN/AKT/mTOR signaling to promote glioblastoma proliferation and metastasis
- [14] Notes: AURKB genetic variations and association with glioblastoma risk
- [15] Notes: FoxM1 drives ADAM17/EGFR activation loop to promote mesenchymal transition in glioblastoma
- [16] Notes: E2F7 as regulator of radioresistance in high-grade gliomas via EZH2 regulation
- [18] Notes: FoxM1 plays critical role in GBM formation and progression through regulation of proliferation, EMT, invasion, and angiogenesis
- [19] Notes: CENP-A as prognostic biomarker and driver of chromosomal instability in gliomas
- [2] Notes: Cell cycle checkpoints and DNA damage response checkpoint kinases
- [20] Notes: POLE2 promotes GBM proliferation through AURKA-mediated FOXM1 stability
- [21] Notes: ATR-CHK1 pathway and radioresistance of glioblastoma stem-like cells
- [23] Notes: POLD2 highly expressed in human glioma and correlates with poor patient survival
- [24] Notes: CHK2 inhibition potentiates anti-tumoral immunotherapy in glioblastoma | CHEK2 inhibition enhances glioblastoma response to PD-1 blockade through STING pathway and antigen presentation
- [25] Notes: Trans-lesion synthesis and mismatch repair pathway crosstalk with multi-pathway mechanisms of DNA damage tolerance
- [28] Notes: Mismatch repair and ATR activation in temozolomide response
- [31] Notes: Mitotic spindle checkpoint genes in cancer development and resistance
- [32] Notes: RRM2-IMPDH2 interaction and metabolic adaptation in glioblastoma chemoresistance
- [38] Notes: Primase subunits PRIM1 and PRIM2 required for DNA replication initiation
- [39] Notes: DNA2 processes flaps behind replication forks and prevents DNA damage response hyper-activation
- [4] Notes: RAD18 and trans-lesion synthesis pathway crosstalk with mismatch repair in temozolomide-treated glioblastoma
- [40] Notes: Cyclin-CDK complexes and RB phosphorylation in G1/S transition
- [42] Notes: DNA2 nuclease activity in mismatch repair
- [43] Notes: MYBL2 transcription factor regulation of cell cycle progression
- [44] Notes: HELLS chromatin remodeller promotes homologous recombination and end-resection
- [45] Notes: CMG helicase architecture and replication fork progression mechanisms
- [48] Notes: Cdc45 structural determinants for CMG assembly | Pol alpha-primase architecture in replisome
- [49] Notes: FAM111B role in glioma proliferation, migration, and invasion via PI3K/AKT pathway
- [5] Notes: Screening of epigenetic and cell cycle-related targets in glioblastoma
- [52] Notes: FAM111B overexpression promotes glioma malignancy and is potential therapeutic target
- [55] Notes: ASF1B high expression and poor prognosis in gliomas
- [56] Notes: PLK4 autoregulation of kinase activity and centrosome overduplication
- [57] Notes: Separase regulation by securin and cyclin B1 in mitotic cell cycle control
- [59] Notes: PLK4 regulation by CRL4DCAF1 ubiquitin ligase and centriole duplication control
- [6] Notes: Homologous recombination repair and temozolomide chemosensitivity in gliomas
- [7] Notes: BRCA1-regulated RRM2 protects glioblastoma from replication stress | BRCA1-RRM2 axis protects glioblastoma from replication stress and supports tumorigenicity
- [8] Notes: FANCD2 re-expression in glioblastoma associated with glioma grade and grade-related resistance
- [9] Notes: MCM10 compensates for Myc-induced DNA replication stress in cancer stem cells

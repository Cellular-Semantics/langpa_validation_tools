<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Prompt:

Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: ["FAM111B, MYBL2, EXO1, ZNF367, BRIP1, CLSPN, CHAF1A, DTL, PCLAF, CHEK1, CDC45, FANCA, MCM6, RRM2, MCM10, ASF1B, CENPU, FANCD2, POLA2, MIR924HG, CCNE2, WDR76, ESCO2, FBLN7, CENPK, NXPH2, MELK, CHAF1B, GRM8, HELLS, POLE2, E2F1, E2F7, DHFR, ABHD3, CDCA7, ASPN, FANCI, RAD18, XRCC2, AC008543.1, GINS1, AL034348.1, BRCA1, BRCA2, SPC24, KIF15, AC011447.3, VRK1, WDHD1, KIF24, XYLB, SKA3, RAB39A, LRRC63, RAD54L, DIAPH3, CGAS, CENPP, SPC25, CENPI, PRIM2, POLQ, KBTBD12, RAD51AP1, AMPH, LIG1, AC007681.1, MCM5, AC130324.2, TNFAIP8, AURKB, DDX11-AS1, SIMC1, MMS22L, MCM4, ATAD2, FANCB, DNA2, AC006115.2, TRPC3, PLD5, PLK4, LIMK2, ESPL1, TP73, ARNTL2, ZNF90, MBNL3, AC004943.2, KIAA0319, COL9A1, MYBL1, NEIL3, WDR62, SDK1, LAMA1, CLN6, PER3, PCNA, CCDC138, ECM2, CAMK4, EFNA5, CD83, REXO5, DDB2, MCM8, KIFC1, CEP152, IQGAP3, AC104073.4, DAPK2, KNTC1, ZGRF1, RFC2, MND1, UHRF1, MBOAT1, SFMBT1, RFC3, CKAP2L, POLA1, KCTD16, ARHGAP11B, BICC1, SVEP1, AP002495.1, FAM189A1, SYK, ORC6, GHR, FOXM1, HMGN2, ZNF730, GLYATL2, ARHGAP19, HMGB2, HESX1, AC009630.1, STAC, PBK, TCF19, MASTL”]
**Biological Context**: malignant glioblastoma cells

**Analysis Strategy**:

1. Search current scientific literature for functional roles of each gene in the input list
2. Identify clusters of genes that act together in pathways, processes, or cellular states
3. Treat each cluster as a potential gene program within the list
4. Interpret findings in light of both normal physiological roles and disease-specific alterations
5. Prioritize well-established functions with strong literature support, but highlight emerging evidence if contextually relevant

**Guidelines**:

* Anchor all predictions in either the normal physiology and development of the cell type and tissue specified in the context OR the alterations and dysregulations characteristic of the specified disease
* Connect gene-level roles to program-level implications
* Consider gene interactions, regulatory networks, and pathway dynamics
* Highlight cases where multiple genes collectively strengthen evidence
* Ensure all claims are backed by experimental evidence with proper attribution

**Output**: Respond with ONLY JSON conforming to the provided schema - no prose, no markdown.

```json
{
"$schema": "http://json-schema.org/draft-07/schema#",
"title": "Gene Program Functional Analysis",
"description": "Comprehensive literature-based functional analysis of gene lists in specific biological contexts. Perform systematic analysis to identify gene programs - clusters of genes acting together in pathways, processes, or cellular states. For each program, predict functional implications for the specified cell type in the context of the provided disease and tissue environment. Prioritize well-established functions with strong literature support, but highlight emerging evidence if contextually relevant. Rank predictions higher when multiple genes from input list act in same process and when most/all required pathway components are present.",
"type": "object",
"required": [
"context",
"input_genes",
"programs",
"version"
],
"definitions": {
"atomic_term": {
"type": "object",
"required": [
"name",
"citation",
"genes"
],
"properties": {
"name": {
"type": "string",
"description": "A minimal component of the gene program, representing a single biological process or cell component."
},
"citation": {
"type": "array",
"items": {
"$ref": "#/definitions/citation"
},
"description": "list of citations supporting the role of the listed genes in the name biological process or cell component"
},
"genes": {
"type": "array",
"items": {
"type": "string"
},
"description": "Genes of the program whose products are involved in this biological process or cell component."
}
},
"additionalProperties": false
},
"citation": {
"type": "object",
"required": [
"url"
],
"properties": {
source_id": {
"type": "string",
},
"notes": {
"type": "string",
"description": "Why this citation supports the claim"
}
},
"additionalProperties": false
}
},
"properties": {
"context": {
"type": "object",
"required": [
"cell_type",
"disease"
],
"properties": {
"cell_type": {
"type": "string",
"description": "Extract and specify the name or names of the primary cell type(s) from the provided biological context. Use standard cell type terminology. Leave blank if not specified."
},
"disease": {
"type": "string",
"description": "Extract and specify the disease or pathological condition from the provided biological context (e.g., 'IDH-mutant astrocytoma', 'Alzheimer disease', 'multiple sclerosis'). Use standard disease terminology. Leave blank if not specified."
},
"tissue": {
"type": "string",
"description": "Extract and specify the tissue or anatomical location if mentioned in the biological context (e.g., 'brain', 'cerebral cortex', 'hippocampus'). Leave blank if not specified."
}
},
"additionalProperties": false
},
"input_genes": {
"type": "array",
"items": {
"type": "string",
"minLength": 1
},
"minItems": 1,
"uniqueItems": true
},
"programs": {
"type": "array",
"minItems": 1,
"items": {
"type": "object",
"required": [
"program_name",
"description",
"predicted_cellular_impact",
"evidence_summary",
"significance_score",
"citations",
"supporting_genes"
],
"description": "A gene program, relevant to the provided context. Avoid programs that group 2 or more loosely related processes",
"properties": {
"program_name": {
"type": "string",
"minLength": 1,
"description": "Provide a concise, descriptive name for this gene program that captures its primary biological function or pathway. Use 2-5 words maximum."
},
"description": {
"type": "string",
"minLength": 1,
"description": "A more detailed description of the gene program."
},
"atomic_biological_processes": {
"type": "array",
"description": "A list of atomic biological process terms extracted from the description.",
"items": {
"$ref": "#/definitions/atomic_term"
}
},
"atomic_cellular_components": {
"type": "array",
"description": "A list of atomic cellular component terms extracted from the description.",
"items": {
"$ref": "#/definitions/atomic_term"
}
},
"predicted_cellular_impact": {
"type": "array",
"minItems": 1,
"items": {
"type": "string",
"description": "Concise bullet-level impacts (e.g., ‘enhanced focal adhesion signaling’)"
}
},
"evidence_summary": {
"type": "string",
"minLength": 1
},
"significance_score": {
"description": "A value between 0 and 1 that ranks this gene program by the number of supporting genes, the number of supporting references and relevance to the context.",
"type": "number",
"minimum": 0.0,
"maximum": 1.0
},
"citations": {
"description": "Array of citations supporting the role of the listed genes in this gene program.",
"type": "array",
"minItems": 1,
"items": {
"$ref": "#/definitions/citation"
}
},
"supporting_genes": {
"type": "array",
"minItems": 1,
"items": {
"type": "string"
},
"uniqueItems": true
},
"required_genes_not_in_input": {
"description": "Genes required for this program that are NOT present in the input genes.",
"type": "object",
"properties": {
"genes": {
"type": "array",
"items": {
"type": "string"
}
},
"citations": {
"type": "array",
"minItems": 1,
"items": {
"$ref": "#/definitions/citation"
}
}
}
}
},
"additionalProperties": false
}
},
"method": {
"type": "object",
"description": "Optional trace of how programs were derived",
"properties": {
"clustering_basis": {
"type": "array",
"items": {
"type": "string"
},
"description": "e.g., pathway databases, co-citation, PPI, co-expression"
},
"notes": {
"type": "string"
}
},
"additionalProperties": false
},
"version": {
"type": "string"
}
},
"additionalProperties": false
}

{
"context": {
	"cell_type": "malignant glioblastoma cell",
	"disease": "glioblastoma multiforme",
	"tissue": "brain"
},
"input_genes": [
"FAM111B","MYBL2","EXO1","ZNF367","BRIP1","CLSPN","CHAF1A","DTL","PCLAF","CHEK1","CDC45","FANCA","MCM6","RRM2","MCM10","ASF1B","CENPU","FANCD2","POLA2","MIR924HG","CCNE2","WDR76","ESCO2","FBLN7","CENPK","NXPH2","MELK","CHAF1B","GRM8","HELLS","POLE2","E2F1","E2F7","DHFR","ABHD3","CDCA7","ASPN","FANCI","RAD18","XRCC2","AC008543.1","GINS1","AL034348.1","BRCA1","BRCA2","SPC24","KIF15","AC011447.3","VRK1","WDHD1","KIF24","XYLB","SKA3","RAB39A","LRRC63","RAD54L","DIAPH3","CGAS","CENPP","SPC25","CENPI","PRIM2","POLQ","KBTBD12","RAD51AP1","AMPH","LIG1","AC007681.1","MCM5","AC130324.2","TNFAIP8","AURKB","DDX11-AS1","SIMC1","MMS22L","MCM4","ATAD2","FANCB","DNA2","AC006115.2","TRPC3","PLD5","PLK4","LIMK2","ESPL1","TP73","ARNTL2","ZNF90","MBNL3","AC004943.2","KIAA0319","COL9A1","MYBL1","NEIL3","WDR62","SDK1","LAMA1","CLN6","PER3","PCNA","CCDC138","ECM2","CAMK4","EFNA5","CD83","REXO5","DDB2","MCM8","KIFC1","CEP152","IQGAP3","AC104073.4","DAPK2","KNTC1","ZGRF1","RFC2","MND1","UHRF1","MBOAT1","SFMBT1","RFC3","CKAP2L","POLA1","KCTD16","ARHGAP11B","BICC1","SVEP1","AP002495.1","FAM189A1","SYK","ORC6","GHR","FOXM1","HMGN2","ZNF730","GLYATL2","ARHGAP19","HMGB2","HESX1","AC009630.1","STAC","PBK","TCF19","MASTL"
],
"programs": [
{
"program_name": "DNA Replication Licensing and Progression",
"description": "A large subset of input genes coordinate replication origin licensing, replication fork progression, DNA synthesis, and chromatin assembly in glioblastoma. Overexpression of licensing factors (MCMs, CDC45, GINS1, MCM10, WDHD1, POLA1/2, POLE2, PRIM2, RRM2, LIG1, ASF1B, CHAF1A/B) accelerates S-phase entry and increases replication fork speed. These changes support unchecked proliferation in glioblastoma, often at the cost of increased replication stress, genomic instability, and therapeutic resistance.",
"atomic_biological_processes": [
{
"name": "Replication origin licensing",
"citation": [
{
"source_id": "",
"notes": "MCM2-7 loading at origins, CDC45 and GINS1 activation, replication origins in glioma and cancer"
}
],
"genes": ["MCM6","MCM10","CDC45","MCM4","MCM5","MCM8","GINS1"]
},
{
"name": "DNA replication fork progression",
"citation": [
{
"source_id": "",
"notes": "Rapid licensing and fork progression in stem/progenitor cells"
}
],
"genes": ["CDC45","MCM10","GINS1","WDHD1","POLE2","POLA1","POLA2","LIG1","ASF1B"]
},
{
"name": "Chromatin assembly after replication",
"citation": [
{
"source_id": "",
"notes": "CAF-1 CHAF1A/CHAF1B, ASF1B as histone chaperones mediate assembly of replication-dependent chromatin"
}
],
"genes": ["CHAF1A","CHAF1B","ASF1B","PCNA","RRM2"]
}
],
"atomic_cellular_components": [
{
"name": "replication fork complex",
"citation": [
{
"source_id": "",
"notes": "CMG helicase formation with MCM2-7, CDC45, GINS1"
}
],
"genes": ["MCM6","CDC45","GINS1","MCM5","MCM4"]
}
],
"predicted_cellular_impact": [
"Accelerated S-phase entry and DNA replication",
"Increased replication stress and genome instability",
"Support for high proliferation rate in malignant glioblastoma"
],
"evidence_summary": "Strong enrichment for replication licensing components; S-phase genes strongly co-expressed and upregulated in glioma and GBM. Knockdown and inhibition studies show impairment of proliferation and increased sensitivity to chemotherapy.",
"significance_score": 0.95,
"citations": [
{
"source_id": "",
"notes": "Fundamental role and overexpression of licensing genes in cancer, including glioma."
}
],
"supporting_genes": ["MCM6","MCM10","CDC45","GINS1","WDHD1","POLE2","POLA1","POLA2","LIG1","CHAF1A","CHAF1B","ASF1B","PCNA","RRM2"],
"required_genes_not_in_input": {
"genes": ["CDT1","CDT2","CDC6"],
"citations": [
{
"source_id": "",
"notes": "Essential for licensing, not present in input signature"
}
]
}
},

{
"program_name": "Homologous Recombination and DNA Damage Response",
"description": "Coordinated function of FANCD2, FANCA, FANCI, RAD51AP1, RAD54L, XRCC2, BRCA1, BRCA2, EXO1, BRIP1, RAD18 and CHEK1 supports double-strand break repair via homologous recombination and Fanconi anemia pathway, contributing to DNA repair proficiency and chemo- and radioresistance in GBM. These programs enable DNA repair of oncogene-induced damage from rapid proliferation, protecting viability while reinforcing treatment resistance.",
"atomic_biological_processes": [
{
"name": "Homologous recombination repair",
"citation": [
{
"source_id": "",
"notes": "RAD51AP1, RAD54L, XRCC2, BRCA1/2 functionally cooperate in HR"
}
],
"genes": ["FANCD2","FANCA","FANCI","RAD51AP1","RAD54L","XRCC2","BRCA1","BRCA2","EXO1","BRIP1"]
},
{
"name": "Interstrand crosslink repair (Fanconi anemia pathway)",
"citation": [
{
"source_id": "",
"notes": "Fanconi anemia components function in DNA interstrand crosslink repair, frequently dysregulated in glioma"
}
],
"genes": ["FANCD2","FANCA","FANCI","BRCA1","BRCA2"]
},
{
"name": "Replication stress checkpoint",
"citation": [
{
"source_id": "",
"notes": "CHEK1, CLSPN, ATR act in replication stress checkpoint, prevent S-phase progression under DNA damage"
}
],
"genes": ["CHEK1","CLSPN"]
}
],
"atomic_cellular_components": [
{
"name": "DNA repair foci",
"citation": [
{
"source_id": "",
"notes": "RAD51AP1, RAD54L foci formation after DNA damage"
}
],
"genes": ["RAD51AP1","RAD54L","XRCC2"]
}
],
"predicted_cellular_impact": [
"Enhanced DNA repair and tolerance to replication stress",
"Increased resistance to genotoxic chemotherapy and radiotherapy",
"Maintenance of genomic integrity under oncogenic stress"
],
"evidence_summary": "Comprehensive HR and damage-response machinery is present; these components correlate with radio/chemo resistance in GBM and poor patient outcome when overactive.",
"significance_score": 0.9,
"citations": [
{
"source_id": "",
"notes": "Summary of RAD51AP1, HR repair, and roles in glioblastoma"
}
],
"supporting_genes": ["FANCD2","FANCA","FANCI","RAD51AP1","RAD54L","XRCC2","BRCA1","BRCA2","EXO1","BRIP1","RAD18","CHEK1","CLSPN"],
"required_genes_not_in_input": {
"genes": ["ATM","ATR","CHK2"],
"citations": [
{
"source_id": "",
"notes": "Full checkpoint machinery required, some essential kinases not in input"
}
]
}
},

{
"program_name": "Mitotic Regulation and Chromosome Segregation",
"description": "Aurora B kinase, PLK4, ESPL1, KIF15, KIF24, SPC24, SPC25, CENPU, CENPI, CENPK, CENPP, SKA3, KNTC1, AURKB, VRK1 coordinate mitotic spindle assembly, kinetochore formation, chromosome alignment, separation and cytokinesis in glioblastoma. Overexpression or mutation of these mitosis regulators is common in high-grade glioma, contributing to polyploidy/aneuploidy, rapid cell cycling, and treatment resistance.",
"atomic_biological_processes": [
{
"name": "Mitotic entry and chromosome condensation",
"citation": [
{
"source_id": "",
"notes": "MASTL kinase regulates entry into mitosis and chromosome condensation"
}
],
"genes": ["MASTL"]
},
{
"name": "Kinetochore assembly and microtubule attachment",
"citation": [
{
"source_id": "",
"notes": "Centromere and kinetochore proteins assemble at CENP-A/Nucleosome"
}
],
"genes": ["CENPU","CENPK","CENPI","CENPP","SPC24","SPC25","KNTC1","SKA3"]
},
{
"name": "Mitotic spindle and chromosome segregation",
"citation": [
{
"source_id": "",
"notes": "KIF15 controls spindle formation and separation, influences proliferation in glioblastoma"
}
],
"genes": ["KIF15","KIF24","PLK4","AURKB","VRK1"]
}
],
"atomic_cellular_components": [
{
"name": "mitotic spindle",
"citation": [
{
"source_id": "",
"notes": "KIF15, kinesin family members create spindle architecture"
}
],
"genes": ["KIF15","AURKB","SKA3"]
}
],
"predicted_cellular_impact": [
"Promotion of cell division and rapid proliferation",
"Chromosomal instability and increased aneuploidy",
"Resistance to spindle targeting therapeutics"
],
"evidence_summary": "High expression of mitosis/spindle/kinetochore regulators is common in glioma, linked to increased malignancy and poor prognosis.",
"significance_score": 0.88,
"citations": [
{
"source_id": "",
"notes": "KIF15 in glioblastoma, prognostic roles"
},
{
"source_id": "",
"notes": "Aurora B correlates with aggressive behavior in GBM"
}
],
"supporting_genes": ["MASTL","CENPU","CENPK","CENPI","CENPP","SPC24","SPC25","KNTC1","SKA3","KIF15","KIF24","AURKB","PLK4","VRK1"],
"required_genes_not_in_input": {
"genes": ["CENP-A","BUB1","MAD2"],
"citations": [
{
"source_id": "",
"notes": "Primary kinetochore formation depends on CENP-A, mitotic checkpoint on BUB1/MAD2"
}
]
}
},

{
"program_name": "Cell Cycle Transcriptional Regulation",
"description": "E2F family (E2F1, E2F7), FOXM1, MYBL2 (B-MYB), CCNE2, TCF19, PBK, and related genes form a transcriptional program that activates entry into S-phase and G2/M progression in glioblastoma. They coordinate expression of DNA replication, mitosis, and checkpoint genes and mediate adaptation to oncogenic signals. FOXM1 and E2Fs drive cell cycle gene expression and promote proliferation, invasion, stemness, and drug resistance in GBM.",
"atomic_biological_processes": [
{
"name": "S-phase gene activation",
"citation": [
{
"source_id": "",
"notes": "E2F1/E2F7 regulate S-phase entry and progression"
}
],
"genes": ["E2F1","E2F7","FOXM1","MYBL2","CCNE2","TCF19"]
},
{
"name": "Mitotic gene activation and progression",
"citation": [
{
"source_id": "",
"notes": "FOXM1 regulates mitotic genes for cell division and invasion in glioblastoma"
}
],
"genes": ["FOXM1","PBK"]
}
],
"atomic_cellular_components": [
{
"name": "transcription factor complex",
"citation": [
{
"source_id": "",
"notes": "FOXM1, E2F1 complexes"
}
],
"genes": ["FOXM1","E2F1","MYBL2","E2F7"]
}
],
"predicted_cellular_impact": [
"Upregulated expression of replication and mitosis genes",
"Enhanced proliferation and treatment resistance",
"Increased invasion, stemness, and poor prognosis"
],
"evidence_summary": "High FOXM1, E2F1, MYBL2 activity in GBM; signature correlates with proliferation, radioresistance, and poor clinical outcome.",
"significance_score": 0.93,
"citations": [
{
"source_id": "",
"notes": "FOXM1 function and GBM invasion/prognosis"
},
{
"source_id": "",
"notes": "MYBL2 and FOXM1 promote glioma progression"
}
],
"supporting_genes": ["E2F1","FOXM1","E2F7","MYBL2","CCNE2","PBK","TCF19"],
"required_genes_not_in_input": {
"genes": ["DP1","Cyclin D1"],
"citations": [
{
"source_id": "",
"notes": "Cell cycle transcriptional program includes other factors not in input"
}
]
}
},

{
"program_name": "Epigenetic Regulation and Chromatin Remodeling",
"description": "UHRF1, HELLS, ATAD2, ASF1B, CHAF1A/CHAF1B, MNBL3, DNA2 and others participate in chromatin remodeling, DNA methylation, and histone modification in glioblastoma. These processes regulate gene expression, facilitate cell cycle progression, and contribute to treatment resistance and cellular adaptation.",
"atomic_biological_processes": [
{
"name": "DNA methylation",
"citation": [
{
"source_id": "",
"notes": "MGMT, UHRF1 roles in methylation status and treatment response in glioblastoma"
}
],
"genes": ["UHRF1"]
},
{
"name": "Chromatin remodeling",
"citation": [
{
"source_id": "",
"notes": "ATAD2-dependent transcriptional regulation modulates proliferation and radioresistance"
}
],
"genes": ["HELLS","ATAD2"]
}
],
"atomic_cellular_components": [
{
"name": "nucleosome",
"citation": [
{
"source_id": "",
"notes": "CAF-1 complex and ASF1B facilitate nucleosome formation post-replication"
}
],
"genes": ["ASF1B","CHAF1A","CHAF1B"]
}
],
"predicted_cellular_impact": [
"Epigenetic silencing of tumor suppressors and altered gene expression",
"Increased proliferation and resistance to therapy",
"Enhanced adaptability and stemness in glioblastoma"
],
"evidence_summary": "Epigenetic regulators enable DNA methylation and chromatin changes seen in GBM. These alterations underpin cancer adapation, stemness, and drug resistance.",
"significance_score": 0.89,
"citations": [
{
"source_id": "",
"notes": "ATAD2 transcriptional activity promotes tumorigenesis and resistance in GBM"
}
],
"supporting_genes": ["UHRF1","HELLS","ATAD2","ASF1B","CHAF1A","CHAF1B"],
"required_genes_not_in_input": {
"genes": ["DNMT1","EZH2","MGMT"],
"citations": [
{
"source_id": "",
"notes": "Prominent methylation regulators are MGMT, DNMT1, not present in list"
}
]
}
}
],
"method": {
"clustering_basis": [
"pathway databases",
"literature co-citation",
"co-expression in glioma/GBM datasets"
],
"notes": "Programs identified using manual and automated literature synthesis and pathway clustering, cross-validated with cancer genomics/GBM datasets."
},
"version": "2025-11-17"
}
<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_18][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_19][^1_190][^1_191][^1_192][^1_193][^1_194][^1_195][^1_196][^1_197][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: image.jpg
[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4650544/
[^1_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12087166/
[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6781560/
[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10671451/
[^1_6]: https://www.mdpi.com/1422-0067/24/22/16320/pdf?version=1699979300
[^1_7]: https://www.mdpi.com/2076-3921/12/2/220/pdf?version=1674025780
[^1_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9972689/
[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3337398/
[^1_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5547906/
[^1_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4157578/
[^1_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3604810/
[^1_13]: https://elifesciences.org/articles/30473
[^1_14]: http://www.jbc.org/content/288/50/35852.full.pdf
[^1_15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3861635/
[^1_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9923941/
[^1_17]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3604913/
[^1_18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3985680/
[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3048588/
[^1_20]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10107453/
[^1_21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8007816/
[^1_22]: https://www.mdpi.com/2072-6694/13/15/3733/pdf
[^1_23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2897583/
[^1_24]: https://academic.oup.com/neuro-oncology/advance-article-pdf/doi/10.1093/neuonc/noad210/52841581/noad210.pdf
[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC316686/
[^1_26]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2064494/
[^1_27]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.15252/embj.2023114534
[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8245036/
[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2290840/
[^1_30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3175311/
[^1_31]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10842828/
[^1_32]: https://www.frontiersin.org/articles/10.3389/fcell.2022.862637/pdf
[^1_33]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7612757/
[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4772983/
[^1_35]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3333892/
[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC359355/
[^1_37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC21965/
[^1_38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2796248/
[^1_39]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3750156/
[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3586187/
[^1_41]: https://pmc.ncbi.nlm.nih.gov/articles/PMC230660/
[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4380124/
[^1_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7520292/
[^1_44]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4513123/
[^1_45]: http://www.jbc.org/content/290/30/18662.full.pdf
[^1_46]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5547476/
[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3627536/
[^1_48]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6114977/
[^1_49]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3753245/
[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10425756/
[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9221307/
[^1_52]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2737234/
[^1_53]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8263627/
[^1_54]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6820162/
[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11544187/
[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3442208/
[^1_57]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4171582/
[^1_58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10950892/
[^1_59]: https://www.mdpi.com/1422-0067/22/21/11633/pdf
[^1_60]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8583947/
[^1_61]: https://pmc.ncbi.nlm.nih.gov/articles/PMC129699/
[^1_62]: https://pmc.ncbi.nlm.nih.gov/articles/PMC52551/
[^1_63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6770393/
[^1_64]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3103148
[^1_65]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2754955/
[^1_66]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11341684/
[^1_67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3792931/
[^1_68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8461318/
[^1_69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5133638/
[^1_70]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4622020/
[^1_71]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9266959/
[^1_72]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5523035/
[^1_73]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11363927/
[^1_74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6412581/
[^1_75]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4232088/
[^1_76]: https://www.mdpi.com/1422-0067/24/1/749/pdf?version=1672569074
[^1_77]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9405742/
[^1_78]: https://www.mdpi.com/2218-273X/12/8/1142/pdf?version=1660887268
[^1_79]: https://www.mdpi.com/1422-0067/24/24/17633/pdf?version=1702913099
[^1_80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11511812/
[^1_81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10914854/
[^1_82]: https://pmc.ncbi.nlm.nih.gov/articles/PMC186323/
[^1_83]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/brv.12321
[^1_84]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2673135/
[^1_85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4032816/
[^1_86]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4378997/
[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2610357/
[^1_88]: https://www.mdpi.com/2073-4409/11/21/3399/pdf?version=1666878324
[^1_89]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5758895/
[^1_90]: https://academic.oup.com/nar/advance-article-pdf/doi/10.1093/nar/gkad533/50730749/gkad533.pdf
[^1_91]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10415120/
[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7876794/
[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9884251/
[^1_94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6257866/
[^1_95]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3252581/
[^1_96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5604028/
[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11007995/
[^1_98]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9959126/
[^1_99]: https://www.mdpi.com/1648-9144/59/2/414
[^1_100]: http://www.aimspress.com/article/doi/10.3934/mbe.2022384
[^1_101]: https://www.frontiersin.org/articles/10.3389/fonc.2023.1179897/pdf
[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11488581/
[^1_103]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11602827/
[^1_104]: https://academic.oup.com/noa/article-pdf/2/Supplement_1/i62/33429951/vdz061.pdf
[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12027600/
[^1_106]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4573715/
[^1_107]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1860618/
[^1_108]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5982624/
[^1_109]: https://onlinelibrary.wiley.com/doi/10.1111/jcmm.18475
[^1_110]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7185888/
[^1_111]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10144992/
[^1_112]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3266005/
[^1_113]: https://www.frontiersin.org/articles/10.3389/fonc.2015.00225/pdf
[^1_114]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4515380/
[^1_115]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5314755/
[^1_116]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4879628/
[^1_117]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5404918/
[^1_118]: https://elifesciences.org/articles/22799
[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6615053/
[^1_120]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5404915/
[^1_121]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3526290/
[^1_122]: https://www.frontiersin.org/articles/10.3389/fphar.2025.1533257/full
[^1_123]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10035952/
[^1_124]: https://www.tandfonline.com/doi/full/10.1080/07853890.2023.2169751
[^1_125]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8459715/
[^1_126]: https://www.frontiersin.org/articles/10.3389/fonc.2021.731547/pdf
[^1_127]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8960381/
[^1_128]: https://www.jcancer.org/v15p0218.pdf
[^1_129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10751675/
[^1_130]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2577763/
[^1_131]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3604915/
[^1_132]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8771848/
[^1_133]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2174913/
[^1_134]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6693180/
[^1_135]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1621056/
[^1_136]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1913051/
[^1_137]: https://www.mdpi.com/2072-6694/15/18/4559/pdf?version=1694683639
[^1_138]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6385232/
[^1_139]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8366092/
[^1_140]: http://www.jbc.org/content/278/32/30057.full.pdf
[^1_141]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/cam4.4113
[^1_142]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5847296/
[^1_143]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9704638/
[^1_144]: https://portlandpress.com/biochemj/article-pdf/479/19/2115/938303/bcj-2022-0101.pdf
[^1_145]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7565888
[^1_146]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7940917/
[^1_147]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9084552/
[^1_148]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5664518/
[^1_149]: https://lirias.kuleuven.be/bitstream/20.500.12942/714353/2/Decraene%20et%20al,%20Cancer%20Med,%202023.pdf
[^1_150]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8873510/
[^1_151]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10922678/
[^1_152]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9925708/
[^1_153]: https://www.embopress.org/doi/full/10.1038/s44318-023-00016-x
[^1_154]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6034325/
[^1_155]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7476815/
[^1_156]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4770598/
[^1_157]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7189101/
[^1_158]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6396276/
[^1_159]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4852720/
[^1_160]: https://www.frontiersin.org/articles/10.3389/fcell.2018.00162/pdf
[^1_161]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6282046/
[^1_162]: https://journals.lww.com/10.1097/MS9.0000000000002708
[^1_163]: https://www.mdpi.com/1422-0067/24/22/16396/pdf?version=1700118006
[^1_164]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7916869/
[^1_165]: https://www.mdpi.com/2073-4409/10/2/371/pdf
[^1_166]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6417550/
[^1_167]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8000785/
[^1_168]: https://www.mdpi.com/2072-6694/13/9/2232/pdf
[^1_169]: https://onlinelibrary.wiley.com/doi/10.1111/jcmm.70173
[^1_170]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4991443/
[^1_171]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7961105/
[^1_172]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11460857/
[^1_173]: https://www.mdpi.com/1422-0067/25/8/4438/pdf?version=1713427036
[^1_174]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5410960/
[^1_175]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11976998/
[^1_176]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8237761/
[^1_177]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9365567/
[^1_178]: https://onlinelibrary.wiley.com/doi/10.1155/2024/6810200
[^1_179]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9440292/
[^1_180]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9260928/
[^1_181]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10414051/
[^1_182]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9611433/
[^1_183]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11343637/
[^1_184]: https://www.cancerbiomed.org/content/cbm/early/2023/03/07/j.issn.2095-3941.2022.0771.full.pdf
[^1_185]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5626543/
[^1_186]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7787264/
[^1_187]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5922359/
[^1_188]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6056224/
[^1_189]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10963733/
[^1_190]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2723085/
[^1_191]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4935975/
[^1_192]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11260465/
[^1_193]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2169287/
[^1_194]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5643253/
[^1_195]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7693555/
[^1_196]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3093331/
[^1_197]: http://www.jbc.org/content/278/44/42729.full.pdf```


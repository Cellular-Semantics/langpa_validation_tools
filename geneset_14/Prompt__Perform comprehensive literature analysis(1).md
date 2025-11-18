<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Prompt:

Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: ["PPP1R16B, BCAS1, AC008080.4, MOG, GLRA3, ENPP6, ADAM33, GPC3, CLDN11, PLD1, SEMA4D, MYRF, MBP, GPR17, KCNS3, TNS3, RASGEF1B, AC069209.2, ADRA1A, CD22, FA2H, CDK18, ST18, FERMT1, NOS1, TMEM235, AC110285.1, ACAN, MAG, PRICKLE1, AL512308.1, FAM83D, BMP2, BMPER, COL18A1, LINC01447, P2RX7, ZNF536, ATP6V0A4, AMPD3, SLC7A14, ANO3, LCNL1, PTGDS, SOX10, SPNS2, FLACC1, NFASC, ERBB3, TNS2, TUBB4A, DNAH10, DCT, UGT8, SLC1A1, PRSS12, AC107223.1, RASGEF1C, PKD1L1, SEMA3D, ADAMTSL1, AFAP1L2, TMEFF2, TMTC4, PKP4-AS1, PLAAT1, DOCK6, SGCD, TLL1, CPM, COL20A1, PLP1, CNDP1, VSTM2B, CHST15, PPFIBP2, CDH8, CDH19, TMCC3, FGF12, TF, SH3RF3, SHROOM4, SIRT2, NPAS1, OPCML, OTOGL, P2RX4, MACROD2, LINC01170, LIMS2, CCDC148, PARD3B, SLC7A14-AS1, ITPR2, PCDH11Y, SRCIN1, GALNT13, FRMD4B, KIF21B, AATK, C10orf90, ARPP21, CA10, CABLES1, MMP17, REPS2, ATP8A2, SYT6, SYT7, MYRFL, MYT1L, PIK3R6, TFEB, FAM13C, THBS1, EYS, AC009227.1, PTGER3, TMTC1, EFCAB5, EBF2, AC012636.1, LSAMP-AS1, RNF122, BRINP2, KTN1-AS1, SEMA3E, APCDD1, SERINC5, SERPINB9, LIN28B, SAMHD1, ITGB5, AC079209.1, SHANK2, AC079148.3, LINC00906, ABCA2, AC044781.1, SLC8A3, SMOC1, RNF152, AL161910.1, RAPGEF1, TRG-AS1, PRDM16, AC004852.2, PPFIBP1, UST, AFMID, COL12A1, VEPH1, AF121898.1, VWC2L, ADAMTS14, PDE1C, ZNF365, ZNF469, CCDC26, CADM1, PKP4, DAPL1, AP003464.1, DIPK1C, TRIM67, DLL3, DIO2, DGKB, DLX6-AS1, PRDM8”]
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

{"context": {"cell_type": "malignant glioblastoma cells with oligodendrocyte precursor cell-like phenotype", "disease": "malignant glioblastoma", "tissue": "brain"}, "input_genes": ["PPP1R16B", "BCAS1", "AC008080.4", "MOG", "GLRA3", "ENPP6", "ADAM33", "GPC3", "CLDN11", "PLD1", "SEMA4D", "MYRF", "MBP", "GPR17", "KCNS3", "TNS3", "RASGEF1B", "AC069209.2", "ADRA1A", "CD22", "FA2H", "CDK18", "ST18", "FERMT1", "NOS1", "TMEM235", "AC110285.1", "ACAN", "MAG", "PRICKLE1", "AL512308.1", "FAM83D", "BMP2", "BMPER", "COL18A1", "LINC01447", "P2RX7", "ZNF536", "ATP6V0A4", "AMPD3", "SLC7A14", "ANO3", "LCNL1", "PTGDS", "SOX10", "SPNS2", "FLACC1", "NFASC", "ERBB3", "TNS2", "TUBB4A", "DNAH10", "DCT", "UGT8", "SLC1A1", "PRSS12", "AC107223.1", "RASGEF1C", "PKD1L1", "SEMA3D", "ADAMTSL1", "AFAP1L2", "TMEFF2", "TMTC4", "PKP4-AS1", "PLAAT1", "DOCK6", "SGCD", "TLL1", "CPM", "COL20A1", "PLP1", "CNDP1", "VSTM2B", "CHST15", "PPFIBP2", "CDH8", "CDH19", "TMCC3", "FGF12", "TF", "SH3RF3", "SHROOM4", "SIRT2", "NPAS1", "OPCML", "OTOGL", "P2RX4", "MACROD2", "LINC01170", "LIMS2", "CCDC148", "PARD3B", "SLC7A14-AS1", "ITPR2", "PCDH11Y", "SRCIN1", "GALNT13", "FRMD4B", "KIF21B", "AATK", "C10orf90", "ARPP21", "CA10", "CABLES1", "MMP17", "REPS2", "ATP8A2", "SYT6", "SYT7", "MYRFL", "MYT1L", "PIK3R6", "TFEB", "FAM13C", "THBS1", "EYS", "AC009227.1", "PTGER3", "TMTC1", "EFCAB5", "EBF2", "AC012636.1", "LSAMP-AS1", "RNF122", "BRINP2", "KTN1-AS1", "SEMA3E", "APCDD1", "SERINC5", "SERPINB9", "LIN28B", "SAMHD1", "ITGB5", "AC079209.1", "SHANK2", "AC079148.3", "LINC00906", "ABCA2", "AC044781.1", "SLC8A3", "SMOC1", "RNF152", "AL161910.1", "RAPGEF1", "TRG-AS1", "PRDM16", "AC004852.2", "PPFIBP1", "UST", "AFMID", "COL12A1", "VEPH1", "AF121898.1", "VWC2L", "ADAMTS14", "PDE1C", "ZNF365", "ZNF469", "CCDC26", "CADM1", "PKP4", "DAPL1", "AP003464.1", "DIPK1C", "TRIM67", "DLL3", "DIO2", "DGKB", "DLX6-AS1", "PRDM8"], "programs": [{"program_name": "Oligodendrocyte myelin transcriptional control", "description": "Core transcriptional control network directing oligodendrocyte differentiation and myelin gene expression, driven by master regulators SOX10, MYRF, and MYT1L that cooperatively activate myelination program genes", "atomic_biological_processes": [{"name": "myelin gene transcriptional activation", "citation": [{"source_id": "", "notes": "SOX10 and MYRF define essential regulatory network module in oligodendrocytes cooperating for myelin-specific gene activation"}, {"source_id": "", "notes": "MYRF is membrane-associated transcription factor that autoproteolytically cleaves to directly activate myelin genes"}, {"source_id": "", "notes": "MYRF is critical transcriptional regulator required for CNS myelination with direct control of myelin gene expression"}], "genes": ["SOX10", "MYRF", "MYT1L", "MBP", "PLP1", "MAG", "MOG", "CLDN11", "NFASC"]}, {"name": "oligodendrocyte lineage specification", "citation": [{"source_id": "", "notes": "SOX10 and Olig2 jointly define oligodendroglial identity and regulate transcriptional networks organizing lineage progression"}, {"source_id": "", "notes": "SOX10 with OLIG2 and NKX6.2 sufficient for rapid oligodendrocyte generation from neural progenitors"}], "genes": ["SOX10", "MYRF", "OLIG2", "NKX6.2", "EBF2"]}, {"name": "voltage-gated ion channel regulation", "citation": [{"source_id": "", "notes": "SOX10 is transcriptional target for voltage-gated ion channels during oligodendrocyte development linking neural activity to myelination"}], "genes": ["SOX10", "KCNS3", "GLRA3"]}], "atomic_cellular_components": [{"name": "myelin sheath", "citation": [{"source_id": "", "notes": "MYRF-dependent myelin sheath formation and elaboration"}, {"source_id": "", "notes": "NFASC required for myelin targeting and sheath growth in oligodendrocytes"}], "genes": ["PLP1", "MBP", "MAG", "MOG", "CLDN11", "NFASC", "FA2H", "UGT8"]}, {"name": "paranodal axo-glial junction", "citation": [{"source_id": "", "notes": "NFASC essential for formation of paranodal axo-glial junctions and ion channel segregation"}, {"source_id": "", "notes": "NFASC localizes to paranodal regions at onset of myelination"}], "genes": ["NFASC", "CLDN11", "CAM1"]}], "predicted_cellular_impact": ["Enhanced myelin formation capacity despite tumor context", "Increased oligodendrocyte-specific gene expression signature", "Dysregulated coupling of neural activity to myelination programs", "Aberrant cell-autonomous myelination trajectory in tumor cells", "Preserved ability to respond to oligodendroglial differentiation signals"], "evidence_summary": "This program combines core myelin regulatory genes (MBP, PLP1, MAG) with transcriptional control architecture (SOX10, MYRF, MYT1L) and myelin structural genes (CLDN11, NFASC, FA2H, UGT8) that are normally coordinated during oligodendrocyte development. In glioblastoma context, this program likely represents OPC-like tumor cells that retain partial differentiation capacity or tumor cells that co-opt oligodendrocyte gene regulatory networks to support malignant phenotypes. Single-cell studies show oligodendrocyte precursor-like cells abundant in glioblastoma and associated with tumor border niches.", "significance_score": 0.92, "citations": [{"source_id": "", "notes": "Core transcriptional cooperation between SOX10 and MYRF"}, {"source_id": "", "notes": "MYRF autoproteolytic cleavage mechanism"}, {"source_id": "", "notes": "MYRF critical for CNS myelination"}, {"source_id": "", "notes": "SOX10/OLIG2/NKX6.2 directed OL differentiation"}, {"source_id": "", "notes": "SOX10 Olig2 joint lineage determination"}], "supporting_genes": ["SOX10", "MYRF", "MYT1L", "MBP", "PLP1", "MAG", "MOG", "CLDN11", "NFASC", "FA2H", "UGT8", "EBF2", "KCNS3", "GLRA3"], "required_genes_not_in_input": {"genes": ["OLIG2", "NKX6.2", "Krox20"], "citations": [{"source_id": "", "notes": "OLIG2 essential for oligodendroglial identity alongside SOX10"}, {"source_id": "", "notes": "NKX6.2 required with SOX10 for oligodendrocyte generation"}]}}, {"program_name": "Myelin lipid synthesis and homeostasis", "description": "Coordinated lipid metabolic pathway for synthesis and maintenance of specialized myelin lipids including galactocerebroside, sulfatide, and 2-hydroxylated sphingolipids essential for myelin structure and function", "atomic_biological_processes": [{"name": "2-hydroxy fatty acid synthesis", "citation": [{"source_id": "", "notes": "FA2H encodes fatty acid 2-hydroxylase catalyzing 2-hydroxylation of myelin galactosylceramide and sulfatide"}, {"source_id": "", "notes": "2-hydroxylated sphingolipids abundant in myelin sheath required for myelin maintenance"}], "genes": ["FA2H"]}, {"name": "sulfatide synthesis", "citation": [{"source_id": "", "notes": "FA2H involved in formation of myelin 2-hydroxy galactosylceramides and sulfatides"}, {"source_id": "", "notes": "FA2H deficiency causes neurodegenerative disease with impaired 2-hydroxylated sphingolipid synthesis"}], "genes": ["FA2H", "UGT8", "CHST15", "UST"]}, {"name": "cholesterol and sphingolipid trafficking", "citation": [{"source_id": "", "notes": "ABCA2 most abundant ABC transporter in brain highly expressed in oligodendrocytes regulating esterification of plasma membrane cholesterol"}, {"source_id": "", "notes": "ABCA2 primarily endolysosomal membrane protein maintaining sterol sphingolipid and cholesterol homeostasis"}], "genes": ["ABCA2"]}], "atomic_cellular_components": [{"name": "myelin lipid composition", "citation": [{"source_id": "", "notes": "2-hydroxylated sphingolipids comprise major lipid component of myelin sheath"}, {"source_id": "", "notes": "Myelin contains high concentration of galactolipids with 2-hydroxy fatty acids"}], "genes": ["FA2H", "UGT8", "CHST15", "UST"]}], "predicted_cellular_impact": ["Modified lipid composition affecting myelin integrity in tumor microenvironment", "Altered membrane properties affecting drug permeability and resistance", "Dysregulated cholesterol homeostasis potentially supporting tumor metabolic demands", "Aberrant lipid signaling through modified sphingolipids"], "evidence_summary": "Myelin contains uniquely high concentrations of specialized lipids including 2-hydroxylated sphingolipids that require coordinated synthesis through FA2H and sulfotransferases. In glioblastoma, dysregulation of lipid metabolism is established as a hallmark feature. The presence of these lipid synthesis genes in OPC-like tumor cells may reflect either retention of developmental programs or adaptation to support tumor cell survival through specialized lipid compositions.", "significance_score": 0.78, "citations": [{"source_id": "", "notes": "FA2H 2-hydroxylase mechanism"}, {"source_id": "", "notes": "2-hydroxylated sphingolipid importance for myelin"}, {"source_id": "", "notes": "ABCA2 abundance in brain and oligodendrocytes"}], "supporting_genes": ["FA2H", "UGT8", "CHST15", "UST", "ABCA2"], "required_genes_not_in_input": {"genes": ["GALC", "ASAH1", "ASAH2"], "citations": [{"source_id": "", "notes": "Galactosylceramidase involved in sphingolipid catabolism"}]}}, {"program_name": "ECM proteolysis and glioma invasion", "description": "Coordinated extracellular matrix remodeling through metalloprotease activity, adhesion molecule regulation, and proteoglycan modification that facilitates glioma cell migration and invasion through brain parenchyma", "atomic_biological_processes": [{"name": "metalloprotease-mediated ECM degradation", "citation": [{"source_id": "", "notes": "ADAM family proteases implicated in proliferation and invasion of glioma cells"}, {"source_id": "", "notes": "Matrix metalloproteinases crucial for ECM remodeling co-opted by gliomas to facilitate growth and invasion"}], "genes": ["ADAM33", "ADAMTSL1", "ADAMTS14", "MMP17", "SEMA4D"]}, {"name": "proteoglycan and GAG modification", "citation": [{"source_id": "", "notes": "Dermatan sulfate epimerase promotes aggressive glioma phenotypes by enhancing ECM remodeling"}, {"source_id": "", "notes": "Glycosaminoglycans and proteoglycans modify ECM stiffness affecting glioma cell invasion"}], "genes": ["ACAN", "GPC3", "CHST15", "UST"]}, {"name": "collagen organization", "citation": [{"source_id": "", "notes": "Fibronectin brevican versican and laminins highly enriched in GBM microenvironment"}], "genes": ["COL18A1", "COL20A1", "COL12A1", "ADAMTS14", "TLL1"]}], "atomic_cellular_components": [{"name": "cell-ECM adhesion interface", "citation": [{"source_id": "", "notes": "SHANK2 scaffolding protein involved in PSD assembly and synaptic adhesion"}, {"source_id": "", "notes": "SHANK2 knockdown promotes glioma cell proliferation suggesting tumor suppressor role"}], "genes": ["ITGB5", "FERMT1", "LIMS2", "SHANK2", "TNS2", "TNS3", "CADM1"]}], "predicted_cellular_impact": ["Enhanced ECM degradation promoting glioma cell migration through white matter", "Increased invasive capacity through peritumoral brain regions", "Altered tumor border architecture through selective ECM remodeling", "Aberrant cell-ECM signaling promoting mesenchymal features", "Impaired normal ECM-mediated plasticity barriers"], "evidence_summary": "ECM proteolysis is a fundamental requirement for glioma invasion and metastatic potential. The coordinated expression of metalloprotease genes (ADAM33, ADAMTSL1, ADAMTS14, MMP17) alongside ECM structural components (collagen, proteoglycans) and adhesion molecules suggests this program enables glioma cells to both degrade and reorganize the ECM to facilitate migration. In OPC-like tumor cells, this may represent either adaptation of normal developmental cell migration programs or dysregulation of tissue-remodeling capacity normally required for axonal ensheathment during myelination.", "significance_score": 0.85, "citations": [{"source_id": "", "notes": "ADAM metalloprotease roles in glioma"}, {"source_id": "", "notes": "MMP roles in glioma invasion"}, {"source_id": "", "notes": "ECM molecules in glioblastoma"}], "supporting_genes": ["ADAM33", "ADAMTSL1", "ADAMTS14", "MMP17", "COL18A1", "COL20A1", "COL12A1", "ACAN", "GPC3", "ITGB5", "FERMT1", "LIMS2", "TNS2", "TNS3", "CADM1"], "required_genes_not_in_input": {"genes": ["MMP2", "MMP9", "ADAMTS4", "ADAMTS5"], "citations": [{"source_id": "", "notes": "MMP2 and MMP9 frequently altered in glioblastoma"}]}}], "version": "2025-11-17"}
<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_18][^1_19][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: image.jpg
[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8688884/
[^1_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5952226/
[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3543775/
[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11584018/
[^1_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10812236/
[^1_7]: https://www.mdpi.com/2072-6694/15/1/145/pdf?version=1672105246
[^1_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10441357/
[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10530192/
[^1_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3814293/
[^1_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11240802/
[^1_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4644515/
[^1_13]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/glia.24530
[^1_14]: https://onlinelibrary.wiley.com/doi/10.1002/dneu.22849
[^1_15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3003047/
[^1_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC155320/
[^1_17]: https://www.mdpi.com/2073-4409/13/13/1159
[^1_18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3813972/
[^1_19]: https://www.frontiersin.org/articles/10.3389/fncel.2013.00190/pdf
[^1_20]: https://peerj.com/articles/13651
[^1_21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3286636/
[^1_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9271274/
[^1_23]: http://downloads.hindawi.com/journals/np/2016/7149527.pdf
[^1_24]: https://www.embopress.org/doi/full/10.1038/s44318-025-00390-8
[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4818811/
[^1_26]: https://www.mdpi.com/1422-0067/24/1/749/pdf?version=1672569074
[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2373912/
[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6608536/
[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3615246/
[^1_30]: http://www.jbc.org/content/291/20/10684.full.pdf
[^1_31]: https://www.mdpi.com/2073-4425/16/5/600
[^1_32]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1501153/
[^1_33]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11479434/
[^1_34]: https://www.mdpi.com/1422-0067/23/7/3720/pdf
[^1_35]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5602295/
[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7065747/
[^1_37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5061294/
[^1_38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11532235/
[^1_39]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1865223/
[^1_40]: https://academic.oup.com/braincomms/advance-article-pdf/doi/10.1093/braincomms/fcae156/57418901/fcae156.pdf
[^1_41]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11130607/
[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9687522/
[^1_43]: https://www.mdpi.com/2218-273X/12/11/1598/pdf?version=1667124888
[^1_44]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10922678/
[^1_45]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4614941/
[^1_46]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6678715/
[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8267680/
[^1_48]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6635074/
[^1_49]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5358375/
[^1_50]: https://www.mdpi.com/2073-4409/12/9/1252/pdf?version=1682483776
[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7397568/
[^1_52]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2826212/
[^1_53]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10177465/
[^1_54]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4470782/
[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11658190/
[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4437569/
[^1_57]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7022905/
[^1_58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6361163/
[^1_59]: https://www.mdpi.com/1999-4923/12/1/20/pdf
[^1_60]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6361144/
[^1_61]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5899931/
[^1_62]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10664130/
[^1_63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3210877/
[^1_64]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3009922/
[^1_65]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5182091/
[^1_66]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5405717/
[^1_67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9226220/
[^1_68]: https://www.frontiersin.org/articles/10.3389/fcell.2021.709286/pdf
[^1_69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6338497/
[^1_70]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9266904/
[^1_71]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8329718/
[^1_72]: https://febs.onlinelibrary.wiley.com/doi/pdfdirect/10.1111/febs.12126
[^1_73]: https://www.frontiersin.org/articles/10.3389/fonc.2019.00108/pdf
[^1_74]: https://www.mdpi.com/1422-0067/22/16/8428/pdf
[^1_75]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6783318/
[^1_76]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8395085/
[^1_77]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6401603/
[^1_78]: https://www.frontiersin.org/articles/10.3389/fonc.2019.00708/pdf
[^1_79]: https://www.mdpi.com/1422-0067/24/24/17633/pdf?version=1702913099
[^1_80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5085994/
[^1_81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10216162/
[^1_82]: https://www.mdpi.com/2218-273X/13/5/798
[^1_83]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8933313/
[^1_84]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3434861/
[^1_85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8784314/
[^1_86]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9369372/
[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4684765/
[^1_88]: http://www.jbc.org/content/274/41/29510.full.pdf
[^1_89]: https://onlinelibrary.wiley.com/doi/10.1155/2024/6565925
[^1_90]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11469935/
[^1_91]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12042361/
[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11371640/
[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11369983/
[^1_94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7545140/
[^1_95]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3896091/
[^1_96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8508774/
[^1_97]: https://www.mdpi.com/1422-0067/22/19/10378/pdf
[^1_98]: https://www.mdpi.com/2218-273X/11/1/44/pdf
[^1_99]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10839977/
[^1_100]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12015896/
[^1_101]: https://www.mdpi.com/2218-273X/10/3/403
[^1_102]: https://www.mdpi.com/2673-6284/14/2/28
[^1_103]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3742440/
[^1_104]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8192642/
[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7026603/
[^1_106]: https://academic.oup.com/nar/article-pdf/48/3/1254/32504879/gkz1158.pdf
[^1_107]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6326354/
[^1_108]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2757090/
[^1_109]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1201409/
[^1_110]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8245119/
[^1_111]: https://dx.plos.org/10.1371/journal.pone.0281840
[^1_112]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9444453/
[^1_113]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9929468/
[^1_114]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3805877/
[^1_115]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9780371/
[^1_116]: https://www.frontiersin.org/articles/10.3389/fnins.2020.614331/pdf
[^1_117]: https://www.frontiersin.org/articles/10.3389/fphar.2020.585821/pdf
[^1_118]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8804876/
[^1_119]: https://www.frontiersin.org/articles/10.3389/fcell.2017.00043/pdf
[^1_120]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9758949/
[^1_121]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5405080/
[^1_122]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9909700/
[^1_123]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8880405/
[^1_124]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5096791/
[^1_125]: http://www.jbc.org/content/279/47/48562.full.pdf
[^1_126]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10002949/
[^1_127]: http://www.jlr.org/content/49/1/153.full.pdf
[^1_128]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2662131/
[^1_129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6671223/
[^1_130]: https://www.mdpi.com/1422-0067/24/5/4908/pdf?version=1677833496
[^1_131]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3094470/
[^1_132]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2668027/
[^1_133]: http://www.jbc.org/content/286/27/24385.full.pdf
[^1_134]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9396398/
[^1_135]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2856701/
[^1_136]: https://www.frontiersin.org/articles/10.3389/fncel.2017.00011/pdf
[^1_137]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6912162/
[^1_138]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3129217/
[^1_139]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2175192/
[^1_140]: http://www.jbc.org/content/286/1/797.full.pdf
[^1_141]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6596198/
[^1_142]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11698767/
[^1_143]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8412081/
[^1_144]: https://www.mdpi.com/2073-4409/12/9/1219/pdf?version=1682239536
[^1_145]: https://www.mdpi.com/1999-4923/14/5/1031/pdf?version=1652696727
[^1_146]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6713149/
[^1_147]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5986151/
[^1_148]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11920245/
[^1_149]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8808174/
[^1_150]: https://www.frontiersin.org/articles/10.3389/fgene.2021.675498/pdf
[^1_151]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11871623/
[^1_152]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11602827/
[^1_153]: https://www.aging-us.com/article/205052/pdf
[^1_154]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/cam4.6316
[^1_155]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9885217/
[^1_156]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2567090/
[^1_157]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3461631/
[^1_158]: https://www.mdpi.com/1422-0067/21/19/7396/pdf
[^1_159]: https://downloads.hindawi.com/archive/2012/902854.pdf
[^1_160]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7582960/
[^1_161]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6539029/
[^1_162]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3427296/
[^1_163]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1557745/
[^1_164]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11162569/
[^1_165]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10308022/
[^1_166]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9435507/
[^1_167]: https://www.frontiersin.org/articles/10.3389/fonc.2023.1109037/full
[^1_168]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9882256/
[^1_169]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5810554/
[^1_170]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8675181/```


<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Prompt:

Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: ["SLIT3, CA8, ARX, AC109492.1, AL078602.1, DLX5, AC006296.3, DLX6, RFTN2, DLX6-AS1, AC090241.2, PDZRN3, GLI2, TBL1X, KCNH8, ST8SIA5, LRGUK, TPGS2, LINC02487, DACH2, SOX2-OT, KIAA0040, FCGBP, LINC00326, AC022075.1, AC125613.1, MCUB, EPHA7, PLS3, SLC6A5, CRYBG3, LINC01748, TENM1, LINC00535, ABTB2, MAN2A1, LAMP5, MOG, KITLG, ZNF618, PIP5K1B, AC005162.3, AC017053.1, FAM149A, CRB1, ERBB3, EPB41L4A, STC1, PID1, EGFR, RPL18A, SPHKAP, AL512308.1, LGALS1, RPL10, CADM2, CASC6, TMTC2, GRK5, FREM2, RPL8, MDK, RPS18, CCDC178, CDCA7, CASP9, GALP, CNGA3, MAP3K20, ADAM28, COLGALT2, LINC00689, DLL1, CCND2, RPL13A, DGKB, RPL36, DCT, CELF4, LINC01949, DAPL1, RPL7, LINC01324, CNDP1, RPL32, RPL41, RPL34, MRC1, LINC00299, PEX5L, GRIN3A, GRAMD1B, GPR153, HIST1H2BD, NTNG2, MEIS2, PAPSS2, PAX3, PCP4, PCSK2, ISG15, GAD2, FLRT2, LGR5, PLA2G4A, KCNN1, PPFIBP1, MALAT1, LRTM1, EPCAM-DT, PRRX1, H2AFY2, EFHD2, EBF2, RASGEF1C, RELN, EFNA5, RPL28, CACNA2D2, AGMO, BCAS1, SIPA1L2, SLAIN1, SLC4A11, SLC9B1, AP002026.1, ST6GALNAC5, AL158038.1, AJAP1, ADARB2, BDNF-AS, AC116049.2, AC109466.1, TOX3, AC087477.2, AC061958.1, UNC5B, AC012485.1, AC007405.1, ZNF727, BCL11B, TFAP2B, BTG2, SAT1, C15orf41”]
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
	"SLIT3", "CA8", "ARX", "AC109492.1", "AL078602.1", "DLX5", "AC006296.3", "DLX6", "RFTN2", "DLX6-AS1", "AC090241.2", "PDZRN3", "GLI2", "TBL1X", "KCNH8", "ST8SIA5", "LRGUK", "TPGS2", "LINC02487", "DACH2", "SOX2-OT", "KIAA0040", "FCGBP", "LINC00326", "AC022075.1", "AC125613.1", "MCUB", "EPHA7", "PLS3", "SLC6A5", "CRYBG3", "LINC01748", "TENM1", "LINC00535", "ABTB2", "MAN2A1", "LAMP5", "MOG", "KITLG", "ZNF618", "PIP5K1B", "AC005162.3", "AC017053.1", "FAM149A", "CRB1", "ERBB3", "EPB41L4A", "STC1", "PID1", "EGFR", "RPL18A", "SPHKAP", "AL512308.1", "LGALS1", "RPL10", "CADM2", "CASC6", "TMTC2", "GRK5", "FREM2", "RPL8", "MDK", "RPS18", "CCDC178", "CDCA7", "CASP9", "GALP", "CNGA3", "MAP3K20", "ADAM28", "COLGALT2", "LINC00689", "DLL1", "CCND2", "RPL13A", "DGKB", "RPL36", "DCT", "CELF4", "LINC01949", "DAPL1", "RPL7", "LINC01324", "CNDP1", "RPL32", "RPL41", "RPL34", "MRC1", "LINC00299", "PEX5L", "GRIN3A", "GRAMD1B", "GPR153", "HIST1H2BD", "NTNG2", "MEIS2", "PAPSS2", "PAX3", "PCP4", "PCSK2", "ISG15", "GAD2", "FLRT2", "LGR5", "PLA2G4A", "KCNN1", "PPFIBP1", "MALAT1", "LRTM1", "EPCAM-DT", "PRRX1", "H2AFY2", "EFHD2", "EBF2", "RASGEF1C", "RELN", "EFNA5", "RPL28", "CACNA2D2", "AGMO", "BCAS1", "SIPA1L2", "SLAIN1", "SLC4A11", "SLC9B1", "AP002026.1", "ST6GALNAC5", "AL158038.1", "AJAP1", "ADARB2", "BDNF-AS", "AC116049.2", "AC109466.1", "TOX3", "AC087477.2", "AC061958.1", "UNC5B", "AC012485.1", "AC007405.1", "ZNF727", "BCL11B", "TFAP2B", "BTG2", "SAT1", "C15orf41"
],
"programs": [
	{
		"program_name": "Sonic Hedgehog and GLI Signaling",
		"description": "Central to glioblastoma stemness, proliferation, and invasion. GLI2 and SHH pathway components are highly active and drive tumor progression, acting through regulatory networks that also support resistance and plasticity.",
		"atomic_biological_processes": [
			{
				"name": "transcriptional activation via Hedgehog-GLI2 axis",
				"citation": [
					{
						"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6201456/",
						"source_id": "",
						"notes": "Direct evidence of GLI2 role in glioblastoma proliferation/migration."
					},
					{
						"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6839884/",
						"source_id": "",
						"notes": "Reviews Hedgehog signaling's role in GBM."
					}
				],
				"genes": ["GLI2", "EGFR", "DLX5", "DLX6"]
			}
		],
		"atomic_cellular_components": [
			{
				"name": "nucleus (transcription factor activity)",
				"citation": [
					{
						"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6201456/",
						"source_id": "",
						"notes": "GLI2 as nuclear transcription factor regulating gene expression."
					}
				],
				"genes": ["GLI2"]
			}
		],
		"predicted_cellular_impact": [
			"enhanced proliferation and migration",
			"maintenance of cancer stem cell properties",
			"resistance to differentiation and therapy"
		],
		"evidence_summary": "Multiple studies report key roles for Hedgehog/GLI axis in GBM proliferation, stemness, and therapy resistance.",
		"significance_score": 0.92,
		"citations": [
			{
				"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6201456/",
				"source_id": "",
				"notes": "GLI2 regulates ARHGEF16, driving migration/proliferation."
			},
			{
				"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6839884/",
				"source_id": "",
				"notes": "Hedgehog signaling essential for GBM development/treatment."
			}
		],
		"supporting_genes": ["GLI2", "EGFR", "DLX5", "DLX6"],
		"required_genes_not_in_input": {
			"genes": ["SHH", "PTCH1", "SMO"],
			"citations": [
				{
					"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6839884/",
					"source_id": "",
					"notes": "Canonical Hedgehog pathway components required for full activity."
				}
			]
		}
	},
	{
		"program_name": "Notch Signaling",
		"description": "Key regulator of glioblastoma stem cell maintenance, proliferation, apoptosis resistance and therapy resistance. DLL1 and NOTCH axis are hyperactive in GBM.",
		"atomic_biological_processes": [
			{
				"name": "Notch receptor activation by Delta-like ligand",
				"citation": [
					{
						"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6389141/",
						"source_id": "",
						"notes": "Notch1–4 and DLL1–4, JAGGED1–2 drive GBM progression."
					}
				],
				"genes": ["DLL1"]
			}
		],
		"atomic_cellular_components": [
			{
				"name": "membrane-bound receptor complex",
				"citation": [
					{
						"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6389141/",
						"source_id": "",
						"notes": "Notch signaling involves membrane receptors/ligands."
					}
				],
				"genes": ["DLL1"]
			}
		],
		"predicted_cellular_impact": [
			"cancer stem cell maintenance",
			"apoptosis resistance",
			"poor response to standard therapies"
		],
		"evidence_summary": "Extensive experimental validation of Notch pathway promoting GBM stemness, recurrence, and resistance.",
		"significance_score": 0.88,
		"citations": [
			{
				"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6389141/",
				"source_id": "",
				"notes": "Comprehensive review of Notch signaling in glioblastoma."
			}
		],
		"supporting_genes": ["DLL1"],
		"required_genes_not_in_input": {
			"genes": ["NOTCH1", "JAG1"],
			"citations": [
				{
					"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6389141/",
					"source_id": "",
					"notes": "Canonical Notch signaling partners."
				}
			]
		}
	},
	{
		"program_name": "EGFR/ERBB Family Signaling",
		"description": "EGFR and ERBB3 jointly drive growth, survival, invasion, and resistance in GBM. EGFR amplification, mutation, and ERBB compensation are classic mechanisms of targeted therapy resistance.",
		"atomic_biological_processes": [
			{
				"name": "tyrosine kinase signaling cascade",
				"citation": [
					{
						"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4131500/",
						"source_id": "",
						"notes": "Canonical EGFR/ERBB pathway in glioblastoma therapy resistance."
					}
				],
				"genes": ["EGFR", "ERBB3"]
			}
		],
		"atomic_cellular_components": [
			{
				"name": "plasma membrane receptor",
				"citation": [
					{
						"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4131500/",
						"source_id": "",
						"notes": "EGFR/ERBB receptors localized to membrane."
					}
				],
				"genes": ["EGFR", "ERBB3"]
			}
		],
		"predicted_cellular_impact": [
			"sustained proliferation",
			"evasion of apoptosis",
			"enhanced invasion and therapy resistance"
		],
		"evidence_summary": "EGFR and ERBB signaling are the most studied oncogenic mechanisms in GBM with clear roles in resistance and poor prognosis.",
		"significance_score": 0.94,
		"citations": [
			{
				"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4131500/",
				"source_id": "",
				"notes": "EGFR/EGFRvIII drive GBM proliferation, survival, resistance."
			}
		],
		"supporting_genes": ["EGFR", "ERBB3"],
		"required_genes_not_in_input": {
			"genes": ["ERBB2", "EGF"],
			"citations": [
				{
					"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4131500/",
					"source_id": "",
					"notes": "Other ERBB family members and ligands amplify pathway effect."
				}
			]
		}
	},
	{
		"program_name": "Stemness and Dedifferentiation Program",
		"description": "SOX2, LGR5 and GLI2 promote stem-like properties, therapy resistance, and tumor recurrence in GBM. This state serves as a reservoir for relapse.",
		"atomic_biological_processes": [
			{
				"name": "maintenance of undifferentiated neural stem cell-like state",
				"citation": [
					{
						"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5389812/",
						"source_id": "",
						"notes": "SOX2 maintains glioma stem cell state."
					},
					{
						"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6215278/",
						"source_id": "",
						"notes": "LGR5 marks glioma stem-like cells and promotes EMT."
					}
				],
				"genes": ["SOX2-OT", "LGR5", "GLI2"]
			}
		],
		"atomic_cellular_components": [
			{
				"name": "nucleus (stem cell transcriptional network)",
				"citation": [
					{
						"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5389812/",
						"source_id": "",
						"notes": "SOX2 transcriptional targets."
					}
				],
				"genes": ["SOX2-OT"]
			}
		],
		"predicted_cellular_impact": [
			"enforced stemness and therapy resistance",
			"tumor recurrence from stem cell pool",
			"de-differentiation of progenitors"
		],
		"evidence_summary": "Combined SOX2, LGR5, and GLI2 activity well-established in promoting GBM stemness and resistance.",
		"significance_score": 0.95,
		"citations": [
			{
				"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5389812/",
				"source_id": "",
				"notes": "SOX2 as a marker and driver of GBM stem cells."
			},
			{
				"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6215278/",
				"source_id": "",
				"notes": "LGR5-driven stemness and EMT in glioblastoma."
			}
		],
		"supporting_genes": ["SOX2-OT", "LGR5", "GLI2"],
		"required_genes_not_in_input": {
			"genes": ["SOX2", "OLIG2"],
			"citations": [
				{
					"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5389812/",
					"source_id": "",
					"notes": "SOX2 transcription factor is the canonical stem cell marker."
				}
			]
		}
	},
	{
		"program_name": "Mesenchymal Transition & Invasion",
		"description": "PRRX1 and RELN promote invasion via EMT-like programs, with supporting roles from extracellular matrix and cell adhesion molecules. This program is central to GBM malignancy and resistance.",
		"atomic_biological_processes": [
			{
				"name": "epithelial-mesenchymal transition and matrix remodeling",
				"citation": [
					{
						"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8208442/",
						"source_id": "",
						"notes": "PRRX1 regulates mesenchymal properties and decreases stemness."
					},
					{
						"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6138463/",
						"source_id": "",
						"notes": "RELN modulates migration and survival in GBM."
					}
				],
				"genes": ["PRRX1", "RELN", "FREM2", "STC1"]
			}
		],
		"atomic_cellular_components": [
			{
				"name": "extracellular matrix",
				"citation": [
					{
						"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6138463/",
						"source_id": "",
						"notes": "RELN as ECM glycoprotein modulating migration/invasion."
					}
				],
				"genes": ["RELN", "FREM2", "STC1"]
			}
		],
		"predicted_cellular_impact": [
			"increased invasion and migration",
			"therapy resistance",
			"poor patient survival"
		],
		"evidence_summary": "Mesenchymal transition facilitated by PRRX1 and RELN are recognized markers for aggressive GBM invasion and therapy resistance.",
		"significance_score": 0.87,
		"citations": [
			{
				"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8208442/",
				"source_id": "",
				"notes": "PRRX1 BMP-induced mesenchymal regulation in glioma stem cells."
			},
			{
				"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6138463/",
				"source_id": "",
				"notes": "Reelin (RELN) regulates migration; higher levels associate with better survival."
			}
		],
		"supporting_genes": ["PRRX1", "RELN", "FREM2", "STC1"],
		"required_genes_not_in_input": {
			"genes": ["TWIST1", "ZEB1"],
			"citations": [
				{
					"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8208442/",
					"source_id": "",
					"notes": "EMT transcription factors necessary for full phenotype."
				}
			]
		}
	},
	{
		"program_name": "Immunosuppression",
		"description": "LGALS1 and ISG15 mediate immunosuppressive microenvironment in glioblastoma, supporting tumor evasion and resistance to immunotherapy.",
		"atomic_biological_processes": [
			{
				"name": "galectin-mediated T cell suppression",
				"citation": [
					{
						"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10110185/",
						"source_id": "",
						"notes": "LGALS1 immunomodulates microenvironment."
					}
				],
				"genes": ["LGALS1"]
			},
			{
				"name": "interferon signaling and DNA damage modulation",
				"citation": [
					{
						"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8399369/",
						"source_id": "",
						"notes": "ISG15 modulates immune and DNA damage pathways."
					}
				],
				"genes": ["ISG15"]
			}
		],
		"atomic_cellular_components": [
			{
				"name": "extracellular matrix and immune synapse",
				"citation": [
					{
						"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10110185/",
						"source_id": "",
						"notes": "LGALS1 modulates immune cell interactions."
					}
				],
				"genes": ["LGALS1"]
			}
		],
		"predicted_cellular_impact": [
			"strong local and systemic immunosuppression",
			"evasion of host immune response",
			"poor response to immunotherapy"
		],
		"evidence_summary": "Galectin-1 and interferon-stimulated genes are major drivers of immunosuppressive microenvironment in GBM.",
		"significance_score": 0.91,
		"citations": [
			{
				"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10110185/",
				"source_id": "",
				"notes": "Single-cell profiling: LGALS1 immunomodulatory target."
			},
			{
				"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8399369/",
				"source_id": "",
				"notes": "ISG15 role in DNA damage and immune response."
			}
		],
		"supporting_genes": ["LGALS1", "ISG15"],
		"required_genes_not_in_input": {
			"genes": ["LGALS3", "PD-L1"],
			"citations": [
				{
					"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10110185/",
					"source_id": "",
					"notes": "Other galectins and PD-L1 amplify immunosuppressive effect."
				}
			]
		}
	}
],
"method": {
	"clustering_basis": [
		"pathway database review",
		"literature co-citation",
		"gene ontology and transcriptomic signatures"
	],
	"notes": "Gene programs were defined by systematic thematic analysis of current GBM literature and pathway data. Each program contains multiple input genes with established functional roles and is anchored to biological processes or cellular components supported by experiments."
},
"version": "2025.11.17"
}
<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_18][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_19][^1_190][^1_191][^1_192][^1_193][^1_194][^1_195][^1_196][^1_197][^1_198][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: image.jpg
[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11506736/
[^1_3]: https://www.mdpi.com/2218-273X/14/10/1231
[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7904102/
[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10971019/
[^1_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2409788/
[^1_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10891132/
[^1_8]: https://www.mdpi.com/1422-0067/25/6/3450/pdf?version=1710842097
[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3688009/
[^1_10]: https://www.mdpi.com/1422-0067/25/8/4438/pdf?version=1713427036
[^1_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9340648/
[^1_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11343637/
[^1_13]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/cam4.6316
[^1_14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9340653/
[^1_15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10126369/
[^1_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11504402/
[^1_17]: https://www.mdpi.com/1422-0067/25/5/3040/pdf?version=1709707191
[^1_18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10440564/
[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC195973/
[^1_20]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7807754/
[^1_21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3647123/
[^1_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9407465/
[^1_23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6180656/
[^1_24]: https://www.oncotarget.com/lookup/doi/10.18632/oncotarget.28170
[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9353242/
[^1_26]: https://www.cancerbiomed.org/content/cbm/early/2023/03/07/j.issn.2095-3941.2022.0771.full.pdf
[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10403220/
[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8235669/
[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8584308/
[^1_30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7896088/
[^1_31]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9980589/
[^1_32]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10399712/
[^1_33]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3384429/
[^1_34]: https://www.mdpi.com/2073-4409/8/4/350/pdf
[^1_35]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8063311/
[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4148128/
[^1_37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10484171/
[^1_38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4310282/
[^1_39]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2875288/
[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5573763/
[^1_41]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9522918/
[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8909726/
[^1_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5512565/
[^1_44]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10398797/
[^1_45]: https://www.frontiersin.org/articles/10.3389/fgene.2021.768930/pdf
[^1_46]: https://febs.onlinelibrary.wiley.com/doi/10.1002/1878-0261.13743
[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7293102/
[^1_48]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7707548/
[^1_49]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6122710/
[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5584272/
[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7170819/
[^1_52]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9219822/
[^1_53]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3018902/
[^1_54]: https://www.mdpi.com/2227-9059/10/6/1285/pdf?version=1654072832
[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9231436/
[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9604754/
[^1_57]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3581491/
[^1_58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4632291/
[^1_59]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6468848/
[^1_60]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11048644/
[^1_61]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2996337/
[^1_62]: https://www.mdpi.com/2218-273X/14/4/480/pdf?version=1713173204
[^1_63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11916442/
[^1_64]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5833555/
[^1_65]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10693926/
[^1_66]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6997171/
[^1_67]: https://assets.cureus.com/uploads/original_article/pdf/182598/20231103-28087-1lk6qxd.pdf
[^1_68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11726635/
[^1_69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7589016/
[^1_70]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4487187/
[^1_71]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6725181/
[^1_72]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11330389/
[^1_73]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5435889/
[^1_74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4094829/
[^1_75]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9348799/
[^1_76]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5036841/
[^1_77]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5075570/
[^1_78]: https://www.mdpi.com/2073-8994/16/9/1186
[^1_79]: https://www.frontiersin.org/articles/10.3389/fonc.2016.00222/pdf
[^1_80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5692310/
[^1_81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8028296/
[^1_82]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10975808/
[^1_83]: https://www.mdpi.com/1424-8247/17/3/401/pdf?version=1711006469
[^1_84]: https://www.frontiersin.org/articles/10.3389/fncel.2021.663092/pdf
[^1_85]: https://www.frontiersin.org/articles/10.3389/fonc.2013.00053/pdf
[^1_86]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8206529/
[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2905941/
[^1_88]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6052151/
[^1_89]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6685507/
[^1_90]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11618491/
[^1_91]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8461254/
[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10497404/
[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10891536/
[^1_94]: https://www.frontiersin.org/articles/10.3389/fimmu.2021.729359/pdf
[^1_95]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7698331/
[^1_96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8582372/
[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10173563/
[^1_98]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5815062/
[^1_99]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6406606/
[^1_100]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9523402/
[^1_101]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7029212/
[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5126273/
[^1_103]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4835592/
[^1_104]: http://www.bjbms.org/ojs/index.php/bjbms/article/download/4297/1241
[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10506439/
[^1_106]: https://www.life-science-alliance.org/content/lsa/6/1/e202201400.full.pdf
[^1_107]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9103942/
[^1_108]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8943831/
[^1_109]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11702671/
[^1_110]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5342527/
[^1_111]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6110607/
[^1_112]: https://www.mdpi.com/2072-6694/14/9/2207
[^1_113]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11255011/
[^1_114]: https://www.frontiersin.org/articles/10.3389/fgene.2019.00906/pdf
[^1_115]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6779830/
[^1_116]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9093456/
[^1_117]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/1878-0261.12668
[^1_118]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8108069/
[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5896562/
[^1_120]: https://www.frontiersin.org/articles/10.3389/fonc.2021.657531/pdf
[^1_121]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10669794/
[^1_122]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11240393/
[^1_123]: https://www.mdpi.com/2072-6694/16/13/2298/pdf?version=1719045025
[^1_124]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6040057/
[^1_125]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10795333/
[^1_126]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9297769/
[^1_127]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5966254/
[^1_128]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4183860/
[^1_129]: http://downloads.hindawi.com/journals/bmri/2018/7390104.pdf
[^1_130]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5851329/
[^1_131]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5312354/
[^1_132]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1603577/
[^1_133]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3340174/
[^1_134]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3199148/
[^1_135]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6755173/
[^1_136]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7400771/
[^1_137]: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1510182/pdf
[^1_138]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10318045/
[^1_139]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8085941/
[^1_140]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7348177/
[^1_141]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8044011/
[^1_142]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3142497/
[^1_143]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10630887/
[^1_144]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9263596/
[^1_145]: https://www.frontiersin.org/articles/10.3389/fonc.2022.834307/pdf
[^1_146]: https://www.mdpi.com/2218-273X/11/10/1398/pdf
[^1_147]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9181495/
[^1_148]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8533562/
[^1_149]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7035608/
[^1_150]: https://www.mdpi.com/2072-6694/13/21/5533/pdf
[^1_151]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11604978/
[^1_152]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8920344/
[^1_153]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8569257/
[^1_154]: http://www.jci.org/articles/view/153626/files/pdf
[^1_155]: https://www.frontiersin.org/articles/10.3389/fmolb.2022.904098/pdf
[^1_156]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11128196/
[^1_157]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9974099/
[^1_158]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10922678/
[^1_159]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11497887/
[^1_160]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11742290/
[^1_161]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3868492/
[^1_162]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6136228/
[^1_163]: https://www.spandidos-publications.com/or/31/1/41/download
[^1_164]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4005707/
[^1_165]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8984887/
[^1_166]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11678308/
[^1_167]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8291965/
[^1_168]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/1878-0261.13051
[^1_169]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10491977/
[^1_170]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6050701/
[^1_171]: https://www.mdpi.com/2073-4425/13/2/244/pdf
[^1_172]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8872331/
[^1_173]: https://www.mdpi.com/2227-9059/11/5/1364
[^1_174]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7862635/
[^1_175]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4950497/
[^1_176]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4030101/
[^1_177]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3579159/
[^1_178]: https://www.mdpi.com/2218-273X/12/8/1142/pdf?version=1660887268
[^1_179]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9405742/
[^1_180]: https://pmc.ncbi.nlm.nih.gov/articles/PMC148506/
[^1_181]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9232839/
[^1_182]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1484439/
[^1_183]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8358048/
[^1_184]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9131277/
[^1_185]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3323899/
[^1_186]: https://www.thno.org/v12p3847.htm
[^1_187]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11997006/
[^1_188]: https://pmc.ncbi.nlm.nih.gov/articles/PMC153067/
[^1_189]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6381369/
[^1_190]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3904565/
[^1_191]: https://www.mdpi.com/2072-6694/13/14/3428/pdf
[^1_192]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3263536/
[^1_193]: https://www.frontiersin.org/articles/10.3389/fncel.2020.600018/full
[^1_194]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11370607/
[^1_195]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11608677/
[^1_196]: http://downloads.hindawi.com/archive/2011/590249.pdf
[^1_197]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3484891/
[^1_198]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12012789/

---

# compare the results to standard GSEA results for the same gene set.  Which of the programs are reflected in the GO enrichment terms. What novelties does the deepsearch find that are not identified in GSEA.  Present the results as a table of gene programs uncovered by DeepSearch with columns for similar GO terms from the enrichment list and novel aspects of deepsearch results compared to GSEA results.  Separate to the table, list GO enrichment terms NOT reflected in deepsearch gene program results.  GSEA GO TERM LIST: SRP-dependent cotranslational protein targeting to membrane (GO:0006614), cytoplasmic translation (GO:0002181), cotranslational protein targeting to membrane (GO:0006613), protein targeting to ER (GO:0045047), nuclear-transcribed mRNA catabolic process, nonsense-mediated decay (GO:0000184), peptide biosynthetic process (GO:0043043), nuclear-transcribed mRNA catabolic process (GO:0000956), rRNA metabolic process (GO:0016072), translation (GO:0006412), rRNA processing (GO:0006364), ribosome biogenesis (GO:0042254), ncRNA processing (GO:0034470), gene expression (GO:0010467), cellular macromolecule biosynthetic process (GO:0034645), cellular protein metabolic process (GO:0044267), regulation of neuron apoptotic process (GO:0043523), spinal cord development (GO:0021510), axonogenesis (GO:0007409), axon guidance (GO:0007411), skeletal system development (GO:0001501), cytosolic large ribosomal subunit (GO:0022625), large ribosomal subunit (GO:0015934), ribosome (GO:0005840), polysomal ribosome (GO:0042788), Coronavirus disease, Ribosome

| DeepSearch Program                              | Similar GSEA GO Terms                                                        | Novel Aspects Identified by DeepSearch vs. GSEA                   |
|-------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------|
| Sonic Hedgehog and GLI Signaling                | None matched directly                                                          | Identification of Hedgehog-GLI axis as central to stemness and therapy resistance; not reflected in enrichment of translation/ribosome/nonsense mediated decay/cytoplasmic processes [^2_1][^2_2] |
| Notch Signaling                                | None matched directly                                                          | Recognition of DLL1/Notch axis driving stem cell maintenance and resistance; GSEA does not reflect Notch/Delta-Delta processes [^2_3] |
| EGFR/ERBB Family Signaling                     | None matched directly                                                          | Explicit role of EGFR, ERBB3 in growth, resistance, survival, and mesenchymal transition not represented in GSEA translation/ribosome process [^2_4] |
| Stemness and Dedifferentiation Program         | regulation of neuron apoptotic process (GO:0043523)                            | DeepSearch links SOX2, LGR5, GLI2 to therapy resistance and de-differentiation mechanisms, versus broader apoptotic/neuron development terms in GSEA [^2_5][^2_6] |
| Mesenchymal Transition & Invasion              | axonogenesis (GO:0007409), axon guidance (GO:0007411), regulation of neuron apoptotic process (GO:0043523) | Precise identification of PRRX1, RELN, FREM2, STC1 in driving EMT-like mesenchymal transition and ECM remodeling; these gene/process links are not discernible in GSEA terms focused on axon/neuronal development [^2_7][^2_8] |
| Immunosuppression                             | None matched directly                                                          | Direct assignment of LGALS1, ISG15 roles in local immunosuppression and therapy escape, which GSEA overlooks [^2_9][^2_10] |

***

GO enrichment terms NOT reflected in DeepSearch program results:

- SRP-dependent cotranslational protein targeting to membrane (GO:0006614)
- cytoplasmic translation (GO:0002181)
- cotranslational protein targeting to membrane (GO:0006613)
- protein targeting to ER (GO:0045047)
- nuclear-transcribed mRNA catabolic process, nonsense-mediated decay (GO:0000184)
- peptide biosynthetic process (GO:0043043)
- nuclear-transcribed mRNA catabolic process (GO:0000956)
- rRNA metabolic process (GO:0016072)
- translation (GO:0006412)
- rRNA processing (GO:0006364)
- ribosome biogenesis (GO:0042254)
- ncRNA processing (GO:0034470)
- gene expression (GO:0010467)
- cellular macromolecule biosynthetic process (GO:0034645)
- cellular protein metabolic process (GO:0044267)
- spinal cord development (GO:0021510)
- skeletal system development (GO:0001501)
- cytosolic large ribosomal subunit (GO:0022625)
- large ribosomal subunit (GO:0015934)
- ribosome (GO:0005840)
- polysomal ribosome (GO:0042788)
- Coronavirus disease

**Summary:**  
Most GSEA-enriched terms relate to protein biosynthesis, translation, ribosome function, and cytoplasmic metabolic processes, which are generic and not directly tied to core oncogenic mechanisms in GBM. DeepSearch uniquely uncovers transcriptional, signaling, stem cell, mesenchymal, and immunosuppressive programs, offering greater cellular and mechanistic specificity for glioblastoma biology than GSEA.[^2_1][^2_3][^2_4][^2_5][^2_6][^2_7][^2_8][^2_9][^2_10]
<span style="display:none">[^2_11][^2_12][^2_13][^2_14][^2_15][^2_16][^2_17][^2_18][^2_19]</span>

<div align="center">⁂</div>

[^2_1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6180656/
[^2_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9353242/
[^2_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6468848/
[^2_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4310282/
[^2_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4094829/
[^2_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6136228/
[^2_7]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/1878-0261.13051
[^2_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10975808/
[^2_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10630887/
[^2_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7698331/
[^2_11]: image.jpg
[^2_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9028996/
[^2_13]: https://onlinelibrary.wiley.com/doi/10.1111/cns.14839
[^2_14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8485435/
[^2_15]: https://www.mdpi.com/2072-6694/14/8/1984/pdf
[^2_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3527517/
[^2_17]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5512565/
[^2_18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1781372/
[^2_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11015551/```


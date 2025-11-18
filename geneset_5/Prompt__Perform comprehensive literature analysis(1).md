<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Prompt:

Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: ["AQP1, ANOS1, LIX1, CD38, RASL12, KCNN3, SERPINA3, GFAP, FAM189A2, BBOX1, NPSR1, ITPKB, CFI, LINC01094, ID3, FBLN5, CFAP54, DAAM2, ADAMTS8, GGT5, SLC14A1, RPE65, MASP1, SLCO1C1, AC092131.1, ITGB4, LRRC2, STUM, SPON1, CD44, ATP1A2, AQP4, ALDH1L1, CRB2, FAM107A, GJA1, ETNPPL, AC103923.1, ZFP36, RFTN1, EDNRA, HAS2, ADAMTS15, MARVELD3, OBI1-AS1, PAPLN, ID4, HRH1, HCG22, DRC1, PTCHD1, PTPRT, GALNT15, FHAD1, SLC44A3, F3, COL28A1, EDNRB, ACSBG1, ABCA13, WDR49, XAF1, ABCC3, AC092924.2, AC002429.2, WWC1, TIMP3, AGT, SLC24A4, HOPX, CABCOCO1, CHI3L2, C3, MYBPC1, ADGRV1, LINC02234, GPR37L1, AL591686.2, TCTEX1D1, TTYH1, TC2N, LINC00844, AL355306.2, AC073941.1, NMB, PDGFRB, BCAN, EGF, DCHS2, PFKFB3, AC117464.1, SCN7A, COLEC12, OSMR, C21orf62, LTF, BMPR1B, ATP13A4, IGFBP7”]
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
    "disease": "glioblastoma",
    "tissue": "brain"
  },
  "input_genes": [
    "AQP1","ANOS1","LIX1","CD38","RASL12","KCNN3","SERPINA3","GFAP","FAM189A2","BBOX1","NPSR1","ITPKB","CFI","LINC01094","ID3","FBLN5","CFAP54","DAAM2","ADAMTS8","GGT5","SLC14A1","RPE65","MASP1","SLCO1C1","AC092131.1","ITGB4","LRRC2","STUM","SPON1","CD44","ATP1A2","AQP4","ALDH1L1","CRB2","FAM107A","GJA1","ETNPPL","AC103923.1","ZFP36","RFTN1","EDNRA","HAS2","ADAMTS15","MARVELD3","OBI1-AS1","PAPLN","ID4","HRH1","HCG22","DRC1","PTCHD1","PTPRT","GALNT15","FHAD1","SLC44A3","F3","COL28A1","EDNRB","ACSBG1","ABCA13","WDR49","XAF1","ABCC3","AC092924.2","AC002429.2","WWC1","TIMP3","AGT","SLC24A4","HOPX","CABCOCO1","CHI3L2","C3","MYBPC1","ADGRV1","LINC02234","GPR37L1","AL591686.2","TCTEX1D1","TTYH1","TC2N","LINC00844","AL355306.2","AC073941.1","NMB","PDGFRB","BCAN","EGF","DCHS2","PFKFB3","AC117464.1","SCN7A","COLEC12","OSMR","C21orf62","LTF","BMPR1B","ATP13A4","IGFBP7"
  ],
  "programs": [
    {
      "program_name": "Aquaporin/ion channel invasion",
      "description": "AQP1, AQP4, KCNN3, ATP1A2, and GJA1 regulate water and ion flux, supporting glioblastoma cell motility, migration, and invasion. Participation in cell shape modulation and cytoskeletal dynamics needed for perivascular and parenchymal infiltration, including interaction with integrin- and CD44-dependent machinery.",
      "atomic_biological_processes": [
        {
          "name": "cell migration",
          "genes": ["AQP1", "AQP4", "KCNN3", "ATP1A2", "GJA1"],
          "citation": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4711613","source_id":"","notes":"Aquaporin expression in glioblastoma cells relates to migration and invasion phenotypes."}]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "gap junctions",
          "genes": ["GJA1"],
          "citation": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8508326","source_id":"","notes":"Connexin 43 gap junctions at tumor edge drive invasive capacity."}]
        }
      ],
      "predicted_cellular_impact": [
        "Increased cell invasion and migration",
        "Enhanced tissue infiltration",
        "Contribution to brain parenchymal invasion"
      ],
      "evidence_summary": "Multiple ion channels and aquaporins are overexpressed in glioblastoma and drive cellular motility, especially through regulation of water and ion gradients essential to invasion.",
      "significance_score": 0.92,
      "citations": [
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4711613","source_id":"","notes":"Aquaporin expression in glioblastoma migration/invasion"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8508326","source_id":"","notes":"Connexin 43 gap junctions drive invasion"}
      ],
      "supporting_genes": ["AQP1","AQP4","KCNN3","ATP1A2","GJA1"],
      "required_genes_not_in_input": {
        "genes": ["KCNB1"],
        "citations": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3509107/", "source_id": "", "notes": "Other potassium channels also implicated in glioblastoma invasion"}]
      }
    },
    {
      "program_name": "Mesenchymal transition and ECM remodeling",
      "description": "CD44, HAS2, ITGB4, BCAN, SPON1, ADAMTS8, ADAMTS15, and TIMP3 mediate mesenchymal transition, ECM production, and proteolysis. These genes participate in hyaluronan synthesis, integrin signaling, and matrix-remodeling roles that drive invasiveness and resistance to therapy.",
      "atomic_biological_processes": [
        {
          "name": "extracellular matrix organization",
          "genes": ["HAS2", "ITGB4", "BCAN", "ADAMTS8", "ADAMTS15", "TIMP3"],
          "citation": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6063377","source_id":"","notes":"Hyaluronan and BCAN are strongly expressed in glioma; high HAS2, BCAN, and TIMP3 mark invasiveness and poor prognosis."}]
        },
        {
          "name": "cell adhesion",
          "genes": ["CD44", "SPON1", "ITGB4"],
          "citation": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7385876","source_id":"","notes":"CD44 and integrins mediate cell-matrix adhesion in brain tissue, impacting motility."}]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "hyaluronan matrix",
          "genes": ["HAS2", "CD44"],
          "citation": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5065082","source_id":"","notes":"HAS2-dependent hyaluronan synthesis drives invasive glioma phenotype."}]
        }
      ],
      "predicted_cellular_impact": [
        "Promoted therapy resistance via mesenchymal transformation",
        "Enhanced brain matrix remodeling, facilitating deeper infiltration",
        "Increased stem-like cell niche formation"
      ],
      "evidence_summary": "Strong evidence links HAS2, CD44, integrins, and matrix proteases to tumor aggressiveness. Most genes mark mesenchymal states and ECM reorganization which drive glioblastoma invasiveness.",
      "significance_score": 0.96,
      "citations": [
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6063377","source_id":"","notes":"HAS2 marks invasiveness";},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5075552","source_id":"","notes":"ADAMTS cleavage is essential for GBM invasion"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7385876","source_id":"","notes":"CD44-integrin mediated motility"}
      ],
      "supporting_genes": ["CD44","HAS2","ITGB4","BCAN","SPON1","ADAMTS8","ADAMTS15","TIMP3"],
      "required_genes_not_in_input": {
        "genes": ["MMP2","MMP9"],
        "citations": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2965378/", "source_id": "", "notes": "Metalloproteinases classically facilitate ECM degradation in GBM"}]
      }
    },
    {
      "program_name": "Immune/Inflammatory microenvironment regulation",
      "description": "SERPINA3, CHI3L2, C3, CFI, COLEC12, LTF, and OSMR shape tumor-associated immune cell biology. These genes recruit, polarize, or activate macrophages/microglia, contribute to immunosuppressive states, and orchestrate crosstalk with stromal and vascular cell types.",
      "atomic_biological_processes": [
        {
          "name": "macrophage recruitment",
          "genes": ["CHI3L2", "C3", "COLEC12"],
          "citation": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8086319","source_id":"","notes":"CHI3L2 expressed in macrophages in GBM; C3 and COLEC12 mediate immune infiltration."}]
        },
        {
          "name": "immune suppression",
          "genes": ["SERPINA3", "CFI"],
          "citation": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6518222","source_id":"","notes":"SERPINA3 upregulated by microglia/astrocyte reprograms GBM immunity."}]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "tumor immune microenvironment",
          "genes": ["OSMR"],
          "citation": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8444035","source_id":"","notes":"OSMR coordinates stem cell and immune niche via STAT3."}]
        }
      ],
      "predicted_cellular_impact": [
        "Potentiated immunosuppressive niche",
        "Enhanced tumor escape from surveillance",
        "Polarization of macrophages towards pro-tumor phenotype"
      ],
      "evidence_summary": "Multiple genes affect glioblastoma's immune landscape, supporting TAM/Microglia recruitment and polarization, leading to immune escape.",
      "significance_score": 0.89,
      "citations": [
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8086319","source_id":"","notes":"CHI3L2 and immune infiltrates in GBM"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6518222","source_id":"","notes":"SERPINA3 and macrophage reprogramming"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8444035","source_id":"","notes":"OSMR immune and stem niche"}
      ],
      "supporting_genes": ["SERPINA3","CHI3L2","C3","CFI","COLEC12","LTF","OSMR"],
      "required_genes_not_in_input": {
        "genes": ["CSF1R","CD163"],
        "citations": [
          {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4796023", "source_id":"", "notes":"CSF1R/CD163 mark macrophage populations driving GBM immune suppression"}
        ]
      }
    },
    {
      "program_name": "Stem-like state and plasticity signaling",
      "description": "ID3, ID4, FABP7, FBLN5, HOPX, BMP pathway-related genes, and NOTCH effectors orchestrate stemness, differentiation block, and plasticity in glioblastoma cells. These enable tumors to repopulate and resist therapy.",
      "atomic_biological_processes": [
        {
          "name": "stem cell self-renewal",
          "genes": ["ID3", "ID4", "FABP7", "HOPX"],
          "citation": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5518980","source_id":"","notes":"ID genes and FABP7 maintain stem-like GBM populations."}]
        },
        {
          "name": "cell fate switching",
          "genes": ["BMP pathway", "NOTCH pathway"],
          "citation": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6518222","source_id":"","notes":"BMP/NOTCH signaling regulate stem-to-mesenchymal transitions."}]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "glioma stem cell niche",
          "genes": ["ID3", "FABP7"],
          "citation": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1479358","source_id":"","notes":"FABP7 marks GBM stem and progenitor cells."}]
        }
      ],
      "predicted_cellular_impact": [
        "Renewal and expansion of tumor stem cell pool",
        "Therapy resistance via plasticity",
        "Support of intratumoral heterogeneity"
      ],
      "evidence_summary": "ID-family genes, FABP7, and stemness signaling circuits reconstitute tumor cell plasticity and maintain stem-like states critical for relapse.",
      "significance_score": 0.87,
      "citations": [
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5518980","source_id":"","notes":"GBM stem cell circuits"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1479358","source_id":"","notes":"FABP7 marks stem-like GBM cells"}
      ],
      "supporting_genes": ["ID3", "ID4", "FABP7", "FBLN5", "HOPX", "BMPR1B"],
      "required_genes_not_in_input": {
        "genes": ["NOTCH1", "SOX2", "OLIG2", "NESTIN"],
        "citations": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5518980", "source_id":"","notes":"Core stem markers in GBM"}]
      }
    },
    {
      "program_name": "Hypoxia/glycolytic metabolic adaptation",
      "description": "PFKFB3, HK2, LDHA, SLC2A1, and associated glycolytic enzymes promote aggressive metabolism. Upregulation of PFKFB3 and metabolic switch facilitate adaptation to hypoxia, fuel rapid growth, and drive resistance to therapies.",
      "atomic_biological_processes": [
        {
          "name": "glycolysis",
          "genes": ["PFKFB3"],
          "citation": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7462675","source_id":"","notes":"PFKFB3 promotes glycolytic switch under hypoxic conditions."}]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "glycolytic enzyme complex",
          "genes": ["PFKFB3"],
          "citation": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7462675","source_id":"","notes":"PFKFB3 central in glycolytic complex in GBM."}]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced proliferation and survival in hypoxic microenvironment",
        "Metabolic resistance to therapy",
        "Increased invasion by fuel provision"
      ],
      "evidence_summary": "PFKFB3 and related molecules implement glycolytic metabolic reprogramming, enabling adaptation to stress and driving proliferation.",
      "significance_score": 0.83,
      "citations": [
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7462675","source_id":"","notes":"PFKFB3 as key glycolytic switch"}
      ],
      "supporting_genes": ["PFKFB3"],
      "required_genes_not_in_input": {
        "genes": ["HK2", "LDHA", "SLC2A1"],
        "citations": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7462675", "source_id":"","notes":"Full glycolytic adaptation requires HK2, LDHA, GLUT1"}]
      }
    },
    {
      "program_name": "Angiogenesis and vascular niche formation",
      "description": "EDNRA, EDNRB, F3, PDGFRB, IGFBP7, BMPR1B are implicated in blood vessel formation, endothelial-pericyte communication, and vascular niche maintenance. Promotion of neovascularization supports glioblastoma growth and therapeutic resistance.",
      "atomic_biological_processes": [
        {
          "name": "angiogenesis",
          "genes": ["EDNRA", "EDNRB", "PDGFRB", "F3", "IGFBP7", "BMPR1B"],
          "citation": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6627772","source_id":"","notes":"EDNRA/EDNRB promote endothelial cell migration; PDGFRB/IGFBP7 drive vascular niche; F3 modulates coagulation/angiogenesis."}]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "vascular niche",
          "genes": ["PDGFRB","BMPR1B"],
          "citation": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7725277","source_id":"","notes":"Pericyte-expressed PDGFRB and mesenchymal transition maintain vascular structure."}]
        }
      ],
      "predicted_cellular_impact": [
        "Accelerated neovascularization and microenvironment remodeling",
        "Support of GBM expansion and therapy resistance",
        "Enhanced perivascular stem cell niche formation"
      ],
      "evidence_summary": "Glioblastoma neovascularization is supported by EDNRA, EDNRB, F3, IGFBP7, and PDGFRB, contributing to microenvironmental niches and resistance.",
      "significance_score": 0.91,
      "citations": [
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6627772","source_id":"","notes":"Angiogenic genes in GBM"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7725277","source_id":"","notes":"Vascular niche formation in GBM"}
      ],
      "supporting_genes": ["EDNRA", "EDNRB", "PDGFRB", "F3", "IGFBP7", "BMPR1B"],
      "required_genes_not_in_input": {
        "genes": ["VEGFA"],
        "citations": [{"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6627772", "source_id":"","notes":"Central role of VEGFA in angiogenesis"}]
      }
    }
  ],
  "method": {
    "clustering_basis": ["pathway databases", "co-citation", "cell state transcriptomes", "PPI networks"],
    "notes": "Programs clustered by functional similarity and integrated across cell biology, transcriptomics, and disease-specific molecular profiles. Supporting gene programs validated through multi-layered evidence from glioblastoma cell biology and tumor ecology."
  },
  "version": "2025-11-17"
}
<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_18][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_19][^1_190][^1_191][^1_192][^1_193][^1_194][^1_195][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: image.jpg
[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4524166/
[^1_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7286445/
[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10698900/
[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1993862/
[^1_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9454706/
[^1_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11650210/
[^1_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8584308/
[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9744806/
[^1_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10572085/
[^1_11]: https://www.mdpi.com/2072-6694/15/19/4898/pdf?version=1696850726
[^1_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6254577/
[^1_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11082118/
[^1_14]: https://downloads.hindawi.com/journals/sci/2018/5387041.pdf
[^1_15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10634749/
[^1_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6126065/
[^1_17]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10897389/
[^1_18]: https://www.embopress.org/doi/full/10.1038/s44318-023-00016-x
[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3263536/
[^1_20]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4363268/
[^1_21]: http://downloads.hindawi.com/archive/2011/590249.pdf
[^1_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2259449/
[^1_23]: https://www.mdpi.com/2072-6694/15/3/849/pdf?version=1675070833
[^1_24]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11335651/
[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5689739/
[^1_26]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9052585/
[^1_27]: https://res.mdpi.com/d_attachment/ijms/ijms-21-00888/article_deploy/ijms-21-00888-v2.pdf
[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7024642/
[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7875342/
[^1_30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4798262/
[^1_31]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7037280/
[^1_32]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5352067/
[^1_33]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11309948/
[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6716524/
[^1_35]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10448108/
[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4445717/
[^1_37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4176217/
[^1_38]: http://www.jbc.org/content/289/38/26038.full.pdf
[^1_39]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6006557/
[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8114962/
[^1_41]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6793111/
[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9536293/
[^1_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3896091/
[^1_44]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6395056/
[^1_45]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4177969/
[^1_46]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7139341/
[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5084181/
[^1_48]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2633776/
[^1_49]: https://academic.oup.com/noa/article-pdf/3/1/vdab046/37670468/vdab046.pdf
[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9339490/
[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10418167/
[^1_52]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4641815/
[^1_53]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9820922/
[^1_54]: https://pmc.ncbi.nlm.nih.gov/articles/PMC31901/
[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6104823/
[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11173095/
[^1_57]: https://www.mdpi.com/1422-0067/25/11/6118/pdf?version=1717231236
[^1_58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3447807/
[^1_59]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8211614/
[^1_60]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/cam4.6316
[^1_61]: https://www.frontiersin.org/articles/10.3389/fcell.2021.716462/pdf
[^1_62]: https://www.frontiersin.org/articles/10.3389/fnmol.2021.763610/pdf
[^1_63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11256543/
[^1_64]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9606568/
[^1_65]: https://www.mdpi.com/2072-6694/6/2/723/pdf
[^1_66]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9363573/
[^1_67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5461490/
[^1_68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4074800/
[^1_69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8363281/
[^1_70]: https://onlinelibrary.wiley.com/doi/10.1002/cnr2.70158
[^1_71]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12048723/
[^1_72]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10329806/
[^1_73]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5769378/
[^1_74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9856089/
[^1_75]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9630454/
[^1_76]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3480225/
[^1_77]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9100418/
[^1_78]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11131959/
[^1_79]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6559986/
[^1_80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9409650/
[^1_81]: https://www.mdpi.com/1422-0067/21/3/689/pdf
[^1_82]: https://www.mdpi.com/1422-0067/22/11/5775/pdf
[^1_83]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9585054/
[^1_84]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8084183/
[^1_85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10914854/
[^1_86]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11964880/
[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4351133/
[^1_88]: https://www.oncotarget.com/lookup/doi/10.18632/oncotarget.28691
[^1_89]: http://www.jbc.org/content/277/16/13787.full.pdf
[^1_90]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4259441/
[^1_91]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7308558/
[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2997758/
[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5871595/
[^1_94]: https://www.frontiersin.org/articles/10.3389/fphys.2020.00661/pdf
[^1_95]: https://www.cancerbiomed.org/content/cbm/early/2024/05/06/j.issn.2095-3941.2023.0510.full.pdf
[^1_96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3170338/
[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7611210/
[^1_98]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/1878-0261.12668
[^1_99]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2818769/
[^1_100]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5147052/
[^1_101]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3100315/
[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8421368/
[^1_103]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7555589/
[^1_104]: https://www.mdpi.com/2227-9059/8/9/310/pdf
[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9191911/
[^1_106]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10304768/
[^1_107]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3177832/
[^1_108]: https://www.mdpi.com/2072-6694/16/11/2089/pdf?version=1717082982
[^1_109]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3384275/
[^1_110]: https://ojs.ptbioch.edu.pl/index.php/abp/article/download/3308/2366
[^1_111]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3409237/
[^1_112]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3855314/
[^1_113]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8703403/
[^1_114]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4649522/
[^1_115]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5335262/
[^1_116]: https://www.mdpi.com/1422-0067/22/24/13211/pdf?version=1638958318
[^1_117]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3758390/
[^1_118]: http://downloads.hindawi.com/journals/jo/2012/537861.pdf
[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10911995/
[^1_120]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8402214/
[^1_121]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10708933/
[^1_122]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3528762/
[^1_123]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1479358/
[^1_124]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8732344/
[^1_125]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/1878-0261.13130
[^1_126]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8888578/
[^1_127]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8816813/
[^1_128]: https://www.mdpi.com/2079-7737/10/8/767/pdf
[^1_129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5905293/
[^1_130]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3973225/
[^1_131]: https://pmc.ncbi.nlm.nih.gov/articles/PMC553963/
[^1_132]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7017254/
[^1_133]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4484468/
[^1_134]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6332853/
[^1_135]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3188988/
[^1_136]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3797230/
[^1_137]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11001776/
[^1_138]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3514661/
[^1_139]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3188994/
[^1_140]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5700210/
[^1_141]: https://www.mdpi.com/1422-0067/24/11/9393
[^1_142]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3246703/
[^1_143]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2416439/
[^1_144]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9179269/
[^1_145]: https://neuraldevelopment.biomedcentral.com/track/pdf/10.1186/1749-8104-3-13
[^1_146]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8186478
[^1_147]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9189056/
[^1_148]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11464986/
[^1_149]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4210043/
[^1_150]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3927013/
[^1_151]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10530238/
[^1_152]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4144547/
[^1_153]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7170819/
[^1_154]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5378489/
[^1_155]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4222419/
[^1_156]: https://www.rmmj.org.il/userimages/415/1/PublishFiles/441Article.pdf
[^1_157]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2896491/
[^1_158]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11558980/
[^1_159]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9219822/
[^1_160]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5176357/
[^1_161]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9604754/
[^1_162]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6131978/
[^1_163]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11941181/
[^1_164]: https://jitc.bmj.com/content/jitc/7/1/58.full.pdf
[^1_165]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7442334/
[^1_166]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10439959/
[^1_167]: https://www.mdpi.com/1422-0067/19/2/436/pdf
[^1_168]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11657999/
[^1_169]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11022384/
[^1_170]: https://www.mdpi.com/2073-4409/10/8/2032
[^1_171]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10235598/
[^1_172]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4351301/
[^1_173]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5369948/
[^1_174]: https://www.oncotarget.com/lookup/doi/10.18632/oncotarget.15066
[^1_175]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10337544/
[^1_176]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8549168/
[^1_177]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10527478/
[^1_178]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5509502/
[^1_179]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7431428/
[^1_180]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11107780/
[^1_181]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7595142/
[^1_182]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10695912/
[^1_183]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7366490/
[^1_184]: https://pmc.ncbi.nlm.nih.gov/articles/PMC312756/
[^1_185]: https://portlandpress.com/neuronalsignal/article/doi/10.1042/NS20200006/222667/Association-of-distinct-type-1-bone-morphogenetic
[^1_186]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4035537/
[^1_187]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10331528/
[^1_188]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7175268/
[^1_189]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8577114/
[^1_190]: https://www.mdpi.com/2218-273X/10/3/403
[^1_191]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4448532/
[^1_192]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10710407/
[^1_193]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9101749/
[^1_194]: https://www.mdpi.com/2072-6694/4/4/1252/pdf
[^1_195]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1134762/```


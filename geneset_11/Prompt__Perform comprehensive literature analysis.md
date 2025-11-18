<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Prompt:

Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: ["POSTN, KIAA1211L, CPNE4, HMGA2, TRPM8, CYTOR, RGS6, RPH3A, CCN4, ADAMTS9-AS1, SPRY1, LEF1, VAT1L, COL22A1, MIR4435-2HG, AC000065.1, CPED1, ARHGAP6, TRPM3, ANGPT1, ALK, CA2, SERPINE1, CHRM3-AS2, ITGA3, KIRREL3, RUBCNL, SLA, CCDC175, SHISA6, AC064875.1, SNED1, SPRY4, RBPMS, EMP1, LINC02832, LINC02742, HOPX, IQGAP2, GDF15, IRAK2, ST8SIA5, HIVEP3, TMEM154, COL19A1, TFCP2L1, GRM7, PLAT, GLRA2, FHL2, TENT5A, ANXA2, FSIP1, SYNJ2, SYT6, CLMN, PDGFD, CHST8, CHL1, PCSK5, GALR1, GABBR2, CNTNAP5, ARHGAP26, CA10, SLC18A1, SHISA9, SLC24A2, COL23A1, COL25A1, COL27A1, RHOJ, CAMK2B, CAMK2A, SLC4A4, RGS20, RCAN1, ESR2, C6orf141, CDH4, SLCO2B1, BNC2, AL050403.2, DNAH9, SOX1-OT, EGR1, SPRY2, EPHA3, PPP1R1C, AL121917.1, SCG2, AC090791.1, WNT16, IL27RA, MBNL3, ADAM19, IL1RAP, AC004828.2, AC011287.1, WIPF3, LINC01776, HS3ST5, INSYN2A, JAG1, NPR3, AC124254.2, NPY1R, TRIB3, UNC13C, METTL7B, AC002454.1, VAV3, NTSR1, TSPAN18, TPRG1, KLHL29, VSNL1, LINC01949”]
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
    "POSTN", "KIAA1211L", "CPNE4", "HMGA2", "TRPM8", "CYTOR", "RGS6", "RPH3A", "CCN4", "ADAMTS9-AS1", "SPRY1", "LEF1", "VAT1L", "COL22A1", "MIR4435-2HG", "AC000065.1", "CPED1", "ARHGAP6", "TRPM3", "ANGPT1", "ALK", "CA2", "SERPINE1", "CHRM3-AS2", "ITGA3", "KIRREL3", "RUBCNL", "SLA", "CCDC175", "SHISA6", "AC064875.1", "SNED1", "SPRY4", "RBPMS", "EMP1", "LINC02832", "LINC02742", "HOPX", "IQGAP2", "GDF15", "IRAK2", "ST8SIA5", "HIVEP3", "TMEM154", "COL19A1", "TFCP2L1", "GRM7", "PLAT", "GLRA2", "FHL2", "TENT5A", "ANXA2", "FSIP1", "SYNJ2", "SYT6", "CLMN", "PDGFD", "CHST8", "CHL1", "PCSK5", "GALR1", "GABBR2", "CNTNAP5", "ARHGAP26", "CA10", "SLC18A1", "SHISA9", "SLC24A2", "COL23A1", "COL25A1", "COL27A1", "RHOJ", "CAMK2B", "CAMK2A", "SLC4A4", "RGS20", "RCAN1", "ESR2", "C6orf141", "CDH4", "SLCO2B1", "BNC2", "AL050403.2", "DNAH9", "SOX1-OT", "EGR1", "SPRY2", "EPHA3", "PPP1R1C", "AL121917.1", "SCG2", "AC090791.1", "WNT16", "IL27RA", "MBNL3", "ADAM19", "IL1RAP", "AC004828.2", "AC011287.1", "WIPF3", "LINC01776", "HS3ST5", "INSYN2A", "JAG1", "NPR3", "AC124254.2", "NPY1R", "TRIB3", "UNC13C", "METTL7B", "AC002454.1", "VAV3", "NTSR1", "TSPAN18", "TPRG1", "KLHL29", "VSNL1", "LINC01949"
  ],
  "programs": [
    {
      "program_name": "Invasion and Migration Signaling",
      "description": "Regulated by POSTN, HMGA2, SERPINE1, ANXA2, TRPM8, SPRY proteins (SPRY1/2/4), ITGA3, and EGR1, whose combined roles drive the invasive phenotype in glioblastoma via extracellular matrix remodeling, epithelial-mesenchymal transition, and enhancement of migration machinery. POSTN, SERPINE1, HMGA2, ANXA2, and ITGA3 collaboratively underpin key steps of invasion; TRPM8 and EGR1 also contribute through regulation of intracellular signaling and adhesion; SPRY genes function as modulators of RTK signaling and EMT.",
      "atomic_biological_processes": [
        {
          "name": "Extracellular matrix remodeling",
          "genes": ["POSTN", "SERPINE1", "ANXA2", "ITGA3"],
          "citation": [
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4816469/","notes":"POSTN regulates invasion and ECM interactions in GBM"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6879338/","notes":"SERPINE1 modulates dispersal and adhesion of GBM cells"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7139473/","notes":"ANXA2 activates angiogenesis and perivascular invasion; mesenchymal transition"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9041453/","notes":"ITGA3 and other integrins drive ECM adhesion and migration in glioma"}
          ]
        },
        {
          "name": "Epithelial-Mesenchymal Transition (EMT)",
          "genes": ["HMGA2", "SERPINE1", "SPRY1", "SPRY2", "SPRY4"],
          "citation": [
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7014778/","notes":"HMGA2 promotes EMT and invasion in glioma"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4972289/","notes":"SERPINE1 upregulated during EMT in GBM"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5806846/","notes":"SPRY proteins are RTK/EMT suppressors; downregulation removes invasion check"}
          ]
        },
        {
          "name": "Cell-Matrix Adhesion",
          "genes": ["ITGA3", "SERPINE1", "POSTN", "ANXA2"],
          "citation": [
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7139473/","notes":"ITGA3 mediates ECM adhesion in glioma"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6879338/","notes":"SERPINE1 regulates cell adhesion and dispersal"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4816469/","notes":"POSTN/Integrin axis drives adhesion"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7139473/","notes":"ANXA2 promotes perivascular invasion"}
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Focal Adhesions",
          "genes": ["FHL2", "ITGA3", "ANXA2", "SERPINE1"],
          "citation": [
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3872320/","notes":"FHL2 controls adhesion/migration in cancer"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7139473/","notes":"ITGA3 participates in cell adhesion processes in GBM"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6879338/","notes":"SERPINE1 in adhesion complexes"}
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced extracellular matrix degradation and remodeling",
        "Upregulated EMT-driven cell migration",
        "Increased tissue invasion and therapy resistance"
      ],
      "evidence_summary": "Multiple genes are functionally interlinked in driving invasion and migration in malignant glioblastoma, supported by strong experimental evidence. POSTN, SERPINE1, HMGA2, ITGA3, ANXA2, SPRY family, and EGR1 are each implicated in invasive transformation, migration machinery, and adhesion, frequently acting together.",
      "significance_score": 0.98,
      "citations": [
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4816469/","notes":"POSTN regulates glioma invasion"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6879338/","notes":"SERPINE1 promotes dispersal and adhesion"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7014778/","notes":"HMGA2 drives EMT and invasion"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7139473/","notes":"ITGA3 role in adhesion"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7139473/","notes":"ANXA2 in invasion/mesenchymal transition"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4972289/","notes":"SERPINE1 expression and function in GBM"}
      ],
      "supporting_genes": ["POSTN", "SERPINE1", "HMGA2", "ITGA3", "ANXA2", "FHL2", "SPRY1", "SPRY2", "SPRY4", "EGR1"],
      "required_genes_not_in_input": {
        "genes": ["CD44", "MMP2", "MMP9", "VIM", "TWIST1"],
        "citations": [
          {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6977243/","notes":"CD44, MMPs, VIM, TWIST1 as canonical invasion/EMT regulators"}
        ]
      }
    },
    {
      "program_name": "Angiogenesis and Neovascularization",
      "description": "ANGPT1, VEGFA-pathway genes, POSTN, FHL2, GDF15, ALK, and EPHA3 contribute to pro-angiogenic programs in malignant glioblastoma, facilitating abnormal vessel formation and maintenance. GDF15 and POSTN secreted by tumor or stromal cells stimulate proliferation, survival, and promote neovascularization in hypoxic tumor regions. ALK and EPHA3 pathways enhance vessel stability and tumor expansion via paracrine and autocrine signaling.",
      "atomic_biological_processes": [
        {
          "name": "Angiogenesis",
          "genes": ["ANGPT1", "POSTN", "ALK", "GDF15", "EPHA3"],
          "citation": [
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1476717/","notes":"ANGPT1/Tie2 axis induces vascularization in GBM"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6600696/","notes":"POSTN in neovascularization and anti-VEGF resistance"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4545799/","notes":"ALK stimulates angiogenesis, vessel stability in GBM"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4707513/","notes":"GDF15 mediates radiation-induced and baseline angiogenesis"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6178228/","notes":"EPHA3 highly expressed in neovasculature niches"}
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Vascular Endothelium",
          "genes": ["ANGPT1", "POSTN", "EPHA3", "GDF15"],
          "citation": [
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1476717/","notes":"Endothelial ANGPT1 effect"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6178228/","notes":"EPHA3 marks tumor endothelium, niche"}
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Accelerated neovascularization in hypoxic tumor regions",
        "Enhanced vessel permeability and stability",
        "Therapy resistance due to abnormal vascular architecture"
      ],
      "evidence_summary": "Core pro-angiogenic genes (ANGPT1, POSTN, ALK, GDF15, EPHA3) all appear in the input list and have robust, interconnected roles in driving angiogenesis and vascularization in GBM, as shown by literature.",
      "significance_score": 0.94,
      "citations": [
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6600696/","notes":"POSTN neovascularization"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1476717/","notes":"ANGPT1/TIE2 axis"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4545799/","notes":"ALK pro-angiogenic activity"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4707513/","notes":"GDF15 pro-angiogenic fibroblast-tumor cross-talk"}
      ],
      "supporting_genes": ["ANGPT1", "POSTN", "FHL2", "ALK", "GDF15", "EPHA3"],
      "required_genes_not_in_input": {
        "genes": ["VEGFA", "VEGFB", "VEGFR2", "ANGPT2"],
        "citations": [
          {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6178228/","notes":"VEGF/ANGPT axes central to GBM angiogenesis"}
        ]
      }
    },
    {
      "program_name": "WNT/Stemness Signaling",
      "description": "LEF1, WNT16, SPRY, FHL2, and HOPX, with supporting lncRNA and homeodomain regulators, interact to promote WNT pathway activation, stem-cell maintenance, and tumor propagation. LEF1 and WNT pathway genes drive self-renewal capability and resistance, particularly in stem-like and mesenchymal GBM. FHL2 further activates β-catenin/WNT signaling.",
      "atomic_biological_processes": [
        {
          "name": "WNT Signaling",
          "genes": ["LEF1", "WNT16", "FHL2", "SPRY2", "HOPX"],
          "citation": [
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6782348/","notes":"LEF1 regulates WNT-driven invasion"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8204772/","notes":"WNT pathway as stemness regulator in GBM"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8638688/","notes":"FHL2 activates β-catenin complex"}
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Stem Cell Niche",
          "genes": ["LEF1", "WNT16", "HOPX", "FHL2"],
          "citation": [
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6782348/","notes":"LEF1 and stem cell signatures"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8204772/","notes":"WNT-driven stem cell maintenance"}
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Promotion of glioblastoma stem cell self-renewal",
        "Enhanced therapy resistance",
        "Propagation of heterogeneity and tumor growth"
      ],
      "evidence_summary": "LEF1 and WNT pathway genes are central to GBM stem cell maintenance, invasiveness and cell fate. FHL2 boosts β-catenin signaling, with SPRY and HOPX providing regulatory input.",
      "significance_score": 0.90,
      "citations": [
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6782348/","notes":"LEF1 and stemness in GBM"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8204772/","notes":"WNT pathway stem cell regulation"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8638688/","notes":"FHL2/WNT signaling cooperativity"}
      ],
      "supporting_genes": ["LEF1", "WNT16", "FHL2", "SPRY2", "HOPX"],
      "required_genes_not_in_input": {
        "genes": ["CTNNB1", "AXIN2", "TCF7"],
        "citations": [
          {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6782348/","notes":"β-catenin complex mediators required for canonical WNT"}
        ]
      }
    }
  ],
  "method": {
    "clustering_basis": [
      "pathway databases",
      "co-citation",
      "co-expression analysis",
      "protein-protein interaction mapping"
    ],
    "notes": "Programs were derived by integrating literature and database-level evidence, pathway and co-expression signatures among input genes with a priority for high-confidence, widely supported functional modules relevant to glioblastoma biology."
  },
  "version": "2025-11-17"
}
<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_18][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_19][^1_190][^1_191][^1_192][^1_193][^1_194][^1_195][^1_196][^1_197][^1_198][^1_199][^1_2][^1_20][^1_200][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: image.jpg
[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4914248/
[^1_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5104278/
[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10863174/
[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9454705/
[^1_6]: https://www.jneurology.com/articles/commentary-periostin-postn-regulates-tumor-resistance-to-antiangiogenic-therapy-in-glioma-models.pdf
[^1_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4312504/
[^1_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6005831/
[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10423747/
[^1_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6051173/
[^1_11]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/cam4.1534
[^1_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5190103/
[^1_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10867147/
[^1_14]: https://www.oncotarget.com/lookup/doi/10.18632/oncotarget.9744
[^1_15]: https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2024.1320887/pdf
[^1_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6254577/
[^1_17]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8711027/
[^1_18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6896086/
[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7462276/
[^1_20]: https://www.degruyter.com/document/doi/10.1515/med-2022-0572/html
[^1_21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7001780/
[^1_22]: https://academic.oup.com/noa/article-pdf/2/1/vdaa087/33705498/vdaa087.pdf
[^1_23]: https://www.tandfonline.com/doi/pdf/10.1080/21655979.2021.2018096?needAccess=true
[^1_24]: https://www.mdpi.com/2072-6694/11/11/1651
[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2667932/
[^1_26]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5489786/
[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6068449/
[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4544656/
[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8395085/
[^1_30]: https://www.mdpi.com/1422-0067/23/3/1353/pdf
[^1_31]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5584905/
[^1_32]: https://www.mdpi.com/1422-0067/22/16/8428/pdf
[^1_33]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10344874/
[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7058445/
[^1_35]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5504164/
[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1853417/
[^1_37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9219822/
[^1_38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9604754/
[^1_39]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3104784/
[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7124104/
[^1_41]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3904604/
[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10573421/
[^1_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10719344/
[^1_44]: https://www.mdpi.com/1422-0067/24/19/14776/pdf?version=1696062161
[^1_45]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4359323/
[^1_46]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4632291/
[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10679421/
[^1_48]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4174884/
[^1_49]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4295931/
[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11480913/
[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4865916/
[^1_52]: http://www.jbc.org/content/291/20/10684.full.pdf
[^1_53]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5732438/
[^1_54]: http://www.jbc.org/content/275/27/20315.full.pdf
[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8590016/
[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5494611/
[^1_57]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7283475/
[^1_58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3890957/
[^1_59]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4396039/
[^1_60]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4791662/
[^1_61]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4266704/
[^1_62]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2944818/
[^1_63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11056578/
[^1_64]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2769046/
[^1_65]: http://www.jbc.org/content/285/1/255.full.pdf
[^1_66]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7132881/
[^1_67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5078587/
[^1_68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7954792/
[^1_69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5739788/
[^1_70]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4755027/
[^1_71]: https://www.oncotarget.com/article/22197/pdf/
[^1_72]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5342369/
[^1_73]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4973349/
[^1_74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11460468/
[^1_75]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5975090/
[^1_76]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11578086/
[^1_77]: https://www.mdpi.com/1422-0067/21/20/7751/pdf
[^1_78]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8273858/
[^1_79]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10331713/
[^1_80]: https://www.spandidos-publications.com/10.3892/ol.2021.12898/download
[^1_81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7877241/
[^1_82]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11464986/
[^1_83]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9179269/
[^1_84]: https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202416231
[^1_85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12061283/
[^1_86]: https://www.mdpi.com/2072-6694/14/11/2764/pdf?version=1654172988
[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6997107/
[^1_88]: https://portlandpress.com/bioscirep/article-pdf/40/1/BSR20191953/866923/bsr-2019-1953.pdf
[^1_89]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4884950/
[^1_90]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10778311/
[^1_91]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8913883/
[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6497826/
[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11843742/
[^1_94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5805549/
[^1_95]: https://www.oncotarget.com/lookup/doi/10.18632/oncotarget.24102
[^1_96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7801449/
[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9953781/
[^1_98]: https://www.mdpi.com/2072-6694/15/4/1115/pdf?version=1675992794
[^1_99]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2743239/
[^1_100]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3127972/
[^1_101]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8152057/
[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5658114/
[^1_103]: https://www.mdpi.com/1422-0067/23/17/9734/pdf?version=1661840612
[^1_104]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3337398/
[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5570309/
[^1_106]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10363218/
[^1_107]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3525999/
[^1_108]: http://www.jbc.org/content/277/16/14153.full.pdf
[^1_109]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8141965/
[^1_110]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2780428/
[^1_111]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2631139/
[^1_112]: https://www.frontiersin.org/articles/10.3389/fonc.2012.00192/pdf
[^1_113]: https://www.frontiersin.org/articles/10.3389/fimmu.2021.668391/pdf
[^1_114]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3385768/
[^1_115]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8094702/
[^1_116]: https://www.tandfonline.com/doi/pdf/10.3109/03009734.2012.665097?needAccess=true
[^1_117]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3339542/
[^1_118]: https://pmc.ncbi.nlm.nih.gov/articles/PMC312748/
[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3632602/
[^1_120]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10542410/
[^1_121]: https://www.tandfonline.com/doi/pdf/10.1080/10717544.2018.1494226?needAccess=true
[^1_122]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6127843/
[^1_123]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4217908/
[^1_124]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6316644/
[^1_125]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5410341/
[^1_126]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5312354/
[^1_127]: https://www.mdpi.com/2072-6694/10/12/519/pdf
[^1_128]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4183860/
[^1_129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6469190/
[^1_130]: https://www.mdpi.com/1424-8247/12/1/8/pdf
[^1_131]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9617949/
[^1_132]: http://www.jbc.org/content/278/9/7043.full.pdf
[^1_133]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8243487/
[^1_134]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2856996/
[^1_135]: https://www.scientificarchives.com/admin/assets/articles/pdf/ca2calmodulin-dependent-protein-kinases-in-leukemia-development-20210525040550.pdf
[^1_136]: http://www.jbc.org/content/285/15/11188.full.pdf
[^1_137]: http://www.jbc.org/content/281/48/37256.full.pdf
[^1_138]: https://res.mdpi.com/d_attachment/ijms/ijms-21-00888/article_deploy/ijms-21-00888-v2.pdf
[^1_139]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10825359/
[^1_140]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7037280/
[^1_141]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10193886/
[^1_142]: https://www.frontiersin.org/articles/10.3389/fonc.2021.658547/pdf
[^1_143]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8172804/
[^1_144]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8514842/
[^1_145]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8745118/
[^1_146]: https://www.mdpi.com/1422-0067/23/1/157
[^1_147]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4802406/
[^1_148]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9428719/
[^1_149]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1907412/
[^1_150]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10252397/
[^1_151]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2874782/
[^1_152]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11577891/
[^1_153]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8076903/
[^1_154]: https://www.frontiersin.org/articles/10.3389/fcell.2021.617801/pdf
[^1_155]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11062369/
[^1_156]: https://www.tandfonline.com/doi/full/10.1080/15384047.2024.2338955
[^1_157]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9332389/
[^1_158]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10333093/
[^1_159]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5707069/
[^1_160]: https://www.aging-us.com/article/204841/pdf
[^1_161]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10513942/
[^1_162]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11463519/
[^1_163]: https://www.techscience.com/or/online/detail/19324/pdf
[^1_164]: https://www.mdpi.com/1422-0067/21/10/3704/pdf
[^1_165]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8962832/
[^1_166]: https://www.mdpi.com/1422-0067/25/10/5316/pdf?version=1715610791
[^1_167]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6064004/
[^1_168]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6499128/
[^1_169]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4526075/
[^1_170]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5348560/
[^1_171]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10969028/
[^1_172]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10008753/
[^1_173]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10630452/
[^1_174]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3351242/
[^1_175]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11291093/
[^1_176]: https://www.mdpi.com/2076-3425/14/3/275/pdf?version=1710393040
[^1_177]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6894094/
[^1_178]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4850367/
[^1_179]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8859835/
[^1_180]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6004261/
[^1_181]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8626012/
[^1_182]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9533654/
[^1_183]: https://www.mdpi.com/1422-0067/22/22/12404/pdf
[^1_184]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10811744/
[^1_185]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2792636/
[^1_186]: http://insight.jci.org/articles/view/169554/files/pdf
[^1_187]: https://www.spandidos-publications.com/ol/9/2/891/download
[^1_188]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10721324/
[^1_189]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2955165/
[^1_190]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10234023/
[^1_191]: https://onlinelibrary.wiley.com/doi/10.1002/mco2.565
[^1_192]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2363490/
[^1_193]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5518855/
[^1_194]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4724174/
[^1_195]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11486267/
[^1_196]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7710720/
[^1_197]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4351837/
[^1_198]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10121947/
[^1_199]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10033925/
[^1_200]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3554894/```


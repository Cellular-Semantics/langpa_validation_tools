<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Prompt:

Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: ["SERPINE1, EMP1, SPOCD1, ARHGAP29, IL1R1, COL6A2, MYOF, F13A1, CXCL10, CHI3L1, MET, IL6, SAA2, BIRC3, MCTP2, ANGPTL4, ICAM1, CCN1, CAV1, APLN, FOSL1, SNTG2-AS1, TPD52L1, SAA4, KRT75, NFATC2, COL5A1, AC243829.2, CLCF1, ARSJ, PLA2G2A, HMGA2, PTX3, TLR2, LINC00698, ALPK2, TNFAIP3, TNFAIP2, NDRG1, SMOC2, ADGRL2, KANK4, GEM, FAS, CXCL8, CFH, ABCC3, CXCL14, ZFP36, RCAN2, GADD45A, COL1A2, LTF, DHRS3, IDO1, HAP1, AXL, ATP6V0D2, KLF5, ST6GALNAC5, GPD1, PAPPA2, BAG3, MYBPH, MYBPC1, MX2, APBB1IP, ANPEP, ALPL, GPRC5A, SPP1, CXCL2, GPC5, RRAD, LIF, CHRNA9, IL4R, NPNT, SAA1, NPR3, PROM1, SLIT3, ITGBL1, MYO5B, RPS5, RPS27, ETS2, PTGS2, RPS18, BNC2, CPA4, NPAS2, CD274, SLC10A6, LRAT, LINC01993, LINC02832, LINC02821, GBP5, AC021851.2, AKAP12, LINC02154, FN1, MIR222HG, VEGFA, GBP2, ZNF735, TSHZ2, TRPM2, LUCAT1, PI3]
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
    "cell_type": "malignant glioblastoma cells",
    "disease": "glioblastoma",
    "tissue": "brain"
  },
  "input_genes": [
    "SERPINE1", "EMP1", "SPOCD1", "ARHGAP29", "IL1R1", "COL6A2", "MYOF", "F13A1", "CXCL10", "CHI3L1", "MET", "IL6", "SAA2", "BIRC3", "MCTP2", "ANGPTL4", "ICAM1", "CCN1", "CAV1", "APLN", "FOSL1", "SNTG2-AS1", "TPD52L1", "SAA4", "KRT75", "NFATC2", "COL5A1", "AC243829.2", "CLCF1", "ARSJ", "PLA2G2A", "HMGA2", "PTX3", "TLR2", "LINC00698", "ALPK2", "TNFAIP3", "TNFAIP2", "NDRG1", "SMOC2", "ADGRL2", "KANK4", "GEM", "FAS", "CXCL8", "CFH", "ABCC3", "CXCL14", "ZFP36", "RCAN2", "GADD45A", "COL1A2", "LTF", "DHRS3", "IDO1", "HAP1", "AXL", "ATP6V0D2", "KLF5", "ST6GALNAC5", "GPD1", "PAPPA2", "BAG3", "MYBPH", "MYBPC1", "MX2", "APBB1IP", "ANPEP", "ALPL", "GPRC5A", "SPP1", "CXCL2", "GPC5", "RRAD", "LIF", "CHRNA9", "IL4R", "NPNT", "SAA1", "NPR3", "PROM1", "SLIT3", "ITGBL1", "MYO5B", "RPS5", "RPS27", "ETS2", "PTGS2", "RPS18", "BNC2", "CPA4", "NPAS2", "CD274", "SLC10A6", "LRAT", "LINC01993", "LINC02832", "LINC02821", "GBP5", "AC021851.2", "AKAP12", "LINC02154", "FN1", "MIR222HG", "VEGFA", "GBP2", "ZNF735", "TSHZ2", "TRPM2", "LUCAT1", "PI3"
  ],
  "programs": [
    {
      "program_name": "Mesenchymal Transition & Invasion",
      "description": "This program encompasses the transition of glioblastoma cells towards a mesenchymal, highly invasive state associated with aggressive tumor progression, therapy resistance, and poor prognosis. Gene products facilitate ECM remodeling, motility, and intratumoral heterogeneity.",
      "atomic_biological_processes": [
        {
          "name": "ECM Remodeling",
          "genes": ["FN1", "COL6A2", "COL1A2", "COL5A1", "TNC", "SPP1", "SERPINE1", "CHI3L1", "MMPs"],
          "citation": [
            {
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7343887/",
              "source_id": "",
              "notes": "Comprehensive review of invasion mechanisms in glioblastoma highlighting ECM gene contributions."
            }
          ]
        },
        {
          "name": "Mesenchymal Marker Upregulation",
          "genes": ["CHI3L1", "SPP1", "FOSL1", "BIRC3", "MET", "AXL", "CAV1", "HMGA2"],
          "citation": [
            {
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3570272/",
              "source_id": "",
              "notes": "FOSL1 regulates proneural-to-mesenchymal transition in glioblastoma stem cells."
            }
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Invadosome Complex",
          "genes": ["CAV1", "FN1", "SERPINE1"],
          "citation": [
            {
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9515361/",
              "source_id": "",
              "notes": "CAV1 required for invadosome formation and matrix invasion."
            }
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced invasion and motility of tumor cells",
        "Promotion of therapy resistance by supporting stem-like populations",
        "ECM remodeling and increased intratumoral heterogeneity"
      ],
      "evidence_summary": "Multiple mesenchymal markers and ECM remodeling genes are co-expressed in glioblastoma, supporting aggressive invasion and resistance to therapy.",
      "significance_score": 0.97,
      "citations": [
        {
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7343887/",
          "source_id": ""
        },
        {
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3570272/",
          "source_id": ""
        }
      ],
      "supporting_genes": ["FN1", "COL6A2", "COL1A2", "COL5A1", "TNC", "SPP1", "SERPINE1", "CHI3L1", "FOSL1", "BIRC3", "MET", "AXL", "CAV1", "HMGA2"],
      "required_genes_not_in_input": {
        "genes": ["MMP2", "MMP9"],
        "citations": [
          {
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7343887/",
            "source_id": ""
          }
        ]
      }
    },
    {
      "program_name": "Hypoxia Response & Angiogenesis",
      "description": "Genes driving responses to hypoxia, neovascularization, and metabolic adaptation. Prominent in glioblastoma's enhancement of vascular networks, therapeutic resistance, and resilience in low-oxygen microenvironments.",
      "atomic_biological_processes": [
        {
          "name": "Hypoxia Response",
          "genes": ["SERPINE1", "VEGFA", "ANGPTL4", "APLN", "NDRG1", "BIRC3", "MET"],
          "citation": [
            {
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7850583/",
              "source_id": "",
              "notes": "NDRG1 and metabolic adaptation to hypoxia in glioblastoma."
            }
          ]
        },
        {
          "name": "Angiogenesis",
          "genes": ["VEGFA", "CCN1", "ANGPTL4", "APLN", "ANPEP", "ICAM1"],
          "citation": [
            {
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6571400/",
              "source_id": "",
              "notes": "Review of angiogenic programs and their genetic regulators in glioblastoma."
            }
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Blood Vessel Endothelium",
          "genes": ["VEGFA", "ANGPTL4", "CCN1", "ICAM1", "APLN", "ANPEP"],
          "citation": [
            {
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6571400/",
              "source_id": "",
              "notes": "Details role of endothelium in glioblastoma neovascularization."
            }
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Induction of angiogenesis and microvascular proliferation",
        "Cellular adaptation to hypoxia and metabolic stress",
        "Promotion of inflammation and immune cell recruitment"
      ],
      "evidence_summary": "Many program genes are direct transcriptional targets of HIF, controlling angiogenesis and metabolic adaptation in glioblastoma.",
      "significance_score": 0.95,
      "citations": [
        {
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6571400/",
          "source_id": ""
        },
        {
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7850583/",
          "source_id": ""
        }
      ],
      "supporting_genes": ["VEGFA", "ANGPTL4", "APLN", "CCN1", "ICAM1", "SERPINE1", "NDRG1", "BIRC3", "MET", "ANPEP"],
      "required_genes_not_in_input": {
        "genes": ["HIF1A", "EGLN1"],
        "citations": [
          {
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6571400/",
            "source_id": ""
          }
        ]
      }
    },
    {
      "program_name": "Immunosuppression & Inflammation",
      "description": "Genes promoting immune evasion, immunosuppressive microenvironment via cytokines, chemokines, immune checkpoints, and inflammation mediators.",
      "atomic_biological_processes": [
        {
          "name": "Cytokine and Chemokine Signaling",
          "genes": ["IL6", "CXCL10", "CXCL8", "IL1R1", "CXCL14", "PTGS2", "TLR2", "ICAM1", "ID01", "SAA1", "SAA2", "SAA4"],
          "citation": [
            {
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6532277/",
              "source_id": "",
              "notes": "Cytokine profiles in glioblastoma and their role in immune suppression."
            }
          ]
        },
        {
          "name": "Immune Checkpoint Regulation",
          "genes": ["CD274", "BIRC3", "TNFAIP3", "IDO1", "FAS"],
          "citation": [
            {
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5792576/",
              "source_id": "",
              "notes": "IDO1 as immune checkpoint and therapeutic target in GBM."
            }
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Immune Synapse",
          "genes": ["ICAM1", "CD274", "FAS"],
          "citation": [
            {
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5792576/",
              "source_id": "",
              "notes": "Details immune checkpoint formation and role in glioblastoma immune evasion."
            }
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Inhibition of anti-tumor immunity",
        "Recruitment of immunosuppressive macrophages and T cells",
        "Promotion of chronic inflammation tissue remodeling"
      ],
      "evidence_summary": "Cytokines and immune checkpoint proteins are key mediators of glioblastoma immunosuppression and therapy resistance.",
      "significance_score": 0.93,
      "citations": [
        {
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6532277/",
          "source_id": ""
        },
        {
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5792576/",
          "source_id": ""
        }
      ],
      "supporting_genes": ["IL6", "CXCL10", "CXCL8", "IL1R1", "PTGS2", "TLR2", "ICAM1", "CD274", "IDO1", "FAS", "BIRC3", "TNFAIP3", "SAA1", "SAA2", "SAA4", "CXCL14"],
      "required_genes_not_in_input": {
        "genes": ["PDCD1", "CTLA4"],
        "citations": [
          {
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5792576/",
            "source_id": ""
          }
        ]
      }
    },
    {
      "program_name": "Stem Cell Maintenance & Therapy Resistance",
      "description": "Genes regulating maintenance, self-renewal, and therapy resistance of glioblastoma stem-like cells, driving tumor initiation, recurrence, and resistance to cytotoxic treatment.",
      "atomic_biological_processes": [
        {
          "name": "Cancer Stem Cell Self-Renewal",
          "genes": ["PROM1", "LIF", "HMGA2", "FOSL1", "BIRC3", "MET"],
          "citation": [
            {
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4939379/",
              "source_id": "",
              "notes": "HMGA2 and stemness in glioblastoma."
            }
          ]
        },
        {
          "name": "Therapy Resistance",
          "genes": ["BIRC3", "FOSL1", "MET", "SERPINE1"],
          "citation": [
            {
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5439291/",
              "source_id": "",
              "notes": "BIRC3 as driver of therapeutic resistance in glioblastoma."
            }
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Stem Cell Niche",
          "genes": ["PROM1", "LIF", "HMGA2"],
          "citation": [
            {
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4939379/",
              "source_id": "",
              "notes": "Stem cell niche and maintenance in glioblastoma."
            }
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Promotion of tumor initiation and recurrence",
        "Resistance to cytotoxic and antiangiogenic treatments",
        "Enhanced stem cell maintenance and plasticity"
      ],
      "evidence_summary": "Stem cell regulators and resistance genes are co-expressed in glioblastoma, supporting tumor renewal and resistance to treatment.",
      "significance_score": 0.92,
      "citations": [
        {
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4939379/",
          "source_id": ""
        },
        {
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5439291/",
          "source_id": ""
        }
      ],
      "supporting_genes": ["PROM1", "LIF", "HMGA2", "FOSL1", "MET", "BIRC3", "SERPINE1"],
      "required_genes_not_in_input": {
        "genes": ["SOX2", "NANOG"],
        "citations": [
          {
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4939379/",
            "source_id": ""
          }
        ]
      }
    }
  ],
  "method": {
    "clustering_basis": ["pathway databases", "co-citation", "co-expression", "protein-protein interaction"],
    "notes": "Gene programs identified by reviewing experimental studies and curated pathway analyses; highlighted cluster overlap and direct citation support for gene-level roles. Only programs with strong literature support or high-level emerging evidence in glioblastoma were prioritized."
  },
  "version": "2025-11-14"
}
<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_18][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_19][^1_190][^1_191][^1_192][^1_193][^1_194][^1_195][^1_196][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: image.jpg
[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6896086/
[^1_3]: https://www.mdpi.com/2072-6694/11/11/1651
[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7412812/
[^1_5]: https://www.degruyter.com/document/doi/10.1515/med-2022-0572/html
[^1_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11805447/
[^1_7]: https://www.frontiersin.org/articles/10.3389/fmolb.2022.904098/pdf
[^1_8]: https://www.tandfonline.com/doi/pdf/10.1080/21655979.2021.2018096?needAccess=true
[^1_9]: https://www.frontiersin.org/articles/10.3389/fonc.2021.646060/pdf
[^1_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6254577/
[^1_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2905941/
[^1_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8584308/
[^1_13]: https://academic.oup.com/neuro-oncology/advance-article-pdf/doi/10.1093/neuonc/noad210/52841581/noad210.pdf
[^1_14]: http://downloads.hindawi.com/journals/jo/2010/430142.pdf
[^1_15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10102065/
[^1_16]: https://www.mdpi.com/1422-0067/24/8/7047/pdf?version=1681194698
[^1_17]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9618559/
[^1_18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7441403/
[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9666495/
[^1_20]: https://www.mdpi.com/2072-6694/15/17/4257/pdf?version=1692956767
[^1_21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11668713/
[^1_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7180208/
[^1_23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3908752/
[^1_24]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2836500/
[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4848844/
[^1_26]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5369967/
[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3015073/
[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6307970/
[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11832131/
[^1_30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5817947/
[^1_31]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10071791/
[^1_32]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5325397/
[^1_33]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10587537/
[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2694268/
[^1_35]: https://www.aging-us.com/lookup/doi/10.18632/aging.100795
[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3480262/
[^1_37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8096031/
[^1_38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3156184/
[^1_39]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6945232/
[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11267112/
[^1_41]: https://downloads.hindawi.com/journals/omcl/2022/1614336.pdf
[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10766829/
[^1_43]: https://www.frontiersin.org/articles/10.3389/fonc.2023.1279923/full
[^1_44]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10616617/
[^1_45]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10671437/
[^1_46]: https://www.mdpi.com/2072-6694/15/24/5852
[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6144698/
[^1_48]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10378451/
[^1_49]: https://www.mdpi.com/2072-6694/13/12/2983/pdf
[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6591719/
[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5596164/
[^1_52]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6068130/
[^1_53]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8639612/
[^1_54]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6847204/
[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7034242/
[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8189438/
[^1_57]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3512081/
[^1_58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5993506/
[^1_59]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5922378/
[^1_60]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4185805/
[^1_61]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4724183/
[^1_62]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4766797/
[^1_63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6333638/
[^1_64]: https://www.frontiersin.org/articles/10.3389/fphar.2018.01503/pdf
[^1_65]: https://europepmc.org/articles/pmc4766797?pdf=render
[^1_66]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3813418/
[^1_67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6674840/
[^1_68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6560150/
[^1_69]: https://www.frontiersin.org/articles/10.3389/fphar.2019.00506/pdf
[^1_70]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11171200/
[^1_71]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2585048/
[^1_72]: https://www.mdpi.com/2072-6694/16/11/1972/pdf?version=1716389922
[^1_73]: https://www.frontiersin.org/articles/10.3389/fonc.2020.603495/pdf
[^1_74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9532932/
[^1_75]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7479068/
[^1_76]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10539593/
[^1_77]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11083335/
[^1_78]: https://www.mdpi.com/2072-6694/16/9/1637/pdf?version=1713949580
[^1_79]: https://www.frontiersin.org/articles/10.3389/fcell.2020.00795/pdf
[^1_80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5600337/
[^1_81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9379258/
[^1_82]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4891090/
[^1_83]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4599264/
[^1_84]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3342018/
[^1_85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4855077/
[^1_86]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10541364/
[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5584143/
[^1_88]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8781963
[^1_89]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5984695/
[^1_90]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5532623/
[^1_91]: https://www.mdpi.com/2072-6694/9/7/87/pdf
[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3556940/
[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10854665/
[^1_94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11176650/
[^1_95]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4211615/
[^1_96]: https://www.mdpi.com/2073-4409/13/3/218/pdf?version=1706158921
[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4217881/
[^1_98]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8417742/
[^1_99]: https://www.frontiersin.org/articles/10.3389/fonc.2021.701933/pdf
[^1_100]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5762371/
[^1_101]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jcmm.15076
[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7131935/
[^1_103]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7295042/
[^1_104]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10709148/
[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3680531/
[^1_106]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10922678/
[^1_107]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5674895/
[^1_108]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8206529/
[^1_109]: https://www.cellmolbiol.org/index.php/CMB/article/download/3597/1657
[^1_110]: https://www.thno.org/v13p5130.htm
[^1_111]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7408126/
[^1_112]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8946526/
[^1_113]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10571788/
[^1_114]: https://www.mdpi.com/2072-6694/14/6/1480/pdf
[^1_115]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10354941/
[^1_116]: https://www.mdpi.com/2073-4409/12/19/2344/pdf?version=1695552963
[^1_117]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9263249/
[^1_118]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11638655/
[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6266956/
[^1_120]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4757860/
[^1_121]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4582982/
[^1_122]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7792207/
[^1_123]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5355046/
[^1_124]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11997006/
[^1_125]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5570925/
[^1_126]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8745052/
[^1_127]: https://www.mdpi.com/1422-0067/19/12/3773/pdf
[^1_128]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6203104/
[^1_129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5572400/
[^1_130]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5473440/
[^1_131]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9138293/
[^1_132]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3375179/
[^1_133]: https://www.mdpi.com/2227-9059/10/5/935/pdf?version=1650371897
[^1_134]: https://www.frontiersin.org/articles/10.3389/fimmu.2018.00104/pdf
[^1_135]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5826380/
[^1_136]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5664518/
[^1_137]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9248408/
[^1_138]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2767465/
[^1_139]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2825672/
[^1_140]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10723753/
[^1_141]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9100635/
[^1_142]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5822422/
[^1_143]: https://www.mdpi.com/1422-0067/23/9/4602/pdf?version=1650612796
[^1_144]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6726423/
[^1_145]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/cam4.6316
[^1_146]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9219822/
[^1_147]: https://www.frontiersin.org/articles/10.3389/fcell.2021.716462/pdf
[^1_148]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8502969/
[^1_149]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7170819/
[^1_150]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5378489/
[^1_151]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11256543/
[^1_152]: https://urncst.com/index.php/urncst/article/download/627/369
[^1_153]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1535024/
[^1_154]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5722538/
[^1_155]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2713456/
[^1_156]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10215618/
[^1_157]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/advs.202102768
[^1_158]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7977775/
[^1_159]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6453839/
[^1_160]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3198371/
[^1_161]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10501277/
[^1_162]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7349965/
[^1_163]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10960415/
[^1_164]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11158285/
[^1_165]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11952521/
[^1_166]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3810939/
[^1_167]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3820114/
[^1_168]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6827046/
[^1_169]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2729925/
[^1_170]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4153667/
[^1_171]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10528301/
[^1_172]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4277468/
[^1_173]: https://www.mdpi.com/1718-7729/30/9/601
[^1_174]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7555589/
[^1_175]: https://www.mdpi.com/2227-9059/8/9/310/pdf
[^1_176]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7281616/
[^1_177]: https://europepmc.org/articles/pmc7281616?pdf=render
[^1_178]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5417003/
[^1_179]: https://www.mdpi.com/1422-0067/22/22/12608/pdf
[^1_180]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9837376/
[^1_181]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5091648/
[^1_182]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5190103/
[^1_183]: https://www.oncotarget.com/lookup/doi/10.18632/oncotarget.9744
[^1_184]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4495393/
[^1_185]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7738619/
[^1_186]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4059010/
[^1_187]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3615428/
[^1_188]: https://www.mdpi.com/2072-6694/14/15/3743/pdf?version=1659587166
[^1_189]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9164955/
[^1_190]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4050114/
[^1_191]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6643226/
[^1_192]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4873413/
[^1_193]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9905823/
[^1_194]: http://www.jbc.org/content/289/9/5997.full.pdf
[^1_195]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8177779/
[^1_196]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5767169/```


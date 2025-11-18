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
    "cell_type": "malignant glioblastoma cell",
    "disease": "glioblastoma",
    "tissue": "brain"
  },
  "input_genes": [
    "SERPINE1", "EMP1", "SPOCD1", "ARHGAP29", "IL1R1", "COL6A2", "MYOF", "F13A1", "CXCL10",
    "CHI3L1", "MET", "IL6", "SAA2", "BIRC3", "MCTP2", "ANGPTL4", "ICAM1", "CCN1", "CAV1", "APLN",
    "FOSL1", "SNTG2-AS1", "TPD52L1", "SAA4", "KRT75", "NFATC2", "COL5A1", "AC243829.2", "CLCF1",
    "ARSJ", "PLA2G2A", "HMGA2", "PTX3", "TLR2", "LINC00698", "ALPK2", "TNFAIP3", "TNFAIP2", "NDRG1",
    "SMOC2", "ADGRL2", "KANK4", "GEM", "FAS", "CXCL8", "CFH", "ABCC3", "CXCL14", "ZFP36", "RCAN2",
    "GADD45A", "COL1A2", "LTF", "DHRS3", "IDO1", "HAP1", "AXL", "ATP6V0D2", "KLF5", "ST6GALNAC5",
    "GPD1", "PAPPA2", "BAG3", "MYBPH", "MYBPC1", "MX2", "APBB1IP", "ANPEP", "ALPL", "GPRC5A", "SPP1",
    "CXCL2", "GPC5", "RRAD", "LIF", "CHRNA9", "IL4R", "NPNT", "SAA1", "NPR3", "PROM1", "SLIT3",
    "ITGBL1", "MYO5B", "RPS5", "RPS27", "ETS2", "PTGS2", "RPS18", "BNC2", "CPA4", "NPAS2", "CD274",
    "SLC10A6", "LRAT", "LINC01993", "LINC02832", "LINC02821", "GBP5", "AC021851.2", "AKAP12",
    "LINC02154", "FN1", "MIR222HG", "VEGFA", "GBP2", "ZNF735", "TSHZ2", "TRPM2", "LUCAT1", "PI3"
  ],
  "programs": [
    {
      "program_name": "Mesenchymal Transition & Invasion",
      "description": "This program assembles genes regulating key drivers of mesenchymal transition, cellular motility, matrix remodeling, tumor infiltration, and invasion through both transcriptional reprogramming and effector proteins. FOSL1/AP-1, CHI3L1, SPP1, SERPINE1, CAV1, MET, AXL, FN1, COL5A1, and COL6A2 are prominent in driving or supporting mesenchymal phenotype and cellular invasion processes in glioblastoma.",
      "atomic_biological_processes": [
        {
          "name": "epithelial-to-mesenchymal transition",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8916548/",
              "notes": "FOSL1/AP-1 as a master regulator of mesenchymal shift and invasion in glioblastoma stem cells."
            },
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10699000/",
              "notes": "FN1 supports CAF-driven GBM migration & invasion."
            }
          ],
          "genes": ["FOSL1","CHI3L1","SERPINE1","SPP1"]
        },
        {
          "name": "cell migration",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8916548/",
              "notes": "AP1-driven transcription, MET/AXL crosstalk, and CAV1 all potentiate migration."
            }
          ],
          "genes": ["MET","AXL","FOSL1","CAV1"]
        },
        {
          "name": "extracellular matrix remodeling",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.mdpi.com/2072-6694/15/5/1451",
              "notes": "ECM and collagens COL5A1, COL6A2, FN1, and SPP1 modify tumor microenvironment and invasiveness."
            }
          ],
          "genes": ["FN1","COL1A2","COL5A1","COL6A2","SPP1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "extracellular matrix",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.mdpi.com/2072-6694/15/5/1451",
              "notes": "Collagens and fibronectin as core ECM regulators in glioblastoma."
            }
          ],
          "genes": ["COL1A2","COL5A1","COL6A2","FN1","SPP1"]
        },
        {
          "name": "focal adhesion",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8916548/",
              "notes": "FOSL1 targets adhesion molecules and modulates cytoskeletal organization."
            }
          ],
          "genes": ["FOSL1","CAV1","MET"]
        }
      ],
      "predicted_cellular_impact": [
        "promotes mesenchymal shift and invasion",
        "enhances cell migration and ECM degradation",
        "supports CAF-like microenvironment"
      ],
      "evidence_summary": "Strongly supported by transcriptomic, functional, and clinical datasets associating mesenchymal signature genes with poor prognosis, rapid tumor infiltration, and therapy-resistant GBM.",
      "significance_score": 0.98,
      "citations": [
        {
          "source_id": "",
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8916548/"
        },
        {
          "source_id": "",
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10699000/"
        },
        {
          "source_id": "",
          "url": "https://www.mdpi.com/2072-6694/15/5/1451"
        }
      ],
      "supporting_genes": [
        "FOSL1","CHI3L1","SERPINE1","SPP1","FN1","CAV1","MET","AXL","COL1A2","COL5A1","COL6A2"
      ],
      "required_genes_not_in_input": {
        "genes": ["MMP2","VIM","ZEB1"], 
        "citations": [
          {
            "source_id": "",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8916548/",
            "notes": "Canonical MES signature—core invasion factors."
          }
        ]
      }
    },
    {
      "program_name": "Immune Modulation and Inflammation",
      "description": "Cluster of genes representing cytokine/chemokine signaling, inflammatory response, and immune evasion mechanisms. Includes proinflammatory cytokines (IL6, IL1R1), acute phase reactants (SAA1/2/4), chemokines (CXCL8, CXCL10, CXCL14), and immune regulatory checkpoints (CD274), emphasizing the immunosuppressive and inflammatory tumor microenvironment in GBM.",
      "atomic_biological_processes": [
        {
          "name": "cytokine-mediated signaling",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9055064/",
              "notes": "IL6 and IL1R1 are hubs of inflammatory cytokine pathways in GBM."
            }
          ],
          "genes": ["IL6","IL1R1"]
        },
        {
          "name": "chemokine activity",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3087854/",
              "notes": "CXCL8, CXCL10 upregulated in hypoxic, inflammatory GBM microenvironments."
            }
          ],
          "genes": ["CXCL8","CXCL10","CXCL14","CXCL2"]
        },
        {
          "name": "acute phase response",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7973823/",
              "notes": "SAA1/SAA2/SAA4 and CRP-related systemic and local inflammatory signals in GBM."
            }
          ],
          "genes": ["SAA1","SAA2","SAA4"]
        },
        {
          "name": "immune checkpoint signaling",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6862926/",
              "notes": "IDO1 and CD274 (PD-L1) are immunoregulatory in glioblastoma."
            }
          ],
          "genes": ["IDO1","CD274"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "immune synapse",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6862926/",
              "notes": "PD-L1/PD-1 checkpoint operates at the immune interface."
            }
          ],
          "genes": ["CD274"]
        }
      ],
      "predicted_cellular_impact": [
        "drives immunosuppressive microenvironment",
        "sustains chronic inflammation and paracrine tumor support",
        "facilitates immune escape"
      ],
      "evidence_summary": "Multiple GBM studies confirm robust activation of cytokine/chemokine pathways with immune checkpoint regulation; SAA proteins are linked to higher apoptosis resistance.",
      "significance_score": 0.93,
      "citations": [
        {
          "source_id": "",
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9055064/"
        },
        {
          "source_id": "",
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6862926/"
        },
        {
          "source_id": "",
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7973823/"
        }
      ],
      "supporting_genes": [
        "IL6","IL1R1","SAA1","SAA2","SAA4","CXCL8","CXCL10","CXCL14","IDO1","CD274"
      ],
      "required_genes_not_in_input": {
        "genes": ["PDCD1","CD8A"],
        "citations": [
          {
            "source_id": "",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6862926/",
            "notes": "Immune setpoint in GBM."
          }
        ]
      }
    },
    {
      "program_name": "Stemness and Therapy Resistance",
      "description": "Genes maintaining glioblastoma stem-like cell (GSC) identity, pluripotency, and resistance to therapy, such as PROM1 (CD133), HMGA2, LIF, and BAG3. Markers here also impact tumor recurrence, plasticity, and response to stress.",
      "atomic_biological_processes": [
        {
          "name": "stem cell maintenance",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9985426/",
              "notes": "PROM1 (CD133) as a functional and controversial GSC marker in GBM."
            }
          ],
          "genes": ["PROM1","HMGA2","LIF"]
        },
        {
          "name": "transcriptional regulation of pluripotency",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4932936/",
              "notes": "HMGA2, LIF and supporting evidence for stemness and recurrence in GBM."
            }
          ],
          "genes": ["HMGA2","LIF"]
        },
        {
          "name": "autophagy",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4372074/",
              "notes": "BAG3 upregulates autophagy for GBM survival and chemoresistance."
            }
          ],
          "genes": ["BAG3"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "perivascular niche",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2760935/",
              "notes": "Stem-like tumor cells thrive in hypoxic niches within GBM."
            }
          ],
          "genes": ["PROM1","LIF"]
        }
      ],
      "predicted_cellular_impact": [
        "supports GSC identity and heterogeneity",
        "maintains tumor-initiating potential and recurrence risk",
        "drives resistance to therapies"
      ],
      "evidence_summary": "PROM1, HMGA2, and LIF together denote stemness; BAG3/autophagy pathway counteracts cell stress, supporting survival under chemo/radiation.",
      "significance_score": 0.91,
      "citations": [
        {
          "source_id": "",
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9985426/"
        },
        {
          "source_id": "",
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4932936/"
        },
        {
          "source_id": "",
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4372074/"
        }
      ],
      "supporting_genes": [
        "PROM1","HMGA2","LIF","BAG3"
      ],
      "required_genes_not_in_input": {
        "genes": ["SOX2","OLIG2"],
        "citations": [
          {
            "source_id": "",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9985426/",
            "notes": "Alternate stemness transcription factors."
          }
        ]
      }
    },
    {
      "program_name": "Angiogenesis & Hypoxic Response",
      "description": "Groups angiogenic regulators (VEGFA, ANGPTL4, APLN, MET, COL1A2), hypoxia response elements (NDRG1, PTX3), and matrix modifiers, controlling vascular niche formation and metabolic adaptation.",
      "atomic_biological_processes": [
        {
          "name": "angiogenesis",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6618529/",
              "notes": "VEGFA, MET, ANGPTL4, and APLN as angiogenesis drivers in GBM."
            }
          ],
          "genes": ["VEGFA","ANGPTL4","APLN","MET"]
        },
        {
          "name": "hypoxic response",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10400082/",
              "notes": "NDRG1 and PTX3 linked to hypoxic activation and tumor progression."
            }
          ],
          "genes": ["NDRG1","PTX3"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "vascular niche",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2760935/",
              "notes": "Perivascular and hypoxic microenvironments sustain stem-like GSCs and angiogenesis."
            }
          ],
          "genes": ["VEGFA","ANGPTL4","PTX3"]
        }
      ],
      "predicted_cellular_impact": [
        "promotes neovascularization",
        "supports metabolic adaptation to hypoxia",
        "enhances tumor growth and survival"
      ],
      "evidence_summary": "Canonical angiogenic genes and hypoxic response elements are well-known GBM determinants, enriching the tumor microenvironment and sustaining stemness.",
      "significance_score": 0.92,
      "citations": [
        {
          "source_id": "",
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6618529/"
        },
        {
          "source_id": "",
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10400082/"
        },
        {
          "source_id": "",
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2760935/"
        }
      ],
      "supporting_genes": [
        "VEGFA","ANGPTL4","APLN","MET","PTX3","NDRG1"
      ],
      "required_genes_not_in_input": {
        "genes": ["HIF1A"],
        "citations": [
          {
            "source_id": "",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2760935/",
            "notes": "Canonical hypoxic response mediator."
          }
        ]
      }
    },
    {
      "program_name": "Therapy Resistance and Drug Efflux",
      "description": "Genes related to apoptosis suppression (BIRC3, TNFAIP3/2), multidrug resistance (ABCC3), and survival pathways. Program involves resistance to cell stress, apoptosis, and ineffective drug penetration.",
      "atomic_biological_processes": [
        {
          "name": "apoptosis suppression",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4780503/",
              "notes": "BIRC3 as mediator of apoptosis evasion and chemoresistance in GBM."
            }
          ],
          "genes": ["BIRC3","TNFAIP3","TNFAIP2"]
        },
        {
          "name": "drug transport",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9026706/",
              "notes": "ABCC3 confers chemoresistance via active transport of drug molecules."
            }
          ],
          "genes": ["ABCC3"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "multidrug resistance transporter complex",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9026706/",
              "notes": "Position and function of ABCC3."
            }
          ],
          "genes": ["ABCC3"]
        }
      ],
      "predicted_cellular_impact": [
        "increases resistance to chemotherapy",
        "suppresses apoptosis",
        "enhances tumor survival"
      ],
      "evidence_summary": "BIRC3, TNFAIP3/2 and ABCC3 are upregulated with therapy, promote therapy resistance, and are tied to poor GBM clinical outcomes.",
      "significance_score": 0.87,
      "citations": [
        {
          "source_id": "",
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4780503/"
        },
        {
          "source_id": "",
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9026706/"
        }
      ],
      "supporting_genes": [
        "BIRC3","TNFAIP3","TNFAIP2","ABCC3"
      ],
      "required_genes_not_in_input": {
        "genes": ["MGMT"],
        "citations": [
          {
            "source_id": "",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9026706/",
            "notes": "Common resistance marker in GBM."
          }
        ]
      }
    }
  ],
  "version": "2025-11-14 GBM Literature Synthesis 1.0"
}
<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_18][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_19][^1_190][^1_191][^1_192][^1_193][^1_194][^1_195][^1_196][^1_197][^1_198][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6896086/
[^1_2]: https://www.mdpi.com/2072-6694/11/11/1651
[^1_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7412812/
[^1_4]: https://www.degruyter.com/document/doi/10.1515/med-2022-0572/html
[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11805447/
[^1_6]: https://www.frontiersin.org/articles/10.3389/fmolb.2022.904098/pdf
[^1_7]: https://www.tandfonline.com/doi/pdf/10.1080/21655979.2021.2018096?needAccess=true
[^1_8]: https://www.frontiersin.org/articles/10.3389/fonc.2021.646060/pdf
[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4757860/
[^1_10]: https://www.frontiersin.org/articles/10.3389/fonc.2020.01631/pdf
[^1_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11382672/
[^1_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7935068/
[^1_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3799953/
[^1_14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10939876/
[^1_15]: https://www.mdpi.com/1422-0067/23/13/7330/pdf?version=1656646213
[^1_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9100418/
[^1_17]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2694268/
[^1_18]: https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2024.1391921/pdf
[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8393628/
[^1_20]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3098164/
[^1_21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9379258/
[^1_22]: https://www.mdpi.com/2076-3921/12/2/220/pdf?version=1674025780
[^1_23]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jcmm.14507
[^1_24]: https://www.mdpi.com/2072-6694/15/6/1879/pdf?version=1679382163
[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10046791/
[^1_26]: https://onlinelibrary.wiley.com/doi/10.1155/bmri/2004975
[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6313004/
[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5084181/
[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10326062/
[^1_30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11101656/
[^1_31]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8548600/
[^1_32]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6177597/
[^1_33]: http://www.jbc.org/content/293/40/15397.full.pdf
[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3342018/
[^1_35]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6585013/
[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4599264/
[^1_37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4012720/
[^1_38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7332240/
[^1_39]: https://www.embopress.org/doi/10.15252/emmm.201505890
[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9263249/
[^1_41]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8370767/
[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11638655/
[^1_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11980931/
[^1_44]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11121637/
[^1_45]: https://www.mdpi.com/1422-0067/25/10/5362/pdf?version=1715692239
[^1_46]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6266956/
[^1_47]: https://www.mdpi.com/2072-6694/14/6/1480/pdf
[^1_48]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7555589/
[^1_49]: https://www.mdpi.com/2227-9059/8/9/310/pdf
[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9262576/
[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2610484/
[^1_52]: https://www.mdpi.com/2076-3425/12/4/473/pdf
[^1_53]: https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202416231
[^1_54]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12061283/
[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6591719/
[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6847204/
[^1_57]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8639612/
[^1_58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5596164/
[^1_59]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6068130/
[^1_60]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11279595/
[^1_61]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9206138/
[^1_62]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4681601/
[^1_63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8098208/
[^1_64]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1853267/
[^1_65]: http://downloads.hindawi.com/journals/bmri/2017/7403747.pdf
[^1_66]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11193792/
[^1_67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5702396/
[^1_68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6320836/
[^1_69]: https://www.mdpi.com/1422-0067/19/12/3773/pdf
[^1_70]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8945784/
[^1_71]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4373658/
[^1_72]: https://royalsocietypublishing.org/doi/pdf/10.1098/rsob.200184
[^1_73]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7536068/
[^1_74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7865981/
[^1_75]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7540153/
[^1_76]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5833690/
[^1_77]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6193815/
[^1_78]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6949068/
[^1_79]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3810939/
[^1_80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4153667/
[^1_81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2729925/
[^1_82]: https://www.mdpi.com/2072-6694/15/5/1557/pdf?version=1677738914
[^1_83]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4878508/
[^1_84]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10508696/
[^1_85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10528301/
[^1_86]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3820114/
[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3538149/
[^1_88]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6852885/
[^1_89]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8869716/
[^1_90]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2767465/
[^1_91]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10723753/
[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9248408/
[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2825672/
[^1_94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9367289/
[^1_95]: https://www.frontiersin.org/articles/10.3389/fimmu.2021.729359/pdf
[^1_96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6685507/
[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7896088/
[^1_98]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11343637/
[^1_99]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10989959/
[^1_100]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10973500/
[^1_101]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8582528/
[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9087910/
[^1_103]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5091648/
[^1_104]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6051173/
[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5190103/
[^1_106]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/cam4.1534
[^1_107]: https://www.oncotarget.com/lookup/doi/10.18632/oncotarget.9744
[^1_108]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4059010/
[^1_109]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11907455/
[^1_110]: https://www.frontiersin.org/articles/10.3389/fcell.2020.558961/pdf
[^1_111]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8773542/
[^1_112]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4143920/
[^1_113]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9283442/
[^1_114]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6681735/
[^1_115]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11529598/
[^1_116]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10932253/
[^1_117]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10922678/
[^1_118]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7702012/
[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8417742/
[^1_120]: https://www.frontiersin.org/articles/10.3389/fonc.2021.701933/pdf
[^1_121]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5762371/
[^1_122]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jcmm.15076
[^1_123]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7131935/
[^1_124]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8206529/
[^1_125]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8584308/
[^1_126]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2905941/
[^1_127]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10960415/
[^1_128]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4469333/
[^1_129]: http://www.jbc.org/content/289/50/34520.full.pdf
[^1_130]: https://downloads.hindawi.com/journals/bmri/2021/6642973.pdf
[^1_131]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4263860/
[^1_132]: http://downloads.hindawi.com/journals/cmmi/2018/5315172.pdf
[^1_133]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4520645/
[^1_134]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7972841/
[^1_135]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10412822/
[^1_136]: https://www.frontiersin.org/articles/10.3389/fphys.2023.1217828/pdf
[^1_137]: https://www.mdpi.com/2072-6694/13/14/3428/pdf
[^1_138]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3699330/
[^1_139]: https://www.frontiersin.org/articles/10.3389/fcell.2021.618961/pdf
[^1_140]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11239348/
[^1_141]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8388852/
[^1_142]: https://www.frontiersin.org/articles/10.3389/fimmu.2024.1391355/full
[^1_143]: https://www.thno.org/v13p3794.pdf
[^1_144]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2408856/
[^1_145]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10200060/
[^1_146]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7174070/
[^1_147]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5681489/
[^1_148]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8424516/
[^1_149]: https://www.frontiersin.org/articles/10.3389/fimmu.2017.01438/pdf
[^1_150]: https://res.mdpi.com/d_attachment/biomolecules/biomolecules-10-00456/article_deploy/biomolecules-10-00456.pdf
[^1_151]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5688930/
[^1_152]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9123716/
[^1_153]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7377936/
[^1_154]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7875342/
[^1_155]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6529605/
[^1_156]: https://onlinelibrary.wiley.com/doi/10.1111/cpr.12836
[^1_157]: https://www.frontiersin.org/articles/10.3389/fonc.2020.00259/pdf
[^1_158]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5689739/
[^1_159]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8040715/
[^1_160]: https://www.jcancer.org/v12p2756.pdf
[^1_161]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11885894/
[^1_162]: https://www.frontiersin.org/articles/10.3389/fimmu.2025.1544085/full
[^1_163]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6608020/
[^1_164]: http://www.jbc.org/content/288/4/2744.full.pdf
[^1_165]: https://www.frontiersin.org/articles/10.3389/fimmu.2020.00843/pdf
[^1_166]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5405626/
[^1_167]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4518733/
[^1_168]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8232134/
[^1_169]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7794986/
[^1_170]: https://www.mdpi.com/1422-0067/22/12/6385/pdf
[^1_171]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10628546/
[^1_172]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8493376/
[^1_173]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9019268/
[^1_174]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11251740/
[^1_175]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10950892/
[^1_176]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7293068/
[^1_177]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/1878-0261.13571
[^1_178]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6770393/
[^1_179]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9329787/
[^1_180]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11887670/
[^1_181]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10546978/
[^1_182]: https://www.mdpi.com/1422-0067/24/24/17633/pdf?version=1702913099
[^1_183]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10253701/
[^1_184]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10266237/
[^1_185]: https://www.mdpi.com/1420-3049/22/4/539/pdf
[^1_186]: https://www.mdpi.com/1422-0067/24/11/9393
[^1_187]: https://www.mdpi.com/2079-9721/12/3/63/pdf?version=1711070794
[^1_188]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jcmm.18339
[^1_189]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5570559/
[^1_190]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10968914/
[^1_191]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5000706/
[^1_192]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11611868/
[^1_193]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3848550/
[^1_194]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4079276/
[^1_195]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11299042/
[^1_196]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12077904/
[^1_197]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2584051/
[^1_198]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7782833/```


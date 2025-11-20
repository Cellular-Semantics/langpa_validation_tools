<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Prompt:

Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: ["AFAP1L2, COL4A3, FERMT1, VIPR2, AL512308.1, CALCRL, REPS2, FGF12, CCDC26, OTOGL, ELMO1, PCDH15, COL4A4, THSD4, FA2H, LRRC7, PLPP4, PLA2G4A, AR, LINC00689, TNS3, BCAS1, DLL3, KCNIP3, MIR503HG, ANO3, PLAAT1, MEGF11, GSG1L, UGT8, COL20A1, ALCAM, C2orf27A, LHFPL3-AS1, CA10, SLC5A4, ADAMTS17, DCT, CHST9, NRSN1, AC110285.1, CCND1, TRPC4, TACR1, TNR, SOX6, PDE4A, GPR17, ARPP21, MYRF, PRKG2, LINC01268, LINC01322, AC023282.1, EYA1, ERBB3, LRRC3B, DISC1, BRINP1, SLC8A3, SLIT1, ATP13A5, LINC00320, SMOC1, LIN28B, CACNA1E, OMG, LAMB4, SLC26A7, GFPT2, PDE7B, FRG1-DT, PODN, PCSK2, FAM160A1, PRSS12, HS6ST2, PAPPA, DOCK10, ITGA9, DLL1, DGKB, OR4N2, CSMD3, CRYBG3, MDGA2, SEMA3E, CLDN11, KIF21B, NKD1, AQP4, GHR, AGMO, AC068308.1, MOG, TMPRSS9, USP43, MIR217HG, LRFN5, UGDH, AL139231.1, AL136114.1, AC005909.2, MYRIP, ANO4, TMEM132C, AC077690.1, AL031293.1, AC104051.2”]
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
    "AFAP1L2", "COL4A3", "FERMT1", "VIPR2", "AL512308.1", "CALCRL", "REPS2", "FGF12", "CCDC26", "OTOGL", "ELMO1", "PCDH15", "COL4A4", "THSD4", "FA2H", "LRRC7", "PLPP4", "PLA2G4A", "AR", "LINC00689", "TNS3", "BCAS1", "DLL3", "KCNIP3", "MIR503HG", "ANO3", "PLAAT1", "MEGF11", "GSG1L", "UGT8", "COL20A1", "ALCAM", "C2orf27A", "LHFPL3-AS1", "CA10", "SLC5A4", "ADAMTS17", "DCT", "CHST9", "NRSN1", "AC110285.1", "CCND1", "TRPC4", "TACR1", "TNR", "SOX6", "PDE4A", "GPR17", "ARPP21", "MYRF", "PRKG2", "LINC01268", "LINC01322", "AC023282.1", "EYA1", "ERBB3", "LRRC3B", "DISC1", "BRINP1", "SLC8A3", "SLIT1", "ATP13A5", "LINC00320", "SMOC1", "LIN28B", "CACNA1E", "OMG", "LAMB4", "SLC26A7", "GFPT2", "PDE7B", "FRG1-DT", "PODN", "PCSK2", "FAM160A1", "PRSS12", "HS6ST2", "PAPPA", "DOCK10", "ITGA9", "DLL1", "DGKB", "OR4N2", "CSMD3", "CRYBG3", "MDGA2", "SEMA3E", "CLDN11", "KIF21B", "NKD1", "AQP4", "GHR", "AGMO", "AC068308.1", "MOG", "TMPRSS9", "USP43", "MIR217HG", "LRFN5", "UGDH", "AL139231.1", "AL136114.1", "AC005909.2", "MYRIP", "ANO4", "TMEM132C", "AC077690.1", "AL031293.1", "AC104051.2"
  ],
  "programs": [
    {
      "program_name": "Cell Migration and Invasion",
      "description": "Encompasses activation of cytoskeletal dynamics, ECM remodeling, and integrin/adhesion signaling via upregulation of AFAP1L2, FERMT1, ELMO1, COL4A3/COL4A4, ITGA9, TNS3, ALCAM, PRSS12, and focal adhesion/cytoskeletal regulators. These support aggressive migratory and invasive behaviors fundamental to malignant glioblastoma cells.",
      "atomic_biological_processes": [
        {
          "name": "Focal adhesion signaling",
          "citation": [
            {
              "source_id": "",
              "url": "https://downloads.hindawi.com/journals/jo/2010/473063.pdf",
              "notes": "Describes roles of adhesion signaling molecules and cytoskeleton in mesenchymal migration of glioblastoma cells"
            },
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6184201/",
              "notes": "Review of integrins and ECM connectivity in glioblastoma migration and possible therapeutic targets"
            }
          ],
          "genes": ["TNS3", "ITGA9", "FERMT1", "AFAP1L2"]
        },
        {
          "name": "Rac1-mediated cell motility",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1950732/",
              "notes": "ELMO1 and Dock180 drive glioma cell invasion via Rac1 activation"
            }
          ],
          "genes": ["ELMO1"]
        },
        {
          "name": "ECM remodeling",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.mdpi.com/2072-6694/15/3/813",
              "notes": "Role of ECM and major matrix proteins in tumor development and invasion"
            }
          ],
          "genes": ["COL4A3", "COL4A4", "ALCAM", "PODN", "PRSS12"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Extracellular matrix",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.mdpi.com/2072-6694/15/3/813",
              "notes": "Covers ECM composition and remodeling enzymes in GBM"
            }
          ],
          "genes": ["COL4A3", "COL4A4", "PODN"]
        },
        {
          "name": "Focal adhesion",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6184201/",
              "notes": "Integrins, focal adhesion kinases and receptors in migration"
            }
          ],
          "genes": ["ITGA9", "TNS3", "FERMT1"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced cytoskeletal dynamics and adhesion-dependent migration",
        "Accelerated ECM breakdown facilitating invasion",
        "Upregulated integrin and focal adhesion machinery driving motility"
      ],
      "evidence_summary": "Multiple molecules from the input gene list encode structural ECM components, integrin partners, and cytoskeletal regulators. Collectively, these molecules have established roles in tumor cell migration and invasion. Glioblastoma's highly invasive character is driven by such coordinated gene programs.",
      "significance_score": 0.98,
      "citations": [
        {
          "source_id": "",
          "url": "https://downloads.hindawi.com/journals/jo/2010/473063.pdf",
          "notes": "Adhesion signaling in GBM migration"
        },
        {
          "source_id": "",
          "url": "https://www.mdpi.com/2072-6694/15/3/813",
          "notes": "ECM and invasion in GBM"
        }
      ],
      "supporting_genes": ["AFAP1L2", "FERMT1", "TNS3", "ITGA9", "COL4A3", "COL4A4", "ELMO1", "PRSS12", "ALCAM", "PODN"],
      "required_genes_not_in_input": {
        "genes": ["CD44", "MMP2", "MMP9"],
        "citations": [
          {
            "source_id": "",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6184201/",
            "notes": "Reviews roles of CD44 and MMPs in migration; not present in input"
          }
        ]
      }
    },
    {
      "program_name": "Oligodendrocyte/Stem-like Myelination Program",
      "description": "Includes key drivers of myelin gene expression, oligodendrocyte precursor function, and glioma stemness—BCAS1, MYRF, SOX6, UGT8, CLDN11, FA2H—often hijacked by glioblastoma to fuel growth, plasticity, and stem cell-like properties.",
      "atomic_biological_processes": [
        {
          "name": "Oligodendrogenesis and myelin formation",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3781343/",
              "notes": "MYRF and SOX10 define network for oligodendrocyte differentiation and myelin gene expression"
            },
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8674826/",
              "notes": "Glioblastoma cell populations and oligodendrocyte-like features"
            }
          ],
          "genes": ["MYRF", "BCAS1", "UGT8", "CLDN11", "FA2H"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Myelin sheath",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8192642/",
              "notes": "MYRF in myelin development and maintenance"
            }
          ],
          "genes": ["MYRF", "BCAS1", "UGT8", "FA2H", "CLDN11"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced lineage plasticity and stem-like features",
        "Upregulation of myelin gene expression enables tumor adaptability",
        "Supports aggressive proliferation and potential resistance to therapy"
      ],
      "evidence_summary": "Glioblastoma frequently co-opts myelination and oligodendroglial gene programs to support stem-like character, increase growth versatility, and promote therapy resistance.",
      "significance_score": 0.92,
      "citations": [
        {
          "source_id": "",
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8674826/",
          "notes": "GBM single-cell analysis showing oligodendroglial/myelinating programs"
        },
        {
          "source_id": "",
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3781343/",
          "notes": "Network involving MYRF, SOX10, and myelin genes"
        }
      ],
      "supporting_genes": ["BCAS1", "MYRF", "SOX6", "UGT8", "CLDN11", "FA2H"],
      "required_genes_not_in_input": {
        "genes": ["SOX10", "OLIG2"],
        "citations": [
          {
            "source_id": "",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3781343/",
            "notes": "SOX10 and OLIG2 are key regulators of myelination in CNS"
          }
        ]
      }
    },
    {
      "program_name": "Calcium, Ion Channel, and Synaptic Pathway",
      "description": "Multiple input genes encode voltage-gated calcium channels, synaptic receptor subunits, and ion channel regulators (CACNA1E, TRPC4, ANO3, GSG1L, SLC8A3, KCNIP3, AQP4). These orchestrate dysregulated ionic homeostasis, drive excitatory signaling, and enable tumor proliferation, migration, and neuro-glial network hijacking.",
      "atomic_biological_processes": [
        {
          "name": "Calcium signaling and migration",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10716412/",
              "notes": "GBM ion channel genes and correlation with migration/proliferation"
            }
          ],
          "genes": ["CACNA1E", "TRPC4", "SLC8A3", "KCNIP3"]
        },
        {
          "name": "AMPA receptor-driven excitatory signaling",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7134381/",
              "notes": "AMPA receptors and synaptic protein enrichment in GBM"
            }
          ],
          "genes": ["GSG1L"]
        },
        {
          "name": "Aquaporin channel function",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8543622/",
              "notes": "Aquaporin channels potentiate cell migration and invasion in GBM"
            }
          ],
          "genes": ["AQP4"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Voltage-gated channels",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3225252/",
              "notes": "Overview of ion channel involvement in GBM"
            }
          ],
          "genes": ["CACNA1E", "TRPC4", "SLC8A3", "KCNIP3"]
        },
        {
          "name": "Synaptic compartment",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9725506/",
              "notes": "AMPA receptor signaling's role in aggressive GBM"
            }
          ],
          "genes": ["GSG1L"]
        }
      ],
      "predicted_cellular_impact": [
        "Promotes dysregulated migration, proliferation, and network formation",
        "Amplifies survival via altered calcium signaling",
        "Enhances invasive behavior through aquaporin regulation"
      ],
      "evidence_summary": "Coordination of calcium channels, aquaporins, and synaptic machinery underlies the plasticity and chemoresistance of malignant glioblastoma cells, matching the high content of relevant genes in the input list.",
      "significance_score": 0.87,
      "citations": [
        {
          "source_id": "",
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3225252/",
          "notes": "Ion channel review in GBM"
        },
        {
          "source_id": "",
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7134381/",
          "notes": "GBM glutamate/AMPA signaling"
        }
      ],
      "supporting_genes": ["CACNA1E", "TRPC4", "SLC8A3", "KCNIP3", "GSG1L", "ANO3", "AQP4", "UGT8"],
      "required_genes_not_in_input": {
        "genes": ["GRIA1", "KCNH6", "KCNN4"],
        "citations": [
          {
            "source_id": "",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10716412/",
            "notes": "Three-channel risk model for GBM includes these"
          }
        ]
      }
    },
    {
      "program_name": "Angiogenesis and Vascular Remodeling",
      "description": "Features regulation of angiogenic growth factors, ECM and vessel-related proteins (THSD4, COL4A3, COL4A4, LAMB4, ITGA9, PODN) crucial to neovascularization, blood-brain barrier adaptation, and relapse.",
      "atomic_biological_processes": [
        {
          "name": "VEGF-related angiogenesis",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7074633/",
              "notes": "Mechanistic review of angiogenesis in GBM"
            }
          ],
          "genes": ["THSD4", "COL4A3", "COL4A4", "LAMB4", "ITGA9"]
        },
        {
          "name": "Basement membrane organization",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9145425/",
              "notes": "Basement membrane proteins and their role in vascular niche of GBM"
            }
          ],
          "genes": ["COL4A3", "COL4A4", "LAMB4"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Blood vessel endothelium",
          "citation": [
            {
              "source_id": "",
              "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11256543/",
              "notes": "Endothelial cells in GBM vasculature"
            }
          ],
          "genes": ["THSD4", "ITGA9", "LAMB4"]
        }
      ],
      "predicted_cellular_impact": [
        "Promotes vessel formation and aberrant angiogenesis",
        "Facilitates tumor expansion and immune evasion",
        "Enables therapy resistance via vascular remodeling"
      ],
      "evidence_summary": "Extracellular matrix and angiogenesis genes are well established drivers of the hypervascular GBM phenotype, correlating with therapeutic resistance.",
      "significance_score": 0.86,
      "citations": [
        {
          "source_id": "",
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7074633/",
          "notes": "Angiogenic signaling review in GBM"
        },
        {
          "source_id": "",
          "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11256543/",
          "notes": "Endothelial contributions in GBM angiogenesis"
        }
      ],
      "supporting_genes": ["THSD4", "COL4A3", "COL4A4", "LAMB4", "ITGA9", "PODN"],
      "required_genes_not_in_input": {
        "genes": ["VEGFA", "ANGPT2"],
        "citations": [
          {
            "source_id": "",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9145425/",
            "notes": "VEGF and ANGPT2 are canonical angiogenesis drivers"
          }
        ]
      }
    }
  ],
  "version": "2025-11-17"
}
<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_18][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_19][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: image.jpg
[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6594811/
[^1_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10155653/
[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10922678/
[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11752630/
[^1_6]: https://www.aging-us.com/lookup/doi/10.18632/aging.102018
[^1_7]: https://www.frontiersin.org/articles/10.3389/fmolb.2022.904098/pdf
[^1_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10165763/
[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3337451/
[^1_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10321640/
[^1_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11322382/
[^1_12]: https://www.frontiersin.org/articles/10.3389/fphar.2016.00139/pdf
[^1_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9550923/
[^1_14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9580613/
[^1_15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9091202/
[^1_16]: https://www.mdpi.com/2072-6694/11/1/123/pdf
[^1_17]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7687855/
[^1_18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2905941/
[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11082118/
[^1_20]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11600334/
[^1_21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3011255/
[^1_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9000211/
[^1_23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8206529/
[^1_24]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2867339/
[^1_25]: https://www.frontiersin.org/articles/10.3389/fncel.2021.663092/pdf
[^1_26]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5765207/
[^1_27]: http://downloads.hindawi.com/journals/jo/2010/430142.pdf
[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8584308/
[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6254577/
[^1_30]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/cam4.6316
[^1_31]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9219822/
[^1_32]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7170819/
[^1_33]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11256543/
[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5378489/
[^1_35]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2940950/
[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4673177/
[^1_37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10423747/
[^1_38]: https://www.mdpi.com/1422-0067/23/22/13818/pdf?version=1668058723
[^1_39]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11914282/
[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8085851/
[^1_41]: https://www.mdpi.com/2072-6694/16/2/397/pdf?version=1705485981
[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10093493/
[^1_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9797845/
[^1_44]: https://www.frontiersin.org/articles/10.3389/fonc.2022.1085034/pdf
[^1_45]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10814456/
[^1_46]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10812236/
[^1_47]: https://www.mdpi.com/2072-6694/14/16/3890/pdf?version=1660277642
[^1_48]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9405932/
[^1_49]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11772157/
[^1_50]: https://www.frontiersin.org/articles/10.3389/fimmu.2024.1522381/full
[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8688884/
[^1_52]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11884765/
[^1_53]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7391509/
[^1_54]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9740065/
[^1_55]: https://www.mdpi.com/2072-6694/14/23/5932/pdf?version=1669814747
[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9304377/
[^1_57]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3287158/
[^1_58]: https://linkinghub.elsevier.com/retrieve/pii/S1476558624000228
[^1_59]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10881536/
[^1_60]: https://www.mdpi.com/2072-6694/14/19/4960/pdf?version=1665401479
[^1_61]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3479115/
[^1_62]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2718970/
[^1_63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11945080/
[^1_64]: https://dx.plos.org/10.1371/journal.pone.0047846
[^1_65]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7118801/
[^1_66]: https://www.frontiersin.org/articles/10.3389/fphar.2020.00358/pdf
[^1_67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6361447/
[^1_68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3664620/
[^1_69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3452333/
[^1_70]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7699035/
[^1_71]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6639050/
[^1_72]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3159468/
[^1_73]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10702825/
[^1_74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10418167/
[^1_75]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8330525/
[^1_76]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9177076/
[^1_77]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8037102/
[^1_78]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8440018/
[^1_79]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9339490/
[^1_80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11698767/
[^1_81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11327863/
[^1_82]: https://www.frontiersin.org/articles/10.3389/fneur.2018.01087/pdf
[^1_83]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9916806/
[^1_84]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7794959/
[^1_85]: https://www.mdpi.com/2072-6694/13/1/41/pdf
[^1_86]: https://downloads.hindawi.com/journals/bmri/2022/6291504.pdf
[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10587102/
[^1_88]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9006081/
[^1_89]: https://academic.oup.com/neuro-oncology/advance-article-pdf/doi/10.1093/neuonc/noad210/52841581/noad210.pdf
[^1_90]: https://www.frontiersin.org/articles/10.3389/fimmu.2019.01790/pdf
[^1_91]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6433792/
[^1_92]: https://www.mdpi.com/1422-0067/23/18/10616/pdf?version=1663067924
[^1_93]: https://www.thno.org/v11p2080.htm
[^1_94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7444459/
[^1_95]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3106141/
[^1_96]: https://www.mdpi.com/1422-0067/22/18/9665/pdf
[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9502408/
[^1_98]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3742440/
[^1_99]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7026603/
[^1_100]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8192642/
[^1_101]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3185407/
[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3814293/
[^1_103]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3370422/
[^1_104]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5316316/
[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6596239/
[^1_106]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8632286/
[^1_107]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4018830/
[^1_108]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4629334/
[^1_109]: http://www.jbc.org/content/292/2/597.full.pdf
[^1_110]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3958038/
[^1_111]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6892224/
[^1_112]: https://www.mdpi.com/1422-0067/26/8/3503
[^1_113]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9271693/
[^1_114]: https://www.cancerbiomed.org/content/cbm/early/2023/03/07/j.issn.2095-3941.2022.0771.full.pdf
[^1_115]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jcmm.16330
[^1_116]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11080186/
[^1_117]: https://www.mdpi.com/2072-6694/12/4/892/pdf
[^1_118]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7957270/
[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11555236/
[^1_120]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10932054/
[^1_121]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11908050/
[^1_122]: https://www.mdpi.com/1422-0067/25/5/2743/pdf?version=1709031965
[^1_123]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7385348/
[^1_124]: https://www.mdpi.com/1422-0067/24/24/17633/pdf?version=1702913099
[^1_125]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6441844/
[^1_126]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4116979/
[^1_127]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10252397/
[^1_128]: https://www.mdpi.com/2072-6694/13/14/3428/pdf
[^1_129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11608677/
[^1_130]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3263536/
[^1_131]: http://downloads.hindawi.com/archive/2011/590249.pdf
[^1_132]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11370607/
[^1_133]: https://www.frontiersin.org/articles/10.3389/fncel.2020.600018/full
[^1_134]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8403340/
[^1_135]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10253701/
[^1_136]: https://www.mdpi.com/1422-0067/24/11/9393
[^1_137]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10341066/
[^1_138]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5104636/
[^1_139]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6889222/
[^1_140]: https://www.tandfonline.com/doi/pdf/10.1080/15384047.2015.1056406?needAccess=true
[^1_141]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9728051/
[^1_142]: https://www.tandfonline.com/doi/full/10.2144/fsoa-2023-0136
[^1_143]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7993100/
[^1_144]: https://www.mdpi.com/2072-6694/15/6/1879/pdf?version=1679382163
[^1_145]: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1336476/pdf
[^1_146]: https://onlinelibrary.wiley.com/doi/10.1155/bmri/2004975
[^1_147]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10876826/
[^1_148]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10046791/
[^1_149]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7532506/
[^1_150]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11859630/
[^1_151]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5713271/
[^1_152]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10628205/
[^1_153]: https://www.mdpi.com/1422-0067/18/11/2301/pdf
[^1_154]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8904718/
[^1_155]: https://www.frontiersin.org/articles/10.3389/fcell.2022.833938/pdf
[^1_156]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10994782/
[^1_157]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8585801/
[^1_158]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6059807/
[^1_159]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10193886/
[^1_160]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5689739/
[^1_161]: https://res.mdpi.com/d_attachment/ijms/ijms-21-00888/article_deploy/ijms-21-00888-v2.pdf
[^1_162]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3218606/
[^1_163]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7037280/
[^1_164]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4798262/
[^1_165]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1603783/
[^1_166]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5989280/
[^1_167]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11372124/
[^1_168]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2933693/
[^1_169]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8908177/
[^1_170]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10513942/
[^1_171]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10640286/
[^1_172]: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1326753/pdf
[^1_173]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4878508/
[^1_174]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3376853/
[^1_175]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3427296/
[^1_176]: https://www.embopress.org/doi/10.1002/emmm.201200206
[^1_177]: https://figshare.com/articles/journal_contribution/Supplementary_Figure_1_from_Proteolytic_Processing_Converts_the_Repelling_Signal_Sema3E_into_an_Inducer_of_Invasive_Growth_and_Lung_Metastasis/22363310/1/files/39807509.pdf
[^1_178]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2912208/
[^1_179]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6539029/
[^1_180]: http://jcs.biologists.org/content/122/11/1723.full.pdf
[^1_181]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12049150/
[^1_182]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10038739/
[^1_183]: https://www.hindawi.com/journals/gr/2023/1184101/
[^1_184]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4544656/
[^1_185]: https://www.mdpi.com/1422-0067/22/16/8428/pdf
[^1_186]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8395085/
[^1_187]: https://www.mdpi.com/2218-273X/14/4/480/pdf?version=1713173204
[^1_188]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6468848/
[^1_189]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6499328/```


<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Prompt:

Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: [LINC01727, AC117464.1, XYLT1, MMD2, EEPD1, AC013265.1, MYO5B, PLA2G4A, KCNIP1, ITGB4, AC019068.1, UNC5D, MIR3681HG, LINC02125, LINC02246, LRRC4C, LUCAT1, MDGA2, AC077690.1, CTXND1, AL353138.1, CDH18, MN1, AL356737.2, NKAIN3, CD44, NLRC5, LINC01776, LINC01117, DAB1, GFAP, DCHS2, DIPK1C, COL20A1, ELMOD1, ERICH3, ADAMTS5, GPC5, CHST8, AC233296.1, AC124254.2, NPR3, HRH1, INPP4B, AL159156.1, LINC02328, ARC, PDZRN4, AC007344.1, RGMA, PPARGC1A, TNR, ST8SIA5, ST8SIA1, SLC7A11]
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
    "LINC01727", "AC117464.1", "XYLT1", "MMD2", "EEPD1", "AC013265.1", "MYO5B", "PLA2G4A", "KCNIP1", "ITGB4", "AC019068.1", "UNC5D", "MIR3681HG", "LINC02125", "LINC02246", "LRRC4C", "LUCAT1", "MDGA2", "AC077690.1", "CTXND1", "AL353138.1", "CDH18", "MN1", "AL356737.2", "NKAIN3", "CD44", "NLRC5", "LINC01776", "LINC01117", "DAB1", "GFAP", "DCHS2", "DIPK1C", "COL20A1", "ELMOD1", "ERICH3", "ADAMTS5", "GPC5", "CHST8", "AC233296.1", "AC124254.2", "NPR3", "HRH1", "INPP4B", "AL159156.1", "LINC02328", "ARC", "PDZRN4", "AC007344.1", "RGMA", "PPARGC1A", "TNR", "ST8SIA5", "ST8SIA1", "SLC7A11"
  ],
  "programs": [
    {
      "program_name": "Mesenchymal Invasion and ECM Remodeling",
      "description": "Co-activation of genes encoding ECM receptors and remodeling proteins (CD44, ITGB4, ADAMTS5, PLA2G4A, COL20A1, CHST8, XYLT1, GPC5, TNR) promote invasive, mesenchymal state and facilitate glioblastoma cell migration through the brain parenchyma. Many are upregulated in GBM with mesenchymal phenotype, linked to recurrent tumors and poor prognosis.",
      "atomic_biological_processes": [
        {
          "name": "ECM remodeling and invasion",
          "citation": [
            {"url": "https://www.mdpi.com/1422-0067/24/5/4891", "source_id": "17", "notes": "Systematic review of glioblastoma ECM modification and invasion."},
            {"url": "https://pubmed.ncbi.nlm.nih.gov/37784103", "source_id": "162", "notes": "CD44-driven GBM invasion."}
          ],
          "genes": ["CD44", "ITGB4", "PLA2G4A", "COL20A1", "CHST8", "XYLT1", "GPC5", "TNR", "ADAMTS5"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Extracellular matrix, focal adhesion, invadopodia",
          "citation": [
            {"url": "https://www.mdpi.com/1422-0067/24/5/4891", "source_id": "17", "notes": "Detailed structure of ECM in glioblastoma."}
          ],
          "genes": ["CD44", "ITGB4", "TNR", "COL20A1"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced migratory capacity and brain infiltration",
        "Therapy resistance via ECM protection",
        "Recurrence after surgical resection"
      ],
      "evidence_summary": "Combinatorial upregulation of ECM modifying enzymes and receptors closely correlates with highly invasive glioblastoma subtypes and correlates with poor patient outcomes.",
      "significance_score": 0.98,
      "citations": [
        {"url": "https://www.mdpi.com/1422-0067/24/5/4891", "source_id": "17", "notes": "Comprehensive review evidencing ECM gene upregulation in GBM."},
        {"url": "https://pubmed.ncbi.nlm.nih.gov/37784103", "source_id": "162", "notes": "CD44 role in GBM invasion and recurrence."}
      ],
      "supporting_genes": ["CD44", "ITGB4", "PLA2G4A", "ADAMTS5", "COL20A1", "CHST8", "XYLT1", "GPC5", "TNR"],
      "required_genes_not_in_input": {
        "genes": ["MMP2", "MMP9", "Hyaluronan synthases"],
        "citations": [
          {"url": "https://www.mdpi.com/1422-0067/24/5/4891", "source_id": "17", "notes": "Matrix metalloproteinases are classical ECM modulators critical for GBM invasion."}
        ]
      }
    },
    {
      "program_name": "Cancer Stemness, Plasticity, and Therapy Resistance",
      "description": "Markers of stem cell phenotype (GFAP, CD44, SLC7A11, GPC5, LUCAT1, PPARGC1A) and key regulatory lncRNAs enable glioblastoma cells to maintain stem-like state, resist differentiation, and survive stressors including hypoxia and chemotherapy.",
      "atomic_biological_processes": [
        {
          "name": "Stem cell maintenance and chemoresistance",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/pmc/articles/PMC9481599/", "source_id": "6", "notes": "Glioma stem cell involvement in therapy resistance."}
          ],
          "genes": ["GFAP", "CD44", "SLC7A11", "PPARGC1A"]
        },
        {
          "name": "Hypoxia-responsive regulation",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11001947/", "source_id": "151", "notes": "LUCAT1 and hypoxia response in GBM."}
          ],
          "genes": ["LUCAT1", "PPARGC1A"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Cancer stem cell niche",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/pmc/articles/PMC9481599/", "source_id": "6", "notes": "GBM stem cell niche and therapy resistance."}
          ],
          "genes": ["GFAP", "CD44"]
        }
      ],
      "predicted_cellular_impact": [
        "Maintains cell population capable of recurrence after therapy",
        "Resistance to chemoradiation",
        "Adaptation to hypoxic, nutrient-poor microenvironments"
      ],
      "evidence_summary": "Stem cell features in GBM are driven by combined action of key protein and lncRNA markers, with strong experimental evidence linking their expression to therapy failure, recurrence, and poor survival.",
      "significance_score": 0.95,
      "citations": [
        {"url": "https://pmc.ncbi.nlm.nih.gov/pmc/articles/PMC9481599/", "source_id": "6", "notes": "Role of stem cells in GBM therapy resistance."},
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11001947/", "source_id": "151", "notes": "LUCAT1 function in hypoxia response in glioblastoma."}
      ],
      "supporting_genes": ["GFAP", "CD44", "SLC7A11", "GPC5", "LUCAT1", "PPARGC1A"],
      "required_genes_not_in_input": {
        "genes": ["SOX2", "NES", "OLIG2", "CD133"],
        "citations": [
          {"url": "https://pmc.ncbi.nlm.nih.gov/pmc/articles/PMC9481599/", "source_id": "6", "notes": "Classical cancer stem cell markers for glioblastoma stemness."}
        ]
      }
    },
    {
      "program_name": "Immune Evasion and Immune Microenvironment Interaction",
      "description": "NLRC5, SLC7A11, and lncRNAs interact to modulate antigen presentation and redox state in glioblastoma, facilitating immune escape. Additional ECM–related genes assist in constructing immunosuppressive niches.",
      "atomic_biological_processes": [
        {
          "name": "MHC class I antigen presentation",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2919433/", "source_id": "34", "notes": "NLRC5 function as MHC class I transactivator."}
          ],
          "genes": ["NLRC5"]
        },
        {
          "name": "Suppression of ferroptosis and redox modulation",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7484322/", "source_id": "13", "notes": "SLC7A11 as ferroptosis inhibitor in cancer, including GBM."}
          ],
          "genes": ["SLC7A11"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Immune suppressive microenvironment",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6684490/", "source_id": "41", "notes": "Epigenetic and metabolic barriers to immune attack in GBM."}
          ],
          "genes": ["NLRC5", "SLC7A11"]
        }
      ],
      "predicted_cellular_impact": [
        "Evades T cell recognition",
        "Promotes redox homeostasis and resistance to immune cell mediated killing",
        "Maintains local immunosuppressive microenvironment"
      ],
      "evidence_summary": "GBM exploits regulatory networks (e.g., NLRC5-mediated antigen presentation and SLC7A11-driven ferroptosis suppression) to diminish immune cell killing and minimize antitumor responses.",
      "significance_score": 0.90,
      "citations": [
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2919433/", "source_id": "34", "notes": "NLRC5 as central regulator of MHC class I."},
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7484322/", "source_id": "13", "notes": "SLC7A11 axes and ferroptosis–immune crosstalk in GBM."}
      ],
      "supporting_genes": ["NLRC5", "SLC7A11"],
      "required_genes_not_in_input": {
        "genes": ["PD-L1", "IDH1", "MGMT", "CD274"],
        "citations": [
          {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6684490/", "source_id": "41", "notes": "Immune checkpoints integrated in GBM immune evasion programs."}
        ]
      }
    },
    {
      "program_name": "Proliferation and Aberrant Cell Cycle Regulation",
      "description": "PPARGC1A, KCNIP1, INPP4B, PLA2G4A, CD44, and specific lncRNAs (e.g., LUCAT1) coordinate metabolic and cell cycle programs to support high proliferative rates of glioblastoma cells.",
      "atomic_biological_processes": [
        {
          "name": "Mitochondrial biogenesis and metabolism",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4920288/", "source_id": "191", "notes": "PGC1α drives OXPHOS and metabolic adaptation in invasive and metastatic cancer."}
          ],
          "genes": ["PPARGC1A"]
        },
        {
          "name": "PI3K/AKT signaling modulation",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/35330704", "source_id": "127", "notes": "INPP4B tumor suppressor role, inhibits GBM cell proliferation via PI3K/AKT axis."}
          ],
          "genes": ["INPP4B"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Mitochondria, cytoplasm",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4920288/", "source_id": "191", "notes": "PGC1α required for metastatic phenotype via mitochondrial adaptation."}
          ],
          "genes": ["PPARGC1A"]
        }
      ],
      "predicted_cellular_impact": [
        "Increased proliferation and metabolic flexibility",
        "Survival under nutrient and hypoxia stress",
        "Therapy resistance through metabolic adaptation"
      ],
      "evidence_summary": "GBM cells combine multiple metabolic, signaling, and lncRNA-mediated programs to facilitate rapid growth and evade cell death.",
      "significance_score": 0.93,
      "citations": [
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4920288/", "source_id": "191", "notes": "PGC1α and metabolic adaptation in cancer invasion."},
        {"url": "https://pubmed.ncbi.nlm.nih.gov/35330704", "source_id": "127", "notes": "PI3K/AKT pathway regulation by INPP4B in GBM."}
      ],
      "supporting_genes": ["PPARGC1A", "KCNIP1", "INPP4B", "PLA2G4A", "CD44", "LUCAT1"],
      "required_genes_not_in_input": {
        "genes": ["EGFR", "PI3KCA", "PDGFRA"],
        "citations": [
          {"url": "https://pubmed.ncbi.nlm.nih.gov/35330704", "source_id": "127", "notes": "Receptor tyrosine kinases as classical GBM proliferation drivers."}
        ]
      }
    },
    {
      "program_name": "Aberrant Neural and Synaptic Programs",
      "description": "Genes encoding cell adhesion molecules, synaptic scaffolding proteins, and neural developmental regulators (UNC5D, LRRC4C, MDGA2, ARC, KCNIP1, ST8SIA1, ST8SIA5) are often upregulated in glioblastoma, supporting tumor-neuronal communication, invasion, and plasticity.",
      "atomic_biological_processes": [
        {
          "name": "Neuronal–glioma synaptic remodeling",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10611371/", "source_id": "170", "notes": "Glioma synapses and adaptive plasticity mechanisms in GBM."}
          ],
          "genes": ["ARC", "ST8SIA1", "ST8SIA5", "UNC5D", "MDGA2"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Synaptic junctions, neural cell adhesion complexes",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10611371/", "source_id": "170", "notes": "Synaptic network architecture in glioma."}
          ],
          "genes": ["ARC", "MDGA2", "ST8SIA1", "ST8SIA5", "UNC5D"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced tumor–neuron electrical coupling",
        "Network remodeling favoring tumor invasion",
        "Synaptic plasticity supporting proliferation and migration"
      ],
      "evidence_summary": "Glioblastoma cells hijack neural developmental and synaptic mechanisms to interact with surrounding neural circuits, fostering malignant phenotypes.",
      "significance_score": 0.90,
      "citations": [
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10611371/", "source_id": "170", "notes": "Role of glioma synapses in cell network remodeling."}
      ],
      "supporting_genes": ["ARC", "MDGA2", "ST8SIA1", "ST8SIA5", "UNC5D"],
      "required_genes_not_in_input": {
        "genes": ["NRXN1", "NLGN1", "SHANK3"],
        "citations": [
          {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10611371/", "source_id": "170", "notes": "Key synaptic network molecules in brain tumor neural crosstalk."}
        ]
      }
    }
  ],
  "method": {
    "clustering_basis": [
      "Pathway databases",
      "Co-citation in glioblastoma literature",
      "Gene co-expression evidence",
      "Protein–protein interaction and network analysis"
    ],
    "notes": "Program clusters supported by convergent literature, multi-gene co-expression, PPI, and functional redundancy; prioritization based on presence of multiple required pathway components and links to malignant cell states."
  },
  "version": "2025-11-14"
}
<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_18][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_19][^1_190][^1_191][^1_192][^1_193][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5907913/
[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4783030/
[^1_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5335262/
[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3955956/
[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9953941/
[^1_6]: https://www.mdpi.com/2072-6694/15/13/3458/pdf?version=1688194126
[^1_7]: https://www.frontiersin.org/articles/10.3389/fcell.2023.1221671/pdf?isPublishedV2=False
[^1_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8971704/
[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10891132/
[^1_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11859122/
[^1_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11577153/
[^1_12]: https://onlinelibrary.wiley.com/doi/10.1002/ctm2.70257
[^1_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8310547/
[^1_14]: https://www.frontiersin.org/articles/10.3389/fmolb.2022.904098/pdf
[^1_15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8904967/
[^1_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8897698/
[^1_17]: https://www.mdpi.com/2072-6694/15/6/1879/pdf?version=1679382163
[^1_18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10046791/
[^1_19]: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1336476/pdf
[^1_20]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10876826/
[^1_21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6782606/
[^1_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11308147/
[^1_23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9145282/
[^1_24]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8414390/
[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11908050/
[^1_26]: https://www.mdpi.com/2072-6694/15/3/946/pdf?version=1675391906
[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9913267/
[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6286943/
[^1_29]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jcmm.17140
[^1_30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8899163/
[^1_31]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4461378/
[^1_32]: http://www.jlr.org/content/45/2/205.full.pdf
[^1_33]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3289513/
[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2922274/
[^1_35]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4875496/
[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11044055/
[^1_37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7884647/
[^1_38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4950760/
[^1_39]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3345046/
[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3391022/
[^1_41]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9952003/
[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4884578/
[^1_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7066386/
[^1_44]: http://downloads.hindawi.com/journals/bmri/2016/7487313.pdf
[^1_45]: https://www.frontiersin.org/articles/10.3389/fsurg.2016.00011/pdf
[^1_46]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10813491/
[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11794508/
[^1_48]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/cns.14217
[^1_49]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10646304/
[^1_50]: https://www.mdpi.com/1422-0067/18/12/2774/pdf
[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8200817/
[^1_52]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9451528/
[^1_53]: https://www.mdpi.com/2073-4409/10/8/2066/pdf
[^1_54]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7409063/
[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8773537/
[^1_56]: https://www.mdpi.com/2073-4409/9/1/96/pdf
[^1_57]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11698767/
[^1_58]: https://www.mdpi.com/2072-6694/16/13/2298/pdf?version=1719045025
[^1_59]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11240393/
[^1_60]: https://www.frontiersin.org/articles/10.3389/fnmol.2021.633719/pdf
[^1_61]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11385527/
[^1_62]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8021962/
[^1_63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4365714/
[^1_64]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9723066/
[^1_65]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3235977/
[^1_66]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7788295/
[^1_67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9366078/
[^1_68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11011684/
[^1_69]: https://www.frontiersin.org/articles/10.3389/fonc.2019.00812/pdf
[^1_70]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8215594/
[^1_71]: https://www.mdpi.com/1422-0067/25/8/4438/pdf?version=1713427036
[^1_72]: https://journals.lww.com/10.1097/MD.0000000000039205
[^1_73]: http://www.jbc.org/content/282/25/18129.full.pdf
[^1_74]: http://www.jbc.org/content/280/33/29820.full.pdf
[^1_75]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2748278
[^1_76]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8307702/
[^1_77]: https://www.mdpi.com/2075-1729/11/7/708/pdf
[^1_78]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1933414/
[^1_79]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2905941/
[^1_80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7118801/
[^1_81]: https://www.mdpi.com/2073-4409/12/9/1219/pdf?version=1682239536
[^1_82]: https://www.mdpi.com/2227-9059/12/3/572/pdf?version=1709562376
[^1_83]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6932748/
[^1_84]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10256685/
[^1_85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5986151/
[^1_86]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9048137/
[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5017143/
[^1_88]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2854115/
[^1_89]: https://www.mdpi.com/2073-4409/12/23/2758/pdf?version=1701510975
[^1_90]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4161890/
[^1_91]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9455737/
[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10453990/
[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10628944/
[^1_94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10706364/
[^1_95]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8479294/
[^1_96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10106153/
[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5123285/
[^1_98]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1525233/
[^1_99]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5732324/
[^1_100]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7269909/
[^1_101]: https://www.frontiersin.org/articles/10.3389/fimmu.2017.01748/pdf
[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8729785/
[^1_103]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6305344/
[^1_104]: https://www.frontiersin.org/articles/10.3389/fnmol.2018.00472/pdf
[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9339490/
[^1_106]: https://www.mdpi.com/2072-6694/15/3/849/pdf?version=1675070833
[^1_107]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11369983/
[^1_108]: https://www.frontiersin.org/articles/10.3389/fnins.2020.595664/pdf
[^1_109]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10418167/
[^1_110]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7734145/
[^1_111]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7960998/
[^1_112]: https://www.mdpi.com/1422-0067/18/11/2369/pdf
[^1_113]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12027600/
[^1_114]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6610052/
[^1_115]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4190379/
[^1_116]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2259449/
[^1_117]: https://www.mdpi.com/1422-0067/26/8/3737
[^1_118]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9138293/
[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4684289/
[^1_120]: https://www.mdpi.com/2072-6694/9/6/57/pdf
[^1_121]: http://www.jbc.org/content/292/7/2795.full.pdf
[^1_122]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11021989/
[^1_123]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5483876/
[^1_124]: https://www.mdpi.com/2072-6694/13/5/944/pdf
[^1_125]: https://esmed.org/MRA/mra/article/download/3994/99193547030
[^1_126]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2879424/
[^1_127]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9487419/
[^1_128]: https://www.frontiersin.org/articles/10.3389/fonc.2022.983537/pdf
[^1_129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4807978/
[^1_130]: https://www.oncotarget.com/lookup/doi/10.18632/oncotarget.6663
[^1_131]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2957372/
[^1_132]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3248162/
[^1_133]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8558642/
[^1_134]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4497843/
[^1_135]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7724090/
[^1_136]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6944026/
[^1_137]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1524865/
[^1_138]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10079750/
[^1_139]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8260465/
[^1_140]: http://www.jbc.org/content/279/20/20807.full.pdf
[^1_141]: http://www.jbc.org/content/277/8/5699.full.pdf
[^1_142]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8916685/
[^1_143]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9582955/
[^1_144]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4896547/
[^1_145]: https://linkinghub.elsevier.com/retrieve/pii/S1535947620304011
[^1_146]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2646508/
[^1_147]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10136350/
[^1_148]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4539765/
[^1_149]: http://www.cell-stress.com/wp-content/uploads/2019/01/2019A-Won-Cell-Stress.pdf
[^1_150]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9219822/
[^1_151]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11300024/
[^1_152]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7844754/
[^1_153]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11249581/
[^1_154]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7409010/
[^1_155]: https://www.frontiersin.org/articles/10.3389/fgene.2024.1416772/full
[^1_156]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11766336/
[^1_157]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8161569/
[^1_158]: https://www.mdpi.com/2072-6694/12/7/1842
[^1_159]: https://www.frontiersin.org/articles/10.3389/fonc.2024.1406186/full
[^1_160]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11011546/
[^1_161]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9339241/
[^1_162]: https://www.mdpi.com/2072-6694/15/19/4898/pdf?version=1696850726
[^1_163]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10572085/
[^1_164]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9138893/
[^1_165]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8539357/
[^1_166]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3999042/
[^1_167]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5464873/
[^1_168]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11269341/
[^1_169]: https://www.mdpi.com/2079-7737/11/2/313/pdf
[^1_170]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10632140/
[^1_171]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9820922/
[^1_172]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9197936/
[^1_173]: https://www.frontiersin.org/articles/10.3389/fgene.2025.1582504/full
[^1_174]: https://www.mdpi.com/1422-0067/22/16/8428/pdf
[^1_175]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8395085/
[^1_176]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7844840/
[^1_177]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9899608/
[^1_178]: https://www.mdpi.com/1422-0067/23/3/1353/pdf
[^1_179]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7398200/
[^1_180]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5783613/
[^1_181]: https://onlinelibrary.wiley.com/doi/10.1111/cns.14839
[^1_182]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5702396/
[^1_183]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10858941/
[^1_184]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11997006/
[^1_185]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5187672/
[^1_186]: https://elifesciences.org/articles/84036
[^1_187]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8440018/
[^1_188]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4642306/
[^1_189]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5465638/
[^1_190]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3976607/
[^1_191]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4369153/
[^1_192]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4757583/
[^1_193]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6620024/```


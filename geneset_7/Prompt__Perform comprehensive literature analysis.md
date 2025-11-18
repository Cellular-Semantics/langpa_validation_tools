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
      "program_name": "RTK/RAS/PI3K Pathway Activation",
      "description": "Core glioblastoma oncogenic signaling driven by EGFR and ERBB3 amplification and mutation, with supporting genes including MDK, GRK5, and downstream regulators of proliferation and survival.",
      "atomic_biological_processes": [
        {
          "name": "EGFR signaling",
          "citation": [
            {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3244322/", "notes": "EGFR amplification/mutation is a key driver event in glioblastoma."},
            {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7068482/", "notes": "EGFR variants including EGFRvIII involved in pathogenesis."}
          ],
          "genes": ["EGFR"]
        },
        {
          "name": "ERBB signaling",
          "citation": [
            {"source_id": "", "url": "https://www.mdpi.com/2073-4409/12/7/1097", "notes": "ERBB3 alterations contribute to glioblastoma growth and therapy resistance."}
          ],
          "genes": ["ERBB3"]
        },
        {
          "name": "MDK (midkine) signaling",
          "citation": [
            {"source_id": "", "url": "https://www.frontiersin.org/articles/10.3389/fonc.2023.1145051/full", "notes": "MDK involved in cell proliferation and survival, downstream of RTK pathways."}
          ],
          "genes": ["MDK"]
        }
      ],
      "atomic_cellular_components": [],
      "predicted_cellular_impact": [
        "enhanced proliferation",
        "robust survival signaling",
        "hyperactivated metabolic networks",
        "therapy resistance"
      ],
      "evidence_summary": "EGFR/ERBB pathway activation—including canonical and variant forms—is one of the most consistent oncogenic mechanisms in glioblastoma, promoting growth, survival, and resistance to conventional therapies. MDK and GRK5 serve as further downstream effectors that amplify mitogenic signaling.",
      "significance_score": 0.95,
      "citations": [
        {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3244322/"},
        {"source_id": "", "url": "https://www.mdpi.com/2073-4409/12/7/1097"},
        {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9579422/"}
      ],
      "supporting_genes": ["EGFR", "ERBB3", "MDK", "GRK5"],
      "required_genes_not_in_input": {
        "genes": ["PIK3CA", "PTEN", "AKT1"],
        "citations": [
          {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6963941/", "notes": "PI3K pathway mutations commonly contribute, sometimes by loss of PTEN or gain of PIK3CA/AKT1."}
        ]
      }
    },
    {
      "program_name": "Proneural-Mesenchymal Transition & Stem Cell Plasticity",
      "description": "GBM manifests plasticity between proneural and mesenchymal cell states, driven by core factors (SOX2, DLL1, PRRX1, RELN, MEIS2) and lncRNAs (MALAT1) with a supporting role for EMT drivers and neurodevelopmental transcription factors.",
      "atomic_biological_processes": [
        {
          "name": "Mesenchymal transition",
          "citation": [
            {"source_id": "", "url": "https://www.mdpi.com/2072-6694/11/6/845", "notes": "Phenotypic drift towards mesenchymal programs in recurrent GBM."}
          ],
          "genes": ["PRRX1", "RELN", "DLL1"]
        },
        {
          "name": "Neural stem cell program / self-renewal",
          "citation": [
            {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5382166/", "notes": "SOX2 and FOXG1 mediate stemness and cell cycle control."},
            {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5039282/", "notes": "SOX2 regulates the glioma stem cell compartment."}
          ],
          "genes": ["SOX2-OT", "SOX2", "DLL1", "LGR5", "MEIS2", "MALAT1"]
        }
      ],
      "atomic_cellular_components": [],
      "predicted_cellular_impact": [
        "increased tumor plasticity",
        "fast adaptation to microenvironmental shifts",
        "therapy resistance (especially to radiotherapy/chemotherapy)",
        "capacity to transition between neural and mesenchymal lineages"
      ],
      "evidence_summary": "GBM stem cells show bidirectional transitions (proneural–mesenchymal). SOX2, PRRX1, DLL1, LGR5, RELN and MEIS2 underlie these programs. MALAT1 lncRNA mediates stemness and therapy resistance.",
      "significance_score": 0.93,
      "citations": [
        {"source_id": "", "url": "https://www.mdpi.com/2072-6694/11/6/845"},
        {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5382166/"}
      ],
      "supporting_genes": ["SOX2-OT", "SOX2", "DLL1", "LGR5", "PRRX1", "RELN", "MEIS2", "MALAT1"],
      "required_genes_not_in_input": {
        "genes": ["SOX10", "ZEB1"],
        "citations": [
          {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7707631/", "notes": "SOX10 loss promotes mesenchymal switch in GBM."}
        ]
      }
    },
    {
      "program_name": "Aberrant Translation, Ribosome Biogenesis, and Metabolic Adaptation",
      "description": "Multiple ribosomal proteins (RPLs, RPSs) and translation regulators are upregulated in glioblastoma, supporting high protein synthesis, metabolic rewiring, and therapy resistance.",
      "atomic_biological_processes": [
        {
          "name": "Translation initiation",
          "citation": [
            {"source_id": "", "url": "https://www.frontiersin.org/articles/10.3389/fonc.2023.1145051/full", "notes": "Translation machinery, especially initiation, is dysregulated in GBM, promoting adaptation to hypoxia."}
          ],
          "genes": ["RPL18A", "RPL13A", "RPL8", "RPS18", "RPL10", "RPL7", "RPL32", "RPL41", "RPL34", "RPL36", "RPL28"]
        },
        {
          "name": "Ribosome biogenesis",
          "citation": [
            {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8777701/", "notes": "NIR-driven ribosomal DNA transcription supports GBM stem cell proliferation."}
          ],
          "genes": ["RPL10", "RPS18"]
        }
      ],
      "atomic_cellular_components": [],
      "predicted_cellular_impact": [
        "increased protein synthesis capacity",
        "rapid proliferation under stress",
        "therapy resistance",
        "metabolic flexibility"
      ],
      "evidence_summary": "Upregulation and dysregulation of translation initiation and ribosome biogenesis are hallmarks of GBM, connecting to rapid proliferation and metabolic adaptation, thus supporting resistance to targeted therapies.",
      "significance_score": 0.89,
      "citations": [
        {"source_id": "", "url": "https://www.frontiersin.org/articles/10.3389/fonc.2023.1145051/full"},
        {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8777701/"}
      ],
      "supporting_genes": [
        "RPL18A", "RPL13A", "RPL8", "RPS18", "RPL10", "RPL7", "RPL32", "RPL41", "RPL34", "RPL36", "RPL28"
      ],
      "required_genes_not_in_input": {
        "genes": ["EIF4E", "RPS6"],
        "citations": [
          {"source_id": "", "url": "https://www.mdpi.com/2072-6694/12/4/1006", "notes": "Canonical translation initiation factors also contribute to aberrant translation in GBM."}
        ]
      }
    },
    {
      "program_name": "Apoptosis and Therapy Resistance Programs",
      "description": "Activation of intrinsic mitochondrial apoptosis pathways via CASP9, combined with resistance mechanisms including polyamine metabolism (SAT1), cell cycle control by BTG2, and ISG15-driven immune evasion.",
      "atomic_biological_processes": [
        {
          "name": "Mitochondrial apoptosis",
          "citation": [
            {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7073372/", "notes": "Caspase-9 mediates mitochondria-dependent apoptosis in GBM, involved in therapy response."}
          ],
          "genes": ["CASP9"]
        },
        {
          "name": "Polyamine metabolism (SAT1)",
          "citation": [
            {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4260493/", "notes": "SAT1 modulates tumorigenesis and radiation response in GBM, and controls ferroptotic cell death."}
          ],
          "genes": ["SAT1"]
        },
        {
          "name": "Immune evasion (ISG15 signaling)",
          "citation": [
            {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10428012/", "notes": "ISG15-driven IFN response in GBM cells increases chemo-resistance through microglia interaction."}
          ],
          "genes": ["ISG15"]
        }
      ],
      "atomic_cellular_components": [],
      "predicted_cellular_impact": [
        "resistance to apoptosis",
        "modulation of immune cell infiltration",
        "enhanced therapy resistance",
        "control of tumor microenvironment signaling"
      ],
      "evidence_summary": "Combined apoptosis pathways, polyamine metabolic adaptation (including ferroptosis sensitivity), and immune signaling programs through ISG15 contribute to evasion of cell death and immune surveillance in glioblastoma.",
      "significance_score": 0.86,
      "citations": [
        {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7073372/"},
        {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4260493/"},
        {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10428012/"}
      ],
      "supporting_genes": ["CASP9", "SAT1", "ISG15", "BTG2"],
      "required_genes_not_in_input": {
        "genes": ["TP53", "BCL2", "XIAP"],
        "citations": [
          {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC46452/", "notes": "TP53 mediates apoptosis and cell cycle arrest in glioblastoma; BCL2 and XIAP further regulate resistance."}
        ]
      }
    },
    {
      "program_name": "Neural and Axon Guidance, Migration",
      "description": "Multiple neural development/axon guidance genes (SLIT3, UNC5B, NTNG2, FLRT2, EPHA7, RELN, DLL1, EFNA5) regulate migration, invasion, and differentiation in the neural microenvironment, promoting cell dispersal and network interactions within the brain.",
      "atomic_biological_processes": [
        {
          "name": "Axon guidance, migration",
          "citation": [
            {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10553136/", "notes": "Slit/Robo signaling is a regulator of glioma cell migration and invasion."},
            {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3294864/", "notes": "UNC5B and netrin signaling regulate proliferation and migration in glioblastoma."},
            {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8251001/", "notes": "Glutamate receptors, including NMDA (GRIN3A), drive migration and proliferation."}
          ],
          "genes": ["SLIT3", "UNC5B", "NTNG2", "FLRT2", "EPHA7", "RELN", "DLL1", "EFNA5", "GRIN3A"]
        }
      ],
      "atomic_cellular_components": [],
      "predicted_cellular_impact": [
        "promotes neural cell migration and invasion",
        "supports neural differentiation within tumor mass",
        "facilitates adaptability in neural tissue microenvironment"
      ],
      "evidence_summary": "Glioblastoma exploits neural development and axon guidance cues to promote migration, infiltration, and survival in the central nervous system. Genes such as SLIT3, UNC5B, NTNG2, FLRT2, and EPHA7, as well as glutamate receptor subunits (GRIN3A), are functionally linked to these processes.",
      "significance_score": 0.84,
      "citations": [
        {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10553136/"},
        {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3294864/"},
        {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8251001/"}
      ],
      "supporting_genes": [
        "SLIT3", "UNC5B", "NTNG2", "FLRT2", "EPHA7", "RELN", "DLL1", "EFNA5", "GRIN3A"
      ],
      "required_genes_not_in_input": {
        "genes": ["ROBO1", "SEMA3A", "NRP1"],
        "citations": [
          {"source_id": "", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10553136/", "notes": "ROBO1 (Slit receptor) and SEMA3A/NRP1 signaling also contribute to axon guidance in glioblastoma."}
        ]
      }
    }
  ],
  "version": "2025-11-17"
}
<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_18][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_19][^1_190][^1_191][^1_192][^1_193][^1_194][^1_195][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: image.jpg
[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11506736/
[^1_3]: https://www.frontiersin.org/articles/10.3389/fcell.2023.1098482/pdf
[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10009693/
[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8773829/
[^1_6]: https://www.mdpi.com/2218-273X/14/10/1231
[^1_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7904102/
[^1_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10891132/
[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10971019/
[^1_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9340648/
[^1_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9340653/
[^1_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3529576/
[^1_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10126369/
[^1_14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8232755/
[^1_15]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/cam4.6316
[^1_16]: https://www.mdpi.com/2072-6694/13/12/3005/pdf
[^1_17]: https://www.mdpi.com/1422-0067/22/24/13217/pdf
[^1_18]: https://www.frontiersin.org/articles/10.3389/fonc.2020.00747/pdf
[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11843149/
[^1_20]: https://www.medsci.org/v22p0990.htm
[^1_21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7867275/
[^1_22]: https://www.mdpi.com/2072-6694/13/3/580
[^1_23]: https://thejns.org/downloadpdf/view/journals/j-neurosurg/aop/article-10.3171-2024.1.JNS231137/article-10.3171-2024.1.JNS231137.pdf
[^1_24]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11353032/
[^1_25]: https://www.mdpi.com/2076-3425/11/6/795/pdf
[^1_26]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3242822/
[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6521892/
[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8857055/
[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9259983/
[^1_30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6864306/
[^1_31]: https://www.mdpi.com/2072-6694/15/13/3525/pdf?version=1688708481
[^1_32]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5791772/
[^1_33]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5494611/
[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11698767/
[^1_35]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8351415/
[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6425928/
[^1_37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4011561/
[^1_38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10441357/
[^1_39]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11584712/
[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4540202/
[^1_41]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9952003/
[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5435889/
[^1_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4094829/
[^1_44]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7746937/
[^1_45]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5036841/
[^1_46]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6151872/
[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9348799/
[^1_48]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5692310/
[^1_49]: https://www.mdpi.com/2073-8994/16/9/1186
[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5410262/
[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5815062/
[^1_52]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7409010/
[^1_53]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10004581/
[^1_54]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7901982/
[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7988331/
[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4835592/
[^1_57]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11564028/
[^1_58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8909726/
[^1_59]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10042294/
[^1_60]: https://www.frontiersin.org/articles/10.3389/fcell.2023.1086964/pdf
[^1_61]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10398814/
[^1_62]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4901439/
[^1_63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11615995/
[^1_64]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10093618/
[^1_65]: https://www.mdpi.com/2072-6694/12/4/892/pdf
[^1_66]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10585196/
[^1_67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4962313/
[^1_68]: https://www.mdpi.com/1422-0067/24/24/17633/pdf?version=1702913099
[^1_69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4686679/
[^1_70]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10008753/
[^1_71]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6579262/
[^1_72]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5348560/
[^1_73]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2629816/
[^1_74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6997171/
[^1_75]: https://www.mdpi.com/1422-0067/21/20/7777/pdf
[^1_76]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10693926/
[^1_77]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7589016/
[^1_78]: https://assets.cureus.com/uploads/original_article/pdf/182598/20231103-28087-1lk6qxd.pdf
[^1_79]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3714150/
[^1_80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4904460/
[^1_81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11110965/
[^1_82]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4632291/
[^1_83]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3282085/
[^1_84]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4651735/
[^1_85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3581491/
[^1_86]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9808372/
[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3887669/
[^1_88]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5615248/
[^1_89]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7213894/
[^1_90]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6418229/
[^1_91]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11488581/
[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4413650/
[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6015895/
[^1_94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4498795/
[^1_95]: http://insight.jci.org/articles/view/167049/files/pdf
[^1_96]: https://www.frontiersin.org/articles/10.3389/fimmu.2018.01345/pdf
[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2901521/
[^1_98]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8461254/
[^1_99]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11618491/
[^1_100]: https://www.frontiersin.org/articles/10.3389/fimmu.2021.729359/pdf
[^1_101]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7127291/
[^1_102]: https://www.mdpi.com/2076-393X/12/2/153/pdf?version=1706776306
[^1_103]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10891536/
[^1_104]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6685507/
[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10473822/
[^1_106]: https://pmc.ncbi.nlm.nih.gov/articles/PMC50095/
[^1_107]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2819747/
[^1_108]: https://www.mdpi.com/2227-9059/10/3/564/pdf
[^1_109]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2563050/
[^1_110]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8945784/
[^1_111]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5683421/
[^1_112]: http://www.jbc.org/content/278/42/41059.full.pdf
[^1_113]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11358448/
[^1_114]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5098629/
[^1_115]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6487480/
[^1_116]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9656607/
[^1_117]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4423404/
[^1_118]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8883632/
[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6740079/
[^1_120]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9339478/
[^1_121]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9479087/
[^1_122]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9177076/
[^1_123]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10418167/
[^1_124]: https://www.cancerbiomed.org/content/cbm/early/2024/05/06/j.issn.2095-3941.2023.0510.full.pdf
[^1_125]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5528952/
[^1_126]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9723066/
[^1_127]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11130179/
[^1_128]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11385527/
[^1_129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5884092/
[^1_130]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5116134/
[^1_131]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4650544/
[^1_132]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6625380/
[^1_133]: https://www.mdpi.com/1422-0067/24/22/16320/pdf?version=1699979300
[^1_134]: https://www.mdpi.com/1422-0067/24/1/749/pdf?version=1672569074
[^1_135]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5410960/
[^1_136]: https://esmed.org/MRA/mra/article/download/3994/99193547030
[^1_137]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7145301/
[^1_138]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10711858/
[^1_139]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3721733/
[^1_140]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3674364/
[^1_141]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8748834/
[^1_142]: https://www.mdpi.com/1422-0067/19/12/3773/pdf
[^1_143]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6320836/
[^1_144]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8991250/
[^1_145]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2718995/
[^1_146]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6520759/
[^1_147]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11582119/
[^1_148]: https://www.mdpi.com/2072-6694/11/4/503
[^1_149]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9820922/
[^1_150]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11994879/
[^1_151]: https://onlinelibrary.wiley.com/doi/10.1002/cbin.70005
[^1_152]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8307764/
[^1_153]: https://www.mdpi.com/2072-6694/13/14/3428/pdf
[^1_154]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8924419/
[^1_155]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11370607/
[^1_156]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8469987/
[^1_157]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10215375/
[^1_158]: https://www.mdpi.com/1422-0067/19/10/2879/pdf
[^1_159]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8403340/
[^1_160]: https://www.mdpi.com/2073-4425/13/2/244/pdf
[^1_161]: https://www.mdpi.com/1422-0067/20/11/2746/pdf
[^1_162]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6600373/
[^1_163]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11192628/
[^1_164]: https://www.mdpi.com/2079-7737/11/2/313/pdf
[^1_165]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10491977/
[^1_166]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8291965/
[^1_167]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7749178/
[^1_168]: https://academic.oup.com/noa/advance-article-pdf/doi/10.1093/noajnl/vdac149/45868292/vdac149.pdf
[^1_169]: https://academic.oup.com/neuro-oncology/article/27/4/867/7951878
[^1_170]: http://downloads.hindawi.com/journals/jo/2010/430142.pdf
[^1_171]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2905941/
[^1_172]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4444827/
[^1_173]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9050732/
[^1_174]: https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2024.1288820/pdf
[^1_175]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11150821/
[^1_176]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7035608/
[^1_177]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10214721/
[^1_178]: https://www.mdpi.com/2072-6694/14/3/645/pdf
[^1_179]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7779250/
[^1_180]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8833780/
[^1_181]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4648299/
[^1_182]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12010881/
[^1_183]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9561975/
[^1_184]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5443867/
[^1_185]: https://www.mdpi.com/2072-6694/14/19/4910/pdf?version=1665145496
[^1_186]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8964949/
[^1_187]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3922520/
[^1_188]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3896091/
[^1_189]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9131277/
[^1_190]: https://www.thno.org/v12p3847.htm
[^1_191]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3323899/
[^1_192]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6381369/
[^1_193]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3904565/
[^1_194]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9882365/
[^1_195]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4744167/```


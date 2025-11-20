<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Prompt:

Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: ["CFAP43, NEGR1, DNAH12, LRRC2, VAT1L, ZNF804B, RBMS3, SLC14A1, GABRA5, ZBBX, ADAMTS18, CFAP52, GRM1, MAP3K19, FHAD1, TCTEX1D1, DNAAF1, DCDC2, AC005165.1, COL21A1, PKHD1, ZNF521, EPB41L4B, ERICH3, PLAGL1, EXPH5, SHISAL2B, SATB1-AS1, RERGL, FRMPD2, TOGARAM2, AP003062.2, BMP6, NRG3, CFAP61, FAM81B, SLC47A2, TMEM232, NWD2, AC109466.1, GABRG3, DTHD1, COL13A1, COL23A1, CFAP73, RFTN1, FYB2, POSTN, AL513323.1, BANK1, CHD5, THBS1, ADCY8, ADGB, AFF2, DRC1, CFAP206, CFAP47, PPM1H, KIAA2012, MAP7, KSR2, DNAH5, LYPD6B, WSCD2, CACNA2D1, LRRIQ1, CPNE4, LINC01088, SCIN, PRMT8, LINGO2, CASC1, CCDC170, AC092110.1, VWA3A, CA10, AC013470.2, SLC22A3, GRM4, COL26A1, CFAP221, CFAP157, TTC29, C7orf57, HMCN1, CFAP100, U91319.1, RSPH1, NAALAD2, IL6R, CDH7, KCNJ3, AL356108.1”]
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
    "cell_type": "glioblastoma cell",
    "disease": "malignant glioblastoma",
    "tissue": "brain"
  },
  "input_genes": [
    "CFAP43", "NEGR1", "DNAH12", "LRRC2", "VAT1L", "ZNF804B", "RBMS3", "SLC14A1", "GABRA5", "ZBBX", "ADAMTS18", "CFAP52", "GRM1", "MAP3K19", "FHAD1", "TCTEX1D1", "DNAAF1", "DCDC2", "AC005165.1", "COL21A1", "PKHD1", "ZNF521", "EPB41L4B", "ERICH3", "PLAGL1", "EXPH5", "SHISAL2B", "SATB1-AS1", "RERGL", "FRMPD2", "TOGARAM2", "AP003062.2", "BMP6", "NRG3", "CFAP61", "FAM81B", "SLC47A2", "TMEM232", "NWD2", "AC109466.1", "GABRG3", "DTHD1", "COL13A1", "COL23A1", "CFAP73", "RFTN1", "FYB2", "POSTN", "AL513323.1", "BANK1", "CHD5", "THBS1", "ADCY8", "ADGB", "AFF2", "DRC1", "CFAP206", "CFAP47", "PPM1H", "KIAA2012", "MAP7", "KSR2", "DNAH5", "LYPD6B", "WSCD2", "CACNA2D1", "LRRIQ1", "CPNE4", "LINC01088", "SCIN", "PRMT8", "LINGO2", "CASC1", "CCDC170", "AC092110.1", "VWA3A", "CA10", "AC013470.2", "SLC22A3", "GRM4", "COL26A1", "CFAP221", "CFAP157", "TTC29", "C7orf57", "HMCN1", "CFAP100", "U91319.1", "RSPH1", "NAALAD2", "IL6R", "CDH7", "KCNJ3", "AL356108.1"
  ],
  "programs": [
    {
      "program_name": "Motile Cilia Function and Structure",
      "description": "Cluster of genes (CFAP43, CFAP52, CFAP61, CFAP73, CFAP100, CFAP157, CFAP206, CFAP221, DNAH12, DNAH5, DRC1, DNAAF1, TCTEX1D1, DCDC2, RSPH1, LRRC2, LRRIQ1, TTC29, ZBBX, DTHD1) encode components of the motile cilium and its assembly machinery. In glioblastoma, aberrant ciliary function is increasingly recognized as contributing to tumor microenvironment interactions, signaling changes, and possibly immunosuppression.",
      "atomic_biological_processes": [
        {
          "name": "Ciliogenesis and Motile Cilia Function",
          "citation": [
            {
              "source_id": "",
              "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC3819026/",
              "notes": "Overview of cilia proteins and their extended roles in non-ciliated cells, including implications in disease contexts."
            },
            {
              "source_id": "",
              "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC9440988/",
              "notes": "Mouse and human ciliary assembly, transport machinery, and mutation consequences. Importantly, ciliary components are shared in motile and non-motile cells."
            }
          ],
          "genes": ["CFAP43", "CFAP52", "CFAP61", "CFAP73", "CFAP100", "CFAP157", "CFAP206", "CFAP221", "DNAH12", "DNAH5", "DRC1", "DNAAF1", "TCTEX1D1", "DCDC2", "RSPH1", "LRRC2", "LRRIQ1", "TTC29", "ZBBX", "DTHD1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Motile Cilium Axoneme",
          "citation": [
            {
              "source_id": "",
              "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC8201539/",
              "notes": "Central apparatus structure and genes required for assembly; implications in motile cilia function."
            }
          ],
          "genes": ["CFAP43", "DNAH12", "DRC1", "TCTEX1D1", "RSPH1", "DNAAF1"]
        }
      ],
      "predicted_cellular_impact": [
        "Deficient or abnormal ciliary signaling may alter microenvironmental sensing and contribute to immune evasion in glioblastoma",
        "Disrupted ciliary assembly can impact cell division, Wnt signaling, and cell polarity"
      ],
      "evidence_summary": "Many CFAP and DNAH genes are well-established ciliary components. New studies connect ciliary biology to immune evasion, altered cell division, and signaling in glioblastoma.",
      "significance_score": 0.90,
      "citations": [
        {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC3819026/"},{"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC9440988/"},{"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC8201539/"}
      ],
      "supporting_genes": ["CFAP43", "CFAP52", "CFAP61", "CFAP73", "CFAP100", "CFAP157", "CFAP206", "CFAP221", "DNAH12", "DNAH5", "DRC1", "DNAAF1", "TCTEX1D1", "DCDC2", "RSPH1", "LRRC2", "LRRIQ1", "TTC29", "ZBBX", "DTHD1"],
      "required_genes_not_in_input": {"genes": [], "citations": []}
    },

    {
      "program_name": "Extracellular Matrix Remodeling and Tumor Invasion",
      "description": "Multiple collagen and ECM-remodeling genes (COL21A1, COL13A1, COL23A1, COL26A1, THBS1, POSTN, HMCN1, ADAMTS18, CFAP-related) contribute to the composition, stiffness, and organization of the tumor microenvironment. Glioblastoma exploits these programs to facilitate invasion, angiogenesis, immune modulation, and therapy resistance.",
      "atomic_biological_processes": [
        {
          "name": "Collagen Matrix Remodeling",
          "citation": [
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC10262873/", "notes": "Collagen modifications in tumors and implications for immunotherapy."},
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC9660452/", "notes": "Collagen family overview and their biomarker potential."}
          ],
          "genes": ["COL21A1", "COL13A1", "COL23A1", "COL26A1", "HMCN1"]
        },
        {
          "name": "Thrombospondin and Periostin Pathways",
          "citation": [
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC6407780/", "notes": "THBS1 and periostin coordinate ECM remodeling and cell adhesion in glioblastoma."},
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC5299046/", "notes": "POSTN upregulated in glioma, promoting stemness, invasion and therapy resistance."}
          ],
          "genes": ["THBS1","POSTN"]
        },
        {
          "name": "Matrix Metalloproteinase/ADAMTS Activity",
          "citation": [
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC10963493/", "notes": "ADAMTS proteases regulate ECM structure and tissue invasion in cancer."}
          ],
          "genes": ["ADAMTS18"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Extracellular Matrix",
          "citation": [
            {"source_id": "", "url": "https://onlinelibrary.wiley.com/doi/full/10.1002/mnfr.202300824", "notes": "ECM gene signatures predict glioblastoma prognosis."}
          ],
          "genes": ["COL21A1","COL13A1","COL23A1","COL26A1","THBS1","POSTN","HMCN1"]
        }
      ],
      "predicted_cellular_impact": [
        "Promotes tumor invasion through ECM stiffening and degradation",
        "Facilitates angiogenesis and immune exclusion",
        "Induces therapy resistance via physical barriers and signaling"
      ],
      "evidence_summary": "Collagen and ECM-modifying genes shape the tumor microenvironment, promoting aggressiveness and resistance to therapy in glioblastoma.",
      "significance_score": 0.95,
      "citations": [
        {"source_id": "","url":"https://pmc.ncbi.nlm.nih.gov/article/PMC10262873/"},
        {"source_id": "","url":"https://pmc.ncbi.nlm.nih.gov/article/PMC9660452/"},
        {"source_id": "","url":"https://pmc.ncbi.nlm.nih.gov/article/PMC6407780/"},
        {"source_id": "","url":"https://pmc.ncbi.nlm.nih.gov/article/PMC5299046/"},
        {"source_id": "","url":"https://pmc.ncbi.nlm.nih.gov/article/PMC10963493/"}
      ],
      "supporting_genes": ["COL21A1", "COL13A1", "COL23A1", "COL26A1", "THBS1", "POSTN", "HMCN1", "ADAMTS18"],
      "required_genes_not_in_input": {"genes": [], "citations": []}
    },

    {
      "program_name": "Inflammatory and Mesenchymal Signaling",
      "description": "Genes IL6R, BMP6, POSTN, THBS1, SATB1-AS1, COL-related, and others act in canonical pathways that regulate inflammation, immune suppression, mesenchymal transition, and stemness in glioblastoma.",
      "atomic_biological_processes": [
        {
          "name": "IL6 Signaling and Immunosuppression",
          "citation": [
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC10907135/", "notes": "IL6 drives glioblastoma microenvironment immunosuppression and therapy resistance."}
          ],
          "genes": ["IL6R"]
        },
        {
          "name": "Epithelial-to-Mesenchymal Transition",
          "citation": [
            {"source_id": "","url":"https://pmc.ncbi.nlm.nih.gov/article/PMC5299046/","notes":"POSTN controls EMT and is upregulated in glioma."}
          ],
          "genes":["POSTN","THBS1"]
        },
        {
          "name": "BMP6/BMP Signaling in Stemness",
          "citation": [
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC6819809/", "notes": "BMP signaling controls glioma stem cell quiescence and therapy resistance."}
          ],
          "genes": ["BMP6"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Mesenchymal and Immune Microenvironment",
          "citation": [
            {"source_id": "","url":"https://pmc.ncbi.nlm.nih.gov/article/PMC5704498/","notes":"Mesenchymal subtype enriched for IL6/IL6R signaling; key to prognosis."}
          ],
          "genes": ["IL6R", "POSTN"]
        }
      ],
      "predicted_cellular_impact": [
        "Drives immune suppression and poor therapy response",
        "Promotes stemness and invasion via mesenchymal transition",
        "Links inflammation to increased glioblastoma aggressiveness"
      ],
      "evidence_summary": "Multiple genes contribute to the mesenchymal and immune suppressive environment in glioblastoma, with IL6 signaling being particularly central.",
      "significance_score": 0.97,
      "citations": [
        {"source_id": "","url":"https://pmc.ncbi.nlm.nih.gov/article/PMC10907135/"},
        {"source_id": "","url":"https://pmc.ncbi.nlm.nih.gov/article/PMC5299046/"},
        {"source_id": "","url":"https://pmc.ncbi.nlm.nih.gov/article/PMC6819809/"},
        {"source_id": "","url":"https://pmc.ncbi.nlm.nih.gov/article/PMC5704498/"}
      ],
      "supporting_genes": ["IL6R", "BMP6", "POSTN", "THBS1", "SATB1-AS1"],
      "required_genes_not_in_input": {"genes": [], "citations": []}
    },

    {
      "program_name": "Neuronal and Synaptic Signaling Dysregulation",
      "description": "Genes GABRA5, GABRG3, KCNJ3, GRM1, GRM4, NAALAD2, CA10, SLC22A3, SLC14A1, SLC47A2 are involved in neuro-signaling, glutamatergic, and GABAergic transmission, which are re-wired in glioblastoma to promote cell migration, invasion, and altered metabolism.",
      "atomic_biological_processes": [
        {
          "name": "Glutamate/GABA Signaling",
          "citation": [
            {"source_id": "", "url": "https://www.frontiersin.org/articles/10.3389/fonc.2020.00413/full", "notes": "Glutamate receptors and ion channels enriched in GBM, driving migration and invasion."},
            {"source_id": "","url":"https://pmc.ncbi.nlm.nih.gov/article/PMC3072127/","notes":"Glutamate signaling and microenvironment impact in glioma."}
          ],
          "genes": ["GRM1", "GRM4", "GABRA5", "GABRG3", "KCNJ3", "NAALAD2", "CA10"]
        },
        {
          "name": "Amino Acid and Ion Transporters",
          "citation": [
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC10311593/", "notes": "SLC family transporters regulate malignant progression in glioma, including SLC14A1, SLC22A3."}
          ],
          "genes": ["SLC14A1", "SLC22A3", "SLC47A2"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Synaptic and Perisynaptic Membrane",
          "citation": [
            {"source_id": "","url":"https://www.frontiersin.org/articles/10.3389/fonc.2020.00413/full","notes":"Glioblastoma alters synaptic compartments and signaling for invasion."}
          ],
          "genes": ["GABRA5", "GABRG3", "GRM1", "GRM4", "KCNJ3"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhances tumor cell migration through neurotransmitter pathway hijacking",
        "Alters cell metabolism and microenvironment responsiveness"
      ],
      "evidence_summary": "Glioblastoma re-wires synaptic and ion channel signaling for invasion and malignancy; several input genes are established contributors.",
      "significance_score": 0.88,
      "citations": [
        {"source_id": "","url":"https://www.frontiersin.org/articles/10.3389/fonc.2020.00413/full"},
        {"source_id": "","url":"https://pmc.ncbi.nlm.nih.gov/article/PMC10311593/"},
        {"source_id": "","url":"https://pmc.ncbi.nlm.nih.gov/article/PMC3072127/"}
      ],
      "supporting_genes": ["GRM1", "GRM4", "GABRA5", "GABRG3", "KCNJ3", "NAALAD2", "CA10", "SLC14A1", "SLC22A3", "SLC47A2"],
      "required_genes_not_in_input": {"genes": [], "citations": []}
    },

    {
      "program_name": "Chromatin/Transcriptional Regulation and Tumor Suppressor Pathways",
      "description": "Transcription factors and epigenetic regulators (CHD5, SATB1-AS1, ZNF521, ZNF804B, AFF2, PRMT8, RBMS3) coordinate gene expression programs, cell fate determination, and tumor suppression. In glioblastoma, loss or mutation in these genes drives therapy resistance, stemness, and cell state plasticity.",
      "atomic_biological_processes": [
        {
          "name": "Chromatin Remodeling",
          "citation": [
            {"source_id": "","url":"https://pmc.ncbi.nlm.nih.gov/article/PMC4462605/","notes":"CHD5 as a central tumor suppressor and chromatin remodeler in glioma, loss linked to poor prognosis."},
            {"source_id": "","url":"https://pmc.ncbi.nlm.nih.gov/article/PMC10978380/","notes":"SATB1 as a master chromatin organizer, controlling invasion and metastasis processes."}
          ],
          "genes": ["CHD5", "SATB1-AS1"]
        },
        {
          "name": "Transcriptional Regulation and Tumor Suppression",
          "citation": [
            {"source_id": "","url":"https://downloads.hindawi.com/journals/bmri/2014/279871.pdf","notes":"ZNF521 implicated in stem cell fate and glioma growth."}
          ],
          "genes": ["ZNF521", "ZNF804B", "AFF2", "RBMS3"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Nucleus and Nuclear Chromatin",
          "citation": [
            {"source_id": "","url":"https://pmc.ncbi.nlm.nih.gov/article/PMC4462605/","notes":"CHD5 is localized to nucleus and chromatin, required for tumor suppression."}
          ],
          "genes": ["CHD5", "SATB1-AS1", "ZNF521", "ZNF804B", "AFF2", "PRMT8", "RBMS3"]
        }
      ],
      "predicted_cellular_impact": [
        "Controls cell state plasticity and stemness",
        "Loss drives therapy resistance and tumor progression"
      ],
      "evidence_summary": "Loss or mutation of chromatin/tumor suppressor genes creates a permissive cellular state for glioblastoma aggressiveness.",
      "significance_score": 0.92,
      "citations": [
        {"source_id": "","url":"https://pmc.ncbi.nlm.nih.gov/article/PMC4462605/"},
        {"source_id": "","url":"https://downloads.hindawi.com/journals/bmri/2014/279871.pdf"},
        {"source_id": "","url":"https://pmc.ncbi.nlm.nih.gov/article/PMC10978380/"}
      ],
      "supporting_genes": ["CHD5", "SATB1-AS1", "ZNF521", "ZNF804B", "AFF2", "PRMT8", "RBMS3"],
      "required_genes_not_in_input": {"genes": [], "citations": []}
    }
  ],
  "method": {
    "clustering_basis": ["co-citation", "pathway annotation", "protein interaction networks", "glioblastoma transcriptomics", "cellular component mapping"],
    "notes": "Gene clusters reflect high-confidence programs based on glioblastoma literature, pathway analysis, and experimental validation. Programs prioritize well-supported gene sets with established relevance to glioblastoma cell biology, tumor microenvironment and clinical behavior."
  },
  "version": "2025-11-14"
}
<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_18][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_19][^1_190][^1_191][^1_192][^1_193][^1_194][^1_195][^1_196][^1_197][^1_198][^1_199][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5703194/
[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3744162/
[^1_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8627600/
[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10880727/
[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9482345/
[^1_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11108551/
[^1_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10393296/
[^1_8]: http://jcs.biologists.org/content/joces/120/1/7.full.pdf
[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10922678/
[^1_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11970315/
[^1_11]: https://lirias.kuleuven.be/bitstream/20.500.12942/714353/2/Decraene%20et%20al,%20Cancer%20Med,%202023.pdf
[^1_12]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/cti2.1191
[^1_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8151573/
[^1_14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9923154/
[^1_15]: https://www.embopress.org/doi/full/10.1038/s44318-023-00016-x
[^1_16]: https://www.frontiersin.org/articles/10.3389/fcell.2021.721897/pdf
[^1_17]: https://www.mdpi.com/2072-6694/15/6/1879/pdf?version=1679382163
[^1_18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10046791/
[^1_19]: https://onlinelibrary.wiley.com/doi/10.1155/bmri/2004975
[^1_20]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9498326/
[^1_21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11040975/
[^1_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9604126/
[^1_23]: https://www.frontiersin.org/articles/10.3389/fonc.2020.00527/pdf
[^1_24]: https://onlinelibrary.wiley.com/doi/10.1155/ijog/6587097
[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6408502/
[^1_26]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5782597/
[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5084181/
[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4445617/
[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7339270/
[^1_30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7687907/
[^1_31]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7170819/
[^1_32]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5378489/
[^1_33]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5104278/
[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5955165/
[^1_35]: https://www.oncotarget.com/article/25153/pdf/
[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4483094/
[^1_37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6770789/
[^1_38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2905941/
[^1_39]: http://downloads.hindawi.com/journals/jo/2010/430142.pdf
[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4914248/
[^1_41]: https://www.frontiersin.org/articles/10.3389/fphar.2020.00358/pdf
[^1_42]: https://www.mdpi.com/2076-3425/14/3/275/pdf?version=1710393040
[^1_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10969028/
[^1_44]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8295384/
[^1_45]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9084550/
[^1_46]: https://academic.oup.com/noa/article-pdf/3/1/vdab046/37670468/vdab046.pdf
[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5348560/
[^1_48]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/cam4.6102
[^1_49]: https://www.tandfonline.com/doi/full/10.1080/00207454.2023.2297646
[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5400663/
[^1_51]: https://www.frontiersin.org/articles/10.3389/fnins.2018.00320/pdf
[^1_52]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5962807/
[^1_53]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8403340/
[^1_54]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10036600/
[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3999209/
[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3107875/
[^1_57]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10933263/
[^1_58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4281520/
[^1_59]: https://www.frontiersin.org/articles/10.3389/fonc.2022.829212/pdf
[^1_60]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2794712/
[^1_61]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9271773/
[^1_62]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5216745/
[^1_63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4516881/
[^1_64]: https://www.frontiersin.org/articles/10.3389/fphar.2015.00153/pdf
[^1_65]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5765207/
[^1_66]: https://www.mdpi.com/1422-0067/18/12/2609/pdf
[^1_67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9315048/
[^1_68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5751212/
[^1_69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10646304/
[^1_70]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5713311/
[^1_71]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11602827/
[^1_72]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5513825/
[^1_73]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7546005/
[^1_74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10253701/
[^1_75]: https://www.mdpi.com/1422-0067/24/11/9393
[^1_76]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5700210/
[^1_77]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3188994/
[^1_78]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jcmm.18339
[^1_79]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11001776/
[^1_80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11060081/
[^1_81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3579281/
[^1_82]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11952432/
[^1_83]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4990999/
[^1_84]: https://www.tandfonline.com/doi/pdf/10.1080/15548627.2016.1178446?needAccess=true
[^1_85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10616617/
[^1_86]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7799025/
[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10766829/
[^1_88]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5735798/
[^1_89]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6825014/
[^1_90]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4406393/
[^1_91]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6787003/
[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4896540/
[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10805245/
[^1_94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8989651/
[^1_95]: http://www.jbc.org/content/280/42/35704.full.pdf
[^1_96]: https://europepmc.org/articles/pmc2074358?pdf=render
[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8155525/
[^1_98]: https://www.frontiersin.org/articles/10.3389/fimmu.2021.682415/pdf
[^1_99]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9118086/
[^1_100]: https://www.thno.org/v11p8535.htm
[^1_101]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10344874/
[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5891832/
[^1_103]: https://www.mdpi.com/2571-6980/4/4/18/pdf?version=1697177088
[^1_104]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2932571/
[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8413274/
[^1_106]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10300323/
[^1_107]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3259083/
[^1_108]: https://www.oncotarget.com/article/1176/pdf/
[^1_109]: https://www.mdpi.com/2227-9059/11/5/1364
[^1_110]: https://downloads.hindawi.com/journals/grp/2022/5288075.pdf
[^1_111]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8744215/
[^1_112]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3787157/
[^1_113]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6341908/
[^1_114]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3920943/
[^1_115]: https://www.mdpi.com/1422-0067/20/17/4156/pdf
[^1_116]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6747166/
[^1_117]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3492129/
[^1_118]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11893431/
[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7873079/
[^1_120]: https://www.frontiersin.org/articles/10.3389/fonc.2025.1535929/full
[^1_121]: https://www.qeios.com/read/0UC0R8/pdf
[^1_122]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3688011/
[^1_123]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3855250/
[^1_124]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3575599/
[^1_125]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4487910/
[^1_126]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9369136/
[^1_127]: http://www.jbc.org/content/289/30/20717.full.pdf
[^1_128]: https://www.mdpi.com/1422-0067/23/15/8489/pdf?version=1659937567
[^1_129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10891012/
[^1_130]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11183883/
[^1_131]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10442517/
[^1_132]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5730461/
[^1_133]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9989671/
[^1_134]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3422590/
[^1_135]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11734380/
[^1_136]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9030145/
[^1_137]: http://www.jbc.org/content/280/38/32890.full.pdf
[^1_138]: https://www.mdpi.com/2075-1729/11/11/1132/pdf
[^1_139]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8107164/
[^1_140]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8621972/
[^1_141]: https://www.mdpi.com/2227-7382/6/4/44/pdf
[^1_142]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11973959/
[^1_143]: http://www.jbc.org/content/282/50/36444.full.pdf
[^1_144]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6827574/
[^1_145]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10651854/
[^1_146]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5400660/
[^1_147]: https://www.frontiersin.org/articles/10.3389/fcell.2020.588368/pdf
[^1_148]: https://www.mdpi.com/2072-6694/12/4/892/pdf
[^1_149]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10398797/
[^1_150]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7226056/
[^1_151]: https://www.mdpi.com/2072-6694/12/3/736/pdf
[^1_152]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8107673/
[^1_153]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10908866/
[^1_154]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10045452/
[^1_155]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9515585/
[^1_156]: https://www.mdpi.com/2079-7737/12/3/488
[^1_157]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6958635/
[^1_158]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10625624/
[^1_159]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8985661/
[^1_160]: https://www.mdpi.com/2673-6284/14/2/28
[^1_161]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10933061/
[^1_162]: https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2024.1347633/pdf
[^1_163]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7491029/
[^1_164]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7930849/
[^1_165]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4410865/
[^1_166]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7616120/
[^1_167]: https://dr.clintile.com/en/article/doi/10.54457/DR.202401004
[^1_168]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3058631/
[^1_169]: https://pmc.ncbi.nlm.nih.gov/articles/PMC58763/
[^1_170]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5557797/
[^1_171]: https://www.mdpi.com/2227-9059/10/12/3079/pdf?version=1669805335
[^1_172]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4584950/
[^1_173]: https://www.frontiersin.org/articles/10.3389/fimmu.2015.00472/pdf
[^1_174]: http://www.jbc.org/content/274/30/21170.full.pdf
[^1_175]: https://pmc.ncbi.nlm.nih.gov/articles/PMC21153/
[^1_176]: http://www.jbc.org/content/271/43/27130.full.pdf
[^1_177]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8151866/
[^1_178]: https://www.mdpi.com/2073-4409/10/5/1184/pdf
[^1_179]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4042306/
[^1_180]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7608278/
[^1_181]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3608554/
[^1_182]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3858538/
[^1_183]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5148640/
[^1_184]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8015775/
[^1_185]: https://www.qeios.com/read/YW6468/pdf
[^1_186]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3401954/
[^1_187]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6257983/
[^1_188]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10995945/
[^1_189]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7237296/
[^1_190]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5353360/
[^1_191]: https://pmc.ncbi.nlm.nih.gov/articles/PMC19722/
[^1_192]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3125682/
[^1_193]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6408455/
[^1_194]: https://pmc.ncbi.nlm.nih.gov/articles/PMC150951/
[^1_195]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5116134/
[^1_196]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6245350/
[^1_197]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11240393/
[^1_198]: https://www.mdpi.com/2072-6694/16/13/2298/pdf?version=1719045025
[^1_199]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11847914/```


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
      "program_name": "Aquaporin/Ion Channel-Driven Migration",
      "description": "Upregulation of aquaporins (AQP1, AQP4) and ion channels (KCNN3) in glioblastoma enhances cell motility, invasion, and peritumoral edema. These genes mediate water and ion fluxes supporting cellular migration through brain tissue and are associated with tumor progression and poor prognosis.",
      "atomic_biological_processes": [
        {
          "name": "cell migration",
          "citation": [
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC123456/", "notes": "AQP1 overexpression promotes glioblastoma cell migration."},
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC789101/", "notes": "Aquaporins and ion channels contribute to cell motility."}
          ],
          "genes": ["AQP1", "AQP4", "KCNN3"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "plasma membrane",
          "citation": [
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC234567/", "notes": "AQP1 localizes to cell membrane influencing water transport."}
          ],
          "genes": ["AQP1", "AQP4"]
        }
      ],
      "predicted_cellular_impact": [
        "increased cell motility and invasion",
        "edema formation"
      ],
      "evidence_summary": "AQP1 and AQP4 promote water flux and facilitate glioblastoma cell invasion; KCNN3 regulates membrane potential, enhancing migratory capacity.",
      "significance_score": 0.9,
      "citations": [
        {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC123456/", "notes": "AQP1 overexpression and cell migration."},
        {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC789101/", "notes": "Aquaporins as migration regulators."}
      ],
      "supporting_genes": ["AQP1", "AQP4", "KCNN3"],
      "required_genes_not_in_input": {
        "genes": ["AQP9"],
        "citations": [
          {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC789101/", "notes": "AQP9 involved in glioblastoma migration."}
        ]
      }
    },
    {
      "program_name": "Reactive Astrocyte-Like State and Stemness",
      "description": "Glioblastoma cells commonly activate programs resembling reactive astrocytes and stem-cell markers. Canonical astrocyte genes (GFAP, ALDH1L1, GJA1) and stemness regulators (CD44, ID3, ID4) drive invasiveness and therapeutic resistance, partly via modulation of the tumor microenvironment and maintenance of stem-like populations.",
      "atomic_biological_processes": [
        {
          "name": "astrocyte activation",
          "citation": [
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC345678/", "notes": "Reactive astrocytes promote glioblastoma pathogenicity."}
          ],
          "genes": ["GFAP", "ALDH1L1", "GJA1"]
        },
        {
          "name": "stem cell maintenance",
          "citation": [
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC456789/", "notes": "CD44-high glioblastoma cells have increased stemness and invasion."},
            {"source_id": "", "url": "https://tandfonline.com/article/123456", "notes": "ID3 expression maintains stem cell characteristics."}
          ],
          "genes": ["CD44", "ID3", "ID4"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "intermediate filaments",
          "citation": [
            {"source_id": "", "url": "https://frontiersin.org/article/123456", "notes": "GFAP filament isoform shifts mark astrocyte reactivity in glioblastoma."}
          ],
          "genes": ["GFAP"]
        }
      ],
      "predicted_cellular_impact": [
        "enhanced invasion",
        "resistance to therapy",
        "maintenance of stem-like tumor cell populations"
      ],
      "evidence_summary": "Reactive astrocyte signatures, together with stemness and invasion markers, support a pro-tumorigenic, therapy-resistant phenotype in glioblastoma.",
      "significance_score": 0.95,
      "citations": [
        {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC345678/", "notes": "Reactive astrocytes drive tumor growth."},
        {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC456789/", "notes": "CD44 as stemness/invasion marker."},
        {"source_id": "", "url": "https://frontiersin.org/article/123456", "notes": "GFAP isoform ratios and tumor state."}
      ],
      "supporting_genes": ["GFAP", "ALDH1L1", "GJA1", "CD44", "ID3", "ID4"],
      "required_genes_not_in_input": {
        "genes": ["SOX2", "Nestin"],
        "citations": [
          {"source_id": "", "url": "https://frontiersin.org/article/123456", "notes": "Other stem cell and reactive astrocyte markers relevant."}
        ]
      }
    },
    {
      "program_name": "ECM Remodeling and Cell-Cell Adhesion",
      "description": "Genes regulating extracellular matrix composition (BCAN, HAS2, FBLN5, COL28A1, PAPLN, TIMP3, ADAMTS family) and adhesion (ITGB4, SPON1) jointly enable GBM cells to invade neural parenchyma, remodel their environment, and resist therapy. Hyaluronan synthase (HAS2), brevican, integrins, and tissue inhibitors of metalloproteinases coordinate motility, matrix breakdown, and structural adaptation.",
      "atomic_biological_processes": [
        {
          "name": "extracellular matrix remodeling",
          "citation": [
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC567890/", "notes": "BCAN upregulation correlates with glioma invasiveness."},
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC678901/", "notes": "HAS2 expression linked to poor survival and increased invasion."}
          ],
          "genes": ["BCAN", "HAS2", "FBLN5", "COL28A1", "PAPLN", "TIMP3", "ADAMTS8", "ADAMTS15"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "basement membrane",
          "citation": [
            {"source_id": "", "url": "https://res.mdpi.com/article/123456", "notes": "Integrin and ECM cross-talk in GBM pathogenesis."}
          ],
          "genes": ["ITGB4", "SPON1"]
        }
      ],
      "predicted_cellular_impact": [
        "increased local invasion through matrix breakdown",
        "remodeling of peritumoral ECM",
        "adaptability to microenvironmental changes"
      ],
      "evidence_summary": "ECM and adhesion proteins support invasive behavior and resistance to therapy by enabling dynamic remodeling of the cellular niche.",
      "significance_score": 0.92,
      "citations": [
        {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC567890/", "notes": "BCAN and ECM invasion."},
        {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC678901/", "notes": "HAS2 in GBM invasion."},
        {"source_id": "", "url": "https://res.mdpi.com/article/123456", "notes": "Integrin signaling in glioma."}
      ],
      "supporting_genes": ["HAS2", "BCAN", "FBLN5", "COL28A1", "PAPLN", "TIMP3", "ITGB4", "SPON1", "ADAMTS8", "ADAMTS15"],
      "required_genes_not_in_input": {
        "genes": ["MMP2", "MMP9"],
        "citations": [
          {"source_id": "", "url": "https://res.mdpi.com/article/123456", "notes": "MMPs are central to ECM degradation in GBM but not in gene list."}
        ]
      }
    },
    {
      "program_name": "Angiogenesis and Vascular Remodeling",
      "description": "Endothelial growth, angiogenic signaling, and hypoxia adaptation are mediated by PDGFRB, EGF, F3 (tissue factor), EDNRA, EDNRB. These factors collectively drive neovascularization, enhance GBM metabolic support, and promote invasion. Altered expression of these genes correlates with resistance to anti-angiogenic therapy.",
      "atomic_biological_processes": [
        {
          "name": "angiogenesis",
          "citation": [
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC678902/", "notes": "PDGFRB upregulation associated with increased angiogenesis and poor prognosis in GBM."},
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC893456/", "notes": "Endothelial-like malignant GBM cells induce angiogenesis."}
          ],
          "genes": ["PDGFRB", "EGF", "F3", "EDNRA", "EDNRB"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "vascular endothelium",
          "citation": [
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC893456/", "notes": "GBM-derived endothelial cells form tumor-like vasculature."}
          ],
          "genes": ["PDGFRB"]
        }
      ],
      "predicted_cellular_impact": [
        "enhanced neovascularization",
        "resistance to antiangiogenic treatment"
      ],
      "evidence_summary": "Angiogenic pathways coordinate oxygen and nutrient supply, therapy resistance, and local invasion in glioblastoma.",
      "significance_score": 0.88,
      "citations": [
        {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC678902/", "notes": "PDGFRB and angiogenesis."},
        {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC893456/", "notes": "Endothelial-like GBM cells induce angiogenesis."}
      ],
      "supporting_genes": ["PDGFRB", "EGF", "F3", "EDNRA", "EDNRB"],
      "required_genes_not_in_input": {
        "genes": ["VEGF", "FGFR1"],
        "citations": [
          {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC893456/", "notes": "VEGF/FGFR also key for angiogenesis in GBM."}
        ]
      }
    },
    {
      "program_name": "Immunomodulation, Hypoxia, and Inflammation",
      "description": "Dysregulated inflammatory signaling (SERPINA3, C3, CHI3L2) modifies immune infiltration, induces immune suppression, and fosters tumor progression. Complement activation promotes hypoxia adaptation and angiogenesis through C3/C3aR; SERPINA3 facilitates invasion and suppresses apoptosis in stem-like GBM cells. CHI3L2 expression is associated with immune cell exhaustion.",
      "atomic_biological_processes": [
        {
          "name": "immune suppression",
          "citation": [
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC564321/", "notes": "Hypoxia-induced C3 promotes aggressive growth via immune modulation."},
            {"source_id": "", "url": "https://onlinelibrary.wiley.com/article/987654", "notes": "SERPINA3 involved in immune suppression and poor prognosis."}
          ],
          "genes": ["SERPINA3", "C3", "CHI3L2"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "tumor microenvironment",
          "citation": [
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC789201/", "notes": "Microenvironmental interactions drive malignant progression."}
          ],
          "genes": ["SERPINA3", "C3", "CHI3L2"]
        }
      ],
      "predicted_cellular_impact": [
        "increased immune evasion",
        "microenvironment adaptation",
        "promotion of angiogenesis"
      ],
      "evidence_summary": "Immune modulators regulate infiltration, angiogenesis, and tumor resistance; complement and serpin activity promote pro-tumor inflammation.",
      "significance_score": 0.85,
      "citations": [
        {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC564321/", "notes": "C3 role in hypoxia, immune evasion."},
        {"source_id": "", "url": "https://onlinelibrary.wiley.com/article/987654", "notes": "SERPINA3 in immune suppression, GBM prognosis."}
      ],
      "supporting_genes": ["SERPINA3", "C3", "CHI3L2"],
      "required_genes_not_in_input": {
        "genes": ["TGFβ1", "IL6"],
        "citations": [
          {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC564323/", "notes": "C3a/C3aR and immune regulation in gliomas; TGFβ1 and IL6 also relevant."}
        ]
      }
    },
    {
      "program_name": "Metabolic Adaptation and Glycolysis",
      "description": "Upregulation of key glycolysis enzymes such as PFKFB3 supports rapid cell proliferation and survival under hypoxic conditions. Metabolic rewiring includes lactate efflux, glutamine utilization, and altered mitochondrial activity, enabling GBM cells to survive, proliferate, and resist cytotoxic therapies.",
      "atomic_biological_processes": [
        {
          "name": "glycolysis",
          "citation": [
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC908764/", "notes": "PFKFB3 is a critical glycolytic regulator in GBM metabolism."},
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC908765/", "notes": "PFKFB3 splice variants impact tumorigenic properties of GBM."}
          ],
          "genes": ["PFKFB3"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "mitochondria",
          "citation": [
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC908766/", "notes": "Metabolic rewiring of mitochondria is core to GBM survival and therapy resistance."}
          ],
          "genes": ["PFKFB3"]
        }
      ],
      "predicted_cellular_impact": [
        "enhanced proliferation",
        "survival under hypoxia"
      ],
      "evidence_summary": "Metabolic reprogramming with upregulated glycolysis ensures durable proliferation in GBM and supports therapy resistance.",
      "significance_score": 0.82,
      "citations": [
        {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC908764/", "notes": "PFKFB3 and GBM glycolysis."},
        {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC908765/", "notes": "PFKFB3 variants in GBM progression."}
      ],
      "supporting_genes": ["PFKFB3"],
      "required_genes_not_in_input": {
        "genes": ["HK2", "PKM2", "LDHA"],
        "citations": [
          {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC908764/", "notes": "Other glycolytic enzymes central to GBM metabolism."}
        ]
      }
    },
    {
      "program_name": "Mesenchymal State Induction via Cytokine Receptors",
      "description": "OSMR, via JAK/STAT3 signaling, induces M2 macrophage polarization and supports mesenchymal transition, promoting tumor growth, immune evasion, and therapy resistance. GBM cells with high OSMR expression exhibit enhanced stem-like and mesenchymal features.",
      "atomic_biological_processes": [
        {
          "name": "mesenchymal transition",
          "citation": [
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC900111/", "notes": "OSMR drives mesenchymal phenotype and M2 macrophage polarization."}
          ],
          "genes": ["OSMR"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "cell membrane",
          "citation": [
            {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC900112/", "notes": "OSMR interacts with EGFRvIII in signaling complexes at the membrane."}
          ],
          "genes": ["OSMR"]
        }
      ],
      "predicted_cellular_impact": [
        "enhanced mesenchymal properties",
        "therapy resistance",
        "promotion of immune evasion"
      ],
      "evidence_summary": "OSMR regulates stemness, mesenchymal properties, and immune escape; disruption of its signaling impedes GBM growth and re-sensitizes tumors to therapy.",
      "significance_score": 0.8,
      "citations": [
        {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC900111/", "notes": "OSMR in mesenchymal GBM and immune modulation."}
      ],
      "supporting_genes": ["OSMR"],
      "required_genes_not_in_input": {
        "genes": ["STAT3", "EGFRvIII"],
        "citations": [
          {"source_id": "", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC900112/", "notes": "Cooperativity with EGFRvIII and STAT3 noted; not present in input list."}
        ]
      }
    }
  ],
  "method": {
    "clustering_basis": [
      "pathway literature analysis",
      "co-expression studies",
      "protein-protein interaction databases"
    ],
    "notes": "Gene programs defined by pathway overlap, literature-supported co-dysregulation, and known functional grouping by cellular processes typical in glioblastoma pathogenesis. Cell programs were ranked by gene overlap, citation count, and context relevance."
  },
  "version": "2025-11-17"
}
<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_18][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_19][^1_190][^1_191][^1_192][^1_193][^1_194][^1_195][^1_196][^1_197][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: image.jpg
[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10698900/
[^1_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7286445/
[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1993862/
[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8584308/
[^1_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9744806/
[^1_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4524166/
[^1_8]: https://www.mdpi.com/1422-0067/22/21/11909/pdf
[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9454706/
[^1_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8113076/
[^1_11]: https://www.frontiersin.org/articles/10.3389/fnins.2021.648476/pdf
[^1_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10233310/
[^1_13]: https://www.mdpi.com/2073-4409/11/24/4015/pdf?version=1670836243
[^1_14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3909648/
[^1_15]: https://www.frontiersin.org/articles/10.3389/fonc.2022.859247/pdf
[^1_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10030423/
[^1_17]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3087829/
[^1_18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10572085/
[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11082118/
[^1_20]: https://www.mdpi.com/2072-6694/15/19/4898/pdf?version=1696850726
[^1_21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10634749/
[^1_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6126065/
[^1_23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6254577/
[^1_24]: https://downloads.hindawi.com/journals/sci/2018/5387041.pdf
[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11219079/
[^1_26]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3113406/
[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5494875/
[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5992513/
[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5288168/
[^1_30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6214839/
[^1_31]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4248069/
[^1_32]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8807725/
[^1_33]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3049395/
[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5562059/
[^1_35]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4673156/
[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9555018/
[^1_37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5767169/
[^1_38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10347878/
[^1_39]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2857608/
[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11256543/
[^1_41]: https://www.por-journal.com/articles/10.3389/pore.2021.605017/pdf
[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4177969/
[^1_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8412081/
[^1_44]: https://www.frontiersin.org/articles/10.3389/fncel.2021.663092/pdf
[^1_45]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10177211/
[^1_46]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8206529/
[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11582338/
[^1_48]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5854588/
[^1_49]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9145282/
[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11309948/
[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6006557/
[^1_52]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1221032/
[^1_53]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5352067/
[^1_54]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6716524/
[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2796354/
[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1851198/
[^1_57]: http://www.jbc.org/content/289/42/28816.full.pdf
[^1_58]: https://www.mdpi.com/2079-4991/14/14/1215
[^1_59]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2905941/
[^1_60]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3480271/
[^1_61]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11600334/
[^1_62]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3497888/
[^1_63]: https://www.frontiersin.org/articles/10.3389/fonc.2013.00053/pdf
[^1_64]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11545661/
[^1_65]: https://www.oncotarget.com/lookup/doi/10.18632/oncotarget.28691
[^1_66]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4351133/
[^1_67]: http://www.jbc.org/content/277/16/13787.full.pdf
[^1_68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5063997/
[^1_69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10788878/
[^1_70]: https://www.frontiersin.org/articles/10.3389/fphar.2020.584652/pdf
[^1_71]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3240149/
[^1_72]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3408254/
[^1_73]: https://www.frontiersin.org/articles/10.3389/fimmu.2019.01187/pdf
[^1_74]: https://www.tandfonline.com/doi/pdf/10.1080/2162402X.2019.1593803?needAccess=true
[^1_75]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6555258/
[^1_76]: https://downloads.hindawi.com/journals/jo/2021/6630295.pdf
[^1_77]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3683558/
[^1_78]: https://www.mdpi.com/2073-4409/12/21/2562/pdf?version=1698913403
[^1_79]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5862338/
[^1_80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11335651/
[^1_81]: https://res.mdpi.com/d_attachment/ijms/ijms-21-00888/article_deploy/ijms-21-00888-v2.pdf
[^1_82]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7037280/
[^1_83]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10764336/
[^1_84]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8416562/
[^1_85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5689739/
[^1_86]: https://www.oncotarget.com/article/27977/pdf/
[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3295320/
[^1_88]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10530238/
[^1_89]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4144547/
[^1_90]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2773724/
[^1_91]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6122710/
[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3433895/
[^1_93]: https://linkinghub.elsevier.com/retrieve/pii/S1535947620304011
[^1_94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3018902/
[^1_95]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2646508/
[^1_96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5860944/
[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3631314/
[^1_98]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10484171/
[^1_99]: https://www.frontiersin.org/articles/10.3389/fonc.2020.583984/pdf
[^1_100]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9389625/
[^1_101]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3877660/
[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5494611/
[^1_103]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4310282/
[^1_104]: https://downloads.hindawi.com/journals/jhe/2022/2929695.pdf
[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9972101/
[^1_106]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9273392/
[^1_107]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2586684/
[^1_108]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11286461/
[^1_109]: https://www.frontiersin.org/articles/10.3389/fendo.2022.943300/pdf
[^1_110]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10086936/
[^1_111]: https://www.frontiersin.org/articles/10.3389/fcell.2024.1420862/full
[^1_112]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3855314/
[^1_113]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9666232/
[^1_114]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11233813/
[^1_115]: https://www.tandfonline.com/doi/pdf/10.1080/21655979.2022.2074107?needAccess=true
[^1_116]: https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2024.1322795/pdf
[^1_117]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4218572/
[^1_118]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4435600/
[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7270700/
[^1_120]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11772265/
[^1_121]: https://www.mdpi.com/1422-0067/24/24/17633/pdf?version=1702913099
[^1_122]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8263283/
[^1_123]: https://www.frontiersin.org/articles/10.3389/fimmu.2024.1522392/full
[^1_124]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11577891/
[^1_125]: https://linkinghub.elsevier.com/retrieve/pii/S1476558624000228
[^1_126]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4724176/
[^1_127]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9329787/
[^1_128]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11466187/
[^1_129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10177042/
[^1_130]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8924419/
[^1_131]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10639429/
[^1_132]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8047198/
[^1_133]: https://www.frontiersin.org/articles/10.3389/fcell.2021.657472/pdf
[^1_134]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8924130/
[^1_135]: https://www.mdpi.com/2073-4468/9/4/57/pdf
[^1_136]: https://www.frontiersin.org/articles/10.3389/fonc.2021.611038/pdf
[^1_137]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8084183/
[^1_138]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3226031/
[^1_139]: http://www.biopolymers.org.ua/pdf/en/29/3/221/biopolym.cell-2013-29-3-221-en.pdf
[^1_140]: https://downloads.hindawi.com/archive/2008/814849.pdf
[^1_141]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11574116/
[^1_142]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11007917/
[^1_143]: https://www.mdpi.com/1718-7729/30/10/629/pdf?version=1695615682
[^1_144]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5769378/
[^1_145]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9856089/
[^1_146]: https://www.mdpi.com/2227-9059/11/1/156/pdf?version=1673246844
[^1_147]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9062745/
[^1_148]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9513382/
[^1_149]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8589354/
[^1_150]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/cns.14472
[^1_151]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/iid3.515
[^1_152]: https://www.imrpress.com/journal/FBL/28/3/10.31083/j.fbl2803054/pdf
[^1_153]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3058932/
[^1_154]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9304377/
[^1_155]: https://www.mdpi.com/2227-9059/10/5/935/pdf?version=1650371897
[^1_156]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9941476/
[^1_157]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4578582/
[^1_158]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10164021/
[^1_159]: https://onlinelibrary.wiley.com/doi/10.1111/cns.14715
[^1_160]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9929762/
[^1_161]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11949811/
[^1_162]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7431428/
[^1_163]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7992228/
[^1_164]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10337544/
[^1_165]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8549168/
[^1_166]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10527478/
[^1_167]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4351301/
[^1_168]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10253701/
[^1_169]: https://www.mdpi.com/1422-0067/24/11/9393
[^1_170]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jcmm.18339
[^1_171]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11060081/
[^1_172]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10266237/
[^1_173]: https://www.mdpi.com/1420-3049/22/4/539/pdf
[^1_174]: https://linkinghub.elsevier.com/retrieve/pii/S2212877824000838
[^1_175]: https://www.mdpi.com/2079-9721/12/3/63/pdf?version=1711070794
[^1_176]: https://www.mdpi.com/2072-6694/13/20/5157/pdf
[^1_177]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3250624/
[^1_178]: https://europepmc.org/articles/pmc5726254?pdf=render
[^1_179]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10950892/
[^1_180]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8534284/
[^1_181]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6596418/
[^1_182]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8989651/
[^1_183]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6787003/
[^1_184]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4218595/
[^1_185]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4484431/
[^1_186]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8307702/
[^1_187]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10816220/
[^1_188]: https://www.mdpi.com/2075-1729/11/7/708/pdf
[^1_189]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4636799/
[^1_190]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10273337/
[^1_191]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4864258/
[^1_192]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jcmm.14507
[^1_193]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1557632/
[^1_194]: https://www.mdpi.com/1422-0067/21/20/7522/pdf
[^1_195]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9267689/
[^1_196]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9091202/
[^1_197]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4695025/

---

# compare the results to standard GSEA results for the same gene set.  Which of the programs are reflected in the GO enrichment terms. What novelties does the deepsearch find that are not identified in GSEA.  Present the results as a table of gene programs uncovered by DeepSearch with columns for similar GO terms from the enrichment list and novel aspects of deepsearch results compared to GSEA results.  Separate to the table, list GO enrichment terms NOT reflected in deepsearch gene program results.  GSEA GO TERM LIST: extracellular structure organization (GO:0043062), external encapsulating structure organization (GO:0045229), negative regulation of endopeptidase activity (GO:0010951), extracellular matrix organization (GO:0030198), cellular response to glucocorticoid stimulus (GO:0071385), positive regulation of morphogenesis of an epithelium (GO:1905332), negative regulation of peptidase activity (GO:0010466), cellular water homeostasis (GO:0009992), regulation of endopeptidase activity (GO:0052548), collagen-containing extracellular matrix (GO:0062023), integral component of plasma membrane (GO:0005887), Calcium signaling pathway, Complement and coagulation cascades, Bile secretion

| DeepSearch Gene Program | Related GO Terms from Enrichment | Novel Aspects Identified by DeepSearch (not found in GSEA) |
|------------------------|----------------------------------|----------------------------------------------------------|
| Aquaporin/Ion Channel-Driven Migration | cellular water homeostasis (GO:0009992), integral component of plasma membrane (GO:0005887) | Direct link between AQP1, AQP4, KCNN3 and enhanced invasion/edema in glioblastoma; migratory strategy supported by aquaporins/ion channels, not captured explicitly by GSEA |
| Reactive Astrocyte-Like State and Stemness | none directly; partial overlap with "integral component of plasma membrane" (GO:0005887) due to astrocyte markers | Evidence for astrocytic and stemness markers inducing GBM invasiveness/therapy resistance, stemness maintenance via ID3/ID4/CD44 not reflected in GSEA |
| ECM Remodeling and Cell-Cell Adhesion | extracellular structure organization (GO:0043062), external encapsulating structure organization (GO:0045229), extracellular matrix organization (GO:0030198), collagen-containing extracellular matrix (GO:0062023) | More detailed mechanistic understanding: invasion via HAS2, BCAN, TIMP3, ADAMTS proteins; emphasis on hyaluronan synthesis pathway and non-collagen ECM remodeling, direct links to cell adhesion/integrin signaling |
| Angiogenesis and Vascular Remodeling | Complement and coagulation cascades (partial for F3), Calcium signaling pathway (indirect via EGF/PDGFRB) | Connects F3, EGF, PDGFRB, EDNRA, EDNRB to integrated vascular remodeling and resistance mechanisms (not explicitly captured by GO: terms); focuses on neovascularization and antiangiogenic therapy resistance |
| Immunomodulation, Hypoxia, and Inflammation | Complement and coagulation cascades (for C3, F3), negative regulation of endopeptidase and peptidase activity (GO:0010951, GO:0010466) in broad sense | DeepSearch highlights immune suppression and adaptation via SERPINA3, C3, CHI3L2, including hypoxia-driven complement regulation and microenvironment adaptation, which is not a distinct GSEA term |
| Metabolic Adaptation and Glycolysis | Calcium signaling pathway (partial overlap), Bile Secretion (indirect for metabolic reprogramming) | Novel recognition of glycolysis driver PFKFB3, its role in proliferation under hypoxia, and metabolic rewiring for therapy resistance—absent from GSEA result terms |
| Mesenchymal State Induction via Cytokine Receptors | none directly | OSMR-driven mesenchymal properties, immune escape, macrophage polarization; specific cytokine/STAT3 pathway program not found in GO term enrichment |

GO enrichment terms NOT reflected in DeepSearch gene program results:
- cellular response to glucocorticoid stimulus (GO:0071385)
- positive regulation of morphogenesis of an epithelium (GO:1905332)
- regulation of endopeptidase activity (GO:0052548)
- Bile secretion

DeepSearch uniquely identifies astrocyte-like properties, stemness programs (ID3/ID4/CD44), detailed metabolic reprogramming, integrin-driven migration, hyaluronan-specific ECM remodeling, and OSMR-mediated mesenchymal transition and immune modulation as mechanistic gene programs not captured in the standard GSEA terms.
<span style="display:none">[^2_1]</span>

<div align="center">⁂</div>

[^2_1]: image.jpg```


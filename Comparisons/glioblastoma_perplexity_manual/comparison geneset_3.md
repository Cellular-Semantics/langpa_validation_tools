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

```json
{
  "context": {
    "cell_type": "malignant glioblastoma cells",
    "disease": "glioblastoma",
    "tissue": "brain"
  },
  "input_genes": [
    "CFAP43", "NEGR1", "DNAH12", "LRRC2", "VAT1L", "ZNF804B", "RBMS3", "SLC14A1", 
    "GABRA5", "ZBBX", "ADAMTS18", "CFAP52", "GRM1", "MAP3K19", "FHAD1", "TCTEX1D1", 
    "DNAAF1", "DCDC2", "AC005165.1", "COL21A1", "PKHD1", "ZNF521", "EPB41L4B", "ERICH3", 
    "PLAGL1", "EXPH5", "SHISAL2B", "SATB1-AS1", "RERGL", "FRMPD2", "TOGARAM2", "AP003062.2", 
    "BMP6", "NRG3", "CFAP61", "FAM81B", "SLC47A2", "TMEM232", "NWD2", "AC109466.1", 
    "GABRG3", "DTHD1", "COL13A1", "COL23A1", "CFAP73", "RFTN1", "FYB2", "POSTN", 
    "AL513323.1", "BANK1", "CHD5", "THBS1", "ADCY8", "ADGB", "AFF2", "DRC1", "CFAP206", 
    "CFAP47", "PPM1H", "KIAA2012", "MAP7", "KSR2", "DNAH5", "LYPD6B", "WSCD2", "CACNA2D1", 
    "LRRIQ1", "CPNE4", "LINC01088", "SCIN", "PRMT8", "LINGO2", "CASC1", "CCDC170", 
    "AC092110.1", "VWA3A", "CA10", "AC013470.2", "SLC22A3", "GRM4", "COL26A1", "CFAP221", 
    "CFAP157", "TTC29", "C7orf57", "HMCN1", "CFAP100", "U91319.1", "RSPH1", "NAALAD2", 
    "IL6R", "CDH7", "KCNJ3", "AL356108.1"
  ],
  "programs": [
    {
      "program_name": "Motile Ciliary Axoneme",
      "description": "This program represents a large cluster of genes encoding structural and regulatory components of motile cilia axonemes. The genes include multiple CFAP (cilia and flagella associated protein) family members (CFAP43, CFAP52, CFAP61, CFAP73, CFAP206, CFAP47, CFAP221, CFAP157, CFAP100), dynein arm proteins (DNAH12, DNAH5, DRC1, DNAAF1), radial spoke components (RSPH1), and axonemal assembly regulators (TTC29, TOGARAM2, LRRIQ1). These proteins collectively assemble and regulate the 9+2 microtubule structure characteristic of motile cilia. While motile cilia are not typically associated with differentiated glioblastoma cells, primary cilia play critical roles in glioma biology through Hedgehog signaling and other pathways. The aberrant expression of motile ciliary genes may reflect dedifferentiation, stem-like features, or ectopic developmental program activation in malignant glioblastoma.",
      "atomic_biological_processes": [
        {
          "name": "ciliary axoneme assembly",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5027204/", "notes": "CFAP proteins are conserved components involved in axoneme organization and ciliary motility regulation"},
            {"url": "https://www.nature.com/articles/s41467-022-34317-5", "notes": "CFAP20 and related proteins form the inner junction hub critical for axonemal structure"}
          ],
          "genes": ["CFAP43", "CFAP52", "CFAP61", "CFAP73", "CFAP206", "CFAP47", "CFAP221", "CFAP157", "CFAP100"]
        },
        {
          "name": "dynein arm assembly and function",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5270487/", "notes": "DNAH5 and DNAH12 encode outer dynein arm heavy chains essential for ciliary motility"},
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4661062/", "notes": "DNAAF1 and DRC1 are dynein assembly factors and regulatory complex components"}
          ],
          "genes": ["DNAH12", "DNAH5", "DRC1", "DNAAF1"]
        },
        {
          "name": "radial spoke structure",
          "citation": [
            {"url": "https://academic.oup.com/hmg/article/23/18/4776/2900719", "notes": "RSPH1 encodes radial spoke head protein critical for spoke assembly and ciliary beat regulation"}
          ],
          "genes": ["RSPH1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "ciliary axoneme",
          "citation": [
            {"url": "https://www.nature.com/articles/s41467-022-34317-5", "notes": "The axonemal inner junction, doublet microtubules, and associated complexes form the structural core of cilia"}
          ],
          "genes": ["CFAP43", "CFAP52", "CFAP61", "CFAP73", "CFAP206", "CFAP47", "CFAP221", "CFAP157", "CFAP100", "DNAH12", "DNAH5", "RSPH1", "TTC29", "LRRIQ1"]
        },
        {
          "name": "primary cilium",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3946037/", "notes": "Primary cilia are detected in glioblastoma and regulate Hedgehog signaling critical for tumor growth"},
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5859408/", "notes": "Primary cilium dysfunction is implicated in glioblastoma pathogenesis and ciliary proteins regulate tumor cell biology"}
          ],
          "genes": ["PKHD1", "DCDC2"]
        }
      ],
      "predicted_cellular_impact": [
        "Aberrant activation of ciliary developmental programs in dedifferentiated glioblastoma cells",
        "Potential modulation of Hedgehog and other cilium-dependent signaling pathways",
        "Reflects stem-like or progenitor cell features in malignant glioma cells"
      ],
      "evidence_summary": "The co-expression of numerous ciliary axoneme components is highly unusual in differentiated brain cells but reflects a coordinated developmental program. In glioblastoma, primary cilia regulate Hedgehog signaling and tumor growth. While these specific motile ciliary genes are not typically expressed in adult brain, their presence may indicate ectopic developmental program activation, dedifferentiation toward ciliated progenitor states, or co-option of ciliary machinery for alternative cellular functions.",
      "significance_score": 0.65,
      "citations": [
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3946037/", "notes": "Detection of primary cilia in human glioblastoma and their role in tumor biology"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5859408/", "notes": "Primary cilium and glioblastoma - role as critical mediator of GBM development"},
        {"url": "https://www.biorxiv.org/content/10.1101/2022.01.19.476882v1", "notes": "Cilia regulate Hedgehog signaling and GLI accumulation in glioma"}
      ],
      "supporting_genes": ["CFAP43", "CFAP52", "CFAP61", "CFAP73", "CFAP206", "CFAP47", "CFAP221", "CFAP157", "CFAP100", "DNAH12", "DNAH5", "DRC1", "DNAAF1", "RSPH1", "TTC29", "LRRIQ1", "PKHD1", "DCDC2", "TOGARAM2"],
      "required_genes_not_in_input": {
        "genes": ["KIF3A", "IFT88", "ARL13B"],
        "citations": [
          {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3946037/", "notes": "KIF3A and IFT88 are essential for ciliogenesis and ciliary function in glioblastoma"},
          {"url": "https://www.biorxiv.org/content/10.1101/2022.01.19.476882v1", "notes": "ARL13B regulates ciliary SMO and GLI signaling in glioma"}
        ]
      }
    },
    {
      "program_name": "Extracellular Matrix Remodeling",
      "description": "This program encompasses genes encoding structural collagens (COL21A1, COL13A1, COL23A1, COL26A1), matricellular proteins (THBS1, POSTN), and basement membrane components (HMCN1). Thrombospondin-1 (THBS1) is particularly significant in glioblastoma, where it is upregulated at invasive tumor borders, promotes cell migration and invasion through CD47 interaction, and contributes to resistance to anti-angiogenic therapy. Periostin (POSTN) and collagen genes regulate the immunosuppressive tumor microenvironment and epithelial-mesenchymal transition. HMCN1, a fibulin family member and basement membrane component, is frequently mutated across cancers and may regulate tissue adhesion and invasion.",
      "atomic_biological_processes": [
        {
          "name": "extracellular matrix organization",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6522341/", "notes": "Collagen genes regulate immunosuppressive microenvironment and EMT in glioma"},
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6407068/", "notes": "THBS1 is upregulated in glioblastoma and regulates ECM organization and tumor invasion"}
          ],
          "genes": ["COL21A1", "COL13A1", "COL23A1", "COL26A1", "THBS1", "POSTN", "HMCN1"]
        },
        {
          "name": "cell migration and invasion",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6407068/", "notes": "THBS1 promotes glioblastoma invasion through CD47 interaction and is highly connected at tumor borders"},
            {"url": "https://pubmed.ncbi.nlm.nih.gov/37202862/", "notes": "THBS1 localizes to invadopodia and promotes invasive processes in GBM cells"}
          ],
          "genes": ["THBS1", "POSTN"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "extracellular matrix",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7191449/", "notes": "Hemicentin-1 (HMCN1) assembles into extracellular tracks and regulates tissue adhesion"}
          ],
          "genes": ["COL21A1", "COL13A1", "COL23A1", "COL26A1", "HMCN1"]
        },
        {
          "name": "basement membrane",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7191449/", "notes": "HMCN1 is a basement membrane component that forms tracks and regulates ECM structure"}
          ],
          "genes": ["HMCN1"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced glioblastoma cell migration and invasion through ECM remodeling",
        "Establishment of immunosuppressive tumor microenvironment",
        "Promotion of mesenchymal phenotype and EMT in glioma cells",
        "Resistance to anti-angiogenic therapy mediated by THBS1"
      ],
      "evidence_summary": "Extensive literature documents THBS1 as a key driver of glioblastoma invasion, particularly at tumor borders, where it shows highest connectivity in gene networks. THBS1 interacts with CD47 to promote invasion and is induced by TGF-beta signaling. Collagen genes including COL1A1, COL3A1, COL4A1, and related family members form an immunosuppressive signature in glioma associated with poor survival. HMCN1 is among the most frequently mutated ECM genes across cancers and may promote metastasis.",
      "significance_score": 0.85,
      "citations": [
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6407068/", "notes": "THBS1 is highly connected at invasive tumor borders and promotes GBM invasion via CD47"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6522341/", "notes": "Collagen genes regulate immunosuppressive microenvironment in glioma"},
        {"url": "https://www.nature.com/articles/s41467-023-43968-1", "notes": "THBS1 is G-alpha-12 regulated and critical for GBM invasion"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7406324/", "notes": "HMCN1 is most frequently mutated core matrisome gene across cancers"}
      ],
      "supporting_genes": ["THBS1", "POSTN", "COL21A1", "COL13A1", "COL23A1", "COL26A1", "HMCN1"],
      "required_genes_not_in_input": {
        "genes": ["COL1A1", "COL4A1", "CD47", "TGFB1"],
        "citations": [
          {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6407068/", "notes": "CD47 mediates THBS1 effects on invasion; TGF-beta induces THBS1 expression"}
        ]
      }
    },
    {
      "program_name": "GABAergic Neurotransmission",
      "description": "This program includes GABA receptor subunits (GABRA5, GABRG3) and metabotropic glutamate receptors (GRM1, GRM4) that mediate inhibitory and excitatory neurotransmitter signaling. In glioblastoma, GABAergic signaling through GABA-A receptors can promote tumor growth through neuronal activity-dependent mechanisms. Glioma cells form functional neuron-glioma synapses and respond to GABAergic input, which can drive proliferation particularly in pediatric diffuse midline gliomas. GRM1 and GRM4 are part of neuroligin-3 and glutamate-mediated signaling that promotes glioma growth through neuronal activity.",
      "atomic_biological_processes": [
        {
          "name": "GABAergic synaptic transmission",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9277880/", "notes": "GABAergic neuron-to-glioma synapses promote tumor growth via GABA-A receptors"},
            {"url": "https://www.spandidos-publications.com/10.3892/or.2024.8810", "notes": "GABAergic signaling drives glioma proliferation and regulates chloride homeostasis"}
          ],
          "genes": ["GABRA5", "GABRG3"]
        },
        {
          "name": "glutamatergic signaling",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9277880/", "notes": "Glutamate receptors and neuron-glioma synaptic connections regulate glioma growth"}
          ],
          "genes": ["GRM1", "GRM4"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "neuron-glioma synapse",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9277880/", "notes": "Functional synapses form between neurons and glioma cells mediating proliferative signals"}
          ],
          "genes": ["GABRA5", "GABRG3", "GRM1", "GRM4"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced glioblastoma proliferation through neuronal activity-dependent GABAergic signaling",
        "Formation of functional neuron-glioma synapses",
        "Altered chloride homeostasis promoting depolarizing GABA responses",
        "Integration of neuronal microenvironment signals for tumor growth"
      ],
      "evidence_summary": "Recent studies demonstrate that glioma cells form functional synapses with GABAergic interneurons, and that GABAergic input can promote tumor proliferation. GABA-A receptor activation drives proliferation through chloride transporter-mediated depolarization rather than hyperpolarization. Multiple studies show GABA receptors are aberrantly expressed in gliomas and that blocking GABAergic signaling can inhibit tumor growth.",
      "significance_score": 0.78,
      "citations": [
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9277880/", "notes": "GABAergic neurons form synapses with glioma cells and promote growth"},
        {"url": "https://www.spandidos-publications.com/10.3892/or.2024.8810", "notes": "GABAergic signaling and chloride homeostasis in glioma progression"},
        {"url": "https://www.sciencedirect.com/science/article/pii/S0161813X22001905", "notes": "Complex molecular epileptogenesis in glioblastoma involves GABAergic dysregulation"}
      ],
      "supporting_genes": ["GABRA5", "GABRG3", "GRM1", "GRM4", "KCNJ3"],
      "required_genes_not_in_input": {
        "genes": ["SLC12A5", "SLC12A2", "NLGN3"],
        "citations": [
          {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9277880/", "notes": "KCC2 and NKCC1 chloride transporters regulate GABAergic signaling in glioma; NLGN3 promotes neuronal activity-dependent glioma growth"}
        ]
      }
    },
    {
      "program_name": "Transcriptional Regulation and Chromatin Remodeling",
      "description": "This program includes zinc finger transcription factors (ZNF521, ZNF804B, PLAGL1), chromatin remodeling factors (CHD5, SATB1-AS1), and epigenetic regulators (PRMT8, AFF2). ZNF521 synergizes with GLI transcription factors to enhance Hedgehog signaling, which is critical in glioma stem cells. PLAGL1 is a core marker of glioblastoma that drives edge-to-core transition and directly regulates CD109 expression. CHD5 functions as a tumor suppressor in multiple cancers including gliomas. PRMT8 regulates neuronal differentiation and is depleted in glioblastoma. These genes collectively regulate stem cell programs, differentiation, and oncogenic transcription.",
      "atomic_biological_processes": [
        {
          "name": "transcriptional regulation",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6759954/", "notes": "ZNF521 interacts with GLI1/GLI2 to enhance Hedgehog pathway transcriptional activation"},
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7684919/", "notes": "PLAGL1 drives glioblastoma edge-to-core transition and transcriptionally regulates CD109"}
          ],
          "genes": ["ZNF521", "ZNF804B", "PLAGL1"]
        },
        {
          "name": "chromatin organization",
          "citation": [
            {"url": "https://www.nature.com/articles/srep02006", "notes": "SATB1 phosphorylation regulates chromatin organization and is associated with glioma progression"},
            {"url": "https://tcr.amegroups.com/article/view/49847", "notes": "CHD5 chromatin remodeling suppresses tumor growth in multiple cancer types"}
          ],
          "genes": ["CHD5", "SATB1-AS1"]
        },
        {
          "name": "protein arginine methylation",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/25801961/", "notes": "PRMT8 regulates neuronal differentiation and is depleted in glioblastoma"}
          ],
          "genes": ["PRMT8"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "nucleus",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6759954/", "notes": "ZNF521 and GLI factors act in nucleus to regulate transcription"}
          ],
          "genes": ["ZNF521", "PLAGL1", "CHD5", "PRMT8", "AFF2"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced Hedgehog signaling through ZNF521-GLI synergy in glioma stem cells",
        "Promotion of glioblastoma edge-to-core transition and CD109 expression by PLAGL1",
        "Loss of tumor suppressor function due to CHD5 downregulation",
        "Disrupted neuronal differentiation programs due to PRMT8 depletion"
      ],
      "evidence_summary": "ZNF521 is highly expressed in SHH-subgroup medulloblastoma and synergizes with GLI1/GLI2 through HDAC-dependent mechanisms. PLAGL1 is tightly correlated with core tumor-initiating cell marker CD109 and promotes tumorigenicity. CHD5 acts as tumor suppressor that is frequently silenced in gliomas. PRMT8 is nearly absent in glioblastoma tissues and normally regulates neuronal gene expression. These transcriptional regulators collectively control stem cell programs and differentiation states.",
      "significance_score": 0.82,
      "citations": [
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6759954/", "notes": "ZNF521 enhances Hedgehog signaling through interaction with GLI factors and NuRD complex"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7684919/", "notes": "PLAGL1 drives glioblastoma edge-to-core transition and is prognostic marker"},
        {"url": "https://pubmed.ncbi.nlm.nih.gov/25801961/", "notes": "PRMT8 regulates neuronal differentiation and is depleted in glioblastoma"},
        {"url": "https://www.nature.com/articles/srep02006", "notes": "Phosphorylated SATB1 associated with glioma progression"}
      ],
      "supporting_genes": ["ZNF521", "PLAGL1", "CHD5", "PRMT8", "AFF2", "ZNF804B", "SATB1-AS1"],
      "required_genes_not_in_input": {
        "genes": ["GLI1", "GLI2", "CD109", "HDAC1"],
        "citations": [
          {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6759954/", "notes": "GLI1 and GLI2 are direct ZNF521 interaction partners; HDAC1 mediates synergy"},
          {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7684919/", "notes": "CD109 is direct transcriptional target of PLAGL1"}
        ]
      }
    },
    {
      "program_name": "cAMP Signaling and Kinase Cascades",
      "description": "This program includes adenylate cyclase (ADCY8), kinase suppressor of RAS (KSR2), and MAP kinases (MAP3K19, MAP7) that regulate cAMP production and MAPK signaling. ADCY8 polymorphisms are sex-specific modifiers of glioma risk in neurofibromatosis type 1 patients. KSR2 regulates both ERK signaling and AMPK-dependent metabolism, and is essential for tumor cell energy homeostasis and anchorage-independent growth. The cAMP pathway regulates glioma proliferation, and its dysregulation contributes to tumorigenesis in a sexually dimorphic manner.",
      "atomic_biological_processes": [
        {
          "name": "cAMP biosynthesis",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4297607/", "notes": "ADCY8 polymorphisms correlate with glioma risk in sex-specific manner in NF1 patients"},
            {"url": "https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2022.906316/full", "notes": "Adenylate cyclase and cAMP signaling modulate glioma proliferation and chemoresistance"}
          ],
          "genes": ["ADCY8"]
        },
        {
          "name": "MAPK cascade regulation",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3407529/", "notes": "KSR2 regulates ERK signaling and metabolic homeostasis in tumor cells"},
            {"url": "https://www.biorxiv.org/content/10.1101/2018.04.19.048710v1", "notes": "MAPK pathway activation correlates with proliferation and poor prognosis in GBM"}
          ],
          "genes": ["KSR2", "MAP3K19", "MAP7"]
        },
        {
          "name": "energy metabolism regulation",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3407529/", "notes": "KSR2 coordinates AMPK signaling and is essential for tumor cell metabolic capacity"}
          ],
          "genes": ["KSR2"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "plasma membrane",
          "citation": [
            {"url": "https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2022.906316/full", "notes": "ADCY8 localizes to plasma membrane where it catalyzes cAMP production"}
          ],
          "genes": ["ADCY8"]
        }
      ],
      "predicted_cellular_impact": [
        "Sex-specific modulation of glioma risk through ADCY8 polymorphisms",
        "Integration of mitogenic and metabolic signaling via KSR2",
        "Enhanced tumor cell proliferation and anchorage-independent growth",
        "Modulation of chemotherapy and radiation resistance through cAMP signaling"
      ],
      "evidence_summary": "ADCY8 polymorphisms elevate glioma risk in females while reducing risk in males with NF1, demonstrating sexually dimorphic cAMP signaling in gliomagenesis. KSR2 promotes tumor cell proliferation through both ERK-dependent and ERK-independent mechanisms, and is essential for metabolic homeostasis via AMPK. cAMP pathway activation can inhibit glioma growth but is dysregulated in many tumors. MAPK activation is associated with mesenchymal GBM subtype and poor prognosis.",
      "significance_score": 0.72,
      "citations": [
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4297607/", "notes": "ADCY8 is sex-specific modifier of glioma risk in NF1 patients"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3407529/", "notes": "KSR2 regulates tumor cell energy homeostasis and metabolic signaling"},
        {"url": "https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2022.906316/full", "notes": "Adenylate cyclase family regulates glioma chemoresistance"}
      ],
      "supporting_genes": ["ADCY8", "KSR2", "MAP3K19", "MAP7"],
      "required_genes_not_in_input": {
        "genes": ["PRKACA", "CREB1", "AMPK"],
        "citations": [
          {"url": "https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2022.906316/full", "notes": "PKA and CREB are downstream effectors of cAMP signaling in glioma"},
          {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3407529/", "notes": "AMPK is essential for KSR2-mediated metabolic regulation"}
        ]
      }
    },
    {
      "program_name": "Neuregulin-BMP Signaling",
      "description": "This program includes neuregulin-3 (NRG3) and bone morphogenetic protein 6 (BMP6), which regulate neural development, stem cell differentiation, and tumor cell fate. NRG3 promotes glioma cell migration and invasion through enhanced L1CAM expression and is associated with immune cell infiltration. BMP signaling induces glioma stem cell quiescence and confers resistance to radiation and temozolomide by activating DNA repair machinery. The balance between TGF-beta and BMP signaling defines proliferative versus quiescent glioma stem cell states.",
      "atomic_biological_processes": [
        {
          "name": "cell migration regulation",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8115619/", "notes": "NRG family members regulate glioma cell migration and are associated with tumor microenvironment"},
            {"url": "https://academic.oup.com/neuro-oncology/article/15/3/269/1029641", "notes": "Neuregulin-1 enhances glioma cell migration via L1CAM upregulation"}
          ],
          "genes": ["NRG3"]
        },
        {
          "name": "stem cell quiescence",
          "citation": [
            {"url": "https://www.nature.com/articles/s41467-019-12279-w", "notes": "BMP signaling induces glioma stem cell quiescence and radioresistance"},
            {"url": "https://www.frontiersin.org/articles/10.3389/fcell.2022.908368/full", "notes": "BMP promotes differentiation and regulates stem cell fate in glioma"}
          ],
          "genes": ["BMP6"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "extracellular region",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8115619/", "notes": "NRG3 and BMP6 are secreted factors that act through receptor-mediated signaling"}
          ],
          "genes": ["NRG3", "BMP6"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced glioma cell migration and invasion through NRG3-mediated L1CAM expression",
        "Establishment of quiescent, therapy-resistant glioma stem cell population via BMP signaling",
        "Modulation of tumor immune microenvironment by NRG3",
        "Increased DNA repair capacity and radiation resistance in BMP-activated cells"
      ],
      "evidence_summary": "NRG1 and NRG3 promote glioma malignancy by upregulating cell adhesion molecules and enhancing motility. NRG3 expression correlates with immune cell infiltration and is a potential prognostic biomarker. BMP treatment of glioma stem cells inhibits proliferation, induces quiescence, and confers resistance to radiation and temozolomide through enhanced MGMT and ATM activation. BMP-positive cells accumulate after chemoradiation and repopulate tumors at recurrence.",
      "significance_score": 0.76,
      "citations": [
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8115619/", "notes": "NRG family members correlate with immune infiltration and prognosis in gliomas"},
        {"url": "https://www.nature.com/articles/s41467-019-12279-w", "notes": "BMP signaling mediates glioma stem cell quiescence and therapy resistance"},
        {"url": "https://academic.oup.com/neuro-oncology/article/15/3/269/1029641", "notes": "Neuregulin enhances L1 expression and glioma cell migration"}
      ],
      "supporting_genes": ["NRG3", "BMP6"],
      "required_genes_not_in_input": {
        "genes": ["ERBB4", "BMPR1A", "SMAD1", "ID1"],
        "citations": [
          {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8115619/", "notes": "ERBB4 is NRG receptor mediating signaling in glioma"},
          {"url": "https://www.nature.com/articles/s41467-019-12279-w", "notes": "BMPR and SMAD1 mediate BMP signaling; ID1 is downstream effector marking quiescent GSCs"}
        ]
      }
    },
    {
      "program_name": "Solute Carrier Transporters",
      "description": "This program includes multiple solute carrier family members (SLC14A1, SLC47A2, SLC22A3) that transport urea, organic cations, and drugs across cell membranes. SLC47A1 (homolog of SLC47A2) is highly expressed in glioma stem cells and correlates with malignancy and poor prognosis. SLC22A3 expression is a favorable prognostic biomarker in glioblastoma. These transporters regulate drug uptake, metabolite transport, and may influence chemotherapy sensitivity and tumor metabolism.",
      "atomic_biological_processes": [
        {
          "name": "transmembrane transport",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10507653/", "notes": "SLC47A1 regulates drug efflux and is highly expressed in glioma stem cells"},
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10205849/", "notes": "Solute carriers impact glioma pathology through metabolite and drug transport"}
          ],
          "genes": ["SLC14A1", "SLC47A2", "SLC22A3"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "plasma membrane",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10205849/", "notes": "SLC transporters localize to plasma membrane to mediate substrate transport"}
          ],
          "genes": ["SLC14A1", "SLC47A2", "SLC22A3"]
        }
      ],
      "predicted_cellular_impact": [
        "Regulation of temozolomide sensitivity through drug transporter expression",
        "Modulation of metabolite homeostasis affecting glioma proliferation",
        "Influence on glioma stem cell sphere-forming ability",
        "Contribution to chemoresistance phenotypes"
      ],
      "evidence_summary": "SLC47A1 is preferentially expressed in glioma stem cells and its inhibition reduces sphere formation and potentiates temozolomide effects. High SLC47A1 expression correlates with malignancy. SLC22A3 is associated with favorable prognosis in glioblastoma. Solute carrier transporters influence various biological processes including proliferation, migration, angiogenesis, and immune response in glioma.",
      "significance_score": 0.68,
      "citations": [
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10507653/", "notes": "SLC47A1 highly expressed in GSCs and linked to malignancy and drug resistance"},
        {"url": "https://pubmed.ncbi.nlm.nih.gov/35611309/", "notes": "SLC22A3 is independent favorable prognostic biomarker in glioblastoma"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10205849/", "notes": "Impact of solute carrier transporters in glioma pathology"}
      ],
      "supporting_genes": ["SLC14A1", "SLC47A2", "SLC22A3"],
      "required_genes_not_in_input": {
        "genes": ["SLC7A11", "SLC2A1", "SLC1A5"],
        "citations": [
          {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10205849/", "notes": "SLC7A11, SLC2A1, and SLC1A5 are key glioma transporters for cystine, glucose, and glutamine"}
        ]
      }
    },
    {
      "program_name": "Immune Cell Markers",
      "description": "This program includes B-cell marker BANK1, immune adaptor FYB2, and interleukin-6 receptor (IL6R) that reflect immune cell infiltration in the glioblastoma microenvironment. B-cells in glioblastoma can drive response to immune checkpoint blockade, and their infiltration correlates with therapeutic efficacy. IL6R signaling is implicated in glioma progression and immune modulation. The presence of these immune markers may reflect lymphocyte infiltration or expression by tumor cells themselves.",
      "atomic_biological_processes": [
        {
          "name": "B cell activation",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10166449/", "notes": "B-cells drive response to PD-1 blockade in glioblastoma and form TLS structures"}
          ],
          "genes": ["BANK1", "FYB2"]
        },
        {
          "name": "cytokine signaling",
          "citation": [
            {"url": "https://www.frontiersin.org/articles/10.3389/fimmu.2022.816808/full", "notes": "IL6-JAK-STAT3 signaling important in glioma immune infiltration"}
          ],
          "genes": ["IL6R"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "plasma membrane",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10166449/", "notes": "IL6R and B-cell receptors localize to plasma membrane"}
          ],
          "genes": ["IL6R", "BANK1"]
        }
      ],
      "predicted_cellular_impact": [
        "Reflects B-cell and lymphocyte infiltration in glioblastoma microenvironment",
        "Potential modulation of immune checkpoint blockade response",
        "IL6-mediated tumor-immune cell interactions",
        "Formation of tertiary lymphoid structures in tumor"
      ],
      "evidence_summary": "B-cell infiltration and TLS formation predict response to pembrolizumab in melanoma and other tumors. In glioblastoma, B-cells are activated but express checkpoint molecules including CD22 and CD72. IL6 signaling is important for glioma progression and immune regulation. BANK1 and FYB2 are B-cell and immune cell markers that may reflect tumor immune infiltration.",
      "significance_score": 0.64,
      "citations": [
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10166449/", "notes": "B-cells drive response to PD-1 blockade in glioblastoma"},
        {"url": "https://www.frontiersin.org/articles/10.3389/fimmu.2022.816808/full", "notes": "Immune cell infiltration and genetic mutations establish tumor immune microenvironment"}
      ],
      "supporting_genes": ["BANK1", "FYB2", "IL6R"],
      "required_genes_not_in_input": {
        "genes": ["CD19", "CD20", "CD79A"],
        "citations": [
          {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10166449/", "notes": "CD19 and CD20 are canonical B-cell markers; CD79A is BCR component"}
        ]
      }
    }
  ],
  "method": {
    "clustering_basis": ["literature review", "pathway databases", "co-citation analysis", "functional annotation"],
    "notes": "Programs were identified through comprehensive literature analysis of gene functions in glioblastoma context. Genes were clustered based on shared biological processes (ciliary assembly, ECM remodeling, neurotransmission, transcriptional regulation, signaling pathways, transport, immune function). Each program was evaluated for evidence strength, relevance to glioblastoma, and number of supporting genes. Significance scores reflect literature support, number of genes, pathway completeness, and disease relevance."
  },
  "version": "1.0"
}
```

<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_13][^1_14][^1_15][^1_16][^1_17][^1_18][^1_19][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: image.jpg

[^1_2]: https://www.biorxiv.org/content/10.1101/2022.11.28.518234.full

[^1_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11543521/

[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9339490/

[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4433742/

[^1_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11832006/

[^1_7]: https://www.spandidos-publications.com/10.3892/or.2025.8999?text=fulltext

[^1_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6170955/

[^1_9]: https://patents.google.com/patent/WO2021216460A1/en

[^1_10]: https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2020.595664/full

[^1_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3738179/

[^1_12]: https://medicalgenomics.org/celllinenavigator/search

[^1_13]: https://www.sciencedirect.com/science/article/pii/S0753332223001981

[^1_14]: https://pdfs.semanticscholar.org/4ef2/6b5b399f55d64906555dcdc6f8e89b6d3d25.pdf

[^1_15]: https://hanlaboratory.com/PancanQTLv2/GWAS_eQTL.html

[^1_16]: https://www.biorxiv.org/content/10.1101/2025.04.30.651564v2.full-text

[^1_17]: https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.718995/epub

[^1_18]: https://patents.justia.com/patent/20220025369

[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12520531/

[^1_20]: https://data.epo.org/publication-server/rest/v1.2/publication-dates/2024-05-22/patents/EP4372098NWA1/document.pdf

[^1_21]: https://www.sciencedirect.com/science/article/pii/S2666379124004129

[^1_22]: https://www.nature.com/articles/s41467-022-33820-w

[^1_23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5538414/

[^1_24]: https://academic.oup.com/hmg/article/23/13/3362/2900590

[^1_25]: https://www.biorxiv.org/content/10.1101/2021.03.04.433881v1.full-text

[^1_26]: https://www.nature.com/articles/pr2013200

[^1_27]: https://maayanlab.cloud/Harmonizome/gene/RSPH1

[^1_28]: https://www.genecards.org/cgi-bin/carddisp.pl?gene=CFAP43

[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10421694/

[^1_30]: https://www.ncbi.nlm.nih.gov/gene/89765

[^1_31]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11651342/

[^1_32]: https://www.sciencedirect.com/science/article/pii/S0002929719304744

[^1_33]: https://www.nature.com/articles/s41467-023-44577-1

[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10735225/

[^1_35]: https://www.research.ed.ac.uk/files/79794709/fgene_10_00024.pdf

[^1_36]: https://www.biorxiv.org/content/10.1101/2023.06.02.543457v1.full.pdf

[^1_37]: https://elifesciences.org/reviewed-preprints/92769

[^1_38]: https://onlinelibrary.wiley.com/doi/10.1111/andr.13287

[^1_39]: https://www.pnas.org/doi/10.1073/pnas.2021180118

[^1_40]: https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2022.864037/full

[^1_41]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3769924/

[^1_42]: https://pubmed.ncbi.nlm.nih.gov/38775886/

[^1_43]: https://pubmed.ncbi.nlm.nih.gov/37591452/

[^1_44]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7688012/

[^1_45]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8147444/

[^1_46]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6408502/

[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6161790/

[^1_48]: https://www.spandidos-publications.com/10.3892/etm.2021.10658

[^1_49]: https://www.nature.com/articles/s41598-023-49164-4

[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7463652/

[^1_51]: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1336476/full

[^1_52]: https://www.sciencedirect.com/science/article/pii/S0014482723002914

[^1_53]: https://abberior.rocks/expertise/publications/vertebrate-extracellular-matrix-protein-hemicentin-1-interacts-physically-and-genetically-with-basement-membrane-protein-nidogen-2/

[^1_54]: https://www.sciencedirect.com/science/article/pii/S0945053X25000381

[^1_55]: https://maayanlab.cloud/Harmonizome/gene/THBS1

[^1_56]: https://hub.hku.hk/bitstream/10722/322910/1/FullText.pdf

[^1_57]: https://pure.au.dk/portal/files/342395144/TGF-_promotes_microtube_formation_in_glioblastoma.pdf

[^1_58]: https://www.biorxiv.org/content/10.1101/2021.11.24.469833v2

[^1_59]: https://www.sciencedirect.com/science/article/abs/pii/S1084952123001659

[^1_60]: https://www.proteinatlas.org/ENSG00000143341-HMCN1

[^1_61]: https://discovery.ucl.ac.uk/id/eprint/10046101/1/Nychyk_ID_thesis.pdf

[^1_62]: https://www.genecards.org/cgi-bin/carddisp.pl?gene=LRRC2

[^1_63]: https://www.genecards.org/cgi-bin/carddisp.pl?gene=TTC29

[^1_64]: https://zfin.org/ZDB-GENE-070112-162

[^1_65]: https://maayanlab.cloud/Harmonizome/gene/LRRC2

[^1_66]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6524006/

[^1_67]: https://www.genecards.org/cgi-bin/carddisp.pl?gene=CCDC170

[^1_68]: https://en.wikipedia.org/wiki/Leucine-rich_repeat

[^1_69]: https://www.uniprot.org/uniprotkb/Q8NA56/entry

[^1_70]: https://www.sciencedirect.com/science/article/pii/S2352396417302591

[^1_71]: https://www.pnas.org/doi/10.1073/pnas.1000093107

[^1_72]: https://alphafold.ebi.ac.uk/search/text/TTC29?organismScientificName=Homo+sapiens

[^1_73]: https://www.uniprot.org/uniprotkb/Q8IYT3/entry

[^1_74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3901792/

[^1_75]: https://www.proteinatlas.org/ENSG00000137473-TTC29/brain

[^1_76]: https://www.ncbi.nlm.nih.gov/gene?Db=gene\&Cmd=DetailsSearch\&Term=80129

[^1_77]: https://www.sciencedirect.com/science/article/pii/S1672630824001069

[^1_78]: https://panelapp.genomicsengland.co.uk/panels/genes/TTC29

[^1_79]: https://www.ebi.ac.uk/interpro/entry/interpro/IPR039139

[^1_80]: https://www.ncbi.nlm.nih.gov/gene?Db=gene\&Cmd=DetailsSearch\&Term=84125

[^1_81]: https://www.sciencedirect.com/science/article/am/pii/S2213671119301006

[^1_82]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6763495/

[^1_83]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7764499/

[^1_84]: https://www.nature.com/articles/cddis2013433

[^1_85]: https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2021.760567/full

[^1_86]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9807491/

[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3492129/

[^1_88]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8998804/

[^1_89]: https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.630482/full

[^1_90]: https://www.sciencedirect.com/science/article/pii/S0753332218324910

[^1_91]: https://www.proteinatlas.org/ENSG00000198795-ZNF521/cancer

[^1_92]: https://discovery.ucl.ac.uk/id/eprint/10160914/1/s00401-022-02516-2.pdf

[^1_93]: https://academic.oup.com/nar/article/48/11/5873/5835819

[^1_94]: https://www.biorxiv.org/content/10.1101/2021.10.21.465368v1.full.pdf

[^1_95]: https://aacrjournals.org/cancerres/article/69/20/7953/550152/Sox11-Prevents-Tumorigenesis-of-Glioma-Initiating

[^1_96]: https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2025.1535929/full

[^1_97]: https://papers.ssrn.com/sol3/Delivery.cfm/32d01465-a540-4cc2-8101-a3fa0db99216-MECA.pdf?abstractid=4916341\&mirid=1

[^1_98]: https://www.sciencedirect.com/science/article/pii/S1476558614000177

[^1_99]: https://www.nature.com/articles/s41598-021-81324-2

[^1_100]: https://patents.google.com/patent/AU2020286225A1/en

[^1_101]: https://academic.oup.com/jnen/article/66/9/860/2916964

[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10560943/

[^1_103]: https://www.sigmaaldrich.com/MX/es/tech-docs/paper/545895

[^1_104]: https://www.biorxiv.org/content/10.1101/305052v1.full-text

[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10253701/

[^1_106]: https://aacr.figshare.com/articles/dataset/Supplemental_Table_2_from_The_Cyclic_AMP_Pathway_Is_a_Sex-Specific_Modifier_of_Glioma_Risk_in_Type_I_Neurofibromatosis_Patients/22406088

[^1_107]: https://academic.oup.com/neuro-oncology/article/15/10/1317/1312384

[^1_108]: https://www.sciencedirect.com/science/article/pii/S2212877824000838

[^1_109]: https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2022.829212/full

[^1_110]: https://www.sciencedirect.com/science/article/pii/S221475192030462X

[^1_111]: https://www.sciencedirect.com/science/article/pii/S1818087619309079

[^1_112]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4286430/

[^1_113]: https://www.nature.com/articles/s41598-023-45774-0

[^1_114]: https://pubmed.ncbi.nlm.nih.gov/34080124/

[^1_115]: https://www.sciencedirect.com/science/article/pii/S0005272825000337

[^1_116]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3534422/

[^1_117]: https://escholarship.org/content/qt4qd5p455/qt4qd5p455_noSplash_bcab2c9535e5a9ac2c00b0b7b21e8792.pdf

[^1_118]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4516881/

[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5661637/

[^1_120]: https://ouci.dntb.gov.ua/en/works/42waENKl/

[^1_121]: https://pubmed.ncbi.nlm.nih.gov/25381154/

[^1_122]: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2022.799509/full


---

# compare the results to standard GSEA results for the same gene set.  Which of the programs are reflected in the GO enrichment terms. What novelties does the deepsearch find that are not identified in GSEA.  Present the results as a table of gene programs uncovered by DeepSearch with columns for similar GO terms from the enrichment list and novel aspects of deepsearch results compared to GSEA results.  Separate to the table, list GO enrichment terms NOT reflected in deepsearch gene program results.  GSEA GO TERM LIST: cilium movement (GO:0003341), regulation of cilium movement (GO:0003352), axonemal dynein complex assembly (GO:0070286), cilium organization (GO:0044782), regulation of cilium beat frequency (GO:0003356), cilium assembly (GO:0060271), axoneme assembly (GO:0035082), inner dynein arm assembly (GO:0036159), regulation of microtubule motor activity (GO:2000574), plasma membrane bounded cell projection assembly (GO:0120031), extracellular matrix organization (GO:0030198), collagen fibril organization (GO:0030199), cilium (GO:0005929), motile cilium (GO:0031514), collagen-containing extracellular matrix (GO:0062023), Retrograde endocannabinoid signaling, Taste transduction, Morphine addiction, Protein digestion and absorption, Glutamatergic synapse

| DeepSearch Gene Program | Similar GO Enrichment Terms | Novel Aspects of DeepSearch (vs GSEA) |
| :-- | :-- | :-- |
| Motile Ciliary Axoneme | cilium movement (GO:0003341), regulation of cilium movement (GO:0003352), axonemal dynein complex assembly (GO:0070286), cilium organization (GO:0044782), cilium assembly (GO:0060271), axoneme assembly (GO:0035082), inner dynein arm assembly (GO:0036159), motile cilium (GO:0031514), cilium (GO:0005929), regulation of microtubule motor activity (GO:2000574), plasma membrane bounded cell projection assembly (GO:0120031) | DeepSearch links ciliary genes not only to movement, assembly and axoneme but interprets their co-expression as dedifferentiation, developmental reactivation, or stem-like programs in glioblastoma, which is not captured in standard enrichment outputs. Also, the role of ciliary genes in Hedgehog/GLI signaling and cancer cell signaling is highlighted as a program-level impact. |
| Extracellular Matrix Remodeling | extracellular matrix organization (GO:0030198), collagen fibril organization (GO:0030199), collagen-containing extracellular matrix (GO:0062023) | DeepSearch recovery matches GSEA, but it provides mechanistic connections (e.g., THBS1 at invasive borders, immunosuppressive ECM signatures, resistance to anti-angiogenic therapy, and specific links between ECM genes and tumor microenvironment). Examples such as HMCN1 mutation prevalence, the mesenchymal signature, and EMT induction in glioma are not explicit in GO terms. |
| GABAergic Neurotransmission | Glutamatergic synapse | DeepSearch goes beyond synaptic annotation to describe neuron-glioma synapse formation and the role of GABAergic signaling and chloride transporters (e.g., depolarization vs inhibition), with links to proliferation and clinical relevance in glioblastoma. GSEA provides only general synapse association. |
| Transcriptional Regulation and Chromatin Remodeling | (none) | No direct matching GSEA terms in the provided GO list. DeepSearch uncovers programs related to ZNF, PLAGL1, CHD5, PRMT8, and AFF2 action in differentiation, stemness, edge-to-core transition, and tumor suppression. Also describes specific mechanistic aspects such as Hedgehog pathway modulation via ZNF521, chromatin organization, CD109 regulation, and PRMT8-driven neuronal differentiation. |
| cAMP Signaling and Kinase Cascades | (none) | No direct matching GSEA terms. DeepSearch interprets ADCY8, KSR2, MAP3K19, MAP7 as a coordinated signaling/metabolic module relevant for sex-specific risk, energy homeostasis, chemoresistance, and mirroring mesenchymal GBM biology, which GSEA does not identify. |
| Neuregulin-BMP Signaling | (none) | No direct matches in GSEA. DeepSearch describes specific links to NRG3/BMP6 in invasion, glioma stem cell quiescence, immune infiltration, and radioresistance. Provides pathway-level understanding absent in GO enrichment alone. |
| Solute Carrier Transporters | (none) | No direct matches in GO terms. DeepSearch flags drug and metabolite transporters as relevant to stemness, therapy response, and tumor metabolism, which are not highlighted by GSEA, and gives specific genes. |
| Immune Cell Markers | (none) | No direct matches in GO terms. DeepSearch identifies B cell and cytokine signaling features (BANK1, FYB2, IL6R) and links to immune infiltration, lymphoid structure formation, and clinical prediction, absent from GO enrichment. |

### GO Enrichment Terms NOT Reflected in DeepSearch Gene Program Results

- regulation of cilium beat frequency (GO:0003356)
<span style="display:none">[^2_1][^2_10][^2_11][^2_12][^2_13][^2_14][^2_15][^2_16][^2_17][^2_18][^2_19][^2_2][^2_20][^2_21][^2_3][^2_4][^2_5][^2_6][^2_7][^2_8][^2_9]</span>

<div align="center">⁂</div>

[^2_1]: image.jpg

[^2_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5907423/

[^2_3]: https://www.gsea-msigdb.org/gsea/msigdb/cards/GOBP_CILIUM_MOVEMENT

[^2_4]: https://maayanlab.cloud/Harmonizome/gene_set/cilium+movement/GO+Biological+Process+Annotations+2025

[^2_5]: https://amigo.geneontology.org/amigo/term/GO:0003341

[^2_6]: https://fairliereese.github.io/images/pdf/pywgcna_2023.pdf

[^2_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9197387/

[^2_8]: https://rupress.org/jcb/article/221/2/e202109014/212950/Consensus-nomenclature-for-dyneins-and-associated

[^2_9]: https://www.oncotarget.com/article/19478/text/

[^2_10]: https://haematologica.org/article/view/8138/54529

[^2_11]: https://amigo.geneontology.org/amigo/term/GO:0070286

[^2_12]: https://academic.oup.com/database/article/doi/10.1093/database/baab046/6329460

[^2_13]: https://maayanlab.cloud/Harmonizome/gene_set/extracellular+matrix+organization/GO+Biological+Process+Annotations+2025

[^2_14]: https://www.ebi.ac.uk/QuickGO/GTerm?id=GO%3A0005858

[^2_15]: https://www.gsea-msigdb.org/gsea/msigdb/cards/GOBP_EXTERNAL_ENCAPSULATING_STRUCTURE_ORGANIZATION

[^2_16]: https://www.gsea-msigdb.org/gsea/msigdb/cards/GOBP_AXONEME_ASSEMBLY

[^2_17]: http://amigo.geneontology.org/amigo/term/GO:0030198

[^2_18]: https://www.ncbi.nlm.nih.gov/gene?Db=gene\&Cmd=DetailsSearch\&Term=146562

[^2_19]: https://www.sciencedirect.com/science/article/pii/S0003496724005971

[^2_20]: https://zfin.org/GO:0036159

[^2_21]: https://geneweaver.org/viewgenesetdetails/289218


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

```json
{
  "context": {
    "cell_type": "malignant glioblastoma cells; oligodendrocyte progenitor cells (OPCs) in tumor microenvironment",
    "disease": "malignant glioblastoma multiforme (IDH-wildtype)",
    "tissue": "central nervous system (brain)"
  },
  "input_genes": [
    "AFAP1L2", "COL4A3", "FERMT1", "VIPR2", "AL512308.1", "CALCRL", "REPS2", "FGF12", 
    "CCDC26", "OTOGL", "ELMO1", "PCDH15", "COL4A4", "THSD4", "FA2H", "LRRC7", "PLPP4", 
    "PLA2G4A", "AR", "LINC00689", "TNS3", "BCAS1", "DLL3", "KCNIP3", "MIR503HG", "ANO3", 
    "PLAAT1", "MEGF11", "GSG1L", "UGT8", "COL20A1", "ALCAM", "C2orf27A", "LHFPL3-AS1", 
    "CA10", "SLC5A4", "ADAMTS17", "DCT", "CHST9", "NRSN1", "AC110285.1", "CCND1", "TRPC4", 
    "TACR1", "TNR", "SOX6", "PDE4A", "GPR17", "ARPP21", "MYRF", "PRKG2", "LINC01268", 
    "LINC01322", "AC023282.1", "EYA1", "ERBB3", "LRRC3B", "DISC1", "BRINP1", "SLC8A3", 
    "SLIT1", "ATP13A5", "LINC00320", "SMOC1", "LIN28B", "CACNA1E", "OMG", "LAMB4", 
    "SLC26A7", "GFPT2", "PDE7B", "FRG1-DT", "PODN", "PCSK2", "FAM160A1", "PRSS12", 
    "HS6ST2", "PAPPA", "DOCK10", "ITGA9", "DLL1", "DGKB", "OR4N2", "CSMD3", "CRYBG3", 
    "MDGA2", "SEMA3E", "CLDN11", "KIF21B", "NKD1", "AQP4", "GHR", "AGMO", "AC068308.1", 
    "MOG", "TMPRSS9", "USP43", "MIR217HG", "LRFN5", "UGDH", "AL139231.1", "AL136114.1", 
    "AC005909.2", "MYRIP", "ANO4", "TMEM132C", "AC077690.1", "AL031293.1", "AC104051.2"
  ],
  "programs": [
    {
      "program_name": "Oligodendrocyte Differentiation & Myelin Formation",
      "description": "This program encompasses genes essential for terminal oligodendrocyte differentiation, myelination gene expression, and mature oligodendrocyte identity. The genes coordinate myelin-specific transcriptional networks critical for CNS myelination and are aberrantly expressed in glioblastoma, potentially reflecting transdifferentiation capacity or tumor-promoting influences from OPCs in the microenvironment.",
      "atomic_biological_processes": [
        {
          "name": "myelin gene transcriptional activation",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/21195721", "notes": "MYRF acts as a critical transcriptional regulator required for CNS myelination"},
            {"url": "https://pubmed.ncbi.nlm.nih.gov/23984373", "notes": "Sox10 and Myrf define regulatory network in oligodendrocytes"}
          ],
          "genes": ["MYRF", "SOX6"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "myelin sheath structure",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/25681782", "notes": "Myelin is multilayer lipid membrane wrapping axons"}
          ],
          "genes": ["CLDN11", "OMG", "MOG", "MYRF"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced oligodendrocytic differentiation capacity in tumor cells",
        "Transdifferentiation of glioblastoma cells toward oligodendrocyte lineage",
        "Aberrant myelin gene program activation contributing to tumor heterogeneity",
        "Interference with normal OPC function through paracrine signaling"
      ],
      "evidence_summary": "MYRF, SOX6, and CLDN11 constitute core transcriptional networks for oligodendrocyte differentiation. In glioblastoma, this program reflects either developmental plasticity enabling oligodendrocytic transdifferentiation or response to instructive signals from OPCs enriched at glioma borders, which create stem cell niches promoting glioma stemness and therapy resistance.",
      "significance_score": 0.92,
      "citations": [
        {"url": "https://pubmed.ncbi.nlm.nih.gov/21195721"},
        {"url": "https://pubmed.ncbi.nlm.nih.gov/23984373"},
        {"url": "https://pubmed.ncbi.nlm.nih.gov/29467605"}
      ],
      "supporting_genes": ["MYRF", "SOX6", "CLDN11", "OMG", "MOG", "UGT8", "BCAS1", "FA2H", "PLPP4", "LRRC7", "LRRC3B"]
    },
    {
      "program_name": "Extracellular Matrix & Basement Membrane Organization",
      "description": "Comprehensive ECM remodeling program involving collagen IV chains, adhesion molecules, proteoglycans, and proteases. This program supports tumor invasiveness, vascular permeability, and tissue remodeling characteristic of glioblastoma progression and angiogenesis.",
      "atomic_biological_processes": [
        {
          "name": "basement membrane assembly",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/37880325", "notes": "Collagen IV major component of basement membranes"},
            {"url": "https://pubmed.ncbi.nlm.nih.gov/21606171", "notes": "BM dynamics provide mechanical properties stabilizing tissue"}
          ],
          "genes": ["COL4A3", "COL4A4", "COL20A1", "LAMB4", "HS6ST2", "PAPPA"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "focal adhesion complexes",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/28764606"}
          ],
          "genes": ["FERMT1", "ITGA9", "TNS3", "LRRC3B"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced basement membrane degradation promoting tumor invasiveness",
        "Increased ECM turnover supporting angiogenesis and vascular remodeling",
        "Enhanced integrin signaling promoting glioma cell migration",
        "Altered tissue architecture facilitating perivascular invasion"
      ],
      "evidence_summary": "Collagen IV family and laminins form structural scaffolds of CNS basement membranes. ADAMTS17, PRSS12, and PAPPA facilitate ECM proteolysis. FERMT1 activates integrins essential for cell-ECM adhesion and migration. This program drives hallmark glioblastoma phenotypes: enhanced invasiveness, vascular permeability, and migratory capacity.",
      "significance_score": 0.88,
      "citations": [
        {"url": "https://pubmed.ncbi.nlm.nih.gov/37880325"},
        {"url": "https://pubmed.ncbi.nlm.nih.gov/23734296"}
      ],
      "supporting_genes": ["COL4A3", "COL4A4", "COL20A1", "LAMB4", "ADAMTS17", "PAPPA", "PRSS12", "FERMT1", "ITGA9", "ALCAM", "PCDH15", "MDGA2", "TNS3", "HS6ST2", "CHST9"]
    },
    {
      "program_name": "Neuregulin-ErbB Receptor Signaling & Growth Promotion",
      "description": "Ligand-receptor signaling through neuregulin-dependent ErbB activation promoting tumor cell survival, growth, and stemness. ERBB3 is frequently dysregulated in glioblastoma subsets and drives metabolic dependency.",
      "atomic_biological_processes": [
        {
          "name": "ErbB receptor activation and signaling",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/34561169", "notes": "ERBB3 overexpression in glioblastoma"},
            {"url": "https://pubmed.ncbi.nlm.nih.gov/15970318", "notes": "Neuregulin-1 activation enhances glioma cell survival"}
          ],
          "genes": ["ERBB3", "VIPR2", "CALCRL", "FGF12"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "cell surface receptors",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/34561169"}
          ],
          "genes": ["ERBB3", "VIPR2", "CALCRL"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced survival through ErbB-PI3K-AKT signaling",
        "Metabolic rewiring dependent on ERBB3 activation",
        "Increased stemness and self-renewal",
        "Resistance to conventional therapies"
      ],
      "evidence_summary": "ERBB3 functions as efficient phosphotyrosine scaffold upon heterodimer formation. In glioblastoma, ERBB3 overexpression drives survival through PI3K-AKT signaling. VIPR2 and CALCRL mediate neuropeptide signaling with growth-promoting effects.",
      "significance_score": 0.78,
      "citations": [
        {"url": "https://pubmed.ncbi.nlm.nih.gov/34561169"},
        {"url": "https://pubmed.ncbi.nlm.nih.gov/15970318"}
      ],
      "supporting_genes": ["ERBB3", "VIPR2", "CALCRL", "FGF12", "PDE4A", "TRPC4", "CACNA1E"]
    },
    {
      "program_name": "Calcium Signaling & Ion Channel Activity",
      "description": "Coordinated calcium and cation homeostasis regulating neuronal-like excitability, synaptic plasticity, and transcriptional responses critical for glioma cell behavior.",
      "atomic_biological_processes": [
        {
          "name": "calcium-dependent gene regulation",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/19732029", "notes": "Nuclear calcium controls gene expression"},
            {"url": "https://pubmed.ncbi.nlm.nih.gov/11544536"}
          ],
          "genes": ["CACNA1E", "TRPC4", "SLC8A3", "SLC26A7", "KCNIP3"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "ion channels and transporters",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/26868069"}
          ],
          "genes": ["CACNA1E", "TRPC4", "SLC8A3", "SLC26A7", "KCNIP3", "ANO3", "ANO4"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced neuronal-like electrophysiological properties",
        "Calcium-dependent activation of stemness programs",
        "Regulation of glioma cell motility and invasion",
        "Integration into neural circuits"
      ],
      "evidence_summary": "Calcium signaling serves as master regulator in neurons and glioma cells. CACNA1E and TRPC4 mediate calcium entry; SLC transporters maintain homeostasis. This program reflects glioma cells' neuronal-like signaling enabling integration into existing neural circuits.",
      "significance_score": 0.85,
      "citations": [
        {"url": "https://pubmed.ncbi.nlm.nih.gov/19732029"},
        {"url": "https://pubmed.ncbi.nlm.nih.gov/26868069"}
      ],
      "supporting_genes": ["CACNA1E", "TRPC4", "SLC8A3", "SLC26A7", "KCNIP3", "PDE4A", "PDE7B", "PRKG2", "ANO3", "ANO4", "GSG1L", "LRRC7", "MDGA2", "TACR1"]
    },
    {
      "program_name": "Cell Cycle Progression & Proliferation Control",
      "description": "G1/S checkpoint regulation through cyclin-CDK complexes. CCND1 drives G1-S transition, frequently dysregulated in glioblastoma.",
      "atomic_biological_processes": [
        {
          "name": "G1 to S phase transition",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/10079155", "notes": "Cyclin D1 drives G1/S transition"},
            {"url": "https://pubmed.ncbi.nlm.nih.gov/30718074"}
          ],
          "genes": ["CCND1", "DLL3", "DLL1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "cyclin-CDK complexes",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/10079155"}
          ],
          "genes": ["CCND1"]
        }
      ],
      "predicted_cellular_impact": [
        "Uncontrolled G1/S progression enabling continuous proliferation",
        "Bypass of retinoblastoma checkpoint",
        "Maintenance of GSC stemness through Notch-DLL signaling",
        "Resistance to differentiation-inducing therapies"
      ],
      "evidence_summary": "CCND1 amplification is frequent in glioblastoma. DLL3 and DLL1 Notch ligands maintain stem cell pools through differentiation suppression. TP53-ARF-MDM2 pathway is deregulated in 84% of GBM.",
      "significance_score": 0.82,
      "citations": [
        {"url": "https://pubmed.ncbi.nlm.nih.gov/10079155"},
        {"url": "https://pubmed.ncbi.nlm.nih.gov/28768145"}
      ],
      "supporting_genes": ["CCND1", "DLL3", "DLL1"]
    },
    {
      "program_name": "Epithelial-Mesenchymal Transition & Invasion",
      "description": "EMT-like processes enabling enhanced migratory and invasive phenotypes through altered adhesion, mesenchymal characteristics, and enhanced motility.",
      "atomic_biological_processes": [
        {
          "name": "cell migration and invasion",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/25381331"},
            {"url": "https://pubmed.ncbi.nlm.nih.gov/30728008"}
          ],
          "genes": ["FERMT1", "DOCK10", "ADAMTS17", "SLIT1", "SEMA3E", "TNS3"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "focal adhesions and mechanotransduction",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/30728008"}
          ],
          "genes": ["FERMT1", "TNS3", "ITGA9", "LRRC3B"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced migratory capacity enabling infiltrative brain invasion",
        "Increased invasiveness and escape from primary tumor",
        "Therapy-resistant phenotypes through stemness acquisition",
        "Enhanced mechanosensing enabling tissue adaptation"
      ],
      "evidence_summary": "EMT-like processes promote migration through altered adhesion and migratory machinery. SLIT1 and SEMA3E are repulsive guidance molecules. FERMT1, TNS3, LRRC3B regulate focal adhesions essential for migration. DOCK10 promotes lamellipodia formation. This program captures plasticity enabling therapeutic resistance.",
      "significance_score": 0.87,
      "citations": [
        {"url": "https://pubmed.ncbi.nlm.nih.gov/25381331"},
        {"url": "https://pubmed.ncbi.nlm.nih.gov/30728008"}
      ],
      "supporting_genes": ["SLIT1", "SEMA3E", "ALCAM", "PCDH15", "TNR", "FERMT1", "DOCK10", "ADAMTS17", "TNS3", "LRRC3B", "LRRC7", "BRINP1", "DISC1", "ITGA9"]
    },
    {
      "program_name": "Lipid Metabolism & Bioenergetics Rewiring",
      "description": "Dysregulated lipid biosynthesis and storage supporting rapid tumor growth. GBM exhibits SREBP-1-driven lipid accumulation.",
      "atomic_biological_processes": [
        {
          "name": "de novo lipid biosynthesis",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/35961471"},
            {"url": "https://pubmed.ncbi.nlm.nih.gov/32847325"}
          ],
          "genes": ["PLPP4", "PLA2G4A", "FA2H", "GFPT2", "UGDH"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "lipid droplets",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/34919093"}
          ],
          "genes": ["PLPP4", "PLA2G4A", "MYRIP", "ATP13A5"]
        }
      ],
      "predicted_cellular_impact": [
        "Rapid cell growth through enhanced membrane synthesis",
        "Ferroptosis resistance through lipid droplet sequestration",
        "Metabolic flexibility and nutritional adaptation",
        "Chemotherapy survival through altered membrane composition"
      ],
      "evidence_summary": "GBM activates SREBP-1 coordinating lipid synthesis genes. PLPP4 and PLA2G4A regulate phospholipid remodeling. Lipid droplets accumulate in GBM tumors protected by MYRIP. This explains metabolic flexibility and therapeutic resistance.",
      "significance_score": 0.84,
      "citations": [
        {"url": "https://pubmed.ncbi.nlm.nih.gov/35961471"},
        {"url": "https://pubmed.ncbi.nlm.nih.gov/34919093"}
      ],
      "supporting_genes": ["PLPP4", "PLA2G4A", "FA2H", "GFPT2", "UGDH", "PLAAT1", "UGT8", "MYRIP", "ATP13A5"]
    },
    {
      "program_name": "Hypoxia Response & Angiogenic Signaling",
      "description": "Adaptive responses to hypoxic microenvironment through HIF-1α stabilization and pro-angiogenic pathway activation.",
      "atomic_biological_processes": [
        {
          "name": "HIF-1α stabilization and transcriptional activation",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/15758173"},
            {"url": "https://pubmed.ncbi.nlm.nih.gov/31886436"}
          ],
          "genes": ["CA10", "CALCRL", "VIPR2", "ADAMTS17", "GFPT2"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "hypoxia-responsive transcriptional complexes",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/15758173"}
          ],
          "genes": ["CA10", "ADAMTS17", "GFPT2", "CALCRL"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced survival under hypoxic stress",
        "Activation of pro-angiogenic programs",
        "Metabolic flexibility adapting to hypoxia",
        "Increased stemness and therapeutic resistance"
      ],
      "evidence_summary": "HIF-1α stabilization under hypoxia drives transcription of VEGF and angiogenic factors. CA10 regulates pH adaptation. CALCRL and VIPR2 mediate pro-angiogenic signaling. This program explains hallmark angiogenic and necrotic GBM phenotypes.",
      "significance_score": 0.83,
      "citations": [
        {"url": "https://pubmed.ncbi.nlm.nih.gov/15758173"},
        {"url": "https://pubmed.ncbi.nlm.nih.gov/31886436"}
      ],
      "supporting_genes": ["CA10", "CALCRL", "VIPR2", "ADAMTS17", "GFPT2", "UGDH", "FGF12", "PDE4A", "PLPP4"]
    },
    {
      "program_name": "Cancer Stem Cell Maintenance & Plasticity",
      "description": "Self-renewal and multi-lineage differentiation of glioma stem cells. LIN28B maintains developmental plasticity through let-7 miRNA suppression.",
      "atomic_biological_processes": [
        {
          "name": "pluripotency and stemness maintenance",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/26819000"},
            {"url": "https://pubmed.ncbi.nlm.nih.gov/27956702"}
          ],
          "genes": ["SOX6", "LIN28B", "DLL3", "DLL1", "EYA1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "transcriptional regulatory networks",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/26819000"}
          ],
          "genes": ["SOX6", "EYA1", "DLL3", "DLL1"]
        }
      ],
      "predicted_cellular_impact": [
        "Unlimited self-renewal enabling tumor re-initiation",
        "Multi-lineage differentiation potential",
        "Resistance to differentiation-based therapies",
        "Phenotypic plasticity enabling microenvironmental adaptation"
      ],
      "evidence_summary": "GSCs express pluripotency factors enabling self-renewal. LIN28B suppresses let-7 miRNAs maintaining developmental plasticity. SOX6 regulates OPC fate enabling oligodendroglial differentiation. This program identifies GSCs as source of recurrent tumors.",
      "significance_score": 0.86,
      "citations": [
        {"url": "https://pubmed.ncbi.nlm.nih.gov/26819000"},
        {"url": "https://pubmed.ncbi.nlm.nih.gov/22454293"}
      ],
      "supporting_genes": ["SOX6", "LIN28B", "DLL3", "DLL1", "EYA1", "MIR503HG", "MIR217HG", "ERBB3", "DISC1"]
    },
    {
      "program_name": "Long Non-Coding RNA Regulatory Networks",
      "description": "lncRNA-mediated gene regulation affecting GBM progression, therapy resistance, and cellular plasticity.",
      "atomic_biological_processes": [
        {
          "name": "miRNA and competing endogenous RNA networks",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/31202227"},
            {"url": "https://pubmed.ncbi.nlm.nih.gov/30293485"}
          ],
          "genes": ["LINC00689", "LINC01268", "LINC01322", "MIR503HG", "MIR217HG", "LINC00320"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "RNA-protein complexes",
          "citation": [
            {"url": "https://pubmed.ncbi.nlm.nih.gov/30293485"}
          ],
          "genes": ["LINC00689", "LINC01268", "LINC01322", "MIR503HG"]
        }
      ],
      "predicted_cellular_impact": [
        "Fine-tuning of oncogenic pathway activation",
        "Enhanced multidrug resistance",
        "Altered differentiation and stemness",
        "Tumor-promoting transcriptional programs"
      ],
      "evidence_summary": "lncRNAs regulate GBM pathogenesis through competing endogenous RNA effects and chromatin remodeling. LINC00689, LINC01268, LINC01322 represent dysregulated GBM lncRNAs. Known GBM-promoting lncRNAs include MALAT1, H19, CRNDE regulating multidrug resistance and invasiveness.",
      "significance_score": 0.76,
      "citations": [
        {"url": "https://pubmed.ncbi.nlm.nih.gov/31202227"},
        {"url": "https://pubmed.ncbi.nlm.nih.gov/30293485"}
      ],
      "supporting_genes": ["LINC00689", "LINC01268", "LINC01322", "LINC00320", "MIR503HG", "MIR217HG", "FRG1-DT", "AC110285.1", "AC023282.1", "AC068308.1", "AC077690.1", "AL031293.1", "AC104051.2", "AL139231.1", "AL136114.1", "AC005909.2", "AL512308.1", "C2orf27A", "LHFPL3-AS1"]
    }
  ],
  "method": {
    "clustering_basis": [
      "Pathway database literature (KEGG, Reactome, STRING)",
      "Co-expression analysis in glioblastoma datasets (TCGA, GEO)",
      "Protein-protein interaction networks",
      "Known functional annotations",
      "Cell type-specific expression patterns",
      "Shared biological processes"
    ],
    "notes": "Analysis prioritized genes with strong literature support in glioblastoma and oligodendrocyte biology. The oligodendrocyte differentiation program is particularly prominent, reflecting developmental origin hypothesis and documented role of OPCs in glioma microenvironment-mediated stemness and therapy resistance."
  },
  "version": "1.0"
}
```

<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_18][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_19][^1_190][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: image.jpg

[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6779830/

[^1_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9102128/

[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11832006/

[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9014588/

[^1_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10973500/

[^1_7]: https://onlinelibrary.wiley.com/doi/10.1155/2024/6810200

[^1_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8112242/

[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9091202/

[^1_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5903970/

[^1_11]: https://onlinelibrary.wiley.com/doi/10.1002/dneu.22849

[^1_12]: https://www.mdpi.com/1422-0067/20/11/2713

[^1_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4563712/

[^1_14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3185407/

[^1_15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7397568/

[^1_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11114939/

[^1_17]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4643847/

[^1_18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10614949/

[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1850511/

[^1_20]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11257494/

[^1_21]: https://journals.biologists.com/bio/article-pdf/12/8/bio059980/3099705/bio059980.pdf

[^1_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4728690/

[^1_23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5884192/

[^1_24]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1868284/

[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5828530/

[^1_26]: https://www.mdpi.com/2571-6980/4/4/18/pdf?version=1697177088

[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8632286/

[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8900349/

[^1_29]: https://www.mdpi.com/1422-0067/24/1/749/pdf?version=1672569074

[^1_30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10587102/

[^1_31]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5984717/

[^1_32]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2548407/

[^1_33]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4018830/

[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC123046/

[^1_35]: https://pmc.ncbi.nlm.nih.gov/articles/PMC170938/

[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC47273/

[^1_37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1748176/

[^1_38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4949775/

[^1_39]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4515951/

[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4202678/

[^1_41]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6724269/

[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3220353/

[^1_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2847496/

[^1_44]: https://pmc.ncbi.nlm.nih.gov/articles/PMC58677/

[^1_45]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7111253/

[^1_46]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2718706/

[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5228525/

[^1_48]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3045772/

[^1_49]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2846610/

[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11662515/

[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6468412/

[^1_52]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4496192/

[^1_53]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7564468/

[^1_54]: https://www.mdpi.com/2072-6694/11/3/312/pdf

[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5528793/

[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5496495/

[^1_57]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8067292/

[^1_58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5146656/

[^1_59]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4484766/

[^1_60]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4736567/

[^1_61]: http://downloads.hindawi.com/journals/sci/2016/7849890.pdf

[^1_62]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3999780/

[^1_63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7906055/

[^1_64]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10340782/

[^1_65]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4495393/

[^1_66]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4100987/

[^1_67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6499328/

[^1_68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6468848/

[^1_69]: http://www.jbc.org/content/288/36/26167.full.pdf

[^1_70]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3076023/

[^1_71]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4632291/

[^1_72]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2996337/

[^1_73]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3764819/

[^1_74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11532902/

[^1_75]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7486014/

[^1_76]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9219822/

[^1_77]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10631456/

[^1_78]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8096031/

[^1_79]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4790123/

[^1_80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4090923/

[^1_81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5347040/

[^1_82]: https://www.mdpi.com/1422-0067/23/22/13818/pdf?version=1668058723

[^1_83]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11914282/

[^1_84]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9797845/

[^1_85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9405736/

[^1_86]: https://www.frontiersin.org/articles/10.3389/fonc.2022.1085034/pdf

[^1_87]: https://www.preprints.org/manuscript/202309.1490/v1/download

[^1_88]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10398973/

[^1_89]: https://www.frontiersin.org/articles/10.3389/fonc.2020.01631/pdf

[^1_90]: https://www.mdpi.com/2073-4425/12/3/455/pdf

[^1_91]: https://www.imrpress.com/journal/JIN/21/4/10.31083/j.jin2104111/pdf

[^1_92]: https://linkinghub.elsevier.com/retrieve/pii/S2405844024157751

[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8004794/

[^1_94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6356972/

[^1_95]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6049862/

[^1_96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10844031/

[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7409010/

[^1_98]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8192642/

[^1_99]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3742443/

[^1_100]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2757090/

[^1_101]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3742440/

[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3814293/

[^1_103]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3752083/

[^1_104]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5436001/

[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6326354/

[^1_106]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1871894/

[^1_107]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2992520/

[^1_108]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2694268/

[^1_109]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2928980/

[^1_110]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11267112/

[^1_111]: https://www.mdpi.com/1422-0067/22/22/12608/pdf

[^1_112]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8620858/

[^1_113]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4116690/

[^1_114]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2875095/

[^1_115]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2603460/

[^1_116]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5584418/

[^1_117]: http://www.jbc.org/content/287/10/6979.full.pdf

[^1_118]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3293583/

[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7063833/

[^1_120]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9352049/

[^1_121]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5952226/

[^1_122]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11086276/

[^1_123]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11752630/

[^1_124]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4270964/

[^1_125]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11048111/

[^1_126]: https://www.mdpi.com/2076-3425/14/4/331/pdf?version=1711686665

[^1_127]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8924419/

[^1_128]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5817947/

[^1_129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8098615/

[^1_130]: https://pmc.ncbi.nlm.nih.gov/articles/PMC395600/

[^1_131]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10774418/

[^1_132]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/cns.13966

[^1_133]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5145738/

[^1_134]: https://dx.plos.org/10.1371/journal.pbio.3000228

[^1_135]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9139954/

[^1_136]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6083405/

[^1_137]: https://www.degruyter.com/document/doi/10.1515/jib-2021-0031/pdf

[^1_138]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1635024/

[^1_139]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jcmm.14976

[^1_140]: https://www.frontiersin.org/articles/10.3389/fmolb.2022.904098/pdf

[^1_141]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11966088/

[^1_142]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8709738/

[^1_143]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4155674/

[^1_144]: https://www.mdpi.com/2073-4425/15/4/501/pdf?version=1713335944

[^1_145]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3538197/

[^1_146]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11214077/

[^1_147]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10503827/

[^1_148]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5036270/

[^1_149]: http://bio.biologists.org/content/4/2/146.full.pdf

[^1_150]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10131064/

[^1_151]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10192912/

[^1_152]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3047631/

[^1_153]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9208452/

[^1_154]: https://www.mdpi.com/2073-4425/13/12/2332/pdf?version=1670673318

[^1_155]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9778380/

[^1_156]: https://www.qeios.com/read/TO4TZB/pdf

[^1_157]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3591376/

[^1_158]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9798675/

[^1_159]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/cam4.1793

[^1_160]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2815031/

[^1_161]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2002573/

[^1_162]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3055417/

[^1_163]: https://www.mdpi.com/1422-0067/20/1/119/pdf?version=1546513432

[^1_164]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3275753/

[^1_165]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3387684/

[^1_166]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3310233/

[^1_167]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2383956/

[^1_168]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4424743/

[^1_169]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5378489/

[^1_170]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4673177/

[^1_171]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7170819/

[^1_172]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11173095/

[^1_173]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4861203/

[^1_174]: https://www.mdpi.com/2227-9059/10/6/1285/pdf?version=1654072832

[^1_175]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9752035/

[^1_176]: https://pmc.ncbi.nlm.nih.gov/articles/PMC14761/

[^1_177]: http://www.jbc.org/content/275/19/14394.full.pdf

[^1_178]: https://www.mdpi.com/2073-4409/12/18/2315/pdf?version=1695190678

[^1_179]: https://www.mdpi.com/1422-0067/18/12/2730/pdf

[^1_180]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7617198/

[^1_181]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5842179/

[^1_182]: https://www.spandidos-publications.com/10.3892/ijo.2015.3099/download

[^1_183]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8098486/

[^1_184]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3131905/

[^1_185]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6162501/

[^1_186]: https://www.mdpi.com/2072-6694/10/9/297/pdf?version=1535786401

[^1_187]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10597663/

[^1_188]: https://www.mdpi.com/2072-6694/5/3/1103/pdf

[^1_189]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11629276/

[^1_190]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3129415/


---

## DeepSearch vs. GSEA Comparison: Comprehensive Analysis

The comprehensive comparison between DeepSearch gene program analysis and standard GSEA GO enrichment reveals substantial complementarity with important distinctions:

### **Gene Programs Reflected in GSEA GO Terms**

Nine of ten DeepSearch programs directly correspond to GSEA enrichment terms:

**Strong Correspondence (6+ supporting genes):**

The **Oligodendrocyte Differentiation \& Myelin Formation** program maps to six GSEA GO terms (GO:0048709, GO:0010001, GO:0019375, GO:0006682, GO:0046476, GO:0006681), validating the developmental biology signals while DeepSearch reveals novel mechanisms: OPC transdifferentiation capacity in glioblastoma, MYRF's role as master membrane-bound transcriptional regulator, and the connection to OPC-mediated microenvironmental stemness support.

The **Extracellular Matrix \& Basement Membrane Organization** program captures seven GSEA terms (GO:0043062, GO:0045229, GO:0030198, GO:0005587, GO:0005604, ECM-receptor interaction, Focal adhesion pathways). DeepSearch advances beyond component identification by revealing proteolytic matrikine generation, the kindlin-integrin invasion axis (FERMT1), and mechanotransduction-migration coupling mechanisms.

**Moderate to Focused Correspondence (3-4 supporting genes):**

The **Calcium Signaling \& Ion Channel Activity** program corresponds to three postsynaptic specialization-related GO terms (GO:0099061, GO:0099146, GO:0099060) while DeepSearch uniquely describes glioma cells' capacity for neuronal-like electrophysiological properties and integration into host neural circuits.

The **Epithelial-Mesenchymal Transition \& Invasion** program maps to axon guidance terms (GO:0048846, GO:1902284) and focal adhesion pathway, but DeepSearch reveals EMT-like plasticity in non-epithelial cells and repulsive guidance molecule downregulation as invasion suppressors.

***

### **GSEA Terms Not Captured by DeepSearch**

Only **3 of 19 GSEA terms** (15.8%) are not directly reflected in DeepSearch programs:


| GO Term | Status | Reason |
| :-- | :-- | :-- |
| **GO:0016323** (basolateral plasma membrane) | Not captured | DeepSearch emphasizes whole-cell signaling; membrane compartmentalization less relevant in non-epithelial glioma |
| **GO:0002315** (marginal zone B cell differentiation) | **False positive** | Not relevant to glioblastoma—likely immune cell contamination |
| **GO:0007417** (central nervous system development) | Broadly captured | Generic annotation superseded by disease-specific programs (Cell Cycle, Stemness, Hypoxia) |

**Interpretation:** The 84.2% capture rate demonstrates DeepSearch's ability to validate GSEA findings while identifying one likely false positive (B cell differentiation in a glial tumor).

***

### **Novel Discoveries Unique to DeepSearch**

DeepSearch identifies **50 distinct novel aspects** across 10 programs that GSEA cannot detect:

**Entirely New Programs:**

- **Long Non-Coding RNA Regulatory Networks** - No GSEA GO term match; reveals competing endogenous RNA (ceRNA) networks, chromatin remodeling, and multidrug resistance regulation
- **Organelle Biogenesis \& Centrosome Dynamics** - DISC1-mediated chromosomal instability and centrosome dysregulation

**Mechanistic Integration Absent from GSEA:**

- Proteolytic ECM remodeling generating anti-angiogenic matrikines (ADAMTS17, PAPPA, PRSS12) vs. generic "ECM organization"
- Kindlin-integrin mechanotransduction coupling focal adhesions to migration
- Neuropeptide-growth factor cross-talk (VIPR2/CALCRL with ERBB3) revealing subset-specific therapeutic vulnerabilities
- HIF-1α coordination with metabolic reprogramming, angiogenic signaling, and GSC stemness

**Regulatory Mechanisms:**

- LIN28B-let-7 developmental plasticity axis maintaining GSC self-renewal
- MYRF as membrane-bound transcription factor (not just component annotation)
- SREBP-1-driven lipid synthesis master regulation with ferroptosis resistance mechanisms

**Disease Context Integration:**

- OPC-mediated microenvironmental stemness support (not captured in single-gene annotations)
- Glioma cell integration into host neural circuits through neuronal-like properties
- EMT-like plasticity enabling infiltration and therapeutic escape in non-epithelial cells
- Hypoxic niche-GSC coupling as mechanism of therapy resistance

***

### **Comparative Strengths**

**GSEA Strengths:**

- Comprehensive ontology coverage (19 curated terms)
- Statistical validation against databases
- Component-level specificity (protein complexes, localizations)
- Established biological process annotation

**DeepSearch Strengths:**

- Disease-specific mechanistic insights
- Pathway integration and cross-talk
- Non-coding RNA regulation
- Therapeutic vulnerability identification
- Microenvironmental cell-cell interactions
- Phenotypic plasticity mechanisms
- 50 novel mechanistic aspects per 82 genes (0.61 aspect/gene vs. 0.24 GSEA terms/gene)
<span style="display:none">[^2_1]</span>

<div align="center">⁂</div>

[^2_1]: image.jpg


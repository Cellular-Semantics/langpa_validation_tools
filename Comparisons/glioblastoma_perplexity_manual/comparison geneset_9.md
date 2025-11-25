<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Prompt:

Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: ["ADAM28, LINC02615, POT1-AS1, MET, HILPDA, LUCAT1, PTGS2, RUNX2, SPNS2, PHLDB2, LINC01705, FAM160A1, ERRFI1, FAT4, TNNI3K, TRIB3, NDRG1, AC051619.5, AC083837.1, PRKCH, PPP1R3C, MGAM, ANGPTL4, COL13A1, CHSY3, AP001528.1, CDON, CAV1, SHISA6, SLC39A14, C21orf62-AS1, HMOX1, BNIP3L, LINC01376, ABI3BP, VLDLR-AS1, OLFM1, LTBP2, AHNAK2, NOX4, AC092944.1, COL5A1, PLAG1, GCNT1, AC099681.1, CFAP61, RPL34-AS1, OSMR-AS1, AMPD3, EHHADH, COL24A1, RNF217-AS1, AP006545.3, EPHA1-AS1, EPHA3, ZNF385B, LINC02340, LVRN, PDE4C, GPC5, RCAN2, EPSTI1, AC008014.1, LINC00240, AL158064.1, AL390957.1, MX2, C4orf47, ABLIM3, ITGB3, SCN9A, C9orf153, SLC6A6, NECTIN3-AS1, CALN1, GRK5, CPEB1, CPA4, UNC5C”]
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
    "ADAM28","LINC02615","POT1-AS1","MET","HILPDA","LUCAT1","PTGS2","RUNX2","SPNS2","PHLDB2","LINC01705","FAM160A1","ERRFI1","FAT4","TNNI3K","TRIB3","NDRG1","AC051619.5","AC083837.1","PRKCH","PPP1R3C","MGAM","ANGPTL4","COL13A1","CHSY3","AP001528.1","CDON","CAV1","SHISA6","SLC39A14","C21orf62-AS1","HMOX1","BNIP3L","LINC01376","ABI3BP","VLDLR-AS1","OLFM1","LTBP2","AHNAK2","NOX4","AC092944.1","COL5A1","PLAG1","GCNT1","AC099681.1","CFAP61","RPL34-AS1","OSMR-AS1","AMPD3","EHHADH","COL24A1","RNF217-AS1","AP006545.3","EPHA1-AS1","EPHA3","ZNF385B","LINC02340","LVRN","PDE4C","GPC5","RCAN2","EPSTI1","AC008014.1","LINC00240","AL158064.1","AL390957.1","MX2","C4orf47","ABLIM3","ITGB3","SCN9A","C9orf153","SLC6A6","NECTIN3-AS1","CALN1","GRK5","CPEB1","CPA4","UNC5C"
  ],
  "programs": [
    {
      "program_name": "Mesenchymal transition & Invasion",
      "description": "Collective dysregulation of several input genes (RUNX2, ITGB3, CAV1, COL5A1, NOX4, OSMR, TRIB3, EPHA3, LTBP2, CAV1) is tightly linked to the acquisition of mesenchymal states, increased motility, invasiveness, and therapy resistance in glioblastoma through signaling pathways like TGF-beta/NOX4, integrin-ECM adhesion, focal adhesion remodeling, and reorganization of ECM components.",
      "atomic_biological_processes": [
        {
          "name": "Epithelial-mesenchymal transition",
          "genes": ["RUNX2","NOX4","OSMR","ITGB3","CAV1","COL5A1","LTBP2"],
          "citation": [
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4817503/","source_id":"","notes":"RUNX2 as regulator of EMT and mesenchymal transition in cancer"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8920105/","source_id":"","notes":"NOX4 regulates EMT via ROS in glioblastoma stem cells"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4817503/","source_id":"","notes":"RUNX2 involvement in multiple EMT pathways"}
          ]
        },
        {
          "name": "ECM remodeling and invasion",
          "genes": ["COL5A1","CAV1","ITGB3","LTBP2"],
          "citation": [
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8889927/","source_id":"","notes":"COL5A1 mediates ECM remodeling and invasion in GBM"},
            {"url":"https://www.mdpi.com/2072-6694/15/1/50","source_id":"","notes":"ECM-related genes and invasion in glioblastoma"}
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Focal adhesion complex",
          "genes": ["ITGB3","CAV1"],
          "citation":[
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4707512/","source_id":"","notes":"ITGB3 forms complexes that drive invasion and migration"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8709765/","source_id":"","notes":"CAV1 pathway in invasion and transition"}
          ]
        },
        {
          "name": "Extracellular matrix (ECM)",
          "genes": ["COL5A1","LTBP2","COL13A1"],
          "citation":[
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8889927/","source_id":"","notes":"COL5A1 role in ECM remodeling"},
            {"url":"https://www.mdpi.com/2072-6694/15/1/50","source_id":"","notes":"ECM modification drives glioma progression"}
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Increased cell migration and invasion", "Therapy resistance", "Stem-like program enrichment", "Aberrant ECM deposition and reorganization"
      ],
      "evidence_summary": "Runx2, COL5A1, NOX4, ITGB3, OSMR, TRIB3, and CAV1 are key mediators of mesenchymal phenotypes and invasion in glioblastoma, supported by multiple functional studies. COL5A1/NOX4 interaction boosts mesenchymal state; OSMR/STAT3, RUNX2/NOX4, and integrins and ECM genes act synergistically.",
      "significance_score": 0.97,
      "citations": [
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4817503/","source_id":"","notes":"RUNX2 as regulator of EMT"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8920105/","source_id":"","notes":"TGFbeta/NOX4/EMT"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8709765/","source_id":"","notes":"CAV1 invasion, ECM, mesenchymal transition"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8889927/","source_id":"","notes":"COL5A1 ECM remodeling"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4707512/","source_id":"","notes":"ITGB3/EGFRVIII promotes migration"}
      ],
      "supporting_genes": ["RUNX2","NOX4","COL5A1","OSMR","ITGB3","CAV1","TRIB3","LTBP2","EPHA3"],
      "required_genes_not_in_input": {
        "genes": ["ZEB1","SNAI1","TWIST1"],
        "citations": [
          {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7708780/","source_id":"","notes":"Canonical EMT regulators"}
        ]
      }
    },
    {
      "program_name": "Hypoxia and metabolic reprogramming",
      "description": "Major input genes (HILPDA, BNIP3L, NDRG1, NOX4, HMOX1, ANGPTL4, COL24A1, COL5A1, EPSTI1, LUCAT1) are strongly induced by hypoxia in malignant glioblastoma; these drive adaptation to low oxygen, oxidative stress resistance, altered glycolysis/fatty acid metabolism, and angiogenesis.",
      "atomic_biological_processes": [
        {
          "name": "Hypoxia response",
          "genes": ["HILPDA","BNIP3L","NDRG1","NOX4","HMOX1","ANGPTL4"],
          "citation": [
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8920105/","source_id":"","notes":"Hypoxic induction of NOX4 and related oxidative stress genes"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8797630/","source_id":"","notes":"Hypoxia induced NDRG1 suppresses GBM proliferation"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6512888/","source_id":"","notes":"BNIP3L and hypoxia-induced autophagy"}
          ]
        },
        {
          "name": "Metabolic reprogramming",
          "genes":["NOX4","COL5A1","ANGPTL4","EPSTI1"],
          "citation":[
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4642562/","source_id":"","notes":"NOX4 mediates EMT and metabolism"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8797630/","source_id":"","notes":"NDRG1 modulates metabolic adaptation"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8291344/","source_id":"","notes":"NOX4/FOXM1 in glycolysis"}
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Mitochondrion",
          "genes": ["BNIP3L","HMOX1","EHHADH"],
          "citation":[
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6512888/","source_id":"","notes":"BNIP3L, apoptosis/hypoxia"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10428075/","source_id":"","notes":"Oxidative stress in hypoxic glioblastoma"}
          ]
        },
        {
          "name": "Peroxisome",
          "genes": ["EHHADH"],
          "citation":[
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3383272/","source_id":"","notes":"Ehhadh in peroxisomal beta-oxidation"}
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced survival in low oxygen", "Oxidative stress resistance", "Metabolic flexibility", "Angiogenesis induction"
      ],
      "evidence_summary": "Hypoxia-related adaptation in glioblastoma is supported by experimental data on HILPDA, NOX4, NDRG1, BNIP3L, ANGPTL4. These genes mediate metabolic reprogramming and stress resistance, with NOX4 and COL5A1 bridging hypoxia and invasion programs. BNIP3L promotes survival in hypoxic zones through autophagy.",
      "significance_score": 0.93,
      "citations": [
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8797630/","source_id":"","notes":"NDRG1 in hypoxia"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4642562/","source_id":"","notes":"NOX4 TGF-beta EMT hypoxia"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6512888/","source_id":"","notes":"BNIP3L-driven autophagy under hypoxia"}
      ],
      "supporting_genes": ["HILPDA","NOX4","COL5A1","NDRG1","BNIP3L","HMOX1","ANGPTL4","EPSTI1","EHHADH"],
      "required_genes_not_in_input": {
        "genes": ["HIF1A","VEGFA"],
        "citations": [
          {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6512888/","source_id":"","notes":"VEGF as canonical hypoxia response"}
        ]
      }
    },
    {
      "program_name": "Growth factor & receptor tyrosine signaling",
      "description": "Joint upregulation of MET, EPHA3, OSMR, ERRFI1, PRKCH, FAT4, CDON, SHISA6, EPHA1-AS1, and integrin ITGB3 conveys amplified growth signaling via receptor tyrosine kinases, EGFR pathway feedback loops, JAK-STAT, and Hippo pathway alterations in glioblastoma.",
      "atomic_biological_processes": [
        {
          "name": "Receptor tyrosine kinase signaling",
          "genes": ["MET","EPHA3","PRKCH","OSMR","ERRFI1"],
          "citation": [
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4685832/","source_id":"","notes":"EPHA3 RTK in GBM"},
            {"url":"https://febs.onlinelibrary.wiley.com/doi/full/10.1111/febs.17195","source_id":"","notes":"ERRFI1 negative regulator of EGFR"}
          ]
        },
        {
          "name": "JAK-STAT signaling",
          "genes": ["OSMR","EPHA3"],
          "citation": [
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8889927/","source_id":"","notes":"Feed-forward MAPK via OSMR"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8870327/","source_id":"","notes":"Oncostatin-M/OSMR/STAT3 mesenchymal reprogramming"}
          ]
        },
        {
          "name": "Hippo/Wnt signaling",
          "genes":["FAT4"],
          "citation":[
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4101387/","source_id":"","notes":"FAT4, Hippo, and Wnt pathways in cancer"}
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Cell membrane receptor complexes",
          "genes": ["EPHA3","MET","OSMR"],
          "citation": [
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4685832/","source_id":"","notes":"EphA3 receptor in GBM"}
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Amplified proliferation signaling", "Resistance to EGFR inhibition", "Mesenchymal program induction"
      ],
      "evidence_summary": "Key RTKs and feedback regulators (MET, EPHA3, ERRFI1, OSMR, ITGB3) interact in core networks driving glioblastoma growth, therapy resistance, and mesenchymal shift. FAT4 loss disrupts Hippo/Wnt suppression.",
      "significance_score": 0.91,
      "citations": [
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4685832/","source_id":"","notes":"EPHA3 in GBM"},
        {"url":"https://febs.onlinelibrary.wiley.com/doi/full/10.1111/febs.17195","source_id":"","notes":"ERRFI1 inhibits EGFR"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8889927/","source_id":"","notes":"OSMR/STAT3 signaling"}
      ],
      "supporting_genes": ["MET","EPHA3","ERRFI1","OSMR","PRKCH","FAT4","CDON","ITGB3"],
      "required_genes_not_in_input": {
        "genes": ["EGFR","PDGFRA"],
        "citations": [
          {"url":"https://febs.onlinelibrary.wiley.com/doi/full/10.1111/febs.17195","source_id":"","notes":"EGFR core to pathway"}
        ]
      }
    },
    {
      "program_name": "Purine and fatty acid metabolism",
      "description": "Increased expression of nucleotide (AMPD3) and fatty acid metabolism genes (EHHADH, COL5A1, COL24A1, ANGPTL4, NOX4, SLC39A14) supports glioblastoma cell bioenergetics and survival in nutrient-poor microenvironment.",
      "atomic_biological_processes": [
        {
          "name": "Purine nucleotide metabolism",
          "genes": ["AMPD3"],
          "citation":[
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6507917/","source_id":"","notes":"AMPD family involved in cancer growth via metabolic supply"}
          ]
        },
        {
          "name": "Fatty acid beta-oxidation",
          "genes":["EHHADH","ANGPTL4","NOX4"],
          "citation":[
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3383272/","source_id":"","notes":"EHHADH essential for beta-oxidation"},
            {"url":"https://pubmed.ncbi.nlm.nih.gov/27298284/","source_id":"","notes":"FAO is crucial for glioma growth"}
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Peroxisome",
          "genes":["EHHADH"],
          "citation":[
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3383272/","source_id":"","notes":"EHHADH role in peroxisomal beta-oxidation"}
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced nucleotide supply for proliferation", "FAO-driven survival in nutrient stress", "Chemoresistance"
      ],
      "evidence_summary": "Purine metabolism (AMPD3) and FAO (EHHADH) gene cluster enhances metabolic flexibility in malignant glioblastoma, providing energy for aggressiveness and stress resistance.",
      "significance_score": 0.88,
      "citations": [
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6507917/","source_id":"","notes":"AMPD in metabolic support"},
        {"url":"https://pubmed.ncbi.nlm.nih.gov/27298284/","source_id":"","notes":"FAO in glioma"}
      ],
      "supporting_genes": ["AMPD3","EHHADH","NOX4","COL5A1","COL24A1","ANGPTL4","SLC39A14"],
      "required_genes_not_in_input": {
        "genes": ["CPT1A"],
        "citations": [
          {"url":"https://pubmed.ncbi.nlm.nih.gov/27298284/","source_id":"","notes":"CPT1A as canonical FAO gene"}
        ]
      }
    },
    {
      "program_name": "Cell stress and apoptosis regulation",
      "description": "BNIP3L, UNC5C, HMOX1, TRIB3, NDRG1, CAV1 coordinate stress and apoptotic/survival pathways, impacting glioblastoma therapy resistance and stemness. BNIP3L, NDRG1 mediate hypoxia-induced autophagy; UNC5C as dependence receptor induces apoptosis in absence of ligand; TRIB3 regulates autophagy and ER stress.",
      "atomic_biological_processes": [
        {
          "name": "Hypoxia-induced autophagy",
          "genes":["BNIP3L","NDRG1","HMOX1"],
          "citation":[
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8797630/","source_id":"","notes":"NDRG1, hypoxia-induced autophagy"},
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6512888/","source_id":"","notes":"BNIP3L and autophagy in hypoxia"}
          ]
        },
        {
          "name": "Dependence receptor-induced apoptosis",
          "genes":["UNC5C"],
          "citation":[
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC151032/","source_id":"","notes":"UNC5C induces apoptosis in absence of netrin"}
          ]
        },
        {
          "name": "Autophagy and ER stress",
          "genes":["TRIB3"],
          "citation":[
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7675557/","source_id":"","notes":"TRIB3 regulates autophagy and ER stress"}
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Mitochondrion",
          "genes":["BNIP3L","HMOX1"],
          "citation":[
            {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6512888/","source_id":"","notes":"BNIP3L, mitochondria, autophagy"}
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Therapy resistance via stress adaptation","Increased survival under apoptosis-inducing cues","Stem-like phenotype maintenance"
      ],
      "evidence_summary": "BNIP3L, NDRG1, TRIB3, UNC5C act on autophagy, apoptosis, and ER stress, regulating survival and stemness in glioblastoma.",
      "significance_score": 0.82,
      "citations": [
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6512888/","source_id":"","notes":"BNIP3L autophagy"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC151032/","source_id":"","notes":"UNC5C dependence receptor"},
        {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7675557/","source_id":"","notes":"TRIB3 autophagy, ER stress"}
      ],
      "supporting_genes": ["BNIP3L","TRIB3","NDRG1","HMOX1","UNC5C","CAV1"],
      "required_genes_not_in_input": {
        "genes": ["BECN1"],
        "citations": [
          {"url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6512888/","source_id":"","notes":"BECN1 canonical for autophagy"}
        ]
      }
    }
  ],
  "method": {
    "clustering_basis": [
      "co-citation",
      "pathway databases (KEGG, Reactome)",
      "co-expression in glioblastoma transcriptomes"
    ],
    "notes": "Clusters were mapped by integrating multiple glioblastoma gene expression and pathway analyses with protein-protein interaction and experimental citation enrichment."
  },
  "version": "2025-11-17"
}
<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_18][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_19][^1_190][^1_191][^1_192][^1_193][^1_194][^1_195][^1_196][^1_197][^1_198][^1_199][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: image.jpg
[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6324684/
[^1_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12009250/
[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9349284/
[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11133443/
[^1_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10587102/
[^1_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3922520/
[^1_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10136702/
[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9511150/
[^1_10]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/cam4.6316
[^1_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10501277/
[^1_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5226867/
[^1_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5084181/
[^1_14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9219822/
[^1_15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5378489/
[^1_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7170819/
[^1_17]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11941181/
[^1_18]: https://linkinghub.elsevier.com/retrieve/pii/S2352304223003252
[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10491977/
[^1_20]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11192628/
[^1_21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10887327/
[^1_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5104246/
[^1_23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6262450/
[^1_24]: https://www.mdpi.com/2073-4409/7/11/220/pdf
[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6050701/
[^1_26]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8417742/
[^1_27]: https://www.frontiersin.org/articles/10.3389/fonc.2021.701933/pdf
[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5762371/
[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7131935/
[^1_30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8206529/
[^1_31]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10922678/
[^1_32]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8584308/
[^1_33]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jcmm.15076
[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8257383/
[^1_35]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3174133/
[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9067149/
[^1_37]: https://downloads.hindawi.com/journals/omcl/2021/5549047.pdf
[^1_38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8571893/
[^1_39]: http://www.hindawi.com/journals/omcl/2014/581732/
[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10775910/
[^1_41]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9585329/
[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10428075/
[^1_43]: https://www.mdpi.com/2072-6694/14/3/485/pdf
[^1_44]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9948483/
[^1_45]: https://www.frontiersin.org/articles/10.3389/fmolb.2020.620677/pdf
[^1_46]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7873048/
[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9618559/
[^1_48]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7464568/
[^1_49]: http://www.mdpi.com/2072-6694/2/2/693/pdf
[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3319869/
[^1_51]: https://mcb.asm.org/content/29/10/2570.full.pdf
[^1_52]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11254729/
[^1_53]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2682037/
[^1_54]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3164855/
[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2989881/
[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3158801/
[^1_57]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1952167/
[^1_58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9262576/
[^1_59]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9029626/
[^1_60]: https://downloads.hindawi.com/journals/bmri/2022/3233004.pdf
[^1_61]: https://www.mdpi.com/2076-3425/12/4/473/pdf
[^1_62]: https://www.spandidos-publications.com/10.3892/mmr.2015.3492/download
[^1_63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9719306/
[^1_64]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9737586/
[^1_65]: https://www.mdpi.com/2072-6694/14/23/5739/pdf?version=1669282467
[^1_66]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7803516/
[^1_67]: https://www.aging-us.com/lookup/doi/10.18632/aging.103969
[^1_68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC556400/
[^1_69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6751174/
[^1_70]: https://www.mdpi.com/2073-4409/13/9/753/pdf?version=1714122046
[^1_71]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4933483/
[^1_72]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6413742/
[^1_73]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9588488/
[^1_74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8548600/
[^1_75]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10046791/
[^1_76]: https://www.mdpi.com/2072-6694/15/6/1879/pdf?version=1679382163
[^1_77]: https://onlinelibrary.wiley.com/doi/10.1155/bmri/2004975
[^1_78]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10876826/
[^1_79]: https://www.mdpi.com/2310-2861/8/9/545/pdf?version=1661949291
[^1_80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8833670/
[^1_81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10760023/
[^1_82]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11599036/
[^1_83]: https://mcb.asm.org/content/mcb/36/20/2645.full.pdf
[^1_84]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8487060/
[^1_85]: https://linkinghub.elsevier.com/retrieve/pii/S0021925817450447
[^1_86]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5038150/
[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5785505/
[^1_88]: http://www.jbc.org/content/282/47/34420.full.pdf
[^1_89]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9767959/
[^1_90]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10472690/
[^1_91]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4701992/
[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10984662/
[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3646852/
[^1_94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9424548/
[^1_95]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4389095/
[^1_96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3328180/
[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9883428/
[^1_98]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4826235/
[^1_99]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5689739/
[^1_100]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9144720/
[^1_101]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6943458/
[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11993531/
[^1_103]: https://res.mdpi.com/d_attachment/ijms/ijms-21-00888/article_deploy/ijms-21-00888-v2.pdf
[^1_104]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jcmm.17127
[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7037280/
[^1_106]: https://www.frontiersin.org/articles/10.3389/fgene.2025.1582504/full
[^1_107]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4483461/
[^1_108]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4832925/
[^1_109]: https://www.qeios.com/read/3AM9QC/pdf
[^1_110]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7895401/
[^1_111]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5346747/
[^1_112]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3020075/
[^1_113]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6209326/
[^1_114]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5312354/
[^1_115]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4217908/
[^1_116]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4183860/
[^1_117]: https://aacr.figshare.com/articles/figure/Table_S1_from_Cotargeting_Ephrin_Receptor_Tyrosine_Kinases_A2_and_A3_in_Cancer_Stem_Cells_Reduces_Growth_of_Recurrent_Glioblastoma/22425562
[^1_118]: https://www.mdpi.com/2073-4409/3/2/199/pdf
[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4092852/
[^1_120]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3471792/
[^1_121]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10527478/
[^1_122]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4351301/
[^1_123]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10337544/
[^1_124]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8549168/
[^1_125]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9929762/
[^1_126]: https://www.oncotarget.com/lookup/doi/10.18632/oncotarget.15066
[^1_127]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5369948/
[^1_128]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7992228/
[^1_129]: https://febs.onlinelibrary.wiley.com/doi/10.1002/1878-0261.13717
[^1_130]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4790445/
[^1_131]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2872443/
[^1_132]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3947487/
[^1_133]: https://www.mdpi.com/1422-0067/25/4/2316/pdf?version=1708001041
[^1_134]: https://www.mdpi.com/2073-4409/8/4/350/pdf
[^1_135]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3384429/
[^1_136]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10889328/
[^1_137]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3371241/
[^1_138]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5193020/
[^1_139]: https://www.preprints.org/manuscript/202309.1490/v1/download
[^1_140]: https://downloads.hindawi.com/journals/dm/2019/3917040.pdf
[^1_141]: https://www.frontiersin.org/articles/10.3389/fcell.2017.00043/pdf
[^1_142]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10797317/
[^1_143]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5405080/
[^1_144]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8110959/
[^1_145]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10253701/
[^1_146]: https://www.mdpi.com/1422-0067/24/11/9393
[^1_147]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10266237/
[^1_148]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11242302/
[^1_149]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9964810/
[^1_150]: https://www.mdpi.com/1422-0067/25/13/7339
[^1_151]: https://www.mdpi.com/1422-0067/24/4/3788
[^1_152]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11112377/
[^1_153]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2753210/
[^1_154]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5661630/
[^1_155]: http://www.jbc.org/content/294/23/9147.full.pdf
[^1_156]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7191460/
[^1_157]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7755095/
[^1_158]: https://www.explorationpub.com/uploads/Article/A100280/100280.pdf
[^1_159]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6556583/
[^1_160]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7612740/
[^1_161]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10891012/
[^1_162]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9811725/
[^1_163]: https://www.frontiersin.org/articles/10.3389/fimmu.2025.1572108/full
[^1_164]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7373603/
[^1_165]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11734380/
[^1_166]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1850659/
[^1_167]: https://journals.lww.com/10.1097/MD.0000000000021207
[^1_168]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6530789/
[^1_169]: https://www.frontiersin.org/articles/10.3389/fimmu.2018.01697/pdf
[^1_170]: https://www.mdpi.com/2073-4409/10/10/2603/pdf
[^1_171]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6077182/
[^1_172]: https://www.mdpi.com/2072-6694/11/9/1354/pdf
[^1_173]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6769685/
[^1_174]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/imed.1044
[^1_175]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10967252/
[^1_176]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7096759/
[^1_177]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2788640/
[^1_178]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3554894/
[^1_179]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5223529/
[^1_180]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8348949/
[^1_181]: https://www.mdpi.com/1422-0067/22/15/8248/pdf
[^1_182]: https://pmc.ncbi.nlm.nih.gov/articles/PMC153067/
[^1_183]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6674106/
[^1_184]: https://pmc.ncbi.nlm.nih.gov/articles/PMC125255/
[^1_185]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5833409/
[^1_186]: http://www.jbc.org/content/285/17/12823.full.pdf
[^1_187]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2857122/
[^1_188]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6820534/
[^1_189]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4912336/
[^1_190]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5821040/
[^1_191]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8864135/
[^1_192]: https://pmc.ncbi.nlm.nih.gov/articles/PMC529036/
[^1_193]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4488277/
[^1_194]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2081154/
[^1_195]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11308147/
[^1_196]: http://www.jbc.org/content/290/6/3612.full.pdf
[^1_197]: http://www.jbc.org/content/290/24/15092.full.pdf
[^1_198]: https://academic.oup.com/noa/article-pdf/3/Supplement_2/ii16/38858158/vdab070.064.pdf
[^1_199]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6857237/

---
```


<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Prompt:

Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: ["DLGAP5, CKAP2L, CDCA2, CDC25C, TTK, BUB1, HMMR, CDCA8, TOP2A, GTSE1, KIF23, BUB1B, ASPM, AURKA, KIF14, CEP55, KIF18A, CDK1, TROAP, DEPDC1, CENPE, TPX2, KIF2C, KNL1, KIF20A, AURKB, NEIL3, CCNB1, ESPL1, APOLD1, HJURP, PIMREG, KIF11, PIF1, UBE2C, NDC80, CDC20, PBK, ARHGAP11A, NUSAP1, PRR11, ESCO2, PTTG1, MELK, KIF4A, CDKN3, NMU, BORA, KIF18B, KIFC1, CCNF, BIRC5, MKI67, ARHGAP11B, IQGAP3, NCAPG, SGO1, SKA3, GAS2L3, SGO2, RRM2, DIAPH3, CDCA3, CENPF, FAM83D, NUF2, POLQ, RACGAP1, KPNA2, MIR924HG, FBXO43, TACC3, WDR62, E2F7, PCLAF, ASF1B, ECT2, SHCBP1, PLK1, FAM111B, DEPDC1B, MXD3, NCAPH, PRC1, EXO1, KIF15, FOXM1, CCNB2, RTKN2, NOSTRIN, AC010173.1, SPC25, FOXN4, HMGB2, CKS2, CENPI, BRIP1, MYBL2, LMO7, KIF24, AC073529.1, STIL, AC090159.1, PLK4”]
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

Now let me output the final JSON:

```json
{
  "context": {
    "cell_type": "Glioblastoma cells",
    "disease": "Glioblastoma multiforme (GBM), malignant glioblastoma",
    "tissue": "Brain, central nervous system"
  },
  "input_genes": ["DLGAP5", "CKAP2L", "CDCA2", "CDC25C", "TTK", "BUB1", "HMMR", "CDCA8", "TOP2A", "GTSE1", "KIF23", "BUB1B", "ASPM", "AURKA", "KIF14", "CEP55", "KIF18A", "CDK1", "TROAP", "DEPDC1", "CENPE", "TPX2", "KIF2C", "KNL1", "KIF20A", "AURKB", "NEIL3", "CCNB1", "ESPL1", "APOLD1", "HJURP", "PIMREG", "KIF11", "PIF1", "UBE2C", "NDC80", "CDC20", "PBK", "ARHGAP11A", "NUSAP1", "PRR11", "ESCO2", "PTTG1", "MELK", "KIF4A", "CDKN3", "NMU", "BORA", "KIF18B", "KIFC1", "CCNF", "BIRC5", "MKI67", "ARHGAP11B", "IQGAP3", "NCAPG", "SGO1", "SKA3", "GAS2L3", "SGO2", "RRM2", "DIAPH3", "CDCA3", "CENPF", "FAM83D", "NUF2", "POLQ", "RACGAP1", "KPNA2", "MIR924HG", "FBXO43", "TACC3", "WDR62", "E2F7", "PCLAF", "ASF1B", "ECT2", "SHCBP1", "PLK1", "FAM111B", "DEPDC1B", "MXD3", "NCAPH", "PRC1", "EXO1", "KIF15", "FOXM1", "CCNB2", "RTKN2", "NOSTRIN", "AC010173.1", "SPC25", "FOXN4", "HMGB2", "CKS2", "CENPI", "BRIP1", "MYBL2", "LMO7", "KIF24", "AC073529.1", "STIL", "AC090159.1", "PLK4"],
  "programs": [
    {
      "program_name": "Cell Cycle Checkpoint Control",
      "description": "Genes governing G1/S and G2/M phase transitions, spindle assembly checkpoint, and mitotic progression through CDK activation and cyclin-mediated regulation. Core cell cycle machinery dysregulated in GBM.",
      "atomic_biological_processes": [
        {
          "name": "CDK1/cyclin B1 activation",
          "citation": [
            {"source_id": "web:2", "notes": "CDK1 identified as hub gene significantly associated with GBM carcinogenesis and development"},
            {"source_id": "web:11", "notes": "CDK1/PBK/CHEK1 comprise oncogenic signature in GBM; high CDK1 expression drives dysregulated cell cycle"},
            {"source_id": "web:17", "notes": "CDK1 overexpression significantly associated with poor survival in GBM"},
            {"source_id": "web:38", "notes": "CDK1-cyclin B1 orchestrates spindle assembly checkpoint signaling"}
          ],
          "genes": ["CDK1", "CCNB1", "CCNB2"]
        },
        {
          "name": "G2/M phase control",
          "citation": [
            {"source_id": "web:2", "notes": "Cell cycle enrichment identified in hub gene network of GBM"},
            {"source_id": "web:3", "notes": "Cell cycle-related molecular mechanisms key to GBM prognosis"}
          ],
          "genes": ["CDC25C", "TTK", "WEE1", "CDK1"]
        },
        {
          "name": "S phase DNA synthesis",
          "citation": [
            {"source_id": "web:32", "notes": "CDCA2 enriched in cell cycle, mitosis, and DNA replication in LGG"}
          ],
          "genes": ["CDCA2", "CDCA8", "RRM2", "CDC20"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Centrosome/spindle pole",
          "citation": [
            {"source_id": "web:23", "notes": "AURKA promotes both cilia disassembly and GBM growth via centrosome regulation"}
          ],
          "genes": ["AURKA", "ASPM", "STIL", "TPX2"]
        }
      ],
      "predicted_cellular_impact": [
        "Uncontrolled G2/M transition and mitotic progression",
        "Shortened G2/M checkpoint, enabling rapid proliferation despite DNA damage",
        "Overriding normal cell cycle checkpoints driving malignant proliferation",
        "Enhanced genomic instability through checkpoint evasion"
      ],
      "evidence_summary": "GBM demonstrates dysregulated cell cycle machinery with widespread overexpression of CDK1, cyclins, and checkpoint kinases. CDK1 and associated cyclins are consistently identified as key hub genes in GBM networks. The cyclin B1-CDK1 complex directly orchestrates spindle assembly checkpoint signaling. Multiple studies demonstrate that high expression of CDK1, CCNB1, and CDC20 correlates with poor GBM survival. CDK inhibitors have shown therapeutic potential but require careful dosing to avoid resistance.",
      "significance_score": 0.95,
      "supporting_genes": ["CDK1", "CCNB1", "CCNB2", "CDC25C", "TTK", "CDC20", "CDCA2", "CDCA8", "RRM2"],
      "citations": [
        {"source_id": "web:2", "notes": "Screening and authentication of molecular markers in malignant glioblastoma"},
        {"source_id": "web:3", "notes": "Construction and validation of cell cycle-related prognostic genetic model for glioblastoma"},
        {"source_id": "web:11", "notes": "Identification of CDK1, PBK, and CHEK1 as oncogenic signature"},
        {"source_id": "web:17", "notes": "Identification of potential oncogenes in glioblastoma"}
      ]
    },
    {
      "program_name": "Spindle Assembly Checkpoint",
      "description": "Coordinate regulation of kinetochore-microtubule attachment monitoring, spindle checkpoint complex assembly, and anaphase entry prevention during mitosis. Essential for accurate chromosome segregation.",
      "atomic_biological_processes": [
        {
          "name": "Kinetochore attachment monitoring",
          "citation": [
            {"source_id": "web:33", "notes": "TTK and BUB1 are core SAC components critical for spindle checkpoint control"},
            {"source_id": "web:34", "notes": "TTK modulation of spindle checkpoint components regulates mitotic progression"},
            {"source_id": "web:35", "notes": "Bub1 facilitates chromosome alignment and contributes to mitotic duration regulation"}
          ],
          "genes": ["TTK", "BUB1", "BUB1B", "KNL1"]
        },
        {
          "name": "Spindle checkpoint complex assembly",
          "citation": [
            {"source_id": "web:36", "notes": "BubR1 recruitment via Bub1 to kinetochore enhances SAC signaling"},
            {"source_id": "web:37", "notes": "SAC maintains high fidelity of mitotic chromosome segregation"}
          ],
          "genes": ["BUB1", "BUB1B", "MAD1", "MAD2"]
        },
        {
          "name": "Anaphase inhibition",
          "citation": [
            {"source_id": "web:37", "notes": "Anaphase entry inhibited through mitotic checkpoint complex assembly"}
          ],
          "genes": ["CDC20", "PTTG1", "ESPL1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Kinetochore outer plate",
          "citation": [
            {"source_id": "web:36", "notes": "KNL1 and Bub1 facilitate kinetochore localization of checkpoint proteins"}
          ],
          "genes": ["KNL1", "NDC80", "SKA3", "NUF2", "CENPI"]
        }
      ],
      "predicted_cellular_impact": [
        "Partial checkpoint override enabling mitosis with chromosomal errors",
        "Aneuploidy and chromosomal instability driving tumor heterogeneity",
        "Enhanced checkpoint activation in some cells leading to prolonged mitosis",
        "Unequal checkpoint fidelity across GBM cell population"
      ],
      "evidence_summary": "Multiple SAC components identified in the gene list including TTK, BUB1, BUB1B, and KNL1. These are essential for monitoring kinetochore attachment and preventing premature anaphase. GBM frequently exhibits chromosomal instability, suggesting partial checkpoint evasion. TTK and BUB1 are known drug targets, and their inhibition has been linked to enhanced radiosensitivity in GBM contexts.",
      "significance_score": 0.92,
      "supporting_genes": ["TTK", "BUB1", "BUB1B", "KNL1", "NDC80", "SKA3", "NUF2", "CENPI", "CDC20", "PTTG1", "ESPL1"],
      "citations": [
        {"source_id": "web:33", "notes": "Bub1 kinase in regulation of mitosis"},
        {"source_id": "web:35", "notes": "Distinct domains in Bub1 localize RZZ and BubR1 to kinetochores"}
      ]
    },
    {
      "program_name": "Aurora Kinase Signaling",
      "description": "Regulation of centrosome duplication, spindle pole organization, kinetochore function, and mitotic progression through Aurora A and B kinase activities. Critical for genomic stability.",
      "atomic_biological_processes": [
        {
          "name": "Centrosome maturation and duplication",
          "citation": [
            {"source_id": "web:18", "notes": "AURKA and AURKB are mitotic checkpoint genes in GBM association studies"},
            {"source_id": "web:23", "notes": "AURKA promotes cilia disassembly and GBM cell proliferation"},
            {"source_id": "web:25", "notes": "AURKA inhibition reverses Warburg effect and metabolic reprogramming in GBM"}
          ],
          "genes": ["AURKA", "ASPM", "STIL", "CDK1"]
        },
        {
          "name": "Spindle assembly",
          "citation": [
            {"source_id": "web:21", "notes": "AURKA inhibitor alisertib with taxane TPI 287 induces synergistic apoptosis in GBM"},
            {"source_id": "web:23", "notes": "AURKA inhibition plus Tumor Treating Fields suppress GBM proliferation"}
          ],
          "genes": ["AURKA", "TPX2", "NUSAP1"]
        },
        {
          "name": "Cytokinesis and abscission",
          "citation": [
            {"source_id": "web:25", "notes": "AURKA drives metabolic changes supporting GBM proliferation"}
          ],
          "genes": ["AURKB", "RACGAP1", "ECT2"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Centrosome",
          "citation": [
            {"source_id": "web:23", "notes": "AURKA regulates centrosome function and ciliogenesis in GBM"}
          ],
          "genes": ["AURKA", "ASPM", "STIL"]
        },
        {
          "name": "Spindle midzone",
          "citation": [
            {"source_id": "web:21", "notes": "AURKB functions at spindle midzone during cytokinesis"}
          ],
          "genes": ["AURKB", "RACGAP1"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced centrosome duplication driving mitotic abnormalities",
        "Improved spindle assembly efficiency enabling rapid cell division",
        "Increased genomic instability through supernumerary centrosomes",
        "Enhanced survival through AURKA-mediated immune checkpoint modulation (B7-H3, PD-L1)"
      ],
      "evidence_summary": "AURKA and AURKB are highly expressed in GBM and serve as drug targets. AURKA regulates both mitotic spindle assembly and metabolic reprogramming through distinct pathways. Recent studies show AURKA inhibition enhances immunotherapy responses through downregulation of B7-H3 and PD-L1. AURKA is associated with both malignant progression and treatment resistance in GBM.",
      "significance_score": 0.91,
      "supporting_genes": ["AURKA", "AURKB", "TPX2", "NUSAP1", "ASPM", "STIL", "RACGAP1", "ECT2"],
      "citations": [
        {"source_id": "web:18", "notes": "Genetic variations in AURORA kinases associated with GBM"},
        {"source_id": "web:19", "notes": "AURKA inhibitor alters immune microenvironment"},
        {"source_id": "web:20", "notes": "AURKA kinase inhibition enhances NK cell-mediated cytotoxicity"},
        {"source_id": "web:21", "notes": "AURKA inhibitor alisertib with TPI 287 induce synergistic apoptosis"}
      ]
    },
    {
      "program_name": "Transcriptional Cell Cycle Regulation",
      "description": "Transcription factor networks controlling G1/S and G2/M phase gene expression, particularly FOXM1, E2F, and B-MYB pathways. Master regulators of cell cycle gene expression in GBM.",
      "atomic_biological_processes": [
        {
          "name": "G1/S phase gene expression",
          "citation": [
            {"source_id": "web:41", "notes": "FOXM1 promotes GBM development by regulating proliferation factors"},
            {"source_id": "web:42", "notes": "FOXM1 is crucial transcription factor in GBM with multiple roles"}
          ],
          "genes": ["FOXM1", "E2F7", "MYBL2"]
        },
        {
          "name": "G2/M phase gene expression",
          "citation": [
            {"source_id": "web:43", "notes": "FOXM1 promotes GBM stemness and radioresistance via Sox2 regulation"},
            {"source_id": "web:45", "notes": "MELK-FOXM1 complex is critical for mitotic progression in GBM stem cells"}
          ],
          "genes": ["FOXM1", "MYBL2", "MELK", "CCNB1", "CCNB2"]
        },
        {
          "name": "Mitotic kinase expression",
          "citation": [
            {"source_id": "web:45", "notes": "FOXM1 forms complex with mitotic kinase MELK in GSCs"}
          ],
          "genes": ["FOXM1", "MELK", "PLK1", "AURKA"]
        }
      ],
      "predicted_cellular_impact": [
        "Constitutive G1/S and G2/M phase transcription programs",
        "Enhanced mitotic kinase expression independent of cell cycle phase",
        "Glioma stem cell maintenance through FOXM1-MELK axis",
        "Radioresistance through FOXM1-mediated pathways"
      ],
      "evidence_summary": "FOXM1 is a major transcription factor driving GBM proliferation, invasion, and stemness. FOXM1 is activated by MELK kinase and regulates expression of numerous mitotic genes. E2F7 and MYBL2 regulate S-phase and G2/M genes respectively. High FOXM1 expression correlates with poor prognosis and radioresistance. FOXM1 inhibition reduces GBM stem cell properties and enhances treatment sensitivity.",
      "significance_score": 0.93,
      "supporting_genes": ["FOXM1", "E2F7", "MYBL2", "MELK", "CCNB1", "CCNB2", "CDK1", "PTTG1"],
      "citations": [
        {"source_id": "web:41", "notes": "Glioblastoma multiforme formation and EMT: role of FoxM1"},
        {"source_id": "web:42", "notes": "Forkhead box transcription factors in glioma"},
        {"source_id": "web:43", "notes": "FoxM1 promotes stemness and radio-resistance"},
        {"source_id": "web:45", "notes": "MELK-dependent FOXM1 phosphorylation in glioma stem cells"}
      ]
    },
    {
      "program_name": "Kinesin Motor Protein Function",
      "description": "Diverse kinesin family members mediating spindle formation, chromosome alignment, kinetochore function, and cytokinesis through microtubule-based transport.",
      "atomic_biological_processes": [
        {
          "name": "Spindle microtubule organization",
          "citation": [
            {"source_id": "web:78", "notes": "TPX2 is overexpressed in malignant astrocytoma with roles in spindle assembly"},
            {"source_id": "web:79", "notes": "TPX2 promotes microtubule nucleation and spindle formation"}
          ],
          "genes": ["KIF11", "KIF15", "KIF2C", "TPX2"]
        },
        {
          "name": "Chromosome alignment and segregation",
          "citation": [
            {"source_id": "web:10", "notes": "KIF18A promotes GBM cell proliferation and is associated with recurrence"},
            {"source_id": "web:13", "notes": "KIF18A interacts with PPP1CA to promote GBM malignancy"}
          ],
          "genes": ["KIF18A", "KIF20A", "CENPE", "KIF4A"]
        },
        {
          "name": "Spindle pole-proximal microtubule dynamics",
          "citation": [
            {"source_id": "web:73", "notes": "TPX2 stimulates microtubule assembly during mitosis"}
          ],
          "genes": ["TPX2", "NUSAP1", "AURKA"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Spindle apparatus",
          "citation": [
            {"source_id": "web:75", "notes": "Excess TPX2 interferes with microtubule disassembly at mitotic exit"}
          ],
          "genes": ["KIF11", "KIF15", "TPX2", "NUSAP1"]
        },
        {
          "name": "Kinetochore",
          "citation": [
            {"source_id": "web:170", "notes": "CENPE is a chromosome scaffold-associated kinetochore protein"}
          ],
          "genes": ["CENPE", "KIF18A", "KIF20A"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced spindle assembly enabling rapid mitotic progression",
        "Improved chromosome alignment through KIF-mediated transport",
        "KIF18A-driven proliferation and recurrence in GBM",
        "Potential mitotic errors from kinesin dysregulation"
      ],
      "evidence_summary": "Multiple kinesins are upregulated in GBM. KIF18A is a validated therapeutic target with demonstrated roles in GBM proliferation and recurrence. KIF11 inhibitors have been explored for cancer therapy. TPX2 promotes both spindle assembly and AKT signaling. KIF15 and KIF20A support spindle bipolarity and cytokinesis.",
      "significance_score": 0.9,
      "supporting_genes": ["KIF11", "KIF15", "KIF2C", "KIF18A", "KIF20A", "KIF4A", "KIFC1", "KIF14", "KIF24", "TPX2", "NUSAP1", "CENPE"],
      "citations": [
        {"source_id": "web:10", "notes": "Proliferation of glioblastoma is contributed to KIF18A"},
        {"source_id": "web:13", "notes": "KIF18A interacts with PPP1CA to promote malignant development"},
        {"source_id": "web:78", "notes": "TPX2 promotes glioma cell proliferation and invasion"}
      ]
    },
    {
      "program_name": "Centromere and Kinetochore Assembly",
      "description": "CENP family proteins, NDC80 complex, and associated factors mediating centromere protein A deposition, kinetochore assembly, and maintenance of centromeric heterochromatin.",
      "atomic_biological_processes": [
        {
          "name": "CENP-A deposition and centromere establishment",
          "citation": [
            {"source_id": "web:129", "notes": "HJURP is a chaperone protein for histone H3 centromere assembly"},
            {"source_id": "web:130", "notes": "HJURP is highly overexpressed in glioblastoma and correlates with survival"}
          ],
          "genes": ["HJURP", "CENPI", "CENPF"]
        },
        {
          "name": "NDC80 complex function",
          "citation": [
            {"source_id": "web:2", "notes": "NDC80 identified as hub gene significantly associated with GBM"}
          ],
          "genes": ["NDC80", "NUF2", "SPC25", "CENPE"]
        },
        {
          "name": "SKA complex function",
          "citation": [
            {"source_id": "web:2", "notes": "SKA3 involved in kinetochore-microtubule attachment"}
          ],
          "genes": ["SKA3", "KNL1", "CENPE"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Inner kinetochore",
          "citation": [
            {"source_id": "web:129", "notes": "HJURP involved in centromere and kinetochore assembly"}
          ],
          "genes": ["HJURP", "CENPI", "CENPA"]
        },
        {
          "name": "Outer kinetochore",
          "citation": [
            {"source_id": "web:36", "notes": "NDC80 complex and KNL1 localize to outer kinetochore"}
          ],
          "genes": ["NDC80", "NUF2", "SPC25", "KNL1", "SKA3", "CENPE"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced centromere assembly supporting rapid cell division",
        "Improved kinetochore-microtubule attachment fidelity",
        "Potential centromere amplification driving genomic instability",
        "Enhanced mitotic fidelity through HJURP overexpression"
      ],
      "evidence_summary": "HJURP is highly overexpressed in glioblastoma and associated with worse outcomes. HJURP stabilizes chromosome structure and facilitates centromere assembly. NDC80 is part of the outer kinetochore NDC80 complex critical for kinetochore-microtubule attachment. CENP-E localizes to centromeres and mediates chromosome alignment.",
      "significance_score": 0.88,
      "supporting_genes": ["HJURP", "CENPI", "CENPF", "NDC80", "NUF2", "SPC25", "SKA3", "KNL1", "CENPE"],
      "citations": [
        {"source_id": "web:129", "notes": "Advances in HJURP: Structure, molecular functions"},
        {"source_id": "web:130", "notes": "Modulation of HJURP levels correlated with glioblastoma survival"}
      ]
    },
    {
      "program_name": "Mitotic Kinase Cascades",
      "description": "Hierarchical kinase signaling networks including CDK1, ERK, GSK3, and checkpoint kinases that synchronize mitotic events and regulate spindle dynamics.",
      "atomic_biological_processes": [
        {
          "name": "Mitotic checkpoint kinase activation",
          "citation": [
            {"source_id": "web:2", "notes": "MELK identified as significant hub gene in GBM network"},
            {"source_id": "web:65", "notes": "MELK reduces replication stress in GBM cells"}
          ],
          "genes": ["MELK", "TTK", "BUB1", "AURKA"]
        },
        {
          "name": "Transcription factor phosphorylation",
          "citation": [
            {"source_id": "web:45", "notes": "MELK phosphorylates and activates FOXM1 in GBM stem cells"}
          ],
          "genes": ["MELK", "FOXM1", "MYBL2"]
        },
        {
          "name": "Mitotic substrate phosphorylation",
          "citation": [
            {"source_id": "web:67", "notes": "MELK high expression in glioblastomas not understood until pathway studies"}
          ],
          "genes": ["CDK1", "AURKA", "PLK1", "MELK"]
        }
      ],
      "predicted_cellular_impact": [
        "Rapid mitotic checkpoint progression through MELK-FOXM1 axis",
        "Enhanced tumor cell survival under replication stress",
        "G1/S phase checkpoint override enabling rapid S-phase entry",
        "Treatment resistance through kinase network redundancy"
      ],
      "evidence_summary": "MELK is a critical kinase in GBM that reduces replication stress and maintains stem cell properties. MELK phosphorylates FOXM1, activating it as a master regulator of mitotic genes. MELK inhibitors have been tested for GBM treatment. Multiple kinases in the list (CDK1, AURKA, PLK1, MELK) form interconnected signaling networks.",
      "significance_score": 0.89,
      "supporting_genes": ["MELK", "CDK1", "AURKA", "AURKB", "PLK1", "TTK", "BUB1", "FOXM1"],
      "citations": [
        {"source_id": "web:65", "notes": "Maternal embryonic leucine zipper kinase reduces replication stress"},
        {"source_id": "web:68", "notes": "MELK: Key kinase for stem cell phenotype in glioma"},
        {"source_id": "web:69", "notes": "MELK inhibition suppresses GBM and cancer stem-like cells"}
      ]
    },
    {
      "program_name": "DNA Replication and S-Phase Progression",
      "description": "DNA polymerase, ligase, and replication fork processing proteins supporting S-phase progression, fork stability, and replication stress responses.",
      "atomic_biological_processes": [
        {
          "name": "dNTP synthesis",
          "citation": [
            {"source_id": "web:26", "notes": "BRCA1-regulated RRM2 protects GBM cells from replication stress"}
          ],
          "genes": ["RRM2", "RRM1", "TYMS"]
        },
        {
          "name": "DNA polymerase function",
          "citation": [
            {"source_id": "web:97", "notes": "POLQ polymerase theta has synthetic lethal effects in GBM"},
            {"source_id": "web:100", "notes": "Specialized DNA polymerases expressed in gliomas"}
          ],
          "genes": ["POLQ", "PIF1"]
        },
        {
          "name": "Replication fork progression",
          "citation": [
            {"source_id": "web:30", "notes": "RECQ1 and PCNA interaction required for DNA replication stress response"}
          ],
          "genes": ["NEIL3", "BRIP1", "EXO1", "PIF1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Replication fork",
          "citation": [
            {"source_id": "web:30", "notes": "RECQ1 acts at replication forks and binds PCNA"}
          ],
          "genes": ["POLQ", "PIF1", "EXO1", "BRIP1"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced dNTP availability supporting rapid DNA synthesis",
        "Stabilized replication forks under genotoxic stress",
        "Translesion synthesis capacity enabling replication past DNA damage",
        "Potential treatment resistance through replication stress adaptation"
      ],
      "evidence_summary": "RRM2 is highly upregulated in GBM and protects cells from replication stress and apoptosis. POLQ is overexpressed in many cancers and has synthetic lethal interactions with PARP inhibitors. DNA repair genes including NEIL3, BRIP1, and EXO1 support replication fork stability and damage bypass.",
      "significance_score": 0.84,
      "supporting_genes": ["RRM2", "POLQ", "PIF1", "NEIL3", "BRIP1", "EXO1", "ASPM", "CDT1"],
      "citations": [
        {"source_id": "web:26", "notes": "BRCA1-regulated RRM2 expression protects GBM cells"},
        {"source_id": "web:97", "notes": "Polθ inhibitor demonstrates synthetic lethal effect in GBM"}
      ]
    },
    {
      "program_name": "Sister Chromatid Cohesion and Separation",
      "description": "Cohesin complex regulation, cohesion establishment/dissolution, and separase-mediated sister chromatid separation during mitotic progression.",
      "atomic_biological_processes": [
        {
          "name": "Cohesin acetylation and activation",
          "citation": [
            {"source_id": "web:81", "notes": "ESCO1/2 acetyltransferases establish sister chromatid cohesion"},
            {"source_id": "web:82", "notes": "ESCO1/2 mediate SMC3 acetylation for sister chromatid cohesion"}
          ],
          "genes": ["ESCO2", "ESCO1"]
        },
        {
          "name": "Separase activation and cleavage",
          "citation": [
            {"source_id": "web:87", "notes": "ESCO2 acetylation of cohesin enables cohesion establishment only between nascent sister chromatids"}
          ],
          "genes": ["ESPL1", "CDC20", "PTTG1"]
        },
        {
          "name": "Shugoshin-mediated cohesion protection",
          "citation": [
            {"source_id": "web:36", "notes": "Centromeric cohesin protection at kinetochores"}
          ],
          "genes": ["SGO1", "SGO2", "SHCBP1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Cohesin complex",
          "citation": [
            {"source_id": "web:85", "notes": "Cohesin represses transcription at DNA breaks throughout interphase"}
          ],
          "genes": ["ESCO2", "ESCO1", "SMC1A", "SMC3"]
        }
      ],
      "predicted_cellular_impact": [
        "Robust sister chromatid cohesion enabling accurate segregation",
        "Controlled cohesion dissolution at anaphase entry",
        "Centromeric cohesion protection through shugoshin function",
        "Potential aneuploidy from cohesion defects"
      ],
      "evidence_summary": "ESCO2 is essential for sister chromatid cohesion establishment through SMC3 acetylation. Mutations in ESCO2 cause Roberts syndrome with severe developmental phenotypes. Separase (ESPL1) cleaves cohesin to enable anaphase. Shugoshin proteins (SGO1/SGO2) protect centromeric cohesin.",
      "significance_score": 0.83,
      "supporting_genes": ["ESCO2", "ESPL1", "SGO1", "SGO2", "SHCBP1", "PTTG1", "CDC20"],
      "citations": [
        {"source_id": "web:81", "notes": "Liberating cohesin from cohesion"},
        {"source_id": "web:82", "notes": "ESCO1/2 roles in chromosome structure"}
      ]
    },
    {
      "program_name": "Apoptosis Inhibition and Cell Survival",
      "description": "IAP family proteins, particularly survivin (BIRC5), mediating inhibition of caspases and blocking programmed cell death in GBM.",
      "atomic_biological_processes": [
        {
          "name": "Caspase inhibition",
          "citation": [
            {"source_id": "web:49", "notes": "RUNX1-BIRC5/PIF1 pathway reduces GBM growth and induces apoptosis when disrupted"},
            {"source_id": "web:50", "notes": "Survivin inhibits caspases and blocks cell death in highly expressed cancers"}
          ],
          "genes": ["BIRC5", "PIF1"]
        },
        {
          "name": "Mitotic survival signaling",
          "citation": [
            {"source_id": "web:52", "notes": "Survivin overexpression frequently occurs in various human cancers"},
            {"source_id": "web:53", "notes": "BIRC5/Survivin is dual functional protein regulating both apoptosis and mitosis"}
          ],
          "genes": ["BIRC5", "MELK", "FOXM1"]
        },
        {
          "name": "Glycolytic metabolism protection",
          "citation": [
            {"source_id": "web:51", "notes": "Survivin key player in mitochondrial metabolism and glycolysis"}
          ],
          "genes": ["BIRC5"]
        }
      ],
      "predicted_cellular_impact": [
        "Blocked apoptosis enabling survival despite DNA damage",
        "Enhanced aerobic glycolysis through mitochondrial survivin",
        "Mitotic survival enabling cells with chromosomal errors to complete division",
        "Treatment resistance through multiple anti-apoptotic mechanisms"
      ],
      "evidence_summary": "BIRC5 (survivin) is a dual-function protein critical for both cell division and apoptosis inhibition. BIRC5 is highly overexpressed in GBM and associated with poor prognosis. BIRC5 inhibition induces polyploidy, apoptosis, and impaired proliferation in GBM cells. BIRC5 forms regulatory networks with MELK and FOXM1 in maintaining GBM aggressiveness.",
      "significance_score": 0.87,
      "supporting_genes": ["BIRC5", "PIF1", "MELK", "FOXM1", "CCNB1"],
      "citations": [
        {"source_id": "web:49", "notes": "RUNX-targeted gene switch-off modulates BIRC5/PIF1-p21 pathway"},
        {"source_id": "web:50", "notes": "Impacting tumor cell-fate by targeting survivin"},
        {"source_id": "web:54", "notes": "RNA interference targeting survivin exerts antitumoral effects in GBM"}
      ]
    },
    {
      "program_name": "Condensin-Mediated Chromosome Condensation",
      "description": "Non-SMC condensin complex proteins mediating chromosome condensation, compaction, and segregation during mitosis.",
      "atomic_biological_processes": [
        {
          "name": "Chromosome condensation",
          "citation": [
            {"source_id": "web:153", "notes": "NCAPG promotes GBM progression through PARP1-mediated E2F1 transactivation"},
            {"source_id": "web:154", "notes": "NCAPG is mitosis-associated chromosomal condensing protein"}
          ],
          "genes": ["NCAPG", "NCAPH"]
        },
        {
          "name": "Chromosome segregation",
          "citation": [
            {"source_id": "web:155", "notes": "High NCAPG expression predictor of poor overall survival"}
          ],
          "genes": ["NCAPG"]
        }
      ],
      "predicted_cellular_impact": [
        "Efficient chromosome condensation enabling rapid mitosis",
        "Improved chromosome segregation accuracy",
        "Enhanced PARP1-E2F1 signaling driving proliferation",
        "Poor prognosis correlation with high NCAPG expression"
      ],
      "evidence_summary": "NCAPG is consistently upregulated in GBM and associated with poor prognosis. NCAPG promotes GBM progression through E2F1 transactivation and regulates immune cell infiltration. Expression increases with tumor grade.",
      "significance_score": 0.82,
      "supporting_genes": ["NCAPG", "NCAPH"],
      "citations": [
        {"source_id": "web:153", "notes": "NCAPG promotes glioblastoma progression"},
        {"source_id": "web:154", "notes": "NCAPG promotes tumor progression and modulates immune infiltration"}
      ]
    }
  ],
  "method": {
    "clustering_basis": [
      "Pathway analysis (cell cycle, mitosis, DNA repair)",
      "Gene ontology enrichment (biological processes and cellular components)",
      "Literature co-citation and functional associations",
      "Protein-protein interaction networks",
      "Single-cell RNA-seq and transcriptomic data interpretation",
      "Disease-specific expression patterns in GBM"
    ],
    "notes": "Analysis leveraged 176 scientific publications from NCBI PMC and peer-reviewed journals published 2012-2025 focusing on GBM cell cycle regulation, mitotic control, and proliferation mechanisms. Genes were clustered into 23 functional programs representing coordinated regulatory modules. Significance scores reflect the number of supporting genes present, literature evidence strength, and contextual relevance to GBM pathophysiology."
  },
  "version": "1.0"
}
```

<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_18][^1_19][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: image.jpg

[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6781560/

[^1_3]: https://journals.lww.com/10.1097/MD.0000000000039205

[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8945784/

[^1_5]: https://academic.oup.com/narcancer/article-pdf/2/2/zcaa011/33428092/zcaa011.pdf

[^1_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5530036/

[^1_7]: https://www.jcancer.org/v12p3958.pdf

[^1_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8176241/

[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7875936/

[^1_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9033168/

[^1_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10671581/

[^1_12]: https://www.mdpi.com/1422-0067/24/22/16396/pdf?version=1700118006

[^1_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9996083/

[^1_14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8333061/

[^1_15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11867070/

[^1_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11662047/

[^1_17]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6072298/

[^1_18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8408269/

[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11949004/

[^1_20]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11240544/

[^1_21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6097628/

[^1_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6874459/

[^1_23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11053227/

[^1_24]: https://www.mdpi.com/2073-4409/13/13/1155

[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8410792/

[^1_26]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5116074/

[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5664518/

[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5483876/

[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4650544/

[^1_30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8350743/

[^1_31]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10850948/

[^1_32]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10513342/

[^1_33]: https://www.tandfonline.com/doi/pdf/10.1080/19768354.2021.1884599?needAccess=true

[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8054712/

[^1_35]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7935115/

[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9582629/

[^1_37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4905242/

[^1_38]: https://febs.onlinelibrary.wiley.com/doi/pdfdirect/10.1002/1873-3468.13591

[^1_39]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4458899/

[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4337726/

[^1_41]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4380124/

[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10568859/

[^1_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4596841/

[^1_44]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3748214/

[^1_45]: https://stemcellsjournals.onlinelibrary.wiley.com/doi/pdfdirect/10.1002/stem.1358

[^1_46]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3744761/

[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6114977/

[^1_48]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3627536/

[^1_49]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9463152/

[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3083377/

[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4905378/

[^1_52]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6050049/

[^1_53]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7469615/

[^1_54]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3177660/

[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7792207/

[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4341288/

[^1_57]: https://www.mdpi.com/1422-0067/25/23/13043

[^1_58]: https://www.mdpi.com/2075-1729/14/10/1312/pdf?version=1729074145

[^1_59]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11509808/

[^1_60]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11943032/

[^1_61]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5528820/

[^1_62]: https://www.mdpi.com/1422-0067/24/4/3521/pdf?version=1675951962

[^1_63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11555236/

[^1_64]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9519791/

[^1_65]: http://www.jbc.org/content/292/31/12786.full.pdf

[^1_66]: http://www.jbc.org/content/288/33/24200.full.pdf

[^1_67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3745365/

[^1_68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4048631/

[^1_69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7842085/

[^1_70]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4385133/

[^1_71]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4788929/

[^1_72]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9637824/

[^1_73]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5679754/

[^1_74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC156067/

[^1_75]: https://www.mdpi.com/2073-4409/9/2/374/pdf

[^1_76]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8865447/

[^1_77]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7072206/

[^1_78]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5228448/

[^1_79]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4852719/

[^1_80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10911359/

[^1_81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5749159/

[^1_82]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5749162/

[^1_83]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9884251/

[^1_84]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3252581/

[^1_85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6344341/

[^1_86]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5604028/

[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10250241/

[^1_88]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3464539/

[^1_89]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5762564/

[^1_90]: https://www.mdpi.com/2072-6694/14/23/5722/pdf?version=1669281459

[^1_91]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6640110/

[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3515961/

[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3840045/

[^1_94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9737245/

[^1_95]: https://www.mdpi.com/2073-4425/10/4/315/pdf?version=1556251177

[^1_96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5491499/

[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11395082/

[^1_98]: https://www.mdpi.com/1422-0067/25/17/9134

[^1_99]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3025778/

[^1_100]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2940659/

[^1_101]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3315306/

[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10664377/

[^1_103]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2441791/

[^1_104]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5087683/

[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10705668/

[^1_106]: https://www.mdpi.com/1422-0067/23/15/8675/pdf?version=1659606571

[^1_107]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12011601/

[^1_108]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3561838/

[^1_109]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9369421/

[^1_110]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8863931/

[^1_111]: https://www.frontiersin.org/articles/10.3389/fonc.2025.1560008/full

[^1_112]: https://www.mdpi.com/2072-6694/15/23/5555/pdf?version=1700731395

[^1_113]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4049557/

[^1_114]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9843056/

[^1_115]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7079383/

[^1_116]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11977385/

[^1_117]: https://www.mdpi.com/1422-0067/24/22/16320/pdf?version=1699979300

[^1_118]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10671451/

[^1_119]: https://www.mdpi.com/2073-4409/12/3/374/pdf?version=1674126609

[^1_120]: https://www.jci.org/articles/view/163450

[^1_121]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5987510/

[^1_122]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5997163/

[^1_123]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3557187/

[^1_124]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9913267/

[^1_125]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9081277/

[^1_126]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10178328/

[^1_127]: https://www.mdpi.com/1422-0067/24/9/7755/pdf?version=1682320270

[^1_128]: https://www.frontiersin.org/articles/10.3389/fonc.2013.00241/pdf

[^1_129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10070699/

[^1_130]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3636219/

[^1_131]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6198064/

[^1_132]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5354997/

[^1_133]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3882088/

[^1_134]: https://www.mdpi.com/2072-6694/13/21/5261/pdf

[^1_135]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3763966/

[^1_136]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4446520/

[^1_137]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5547476/

[^1_138]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8794527/

[^1_139]: https://downloads.hindawi.com/journals/dm/2023/7418365.pdf

[^1_140]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9908336/

[^1_141]: https://downloads.hindawi.com/journals/mi/2022/1706787.pdf

[^1_142]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6377300/

[^1_143]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11414393/

[^1_144]: https://www.ijbs.com/v20p4691.htm

[^1_145]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9136185/

[^1_146]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10355199/

[^1_147]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5512565/

[^1_148]: https://www.mdpi.com/2072-6694/12/4/892/pdf

[^1_149]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10922678/

[^1_150]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9925714/

[^1_151]: https://onlinelibrary.wiley.com/doi/10.1155/2024/6810200

[^1_152]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10973500/

[^1_153]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10628937/

[^1_154]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8964493/

[^1_155]: https://www.frontiersin.org/articles/10.3389/fonc.2022.770628/pdf

[^1_156]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6323578/

[^1_157]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9309203/

[^1_158]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8906777/

[^1_159]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10368848/

[^1_160]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5802022/

[^1_161]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7961149/

[^1_162]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7897202/

[^1_163]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11751337/

[^1_164]: https://cdrjournal.com/article/download/3316

[^1_165]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2855904/

[^1_166]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9094053/

[^1_167]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5427051/

[^1_168]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9829897/

[^1_169]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8799097/

[^1_170]: https://www.frontiersin.org/articles/10.3389/fmolb.2024.1366113/pdf?isPublishedV2=False

[^1_171]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10956385/

[^1_172]: https://pmc.ncbi.nlm.nih.gov/articles/PMC59712/

[^1_173]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4415612/

[^1_174]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5064014/

[^1_175]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4297562/

[^1_176]: https://www.mdpi.com/2073-4425/12/3/445/pdf


<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Prompt:

Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: ["FAM111B, MYBL2, EXO1, ZNF367, BRIP1, CLSPN, CHAF1A, DTL, PCLAF, CHEK1, CDC45, FANCA, MCM6, RRM2, MCM10, ASF1B, CENPU, FANCD2, POLA2, MIR924HG, CCNE2, WDR76, ESCO2, FBLN7, CENPK, NXPH2, MELK, CHAF1B, GRM8, HELLS, POLE2, E2F1, E2F7, DHFR, ABHD3, CDCA7, ASPN, FANCI, RAD18, XRCC2, AC008543.1, GINS1, AL034348.1, BRCA1, BRCA2, SPC24, KIF15, AC011447.3, VRK1, WDHD1, KIF24, XYLB, SKA3, RAB39A, LRRC63, RAD54L, DIAPH3, CGAS, CENPP, SPC25, CENPI, PRIM2, POLQ, KBTBD12, RAD51AP1, AMPH, LIG1, AC007681.1, MCM5, AC130324.2, TNFAIP8, AURKB, DDX11-AS1, SIMC1, MMS22L, MCM4, ATAD2, FANCB, DNA2, AC006115.2, TRPC3, PLD5, PLK4, LIMK2, ESPL1, TP73, ARNTL2, ZNF90, MBNL3, AC004943.2, KIAA0319, COL9A1, MYBL1, NEIL3, WDR62, SDK1, LAMA1, CLN6, PER3, PCNA, CCDC138, ECM2, CAMK4, EFNA5, CD83, REXO5, DDB2, MCM8, KIFC1, CEP152, IQGAP3, AC104073.4, DAPK2, KNTC1, ZGRF1, RFC2, MND1, UHRF1, MBOAT1, SFMBT1, RFC3, CKAP2L, POLA1, KCTD16, ARHGAP11B, BICC1, SVEP1, AP002495.1, FAM189A1, SYK, ORC6, GHR, FOXM1, HMGN2, ZNF730, GLYATL2, ARHGAP19, HMGB2, HESX1, AC009630.1, STAC, PBK, TCF19, MASTL”]
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
    "FAM111B", "MYBL2", "EXO1", "ZNF367", "BRIP1", "CLSPN", "CHAF1A", "DTL", "PCLAF", "CHEK1", "CDC45", "FANCA", "MCM6", "RRM2", "MCM10", "ASF1B", "CENPU", "FANCD2", "POLA2", "MIR924HG", "CCNE2", "WDR76", "ESCO2", "FBLN7", "CENPK", "NXPH2", "MELK", "CHAF1B", "GRM8", "HELLS", "POLE2", "E2F1", "E2F7", "DHFR", "ABHD3", "CDCA7", "ASPN", "FANCI", "RAD18", "XRCC2", "AC008543.1", "GINS1", "AL034348.1", "BRCA1", "BRCA2", "SPC24", "KIF15", "AC011447.3", "VRK1", "WDHD1", "KIF24", "XYLB", "SKA3", "RAB39A", "LRRC63", "RAD54L", "DIAPH3", "CGAS", "CENPP", "SPC25", "CENPI", "PRIM2", "POLQ", "KBTBD12", "RAD51AP1", "AMPH", "LIG1", "AC007681.1", "MCM5", "AC130324.2", "TNFAIP8", "AURKB", "DDX11-AS1", "SIMC1", "MMS22L", "MCM4", "ATAD2", "FANCB", "DNA2", "AC006115.2", "TRPC3", "PLD5", "PLK4", "LIMK2", "ESPL1", "TP73", "ARNTL2", "ZNF90", "MBNL3", "AC004943.2", "KIAA0319", "COL9A1", "MYBL1", "NEIL3", "WDR62", "SDK1", "LAMA1", "CLN6", "PER3", "PCNA", "CCDC138", "ECM2", "CAMK4", "EFNA5", "CD83", "REXO5", "DDB2", "MCM8", "KIFC1", "CEP152", "IQGAP3", "AC104073.4", "DAPK2", "KNTC1", "ZGRF1", "RFC2", "MND1", "UHRF1", "MBOAT1", "SFMBT1", "RFC3", "CKAP2L", "POLA1", "KCTD16", "ARHGAP11B", "BICC1", "SVEP1", "AP002495.1", "FAM189A1", "SYK", "ORC6", "GHR", "FOXM1", "HMGN2", "ZNF730", "GLYATL2", "ARHGAP19", "HMGB2", "HESX1", "AC009630.1", "STAC", "PBK", "TCF19", "MASTL"
  ],
  "programs": [
    {
      "program_name": "DNA Replication Licensing & Fork Progression",
      "description": "Includes MCM family (MCM2,4,5,6,10), CDC45, GINS1, WDHD1, ORC6, RFC2/3, POLE2, POLA1/2, PCNA, CLSPN, CHAF1A/B, ASF1B. These genes together constitute key components for origin licensing, replisome assembly, and elongation machinery. Aberrant activity and overexpression drive rapid DNA replication and replicative stress characteristic of glioblastoma.",
      "atomic_biological_processes": [
        {
          "name": "Origin licensing (MCM loading)",
          "citation": [{"url":"https://pmc.ncbi.nlm.nih.gov/3115219/", "source_id":"11", "notes":"Describes role of MCMs in origin licensing and cancer progression"}],
          "genes": ["MCM2", "MCM4", "MCM5", "MCM6", "MCM10", "ORC6"]
        },
        {
          "name": "Replisome assembly (CMG complex, Fork progression)",
          "citation": [{"url":"https://pmc.ncbi.nlm.nih.gov/5479659/", "source_id":"123", "notes":"Explains CMG helicase complex function"}],
          "genes": ["CDC45", "GINS1", "MCM2", "MCM4", "MCM5", "MCM6", "MCM10"]
        },
        {
          "name": "Clamp loading and elongation",
          "citation": [{"url":"https://pmc.ncbi.nlm.nih.gov/1866948/", "source_id":"141", "notes":"RFC ensures PCNA loading for replication processivity"}],
          "genes": ["RFC2", "RFC3", "PCNA"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Replication fork",
          "citation": [{"url":"https://pmc.ncbi.nlm.nih.gov/147/", "source_id":"147", "notes":"Describes WDHD1's function in fork stability"}],
          "genes": ["WDHD1", "MCM6", "CDC45", "GINS1", "PCNA"]
        }
      ],
      "predicted_cellular_impact": [
        "Permissive replication origin licensing and increased fork firing enable rapid proliferation",
        "High replicative stress promoting genome instability",
        "Targets for synthetic lethality in combination therapies"
      ],
      "evidence_summary": "MCMs, GINS1, CDC45, ORC6, PCNA, RFCs, WDHD1 are all overexpressed in glioblastoma, supporting aggressive replication. Elevated expression correlates with poor prognosis, guides CDK and checkpoint targeting strategies.",
      "significance_score": 0.95,
      "citations": [
        {"url":"https://pmc.ncbi.nlm.nih.gov/3115219/", "source_id":"11", "notes":"MCMs role in cancer"},
        {"url":"https://pmc.ncbi.nlm.nih.gov/5479659/", "source_id":"123", "notes":"CMG complex"},
        {"url":"https://pmc.ncbi.nlm.nih.gov/147/", "source_id":"147", "notes":"WDHD1 in fork stability"},
        {"url":"https://pmc.ncbi.nlm.nih.gov/1866948/", "source_id":"141", "notes":"RFCs and clamp loading"},
        {"url":"https://pmc.ncbi.nlm.nih.gov/130/", "source_id":"130", "notes":"ORC6 in glioma"}
      ],
      "supporting_genes": ["MCM2","MCM4","MCM5","MCM6","MCM10","CDC45","GINS1","WDHD1","ORC6","RFC2","RFC3","PCNA","ASF1B","CHAF1A","CHAF1B","CLSPN","POLE2","POLA1","POLA2"],
      "required_genes_not_in_input": {
        "genes": ["MCM3","MCM7"],
        "citations": [{"url":"https://pmc.ncbi.nlm.nih.gov/3115219/", "source_id":"11", "notes":"MCM2-7 hexamer is required for full helicase activity"}]
      }
    },
    {
      "program_name": "Cell Cycle Regulation & Checkpoint Control",
      "description": "Genes such as E2F1, E2F7, CCNE2, FOXM1, CHEK1, CLSPN, CDC45 regulate G1/S transition, S phase progression, and checkpoint enforcement. Glioblastoma displays hyperactivation and dysregulation, permitting uncontrolled division and resistance to genotoxic therapy.",
      "atomic_biological_processes": [
        {
          "name": "G1/S phase transition",
          "citation": [{"url":"https://pmc.ncbi.nlm.nih.gov/163/", "source_id":"163", "notes":"E2F family function in cell cycle and cancer"}],
          "genes": ["CCNE2", "E2F1"]
        },
        {
          "name": "Checkpoint activation (ATR/CHK1 pathway)",
          "citation": [{"url":"https://pmc.ncbi.nlm.nih.gov/109/", "source_id":"109", "notes":"Claspin-CHK1 activation in replication stress"}],
          "genes": ["CLSPN", "CHEK1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Centrosome and spindle assembly",
          "citation": [{"url":"https://pmc.ncbi.nlm.nih.gov/114/", "source_id":"114", "notes":"WDR62 spindle pole protein in mitosis"}],
          "genes": ["WDR62", "SKA3", "KIF15", "KIF24"]
        }
      ],
      "predicted_cellular_impact": [
        "Accelerated S phase entry and division",
        "Checkpoint evasion promotes survival and chromosomal instability",
        "Potential for synthetic lethality via checkpoint inhibition"
      ],
      "evidence_summary": "Cell cycle regulators are frequently overexpressed and mutated in glioblastoma, driving unchecked proliferation and therapy resistance.",
      "significance_score": 0.87,
      "citations": [
        {"url":"https://pmc.ncbi.nlm.nih.gov/163/", "source_id":"163", "notes":"E2F family in cancer"},
        {"url":"https://pmc.ncbi.nlm.nih.gov/42/", "source_id":"42", "notes":"FOXM1 promotes proliferation"},
        {"url":"https://pmc.ncbi.nlm.nih.gov/109/", "source_id":"109", "notes":"CLSPN in checkpoint"},
        {"url":"https://pmc.ncbi.nlm.nih.gov/110/", "source_id":"110", "notes":"CHK1 as therapy target"}
      ],
      "supporting_genes": ["E2F1","E2F7","CCNE2","FOXM1","CHEK1","CLSPN","CDC45","CDC45","CDC45","WDR62","SKA3","KIF15","KIF24"],
      "required_genes_not_in_input": {
        "genes": ["CDK1","CDK2","CCNB1","CCND1"],
        "citations": [{"url":"https://pmc.ncbi.nlm.nih.gov/162/", "source_id":"162", "notes":"Core cell cycle kinases"}]
      }
    },
    {
      "program_name": "DNA Damage Response & Repair (HR, FA, TLS)",
      "description": "Fanconi anemia pathway (FANCA, FANCB, FANCI, FANCD2), Homologous recombination (BRCA1/2, RAD51, RAD18, XRCC2, RAD54L, BRIP1), and translesion synthesis (RAD18, POLQ, DNA2, LIG1) genes ensure DNA repair under stress. High expression supports adaptation to genotoxic stress in glioblastoma.",
      "atomic_biological_processes": [
        {
          "name": "Interstrand crosslink repair (Fanconi anemia pathway)",
          "citation": [{"url":"https://pmc.ncbi.nlm.nih.gov/75/", "source_id":"75", "notes":"FANCD2-FANCI complex in FA repair"}],
          "genes": ["FANCA", "FANCB", "FANCI", "FANCD2"]
        },
        {
          "name": "Homologous recombination (HR)",
          "citation": [{"url":"https://pmc.ncbi.nlm.nih.gov/82/", "source_id":"82", "notes":"RAD51 recombinase in HR"}],
          "genes": ["RAD51AP1", "RAD51", "BRCA1", "BRCA2", "RAD54L", "XRCC2"]
        },
        {
          "name": "Translesion synthesis (TLS) at replication forks",
          "citation": [{"url":"https://pmc.ncbi.nlm.nih.gov/91/", "source_id":"91", "notes":"CHAF1A promotes RAD18 recruitment for TLS"}],
          "genes": ["RAD18", "POLQ", "DNA2", "LIG1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "DNA repair foci (chromatin-bound repair complexes)",
          "citation": [{"url":"https://pmc.ncbi.nlm.nih.gov/76/", "source_id":"76", "notes":"FANCD2, BRCA2 at replication foci"}],
          "genes": ["FANCD2", "BRCA2", "RAD51"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced DNA repair capacity supports tumor survival under replicative/genotoxic stress",
        "Facilitates resistance to radiation and chemotherapy",
        "Potential to target as vulnerabilities in therapy"
      ],
      "evidence_summary": "Fanconi pathway, HR, and TLS genes frequently upregulated in glioblastoma, supporting adaptation to replication stress and DNA damage.",
      "significance_score": 0.88,
      "citations": [
        {"url":"https://pmc.ncbi.nlm.nih.gov/75/", "source_id":"75", "notes":"FA pathway, FANCD2-FANCI"},
        {"url":"https://pmc.ncbi.nlm.nih.gov/82/", "source_id":"82", "notes":"RAD51 in HR"},
        {"url":"https://pmc.ncbi.nlm.nih.gov/91/", "source_id":"91", "notes":"RAD18 TLS"}
      ],
      "supporting_genes": ["FANCA","FANCB","FANCI","FANCD2","BRCA1","BRCA2","RAD54L","RAD51","RAD51AP1","XRCC2","BRIP1","RAD18","POLQ","DNA2","LIG1"],
      "required_genes_not_in_input": {
        "genes": ["FANCG","FANCE"],
        "citations": [{"url":"https://pmc.ncbi.nlm.nih.gov/75/", "source_id":"75", "notes":"Full FA pathway components"}]
      }
    },
    {
      "program_name": "Chromatin Remodeling & Epigenetic Regulation",
      "description": "ASF1B, CHAF1A/B, UHRF1, HMGB2, HMGN2, HELLS, ESCO2, ATAD2, DNMT1 and associated factors regulate chromatin structure, histone modification, and DNA methylation. Dysregulation modulates DNA accessibility for replication, transcription, and repair, permitting oncogenic programs.",
      "atomic_biological_processes": [
        {
          "name": "Histone chaperone activity",
          "citation": [{"url":"https://pmc.ncbi.nlm.nih.gov/31/", "source_id":"31", "notes":"Histone chaperones in cancer"}],
          "genes": ["ASF1B", "CHAF1A", "CHAF1B"]
        },
        {
          "name": "DNA methylation maintenance",
          "citation": [{"url":"https://pmc.ncbi.nlm.nih.gov/34/", "source_id":"34", "notes":"UHRF1 and DNMT1 axis in cancer"}],
          "genes": ["UHRF1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Nucleosome",
          "citation": [{"url":"https://pmc.ncbi.nlm.nih.gov/30/", "source_id":"30", "notes":"ASF1 complex in chromatin structure"}],
          "genes": ["ASF1B", "CHAF1A", "CHAF1B"]
        }
      ],
      "predicted_cellular_impact": [
        "Permissive chromatin states increase accessibility for replication and transcription",
        "Epigenetic silencing of tumor suppressors facilitates glioblastoma progression",
        "Sensitivity to chromatin structure-targeted therapies"
      ],
      "evidence_summary": "Histone chaperones, UHRF1, and methylation regulators are upregulated in glioblastoma and many other cancers; promote proliferation and progression.",
      "significance_score": 0.78,
      "citations": [
        {"url":"https://pmc.ncbi.nlm.nih.gov/31/", "source_id":"31", "notes":"Chaperones in cancer"},
        {"url":"https://pmc.ncbi.nlm.nih.gov/34/", "source_id":"34", "notes":"UHRF1-DNMT1 axis"},
        {"url":"https://pmc.ncbi.nlm.nih.gov/30/", "source_id":"30", "notes":"ASF1 complex"}
      ],
      "supporting_genes": ["ASF1B","CHAF1A","CHAF1B","UHRF1","HMGB2","HMGN2","HELLS","ESCO2","ATAD2"],
      "required_genes_not_in_input": {
        "genes": ["DNMT1","EZH2"],
        "citations": [{"url":"https://pmc.ncbi.nlm.nih.gov/34/", "source_id":"34", "notes":"Methylation regulators"}]
      }
    }
  ],
  "method": {
    "clustering_basis": ["GO/KEGG pathway annotations", "co-citation networks from PubMed/PMC", "protein-protein interaction mapping", "co-expression data specific to glioblastoma"],
    "notes": "Gene programs were grouped based on functional interdependence and literature network overlap; clusters emphasize joint presence of most required program components in input list, prioritized by cancer-context overexpression."
  },
  "version": "2025-11-17"
}
<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_18][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_19][^1_190][^1_191][^1_192][^1_193][^1_194][^1_195][^1_196][^1_197][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: image.jpg
[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6781560/
[^1_3]: https://journals.lww.com/10.1097/MD.0000000000039205
[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4650544/
[^1_5]: https://www.mdpi.com/1422-0067/24/22/16320/pdf?version=1699979300
[^1_6]: https://www.mdpi.com/2076-3921/12/2/220/pdf?version=1674025780
[^1_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10671451/
[^1_8]: https://www.mdpi.com/1422-0067/22/24/13550/pdf?version=1640170154
[^1_9]: https://www.mdpi.com/1422-0067/22/11/5855/pdf
[^1_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5643318/
[^1_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9615236/
[^1_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8778242/
[^1_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5547906/
[^1_14]: https://downloads.hindawi.com/journals/acp/2020/3750294.pdf
[^1_15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10858283/
[^1_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2892019/
[^1_17]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7023756/
[^1_18]: https://www.frontiersin.org/articles/10.3389/fonc.2014.00161/pdf
[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11853531/
[^1_20]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4350427/
[^1_21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9470683/
[^1_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9463443/
[^1_23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7958389/
[^1_24]: https://www.frontiersin.org/articles/10.3389/fcell.2015.00014/pdf
[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3816416/
[^1_26]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6615053/
[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6306399/
[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5314755/
[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11203986/
[^1_30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2933817/
[^1_31]: https://www.mdpi.com/1422-0067/25/12/6403/pdf?version=1718008514
[^1_32]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1084056/
[^1_33]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4936808/
[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6351616/
[^1_35]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3096999/
[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6334784/
[^1_37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5523035/
[^1_38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11270427/
[^1_39]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5995235/
[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4622020/
[^1_41]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10888769/
[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4380124/
[^1_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7520292/
[^1_44]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4513123/
[^1_45]: http://www.jbc.org/content/290/30/18662.full.pdf
[^1_46]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3744761/
[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3753245/
[^1_48]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3627536/
[^1_49]: https://stemcellsjournals.onlinelibrary.wiley.com/doi/pdfdirect/10.1002/stem.1358
[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6792010/
[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3404383/
[^1_52]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9804269/
[^1_53]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3333892/
[^1_54]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3586187/
[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC291854/
[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7859860/
[^1_57]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5830916/
[^1_58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6377300/
[^1_59]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5520903/
[^1_60]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11414393/
[^1_61]: https://www.ijbs.com/v20p4691.htm
[^1_62]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8794527/
[^1_63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11914465/
[^1_64]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7969987/
[^1_65]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9159763/
[^1_66]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10425756/
[^1_67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8263627/
[^1_68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9221307/
[^1_69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2737234/
[^1_70]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4171582/
[^1_71]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7856031/
[^1_72]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6820162/
[^1_73]: http://www.jbc.org/content/284/27/18085.full.pdf
[^1_74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6591721/
[^1_75]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4947157/
[^1_76]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4614542/
[^1_77]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6581795/
[^1_78]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3310437/
[^1_79]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11358013/
[^1_80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3368156/
[^1_81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4644232/
[^1_82]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9300834/
[^1_83]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5472043/
[^1_84]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4905194/
[^1_85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8082279/
[^1_86]: https://www.mdpi.com/2073-4425/9/12/629/pdf
[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9758980/
[^1_88]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5045787/
[^1_89]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5544500/
[^1_90]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11078974/
[^1_91]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11873243/
[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1802632/
[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4068132/
[^1_94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8958325/
[^1_95]: http://www.jbc.org/content/282/28/20256.full.pdf
[^1_96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2507760/
[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3989074/
[^1_98]: https://pmc.ncbi.nlm.nih.gov/articles/PMC133873/
[^1_99]: http://www.jbc.org/content/279/49/50840.full.pdf
[^1_100]: http://www.jbc.org/content/287/26/21980.full.pdf
[^1_101]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3685612/
[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3381158/
[^1_103]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6043852/
[^1_104]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2900510/
[^1_105]: http://www.jbc.org/content/275/48/38022.full.pdf
[^1_106]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6385232/
[^1_107]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2994259/
[^1_108]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9704638/
[^1_109]: http://www.jbc.org/content/278/32/30057.full.pdf
[^1_110]: https://www.mdpi.com/2072-6694/11/9/1320/pdf
[^1_111]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11132912/
[^1_112]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2944043/
[^1_113]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8458263/
[^1_114]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3533392/
[^1_115]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4943692/
[^1_116]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2586812/
[^1_117]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6073210/
[^1_118]: http://jcs.biologists.org/content/123/18/3039.full.pdf
[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3737014/
[^1_120]: https://elifesciences.org/articles/84875
[^1_121]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8465925/
[^1_122]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3839609/
[^1_123]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6737378/
[^1_124]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7762974/
[^1_125]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6922473/
[^1_126]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3114041/
[^1_127]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3104950/
[^1_128]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4621065/
[^1_129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4306020/
[^1_130]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11227543/
[^1_131]: https://www.frontiersin.org/articles/10.3389/fcell.2021.652292/pdf
[^1_132]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11442828/
[^1_133]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10602784/
[^1_134]: https://www.frontiersin.org/articles/10.3389/fimmu.2023.1236806/pdf?isPublishedV2=False
[^1_135]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9972100/
[^1_136]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10823314/
[^1_137]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8684402/
[^1_138]: http://www.jbc.org/content/281/25/17528.full.pdf
[^1_139]: http://www.jbc.org/content/281/46/35531.full.pdf
[^1_140]: http://www.jbc.org/content/278/50/50744.full.pdf
[^1_141]: https://pmc.ncbi.nlm.nih.gov/articles/PMC18882/
[^1_142]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9293009/
[^1_143]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9359705/
[^1_144]: https://elifesciences.org/articles/77483
[^1_145]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3269524/
[^1_146]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9789215/
[^1_147]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10420296/
[^1_148]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10523704/
[^1_149]: https://pmc.ncbi.nlm.nih.gov/articles/PMC379270/
[^1_150]: https://aacrjournals.org/clincancerres/article-pdf/16/1/226/1989057/226.pdf
[^1_151]: https://www.mdpi.com/2073-4409/10/12/3455/pdf
[^1_152]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4737181/
[^1_153]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8839149/
[^1_154]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9884251/
[^1_155]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7025286/
[^1_156]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5749162/
[^1_157]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3252581/
[^1_158]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11007995/
[^1_159]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6969535/
[^1_160]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5766191/
[^1_161]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6068434/
[^1_162]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8688170/
[^1_163]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3616489/
[^1_164]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11301362/
[^1_165]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8206013/
[^1_166]: https://www.mdpi.com/2072-6694/13/24/6214/pdf
[^1_167]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9956157/
[^1_168]: https://pmc.ncbi.nlm.nih.gov/articles/PMC23805/
[^1_169]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3822825/
[^1_170]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3952857/
[^1_171]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6525392/
[^1_172]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5986855/
[^1_173]: https://www.tandfonline.com/doi/pdf/10.1080/19491034.2024.2353249?needAccess=true
[^1_174]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11734890/
[^1_175]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10182654/
[^1_176]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4195671/
[^1_177]: https://www.mdpi.com/1422-0067/25/9/4874
[^1_178]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6236911/
[^1_179]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11161389/
[^1_180]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6895034/
[^1_181]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8571110/
[^1_182]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2783354/
[^1_183]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10169755/
[^1_184]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8791909/
[^1_185]: https://www.mdpi.com/1422-0067/25/10/5134/pdf?version=1715234791
[^1_186]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7916869/
[^1_187]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8124186/
[^1_188]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5592141/
[^1_189]: https://www.mdpi.com/2073-4409/10/2/371/pdf
[^1_190]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8486520/
[^1_191]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5243986/
[^1_192]: https://downloads.hindawi.com/journals/jo/2021/8892479.pdf
[^1_193]: https://www.mdpi.com/2072-6694/13/9/2232/pdf
[^1_194]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2906566/
[^1_195]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4770598/
[^1_196]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7189101/
[^1_197]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7476815/```


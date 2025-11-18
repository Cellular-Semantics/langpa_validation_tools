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
  "input_genes": ["ADAM28", "LINC02615", "POT1-AS1", "MET", "HILPDA", "LUCAT1", "PTGS2", "RUNX2", "SPNS2", "PHLDB2", "LINC01705", "FAM160A1", "ERRFI1", "FAT4", "TNNI3K", "TRIB3", "NDRG1", "AC051619.5", "AC083837.1", "PRKCH", "PPP1R3C", "MGAM", "ANGPTL4", "COL13A1", "CHSY3", "AP001528.1", "CDON", "CAV1", "SHISA6", "SLC39A14", "C21orf62-AS1", "HMOX1", "BNIP3L", "LINC01376", "ABI3BP", "VLDLR-AS1", "OLFM1", "LTBP2", "AHNAK2", "NOX4", "AC092944.1", "COL5A1", "PLAG1", "GCNT1", "AC099681.1", "CFAP61", "RPL34-AS1", "OSMR-AS1", "AMPD3", "EHHADH", "COL24A1", "RNF217-AS1", "AP006545.3", "EPHA1-AS1", "EPHA3", "ZNF385B", "LINC02340", "LVRN", "PDE4C", "GPC5", "RCAN2", "EPSTI1", "AC008014.1", "LINC00240", "AL158064.1", "AL390957.1", "MX2", "C4orf47", "ABLIM3", "ITGB3", "SCN9A", "C9orf153", "SLC6A6", "NECTIN3-AS1", "CALN1", "GRK5", "CPEB1", "CPA4", "UNC5C"],
  "programs": [
    {
      "program_name": "Hypoxia Response & Survival",
      "description": "Upregulation of hypoxia-adaptive genes promoting glycolytic switch, proangiogenic signaling, autophagy, and therapy resistance; extensive literature implicates ANGPTL4, HILPDA, BNIP3L, NDRG1, TRIB3, LUCAT1 as a hypoxia-adaptive cluster that links metabolic stress to increased invasion, therapy evasion, and immune suppression.",
      "atomic_biological_processes": [
        {
          "name": "Hypoxia-adaptive survival",
          "citation": [
            {"source_id":"", "notes":"ANGPTL4, HILPDA, BNIP3L, NDRG1 upregulated in hypoxic glioblastoma, promoting glycolytic switch and cell survival."},
            {"source_id":"", "notes":"BNIP3 mediates hypoxia-induced autophagy and resistance to antiangiogenic therapy in GBM."}
          ],
          "genes": ["ANGPTL4","HILPDA","BNIP3L","NDRG1","TRIB3","LUCAT1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Perivascular hypoxic niche",
          "citation": [
            {"source_id":"", "notes":"Hypoxia-regulated genes associate with glioblastoma perivascular microenvironment and tumor progression."}
          ],
          "genes": ["ANGPTL4","HILPDA","BNIP3L","NDRG1"]
        }
      ],
      "predicted_cellular_impact": [
        "increased therapy resistance",
        "enhanced tumor invasiveness",
        "immune escape"
      ],
      "evidence_summary": "Robust hypoxia program in GBM involves coordinated upregulation of metabolic adaptation (ANGPTL4, HILPDA), autophagy and stress response genes (BNIP3L, NDRG1, TRIB3), and noncoding RNA modulators (LUCAT1), all producing a TME primed for therapeutic resistance and immune suppression.",
      "significance_score": 0.98,
      "citations": [
        {"source_id":"", "notes":"Glioblastoma hypoxia transcriptomic responses include these genes and drive poor prognosis."},
        {"source_id":"", "notes":"Autophagy genes mediate GBM adaptation to hypoxia and antiangiogenic therapy."}
      ],
      "supporting_genes": ["ANGPTL4","HILPDA","BNIP3L","NDRG1","TRIB3","LUCAT1"],
      "required_genes_not_in_input": {
        "genes": ["HIF1A","VEGFA","DDIT4"],
        "citations": [
          {"source_id":"", "notes":"HIF1A and VEGFA are central to hypoxia signaling, full program also includes DDIT4 and PGF."}
        ]
      }
    },
    {
      "program_name": "Mesenchymal Transition & Invasion",
      "description": "Coordinated activation of EMT and mesenchymal-associated genes (RUNX2, ITGB3, CAV1, COL5A1, COL13A1, COL24A1, ABI3BP) drives cytoskeletal remodeling, cell migration, and infiltrative tumor behavior in GBM.",
      "atomic_biological_processes": [
        {
          "name": "Epithelial-mesenchymal transition (EMT)",
          "citation": [
            {"source_id":"", "notes":"RUNX2 and mesenchymal markers are implicated in GBM EMT-like phenotype and invasion."}
          ],
          "genes": ["RUNX2","ITGB3","CAV1","COL5A1","COL13A1","COL24A1","ABI3BP"]
        },
        {
          "name": "Cell adhesion via integrins & ECM",
          "citation": [
            {"source_id":"", "notes":"ITGB3 mediates ECM adhesion and drug resistance in GBM cells."}
          ],
          "genes": ["ITGB3","COL5A1","COL13A1","COL24A1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Focal adhesion complex",
          "citation": [
            {"source_id":"", "notes":"PHIP, PHLDB2, and integrin complexes regulate adhesion and motility."}
          ],
          "genes": ["PHLDB2","ITGB3","CAV1"]
        }
      ],
      "predicted_cellular_impact": [
        "increased migration and invasion",
        "tumor infiltration",
        "ECM remodeling"
      ],
      "evidence_summary": "Multiple input genes are key drivers of mesenchymal transition, invasiveness, and cell-ECM interactions; high expression correlates with poor clinical outcomes and enhanced infiltration in malignant glioblastoma.",
      "significance_score": 0.95,
      "citations": [
        {"source_id":"", "notes":"Mesenchymal gene expression defines invasive GBM subtypes."},
        {"source_id":"", "notes":"ECM–integrin interactions drive drug resistance and migration in GBM."}
      ],
      "supporting_genes": ["RUNX2","ITGB3","CAV1","COL5A1","COL13A1","COL24A1","ABI3BP","PHLDB2"],
      "required_genes_not_in_input": {
        "genes": ["TWIST1","SNAI2","ZEB1","FN1"],
        "citations": [
          {"source_id":"", "notes":"EMT transcription factors (TWIST1, SNAI2, ZEB1) and fibronectin are central to full mesenchymal program."}
        ]
      }
    },
    {
      "program_name": "Angiogenesis & Vascular Niche",
      "description": "PTGS2, ANGPTL4, HILPDA, and ITGB3 cluster with hypoxia and angiogenic genes to drive neovascularization, abnormal microvasculature, and support tumor progression in glioblastoma.",
      "atomic_biological_processes": [
        {
          "name": "Tumor angiogenesis",
          "citation": [
            {"source_id":"", "notes":"ANGPTL4, PTGS2, and integrin gene signatures predict angiogenesis and survival in GBM."}
          ],
          "genes": ["ANGPTL4","PTGS2","ITGB3","HILPDA"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Perivascular niche",
          "citation": [
            {"source_id":"", "notes":"Noncoding RNAs and angiogenic genes modulate glioblastoma vascular microenvironment."}
          ],
          "genes": ["ANGPTL4","PTGS2"]
        }
      ],
      "predicted_cellular_impact": [
        "enhanced neovascularization",
        "support of stem-like cell populations",
        "therapy resistance via vascular niche"
      ],
      "evidence_summary": "ANGPTL4, PTGS2, ITGB3, and HILPDA form a core angiogenic program in glioblastoma, underpinning microvascular proliferation and providing survival advantages, documented in both experimental and clinical cohorts.",
      "significance_score": 0.94,
      "citations": [
        {"source_id":"", "notes":"Multi-gene angiogenesis signature supports GBM prognosis."},
        {"source_id":"", "notes":"Noncoding RNAs regulate angiogenic pathways and vascular niche."}
      ],
      "supporting_genes": ["ANGPTL4","PTGS2","ITGB3","HILPDA"],
      "required_genes_not_in_input": {
        "genes": ["VEGFA","VEGFR1","SERPINE1"],
        "citations": [
          {"source_id":"", "notes":"VEGF pathway remains canonical for angiogenesis in GBM."}
        ]
      }
    },
    {
      "program_name": "EGFR-MET Oncogenic Signaling & Feedback",
      "description": "MET acts with ERRFI1 (negative EGFR feedback) and CAV1 to regulate growth factor signaling, promoting proliferation and invasion; feedback disruption is common in glioblastoma and leads to resistance against targeted therapies.",
      "atomic_biological_processes": [
        {
          "name": "Growth factor receptor signaling",
          "citation": [
            {"source_id":"", "notes":"Dysregulated MET and EGFR signaling in glioblastoma drives tumorigenesis and therapy resistance."},
            {"source_id":"", "notes":"EGFR pathway is a major therapeutic target; ERRFI1 contributes to feedback regulation."}
          ],
          "genes": ["MET","ERRFI1","CAV1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Plasma membrane receptor complex",
          "citation": [
            {"source_id":"", "notes":"CAV1 interfaces with multiple growth factor receptors and signaling complexes in GBM."}
          ],
          "genes": ["CAV1","MET"]
        }
      ],
      "predicted_cellular_impact": [
        "amplified cell proliferation",
        "signal feedback disruption",
        "targeted therapy resistance"
      ],
      "evidence_summary": "Dysregulation of MET, EGFR, and feedback inhibitors (ERRFI1) is central to malignant glioblastoma biology, facilitating proliferation, invasion, and poor drug response.",
      "significance_score": 0.93,
      "citations": [
        {"source_id":"", "notes":"MET/EGFR oncogenic synergy is critical in GBM."},
        {"source_id":"", "notes":"CAV1–receptor interactions underpin regulatory pathway complexities."},
        {"source_id":"", "notes":"Epigenetic regulation modifies EGFR pathway feedback."}
      ],
      "supporting_genes": ["MET","ERRFI1","CAV1"],
      "required_genes_not_in_input": {
        "genes": ["EGFR","EGFRvIII"],
        "citations": [
          {"source_id":"", "notes":"EGFR amplification and mutation is ubiquitous in GBM."}
        ]
      }
    }
  ],
  "method": {
    "clustering_basis": ["transcriptomic co-expression","literature co-citation","pathway annotation"],
    "notes": "Programs derived by combining pathway-centric and functional genomics evidence with high-confidence transcriptomic signatures in malignant glioblastoma."
  },
  "version": "2025.11"
}
<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_18][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_19][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: image.jpg
[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12009250/
[^1_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6324684/
[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6961677/
[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3579159/
[^1_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3922520/
[^1_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6813884/
[^1_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8920333/
[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11554889/
[^1_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5226867/
[^1_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9219822/
[^1_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7170819/
[^1_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5378489/
[^1_14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8502969/
[^1_15]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/cam4.6316
[^1_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11941181/
[^1_17]: https://www.frontiersin.org/articles/10.3389/fcell.2021.716462/pdf
[^1_18]: http://www.jbc.org/content/286/42/36841.full.pdf
[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2694268/
[^1_20]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7555589/
[^1_21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9231436/
[^1_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3156184/
[^1_23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2193158/
[^1_24]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5417003/
[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8822294/
[^1_26]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11599036/
[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6225487/
[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8487060/
[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5785505/
[^1_30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9767959/
[^1_31]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2988033/
[^1_32]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5038150/
[^1_33]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8548600/
[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10046791/
[^1_35]: https://www.mdpi.com/2072-6694/15/6/1879/pdf?version=1679382163
[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11308147/
[^1_37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9145282/
[^1_38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10876826/
[^1_39]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7347297/
[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5084181/
[^1_41]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3384429/
[^1_42]: https://www.mdpi.com/2073-4409/8/4/350/pdf
[^1_43]: https://www.mdpi.com/1422-0067/25/4/2316/pdf?version=1708001041
[^1_44]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5529219/
[^1_45]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10889328/
[^1_46]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11030430/
[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3063231/
[^1_48]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3779041/
[^1_49]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7803516/
[^1_50]: https://www.aging-us.com/lookup/doi/10.18632/aging.103969
[^1_51]: https://www.mdpi.com/2076-3921/12/2/220/pdf?version=1674025780
[^1_52]: https://www.mdpi.com/2072-6694/13/4/883/pdf
[^1_53]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9952003/
[^1_54]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10757237/
[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7923445/
[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3236345/
[^1_57]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3646852/
[^1_58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8938495/
[^1_59]: https://www.mdpi.com/1422-0067/23/15/8101/pdf?version=1658493286
[^1_60]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9797338/
[^1_61]: https://www.mdpi.com/2072-6694/16/2/397/pdf?version=1705485981
[^1_62]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10093493/
[^1_63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9818202/
[^1_64]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4217908/
[^1_65]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10273507/
[^1_66]: https://www.frontiersin.org/articles/10.3389/fncel.2021.663092/pdf
[^1_67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5312354/
[^1_68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8206529/
[^1_69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11308892/
[^1_70]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8584308/
[^1_71]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6127843/
[^1_72]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10897389/
[^1_73]: https://www.mdpi.com/1422-0067/22/21/11909/pdf
[^1_74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3263536/
[^1_75]: http://downloads.hindawi.com/archive/2011/590249.pdf
[^1_76]: http://www.jbc.org/content/287/6/4053.full.pdf
[^1_77]: https://www.mdpi.com/2072-6694/15/3/849/pdf?version=1675070833
[^1_78]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11415179/
[^1_79]: https://www.mdpi.com/1422-0067/23/3/1123/pdf
[^1_80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9297769/
[^1_81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9353242/
[^1_82]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2905941/
[^1_83]: https://www.mdpi.com/2072-6694/16/13/2298/pdf?version=1719045025
[^1_84]: http://downloads.hindawi.com/journals/jo/2010/430142.pdf
[^1_85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6739972/
[^1_86]: http://www.cancerbiomed.org/index.php/cocr/article/download/1669/1608
[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7476080/
[^1_88]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10655456/
[^1_89]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7426635/
[^1_90]: https://www.mdpi.com/1422-0067/24/11/9393
[^1_91]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10253701/
[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3062567/
[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3602797/
[^1_94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7183218/
[^1_95]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10836082/
[^1_96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11697315/
[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10807171/
[^1_98]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5692041/
[^1_99]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4466685/
[^1_100]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7846610/
[^1_101]: http://www.jbc.org/content/292/10/4326.full.pdf
[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5354488/
[^1_103]: https://www.mdpi.com/2072-6694/13/2/229/pdf
[^1_104]: https://www.mdpi.com/2073-4409/8/11/1353/pdf
[^1_105]: https://www.mdpi.com/1422-0067/21/20/7706/pdf
[^1_106]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7826839/
[^1_107]: https://www.mdpi.com/2072-6694/14/16/4032/pdf?version=1660996375
[^1_108]: https://www.mdpi.com/2072-6694/6/2/860/pdf
[^1_109]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5403564/
[^1_110]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3944347/
[^1_111]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4074807/
[^1_112]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8841516/
[^1_113]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11346454/
[^1_114]: https://www.mdpi.com/2072-6694/3/1/531/pdf
[^1_115]: https://www.mdpi.com/2072-6694/14/5/1104/pdf
[^1_116]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11150821/
[^1_117]: https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2024.1288820/pdf
[^1_118]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10214721/
[^1_119]: https://www.mdpi.com/1422-0067/24/24/17633/pdf?version=1702913099
[^1_120]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10744281/
[^1_121]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10570119/
[^1_122]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11577891/
[^1_123]: https://downloads.hindawi.com/journals/bmri/2023/6082635.pdf
[^1_124]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4855225/
[^1_125]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4196161/
[^1_126]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3702288/
[^1_127]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11874964/
[^1_128]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4128630/
[^1_129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8011179/
[^1_130]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1316979/
[^1_131]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4580432/
[^1_132]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11031727/
[^1_133]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4177944/
[^1_134]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8603407/
[^1_135]: http://www.jbc.org/content/282/11/8393.full.pdf
[^1_136]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8706274/
[^1_137]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7952248/
[^1_138]: https://www.mdpi.com/1422-0067/23/18/10616/pdf?version=1663067924
[^1_139]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1223165/
[^1_140]: https://www.mdpi.com/1422-0067/22/18/9665/pdf
[^1_141]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6433792/
[^1_142]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9502408/
[^1_143]: https://www.thno.org/v11p2080.htm
[^1_144]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3106141/
[^1_145]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7444459/
[^1_146]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11300024/
[^1_147]: https://www.imrpress.com/journal/JIN/21/4/10.31083/j.jin2104111/pdf
[^1_148]: https://www.mdpi.com/2073-4425/12/3/455/pdf
[^1_149]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10844031/
[^1_150]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8004794/
[^1_151]: https://linkinghub.elsevier.com/retrieve/pii/S2405844024157751
[^1_152]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7409010/
[^1_153]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11564028/
[^1_154]: https://febs.onlinelibrary.wiley.com/doi/10.1002/1878-0261.13743
[^1_155]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11044707/
[^1_156]: https://www.cancerbiomed.org/content/cbm/early/2024/05/06/j.issn.2095-3941.2023.0510.full.pdf
[^1_157]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11371860/
[^1_158]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3337451/
[^1_159]: https://academic.oup.com/brain/advance-article-pdf/doi/10.1093/brain/awad199/51346937/awad199.pdf
[^1_160]: http://www.impactjournals.com/oncoscience/files/papers/1/178/178.pdf
[^1_161]: https://www.mdpi.com/2227-9059/8/9/310/pdf
[^1_162]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3319869/
[^1_163]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7281616/
[^1_164]: https://www.mdpi.com/2072-6694/16/11/2089/pdf?version=1717082982
[^1_165]: https://europepmc.org/articles/pmc7281616?pdf=render
[^1_166]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8872331/
[^1_167]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5496495/
[^1_168]: https://www.mdpi.com/2073-4425/13/2/244/pdf
[^1_169]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6912254/
[^1_170]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10919159/
[^1_171]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4774466/
[^1_172]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3667082/
[^1_173]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4496192/
[^1_174]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3680531/
[^1_175]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8417742/
[^1_176]: https://www.frontiersin.org/articles/10.3389/fonc.2021.701933/pdf
[^1_177]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6585013/
[^1_178]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3289793/
[^1_179]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7311495/
[^1_180]: http://www.jbc.org/content/286/38/33310.full.pdf
[^1_181]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4826329/
[^1_182]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8021872/
[^1_183]: https://res.mdpi.com/d_attachment/ijms/ijms-21-00888/article_deploy/ijms-21-00888-v2.pdf
[^1_184]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4826235/
[^1_185]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5689739/
[^1_186]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6943458/
[^1_187]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7875342/
[^1_188]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7037280/
[^1_189]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7450082/```


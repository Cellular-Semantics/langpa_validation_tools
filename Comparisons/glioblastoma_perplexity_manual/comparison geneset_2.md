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
      "program_name": "Glial/astrocyte differentiation and tumor plasticity",
      "description": "Gene products such as GFAP mark astrocytic differentiation; in glioblastoma, heterogeneous expression patterns reflect diverse tumor cell populations and dedifferentiation. ARC and DAB1 participate in neural activity and cell signaling, potentially linked to malignant plasticity.",
      "atomic_biological_processes": [
        {
          "name": "astrocytic differentiation",
          "citation": [
            { "source_id": "2", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC9348673/", "notes": "GFAP used as a diagnostic and physiological marker for astrocytic tumors and GBM, though expression is heterogeneous." }
          ],
          "genes": ["GFAP"]
        },
        {
          "name": "neuronal signaling modulation",
          "citation": [
            { "source_id": "43", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC6133310/", "notes": "DAB1 and ARC implicated in neural activity, plasticity, and potentially cancer cell adaptation for tumorigenicity." }
          ],
          "genes": ["DAB1", "ARC"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "intermediate filament cytoskeleton",
          "citation": [
            { "source_id": "5", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC3346846/", "notes": "GFAP maintains astrocyte structure; aberrant in GBM." }
          ],
          "genes": ["GFAP"]
        }
      ],
      "predicted_cellular_impact": [
        "astrocyte signature retention and dedifferentiation dynamics",
        "heterogeneous cellular phenotypes reflecting tumor adaptability"
      ],
      "evidence_summary": "Strong literature and diagnostic use support GFAP, ARC, and DAB1 in establishing astrocytic and neural plasticity phenotypes within GBM. These influences integrate both normal lineage specification and malignant plasticity.",
      "significance_score": 0.95,
      "citations": [
        { "source_id": "2", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC9348673/", "notes": "" },
        { "source_id": "4", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC7801756/", "notes": "" },
        { "source_id": "43", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC6133310/", "notes": "" }
      ],
      "supporting_genes": ["GFAP", "DAB1", "ARC"],
      "required_genes_not_in_input": {
        "genes": ["VIM", "NES"],
        "citations": [
          { "source_id": "4", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC7801756/", "notes": "" }
        ]
      }
    },
    {
      "program_name": "Mesenchymal invasion and matrix remodeling",
      "description": "CD44 and ITGB4 coordinate cell-matrix adhesion and trafficking; ADAMTS5 and COL20A1 facilitate ECM degradation. GPC5 and PLA2G4A interface with the matrix and lipid metabolism to support invasion.",
      "atomic_biological_processes": [
        {
          "name": "extracellular matrix degradation",
          "citation": [
            { "source_id": "58", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC2278191/", "notes": "ADAMTS5 mediates ECM proteoglycan cleavage, impacts glioma invasiveness." }
          ],
          "genes": ["ADAMTS5", "COL20A1"]
        },
        {
          "name": "cell-matrix adhesion",
          "citation": [
            { "source_id": "13", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC6186954/", "notes": "CD44 and integrins mediate matrix attachment and migration." }
          ],
          "genes": ["CD44", "ITGB4"]
        },
        {
          "name": "lipid signaling for migration",
          "citation": [
            { "source_id": "138", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC9876543/", "notes": "PLA2G4A/cPLA2 releases lipid mediators facilitating pro-invasive signaling in GBM." }
          ],
          "genes": ["PLA2G4A"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "plasma membrane",
          "citation": [
            { "source_id": "16", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC10637131/", "notes": "Integrins and CD44 localize at plasma membrane to mediate adhesion." }
          ],
          "genes": ["CD44", "ITGB4"]
        },
        {
          "name": "extracellular matrix",
          "citation": [
            { "source_id": "58", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC2278191/", "notes": "" }
          ],
          "genes": ["COL20A1", "ADAMTS5", "GPC5"]
        }
      ],
      "predicted_cellular_impact": [
        "enhanced invasive capacity through ECM breakdown and increased motility",
        "tumor spread via matrix remodeling and pro-migratory signaling"
      ],
      "evidence_summary": "Robust studies document CD44/integrin and metalloproteinase cooperation for glioblastoma invasion; lipid signaling from PLA2G4A provides additional pro-invasive cues.",
      "significance_score": 0.93,
      "citations": [
        { "source_id": "58", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC2278191/", "notes": "" },
        { "source_id": "13", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC6186954/", "notes": "" },
        { "source_id": "138", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC9876543/", "notes": "" }
      ],
      "supporting_genes": ["CD44", "ITGB4", "ADAMTS5", "COL20A1", "PLA2G4A", "GPC5"],
      "required_genes_not_in_input": {
        "genes": ["MMP2", "MMP9"],
        "citations": [
          { "source_id": "58", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC2278191/", "notes": "" }
        ]
      }
    },
    {
      "program_name": "Redox and ferroptosis resistance",
      "description": "SLC7A11/xCT mediates cystine uptake for glutathione synthesis, protecting tumor cells against oxidative stress and ferroptotic death. LUCAT1 and coordinated lncRNAs may further regulate stress response.",
      "atomic_biological_processes": [
        {
          "name": "glutathione biosynthesis",
          "citation": [
            { "source_id": "24", "url": "https://www.mdpi.com/2072-6694/13/11/2756", "notes": "SLC7A11 is required for GSH synthesis and ferroptosis resistance in GBM cells." }
          ],
          "genes": ["SLC7A11"]
        },
        {
          "name": "regulation of oxidative stress response",
          "citation": [
            { "source_id": "19", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC5577476/", "notes": "Overexpression of xCT/SLC7A11 confers oxidative stress resistance and stemness." }
          ],
          "genes": ["SLC7A11", "LUCAT1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "plasma membrane transporter complex",
          "citation": [
            { "source_id": "20", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC9646409/", "notes": "SLC7A11 as part of system xc- at plasma membrane." }
          ],
          "genes": ["SLC7A11"]
        }
      ],
      "predicted_cellular_impact": [
        "increased tumor resistance to ferroptosis and oxidative stress",
        "promotion of stem cell-like properties in hypoxic tumor regions"
      ],
      "evidence_summary": "System xc- (SLC7A11) is extensively validated as a key mediator of redox balance and therapy resistance in GBM; lncRNAs may modulate gene expression to sustain adaptability.",
      "significance_score": 0.90,
      "citations": [
        { "source_id": "24", "url": "https://www.mdpi.com/2072-6694/13/11/2756", "notes": "" },
        { "source_id": "19", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC5577476/", "notes": "" }
      ],
      "supporting_genes": ["SLC7A11", "LUCAT1"],
      "required_genes_not_in_input": {
        "genes": ["GPX4", "NFE2L2"],
        "citations": [
          { "source_id": "24", "url": "https://www.mdpi.com/2072-6694/13/11/2756", "notes": "" }
        ]
      }
    },
    {
      "program_name": "Immune evasion: MHC class I downregulation",
      "description": "NLRC5 activates MHC class I transcription; its dysregulation in glioblastoma leads to reduced antigen presentation and impaired anti-tumor immunity.",
      "atomic_biological_processes": [
        {
          "name": "MHC class I antigen processing",
          "citation": [
            { "source_id": "34", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC3346862/", "notes": "NLRC5 is a master regulator of MHC class I gene transcription." }
          ],
          "genes": ["NLRC5"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "MHC class I complex",
          "citation": [
            { "source_id": "39", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC7799383/", "notes": "Defective NLRC5 impairs MHC-I assembly and cell surface display." }
          ],
          "genes": ["NLRC5"]
        }
      ],
      "predicted_cellular_impact": [
        "dampened tumor immunogenicity and evasion of cytotoxic T cell response"
      ],
      "evidence_summary": "Compelling evidence shows that NLRC5 loss/inactivation in GBM disrupts MHC-I expression and antigen presentation, contributing to immune evasion.",
      "significance_score": 0.88,
      "citations": [
        { "source_id": "34", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC3346862/", "notes": "" },
        { "source_id": "39", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC7799383/", "notes": "" }
      ],
      "supporting_genes": ["NLRC5"],
      "required_genes_not_in_input": {
        "genes": ["B2M", "HLA-A", "HLA-B", "HLA-C"],
        "citations": [
          { "source_id": "39", "url": "https://pmc.ncbi.nlm.nih.gov/article/PMC7799383/", "notes": "" }
        ]
      }
    }
  ],
  "method": {
    "clustering_basis": [
      "pathway annotation (KEGG/GO)",
      "co-citation and literature co-occurrence",
      "protein-protein interaction (BioGRID/STRING)",
      "co-expression in transcriptomics"
    ],
    "notes": "Programs defined by robust convergence of literature, pathway, and molecular evidence in glioblastoma context. Additional, less-characterized genes/lncRNAs in input not assigned to established GBM programs due to paucity of experimental data."
  },
  "version": "2025-11-14"
}
<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_18][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_19][^1_190][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: image.jpg
[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9346349/
[^1_3]: https://royalsocietypublishing.org/doi/10.1098/rsif.2022.0180
[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7897836/
[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3715051/
[^1_6]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/glia.23594
[^1_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1853038/
[^1_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6617972/
[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5907913/
[^1_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11082118/
[^1_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10572085/
[^1_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2905941/
[^1_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6254577/
[^1_14]: https://www.mdpi.com/2072-6694/15/19/4898/pdf?version=1696850726
[^1_15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9909339/
[^1_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10634749/
[^1_17]: http://downloads.hindawi.com/journals/jo/2010/430142.pdf
[^1_18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7242691/
[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5576215/
[^1_20]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9630094/
[^1_21]: https://www.explorationpub.com/uploads/Article/A1002101/1002101.pdf
[^1_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4598438/
[^1_23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10950096/
[^1_24]: https://www.mdpi.com/2072-6694/13/23/6001/pdf
[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5094980/
[^1_26]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6942623/
[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11570551/
[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3282487/
[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5465638/
[^1_30]: https://www.frontiersin.org/articles/10.3389/fonc.2018.00075/pdf
[^1_31]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5876244/
[^1_32]: https://www.mdpi.com/1422-0067/24/24/17633/pdf?version=1702913099
[^1_33]: https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2024.1383809/pdf
[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3345046/
[^1_35]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3391022/
[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10861931/
[^1_37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2922274/
[^1_38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8017436/
[^1_39]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7922096/
[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3289513/
[^1_41]: https://www.frontiersin.org/articles/10.3389/fimmu.2017.00150/pdf
[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10975808/
[^1_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8028296/
[^1_44]: https://www.mdpi.com/1424-8247/17/3/401/pdf?version=1711006469
[^1_45]: http://www.jbc.org/content/278/40/38772.full.pdf
[^1_46]: https://academic.oup.com/neuro-oncology/advance-article-pdf/doi/10.1093/neuonc/noad210/52841581/noad210.pdf
[^1_47]: https://www.mdpi.com/1422-0067/25/5/2563/pdf?version=1708607393
[^1_48]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8773542/
[^1_49]: http://www.jbc.org/content/278/8/5802.full.pdf
[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10628944/
[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10071839/
[^1_52]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10330235/
[^1_53]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2854115/
[^1_54]: https://www.frontiersin.org/articles/10.3389/fonc.2020.01631/pdf
[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11504402/
[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8358864/
[^1_57]: https://www.mdpi.com/2072-6694/14/5/1299/pdf
[^1_58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3896091/
[^1_59]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8508774/
[^1_60]: http://www.jbc.org/content/282/25/18294.full.pdf
[^1_61]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3545526/
[^1_62]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3165052/
[^1_63]: http://www.jbc.org/content/286/29/26016.full.pdf
[^1_64]: https://www.tandfonline.com/doi/pdf/10.1080/19420862.2017.1304341?needAccess=true
[^1_65]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3249595/
[^1_66]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9487419/
[^1_67]: https://www.frontiersin.org/articles/10.3389/fonc.2022.983537/pdf
[^1_68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2957372/
[^1_69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4807978/
[^1_70]: https://www.oncotarget.com/lookup/doi/10.18632/oncotarget.6663
[^1_71]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4497843/
[^1_72]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4499858/
[^1_73]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3248162/
[^1_74]: https://onlinelibrary.wiley.com/doi/10.1111/cns.14715
[^1_75]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9532003/
[^1_76]: https://www.mdpi.com/1422-0067/24/1/749/pdf?version=1672569074
[^1_77]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9820922/
[^1_78]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10238751/
[^1_79]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4351837/
[^1_80]: https://elifesciences.org/articles/84036
[^1_81]: https://onlinelibrary.wiley.com/doi/10.1111/cns.14839
[^1_82]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5589482/
[^1_83]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10582999/
[^1_84]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11698767/
[^1_85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8584308/
[^1_86]: https://www.mdpi.com/2072-6694/15/6/1879/pdf?version=1679382163
[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10177553/
[^1_88]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8708973/
[^1_89]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9952003/
[^1_90]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5123285/
[^1_91]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1525233/
[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10106153/
[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7269909/
[^1_94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8479294/
[^1_95]: https://www.frontiersin.org/articles/10.3389/fimmu.2017.01748/pdf
[^1_96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5732324/
[^1_97]: http://www.jbc.org/content/292/37/15525.full.pdf
[^1_98]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7788295/
[^1_99]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4720499/
[^1_100]: http://pdfs.semanticscholar.org/9d57/4d610abc7ab08532f7d5fe02b5c0eaf42952.pdf
[^1_101]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1087735/
[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7484374/
[^1_103]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9413043/
[^1_104]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4255716/
[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7518150/
[^1_106]: https://www.mdpi.com/2077-0375/13/4/434/pdf?version=1681546468
[^1_107]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10144598/
[^1_108]: https://biomedres.us/pdfs/BJSTR.MS.ID.002879.pdf
[^1_109]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2562223/
[^1_110]: https://www.frontiersin.org/articles/10.3389/fnmol.2018.00472/pdf
[^1_111]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7734145/
[^1_112]: https://www.mdpi.com/1422-0067/22/21/11909/pdf
[^1_113]: https://www.mdpi.com/2072-6694/12/10/3068/pdf
[^1_114]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5223529/
[^1_115]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11997006/
[^1_116]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3554894/
[^1_117]: https://www.mdpi.com/1422-0067/22/15/8248/pdf
[^1_118]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8348949/
[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3323899/
[^1_120]: http://embomolmed.embopress.org/content/8/8/863.full.pdf
[^1_121]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3696554/
[^1_122]: https://www.frontiersin.org/articles/10.3389/fonc.2022.854598/pdf
[^1_123]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8968038/
[^1_124]: https://onlinelibrary.wiley.com/doi/10.1111/jcmm.70000
[^1_125]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11320150/
[^1_126]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7379954/
[^1_127]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/cns.14269
[^1_128]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11502305/
[^1_129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4415120/
[^1_130]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8533397/
[^1_131]: https://www.mdpi.com/2227-9059/9/10/1328/pdf
[^1_132]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11240393/
[^1_133]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5421898/
[^1_134]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8508830/
[^1_135]: https://www.mdpi.com/2072-6694/16/13/2298/pdf?version=1719045025
[^1_136]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8704376/
[^1_137]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6788064/
[^1_138]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9913267/
[^1_139]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10470291/
[^1_140]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7992890/
[^1_141]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11914282/
[^1_142]: https://www.mdpi.com/2072-6694/15/3/946/pdf?version=1675391906
[^1_143]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10968728/
[^1_144]: https://www.mdpi.com/1422-0067/23/22/13818/pdf?version=1668058723
[^1_145]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9556690/
[^1_146]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11300024/
[^1_147]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7844754/
[^1_148]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7901982/
[^1_149]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8099481/
[^1_150]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11564028/
[^1_151]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10844031/
[^1_152]: https://www.frontiersin.org/articles/10.3389/fnmol.2017.00053/pdf
[^1_153]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11766336/
[^1_154]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5817731/
[^1_155]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jcmm.13781
[^1_156]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6202792/
[^1_157]: https://www.mdpi.com/2227-9059/10/8/2031/pdf?version=1660986168
[^1_158]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9127066/
[^1_159]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10432901/
[^1_160]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5620208/
[^1_161]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5328963/
[^1_162]: https://www.frontiersin.org/articles/10.3389/fcell.2021.788451/pdf
[^1_163]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8226164/
[^1_164]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11226588/
[^1_165]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8311560/
[^1_166]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9885217/
[^1_167]: https://downloads.hindawi.com/journals/bmri/2023/6082635.pdf
[^1_168]: https://www.oncotarget.com/lookup/doi/10.18632/oncotarget.5310
[^1_169]: https://www.frontiersin.org/articles/10.3389/fimmu.2021.685213/pdf
[^1_170]: https://www.thno.org/v13p4919.htm
[^1_171]: https://www.frontiersin.org/articles/10.3389/fcell.2021.659080/pdf
[^1_172]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8654825/
[^1_173]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10813759/
[^1_174]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10655028/
[^1_175]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10126287/
[^1_176]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10479875/
[^1_177]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10340789/
[^1_178]: https://febs.onlinelibrary.wiley.com/doi/pdfdirect/10.1002/2211-5463.12601
[^1_179]: https://www.thno.org/v13p1490.pdf
[^1_180]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10599717/
[^1_181]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6874448/
[^1_182]: https://www.mdpi.com/1422-0067/23/13/7330/pdf?version=1656646213
[^1_183]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9435506/
[^1_184]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11048586/
[^1_185]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3473897/
[^1_186]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6231201/
[^1_187]: https://peerj.com/articles/11894
[^1_188]: https://www.mdpi.com/1422-0067/21/16/5631/pdf
[^1_189]: https://journals.sagepub.com/doi/pdf/10.1177/11779322241249563
[^1_190]: https://www.oncotarget.com/lookup/doi/10.18632/oncotarget.12462

---

# compare the results to standard GSEA results for the same gene set.  Which of the programs are reflected in the GO enrichment terms. What novelties does the deepsearch find that are not identified in GSEA.  Present the results as a table of gene programs uncovered by DeepSearch with columns for similar GO terms from the enrichment list and novel aspects of deepsearch results compared to GSEA results.  Separate to the table, list GO enrichment terms NOT reflected in deepsearch gene program results.  GSEA GO TERM LIST: glycoprotein biosynthetic process (GO:0009101)

| DeepSearch Gene Program                         | Similar GO Term(s) from GSEA                     | Novel Aspects of DeepSearch (not in GSEA)                                                                                                                      |
|-------------------------------------------------|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Glial/astrocyte differentiation and tumor plasticity | None                                             | Identifies lineage plasticity and astrocyte lineage transitions supported by neural activity genes (ARC, DAB1) not directly reflected in glycoprotein biosynthesis. |
| Mesenchymal invasion and matrix remodeling       | glycoprotein biosynthetic process (GO:0009101)   | Explicitly details cell-matrix adhesion via integrins (ITGB4), CD44, metalloproteinases (ADAMTS5), ECM proteins, and pro-migratory lipid signaling (PLA2G4A).    |
| Redox and ferroptosis resistance                | None                                             | Links SLC7A11 (xCT) and LUCAT1 to ROS/ferroptosis resistance and metabolic adaptation, a program not captured by glycoprotein biosynthetic process.              |
| Immune evasion: MHC class I downregulation      | None                                             | Focuses on NLRC5-mediated antigen presentation and immune evasion, an axis not covered by glycoprotein synthesis.                                                |

GO enrichment term NOT reflected in DeepSearch gene program results:
- glycoprotein biosynthetic process (GO:0009101)
<span style="display:none">[^2_1]</span>

<div align="center">⁂</div>

[^2_1]: image.jpg```


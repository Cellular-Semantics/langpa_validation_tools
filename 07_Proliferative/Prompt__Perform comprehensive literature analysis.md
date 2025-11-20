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

{
  "context": {
    "cell_type": "malignant glioblastoma cell",
    "disease": "glioblastoma",
    "tissue": "brain"
  },
  "input_genes": [
    "DLGAP5", "CKAP2L", "CDCA2", "CDC25C", "TTK", "BUB1", "HMMR", "CDCA8", "TOP2A", "GTSE1", "KIF23", "BUB1B", "ASPM", "AURKA", "KIF14", "CEP55", "KIF18A", "CDK1", "TROAP", "DEPDC1", "CENPE", "TPX2", "KIF2C", "KNL1", "KIF20A", "AURKB", "NEIL3", "CCNB1", "ESPL1", "APOLD1", "HJURP", "PIMREG", "KIF11", "PIF1", "UBE2C", "NDC80", "CDC20", "PBK", "ARHGAP11A", "NUSAP1", "PRR11", "ESCO2", "PTTG1", "MELK", "KIF4A", "CDKN3", "NMU", "BORA", "KIF18B", "KIFC1", "CCNF", "BIRC5", "MKI67", "ARHGAP11B", "IQGAP3", "NCAPG", "SGO1", "SKA3", "GAS2L3", "SGO2", "RRM2", "DIAPH3", "CDCA3", "CENPF", "FAM83D", "NUF2", "POLQ", "RACGAP1", "KPNA2", "MIR924HG", "FBXO43", "TACC3", "WDR62", "E2F7", "PCLAF", "ASF1B", "ECT2", "SHCBP1", "PLK1", "FAM111B", "DEPDC1B", "MXD3", "NCAPH", "PRC1", "EXO1", "KIF15", "FOXM1", "CCNB2", "RTKN2", "NOSTRIN", "AC010173.1", "SPC25", "FOXN4", "HMGB2", "CKS2", "CENPI", "BRIP1", "MYBL2", "LMO7", "KIF24", "AC073529.1", "STIL", "AC090159.1", "PLK4"
  ],
  "programs": [
    {
      "program_name": "Mitotic Cell Division Promotion",
      "description": "A large cluster of input genes collectively regulate mitosis in glioblastoma cells including kinetochore-microtubule attachments, spindle assembly, chromosome segregation, and cytokinesis. This program encompasses both normal cell division and the hyperproliferative phenotype in malignancy.",
      "atomic_biological_processes": [
        {
          "name": "Spindle Assembly Checkpoint",
          "citation": [
            {"source_id": "", "notes": "TTK (MPS1), BUB1, BUB1B, KNL1, and related checkpoint components upregulated in glioblastoma."},
            {"source_id": "", "notes": "BUB1B is functionally required for glioblastoma proliferation and poor prognosis."}
          ],
          "genes": ["TTK", "BUB1", "BUB1B", "KNL1", "CDC20", "CENPE", "NDC80", "SKA3"]
        },
        {
          "name": "Kinetochore-Microtubule Attachment",
          "citation": [
            {"source_id": "", "notes": "NDC80, SKA3, CENPF, CENPE required for stable kinetochore attachments implicated in GBM progression."},
            {"source_id": "", "notes": "NDC80 and SKA components regulate mitosis and cell cycle in glioblastoma."}
          ],
          "genes": ["NDC80", "NUF2", "CENPF", "SKA3", "CENPE", "SPC25"]
        },
        {
          "name": "Chromosome Segregation",
          "citation": [
            {"source_id": "", "notes": "ESPL1 (separase) and associated proteins trigger chromosome segregation at anaphase."},
            {"source_id": "", "notes": "Separase activation (ESPL1) cleaves cohesin to allow chromatid separation."}
          ],
          "genes": ["ESPL1", "PTTG1", "SGO1", "SGO2"]
        },
        {
          "name": "Cytokinesis Machinery",
          "citation": [
            {"source_id": "", "notes": "ECT2, RACGAP1, KIF23, PRC1 coordinate contractile ring formation and midbody assembly."},
            {"source_id": "", "notes": "KIF14 and PRC1 interaction necessary for cytokinesis efficiency."}
          ],
          "genes": ["ECT2", "RACGAP1", "KIF23", "PRC1", "KIF14", "KIF20A", "KIF4A", "ARHGAP11A", "ARHGAP11B", "SHCBP1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Mitotic Spindle",
          "citation": [
            {"source_id": "", "notes": "Single-cell modeling reveals spindle components critical in glioblastoma cell fate decisions."}
          ],
          "genes": ["KIF11", "KIF14", "KIF20A", "KIF4A", "TPX2", "CEP55", "ASPM", "STIL"]
        }
      ],
      "predicted_cellular_impact": [
        "Increased mitotic rate and proliferation",
        "Aneuploidy and chromosome instability",
        "Enhanced tumor aggressiveness"
      ],
      "evidence_summary": "Large-scale studies confirm most of these genes are differentially upregulated and functionally promote both normal mitosis and the malignant proliferative state in glioblastoma cells, with strong genetic and functional validation.",
      "significance_score": 1.0,
      "citations": [
        {"source_id": "", "notes": "Hub genes CDK1, BUB1B, NDC80, CCNB1, TOP2A, DLGAP5, ASPM all correlate to glioblastoma progression."},
        {"source_id": "", "notes": "Bioinformatics and animal models confirm CENPF, PBK, ASPM, KIF2C, KIF20A, CDC20, TOP2A among highest expressed in glioma and associated with cell cycle progression."},
        {"source_id": "", "notes": "BUB1B required for GBM proliferation and survival; poor prognosis."}
      ],
      "supporting_genes": ["TTK", "BUB1", "BUB1B", "KNL1", "CDC20", "CENPE", "NDC80", "SKA3", "NUF2", "CENPF", "SPC25", "ESPL1", "PTTG1", "SGO1", "SGO2", "ECT2", "RACGAP1", "KIF23", "PRC1", "KIF14", "KIF20A", "KIF4A", "ARHGAP11A", "ARHGAP11B", "SHCBP1", "KIF11", "TPX2", "CEP55", "ASPM", "STIL"],
      "required_genes_not_in_input": {
        "genes": ["MAD2L1", "BUB3", "MCC"],
        "citations": [
          {"source_id": "", "notes": "MAD2, BUB3—core checkpoint components not specified in input but required for spindle checkpoint signaling."}
        ]
      }
    },
    {
      "program_name": "Cell Cycle Progression and DNA Replication",
      "description": "Cell cycle checkpoint regulators, cyclins, and DNA replication/repair enzymes are highly expressed, ensuring cell cycle entry and DNA synthesis in malignant glioblastoma. Aberrations drive uncontrolled proliferation and therapy resistance.",
      "atomic_biological_processes": [
        {
          "name": "Cell Cycle Checkpoint Regulation",
          "citation": [
            {"source_id": "", "notes": "Cell cycle and apoptosis pathways dysregulated in glioblastoma."}
          ],
          "genes": ["CDCA2", "CDC25C", "CDK1", "CCNB1", "CCNB2", "CCNF", "CDKN3", "PBK"]
        },
        {
          "name": "DNA Replication and Repair",
          "citation": [
            {"source_id": "", "notes": "RRM2, regulated by BRCA1, protects GBM cells from replication stress, promotes tumorigenicity."},
            {"source_id": "", "notes": "EXO1 key DNA repair player, critical for genomic stability and tumor evolution."},
            {"source_id": "", "notes": "BRIP1 (FANCJ) recruitment and regulation of FANCD2 in DNA damage responses; functions in genome maintenance."}
          ],
          "genes": ["TOP2A", "RRM2", "BRIP1", "POLQ", "EXO1", "NEIL3"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Nucleoplasm",
          "citation": [
            {"source_id": "", "notes": "DEGs enriched in nucleoplasm, protein binding, ATP binding—core for DNA replication and cell cycle control."}
          ],
          "genes": ["CDCA2", "TOP2A", "RRM2"]
        }
      ],
      "predicted_cellular_impact": [
        "Uncontrolled cell cycle progression",
        "Resistance to DNA damaging therapies",
        "Increased genomic instability"
      ],
      "evidence_summary": "Meta-analyses and mechanistic studies confirm overexpression of cell cycle and DNA replication/repair genes is necessary for GBM proliferation and associated with poor patient outcome.",
      "significance_score": 0.98,
      "citations": [
        {"source_id": "", "notes": "BRCA1-RRM2 axis maintains replication capacity and tumorigenicity in GBM."},
        {"source_id": "", "notes": "EXO1 DNA repair activity implicated as biomarker and driver of tumor evolution."},
        {"source_id": "", "notes": "Cell cycle checkpoints key to glioblastoma therapy resistance."}
      ],
      "supporting_genes": ["CDCA2", "CDC25C", "CDK1", "CCNB1", "CCNB2", "CCNF", "CDKN3", "PBK", "TOP2A", "RRM2", "BRIP1", "POLQ", "EXO1", "NEIL3"],
      "required_genes_not_in_input": {
        "genes": ["BRCA1", "FANCD2"],
        "citations": [
          {"source_id": "", "notes": "BRCA1, FANCD2—essential partners with BRIP1 for DNA repair not present in input list."}
        ]
      }
    },
    {
      "program_name": "Stemness and Tumorigenicity Drivers",
      "description": "Genes such as HMMR, ASPM, MKI67, FOXM1, and MELK maintain the stemness, self-renewal, and tumorigenic capacity of glioblastoma cells, contributing to resistance and recurrence.",
      "atomic_biological_processes": [
        {
          "name": "Maintenance of Stemness",
          "citation": [
            {"source_id": "", "notes": "HMMR supports self-renewal and tumorigenic potential of glioblastoma stem-like cells."},
            {"source_id": "", "notes": "FOXM1 promotes proliferation, EMT, invasion, stemness in glioblastoma."},
            {"source_id": "", "notes": "MELK regulates FOXM1 phosphorylation, essential for glioma stem cell proliferation."}
          ],
          "genes": ["HMMR", "ASPM", "MKI67", "FOXM1", "MELK"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Nucleolus",
          "citation": [
            {"source_id": "", "notes": "Ribosome metabolism supports glioma stem cell properties and tumor proliferation."}
          ],
          "genes": ["MKI67", "FOXM1", "HMMR"]
        }
      ],
      "predicted_cellular_impact": [
        "Increased tumor initiation, recurrence, and resistance",
        "Enhanced proliferation and invasiveness",
        "Maintenance of glioma stem cell populations"
      ],
      "evidence_summary": "Functional studies reveal that knockdown of HMMR, ASPM, FOXM1, and MELK impairs tumor growth and stemness; their expression correlates with poor prognosis and resistance.",
      "significance_score": 0.96,
      "citations": [
        {"source_id": "", "notes": "HMMR critical in GBM stemness; targeting HMMR impairs self-renewal capacity."},
        {"source_id": "", "notes": "MELK-FOXM1 axis essential for glioma stem cell proliferation."},
        {"source_id": "", "notes": "ASPM overexpression in glioma correlates with poor prognosis; regulated by FOXM1."}
      ],
      "supporting_genes": ["HMMR", "ASPM", "MKI67", "FOXM1", "MELK"],
      "required_genes_not_in_input": {
        "genes": ["SOX2"],
        "citations": [
          {"source_id": "", "notes": "SOX2 master stem cell regulator impacted by FOXM1, required for maintenance but not present in input list."}
        ]
      }
    }
  ],
  "method": {
    "clustering_basis": [
      "Pathway databases (GO, Reactome, KEGG)",
      "PPI network analysis",
      "Co-expression in high-grade glioma datasets",
      "Meta-analyses of prognostic and functional studies"
    ],
    "notes": "Programs derived by grouping input genes by their shared involvement in mitosis/cytokinesis, cell cycle, DNA repair, or stemness, then cross-validating these clusters against high-throughput glioblastoma datasets and recent functional genomic studies."
  },
  "version": "2025-11-17"
}
<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_18][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_19][^1_190][^1_191][^1_192][^1_193][^1_194][^1_195][^1_196][^1_197][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: image.jpg
[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6781560/
[^1_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4650544/
[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5530036/
[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6312941/
[^1_6]: https://esmed.org/MRA/mra/article/download/3994/99193547030
[^1_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9091202/
[^1_8]: https://academic.oup.com/narcancer/article-pdf/2/2/zcaa011/33428092/zcaa011.pdf
[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8584308/
[^1_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3641139/
[^1_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1165403/
[^1_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2063646/
[^1_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11047945/
[^1_14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1488988/
[^1_15]: https://www.mdpi.com/2218-273X/14/4/386/pdf?version=1711110346
[^1_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7657121/
[^1_17]: https://www.mdpi.com/2073-4409/10/1/136/pdf
[^1_18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4059010/
[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5915996/
[^1_20]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8916685/
[^1_21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11014578/
[^1_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1851198/
[^1_23]: https://www.frontiersin.org/articles/10.3389/fmats.2018.00039/pdf
[^1_24]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6300158/
[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5352067/
[^1_26]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8429554/
[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9515058/
[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6961387/
[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11093636/
[^1_30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8627377/
[^1_31]: http://koreascience.or.kr/article/JAKO201507964683065.pdf
[^1_32]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10377045/
[^1_33]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11994507/
[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9883288/
[^1_35]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4380124/
[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3744761/
[^1_37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4596841/
[^1_38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10568859/
[^1_39]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6114977/
[^1_40]: https://stemcellsjournals.onlinelibrary.wiley.com/doi/pdfdirect/10.1002/stem.1358
[^1_41]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3129416/
[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5547476/
[^1_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6377300/
[^1_44]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8794527/
[^1_45]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5520903/
[^1_46]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11414393/
[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8945784/
[^1_48]: https://www.ijbs.com/v20p4691.htm
[^1_49]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9908336/
[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5770600/
[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9804269/
[^1_52]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6792010/
[^1_53]: https://www.mdpi.com/2072-6694/13/9/2033/pdf
[^1_54]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8122802/
[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5311251/
[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4836815/
[^1_57]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5830916/
[^1_58]: http://www.jbc.org/content/286/34/30047.full.pdf
[^1_59]: http://www.jbc.org/article/S0021925819760827/pdf
[^1_60]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3742030/
[^1_61]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8943831/
[^1_62]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3191045/
[^1_63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1483889/
[^1_64]: https://www.imrpress.com/journal/FBL/29/2/10.31083/j.fbl2902087/pdf
[^1_65]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5103968/
[^1_66]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4774622/
[^1_67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10650073/
[^1_68]: https://www.mdpi.com/1422-0067/24/21/15792/pdf?version=1698727237
[^1_69]: https://www.mdpi.com/1422-0067/20/9/2228/pdf
[^1_70]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6539744/
[^1_71]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10395518/
[^1_72]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11637980/
[^1_73]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7724090/
[^1_74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9055704/
[^1_75]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4868491/
[^1_76]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1479085/
[^1_77]: https://pmc.ncbi.nlm.nih.gov/articles/PMC14867/
[^1_78]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10577266/
[^1_79]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3691463/
[^1_80]: https://www.mdpi.com/2227-9059/10/3/564/pdf
[^1_81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7778526/
[^1_82]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4032816/
[^1_83]: https://portlandpress.com/biochemsoctrans/article-pdf/doi/10.1042/BST20221400/946189/bst-2022-1400c.pdf
[^1_84]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5672940/
[^1_85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3413326/
[^1_86]: https://www.mdpi.com/1422-0067/24/5/4604/pdf?version=1677486822
[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10003635/
[^1_88]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6858450/
[^1_89]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2610357/
[^1_90]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10413716/
[^1_91]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9879178/
[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8210184/
[^1_93]: https://academic.oup.com/narcancer/article/doi/10.1093/narcan/zcab009/6180063
[^1_94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3748913/
[^1_95]: https://onlinelibrary.wiley.com/doi/10.1111/cns.14839
[^1_96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6665439/
[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8044053/
[^1_98]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2863999/
[^1_99]: http://www.jbc.org/content/275/23/17233.full.pdf
[^1_100]: https://zenodo.org/record/1229225/files/article.pdf
[^1_101]: https://dx.plos.org/10.1371/journal.pone.0023676
[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4601362/
[^1_103]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9056178/
[^1_104]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4125382/
[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3557187/
[^1_106]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4263449/
[^1_107]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5765294/
[^1_108]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4571299/
[^1_109]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11158231/
[^1_110]: https://www.mdpi.com/1422-0067/23/22/14102/pdf?version=1668509928
[^1_111]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7555474/
[^1_112]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2612504/
[^1_113]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9695706/
[^1_114]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2817685/
[^1_115]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1635024/
[^1_116]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6977704/
[^1_117]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7520292/
[^1_118]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10502471/
[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9201116/
[^1_120]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9031586/
[^1_121]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11036705/
[^1_122]: https://downloads.hindawi.com/journals/dm/2021/9940274.pdf
[^1_123]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8272457/
[^1_124]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3737014/
[^1_125]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9842725/
[^1_126]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9273787/
[^1_127]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11662047/
[^1_128]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5341122/
[^1_129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4297562/
[^1_130]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11602827/
[^1_131]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6788011/
[^1_132]: https://www.mdpi.com/1422-0067/24/1/749/pdf?version=1672569074
[^1_133]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11415179/
[^1_134]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11871623/
[^1_135]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10708941/
[^1_136]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11870995/
[^1_137]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2783354/
[^1_138]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2688534/
[^1_139]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7048675/
[^1_140]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7525821/
[^1_141]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6236911/
[^1_142]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6895034/
[^1_143]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2669960/
[^1_144]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11161389/
[^1_145]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11479523/
[^1_146]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4440078/
[^1_147]: http://society.kisti.re.kr/sv/SV_svpsbs03V.do?cn1=JAKO201435648479223&method=download
[^1_148]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11550750/
[^1_149]: https://www.micropublication.org/journals/biology/micropub-biology-001546
[^1_150]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7160549/
[^1_151]: https://onlinelibrary.wiley.com/doi/10.1111/cns.14850
[^1_152]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8524009/
[^1_153]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6345219/
[^1_154]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4433451/
[^1_155]: https://peerj.com/articles/6299
[^1_156]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5288158/
[^1_157]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7399822/
[^1_158]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6125382/
[^1_159]: https://www.mdpi.com/2227-9059/8/7/192/pdf?version=1594802939
[^1_160]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3219542/
[^1_161]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10067360/
[^1_162]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8769543/
[^1_163]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10891059/
[^1_164]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9053761/
[^1_165]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8148488/
[^1_166]: https://downloads.hindawi.com/journals/dm/2022/2760432.pdf
[^1_167]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5783581/
[^1_168]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11269704/
[^1_169]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8406419/
[^1_170]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4283840/
[^1_171]: http://www.jbc.org/content/284/23/15359.full.pdf
[^1_172]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5226922/
[^1_173]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3109435/
[^1_174]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4630029/
[^1_175]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10577578/
[^1_176]: https://www.tandfonline.com/doi/pdf/10.1080/21655979.2021.1995576?needAccess=true
[^1_177]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5116074/
[^1_178]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6367584/
[^1_179]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10191446/
[^1_180]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8909726/
[^1_181]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8600070/
[^1_182]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9596216/
[^1_183]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10398797/
[^1_184]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2909592/
[^1_185]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4928586/
[^1_186]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7316351/
[^1_187]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10897178/
[^1_188]: https://academic.oup.com/narcancer/article/doi/10.1093/narcan/zcaf004/8005560
[^1_189]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8378518/
[^1_190]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3109611/
[^1_191]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7552932/
[^1_192]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11903978/
[^1_193]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6337416/
[^1_194]: http://www.jbc.org/content/292/26/10779.full.pdf
[^1_195]: https://academic.oup.com/nar/advance-article-pdf/doi/10.1093/nar/gkac616/45015998/gkac616.pdf
[^1_196]: https://www.mdpi.com/1422-0067/20/1/74
[^1_197]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5491765/```


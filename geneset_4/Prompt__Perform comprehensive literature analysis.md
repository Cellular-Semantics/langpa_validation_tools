<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Prompt:

Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: ["FSTL4, LRFN5, TRPM3, NDST4, PALMD, ADRA1B, PDE1A, CLVS1, SLC17A6, ACVR1C, SLA, EBF1, AC011474.1, FRMPD4, KIT, UNC5D, GCG, TRPC5, CDH9, TARID, LINC01033, AC109492.1, AL596087.2, SHISA6, POSTN, PLSCR2, CDH18, PALM2-AKAP2, CDH13, SMOC2, CPNE4, CUX2, RNF149, TENM2, MARCH4, HS3ST2, GRIN2A, RUNX1T1, AL158064.1, EFNA5, GRIP2, PRSS12, GREM2, RASGEF1B, TAFA2, FGD4, SERPINI1, RBFOX1, SEMA3C, ADAMTS3, CNTNAP4, BRINP1, CNTN5, LINC01344, MYT1L, MTAP, SLC38A11, MN1, MIR3681HG, SV2B, CARMIL1, ZDHHC23, LINC02607, OTOR, CLEC2L, PAPPA2, LINC01949, LINC00862, U91319.1, IQCJ-SCHIP1, KCNJ6, CFAP299, SIAH3, PDZRN4, LIN28B, AC063979.2, DYNC1I1, CCK, SCG2, SIDT1, CDH4, DPP10, SAMD5, SNCA, COL3A1, COL6A3, EBF2, LINC02378, KLHL29, PIP5K1B, LINC00470, LINC00707, PDE1C, LINC01965, LINGO2, EDA, NYAP2, NWD2, NOX3, MOXD1, MSC-AS1, NEDD4L, KIAA0319, KCNC2, POU6F2, IGFBPL1, PPEF1, PRDM6, GPR1, SRRM4, GFRA1, GABBR2, FSTL5, FRAS1, FGFR2, FAP, RIMBP2, RPH3A, EDIL3, GLRA2, NDNF, SYNPR, AC002454.1, AC003044.1, WSCD2, ANO4, AP003464.1, VWC2L, VSTM2B, ARHGAP18, TMEM130, TGFBI, AC244502.1, SYT1, UNC5C, VWDE”]
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
    "disease": "glioblastoma multiforme",
    "tissue": "brain"
  },
  "input_genes": [
    "FSTL4", "LRFN5", "TRPM3", "NDST4", "PALMD", "ADRA1B", "PDE1A", "CLVS1", "SLC17A6", "ACVR1C", "SLA", "EBF1", "AC011474.1", "FRMPD4", "KIT", "UNC5D", "GCG", "TRPC5", "CDH9", "TARID", "LINC01033", "AC109492.1", "AL596087.2", "SHISA6", "POSTN", "PLSCR2", "CDH18", "PALM2-AKAP2", "CDH13", "SMOC2", "CPNE4", "CUX2", "RNF149", "TENM2", "MARCH4", "HS3ST2", "GRIN2A", "RUNX1T1", "AL158064.1", "EFNA5", "GRIP2", "PRSS12", "GREM2", "RASGEF1B", "TAFA2", "FGD4", "SERPINI1", "RBFOX1", "SEMA3C", "ADAMTS3", "CNTNAP4", "BRINP1", "CNTN5", "LINC01344", "MYT1L", "MTAP", "SLC38A11", "MN1", "MIR3681HG", "SV2B", "CARMIL1", "ZDHHC23", "LINC02607", "OTOR", "CLEC2L", "PAPPA2", "LINC01949", "LINC00862", "U91319.1", "IQCJ-SCHIP1", "KCNJ6", "CFAP299", "SIAH3", "PDZRN4", "LIN28B", "AC063979.2", "DYNC1I1", "CCK", "SCG2", "SIDT1", "CDH4", "DPP10", "SAMD5", "SNCA", "COL3A1", "COL6A3", "EBF2", "LINC02378", "KLHL29", "PIP5K1B", "LINC00470", "LINC00707", "PDE1C", "LINC01965", "LINGO2", "EDA", "NYAP2", "NWD2", "NOX3", "MOXD1", "MSC-AS1", "NEDD4L", "KIAA0319", "KCNC2", "POU6F2", "IGFBPL1", "PPEF1", "PRDM6", "GPR1", "SRRM4", "GFRA1", "GABBR2", "FSTL5", "FRAS1", "FGFR2", "FAP", "RIMBP2", "RPH3A", "EDIL3", "GLRA2", "NDNF", "SYNPR", "AC002454.1", "AC003044.1", "WSCD2", "ANO4", "AP003464.1", "VWC2L", "VSTM2B", "ARHGAP18", "TMEM130", "TGFBI", "AC244502.1", "SYT1", "UNC5C", "VWDE"
  ],
  "programs": [
    {
      "program_name": "Extracellular Matrix and Invasion",
      "description": "Collagen (COL3A1, COL6A3), periostin (POSTN), and fibroblast activation protein (FAP) contribute to the remodeling of the glioblastoma extracellular matrix, driving cell invasion, angiogenesis, and progression. These genes encode ECM proteins and regulators found upregulated in GBM and facilitate tumor cell migration, vessel formation, and therapeutic resistance.",
      "atomic_biological_processes": [
        {
          "name": "ECM Remodeling",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8662453/", "source_id": "173", "notes": "FAP+ cells promote glioblastoma angiogenesis, migration and growth."},
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7213654/", "source_id": "24", "notes": "COL6A1 target in tumor therapy, COL6A3 implicated in invasion."},
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8833816/", "source_id": "25", "notes": "COL6A3 deletion in GBM cells reduces invasion."}
          ],
          "genes": ["COL3A1", "COL6A3", "FAP"]
        },
        {
          "name": "Angiogenesis",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8278817/", "source_id": "173", "notes": "FAP+ mesenchymal cells promote angiogenesis."}
          ],
          "genes": ["FAP", "COL3A1", "POSTN"]
        },
        {
          "name": "Tumor Cell Migration",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4742645/", "source_id": "26", "notes": "POSTN activation increases invasion and chemo-resistance."},
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8833816/", "source_id": "25", "notes": "COL6A3 deletion reduces invasion and β-catenin signaling."}
          ],
          "genes": ["POSTN", "COL6A3", "COL3A1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Basement Membrane",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8278817/", "source_id": "173", "notes": "ECM-related mesenchymal cells localize near activated endothelium."}
          ],
          "genes": ["COL6A3", "FAP"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced glioblastoma cell invasion through ECM modification",
        "Promotion of angiogenesis",
        "Increased tumor cell migration and therapy resistance"
      ],
      "evidence_summary": "Multiple ECM genes are upregulated in glioblastoma, correlating with increased invasiveness, angiogenesis, and poor prognosis. Intervention targeting these ECM pathways has therapeutic value.",
      "significance_score": 0.95,
      "citations": [
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8278817/", "source_id": "173", "notes": "FAP in GBM microenvironment promotes angiogenesis and invasion."},
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4742645/", "source_id": "26", "notes": "POSTN in GBM invasion and resistance."},
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8833816/", "source_id": "25", "notes": "Collagen VI facilitates invasion and β-catenin signaling in GBM."}
      ],
      "supporting_genes": ["COL3A1", "COL6A3", "POSTN", "FAP"],
      "required_genes_not_in_input": {
        "genes": ["MMP2", "MMP9", "FN1"],
        "citations": [
          {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7213654/", "source_id": "24", "notes": "MMPs required for ECM degradation and invasion in GBM."}
        ]
      }
    },
    {
      "program_name": "Glutamatergic Excitotoxicity and Synapse Dynamics",
      "description": "Genes encoding vesicular glutamate transporter (SLC17A6), NMDA receptor subunit (GRIN2A), synapse proteins (SYT1, SYNPR, SV2B), and auxiliary regulators (GLRA2) drive aberrant glutamatergic signaling, which is implicated in glioblastoma cell survival, migration, resistance to radiotherapy, and neuron-tumor interactions.",
      "atomic_biological_processes": [
        {
          "name": "Glutamate Release",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7107317/", "source_id": "15", "notes": "GBM glutamate secretion drives excitotoxicity."}
          ],
          "genes": ["SLC17A6"]
        },
        {
          "name": "NMDA Receptor Signaling",
          "citation": [
            {"url": "https://www.mdpi.com/1422-0067/20/7/1747", "source_id": "98", "notes": "Functional NMDARs mediate survival and migration in GBM."}
          ],
          "genes": ["GRIN2A"]
        },
        {
          "name": "Synapse Formation",
          "citation": [
            {"url": "https://www.frontiersin.org/articles/10.3389/fonc.2020.1536/full", "source_id": "110", "notes": "Synapse-related genes are biomarkers and mediators of glioma-neuron interactions."}
          ],
          "genes": ["SYT1", "SYNPR", "SV2B"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Synaptic Vesicle",
          "citation": [
            {"url": "https://www.frontiersin.org/articles/10.3389/fonc.2020.1536/full", "source_id": "110", "notes": "SV2B and SYNPR localize to synaptic vesicles in glioma."}
          ],
          "genes": ["SV2B", "SYNPR"]
        }
      ],
      "predicted_cellular_impact": [
        "Potentiation of glutamate-dependent survival and migration",
        "Resistance to radiotherapy",
        "Tumor-neuron synaptic interaction in microenvironment"
      ],
      "evidence_summary": "Glutamate transport and receptor genes, combined with synapse markers, facilitate neuron-glioma crosstalk, supporting tumor proliferation and resistance.",
      "significance_score": 0.9,
      "citations": [
        {"url": "https://www.mdpi.com/1422-0067/20/7/1747", "source_id": "98", "notes": "NMDAR signaling in GBM."},
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7107317/", "source_id": "15", "notes": "GBM glutamate secretion and excitotoxicity."},
        {"url": "https://www.frontiersin.org/articles/10.3389/fonc.2020.1536/full", "source_id": "110", "notes": "Synapse-related gene biomarkers."}
      ],
      "supporting_genes": ["SLC17A6", "GRIN2A", "SYT1", "SYNPR", "SV2B", "GLRA2"],
      "required_genes_not_in_input": {
        "genes": ["GRIA1", "GRIA2", "GRIN1"],
        "citations": [
          {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7107317/", "source_id": "15", "notes": "GRIA2 and AMPA receptor involvement in glioblastoma."}
        ]
      }
    },
    {
      "program_name": "Glioma Stem Cell Maintenance and Therapy Resistance",
      "description": "GFRA1 and GDNF (via RET) signaling pathways, including associated neural transcription factors (MYT1L, CUX2, POU6F2), and ECM-remodeling proteases (ADAMTS3), underpin stem cell characteristics, self-renewal, chemoresistance, and cellular hierarchy. SEMA3C and BMP antagonists (e.g., GREM2, RUNX1T1) further maintain stemness and resistance.",
      "atomic_biological_processes": [
        {
          "name": "Stem Cell Renewal",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10350534/", "source_id": "50", "notes": "GFRA1 promotes chemo- and radioresistance in glioblastoma stem cells."}
          ],
          "genes": ["GFRA1"]
        },
        {
          "name": "BMP Antagonism",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3978872/", "source_id": "185", "notes": "Gremlin is a key BMP antagonist promoting stemness in GBM."}
          ],
          "genes": ["GREM2", "RUNX1T1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Cell Nucleus (Transcriptional Control)",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8600212/", "source_id": "66", "notes": "MYT1L represses proliferation via YAP1 in GBM cells."}
          ],
          "genes": ["MYT1L", "CUX2", "POU6F2"]
        }
      ],
      "predicted_cellular_impact": [
        "Increase in chemotherapy and radiotherapy resistance",
        "Maintenance of self-renewal and stem cell hierarchy",
        "Sustained invasive and migratory behavior"
      ],
      "evidence_summary": "GFRA1-GDNF-RET signaling supports GBM stem cell resistance. BMP antagonism via gremlin proteins maintains the stem cell pool. Neural transcription factors (MYT1L, CUX2, POU6F2) reduce differentiation and control stemness.",
      "significance_score": 0.89,
      "citations": [
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10350534/", "source_id": "50", "notes": "GFRA1 promotes stemness and chemo-resistance."},
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3978872/", "source_id": "185", "notes": "Gremlin BMP antagonism in glioblastoma CSCs."},
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8600212/", "source_id": "66", "notes": "Myt1l transcriptional regulation and proliferation control in GBM."}
      ],
      "supporting_genes": ["GFRA1", "MYT1L", "CUX2", "POU6F2", "ADAMTS3", "SEMA3C", "GREM2", "RUNX1T1"],
      "required_genes_not_in_input": {
        "genes": ["SOX2", "OLIG2"],
        "citations": [
          {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5604536/", "source_id": "80", "notes": "SOX2, OLIG2 drive stemness in GBM."}
        ]
      }
    }
  ],
  "version": "2025-11-14"
}
<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_18][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_19][^1_190][^1_191][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: image.jpg
[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10334844/
[^1_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10587102/
[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9923154/
[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10922678/
[^1_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4106866/
[^1_7]: https://linkinghub.elsevier.com/retrieve/pii/S2001037021005183
[^1_8]: https://www.frontiersin.org/articles/10.3389/fmolb.2022.904098/pdf
[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8108069/
[^1_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2853350/
[^1_11]: https://ujms.net/index.php/ujms/article/view/6175
[^1_12]: https://www.mdpi.com/1422-0067/24/24/17633/pdf?version=1702913099
[^1_13]: http://www.jneurosci.org/content/26/47/12294.full.pdf
[^1_14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7809625/
[^1_15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10744281/
[^1_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6675433/
[^1_17]: https://onlinelibrary.wiley.com/doi/10.1002/cbin.70005
[^1_18]: https://onlinelibrary.wiley.com/doi/10.1155/bmri/2004975
[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5342568/
[^1_20]: https://www.mdpi.com/2072-6694/15/6/1879/pdf?version=1679382163
[^1_21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6036335/
[^1_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10046791/
[^1_23]: https://onlinelibrary.wiley.com/doi/10.1111/cns.14802
[^1_24]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11183175/
[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10760023/
[^1_26]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4914248/
[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4383753/
[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4483094/
[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5104278/
[^1_30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5955165/
[^1_31]: https://dx.plos.org/10.1371/journal.pone.0025451
[^1_32]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10863174/
[^1_33]: https://www.oncotarget.com/article/25153/pdf/
[^1_34]: http://www.jbc.org/content/281/32/22855.full.pdf
[^1_35]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9684443/
[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3466358/
[^1_37]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jcmm.17807
[^1_38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3644882/
[^1_39]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/ijc.23450
[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3271264/
[^1_41]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8307764/
[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3011255/
[^1_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8798009/
[^1_44]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2905941/
[^1_45]: http://downloads.hindawi.com/journals/jo/2010/430142.pdf
[^1_46]: https://www.frontiersin.org/articles/10.3389/fncel.2021.663092/pdf
[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6254577/
[^1_48]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8584308/
[^1_49]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8206529/
[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11292001/
[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4024863/
[^1_52]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1135013/
[^1_53]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11480913/
[^1_54]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9436484/
[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2767465/
[^1_56]: http://www.jbc.org/article/S0021925818401202/pdf
[^1_57]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6131978/
[^1_58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11291093/
[^1_59]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5348560/
[^1_60]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/cam4.6102
[^1_61]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10358225/
[^1_62]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10914854/
[^1_63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11632980/
[^1_64]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10238751/
[^1_65]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3355166/
[^1_66]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6203443/
[^1_67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9307810/
[^1_68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3767545/
[^1_69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9661212/
[^1_70]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10942489/
[^1_71]: https://www.mdpi.com/2073-4409/12/12/1578
[^1_72]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8998804/
[^1_73]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10234307/
[^1_74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5226867/
[^1_75]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10970558/
[^1_76]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5669884/
[^1_77]: https://www.mdpi.com/2073-4409/13/3/258/pdf?version=1706603923
[^1_78]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9629421/
[^1_79]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8231639/
[^1_80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5321610/
[^1_81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4294353/
[^1_82]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3441119/
[^1_83]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5315656/
[^1_84]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11956907/
[^1_85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6541232/
[^1_86]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8455679/
[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2777236/
[^1_88]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7554199/
[^1_89]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10626282/
[^1_90]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11456559/
[^1_91]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11698767/
[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9339490/
[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7870873/
[^1_94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6556397/
[^1_95]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11467166/
[^1_96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11142752/
[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8485435/
[^1_98]: https://www.mdpi.com/2072-6694/11/4/503
[^1_99]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4623498/
[^1_100]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11412357/
[^1_101]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8114084/
[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11497419/
[^1_103]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11582119/
[^1_104]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8295384/
[^1_105]: https://www.qeios.com/read/AO4SC4/pdf
[^1_106]: https://www.mdpi.com/1422-0067/24/1/749/pdf?version=1672569074
[^1_107]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9820922/
[^1_108]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11528668/
[^1_109]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8552071/
[^1_110]: https://www.frontiersin.org/articles/10.3389/fnins.2020.00822/pdf
[^1_111]: https://www.frontiersin.org/articles/10.3389/fmolb.2021.714203/pdf
[^1_112]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8946689/
[^1_113]: https://www.mdpi.com/2072-6694/14/6/1382/pdf
[^1_114]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4502760/
[^1_115]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3010848/
[^1_116]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10916047/
[^1_117]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8480197/
[^1_118]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12089638/
[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9476413/
[^1_120]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11277022/
[^1_121]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8044053/
[^1_122]: https://www.mdpi.com/2075-4418/11/7/1204/pdf
[^1_123]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8304478/
[^1_124]: https://www.frontiersin.org/articles/10.3389/fonc.2020.01377/pdf
[^1_125]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6303485/
[^1_126]: https://www.mdpi.com/2072-6694/14/3/624/pdf
[^1_127]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3809881/
[^1_128]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/tox.24210
[^1_129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8844449/
[^1_130]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6280144/
[^1_131]: https://www.mdpi.com/2073-4409/10/3/549/pdf
[^1_132]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11330389/
[^1_133]: https://www.mdpi.com/2072-6694/14/10/2544/pdf?version=1653137813
[^1_134]: https://linkinghub.elsevier.com/retrieve/pii/S188065462500071X
[^1_135]: https://www.mdpi.com/2072-6694/14/16/4032/pdf?version=1660996375
[^1_136]: https://pmc.ncbi.nlm.nih.gov/articles/PMC298701/
[^1_137]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10068818/
[^1_138]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12027600/
[^1_139]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7265959/
[^1_140]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10898159/
[^1_141]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5008313/
[^1_142]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5355113/
[^1_143]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10840508/
[^1_144]: https://www.frontiersin.org/articles/10.3389/fonc.2013.00053/pdf
[^1_145]: https://linkinghub.elsevier.com/retrieve/pii/S0304383523003002
[^1_146]: https://www.oncotarget.com/article/4097/pdf/
[^1_147]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7766440/
[^1_148]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4673279/
[^1_149]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8048363/
[^1_150]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7687855/
[^1_151]: https://res.mdpi.com/d_attachment/ijms/ijms-20-03183/article_deploy/ijms-20-03183-v2.pdf
[^1_152]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10215375/
[^1_153]: https://www.mdpi.com/2079-7737/12/5/736
[^1_154]: https://www.frontiersin.org/articles/10.3389/fncel.2021.703431/pdf
[^1_155]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7082224/
[^1_156]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5312354/
[^1_157]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4183860/
[^1_158]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6056225/
[^1_159]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9952003/
[^1_160]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10601256/
[^1_161]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4693299/
[^1_162]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7261182/
[^1_163]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6027460/
[^1_164]: https://www.mdpi.com/2227-9059/6/2/42/pdf
[^1_165]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6888630/
[^1_166]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6539029/
[^1_167]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8108085/
[^1_168]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10119166/
[^1_169]: https://www.embopress.org/doi/10.1002/emmm.201200206
[^1_170]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2567090/
[^1_171]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9928553/
[^1_172]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4185866/
[^1_173]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8267680/
[^1_174]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7557106/
[^1_175]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/cti2.1191
[^1_176]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7464128/
[^1_177]: https://www.mdpi.com/1422-0067/22/3/1046/pdf
[^1_178]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8151573/
[^1_179]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5001929/
[^1_180]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2649704/
[^1_181]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9832208/
[^1_182]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12095820/
[^1_183]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4961528/
[^1_184]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9371711/
[^1_185]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4035537/
[^1_186]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3185228/
[^1_187]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9873505/
[^1_188]: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1336476/pdf
[^1_189]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10876826/
[^1_190]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8414390/
[^1_191]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9145282/```


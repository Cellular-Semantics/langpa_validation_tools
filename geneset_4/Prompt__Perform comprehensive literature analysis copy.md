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
    "cell_type": "malignant glioblastoma cells",
    "disease": "glioblastoma",
    "tissue": "brain"
  },
  "input_genes": [
    "FSTL4", "LRFN5", "TRPM3", "NDST4", "PALMD", "ADRA1B", "PDE1A", "CLVS1", "SLC17A6", "ACVR1C", "SLA", "EBF1", "AC011474.1", "FRMPD4", "KIT", "UNC5D", "GCG", "TRPC5", "CDH9", "TARID", "LINC01033", "AC109492.1", "AL596087.2", "SHISA6", "POSTN", "PLSCR2", "CDH18", "PALM2-AKAP2", "CDH13", "SMOC2", "CPNE4", "CUX2", "RNF149", "TENM2", "MARCH4", "HS3ST2", "GRIN2A", "RUNX1T1", "AL158064.1", "EFNA5", "GRIP2", "PRSS12", "GREM2", "RASGEF1B", "TAFA2", "FGD4", "SERPINI1", "RBFOX1", "SEMA3C", "ADAMTS3", "CNTNAP4", "BRINP1", "CNTN5", "LINC01344", "MYT1L", "MTAP", "SLC38A11", "MN1", "MIR3681HG", "SV2B", "CARMIL1", "ZDHHC23", "LINC02607", "OTOR", "CLEC2L", "PAPPA2", "LINC01949", "LINC00862", "U91319.1", "IQCJ-SCHIP1", "KCNJ6", "CFAP299", "SIAH3", "PDZRN4", "LIN28B", "AC063979.2", "DYNC1I1", "CCK", "SCG2", "SIDT1", "CDH4", "DPP10", "SAMD5", "SNCA", "COL3A1", "COL6A3", "EBF2", "LINC02378", "KLHL29", "PIP5K1B", "LINC00470", "LINC00707", "PDE1C", "LINC01965", "LINGO2", "EDA", "NYAP2", "NWD2", "NOX3", "MOXD1", "MSC-AS1", "NEDD4L", "KIAA0319", "KCNC2", "POU6F2", "IGFBPL1", "PPEF1", "PRDM6", "GPR1", "SRRM4", "GFRA1", "GABBR2", "FSTL5", "FRAS1", "FGFR2", "FAP", "RIMBP2", "RPH3A", "EDIL3", "GLRA2", "NDNF", "SYNPR", "AC002454.1", "AC003044.1", "WSCD2", "ANO4", "AP003464.1", "VWC2L", "VSTM2B", "ARHGAP18", "TMEM130", "TGFBI", "AC244502.1", "SYT1", "UNC5C", "VWDE"
  ],
  "programs": [
    {
      "program_name": "Extracellular Matrix Remodeling & Invasion",
      "description": "Enrichment for genes encoding ECM proteins, ECM remodelers and their regulators associated with glioblastoma cell invasion, mesenchymal transition, and tumor angiogenesis. Programs include collagen (COL3A1, COL6A3), periostin (POSTN), TGFBI, FAP, SMOC2, and multiple matrix metalloproteinases (ADAMTS3). Periostin and FAP+ mesenchymal cells promote active angiogenesis, abnormal vascular structure, and stemness.",
      "atomic_biological_processes": [
        {
          "name": "ECM remodeling",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10241737/", "source_id": "34", "notes": "Review of ECM role in glioblastoma progression and mechanisms."},
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9044776/", "source_id": "146", "notes": "FAP+ mesenchymal cells promote angiogenesis in glioblastoma."},
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9128179/", "source_id": "41", "notes": "COL6A3 essential for tumor invasion; knockdown reduces invasion."},
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6971284/", "source_id": "49", "notes": "POSTN marks glioma invasion and malignancy."}
          ],
          "genes": ["COL3A1", "COL6A3", "POSTN", "TGFBI", "FAP", "ECM-regulatory lncRNAs"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Tumor microenvironment: ECM",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10241737/", "source_id": "34"}
          ],
          "genes": ["COL3A1", "COL6A3", "POSTN", "FAP", "SMOC2", "TGFBI"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced invasion through remodeling of matrix",
        "Promotion of abnormal angiogenesis and vascular niche formation",
        "Increased tumor cell migration"
      ],
      "evidence_summary": "Multiple ECM proteins, their regulators (POSTN, FAP, TGFBI), and collagen-modifying enzymes are highly expressed in glioblastoma and strongly linked to increased invasion, angiogenesis, therapy resistance, and poor prognosis. Co-expression supports a coordinated ECM program.",
      "significance_score": 0.96,
      "citations": [
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10241737/", "source_id": "34"},
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9044776/", "source_id": "146"},
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9128179/", "source_id": "41"},
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6971284/", "source_id": "49"}
      ],
      "supporting_genes": ["COL3A1", "COL6A3", "POSTN", "TGFBI", "FAP", "SMOC2", "ADAMTS3", "FRAS1"],
      "required_genes_not_in_input": {
        "genes": ["MMP2", "MMP9", "LOX"],
        "citations": [
          {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9128179/", "source_id": "41"}
        ]
      }
    },
    {
      "program_name": "Glutamatergic & Synaptic Signaling Deregulation",
      "description": "Enrichment for vesicular glutamate transporters (SLC17A6), glutamate receptor components (GRIN2A), and synaptic proteins (SV2B, SYT1, RIMBP2). Tumors hijack glutamatergic synapses and signaling to promote invasion, hyperexcitability, and stem cell maintenance.",
      "atomic_biological_processes": [
        {
          "name": "Glutamate signaling",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4412924/", "source_id": "106", "notes": "Glioblastoma upregulates glutamatergic gene expression in tumor-associated microglia/macrophages."},
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8499409/", "source_id": "107", "notes": "Glutamate receptor expression drives tumor progression and excitotoxicity."}
          ],
          "genes": ["SLC17A6", "GRIN2A", "SV2B", "SYT1", "RIMBP2", "RPH3A"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Synaptic machinery",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8499409/", "source_id": "107"}
          ],
          "genes": ["SYT1", "SV2B", "RIMBP2", "RPH3A"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced glutamatergic signaling drives tumor proliferation and invasion",
        "Tumor-induced hyperexcitability and epileptogenesis",
        "Aberrant synaptic connectivity fosters glioblastoma stem cell niche"
      ],
      "evidence_summary": "Numerous glutamatergic and synaptic genes in the input list, with well-documented expression and function in glioblastoma, map onto a coordinated program of neuron-like signaling adaptation for invasion, stemness, and microenvironmental remodeling.",
      "significance_score": 0.94,
      "citations": [
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4412924/", "source_id": "106"},
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8499409/", "source_id": "107"}
      ],
      "supporting_genes": ["SLC17A6", "GRIN2A", "SV2B", "SYT1", "RPH3A", "RIMBP2"],
      "required_genes_not_in_input": {
        "genes": ["SLC1A3", "GRIA2"],
        "citations": [
          {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4412924/", "source_id": "106"}
        ]
      }
    },
    {
      "program_name": "Axon Guidance & Cell Migration",
      "description": "Collective enrichment for axon guidance proteins (EFNA5, SEMA3C, UNC5D, CNTN5, CNTNAP4), with roles in migration/invasion, tumor plasticity, and stem cell maintenance.",
      "atomic_biological_processes": [
        {
          "name": "Axon guidance",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6987732/", "source_id": "56", "notes": "Eph/ephrin, semaphorin, UNC5/netrin signaling modulate glioma migration and stemness."}
          ],
          "genes": ["EFNA5", "SEMA3C", "UNC5D", "CNTN5", "CNTNAP4"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Growth cone/axon guidance machinery",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6987732/", "source_id": "56"}
          ],
          "genes": ["EFNA5", "SEMA3C", "UNC5D"]
        }
      ],
      "predicted_cellular_impact": [
        "Facilitates invasion via re-purposing axon guidance programs",
        "Supports tumor cell plasticity, migration, and self-renewal"
      ],
      "evidence_summary": "Classic axon guidance genes are highly referenced for driving glioblastoma migration, stemness, and adaptative microenvironment signaling—input list supports a robust migration/invasion program.",
      "significance_score": 0.91,
      "citations": [
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6987732/", "source_id": "56"},
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7238747/", "source_id": "51"}
      ],
      "supporting_genes": ["EFNA5", "SEMA3C", "UNC5D", "CNTN5", "CNTNAP4"],
      "required_genes_not_in_input": {
        "genes": ["DCC", "FLRT1", "EphA2"],
        "citations": [
          {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6987732/", "source_id": "56"}
        ]
      }
    },
    {
      "program_name": "Transcriptional & Epigenetic Reprogramming",
      "description": "Enrichment for transcription factors (EBF1, EBF2, CUX2, MYT1L, POU6F2, RUNX1T1), RNA-binding proteins (RBFOX1), and splicing factors, which drive stemness, plasticity, and resistance. Links to aberrant splicing program.",
      "atomic_biological_processes": [
        {
          "name": "Transcriptional regulation",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7296349/", "source_id": "83", "notes": "EBF family TFs drive neuronal development, differentiation, and are implicated in glioblastoma regulation."}
          ],
          "genes": ["EBF1", "EBF2", "CUX2", "MYT1L", "POU6F2", "RUNX1T1"]
        },
        {
          "name": "Alternative RNA splicing",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7155901/", "source_id": "75", "notes": "Splicing programs strongly influence glioblastoma phenotype and prognosis."}
          ],
          "genes": ["RBFOX1", "SRRM4"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Nucleus (transcriptional/epigenetic complexes)",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7155901/", "source_id": "75"}
          ],
          "genes": ["RBFOX1", "CUX2", "RUNX1T1", "SRRM4"]
        }
      ],
      "predicted_cellular_impact": [
        "High plasticity and drug resistance via transcriptional reprogramming",
        "Enhanced self-renewal and stemness"
      ],
      "evidence_summary": "Many of the TFs and RNA binding proteins in the list are established drivers of stemness, therapy resistance, and cellular identity transitions in glioblastoma.",
      "significance_score": 0.88,
      "citations": [
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7296349/", "source_id": "83"},
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7155901/", "source_id": "75"}
      ],
      "supporting_genes": ["EBF1", "EBF2", "CUX2", "MYT1L", "POU6F2", "RUNX1T1", "RBFOX1", "SRRM4"],
      "required_genes_not_in_input": {
        "genes": ["SOX2", "OLIG2", "STAT3"],
        "citations": [
          {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7155901/", "source_id": "75"}
        ]
      }
    },
    {
      "program_name": "Potassium Channel & Ion Transport Adaptations",
      "description": "Several potassium channel (KCNJ6, KCNC2, DPP10) and ion transport modulators support cellular adaptation for migration, volume regulation, and therapy resistance.",
      "atomic_biological_processes": [
        {
          "name": "Ion transport regulation",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3230698/", "source_id": "123", "notes": "Potassium channels critical for glioma migration and invasion."}
          ],
          "genes": ["KCNJ6", "KCNC2", "DPP10"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Plasma membrane (ion channels)",
          "citation": [
            {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3230698/", "source_id": "123"}
          ],
          "genes": ["KCNJ6", "KCNC2", "DPP10"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced migration and invasiveness",
        "Potential therapy resistance via cell volume regulation"
      ],
      "evidence_summary": "Extensive literature links potassium channel deregulation to invasive behavior and adaptation to therapy and microenvironment.",
      "significance_score": 0.85,
      "citations": [
        {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3230698/", "source_id": "123"}
      ],
      "supporting_genes": ["KCNJ6", "KCNC2", "DPP10"],
      "required_genes_not_in_input": {
        "genes": ["KCNK2", "KCNMA1"],
        "citations": [
          {"url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3230698/", "source_id": "123"}
        ]
      }
    }
  ],
  "method": {
    "clustering_basis": ["pathway databases", "literature co-citation", "protein-protein interaction (PPI) data", "co-expression modules", "functional gene enrichment analysis"],
    "notes": "Programs were derived by systematically mapping input genes to literature-documented pathways and cellular processes, cross-referencing gene functions in malignant glioblastoma, and checking co-expression and PPI data where available."
  },
  "version": "2025-11-17"
}
<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_170][^1_171][^1_172][^1_173][^1_174][^1_175][^1_176][^1_177][^1_178][^1_179][^1_18][^1_180][^1_181][^1_182][^1_183][^1_184][^1_185][^1_186][^1_187][^1_188][^1_189][^1_19][^1_190][^1_191][^1_192][^1_193][^1_194][^1_195][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

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
[^1_10]: https://github.com/elifesciences/enhanced-preprints-data/raw/master/data/88673/v1/88673-v1.pdf
[^1_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2853350/
[^1_12]: http://www.jneurosci.org/content/26/47/12294.full.pdf
[^1_13]: https://www.mdpi.com/1422-0067/24/24/17633/pdf?version=1702913099
[^1_14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7809625/
[^1_15]: https://ujms.net/index.php/ujms/article/view/6175
[^1_16]: https://www.tandfonline.com/doi/pdf/10.1080/15384047.2015.1056406?needAccess=true
[^1_17]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6675433/
[^1_18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8820651/
[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10213810/
[^1_20]: http://downloads.hindawi.com/journals/sci/2014/838950.pdf
[^1_21]: https://www.mdpi.com/1422-0067/24/3/2111/pdf?version=1674221859
[^1_22]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8162173/
[^1_23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3755221/
[^1_24]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2897968/
[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9916747/
[^1_26]: https://www.mdpi.com/2227-9059/9/10/1328/pdf
[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8533397/
[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5421898/
[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8758422/
[^1_30]: https://www.frontiersin.org/articles/10.3389/fcell.2020.588152/pdf
[^1_31]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11489571/
[^1_32]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7523180/
[^1_33]: https://www.oncotarget.com/lookup/doi/10.18632/oncotarget.15302
[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10046791/
[^1_35]: https://www.mdpi.com/2072-6694/15/6/1879/pdf?version=1679382163
[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10876826/
[^1_37]: https://onlinelibrary.wiley.com/doi/10.1155/bmri/2004975
[^1_38]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8414390/
[^1_39]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11101656/
[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5084181/
[^1_41]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10760023/
[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4914248/
[^1_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4490432/
[^1_44]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10423747/
[^1_45]: https://www.mdpi.com/1422-0067/16/6/12108/pdf
[^1_46]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4383753/
[^1_47]: https://dx.plos.org/10.1371/journal.pone.0025451
[^1_48]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9454705/
[^1_49]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4483094/
[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7082224/
[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5312354/
[^1_52]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4183860/
[^1_53]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6056225/
[^1_54]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9952003/
[^1_55]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10601256/
[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4693299/
[^1_57]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7261182/
[^1_58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10119166/
[^1_59]: https://www.mdpi.com/2227-9059/6/2/42/pdf
[^1_60]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6027460/
[^1_61]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6888630/
[^1_62]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6539029/
[^1_63]: http://jcs.biologists.org/content/122/11/1723.full.pdf
[^1_64]: https://www.mdpi.com/1422-0067/20/3/556/pdf
[^1_65]: https://www.embopress.org/doi/10.1002/emmm.201200206
[^1_66]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11100671/
[^1_67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9596381/
[^1_68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5223529/
[^1_69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4301587/
[^1_70]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4744167/
[^1_71]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3696554/
[^1_72]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4139066/
[^1_73]: http://www.jbc.org/content/291/23/12282.full.pdf
[^1_74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8455679/
[^1_75]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7798022/
[^1_76]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5315656/
[^1_77]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7163051/
[^1_78]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10026424/
[^1_79]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4901439/
[^1_80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6912032/
[^1_81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7904102/
[^1_82]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9536135/
[^1_83]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5545892/
[^1_84]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/1878-0261.12668
[^1_85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9972689/
[^1_86]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8885828/
[^1_87]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4011561/
[^1_88]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3113313/
[^1_89]: https://downloads.hindawi.com/journals/jo/2020/9235101.pdf
[^1_90]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8946689/
[^1_91]: https://www.mdpi.com/2072-6694/14/6/1382/pdf
[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4502760/
[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3010848/
[^1_94]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10916047/
[^1_95]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8480197/
[^1_96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12089638/
[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9476413/
[^1_98]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7539681/
[^1_99]: https://www.mdpi.com/1422-0067/24/1/749/pdf?version=1672569074
[^1_100]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4396464/
[^1_101]: https://www.mdpi.com/2227-9067/9/10/1439/pdf?version=1663818482
[^1_102]: https://www.mdpi.com/1422-0067/23/21/12889/pdf?version=1666706216
[^1_103]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11371641/
[^1_104]: https://f1000research.com/articles/13-817/pdf
[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5892144/
[^1_106]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4623498/
[^1_107]: https://www.mdpi.com/2073-4409/10/5/1226/pdf
[^1_108]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8403340/
[^1_109]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11582119/
[^1_110]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10117795/
[^1_111]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8295384/
[^1_112]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6479730/
[^1_113]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11343637/
[^1_114]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8330525/
[^1_115]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6180049/
[^1_116]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5834250/
[^1_117]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6779830/
[^1_118]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5530036/
[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11011684/
[^1_120]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5335262/
[^1_121]: https://www.mdpi.com/1422-0067/22/21/11909/pdf
[^1_122]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8584308/
[^1_123]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3263536/
[^1_124]: https://biomedres.us/pdfs/BJSTR.MS.ID.002879.pdf
[^1_125]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9168818/
[^1_126]: https://linkinghub.elsevier.com/retrieve/pii/S0021925820675305
[^1_127]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7497650/
[^1_128]: http://downloads.hindawi.com/archive/2011/590249.pdf
[^1_129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9075824/
[^1_130]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9732544/
[^1_131]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6961677/
[^1_132]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8048363/
[^1_133]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10840508/
[^1_134]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6635074/
[^1_135]: https://linkinghub.elsevier.com/retrieve/pii/S0304383523003002
[^1_136]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8009861/
[^1_137]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5428538/
[^1_138]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8549703/
[^1_139]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10666796/
[^1_140]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5505128/
[^1_141]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9812627/
[^1_142]: https://www.mdpi.com/1422-0067/22/19/10247/pdf
[^1_143]: https://www.frontiersin.org/articles/10.3389/fphar.2023.1291773/pdf?isPublishedV2=False
[^1_144]: https://downloads.hindawi.com/journals/jo/2022/6093216.pdf
[^1_145]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7864518/
[^1_146]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8267680/
[^1_147]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4185866/
[^1_148]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9928553/
[^1_149]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7557106/
[^1_150]: https://www.mdpi.com/1422-0067/22/3/1046/pdf
[^1_151]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8151573/
[^1_152]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9874686/
[^1_153]: https://res.mdpi.com/d_attachment/ijms/ijms-20-03183/article_deploy/ijms-20-03183-v2.pdf
[^1_154]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/glia.24456
[^1_155]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8020668/
[^1_156]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10326479/
[^1_157]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10181199/
[^1_158]: https://linkinghub.elsevier.com/retrieve/pii/S2352304223003252
[^1_159]: https://www.frontiersin.org/articles/10.3389/fncel.2021.703431/pdf
[^1_160]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9873505/
[^1_161]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5327503/
[^1_162]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3349915/
[^1_163]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4648299/
[^1_164]: https://www.mdpi.com/2218-273X/10/3/403
[^1_165]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10932124/
[^1_166]: https://www.mdpi.com/1422-0067/25/5/2858/pdf?version=1709272105
[^1_167]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5001929/
[^1_168]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6787003/
[^1_169]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8626944/
[^1_170]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11096233/
[^1_171]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11493175/
[^1_172]: https://www.mdpi.com/1422-0067/19/5/1369/pdf
[^1_173]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8844449/
[^1_174]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/tox.24210
[^1_175]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5929440/
[^1_176]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7165076/
[^1_177]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5587982/
[^1_178]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7998903/
[^1_179]: https://www.mdpi.com/2072-6694/14/10/2544/pdf?version=1653137813
[^1_180]: https://www.mdpi.com/2073-4409/10/3/549/pdf
[^1_181]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9247127/
[^1_182]: https://www.mdpi.com/1422-0067/22/18/9665/pdf
[^1_183]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8815087/
[^1_184]: https://www.thno.org/v11p2080.htm
[^1_185]: https://www.mdpi.com/2073-4409/12/23/2759/pdf?version=1701586895
[^1_186]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3372715/
[^1_187]: https://www.mdpi.com/1422-0067/24/8/7617/pdf?version=1682003139
[^1_188]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11121124/
[^1_189]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8714878/
[^1_190]: https://www.frontiersin.org/articles/10.3389/fcell.2020.588368/pdf
[^1_191]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5595534/
[^1_192]: https://www.mdpi.com/2072-6694/12/4/892/pdf
[^1_193]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8688884/
[^1_194]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9869596/
[^1_195]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7226056/```


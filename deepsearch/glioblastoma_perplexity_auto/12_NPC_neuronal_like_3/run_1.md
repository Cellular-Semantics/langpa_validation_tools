---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-11-26T13:33:59.986078'
end_time: '2025-11-26T13:38:53.443392'
duration_seconds: 293.46
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 37
---

## Question

Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: ["GRIN3A", "CUX2", "LINC02144", "LINC00639", "CACNA2D3", "DLX6-AS1", "SYT1", "OLFM3", "TOX", "THRB", "SLAIN1", "GABRB2", "PLCB1", "HRK", "NYAP2", "LINC00581", "AL009178.3", "MAML3", "SLC17A6", "LYPD6B", "LRTM1", "CARMIL1", "CNTN2", "EBF3", "INSYN2B", "NSG2", "GRK5", "FRAS1", "KITLG", "B3GAT2", "MEIS2", "SYNPR", "ZNF618", "CDH12", "SPOCK1", "SRRM4", "SVEP1", "AC006296.3", "PCP4", "LEMD1", "CEMIP2", "NXPH1", "KLHL35", "UNCX", "ABTB2", "MDGA2", "AP003464.1", "ROBO3", "CNTNAP5", "ERBB4", "AC017053.1", "SOX1-OT", "AC022075.1", "EPHA3", "CRIM1", "CRABP1", "ARX", "RBFOX3", "RMST", "ARHGAP18", "FLRT2", "AL392023.2", "GLYCTK-AS1", "BEND7", "LINC02488", "HS3ST5", "CDH4", "LINC02133", "EPHA7", "FGFR2", "ANTXR2", "AL353138.1", "LAMP5", "DACH1", "ARL4D", "CELF4", "DLX6", "CDH18", "PRKCA", "PROX1-AS1", "SSTR2", "OTP", "STMN2", "AC115282.1", "SV2B", "SYT4", "TMEM196", "NRP1", "PCSK2", "NFIA-AS2", "MYT1L", "MYCBP2-AS1", "MIAT", "SLCO4C1", "DUOX1", "ENC1", "SLC4A10", "EPHA5", "SLC18A1", "SLIT1", "EBF1", "SDS", "DYNC1I1", "SPHKAP", "MCUB", "STARD4-AS1", "ST18", "DACH2", "ST6GAL1", "FGD5", "TENM2", "CNDP1", "CLMP", "TP73", "UNC5D", "VWC2L", "WNK2", "CDH22", "SCML4", "GABRA1", "RXRG", "RND3", "MIR548XHG", "LINC01550", "LINC01122", "LINC01102", "NDST4", "NRN1", "KLRD1", "NRSN1", "OSBPL10", "KLHL29", "KLHDC8A", "KCNQ3", "KCNK2", "KCNH8", "IGF1", "PBX3", "HSD11B2", "PIP5K1B", "HMCN1", "PKNOX2", "POU6F2", "GRIP2", "PRDM8", "PTCHD4", "LINC02428", "RBFOX1", "RIPOR2", "ABCB5", "LINC00707", "AC068722.1", "B3GLCT", "AL445623.2", "ADCY8", "BPIFC", "CASC15", "ADAMTS9-AS2", "AC090403.1"]

**Biological Context**: malignant glioblastoma cells

**Analysis Strategy**:
1. Search current scientific literature for functional roles of each gene in the input list
2. Identify clusters of genes that act together in pathways, processes, or cellular states
3. Treat each cluster as a potential gene program within the list
4. Interpret findings in light of both normal physiological roles and disease-specific alterations
5. Prioritize well-established functions with strong literature support, but highlight emerging evidence if contextually relevant.

**Guidelines**:
* Anchor all predictions in either the normal physiology and development of the cell type and tissue specified in the context OR the alterations and dysregulations characteristic of the specified disease
* Connect gene-level roles to program-level implications
* Consider gene interactions, regulatory networks, and pathway dynamics
* Highlight cases where multiple genes collectively strengthen evidence
* Ensure all claims are backed by experimental evidence with proper attribution

**Output**: Respond with JSON conforming to the provided schema - no prose, no markdown.  If you are unable to respond with JSON alone, make sure the text includes tables or fragments of schema compliant that unambiguously capture the elements and their associations that would be captured if returning JSON schema.

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
                "citations": {
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
                "source_id"
            ],
            "properties": {
                "source_id": {
                    "type": "string"
                },
                "notes": {
                    "type": "string",
                    "description": "Why this citation supports the claim."
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

```

## Output

<think>
This is a complex request. The user is asking me to perform a comprehensive literature analysis of 163 genes in the context of malignant glioblastoma cells, using the search results they've provided. They want me to:

1. Identify clusters of genes acting together in pathways/processes
2. Treat each cluster as a "gene program"
3. Interpret findings in light of both normal physiology and disease-specific alterations
4. Return the results as JSON conforming to the provided schema

Looking at the search results provided, I have access to research on:
- Neurogenesis and neuronal differentiation mechanisms
- Post-transcriptional control (RBFOX proteins, PTBP2)
- GABAergic neuron-to-glioma synapses
- Ion channels and calcium signaling in cancer
- Cell adhesion molecules
- Angiogenesis and VEGF signaling
- Axon guidance (ephrins, Slits)
- EBF family as tumor suppressors
- Metabolic reprogramming in GBM
- PDGF signaling in gliomas
- Tumor microenvironment
- PKC signaling
- Transcription factors (Myt1/Myt1l, TP73)
- RNA binding proteins (CELF4, RBFOX)
- Various synaptic and neuronal genes

Let me organize the genes by their known functions and cross-reference with the search results:

**Neuronal Differentiation/Maturation Programs:**
- RBFOX3, RBFOX1: Post-transcriptional control of neuronal programs [3]
- EBF3, EBF1: Transcription factors for neuronal differentiation, tumor suppressors [11]
- MYT1L: Transcription factor limiting GBM proliferation [20]
- CELF4: RNA binding protein controlling synaptic protein translation [30]
- SRRM4: Likely involved in alternative splicing for neuronal differentiation


- TP73: TAp73 isoform maintains stemness capacity [21]

**Synaptic/Neurotransmission:**
- SYT1, SYT4: Synaptotagmin proteins mediating vesicle release
- SLC17A6: Vesicular glutamate transporter
- SLC18A1: Vesicular monoamine transporter
- GABRB2, GABRA1: GABA receptors implicated in DMG growth [4]
- GRIN3A: Glutamate receptor subunit
- PLCB1: Phospholipase C signaling cascade
- GRK5: G-protein receptor kinase
- STR2: Somatostatin receptor [17]
- NRP1: Neuropilin functioning in angiogenic processes [8]

**Axon Guidance/Cell Adhesion:**
- EPHA3, EPHA5, EPHA7: Eph receptor family members [9]
- CNTN2, CNTNAP5: Contact-associated protein complexes
- FLRT2: Fibronectin-leucine-rich repeat protein
- ROBO3: Roundabout receptor
- SLIT1: Slit ligand
- CDH4, CDH12, CDH18, CDH22: Cadherin adhesion molecules [7]
- MDGA2: MAM domain-containing GPI-anchored protein
- LRTM1: Leucine-rich transmembrane protein

**Ion Channels/Chloride Transport:**
- KCNQ3, KCNK2, KCNH8: Potassium channel subtypes
- CACNA2D3: Calcium channel auxiliary subunit with tumor suppressor function [1]
- SLC4A10: Bicarbonate transporter
- NKCC1 appears to modulate GABAergic signaling [4]

**Transcription Factors:**
Multiple regulatory proteins control neuronal differentiation and tumor suppression, including EBF3 and EBF1 [11], along with MYT1L which represses YAP1 to constrain GBM proliferation [20]. Homeodomain factors like ARX, DLX6, UNCX, and PBX3 coordinate developmental programs, while PRDM8, RXRG, and OTP [18] regulate gene expression. PROX1 [36] and MEIS2 [33] function as TALE-class transcription factors, and TOX participates in cell fate determination.

**Post-transcriptional Regulation:**
RBFOX3 and RBFOX1 [3] orchestrate neuronal RNA processing, while CELF4 [30] controls mRNA translation at synapses. SRRM4 modulates splicing patterns, and RMST functions as a regulatory RNA.

**Growth Factor Pathways:**
FGFR2 and ERBB4 [29] represent receptor tyrosine kinases, while NRP1 [8] acts as a VEGF co-receptor. CRABP1 [16] binds retinoic acid and influences MAPK signaling. IGF1 and KITLG provide growth stimulation.

**Signaling and Metabolism:**
ADCY8, GRK5, and PRKCA regulate intracellular signaling cascades. Metabolic enzymes include DUOX1, HSD11B2, and PIP5K1B, while glycosyltransferases like ST6GAL1, B3GAT2, and B3GLCT modify protein structures.

**Extracellular Matrix:**
FRAS1, HMCN1, and SPOCK1 provide structural support, alongside VWC2L and SVEP1 which contain adhesion domains. CEMIP2 promotes cell migration, and ADAMTS9-AS2 and ANTXR2 participate in matrix remodeling.

**Transport and Membrane Functions:**
SLC4A10 and SLCO4C1 facilitate solute transport, OSBPL10 manages oxysterol binding, and ABCB5 functions as an ATP-dependent transporter.

**Neuronal Specialization:**
STMN2 [13] maintains axonal integrity, SV2B [5] localizes to synaptic vesicles, and SYNPR functions in synaptopoiesis. HRK [22] regulates apoptosis, DACH1 and DACH2 [35] suppress tumors, while NYAP2 and NSG2 support neuronal signaling. Transcription factors PKNOX2 and KNOXP2 direct gene expression, and ABTB2, LEMD1, and KLHL35 provide regulatory scaffolding.

**Cytoskeletal and Trafficking Dynamics:**
SLAIN1 stabilizes microtubules, DYNC1I1 powers dynein-mediated transport, and RND3 modulates Rho signaling. RIPOR2 and GRIP2 interact with glutamate receptors, while SPHKAP coordinates sphingosine kinase activity. TENM2 mediates cell-cell adhesion, OLFM3 influences olfactory development, and CLMP serves as a membrane receptor.

**Metabolic Support:**
CNDP1 processes carnosine, MCUB regulates mitochondrial calcium, and NDST4 modifies heparan sulfate. Long non-coding RNAs including LINC02144, DLX6-AS1, SOX1-OT, and others provide regulatory control over these processes.

**Gene Programs Emerging from the Data:**

Neuronal differentiation involves transcriptional regulators EBF3, EBF1, MYT1L alongside RNA-binding proteins RBFOX3, RBFOX1, CELF4, and SRRM4, with ARX and DLX6 driving lineage specification.

Synaptic function centers on GABAergic signaling through GABRB2 and GABRA1, vesicular transporters SLC17A6 and SLC18A1, and calcium regulation via SYT1, SYT4, and GRIN3A. These enable direct synaptic contact between GABAergic neurons and DMG cells, with presynaptic machinery controlling neurotransmitter release and postsynaptic response.

Cell adhesion and axon guidance molecules—including ephrin receptors EPHA3/5/7, cadherins CDH4/12/18/22, and axon guidance cues ROBO3 and SLIT1—regulate cellular positioning and migration. Their dysregulation in GBM facilitates invasion and metastatic spread.

Vascular signaling through NRP1, FGFR2, and ERBB4 coordinates angiogenic responses, with NRP1 particularly responsive to VEGF-driven vascular development.

Ion channels and chloride transporters including CACNA2D3, KCNQ3, and SLC4A10 modulate cellular excitability by controlling chloride gradients, which is essential for maintaining the depolarizing GABA phenotype that supports tumor growth.

Transcriptional regulators TP73, TOX, PBX3, and PROX1 direct cell fate decisions and developmental programming in the tumor microenvironment.  p73 maintains stemness while master regulators like EBF3 control transcriptional networks that preserve the glioma stem cell state and prevent differentiation.

Metabolic rewiring through ADCY8, PRKCA, and related enzymes shifts GBM cells toward glycolytic metabolism and enhances resistance to standard therapies. The extracellular matrix composition, shaped by FRAS1, HMCN1, and SPOCK1, creates a mechanically stiff microenvironment that facilitates invasion and therapeutic evasion.

Post-transcriptional regulation via RBFOX and CELF family proteins dysregulates splicing and translation of neuronal genes, keeping cells in a proliferative rather than differentiated state. Loss of pro-apoptotic factors like HRK and tumor suppressors such as DACH1 allows glioma cells to evade cell death pathways. Cytoskeletal proteins including STMN2 and DYNC1I1 maintain axonal structures necessary for glioma cell migration and survival.
</think>

```json
{
  "context": {
    "cell_type": "malignant glioblastoma cells",
    "disease": "glioblastoma multiforme (GBM)",
    "tissue": "brain"
  },
  "input_genes": [
    "GRIN3A",
    "CUX2",
    "LINC02144",
    "LINC00639",
    "CACNA2D3",
    "DLX6-AS1",
    "SYT1",
    "OLFM3",
    "TOX",
    "THRB",
    "SLAIN1",
    "GABRB2",
    "PLCB1",
    "HRK",
    "NYAP2",
    "LINC00581",
    "AL009178.3",
    "MAML3",
    "SLC17A6",
    "LYPD6B",
    "LRTM1",
    "CARMIL1",
    "CNTN2",
    "EBF3",
    "INSYN2B",
    "NSG2",
    "GRK5",
    "FRAS1",
    "KITLG",
    "B3GAT2",
    "MEIS2",
    "SYNPR",
    "ZNF618",
    "CDH12",
    "SPOCK1",
    "SRRM4",
    "SVEP1",
    "AC006296.3",
    "PCP4",
    "LEMD1",
    "CEMIP2",
    "NXPH1",
    "KLHL35",
    "UNCX",
    "ABTB2",
    "MDGA2",
    "AP003464.1",
    "ROBO3",
    "CNTNAP5",
    "ERBB4",
    "AC017053.1",
    "SOX1-OT",
    "AC022075.1",
    "EPHA3",
    "CRIM1",
    "CRABP1",
    "ARX",
    "RBFOX3",
    "RMST",
    "ARHGAP18",
    "FLRT2",
    "AL392023.2",
    "GLYCTK-AS1",
    "BEND7",
    "LINC02488",
    "HS3ST5",
    "CDH4",
    "LINC02133",
    "EPHA7",
    "FGFR2",
    "ANTXR2",
    "AL353138.1",
    "LAMP5",
    "DACH1",
    "ARL4D",
    "CELF4",
    "DLX6",
    "CDH18",
    "PRKCA",
    "PROX1-AS1",
    "SSTR2",
    "OTP",
    "STMN2",
    "AC115282.1",
    "SV2B",
    "SYT4",
    "TMEM196",
    "NRP1",
    "PCSK2",
    "NFIA-AS2",
    "MYT1L",
    "MYCBP2-AS1",
    "MIAT",
    "SLCO4C1",
    "DUOX1",
    "ENC1",
    "SLC4A10",
    "EPHA5",
    "SLC18A1",
    "SLIT1",
    "EBF1",
    "SDS",
    "DYNC1I1",
    "SPHKAP",
    "MCUB",
    "STARD4-AS1",
    "ST18",
    "DACH2",
    "ST6GAL1",
    "FGD5",
    "TENM2",
    "CNDP1",
    "CLMP",
    "TP73",
    "UNC5D",
    "VWC2L",
    "WNK2",
    "CDH22",
    "SCML4",
    "GABRA1",
    "RXRG",
    "RND3",
    "MIR548XHG",
    "LINC01550",
    "LINC01122",
    "LINC01102",
    "NDST4",
    "NRN1",
    "KLRD1",
    "NRSN1",
    "OSBPL10",
    "KLHL29",
    "KLHDC8A",
    "KCNQ3",
    "KCNK2",
    "KCNH8",
    "IGF1",
    "PBX3",
    "HSD11B2",
    "PIP5K1B",
    "HMCN1",
    "PKNOX2",
    "POU6F2",
    "GRIP2",
    "PRDM8",
    "PTCHD4",
    "LINC02428",
    "RBFOX1",
    "RIPOR2",
    "ABCB5",
    "LINC00707",
    "AC068722.1",
    "B3GLCT",
    "AL445623.2",
    "ADCY8",
    "BPIFC",
    "CASC15",
    "ADAMTS9-AS2",
    "AC090403.1"
  ],
  "programs": [
    {
      "program_name": "Terminal Neuronal Differentiation Blockade",
      "description": "This program encompasses transcriptional and post-transcriptional factors that normally drive neuronal terminal differentiation and maturation. In GBM, systematic loss or repression of these factors prevents transition from progenitor to mature neuronal phenotype, enabling continued proliferation. Key transcription factors (EBF3, EBF1, MYT1L, RBFOX3) and post-transcriptional regulators (CELF4, SRRM4, RBFOX1) coordinate alternative splicing and translation of neuronal genes. Loss of these programs is particularly notable as EBF3 is inactivated through deletion or hypermethylation in 50-90% of high-grade gliomas.",
      "atomic_biological_processes": [
        {
          "name": "neuronal lineage commitment and specification",
          "citations": [
            {
              "source_id": "11",
              "notes": "EBF family members are essential regulators of neuronal differentiation; EBF3 inactivation blocks differentiation and contributes to tumorigenesis"
            },
            {
              "source_id": "2",
              "notes": "Pax6 and downstream transcriptional networks regulate neurogenic fate determination in developing and adult neurogenesis"
            }
          ],
          "genes": [
            "EBF3",
            "EBF1",
            "ARX",
            "DLX6",
            "UNCX",
            "PRDM8"
          ]
        },
        {
          "name": "alternative splicing and post-transcriptional control of neuronal genes",
          "citations": [
            {
              "source_id": "3",
              "notes": "RBFOX1 and RBFOX3 control post-transcriptional programs during neurogenesis through splicing, mRNA stability, and translation regulation of neuronal maturation genes"
            },
            {
              "source_id": "30",
              "notes": "CELF4 translationally represses mRNAs encoding synaptic proteins during prenatal neuronal development"
            }
          ],
          "genes": [
            "RBFOX3",
            "RBFOX1",
            "CELF4",
            "SRRM4"
          ]
        },
        {
          "name": "repression of proliferative and epithelial-mesenchymal transition gene programs",
          "citations": [
            {
              "source_id": "20",
              "notes": "MYT1 and MYT1L expression reduces proliferation in GBM cell lines and activates neuronal differentiation programs while repressing YAP1"
            }
          ],
          "genes": [
            "MYT1L",
            "EBF3",
            "EBF1"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "RNA binding proteins regulating splicing and mRNA processing",
          "citations": [
            {
              "source_id": "3",
              "notes": "RBFOX proteins are neuronal-specific RNA binding proteins that regulate alternative splicing of genes critical for neuronal function"
            }
          ],
          "genes": [
            "RBFOX1",
            "RBFOX3",
            "CELF4",
            "SRRM4"
          ]
        },
        {
          "name": "transcriptional regulatory complexes driving neuronal fate",
          "citations": [
            {
              "source_id": "11",
              "notes": "EBF family members function as lineage-specific transcription factors essential for neuronal differentiation"
            }
          ],
          "genes": [
            "EBF3",
            "EBF1",
            "MEIS2",
            "PBX3",
            "PKNOX2"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Maintenance of proliferative capacity through suppression of terminal differentiation programs",
        "Retention of neural progenitor-like gene expression patterns enabling continued cell cycle entry",
        "Loss of synaptic maturation markers and structural specialization",
        "Reduced expression of differentiation-dependent apoptotic pathways",
        "Enhanced capacity for migration and invasion relative to differentiated neurons"
      ],
      "evidence_summary": "Terminal neuronal differentiation involves coordinated transcriptional and post-transcriptional changes that shift cells from proliferative to post-mitotic phenotypes. In normal brain development, EBF3, EBF1, MYT1L and RBFOX proteins drive neuronal maturation through activation of differentiation-specific genes and repression of proliferative and stemness programs. In glioblastoma, these differentiation-promoting factors are frequently inactivated. EBF3 is deleted or hypermethylated in 50-90% of high-grade gliomas, representing one of the most frequent inactivated genes in GBM. MYT1/MYT1L re-expression in GBM cell lines dramatically reduces proliferation and activates neuronal differentiation programs. RBFOX1 and RBFOX3 are critical regulators of adult neurogenesis and control mRNA stability and translation of neuronal genes including those encoding synaptic proteins. CELF4, expressed in developing cortical neurons, controls translational repression of synaptic protein mRNAs during synaptogenesis. The systematic loss of this program in GBM enables the maintenance of a proliferative, undifferentiated state while suppressing the post-mitotic, specialized phenotypes characteristic of mature neurons.",
      "significance_score": 0.95,
      "citations": [
        {
          "source_id": "11",
          "notes": "Comprehensive review of EBF family tumor suppressor functions; EBF3 inactivation in 50-90% of GBMs represents major differentiation blockade"
        },
        {
          "source_id": "20",
          "notes": "Experimental evidence that Myt1/Myt1l re-expression reduces GBM proliferation and activates neuronal differentiation"
        },
        {
          "source_id": "3",
          "notes": "Detailed mechanisms of RBFOX control of post-transcriptional programs in neuronal differentiation and maturation"
        },
        {
          "source_id": "30",
          "notes": "CELF4 controls translation of synaptic proteins during prenatal cortical development"
        }
      ],
      "supporting_genes": [
        "EBF3",
        "EBF1",
        "MYT1L",
        "RBFOX3",
        "RBFOX1",
        "CELF4",
        "SRRM4",
        "ARX",
        "DLX6",
        "UNCX",
        "PRDM8",
        "MEIS2",
        "PBX3",
        "PKNOX2"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "NEUN",
          "NeuroD1",
          "NeuroD2",
          "NeuroD4",
          "NeuroD6",
          "Neurogenin1",
          "Neurogenin2",
          "Neurogenin3",
          "Ascl1",
          "Math1",
          "Brn3a",
          "Brn3b"
        ],
        "citations": [
          {
            "source_id": "11",
            "notes": "Multiple transcription factors work together with EBF family to drive neuronal differentiation"
          },
          {
            "source_id": "2",
            "notes": "Comprehensive neurogenic transcription factor networks operate during both embryonic and adult neurogenesis"
          }
        ]
      }
    },
    {
      "program_name": "GABAergic Synaptic Tumor Promotion",
      "description": "This program represents a unique tumor-promoting mechanism where GABAergic neurons form functional synapses with GBM cells, particularly in diffuse midline gliomas (DMGs) with H3K27M mutation. GABAergic input through GABA-A receptors produces depolarizing rather than hyperpolarizing currents in GBM cells due to elevated intracellular chloride maintained by NKCC1 transporter. This unusual depolarizing GABA signaling drives tumor cell proliferation and survival. The program includes synaptic vesicle proteins, neurotransmitter transporters, GABA receptors, and the chloride transporter NKCC1 that enables the depolarizing phenotype.",
      "atomic_biological_processes": [
        {
          "name": "GABAergic neurotransmitter synthesis and vesicular packaging",
          "citations": [
            {
              "source_id": "4",
              "notes": "GABAergic neurons form functional neuron-to-glioma synapses with DMG cells expressing GABRG2 (GABA-A receptor subunit)"
            }
          ],
          "genes": [
            "SLC18A1"
          ]
        },
        {
          "name": "synaptic vesicle release and calcium-dependent exocytosis",
          "citations": [
            {
              "source_id": "5",
              "notes": "SV2B regulates presynaptic calcium levels and synaptic vesicle dynamics, critical for neurotransmitter release"
            }
          ],
          "genes": [
            "SYT1",
            "SYT4",
            "SV2B",
            "SYNPR"
          ]
        },
        {
          "name": "GABA-A receptor-mediated ionotropic signaling",
          "citations": [
            {
              "source_id": "4",
              "notes": "H3K27M-altered DMG cells express functional GABA-A receptors (GABRB2, GABRG2) that mediate depolarizing GABAergic currents via NKCC1-driven chloride accumulation"
            }
          ],
          "genes": [
            "GABRB2",
            "GABRA1"
          ]
        },
        {
          "name": "chloride homeostasis and NKCC1-dependent depolarization",
          "citations": [
            {
              "source_id": "4",
              "notes": "NKCC1 function is critical for the depolarizing effect of GABA in DMG cells; blocking NKCC1 with bumetanide reverses the depolarizing GABA response"
            }
          ],
          "genes": []
        },
        {
          "name": "glutamatergic synaptic transmission in parallel with GABAergic input",
          "citations": [
            {
              "source_id": "4",
              "notes": "Both GABAergic and glutamatergic neurons form synapses onto DMG cells; NMDA and AMPA receptors detected on some DMG cell populations"
            }
          ],
          "genes": [
            "GRIN3A",
            "SLC17A6",
            "PLCB1"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "presynaptic terminal containing synaptic vesicles and release machinery",
          "citations": [
            {
              "source_id": "5",
              "notes": "SV2 proteins are integral to synaptic vesicle dynamics and calcium-dependent release machinery"
            }
          ],
          "genes": [
            "SYT1",
            "SYT4",
            "SV2B",
            "SYNPR"
          ]
        },
        {
          "name": "postsynaptic GABA-A receptor complex in glioma cells",
          "citations": [
            {
              "source_id": "4",
              "notes": "Electron microscopy identified GFP-tagged GABRG2 in postsynaptic glioma membranes opposing presynaptic neuronal terminals"
            }
          ],
          "genes": [
            "GABRB2",
            "GABRA1"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Increased intracellular calcium flux through depolarization-activated voltage-gated calcium channels",
        "Activation of calcium-dependent growth and survival signaling pathways",
        "Enhanced proliferation and reduced apoptosis in response to GABAergic input",
        "Increased tumor growth in regions with high GABAergic neuron density",
        "GABA-A antagonists (e.g., lorazepam) reduce DMG tumor growth and proliferation",
        "Depolarizing GABA distinguishes H3K27M-DMG from hemispheric high-grade gliomas lacking NKCC1 depolarizing function"
      ],
      "evidence_summary": "Recent studies identified a remarkable tumor-promoting mechanism specific to H3K27M-mutated diffuse midline gliomas (DMGs) in which GABAergic neurons form functional, growth-promoting synapses with glioma cells. Using patch-clamp electrophysiology, in vivo optogenetics, and patient-derived orthotopic xenografts, researchers demonstrated that GABAergic input produces depolarizing currents in DMG cells via GABA-A receptors. This depolarization, unusual in neurons where GABA typically hyperpolarizes, results from elevated intracellular chloride in DMG cells maintained by the NKCC1 chloride-sodium-potassium cotransporter. This depolarizing GABAergic signaling promotes DMG cell proliferation and tumorigenicity. GABAergic synapse-related gene expression is enriched in all malignant cellular compartments of H3K27M-DMGs and particularly enriched in oligodendrocyte precursor cell-like compartments. Pharmacological GABA-A inhibition with lorazepam dose-dependently reduced DMG xenograft proliferation and survival. In contrast, hemispheric high-grade glioblastomas lacking H3K27M and NKCC1-mediated depolarization showed minimal GABAergic currents and were unresponsive to GABA-A inhibition. This tumor subtype-specific mechanism reveals an unexpected vulnerability of a particular glioma subset to neuron-derived signals.",
      "significance_score": 0.88,
      "citations": [
        {
          "source_id": "4",
          "notes": "Comprehensive characterization of GABAergic neuron-to-glioma synapses in H3K27M-DMGs with functional electrophysiology and in vivo validation"
        },
        {
          "source_id": "34",
          "notes": "WNK kinases regulate NKCC1 function and chloride balance with implications for cancer cell signaling and pain pathways"
        }
      ],
      "supporting_genes": [
        "GABRB2",
        "GABRA1",
        "SYT1",
        "SYT4",
        "SV2B",
        "SYNPR",
        "GRIN3A",
        "SLC17A6",
        "PLCB1",
        "SLC18A1"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "NKCC1",
          "SLC12A2",
          "KCC2",
          "SLC12A5",
          "GABRG2",
          "GAD1",
          "GAD2",
          "VGAT",
          "SLC32A1",
          "ChAT",
          "NMDAR",
          "AMPAR"
        ],
        "citations": [
          {
            "source_id": "4",
            "notes": "NKCC1 is the critical chloride transporter enabling depolarizing GABAergic currents in DMG cells; GAD enzymes produce GABA; GABRG2 detected on glioma cells"
          }
        ]
      }
    },
    {
      "program_name": "Axon Guidance & Cell Adhesion Dysregulation",
      "description": "This program encompasses the classical axon guidance molecules and cell adhesion molecules that normally establish correct neuronal connectivity and cell-cell contacts during brain development. These genes regulate repulsive and attractive interactions between neurons and guide axonal pathfinding. In GBM, altered expression of these molecules disrupts normal adhesive properties and enables aberrant cell migration and invasion. Eph receptors and their ephrin ligands regulate bidirectional signaling that sculpts developing axons and dendrites. Robo receptors bind Slit ligands to mediate repulsive guidance. Cadherins maintain homophilic cell-cell adhesion. In GBM, loss or alteration of adhesion molecules enables enhanced motility and invasion through tissue.",
      "atomic_biological_processes": [
        {
          "name": "Ephrin-A reverse signaling in axon guidance and topographic mapping",
          "citations": [
            {
              "source_id": "9",
              "notes": "Ephrin-A mediates reverse signaling in retinal ganglion cell axons to control axon branching and pathfinding through interactions with neurotrophin receptors"
            }
          ],
          "genes": [
            "EPHA3",
            "EPHA5",
            "EPHA7"
          ]
        },
        {
          "name": "Ephrin-B reverse signaling in presynaptic development and synapse formation",
          "citations": [
            {
              "source_id": "9",
              "notes": "Ephrin-B reverse signaling regulates synapse formation in cultured neurons and plays essential roles in shaft synapse formation through PDZ interactions"
            }
          ],
          "genes": [
            "EPHA3",
            "EPHA5",
            "EPHA7"
          ]
        },
        {
          "name": "Robo-Slit repulsive axon guidance signaling",
          "citations": [
            {
              "source_id": "10",
              "notes": "Slits bind to Robo receptors to induce repulsive signaling during axon guidance and neuronal migration"
            }
          ],
          "genes": [
            "ROBO3",
            "SLIT1"
          ]
        },
        {
          "name": "Cadherin-mediated homophilic cell-cell adhesion",
          "citations": [
            {
              "source_id": "7",
              "notes": "Cadherins are calcium-dependent cell adhesion molecules critical for proper brain development and establishing correct neuronal connectivity"
            }
          ],
          "genes": [
            "CDH4",
            "CDH12",
            "CDH18",
            "CDH22"
          ]
        },
        {
          "name": "Contactin-mediated neuronal cell adhesion and neurite outgrowth",
          "citations": [
            {
              "source_id": "7",
              "notes": "Contactins (CNTN) mediate cell-to-cell communication and are involved in neuronal connectivity"
            }
          ],
          "genes": [
            "CNTN2",
            "CNTNAP5"
          ]
        },
        {
          "name": "Fibronectin-leucine-rich repeat interactions in axon guidance",
          "citations": [
            {
              "source_id": "9",
              "notes": "Fibronectin-containing proteins interact with receptor tyrosine kinases and integrins to regulate axon pathfinding"
            }
          ],
          "genes": [
            "FLRT2",
            "MDGA2",
            "LRTM1"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Eph receptor tyrosine kinases for forward signaling",
          "citations": [
            {
              "source_id": "9",
              "notes": "EphA receptors transduce forward signals through their intracellular kinase domains in response to ephrin binding"
            }
          ],
          "genes": [
            "EPHA3",
            "EPHA5",
            "EPHA7"
          ]
        },
        {
          "name": "Cell adhesion molecule complexes at synaptic and non-synaptic sites",
          "citations": [
            {
              "source_id": "7",
              "notes": "CAMs organize into functional complexes that mediate cell-to-cell communication, signal transduction, and proper arrangement of synaptic structures"
            }
          ],
          "genes": [
            "CDH4",
            "CDH12",
            "CDH18",
            "CDH22",
            "CNTN2",
            "CNTNAP5",
            "FLRT2"
          ]
        },
        {
          "name": "Roundabout and Slit ligand receptor-ligand pairs",
          "citations": [
            {
              "source_id": "10",
              "notes": "Robo receptors form signaling complexes upon Slit ligand binding to trigger repulsive axonal guidance"
            }
          ],
          "genes": [
            "ROBO3",
            "SLIT1"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Reduced adhesion between glioma cells enabling dissociation and migration",
        "Altered axon-like cellular processes affecting glioma cell morphology and directionality",
        "Increased invasiveness through suppressed cell-matrix and cell-cell adhesion mechanisms",
        "Dysregulated responses to repulsive guidance cues that normally confine cells",
        "Enhanced motility through disrupted cadherin-based contact inhibition",
        "Altered signaling downstream of Eph and Robo receptors affecting cytoskeletal dynamics"
      ],
      "evidence_summary": "Axon guidance and cell adhesion molecules are fundamental to establishing proper brain architecture by directing neuronal processes and maintaining appropriate cell-cell contacts. During development, Eph receptors and ephrin ligands establish repulsive gradients that guide axons to correct targets. Ephrin-B reverse signaling is particularly important for presynaptic development and shaft synapse formation. Robo receptors bind Slit ligands to mediate repulsive guidance. Cadherins maintain homophilic cell-cell adhesion crucial for proper connectivity. Contactins and other adhesion molecules facilitate neuronal cell-to-cell communication. In glioblastoma, downregulation or alteration of these adhesion and guidance molecules is associated with increased motility and invasiveness. Loss of cadherin-mediated adhesion reduces contact inhibition. Altered Eph and Robo signaling disrupts the cytoskeletal responses that normally restrain cell movement. The presence of multiple adhesion and guidance molecules in this gene set suggests that GBM exploits dysregulation of these developmental pathways to enhance migratory capacity. ECM stiffening further conditions GBM cells for enhanced invasion and migration through changes in mechanotransduction.",
      "significance_score": 0.82,
      "citations": [
        {
          "source_id": "9",
          "notes": "Comprehensive review of ephrin reverse signaling in axon guidance and synaptogenesis"
        },
        {
          "source_id": "10",
          "notes": "Overview of Slit-Robo repulsive axon guidance signaling"
        },
        {
          "source_id": "7",
          "notes": "Comprehensive annotated functional classification of human cell adhesion molecules and their roles in brain development"
        },
        {
          "source_id": "25",
          "notes": "ECM stiffness conditions GBM cells for invasion"
        }
      ],
      "supporting_genes": [
        "EPHA3",
        "EPHA5",
        "EPHA7",
        "ROBO3",
        "SLIT1",
        "CDH4",
        "CDH12",
        "CDH18",
        "CDH22",
        "CNTN2",
        "CNTNAP5",
        "FLRT2",
        "MDGA2",
        "LRTM1"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "EFNA",
          "EFNB",
          "SLIT2",
          "SLIT3",
          "ROBO1",
          "ROBO2",
          "CDH1",
          "CDH3",
          "CDH5",
          "CDH6",
          "CDH7",
          "CDH8",
          "CDH9",
          "CDH10",
          "CTNND1",
          "CTNND2",
          "CTNNB1",
          "Integrin family",
          "Nectin family"
        ],
        "citations": [
          {
            "source_id": "9",
            "notes": "Ephrin-A and Ephrin-B ligands are required for forward signaling in eph-expressing cells"
          },
          {
            "source_id": "7",
            "notes": "Extended family of cadherins and associated proteins necessary for complete cell adhesion networks"
          }
        ]
      }
    },
    {
      "program_name": "Vascular Growth Factor Signaling & Angiogenesis",
      "description": "This program encompasses receptor tyrosine kinases and their ligands that promote angiogenesis and vascular growth. NRP1 (neuropilin-1) is a VEGF co-receptor that enhances VEGF-165 binding to VEGFR2, amplifying angiogenic signaling. FGFR2 mediates fibroblast growth factor signaling important for vascular development. ERBB4 activation in GBM is associated with shorter survival and promotes tumor growth through ERK activation. KITLG (kit ligand) signals through KIT receptor on hematopoietic and vascular cells. These growth factor pathways drive robust angiogenesis supporting tumor vascularization and nutrient delivery.",
      "atomic_biological_processes": [
        {
          "name": "VEGF-dependent neuropilin-1 induction and VEGFR2 signaling amplification",
          "citations": [
            {
              "source_id": "8",
              "notes": "VEGF165 selectively upregulates NRP1 via VEGFR2-dependent pathway; NRP1 coexists with VEGFR2 to increase VEGF165 binding and angioproliferative signaling"
            }
          ],
          "genes": [
            "NRP1"
          ]
        },
        {
          "name": "Endothelial cell proliferation and neovascular formation",
          "citations": [
            {
              "source_id": "8",
              "notes": "VEGF-stimulated endothelial proliferation is significantly inhibited by anti-NRP1 antibody; NRP1 inhibition suppresses neovascular formation in pathologic angioproliferative models"
            }
          ],
          "genes": [
            "NRP1",
            "FGFR2"
          ]
        },
        {
          "name": "ERBB4 receptor activation and ERK mitogenic signaling",
          "citations": [
            {
              "source_id": "29",
              "notes": "ERBB4 activation in GBM is associated with increased proliferation, angiogenesis, and tumorigenicity; ERBB4 promotes growth through ERK activation"
            }
          ],
          "genes": [
            "ERBB4"
          ]
        },
        {
          "name": "KIT ligand-mediated signaling in vascular and hematopoietic cells",
          "citations": [
            {
              "source_id": "26",
              "notes": "Growth factor ligands including KITLG drive proliferation of progenitor cells including those in vascular tissues"
            }
          ],
          "genes": [
            "KITLG"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Neuropilin-1 VEGF co-receptor complex with VEGFR2",
          "citations": [
            {
              "source_id": "8",
              "notes": "NRP1 coexists with VEGFR2 to increase VEGF165 binding and functional receptor expression in endothelial cells"
            }
          ],
          "genes": [
            "NRP1"
          ]
        },
        {
          "name": "ERBB4 receptor tyrosine kinase and downstream signaling",
          "citations": [
            {
              "source_id": "29",
              "notes": "ERBB4 forms functional receptor complexes that activate downstream ERK and other mitogenic pathways in glioma cells"
            }
          ],
          "genes": [
            "ERBB4"
          ]
        },
        {
          "name": "Fibroblast growth factor receptor 2 signaling complex",
          "citations": [
            {
              "source_id": "26",
              "notes": "FGFR2 mediates FGF signaling important for vascular and developmental processes"
            }
          ],
          "genes": [
            "FGFR2"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced VEGF-dependent endothelial cell recruitment and angiogenesis",
        "Amplified angiogenic signaling through NRP1 co-receptivity with VEGFR2",
        "Increased tumor vascularization supporting nutrient delivery and oxygenation",
        "ERBB4-dependent proliferation and survival signaling in glioma and associated vascular cells",
        "Resistance to anti-EGFR therapeutics through ERBB4 compensatory activation",
        "Increased angiogenesis and tumorigenicity associated with poor patient survival"
      ],
      "evidence_summary": "Angiogenesis is critical for GBM growth, and multiple vascular growth factor pathways are dysregulated in this disease. NRP1 (neuropilin-1) acts as a co-receptor for VEGF165 and VEGFR2, serving to amplify VEGF-dependent angiogenic signaling. VEGF selectively increases NRP1 expression through VEGFR2-dependent transcriptional upregulation in endothelial cells, creating a positive feedback loop that robust angiogenesis. NRP1 coexistence with VEGFR2 quantitatively increases VEGF165 binding and functional receptor expression. In animal models of pathologic angioproliferative retinopathy, intense NRP1 mRNA expression is observed in newly formed vessels, and selective NRP1 inhibition substantially suppresses neovascular formation. In GBM, ERBB4 receptor tyrosine kinase activation is associated with increased proliferation, angiogenesis, and tumorigenicity. Although ERBB4 mRNA levels are generally lower in GBM than in normal brain, ERBB4 protein phosphorylation (activation) is observed in 89% of GBM samples versus only 10% of normal brain, indicating selective post-translational activation. ERBB4 activation independent of EGFR predicts shorter patient survival and enables compensatory growth signaling when EGFR-targeted therapies are administered. These findings establish angiogenic growth factor signaling as a key driver of GBM progression.",
      "significance_score": 0.75,
      "citations": [
        {
          "source_id": "8",
          "notes": "Comprehensive characterization of VEGF-induced NRP1 expression and its role in angiogenic proliferation"
        },
        {
          "source_id": "29",
          "notes": "Evidence that ERBB4 activation is independent prognostic factor and therapeutic vulnerability in GBM"
        }
      ],
      "supporting_genes": [
        "NRP1",
        "FGFR2",
        "ERBB4",
        "KITLG"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "VEGF",
          "VEGFR2",
          "FGF",
          "FGF receptors",
          "HRG",
          "Heregulin",
          "KIT",
          "c-KIT",
          "MAPK",
          "ERK1/2",
          "PI3K",
          "AKT"
        ],
        "citations": [
          {
            "source_id": "8",
            "notes": "VEGF and VEGFR2 are required ligand-receptor pair for NRP1 induction and angiogenic signaling"
          },
          {
            "source_id": "29",
            "notes": "Heregulin-1beta is the ERBB3/ERBB4 ligand; ERK activation is downstream of ERBB4"
          }
        ]
      }
    },
    {
      "program_name": "Ion Channel & Electrolyte Homeostasis Dysregulation",
      "description": "This program encompasses ion channels and transporters that maintain cellular electrolyte balance and control neuronal excitability. Potassium channels (KCNQ3, KCNK2, KCNH8) regulate resting membrane potential and electrical activity. Voltage-gated calcium channels, modulated by CACNA2D3 auxiliary subunit, control calcium influx. CACNA2D3 functions as a tumor suppressor and is downregulated in gliomas. The bicarbonate transporter SLC4A10 participates in pH homeostasis. In GBM, dysregulation of these ion channels and transporters contributes to altered electrolyte balance that supports tumor cell survival and potentially creates a depolarized state permissive for abnormal signaling.",
      "atomic_biological_processes": [
        {
          "name": "Potassium channel regulation of resting membrane potential",
          "citations": [
            {
              "source_id": "6",
              "notes": "Ion channel gene expression profile predicts survival in glioma patients, implicating ion channels in GBM biology"
            }
          ],
          "genes": [
            "KCNQ3",
            "KCNK2",
            "KCNH8"
          ]
        },
        {
          "name": "Voltage-gated calcium channel regulation and calcium influx",
          "citations": [
            {
              "source_id": "1",
              "notes": "CACNA2D3, an auxiliary calcium channel subunit, is downregulated in gliomas and functions as a tumor suppressor"
            },
            {
              "source_id": "5",
              "notes": "Presynaptic calcium signaling regulates neurotransmitter release and synaptic dynamics"
            }
          ],
          "genes": [
            "CACNA2D3"
          ]
        },
        {
          "name": "Bicarbonate transport and pH homeostasis",
          "citations": [
            {
              "source_id": "12",
              "notes": "Solute carrier bicarbonate transporters (SLC4 family) mediate bicarbonate-dependent pH regulation"
            }
          ],
          "genes": [
            "SLC4A10"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Potassium channel proteins controlling membrane excitability",
          "citations": [
            {
              "source_id": "6",
              "notes": "Ion channel gene expression signatures are prognostic in glioma"
            }
          ],
          "genes": [
            "KCNQ3",
            "KCNK2",
            "KCNH8"
          ]
        },
        {
          "name": "Voltage-gated calcium channel auxiliary subunits",
          "citations": [
            {
              "source_id": "1",
              "notes": "CACNA2D3 is a calcium channel auxiliary protein with tumor suppressive function"
            }
          ],
          "genes": [
            "CACNA2D3"
          ]
        },
        {
          "name": "Plasma membrane ion transporters for electrolyte balance",
          "citations": [
            {
              "source_id": "12",
              "notes": "SLC family proteins mediate ion and metabolite transport across cellular membranes"
            }
          ],
          "genes": [
            "SLC4A10"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Altered resting membrane potential affecting cellular signaling thresholds",
        "Dysregulated calcium homeostasis affecting metabolic and signaling processes",
        "Loss of tumor suppressive effects of CACNA2D3 enabling continued proliferation",
        "Altered pH homeostasis supporting metabolic reprogramming",
        "Changes in ion-dependent signaling cascades downstream of calcium and potassium flux",
        "Prognostic significance of ion channel expression profile in predicting GBM survival"
      ],
      "evidence_summary": "Ion channels and transporters are increasingly recognized as important regulators of cancer cell behavior. CACNA2D3, which encodes an auxiliary subunit of voltage-gated calcium channels, is downregulated in gliomas and functions as a tumor suppressor, with re-expression of CACNA2D3 inhibiting glioma cell proliferation. Ion channel gene expression profiles are associated with glioma patient survival, indicating that dysregulation of ionic homeostasis contributes to GBM progression. Potassium channels (KCNQ3, KCNK2, KCNH8) regulate resting membrane potential and neuronal excitability. Loss or downregulation of these channels in GBM may alter the cellular electrolyte balance and create a more depolarized state permissive for abnormal signaling. The bicarbonate transporter SLC4A10 participates in pH regulation, and altered pH homeostasis is implicated in metabolic reprogramming characteristic of GBM. In the context of GABAergic synaptic signaling in DMGs, dysregulation of chloride transporters (particularly NKCC1, which is not in this gene set but is functionally implicated) combined with altered potassium channel function may contribute to the depolarizing GABA phenotype. Overall, ion channel dysregulation represents a potential therapeutic vulnerability in GBM.",
      "significance_score": 0.68,
      "citations": [
        {
          "source_id": "1",
          "notes": "CACNA2D3 functions as tumor suppressor and is downregulated in gliomas"
        },
        {
          "source_id": "6",
          "notes": "Ion channel gene expression profiles predict survival in glioma patients"
        },
        {
          "source_id": "4",
          "notes": "Ion channel function critical in DMG GABAergic synaptic signaling"
        }
      ],
      "supporting_genes": [
        "CACNA2D3",
        "KCNQ3",
        "KCNK2",
        "KCNH8",
        "SLC4A10"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "NKCC1",
          "SLC12A2",
          "KCC2",
          "SLC12A5",
          "CACNA1A",
          "CACNA1B",
          "CACNA1C",
          "Other CACNA family members",
          "Cav channels",
          "STIM",
          "ORAI"
        ],
        "citations": [
          {
            "source_id": "1",
            "notes": "CACNA2D3 functions as auxiliary subunit to full-length calcium channel proteins"
          },
          {
            "source_id": "4",
            "notes": "NKCC1 function critical for depolarizing GABA effect in DMG"
          }
        ]
      }
    },
    {
      "program_name": "Synaptic Plasticity & Dendritic Maturation",
      "description": "This program encompasses genes that control the formation, maturation, and plasticity of synaptic connections. Synaptotagmin proteins (SYT1, SYT4) are calcium sensors in presynaptic vesicles that trigger neurotransmitter release. Postsynaptic density proteins and related factors organize the postsynaptic compartment. CELF4, a translational repressor of synaptic proteins, is critical for prenatal synaptic development. Dendritic spine formation and maintenance depend on polarity proteins that compartmentalize spine structure. Aberrant expression of these genes in GBM disrupts synaptic specialization while potentially enhancing migratory and invasive phenotypes.",
      "atomic_biological_processes": [
        {
          "name": "Calcium-dependent synaptic vesicle release and neurotransmitter secretion",
          "citations": [
            {
              "source_id": "5",
              "notes": "SV2B regulates presynaptic calcium signaling and synaptic vesicle dynamics critical for neurotransmitter release"
            }
          ],
          "genes": [
            "SYT1",
            "SYT4",
            "SV2B"
          ]
        },
        {
          "name": "Translational control of synaptic proteins during development",
          "citations": [
            {
              "source_id": "30",
              "notes": "CELF4 translationally represses mRNAs encoding synaptic proteins, with deletion causing disruption of subplate synapses"
            }
          ],
          "genes": [
            "CELF4"
          ]
        },
        {
          "name": "Dendritic spine morphogenesis and polarity protein function",
          "citations": [
            {
              "source_id": "15",
              "notes": "Polarity proteins regulate dendritic spine formation and maintenance through compartmentalization and cytoskeletal dynamics"
            }
          ],
          "genes": [
            "NYAP2"
          ]
        },
        {
          "name": "Postsynaptic protein organization and function",
          "citations": [
            {
              "source_id": "7",
              "notes": "Cell adhesion molecules and scaffolding proteins organize postsynaptic density and dendritic structure"
            }
          ],
          "genes": [
            "INSYN2B",
            "NSG2",
            "LAMP5",
            "NRSN1"
          ]
        },
        {
          "name": "Synaptic activity-dependent plasticity and long-term potentiation",
          "citations": [
            {
              "source_id": "30",
              "notes": "RNA binding proteins including CELF4 control mRNAs encoding proteins involved in synaptic transmission and plasticity"
            }
          ],
          "genes": [
            "CELF4",
            "GRIP2"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Presynaptic terminal with synaptic vesicles and release machinery",
          "citations": [
            {
              "source_id": "5",
              "notes": "SV2 proteins are integral components of synaptic vesicles regulating calcium-dependent release"
            }
          ],
          "genes": [
            "SYT1",
            "SYT4",
            "SV2B",
            "SYNPR"
          ]
        },
        {
          "name": "Postsynaptic density organizing synaptic proteins and receptors",
          "citations": [
            {
              "source_id": "15",
              "notes": "PSD-95 and associated proteins organize postsynaptic density; dendritic spine structure maintained by polarity complexes"
            }
          ],
          "genes": [
            "GRIP2",
            "INSYN2B",
            "LAMP5",
            "NRSN1"
          ]
        },
        {
          "name": "mRNA localization and translational control at synapses",
          "citations": [
            {
              "source_id": "30",
              "notes": "CELF4 binds and translationally represses mRNAs at developing synapses"
            }
          ],
          "genes": [
            "CELF4"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Loss of synaptic specialization reducing differentiated phenotype",
        "Decreased compartmentalization of dendritic spines affecting cell morphology",
        "Reduced postsynaptic organization and functional synaptic connectivity",
        "Enhanced cellular plasticity enabling migration and invasion",
        "Altered calcium signaling at synapses affecting neuronal communication",
        "Shift from post-mitotic synaptic functions toward proliferative phenotype"
      ],
      "evidence_summary": "Synaptic plasticity and dendritic maturation are hallmarks of differentiated neurons and are progressively lost in glioblastoma. CELF4, an RNA binding protein highly expressed in developing subplate neurons, translationally represses mRNAs encoding synaptic proteins including VAMP, TrkB.T1, and other synaptically active proteins. CELF4 deletion causes sex-specific disruption of subplate synapses and altered dendritic complexity, indicating that CELF4-mediated translational control is essential for appropriate synaptic development. Synaptotagmin proteins (SYT1, SYT4) act as calcium sensors in synaptic vesicles and trigger neurotransmitter release. Polarity proteins maintain dendritic spine compartmentalization, with loss of polarity proteins in developing neurons causing dramatic reduction in PSD-95-positive synapses. In glioblastoma, the loss of genes promoting synaptic specialization enables cells to escape post-mitotic constraints and maintain proliferative capacity. The presence of multiple synaptic genes in this GBM-associated gene set suggests that suppression of the synaptic maturation program is part of the gliomagenic process, allowing cells to retain undifferentiated, proliferative properties.",
      "significance_score": 0.72,
      "citations": [
        {
          "source_id": "30",
          "notes": "CELF4 controls translational repression of synaptic proteins during prenatal synaptic development"
        },
        {
          "source_id": "5",
          "notes": "SV2B regulates presynaptic calcium signaling critical for synaptic vesicle dynamics"
        },
        {
          "source_id": "15",
          "notes": "Polarity proteins regulate dendritic spine formation and plasticity"
        }
      ],
      "supporting_genes": [
        "CELF4",
        "SYT1",
        "SYT4",
        "SV2B",
        "SYNPR",
        "INSYN2B",
        "NSG2",
        "NYAP2",
        "LAMP5",
        "NRSN1",
        "GRIP2"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "PSD95",
          "SAP102",
          "NMDAR",
          "AMPAR",
          "mGluR",
          "Calmodulin",
          "CaMKII",
          "CREB",
          "MAPK",
          "PI3K",
          "AKT"
        ],
        "citations": [
          {
            "source_id": "15",
            "notes": "PSD-95 is key postsynaptic density protein organizing synaptic structure"
          },
          {
            "source_id": "30",
            "notes": "Calcium/calmodulin-dependent protein kinase II (CaMKII) is involved in synaptic plasticity downstream of CELF4 target mRNAs"
          }
        ]
      }
    },
    {
      "program_name": "Axonal Maintenance & Cytoskeletal Integrity",
      "description": "This program encompasses genes that maintain axonal structure, diameter, and conduction velocity through organization of neurofilaments and microtubules. STMN2 (stathmin-2) is critical for establishing and maintaining neurofilament-dependent axoplasmic organization. Loss of STMN2 leads to shrinkage of neurofilament spacing, axonal collapse, and motor and sensory deficits. SV2B regulates presynaptic calcium and synaptic vesicle dynamics affecting axonal function. Dynein motors (DYNC1I1) transport cargo along microtubules. In GBM, dysregulation of axonal maintenance genes may contribute to aberrant cell morphology and altered cellular dynamics.",
      "atomic_biological_processes": [
        {
          "name": "Neurofilament assembly and axoplasmic organization",
          "citations": [
            {
              "source_id": "13",
              "notes": "STMN2 plays critical role in establishing and maintaining neurofilament-dependent axoplasmic organization; loss of STMN2 reduces neurofilament spacing by nearly half"
            }
          ],
          "genes": [
            "STMN2",
            "SLAIN1"
          ]
        },
        {
          "name": "Microtubule dynamics and cargo transport",
          "citations": [
            {
              "source_id": "13",
              "notes": "Microtubule associated proteins regulate dynamics of microtubules important for axonal function and transport"
            }
          ],
          "genes": [
            "DYNC1I1",
            "SLAIN1"
          ]
        },
        {
          "name": "Presynaptic calcium regulation and synaptic vesicle dynamics",
          "citations": [
            {
              "source_id": "5",
              "notes": "SV2B regulates presynaptic calcium levels critical for synaptic transmission and maintaining axonal terminals"
            }
          ],
          "genes": [
            "SV2B"
          ]
        },
        {
          "name": "Actin cytoskeleton organization and cell morphology",
          "citations": [
            {
              "source_id": "15",
              "notes": "Rho family GTPases and associated proteins regulate actin dynamics affecting dendritic spine and axonal morphology"
            }
          ],
          "genes": [
            "RND3",
            "ARHGAP18",
            "SPHKAP"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Neurofilament proteins and spacer proteins in axoplasm",
          "citations": [
            {
              "source_id": "13",
              "notes": "Neurofilament subunits organize into three-dimensional interlinked arrays with STMN2 orchestrating nearest-neighbor distances"
            }
          ],
          "genes": [
            "STMN2"
          ]
        },
        {
          "name": "Microtubule motor complexes and associated proteins",
          "citations": [
            {
              "source_id": "13",
              "notes": "Dynein motors transport cargo along microtubules in neurons and glia"
            }
          ],
          "genes": [
            "DYNC1I1"
          ]
        },
        {
          "name": "Presynaptic terminal ultrastructure and function",
          "citations": [
            {
              "source_id": "5",
              "notes": "SV2B is critical component of synaptic vesicles regulating terminal structure and function"
            }
          ],
          "genes": [
            "SV2B"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Altered axonal diameter and conduction velocity affecting cell communication",
        "Disrupted neurofilament spacing leading to reduced axonal stability",
        "Altered synaptic terminal structure and function",
        "Changes in microtubule dynamics affecting cellular transport",
        "Modified cell morphology with reduced axon-like processes",
        "Potential effects on cellular migration through altered cytoskeletal organization"
      ],
      "evidence_summary": "Axonal integrity is maintained by proper organization of neurofilaments and microtubules that determine axonal diameter and conduction velocity. STMN2 (stathmin-2, also called SCG10) is an essential axonal maintenance factor that orchestrates neurofilament spacing and organization. Sustained loss of STMN2 in adult mice leads to shrinkage of neurofilament spacing from median 29.02 nm to 16.86 nm, resulting in axonal collapse, reduced conduction velocity by 35%, and motor and sensory denervation. STMN2 loss is particularly relevant in amyotrophic lateral sclerosis (ALS), where TDP-43 pathology misprocesses STMN2 mRNA, producing truncated non-functional transcripts. Similar neurofilament spacing reduction (~30%) is observed in ALS patient tissues, indicating that STMN2 dysregulation directly contributes to motor neuron pathology. In GBM, dysregulation of STMN2 and other axonal maintenance genes may disrupt the normal cellular architecture and may contribute to aberrant cell morphology and migration. SV2B regulates presynaptic calcium signaling and synaptic vesicle dynamics, and loss of SV2B alters the pattern of neurotransmitter release. Dynein motors mediate long-distance cargo transport in neuronal and glial processes. The presence of multiple axonal maintenance genes in this GBM gene set suggests that disruption of normal axonal structure may support glioma cell dedifferentiation and altered cellular dynamics.",
      "significance_score": 0.65,
      "citations": [
        {
          "source_id": "13",
          "notes": "Comprehensive characterization of STMN2 role in neurofilament-dependent axonal maintenance and consequences of loss"
        },
        {
          "source_id": "5",
          "notes": "SV2B regulates presynaptic calcium and synaptic vesicle dynamics"
        }
      ],
      "supporting_genes": [
        "STMN2",
        "SLAIN1",
        "SV2B",
        "DYNC1I1",
        "RND3",
        "ARHGAP18",
        "SPHKAP"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "NF-L",
          "NF-M",
          "NF-H",
          "Tau",
          "MAPs",
          "Alpha-tubulin",
          "Beta-tubulin",
          "HDAC6",
          "TDP-43"
        ],
        "citations": [
          {
            "source_id": "13",
            "notes": "Neurofilament subunits are essential partners with STMN2 in maintaining axonal structure"
          }
        ]
      }
    },
    {
      "program_name": "Apoptosis Resistance & Cell Survival Pathways",
      "description": "This program encompasses genes controlling cell death and survival decisions. HRK (Harakiri) is a pro-apoptotic BH3-only protein of the Bcl-2 family that regulates apoptosis by interfering with anti-apoptotic Bcl-2 and Bcl-xL proteins. DACH1 and DACH2 are tumor suppressors that activate cell cycle arrest and apoptosis genes while repressing survival and proliferation genes. TP73 encodes p73, a p53-related transcription factor with complex roles in apoptosis and stemness. Loss or downregulation of these pro-death and pro-differentiation factors enables GBM cells to resist apoptosis and maintain viability despite stress.",
      "atomic_biological_processes": [
        {
          "name": "Intrinsic apoptotic pathway and Bcl-2 family regulation",
          "citations": [
            {
              "source_id": "22",
              "notes": "HRK is a pro-apoptotic Bcl-2 family member that regulates apoptosis by interfering with anti-apoptotic Bcl-2 and Bcl-xL proteins"
            }
          ],
          "genes": [
            "HRK"
          ]
        },
        {
          "name": "Transcriptional control of cell cycle arrest and apoptosis",
          "citations": [
            {
              "source_id": "35",
              "notes": "DACH1 activates genes involved in cell cycle arrest and apoptosis while repressing survival and proliferation genes; functions as tumor suppressor"
            }
          ],
          "genes": [
            "DACH1",
            "DACH2"
          ]
        },
        {
          "name": "TP73-mediated stemness and apoptotic regulation",
          "citations": [
            {
              "source_id": "21",
              "notes": "TAp73 is required for stemness potential in glioblastoma stem cells, regulating balance between differentiation and apoptosis"
            }
          ],
          "genes": [
            "TP73"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Mitochondrial outer membrane permeabilization complex",
          "citations": [
            {
              "source_id": "22",
              "notes": "HRK protein inserts into mitochondrial membrane to promote apoptosis"
            }
          ],
          "genes": [
            "HRK"
          ]
        },
        {
          "name": "Transcriptional repressor complexes with NCoR corepressor",
          "citations": [
            {
              "source_id": "35",
              "notes": "DACH1 contains dachshund domain that interacts with nuclear co-repressor (NCoR) to repress gene expression"
            }
          ],
          "genes": [
            "DACH1",
            "DACH2"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Reduced susceptibility to intrinsic apoptotic triggers through loss of pro-apoptotic signaling",
        "Enhanced cell survival signaling through loss of death-promoting transcription factors",
        "Maintenance of stemness properties through altered TP73 function",
        "Reduced responsiveness to genotoxic stress and chemotherapy-induced apoptosis",
        "Enhanced proliferation through loss of cell cycle checkpoint functions",
        "Increased resistance to radiation and chemotherapy"
      ],
      "evidence_summary": "GBM cells acquire enhanced resistance to apoptosis through dysregulation of cell death programs. HRK (Harakiri), a pro-apoptotic BH3-only member of the Bcl-2 family, promotes intrinsic apoptosis by antagonizing anti-apoptotic Bcl-2 and Bcl-xL proteins at the mitochondrial membrane. Loss or reduced HRK expression would enhance survival signaling. DACH1 (Dachshund-related protein) functions as a tumor suppressor and is frequently lost in various cancers including breast, ovarian, and potentially brain tumors. DACH1 expression is lost in a subset of breast cancers associated with poor prognosis, and re-introduction of DACH1 inhibits tumor cell proliferation and growth through suppression of cyclin D1. DACH1 activates expression of genes involved in cell cycle arrest and apoptosis while simultaneously repressing genes involved in cell survival and proliferation. DACH2 functions similarly. TP73, which encodes p73 protein, is a p53-related transcription factor with complex roles in GBM. Recent studies demonstrate that TAp73 (transcriptionally active p73) is required for stemness potential in glioblastoma stem cells, acting as a regulator of the balance between stemness and differentiation-dependent apoptosis. In GBM, altered TP73 function enables maintenance of stem-like properties resistant to differentiation-induced death. The presence of multiple pro-death and pro-differentiation genes in this GBM-associated gene set suggests that suppression of apoptotic pathways and cell cycle checkpoints is part of the malignant transformation process.",
      "significance_score": 0.70,
      "citations": [
        {
          "source_id": "22",
          "notes": "HRK is pro-apoptotic regulator of intrinsic pathway"
        },
        {
          "source_id": "35",
          "notes": "DACH1 functions as tumor suppressor through activation of cell cycle arrest and apoptosis genes"
        },
        {
          "source_id": "21",
          "notes": "TAp73 regulates stemness and apoptotic balance in GBM stem cells"
        }
      ],
      "supporting_genes": [
        "HRK",
        "DACH1",
        "DACH2",
        "TP73"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "BCL2",
          "BCL-XL",
          "BCL-W",
          "MCL1",
          "BAX",
          "BAK",
          "PUMA",
          "NOXA",
          "TP53",
          "p53",
          "p21",
          "MDM2",
          "Caspase 9",
          "Caspase 3"
        ],
        "citations": [
          {
            "source_id": "22",
            "notes": "HRK interacts with anti-apoptotic BCL2 family members to promote apoptosis"
          },
          {
            "source_id": "35",
            "notes": "DACH1 modulates p53-related transcriptional regulation"
          }
        ]
      }
    },
    {
      "program_name": "Retinoic Acid & MAPK-CaMKII Signaling Integration",
      "description": "This program encompasses genes mediating non-canonical retinoic acid (RA) signaling through cellular retinoic acid binding protein 1 (CRABP1). CRABP1 acts as a signalosome that integrates retinoic acid with MAPK (mitogen-activated protein kinase) and CaMKII (calmodulin-dependent protein kinase II) signaling. CRABP1 suppresses MAPK-dependent cell proliferation by competing with Ras for interaction with RAF kinase, dampening ERK activation. CRABP1 also dampens CaMKII over-activation that could trigger neuronal death. This integrated signaling pathway affects stem cell proliferation, cancer progression, and neuronal survival.",
      "atomic_biological_processes": [
        {
          "name": "Retinoic acid-mediated MAPK signal dampening",
          "citations": [
            {
              "source_id": "16",
              "notes": "CRABP1 competes with Ras to directly interact with RAF kinase, dampening MAPK signal propagation and reducing cell proliferation"
            }
          ],
          "genes": [
            "CRABP1"
          ]
        },
        {
          "name": "CaMKII over-activation suppression and neuroprotection",
          "citations": [
            {
              "source_id": "16",
              "notes": "CRABP1 competes with calmodulin to directly interact with CaMKII, dampening CaMKII over-activation and providing neuroprotection"
            }
          ],
          "genes": [
            "CRABP1"
          ]
        },
        {
          "name": "Cell cycle progression and G1 phase expansion",
          "citations": [
            {
              "source_id": "16",
              "notes": "CRABP1-mediated MAPK dampening suppresses cell cycle progression by expanding G1 phase"
            }
          ],
          "genes": [
            "CRABP1"
          ]
        },
        {
          "name": "Stem cell proliferation control",
          "citations": [
            {
              "source_id": "16",
              "notes": "CRABP1-deficient neural stem cells show enhanced proliferation; CRABP1 acts as tumor suppressor in stem cell populations"
            }
          ],
          "genes": [
            "CRABP1"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Cytoplasmic CRABP1-signaling protein complexes",
          "citations": [
            {
              "source_id": "16",
              "notes": "CRABP1 forms context-dependent complexes with RAF kinase and CaMKII to regulate signaling output"
            }
          ],
          "genes": [
            "CRABP1"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced MAPK-dependent proliferation through loss of CRABP1-mediated signal dampening",
        "Increased growth factor responsiveness and proliferative signaling",
        "Reduced retinoic acid-mediated differentiation and growth suppression",
        "Enhanced CaMKII over-activation potentially contributing to altered neuronal phenotype",
        "Increased neural stem cell and glioma stem cell proliferation",
        "Resistance to retinoic acid-mediated growth suppression"
      ],
      "evidence_summary": "CRABP1 (Cellular Retinoic Acid Binding Protein 1) functions as a critical mediator of non-canonical retinoic acid signaling that integrates RA with major cellular signaling cascades. CRABP1 forms RA-regulated signalsomes—stable complexes with specific signaling molecules—that function in a cell context-dependent manner. In embryonic stem cells and neural stem cells, CRABP1 competes directly with Ras for binding to RAF kinase at its Ras-binding domain, thereby dampening MAPK signal propagation and reducing cell proliferation. This CRABP1-mediated MAPK dampening suppresses cell cycle progression by expanding the G1 phase. In CRABP1-knockout mice, neural stem cells show expanded pools due to enhanced NSC proliferation in hippocampus and improved memory function, indicating that CRABP1 loss promotes stem cell proliferation. In cancer, CRABP1 loss would therefore enhance growth factor-dependent proliferation. Additionally, CRABP1 competes with calmodulin for direct interaction with CaMKII, thereby dampening CaMKII over-activation. Since over-activation of CaMKII is a major trigger of neuronal death and dysfunction, CRABP1-mediated dampening provides neuroprotection. In GBM, loss of CRABP1 would enhance both growth factor-dependent proliferation (through enhanced MAPK signaling) and alter calcium-dependent signaling through CaMKII, supporting tumor growth and potentially affecting neuronal differentiation.",
      "significance_score": 0.62,
      "citations": [
        {
          "source_id": "16",
          "notes": "Comprehensive review of CRABP1-mediated MAPK and CaMKII signaling in stem cells and cancer"
        }
      ],
      "supporting_genes": [
        "CRABP1"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "RAF",
          "MEK",
          "ERK1/2",
          "RAS",
          "Calmodulin",
          "CaMKII",
          "Retinoic acid",
          "RALDH",
          "RAR",
          "RXR"
        ],
        "citations": [
          {
            "source_id": "16",
            "notes": "CRABP1 interacts with RAF and CaMKII; retinoic acid is ligand for CRABP1 signalosome"
          }
        ]
      }
    },
    {
      "program_name": "Metabolic Reprogramming & Warburg Effect Activation",
      "description": "This program encompasses genes involved in metabolic reconfiguration toward aerobic glycolysis (Warburg effect) that characterizes GBM. Protein kinase C (PRKCA) signaling promotes metabolic reprogramming through MAPK pathway activation. Glycosyltransferases and metabolic enzymes (ST6GAL1, PCSK2, ADCY8, HSD11B2, PIP5K1B) support altered glucose, lipid, and nucleotide metabolism. The Warburg effect—preference for glycolysis over oxidative phosphorylation even under normoxia—supports GBM proliferation and contributes to therapy resistance. Hypoxia and metabolic stress activate transcription factors (HIF-1alpha) that drive expression of glycolytic genes.",
      "atomic_biological_processes": [
        {
          "name": "Aerobic glycolysis upregulation and Warburg effect",
          "citations": [
            {
              "source_id": "28",
              "notes": "GBM undergoes Warburg effect with upregulation of glycolytic genes; correlation between glycolytic gene expression and poor survival"
            }
          ],
          "genes": [
            "PRKCA",
            "ADCY8"
          ]
        },
        {
          "name": "Hypoxia-inducible factor signaling and metabolic adaptation",
          "citations": [
            {
              "source_id": "28",
              "notes": "Hypoxia-inducible factor (HIF-1alpha) stabilization drives glycolytic gene expression and metabolic adaptation to hypoxic tumor microenvironment"
            }
          ],
          "genes": [
            "HSD11B2"
          ]
        },
        {
          "name": "Protein kinase C signaling in metabolic reprogramming",
          "citations": [
            {
              "source_id": "14",
              "notes": "PKC family members play essential role in transducing signals related to cell cycle, differentiation, and metabolic reprogramming in GBM"
            }
          ],
          "genes": [
            "PRKCA"
          ]
        },
        {
          "name": "Nucleotide and lipid metabolism dysregulation",
          "citations": [
            {
              "source_id": "28",
              "notes": "GBM shows reprogramming of nucleotide synthesis and lipid metabolism supporting increased proliferation and therapy resistance"
            }
          ],
          "genes": [
            "PCSK2",
            "ST6GAL1",
            "PIP5K1B"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Protein kinase C signaling complexes and kinase pathways",
          "citations": [
            {
              "source_id": "14",
              "notes": "PKC isozymes transduce signals through MAPK and PI3K pathways affecting cell proliferation and metabolism"
            }
          ],
          "genes": [
            "PRKCA"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced glucose uptake and glycolytic flux supporting rapid ATP generation",
        "Increased lactate production and acidic microenvironment",
        "Resistance to radiotherapy and chemotherapy through metabolic support of tumor survival",
        "Enhanced lipid and nucleotide synthesis supporting rapid cell division",
        "Reduced oxidative stress from decreased mitochondrial respiration",
        "Support for hypoxic regions of tumor through glycolytic ATP production",
        "Altered tumor microenvironment acidification affecting immune infiltration"
      ],
      "evidence_summary": "Metabolic reprogramming is a hallmark of glioblastoma and a key mechanism of therapy resistance. GBM cells preferentially utilize aerobic glycolysis (Warburg effect) rather than oxidative phosphorylation, even under normoxic conditions. Multiple studies demonstrate significant correlation between upregulation of glycolytic genes and poor survival in GBM patients. Hypoxia is a significant activator of metabolic reprogramming, with hypoxia-inducible factor-1 alpha (HIF-1alpha) stabilized in low oxygen conditions and translocating to the nucleus where it activates glycolytic genes. GBM also shows dysregulation of nucleotide synthesis and lipid metabolism pathways. Protein kinase C (PKC) family members play essential roles in transducing signals that drive proliferation, differentiation, and metabolic reconfiguration in neural stem cells and glioma stem cells. PKC signaling engages the Ras-MAPK and PI3K-Akt pathways that are critical for metabolic reprogramming. Importantly, lactate dehydrogenase A (LDHA) and anaerobic glycolysis contribute to GBM resistance to both radiotherapy and chemotherapy. Glycolysis inhibition through LDHA gene silencing increases radiation sensitivity and response to temozolomide (TMZ). Inhibition of pyruvate dehydrogenase kinase (PDK) and stimulation of mitochondrial pyruvate dehydrogenase (PDH) can revert the Warburg effect, leading to GBM cytotoxicity and increased TMZ sensitivity. The presence of metabolic enzymes and PKC signaling genes in this GBM-associated gene set indicates that metabolic reprogramming is an active process driven by dysregulated oncogenic signaling.",
      "significance_score": 0.68,
      "citations": [
        {
          "source_id": "28",
          "notes": "Comprehensive review of metabolic reprogramming in GBM including Warburg effect, nucleotide and lipid metabolism dysregulation"
        },
        {
          "source_id": "14",
          "notes": "PKC signaling pathways in GBM metabolic reprogramming and cell cycle control"
        }
      ],
      "supporting_genes": [
        "PRKCA",
        "ADCY8",
        "HSD11B2",
        "PCSK2",
        "ST6GAL1",
        "PIP5K1B",
        "DUOX1",
        "SDS"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "GLUT1",
          "SLC2A1",
          "HIF-1alpha",
          "HIF1A",
          "LDHA",
          "PDK1",
          "PDH",
          "PKM2",
          "PFKFB3",
          "Hexokinase",
          "Pyruvate kinase",
          "Lactate transporter",
          "MCT1"
        ],
        "citations": [
          {
            "source_id": "28",
            "notes": "GLUT1 glucose transporter and glycolytic enzymes are core components of Warburg effect dysregulation in GBM"
          }
        ]
      }
    },
    {
      "program_name": "Extracellular Matrix Remodeling & Cell Migration",
      "description": "This program encompasses genes encoding extracellular matrix (ECM) proteins and enzymes that modify ECM structure, enabling GBM cell migration and invasion. Matrix stiffening through deposition of structural proteins (FRAS1, HMCN1, SPOCK1, SVEP1) and glycosaminoglycan modifications (B3GAT2, B3GLCT, NDST4, HS3ST5) promotes glioma cell invasiveness. ECM stiffness activates mechanotransduction pathways that condition glioma cells for enhanced invasion. Sialyltransferases (ST6GAL1) and other glycosyltransferases modify cell surface glycoproteins affecting cell-cell and cell-matrix interactions. Hyaluronidases (CEMIP2) degrade hyaluronic acid facilitating cell migration.",
      "atomic_biological_processes": [
        {
          "name": "Extracellular matrix protein deposition and stiffening",
          "citations": [
            {
              "source_id": "25",
              "notes": "Extracellular matrix stiffening correlates with GBM invasion; ECM stiffness conditions glioma cells for enhanced invasiveness"
            }
          ],
          "genes": [
            "FRAS1",
            "HMCN1",
            "SPOCK1",
            "SVEP1",
            "CRIM1"
          ]
        },
        {
          "name": "Glycosaminoglycan synthesis and ECM composition",
          "citations": [
            {
              "source_id": "12",
              "notes": "Glycosyltransferases and sulfotransferases regulate glycosaminoglycan composition affecting ECM properties"
            }
          ],
          "genes": [
            "B3GAT2",
            "B3GLCT",
            "NDST4",
            "HS3ST5"
          ]
        },
        {
          "name": "Cell surface glycoprotein modification and adhesion",
          "citations": [
            {
              "source_id": "7",
              "notes": "Glycosylation of CAMs affects cell adhesion and cell-to-cell communication"
            }
          ],
          "genes": [
            "ST6GAL1"
          ]
        },
        {
          "name": "Hyaluronic acid degradation and cell migration",
          "citations": [
            {
              "source_id": "25",
              "notes": "Hyaluronidases degrade ECM hyaluronic acid facilitating cell migration through tissue"
            }
          ],
          "genes": [
            "CEMIP2"
          ]
        },
        {
          "name": "Mechanotransduction and integrin signaling",
          "citations": [
            {
              "source_id": "25",
              "notes": "ECM stiffness activates mechanotransduction through integrin and focal adhesion kinase signaling promoting invasion"
            }
          ],
          "genes": [
            "ANTXR2"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Structural extracellular matrix proteins and proteoglycans",
          "citations": [
            {
              "source_id": "25",
              "notes": "Fibrillar collagens, proteoglycans, and other structural proteins comprise tumor ECM"
            }
          ],
          "genes": [
            "FRAS1",
            "HMCN1",
            "SPOCK1",
            "SVEP1"
          ]
        },
        {
          "name": "Cell surface receptor-ECM interaction complexes",
          "citations": [
            {
              "source_id": "25",
              "notes": "Integrin heterodimers and other receptors mediate cell-matrix contacts transmitting mechanotransduction signals"
            }
          ],
          "genes": [
            "ANTXR2"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced ECM stiffness promoting glioma cell invasion and migration",
        "Altered cell-matrix adhesion dynamics reducing stationary cell behavior",
        "Increased mechanotransduction signaling activating pro-invasive pathways",
        "Reduced physical barriers to cell migration through ECM remodeling",
        "Enhanced glycosaminoglycan composition modulating ECM viscoelasticity",
        "Altered cell surface glycosylation affecting cell-cell adhesion and immune recognition",
        "Facilitated tumor cell dissemination through ECM degradation"
      ],
      "evidence_summary": "The extracellular matrix surrounding glioblastoma cells plays a critical role in promoting invasiveness and metastatic spread. ECM stiffness has been demonstrated to correlate with tumor invasion in various cancer types, including glioblastoma. Physical stiffening of the ECM through deposition of fibrillar collagen and other structural proteins activates mechanotransduction pathways that condition glioma cells for enhanced invasion. This 'stiffness-induced' phenotype is characterized by increased invasive capacity and altered gene expression profiles. ECM composition is actively remodeled by tumor cells and associated stromal cells through synthesis of structural proteins, glycosaminoglycans, and proteoglycans. Glycosyltransferases and sulfotransferases regulate the composition of glycosaminoglycans including heparan sulfate and chondroitin sulfate, which affects ECM properties. Cell surface glycoproteins, including cell adhesion molecules, are modified by sialyltransferases that affect their adhesive properties and recognition by immune cells. Hyaluronidases degrade hyaluronic acid, a major ECM component, facilitating cell migration through tissue. The presence of multiple ECM-related genes in this GBM-associated gene set indicates that active ECM remodeling is part of the malignant GBM phenotype, enabling enhanced invasiveness and dissemination.",
      "significance_score": 0.74,
      "citations": [
        {
          "source_id": "25",
          "notes": "Comprehensive characterization of ECM stiffness conditioning glioblastoma cells for long-term invasion"
        },
        {
          "source_id": "27",
          "notes": "Tumor microenvironment components including ECM interact with GBM cells to promote progression"
        }
      ],
      "supporting_genes": [
        "FRAS1",
        "HMCN1",
        "SPOCK1",
        "SVEP1",
        "CEMIP2",
        "B3GAT2",
        "B3GLCT",
        "NDST4",
        "HS3ST5",
        "ST6GAL1",
        "ANTXR2",
        "CRIM1"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "Collagen alpha-1",
          "COL1A1",
          "Integrin alpha-V",
          "Integrin beta-1",
          "Focal adhesion kinase",
          "FAK",
          "Paxillin",
          "Src kinase",
          "Matrix metalloproteinases",
          "MMP2",
          "MMP9",
          "ADAMTS",
          "TIMP",
          "Versican",
          "Perlecan"
        ],
        "citations": [
          {
            "source_id": "25",
            "notes": "Collagen and integrin family proteins are core ECM components and mechanotransducers"
          }
        ]
      }
    },
    {
      "program_name": "G-Protein-Coupled Receptor & Neuroendocrine Signaling",
      "description": "This program encompasses G-protein-coupled receptors (GPCRs) and associated signaling that drive glioma cell proliferation and survival. SSTR2 (somatostatin receptor 2) is a GPCR highly expressed in neuroendocrine tumors but expression can be downregulated. Recent studies show that SSTR2 interacts with Wnt pathway protein Dvl1 in a ligand-independent manner, targeting SSTR2 for lysosomal degradation. GRK5 (G-protein receptor kinase 5) phosphorylates GPCRs affecting their signaling output and internalization. Adenylyl cyclase (ADCY8) produces cAMP, a key second messenger in GPCR signaling. These pathways affect proliferation, differentiation, and metabolism in GBM.",
      "atomic_biological_processes": [
        {
          "name": "Somatostatin receptor 2 signaling and therapeutic response",
          "citations": [
            {
              "source_id": "17",
              "notes": "SSTR2 is GPCR highly expressed in neuroendocrine tumors; Dvl1-dependent degradation regulates SSTR2 expression independent of agonist"
            }
          ],
          "genes": [
            "SSTR2"
          ]
        },
        {
          "name": "G-protein receptor kinase regulation of GPCR desensitization",
          "citations": [
            {
              "source_id": "17",
              "notes": "GRK phosphorylates GPCRs including SSTR2 affecting internalization and recycling"
            }
          ],
          "genes": [
            "GRK5"
          ]
        },
        {
          "name": "cAMP generation and second messenger signaling",
          "citations": [
            {
              "source_id": "17",
              "notes": "Adenylyl cyclase generates cAMP downstream of GPCR signaling; cAMP affects cell proliferation and differentiation"
            }
          ],
          "genes": [
            "ADCY8"
          ]
        },
        {
          "name": "Wnt-Dvl-mediated GPCR downregulation",
          "citations": [
            {
              "source_id": "17",
              "notes": "Wnt pathway protein Dvl1 targets SSTR2 for lysosomal degradation independent of agonist; Wnt inhibitors boost SSTR2 expression"
            }
          ],
          "genes": [
            "SSTR2"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Seven-transmembrane G-protein-coupled receptor (GPCR) complexes",
          "citations": [
            {
              "source_id": "17",
              "notes": "SSTR2 forms functional GPCR heterotrimeric G-protein complexes"
            }
          ],
          "genes": [
            "SSTR2"
          ]
        },
        {
          "name": "G-protein receptor kinase regulatory complexes",
          "citations": [
            {
              "source_id": "17",
              "notes": "GRK5 phosphorylates and desensitizes GPCRs including SSTR2"
            }
          ],
          "genes": [
            "GRK5"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Altered GPCR signaling affecting cell proliferation and differentiation balance",
        "Enhanced Wnt-Dvl mediated GPCR degradation reducing signaling capacity",
        "Modified cAMP signaling affecting metabolic and proliferative responses",
        "Altered neuroendocrine differentiation state",
        "Potential therapeutic opportunity through Wnt inhibitors boosting SSTR2 expression",
        "Dysregulated GPCR desensitization affecting sustained growth signaling"
      ],
      "evidence_summary": "G-protein-coupled receptors (GPCRs) regulate diverse aspects of cell physiology including proliferation, differentiation, and migration. SSTR2 (somatostatin receptor 2) is a GPCR commonly overexpressed in neuroendocrine tumors, where it serves as a target for therapeutic interventions. However, not all neuroendocrine tumors express SSTR2, and expression can be downregulated with prolonged agonist treatment. Recent studies identified a mechanism by which the Wnt pathway protein Dvl1 (Dishevelled 1) binds to SSTR2 in a ligand-independent manner and targets the receptor for lysosomal degradation, reducing steady-state SSTR2 expression. This Dvl1-mediated degradation can be stimulated by overexpression of Wnt ligands. Importantly, treatment with Wnt pathway inhibitors can boost SSTR2 expression in neuroendocrine tumor cells, suggesting potential therapeutic strategies. GRK5 (G-protein receptor kinase 5) phosphorylates GPCRs following activation, leading to receptor desensitization and internalization. Adenylyl cyclase (ADCY8) catalyzes the synthesis of cAMP from ATP, producing a key second messenger that affects cell proliferation and differentiation downstream of GPCR activation. The presence of GPCR signaling genes in this GBM-associated gene set suggests that altered GPCR-mediated signaling contributes to glioma biology, potentially through effects on proliferation, neuroendocrine differentiation, or metabolic state.",
      "significance_score": 0.58,
      "citations": [
        {
          "source_id": "17",
          "notes": "Detailed characterization of SSTR2 regulation by Dvl1-mediated lysosomal degradation and Wnt pathway interactions"
        }
      ],
      "supporting_genes": [
        "SSTR2",
        "GRK5",
        "ADCY8"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "Somatostatin",
          "SST",
          "Wnt ligands",
          "Wnt1-10",
          "Frizzled receptors",
          "FZD",
          "LRP5/6",
          "GSK3beta",
          "Beta-catenin",
          "CTNNB1",
          "TCF",
          "LEF",
          "Heterotrimeric G proteins",
          "Gs",
          "Gi/o",
          "PKA"
        ],
        "citations": [
          {
            "source_id": "17",
            "notes": "Somatostatin is SSTR2 ligand; Wnt ligands activate Dvl1-mediated signaling; heterotrimeric G proteins are downstream effectors"
          }
        ]
      }
    }
  ],
  "version": "1.0"
}
```

## Citations

1. https://pubmed.ncbi.nlm.nih.gov/27583705/
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC4930921/
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC11040297/
4. https://www.nature.com/articles/s41586-024-08579-3
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC2913707/
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC4522676/
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC4564344/
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC117569/
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC3288821/
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC2774558/
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC5545892/
12. https://en.wikipedia.org/wiki/Solute_carrier_family
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC10842032/
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC8067000/
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC9953585/
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC9003107/
17. https://pubmed.ncbi.nlm.nih.gov/36965619/
18. https://pubmed.ncbi.nlm.nih.gov/29107289/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC11490338/
20. https://pubmed.ncbi.nlm.nih.gov/30312684/
21. https://febs.onlinelibrary.wiley.com/doi/10.1002/1878-0261.13694
22. https://pubmed.ncbi.nlm.nih.gov/30774992/
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC3767545/
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC3787156/
25. https://pubmed.ncbi.nlm.nih.gov/40973065/
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC4248069/
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC10034917/
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC11897528/
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC6116191/
30. https://www.nature.com/articles/s41467-023-41730-8
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC7862665/
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC4669798/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC12631407/
34. https://pmc.ncbi.nlm.nih.gov/articles/PMC9485243/
35. https://pmc.ncbi.nlm.nih.gov/articles/PMC2778848/
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC5768392/
37. https://pubmed.ncbi.nlm.nih.gov/35104247/
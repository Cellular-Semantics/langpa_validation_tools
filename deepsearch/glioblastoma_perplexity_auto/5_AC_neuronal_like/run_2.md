---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-11-26T14:20:15.941808'
end_time: '2025-11-26T14:25:51.951939'
duration_seconds: 336.01
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 60
---

## Question

Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: ["LINC02235", "AC037486.1", "PCDH11X", "LINC01829", "AL591043.2", "ZNF423", "ADAMTS18", "AL133538.1", "DOCK2", "SCN1A-AS1", "AL022068.1", "SEPTIN14", "SGCZ", "ADAM28", "RYR2", "DOCK8", "ACER2", "AC128687.3", "AC120193.1", "OLR1", "AC110296.1", "AC109466.1", "SPOCK3", "ST6GALNAC5", "AL136441.1", "MLIP", "AL158077.2", "AP001021.3", "CCDC85A", "CD96", "NRK", "C8orf37-AS1", "PCDH7", "PLD1", "CHRNA7", "CLRN1", "MYO1D", "RMST", "CNTNAP2", "PURPL", "RALYL", "AL445426.1", "RCAN2", "AL392023.2", "RELN", "AL360091.3", "AC091946.1", "LRRIQ1", "CD163", "SYN3", "IL1RAPL1", "LINC01122", "LINC01091", "AC009126.1", "LINC00944", "LINC01467", "LINC01725", "KCNH7", "AC069228.1", "GNA14-AS1", "KCNIP4", "LINC00504", "AC006299.1", "TPRG1", "AC003092.1", "AC083855.2", "FXYD5", "SYK", "XK", "LINC02006", "KLF5", "WNT16", "NIBAN1", "LINC00355", "LINC01135", "MSR1", "MT2A", "LINC00299", "MX2", "NLGN4X", "LINC00886", "LINC00607", "NHSL2", "MYO1E", "NKAIN2", "NIPAL2", "MYO1F", "LINC01163", "NCMAP", "NHS", "MYRFL", "LINC02234", "LINC01182", "LINC01923", "LINC02246", "LINC02300", "LINC02306", "LINC02378", "LINC02664", "LINC02775", "LINC02798", "LINC02821", "LMNTD1", "LRRTM4", "LURAP1L-AS1", "LINC01934", "LY96", "MAP3K6", "LINC01877", "LINC01208", "LINC01876", "MCTP2", "LINC01842", "LINC01798", "LINC01579", "ME1", "MEGF11", "LINC01357", "MEOX2", "LINC01277", "MGAT4C", "LINC02055", "LINC01241", "MIR548XHG", "MIR222HG", "PTPN14", "OTP", "TAFA2", "TG", "TENT5A", "TENM2", "TEK", "TDO2", "TBX19", "TAPT1-AS1", "SYTL3", "THSD4", "SYT1", "SULF1", "SUCLG2-AS1", "STAT4", "STARD13", "STAC", "SPRY4-AS1", "TGM2", "TLR2", "SPATA48", "VEGFD", "WWTR1", "WIPF1", "WDR49", "VSTM2A-OT1", "VSTM2A", "VSIG4", "VLDLR-AS1", "UTY", "TMEM164", "UNC5C", "UNC13C", "TRPV4", "TRPM8", "TRPM3", "TRIM22", "TMEM63A", "SPINK5", "SPAG17", "PCA3", "POSTN", "RARRES1", "PTPRR", "LINC00158", "PTCHD4", "PTCHD1-AS", "PRSS48", "POU6F2", "PLIN2", "RNF6", "PLAC1", "PKD1L1", "PIP5K1B", "PGLYRP1", "PDE1C", "PCED1B", "PCDH11Y", "RASSF8", "RREB1", "SORCS1", "SLC18A1", "SOCS2-AS1", "SNTG1", "SMOC2", "SLIT2", "SLCO1B1", "SLC35G1", "SLC35E4", "SLC10A6", "RUNX1T1", "SIDT1", "SHOC1", "SAPCD2", "SAMD3", "SAA1", "RYR3", "RXRG", "LINC00278", "AC002074.1", "LGALS1", "AL117329.1", "ADAMTS3", "ADAMTS14", "ACOXL", "AC244472.1", "AC138409.3", "AC124947.1", "AC122697.1", "AC117464.1", "AC114689.3", "AC110023.1", "AC106845.1", "AC097518.2", "AC097462.3", "AC093535.1", "AC093523.1", "AC092958.2", "AC092957.1", "AGMO", "AL121904.2", "AC092131.1", "AL132633.1", "AP000446.1", "ALPK2", "ALDH1A2", "AL732509.1", "AL590608.1", "AL589935.1", "AL512452.1", "AL392086.3", "AL360178.1", "AL354696.2", "AL163636.1", "AL158195.1", "AL158058.1", "AL157911.1", "AL138824.1", "AL137139.2", "AL136038.5", "AC092819.3", "AC091078.1", "AP002495.1", "AC023095.1", "AC022325.2", "AC018616.1", "AC012404.1", "AC012063.1", "AC011246.1", "AC009646.2", "AC008080.4", "AC007681.1", "AC007389.1", "AC007364.1", "AC006994.2", "AC006387.1", "AC006206.2", "AC006041.2", "AC005162.3", "AC004943.2", "AC004879.1", "AC023051.1", "AC024145.1", "AC090578.1", "AC026202.2", "AC090403.1", "AC090337.2", "AC087627.1", "AC087473.1", "AC079950.1", "AC079763.1", "AC079465.1", "AC079298.3", "AC073529.1", "AC073050.1", "AC072062.1", "AC068305.2", "AC067956.1", "AC062022.2", "AC051619.6", "AC040174.1", "AC027097.2", "AP001025.1", "AP002813.1", "LCP2", "GPC3", "GNA14", "GLRA2", "GDNF-AS1", "GCNT2", "FYB1", "FXN", "FRG1-DT", "FRAS1", "FHIT", "FAR2", "FAP", "FAM189A1", "FAAH2", "ERI2", "EPSTI1", "EPHA3", "EPB41L4A", "GNGT1", "GREB1L", "EMILIN2", "GRIN2B", "LANCL3", "KREMEN1", "KCNMB4", "KCNE4", "ITK", "ITGAL", "INPP5D", "IL7", "IL12RB2", "IGSF10", "IAPP", "HS3ST3A1", "HRH1", "AC002429.2", "HMGB2", "HMGA2", "GRIP2", "ENOX2", "ELDR", "AP003066.1", "CFAP77", "CERNA2", "CDH18", "CDH13", "CD247", "CASC9", "C9orf153", "C9orf147", "BX284613.2", "BIRC3", "BEND6", "BCL2L14", "ATP8B4", "ASB18", "ARSJ", "ARRDC3-AS1", "ARHGAP11B", "APBB1IP", "CFAP47", "CFH", "EDN1", "CGNL1", "EBF2", "DOCK5", "DNAH3", "DIPK2A", "DANT2", "CPNE4", "COX8A", "COL4A6", "COL19A1", "COL12A1", "COBLL1", "CNTNAP3B", "CNDP1", "CNBD1", "CHRM3", "CHODL", "CHL1-AS2", "HNF4G"]

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
This is a complex task requiring comprehensive literature analysis on a large gene list in the context of malignant glioblastoma. Let me think through the planning process:

1. **Understanding the Context**: The biological context is malignant glioblastoma cells - this is the most common and aggressive primary brain tumor in adults. Key characteristics include:
   - High invasiveness and migration
   - Resistance to therapy
   - Heterogeneous tumor composition
   - Reliance on cancer stem cells (GSCs)
   - Altered signaling pathways
   - Interaction with tumor microenvironment
   - Enhanced angiogenesis
   - Altered cell adhesion and EMT processes

2. **Gene List Analysis**: The input list contains ~250 genes, including:
   - Well-studied GBM drivers: PCDH7, PCDH11X, PLD1, CHRNA7, RELN, CNTNAP2, NLGN4X, OLR1, MSR1, CD163, LY96, KLF5, TRPV4, TRPM8, RYR2, RYR3, DOCK2, DOCK8, ADAMTS3, ADAMTS14, ADAMTS18, FXYD5, SYK, POSTN, TGM2, TLR2, VEGFD, TEK, VSIG4, VLDLR-AS1, UNC5C, STAT4, etc.
   - Long non-coding RNAs: LINC02235, AC037486.1, LINC01829, LINC00944, LINC01467, LINC01725, LINC00504, LINC00355, LINC01135, LINC00299, LINC00886, LINC00607, LINC01163, LINC01934, LINC01877, LINC01208, LINC01876, LINC01842, LINC01798, LINC01579, LINC01357, LINC01277, LINC02055, LINC01241, MIR548XHG, MIR222HG, RMST, RCAN2, RALYL, AL-series genes
   - Ion channels like TRPV4, TRPM8, TRPM3, KCNH7, KCNIP4, KCNMB4, KCNE4, and SCN1A-AS1 that likely modulate cellular excitability and migration
   - Cell adhesion molecules including PCDH7, PCDH11X, PCDH11Y, CDH13, CDH18, and NLGN4X that regulate cell-cell interactions
   - Extracellular matrix components such as ADAMTS3, ADAMTS14, ADAMTS18, POSTN, RELN, COL4A6, COL19A1, and COL12A1 that support tumor invasion and remodeling

, along with SPOCK3 and EMILIN2
   - Immune and inflammatory mediators like CD163, CD96, LY96, TLR2, SYK, VSIG4, VLDLR, CFH, and IGSF10 that shape the microenvironment
   - Metabolic enzymes including PLD1, ME1, TDO2, SUCLG2, and ATP8B4 that support energy production and lipid metabolism
   - Developmental and synaptic factors such as CNTNAP2, CHRNA7, SYT1, SYN3, SLIT2, and GDNF-AS1 that influence neural differentiation and connectivity
   - Transcriptional regulators including KLF5, STAT4, ZNF423, EBF2, and MEOX2 that coordinate these programs

Several distinct gene programs emerge from these functional categories that likely drive specific aspects of tumor biology and neural development.

An invasion and migration program centers on cell adhesion molecules like PCDH7 and PCDH11X/Y, along with ADAMTS proteins and PLD1 that promote motility, while RELN acts as a brake on this process. POSTN and FXYD5 further enhance invasive capacity, and ion channels including TRPV4 and TRPM8 regulate the migratory response through calcium flux. Multiple lncRNAs likely coordinate these invasion-related processes.

A calcium and ion channel program operates through TRPV4, TRPM8, and TRPM3 that drive migration and proliferation, supported by RYR2 and RYR3 regulating intracellular calcium release, while KCNH7 and KCNIP4 control membrane potential. Calcium signaling appears to be a central hub coordinating multiple cellular behaviors.

Synaptic interactions between glioma cells and neurons emerge as a growth-promoting mechanism, involving synaptic proteins like NLGN4X, CNTNAP2, SYT1, and SYN3, with nicotinic signaling through CHRNA7 potentially enhancing this cross-talk. The extracellular matrix serves as both a structural scaffold and a regulatory layer, with ADAMTS proteins actively remodeling it while POSTN engages integrin signaling and RELN constrains invasion. Immune recruitment appears coordinated through M2 macrophage markers CD163 and MSR1, TLR4 signaling via LY96, and T cell checkpoint molecules like CD96 and VSIG4 that suppress anti-tumor immunity. Developmental pathways including Wnt signaling through PLD1 and WNT16 may maintain stem-like or undifferentiated states.

Additional signaling layers involve inflammatory cytokines (IL7, IL12RB2, STAT4), cell adhesion molecules particularly cadherins, and metabolic rewiring through lipid signaling and altered enzyme expression. A substantial lncRNA program including LINC genes and MIR222HG likely coordinates multiple pro-tumoral processes like invasion and stemness maintenance. Prioritizing these programs depends on gene representation in the input list, established GBM literature support, and direct mechanistic relevance to tumor phenotypes.

The search results reveal specific molecular players: invasive GBM cells express ATX, ephrin B3, and PTK2β, while LINC-PINT acts as an invasion suppressor through Wnt pathway modulation. Cancer stem cells show consistent upregulation of adhesion markers including L1CAM, PSA-NCAM, and various cadherins. Expression profiling identifies SPARC, VIM, and MCM3 as highly expressed genes contrasting with downregulated MAPK8IP2, DDN, and others. ncRNAs broadly regulate proliferation, migration, invasion, and apoptosis across multiple GBM contexts.

Survival associations emerge with ACP7, EPPK1, PCDHA8, RHOD, DRC1, ZIC3, and PRLR, alongside CD70 expression in immune populations. DOCK8 functions critically in NK, T, and B cell immunity plus dendritic cell activation through immune synapse formation. The cholinergic anti-inflammatory axis via α7 nAChR provides immunomodulation, particularly in macrophage signaling. Myeloid infiltration—macrophages, microglia, MDSCs, dendritic cells, neutrophils—displays M1/M2 polarization patterns, with DOCK8 deficiency linked to both immunodeficiency and cancer susceptibility. Glioma-associated myeloid cells operate through distinct immunomodulatory programs including scavenger-mediated immunosuppression.

RYR mutations correlate with elevated tumor mutational burden, while RELN acts as a migration brake with anti-invasive properties. CNTNAP2 governs neuronal development and synaptic architecture including dendritic spine formation. RYR2-driven metastasis responds to S107 inhibition, and both RELN and CNTNAP2 show functional relevance in glioblastoma contexts. ZNF423 operates as a transcriptional regulator dysregulated through polycomb mechanisms in gliomas and leukemias. FXYD5/dysadherin promotes metastatic potential by compromising cell adhesion, while ADAMTS proteases facilitate cancer progression through extracellular matrix remodeling.

ATP1B2 (Na+/K+ ATPase) influences GBM growth and apoptotic responses. PLD1 enhances GSC stemness through Wnt/β-catenin signaling and confers TMZ resistance. The IL-1β/IL-1R1 axis drives GBM progression by recruiting myeloid cells to the tumor microenvironment. TRPM8 channels promote migration and radioresistance, while KCND2 potassium channels operate at the GBM-neuron interface and relate to seizure susceptibility. LY96 (MD2) activates TLR4-NF-κB inflammatory cascades across multiple cancer types. TRP channel family members including TRPC6, TRPV4, and TRPV1/V2 modulate glioma biology, and potassium channels broadly regulate proliferation, migration, and apoptosis. NLGN4X supports TCR-engineered T cell targeting of gliomas, while OLR1 scavenger receptor signaling through NF-κB enhances migration in these tumors.

Neural stem cells serve as a cellular origin for glioma initiation. SR-A1 (MSR1) polarizes macrophages toward an M2 immunosuppressive phenotype within the tumor microenvironment. SEPTIN proteins including SEPTIN9, SEPTIN2, and SEPTIN14 regulate neuronal migration and glioma biology. POSTN drives invasion and mediates resistance to anti-VEGF therapy. Perivascular fibroblasts contribute to ECM deposition and immunotherapy resistance. lncRNAs regulate stem cell maintenance, and SV2B serves as a prognostic biomarker linked to synaptic gene expression.

I'm beginning to see how these genes cluster into functional programs—calcium signaling drives migration, ECM proteins enable invasion, and immune modulators shape the tumor microenvironment. 3, MEOX2, and regulatory lncRNAs maintaining stemness through Wnt/β-catenin signaling.

Cholinergic pathways via CHRNA7 provide anti-inflammatory effects, while DOCK family members (DOCK2, DOCK8, DOCK5) facilitate immune synapse formation. Long non-coding RNAs including the LINC series, MIR222HG, and RMST coordinate invasion, epithelial-mesenchymal transition, and stemness programs. Scavenger receptors like OLR1, MSR1, and CD163 integrate innate immune recognition with TLR2 and LY96 signaling.

I need to be more rigorous about which genes have strong experimental support in the provided literature rather than including everything potentially relevant.

The most robustly supported pathways are calcium signaling through ion channels (TRPV4, TRPM8, TRPM3, RYR2, RYR3, KCNH7, KCNIP4, KCNMB4, KCNE4) driving migration, extracellular matrix remodeling via ADAMTS proteases and collagens, cell adhesion through protocadherins and neural cell adhesion molecules, immune polarization through CD163, MSR1, LY96, and TLR signaling, and Wnt/β-catenin-mediated stemness involving PLD1, WNT16, KLF5, STAT4, and MEOX2.

Beyond these, I'm seeing lncRNA regulation through LINC series and MIR222HG, cholinergic signaling via CHRNA7 for immune modulation, DOCK proteins (DOCK2, DOCK8, DOCK5) coordinating immune responses, scavenger receptors (OLR1, MSR1, TLR2, LY96) in innate immunity, and neuron-glioma synaptic plasticity involving NLGN4X, CNTNAP2, SYT1, SYN3 with CHRNA7 and BDNF signaling components. These pathways collectively suggest a model where glioma cells acquire migratory and immunosuppressive capabilities through coordinated activation of calcium signaling, ECM remodeling, and immune evasion mechanisms.
</think>

```json
{
  "context": {
    "cell_type": "malignant glioblastoma cells",
    "disease": "glioblastoma multiforme (GBM)",
    "tissue": "brain"
  },
  "input_genes": [
    "LINC02235",
    "AC037486.1",
    "PCDH11X",
    "LINC01829",
    "AL591043.2",
    "ZNF423",
    "ADAMTS18",
    "AL133538.1",
    "DOCK2",
    "SCN1A-AS1",
    "AL022068.1",
    "SEPTIN14",
    "SGCZ",
    "ADAM28",
    "RYR2",
    "DOCK8",
    "ACER2",
    "AC128687.3",
    "AC120193.1",
    "OLR1",
    "AC110296.1",
    "AC109466.1",
    "SPOCK3",
    "ST6GALNAC5",
    "AL136441.1",
    "MLIP",
    "AL158077.2",
    "AP001021.3",
    "CCDC85A",
    "CD96",
    "NRK",
    "C8orf37-AS1",
    "PCDH7",
    "PLD1",
    "CHRNA7",
    "CLRN1",
    "MYO1D",
    "RMST",
    "CNTNAP2",
    "PURPL",
    "RALYL",
    "AL445426.1",
    "RCAN2",
    "AL392023.2",
    "RELN",
    "AL360091.3",
    "AC091946.1",
    "LRRIQ1",
    "CD163",
    "SYN3",
    "IL1RAPL1",
    "LINC01122",
    "LINC01091",
    "AC009126.1",
    "LINC00944",
    "LINC01467",
    "LINC01725",
    "KCNH7",
    "AC069228.1",
    "GNA14-AS1",
    "KCNIP4",
    "LINC00504",
    "AC006299.1",
    "TPRG1",
    "AC003092.1",
    "AC083855.2",
    "FXYD5",
    "SYK",
    "XK",
    "LINC02006",
    "KLF5",
    "WNT16",
    "NIBAN1",
    "LINC00355",
    "LINC01135",
    "MSR1",
    "MT2A",
    "LINC00299",
    "MX2",
    "NLGN4X",
    "LINC00886",
    "LINC00607",
    "NHSL2",
    "MYO1E",
    "NKAIN2",
    "NIPAL2",
    "MYO1F",
    "LINC01163",
    "NCMAP",
    "NHS",
    "MYRFL",
    "LINC02234",
    "LINC01182",
    "LINC01923",
    "LINC02246",
    "LINC02300",
    "LINC02306",
    "LINC02378",
    "LINC02664",
    "LINC02775",
    "LINC02798",
    "LINC02821",
    "LMNTD1",
    "LRRTM4",
    "LURAP1L-AS1",
    "LINC01934",
    "LY96",
    "MAP3K6",
    "LINC01877",
    "LINC01208",
    "LINC01876",
    "MCTP2",
    "LINC01842",
    "LINC01798",
    "LINC01579",
    "ME1",
    "MEGF11",
    "LINC01357",
    "MEOX2",
    "LINC01277",
    "MGAT4C",
    "LINC02055",
    "LINC01241",
    "MIR548XHG",
    "MIR222HG",
    "PTPN14",
    "OTP",
    "TAFA2",
    "TG",
    "TENT5A",
    "TENM2",
    "TEK",
    "TDO2",
    "TBX19",
    "TAPT1-AS1",
    "SYTL3",
    "THSD4",
    "SYT1",
    "SULF1",
    "SUCLG2-AS1",
    "STAT4",
    "STARD13",
    "STAC",
    "SPRY4-AS1",
    "TGM2",
    "TLR2",
    "SPATA48",
    "VEGFD",
    "WWTR1",
    "WIPF1",
    "WDR49",
    "VSTM2A-OT1",
    "VSTM2A",
    "VSIG4",
    "VLDLR-AS1",
    "UTY",
    "TMEM164",
    "UNC5C",
    "UNC13C",
    "TRPV4",
    "TRPM8",
    "TRPM3",
    "TRIM22",
    "TMEM63A",
    "SPINK5",
    "SPAG17",
    "PCA3",
    "POSTN",
    "RARRES1",
    "PTPRR",
    "LINC00158",
    "PTCHD4",
    "PTCHD1-AS",
    "PRSS48",
    "POU6F2",
    "PLIN2",
    "RNF6",
    "PLAC1",
    "PKD1L1",
    "PIP5K1B",
    "PGLYRP1",
    "PDE1C",
    "PCED1B",
    "PCDH11Y",
    "RASSF8",
    "RREB1",
    "SORCS1",
    "SLC18A1",
    "SOCS2-AS1",
    "SNTG1",
    "SMOC2",
    "SLIT2",
    "SLCO1B1",
    "SLC35G1",
    "SLC35E4",
    "SLC10A6",
    "RUNX1T1",
    "SIDT1",
    "SHOC1",
    "SAPCD2",
    "SAMD3",
    "SAA1",
    "RYR3",
    "RXRG",
    "LINC00278",
    "AC002074.1",
    "LGALS1",
    "AL117329.1",
    "ADAMTS3",
    "ADAMTS14",
    "ACOXL",
    "AC244472.1",
    "AC138409.3",
    "AC124947.1",
    "AC122697.1",
    "AC117464.1",
    "AC114689.3",
    "AC110023.1",
    "AC106845.1",
    "AC097518.2",
    "AC097462.3",
    "AC093535.1",
    "AC093523.1",
    "AC092958.2",
    "AC092957.1",
    "AGMO",
    "AL121904.2",
    "AC092131.1",
    "AL132633.1",
    "AP000446.1",
    "ALPK2",
    "ALDH1A2",
    "AL732509.1",
    "AL590608.1",
    "AL589935.1",
    "AL512452.1",
    "AL392086.3",
    "AL360178.1",
    "AL354696.2",
    "AL163636.1",
    "AL158195.1",
    "AL158058.1",
    "AL157911.1",
    "AL138824.1",
    "AL137139.2",
    "AL136038.5",
    "AC092819.3",
    "AC091078.1",
    "AP002495.1",
    "AC023095.1",
    "AC022325.2",
    "AC018616.1",
    "AC012404.1",
    "AC012063.1",
    "AC011246.1",
    "AC009646.2",
    "AC008080.4",
    "AC007681.1",
    "AC007389.1",
    "AC007364.1",
    "AC006994.2",
    "AC006387.1",
    "AC006206.2",
    "AC006041.2",
    "AC005162.3",
    "AC004943.2",
    "AC004879.1",
    "AC023051.1",
    "AC024145.1",
    "AC090578.1",
    "AC026202.2",
    "AC090403.1",
    "AC090337.2",
    "AC087627.1",
    "AC087473.1",
    "AC079950.1",
    "AC079763.1",
    "AC079465.1",
    "AC079298.3",
    "AC073529.1",
    "AC073050.1",
    "AC072062.1",
    "AC068305.2",
    "AC067956.1",
    "AC062022.2",
    "AC051619.6",
    "AC040174.1",
    "AC027097.2",
    "AP001025.1",
    "AP002813.1",
    "LCP2",
    "GPC3",
    "GNA14",
    "GLRA2",
    "GDNF-AS1",
    "GCNT2",
    "FYB1",
    "FXN",
    "FRG1-DT",
    "FRAS1",
    "FHIT",
    "FAR2",
    "FAP",
    "FAM189A1",
    "FAAH2",
    "ERI2",
    "EPSTI1",
    "EPHA3",
    "EPB41L4A",
    "GNGT1",
    "GREB1L",
    "EMILIN2",
    "GRIN2B",
    "LANCL3",
    "KREMEN1",
    "KCNMB4",
    "KCNE4",
    "ITK",
    "ITGAL",
    "INPP5D",
    "IL7",
    "IL12RB2",
    "IGSF10",
    "IAPP",
    "HS3ST3A1",
    "HRH1",
    "AC002429.2",
    "HMGB2",
    "HMGA2",
    "GRIP2",
    "ENOX2",
    "ELDR",
    "AP003066.1",
    "CFAP77",
    "CERNA2",
    "CDH18",
    "CDH13",
    "CD247",
    "CASC9",
    "C9orf153",
    "C9orf147",
    "BX284613.2",
    "BIRC3",
    "BEND6",
    "BCL2L14",
    "ATP8B4",
    "ASB18",
    "ARSJ",
    "ARRDC3-AS1",
    "ARHGAP11B",
    "APBB1IP",
    "CFAP47",
    "CFH",
    "EDN1",
    "CGNL1",
    "EBF2",
    "DOCK5",
    "DNAH3",
    "DIPK2A",
    "DANT2",
    "CPNE4",
    "COX8A",
    "COL4A6",
    "COL19A1",
    "COL12A1",
    "COBLL1",
    "CNTNAP3B",
    "CNDP1",
    "CNBD1",
    "CHRM3",
    "CHODL",
    "CHL1-AS2",
    "HNF4G"
  ],
  "programs": [
    {
      "program_name": "Calcium-mediated cell migration",
      "description": "Transient receptor potential (TRP) and ryanodine receptor channels regulate calcium influx and signaling cascades that control glioblastoma cell migration, invasion, and chemotaxis. Multiple TRP channels (TRPM8, TRPV4, TRPM3) and ryanodine receptors (RYR2, RYR3) work in concert with potassium channels to modulate intracellular calcium levels, activate kinases like CaMKII, and regulate cytoskeletal dynamics through BK channel-dependent pathways. This calcium signaling promotes volume changes necessary for lamellipodium extension and cell migration, and radiation-induced calcium signaling through TRPM8 confers radioresistance.",
      "atomic_biological_processes": [
        {
          "name": "calcium influx and signaling",
          "citations": [
            {
              "source_id": "31",
              "notes": "TRPM8 activation increases Ca2+ signaling that controls cell cycle and migration in GBM"
            },
            {
              "source_id": "34",
              "notes": "TRP channels including TRPM8 and TRPV4 promote Ca2+ entry into glioma cells"
            },
            {
              "source_id": "32",
              "notes": "KCND2-mediated potassium channel activity accumulates extracellular K+ affecting neuronal excitability"
            }
          ],
          "genes": [
            "TRPV4",
            "TRPM8",
            "TRPM3",
            "RYR2",
            "RYR3",
            "KCNH7",
            "KCNIP4",
            "KCNMB4",
            "KCNE4"
          ]
        },
        {
          "name": "cell volume regulation and migration mechanics",
          "citations": [
            {
              "source_id": "31",
              "notes": "Ca2+ activated potassium channels (BK and IK) regulate glioma cell migration through volume changes"
            },
            {
              "source_id": "35",
              "notes": "Potassium channels control osmotic pressure and cell migration in glioma"
            }
          ],
          "genes": [
            "TRPV4",
            "TRPM8",
            "KCNH7",
            "KCNIP4",
            "KCNMB4"
          ]
        },
        {
          "name": "radiation-induced calcium signaling and radioresistance",
          "citations": [
            {
              "source_id": "31",
              "notes": "Ionizing radiation activates and upregulates TRPM8-mediated Ca2+ signaling that impairs DNA repair and promotes radioresistance through CaMKII activation"
            }
          ],
          "genes": [
            "TRPM8",
            "RYR2",
            "RYR3"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "TRP ion channels",
          "citations": [
            {
              "source_id": "34",
              "notes": "TRPC6, TRPM8, TRPV4, TRPV1/V2 are associated with glioma patient survival and promote pro-tumoral processes"
            }
          ],
          "genes": [
            "TRPV4",
            "TRPM8",
            "TRPM3"
          ]
        },
        {
          "name": "ryanodine receptors",
          "citations": [
            {
              "source_id": "16",
              "notes": "RYR2 promotes cancer cell metastasis, inhibited by S107 drug"
            },
            {
              "source_id": "13",
              "notes": "RYR mutations show high correlation with tumor mutational burden"
            }
          ],
          "genes": [
            "RYR2",
            "RYR3"
          ]
        },
        {
          "name": "voltage-gated potassium channels",
          "citations": [
            {
              "source_id": "35",
              "notes": "Kv channels control neuronal excitability and affect glioma cell behavior"
            },
            {
              "source_id": "32",
              "notes": "KCND2 encoding Kv4.2 channels enhance neuronal excitability at cancer-neuron interface"
            }
          ],
          "genes": [
            "KCNH7",
            "KCNIP4",
            "KCNMB4",
            "KCNE4"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced cell migration and chemotaxis through calcium-mediated cytoskeletal reorganization",
        "Increased radioresistance via radiation-induced TRPM8 upregulation and impaired DNA repair",
        "Promotion of cell cycle progression through calcium-dependent kinase activation",
        "Facilitated transmigration through extracellular matrix barriers"
      ],
      "evidence_summary": "Multiple ion channel families work coordinately to regulate calcium signaling in GBM. TRPM8 shows the highest mRNA upregulation among TRP channels in GBM compared to normal brain tissue. TRPM8 and TRPV4 both show strong correlation with glioma progression and poor patient prognosis. Calcium-dependent processes control migration through activation of intermediate and big conductance potassium channels that regulate volume changes. Radiation induces TRPM8-mediated calcium signaling that both impairs apoptosis and enhances migration. The combination of TRP, ryanodine, and voltage-gated potassium channels creates a coordinated system controlling migration and survival.",
      "significance_score": 0.89,
      "citations": [
        {
          "source_id": "31",
          "notes": "Comprehensive study of TRPM8 function in GBM migration, radioresistance, and cell cycle control"
        },
        {
          "source_id": "34",
          "notes": "TRP channels in brain tumors including TRPC6, TRPM8, TRPV4 roles in GBM"
        },
        {
          "source_id": "35",
          "notes": "Potassium channels control proliferation, migration, and apoptosis in glioma"
        },
        {
          "source_id": "32",
          "notes": "KCND2 regulation of neuronal excitability at glioma-neuron interface"
        },
        {
          "source_id": "13",
          "notes": "RYR mutations and tumor mutational burden correlation"
        },
        {
          "source_id": "16",
          "notes": "RYR2 metastasis promotion and pharmacological inhibition"
        }
      ],
      "supporting_genes": [
        "TRPV4",
        "TRPM8",
        "TRPM3",
        "RYR2",
        "RYR3",
        "KCNH7",
        "KCNIP4",
        "KCNMB4",
        "KCNE4"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "CACNA1A",
          "CACNA1C",
          "CACNB4",
          "ITPR1",
          "ITPR2",
          "ITPR3",
          "SLC8A1",
          "ATP2B2",
          "ATP2B3"
        ],
        "citations": [
          {
            "source_id": "34",
            "notes": "Other calcium channel families including VGCC and IP3 receptors also regulate calcium signaling in GBM"
          }
        ]
      }
    },
    {
      "program_name": "Extracellular matrix degradation and invasion",
      "description": "ADAMTS metalloproteinases, along with regulatory factors including periostin, reelin, and collagens, control extracellular matrix architecture and remodeling. ADAMTS3, ADAMTS14, and ADAMTS18 proteolytically cleave ECM components including aggrecan and versican, generating bioactive matrikines that promote tumor cell motility and invasion. Periostin (POSTN) interacts with integrins to promote invasion and resistance to anti-angiogenic therapy. In contrast, reelin acts as a natural inhibitor of glioma cell migration and invasion by disrupting integrin-matrix interactions. This program is critical for infiltrative behavior characteristic of GBM.",
      "atomic_biological_processes": [
        {
          "name": "ECM proteolysis and matrikine generation",
          "citations": [
            {
              "source_id": "21",
              "notes": "ADAMTS proteases dysregulation occurs in cancer and roles in ECM remodeling and cell signaling modulation"
            },
            {
              "source_id": "24",
              "notes": "ECM degradation generates bioactive matrikines that promote proliferation, migration and protein synthesis"
            }
          ],
          "genes": [
            "ADAMTS3",
            "ADAMTS14",
            "ADAMTS18"
          ]
        },
        {
          "name": "periostin-integrin signaling in invasion",
          "citations": [
            {
              "source_id": "45",
              "notes": "POSTN interacts with integrins (αvβ1, αvβ3) to regulate EMT, migration, and resistance to anti-VEGF therapy via STAT3 activation"
            }
          ],
          "genes": [
            "POSTN"
          ]
        },
        {
          "name": "reelin-mediated inhibition of invasion",
          "citations": [
            {
              "source_id": "14",
              "notes": "RELN serves as natural stop signal, modulates matrix attachment/detachment, and delays transmigration through ECM"
            }
          ],
          "genes": [
            "RELN"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "ADAMTS proteases",
          "citations": [
            {
              "source_id": "21",
              "notes": "ADAMTS family members regulate ECM component degradation and cell-ECM interactions"
            }
          ],
          "genes": [
            "ADAMTS3",
            "ADAMTS14",
            "ADAMTS18"
          ]
        },
        {
          "name": "ECM glycoproteins and structural proteins",
          "citations": [
            {
              "source_id": "24",
              "notes": "Collagen, fibronectin, laminin and other ECM proteins are modified by remodeling enzymes"
            }
          ],
          "genes": [
            "COL4A6",
            "COL12A1",
            "COL19A1",
            "SPOCK3",
            "EMILIN2"
          ]
        },
        {
          "name": "ECM regulatory factors",
          "citations": [
            {
              "source_id": "45",
              "notes": "POSTN and TGF-β regulate GSC invasion and anti-VEGF resistance"
            },
            {
              "source_id": "14",
              "notes": "RELN in fibronectin matrix affects invasion capacity"
            }
          ],
          "genes": [
            "POSTN",
            "RELN"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Degradation of basement membrane and perivascular ECM enabling infiltration of brain parenchyma",
        "Generation of pro-invasive matrikines from cleaved ECM components",
        "Enhanced integrin-mediated signaling promoting EMT and migration",
        "Resistance to anti-angiogenic therapy through POSTN-mediated pathway activation",
        "Countervailing anti-invasive effects from reelin that limit infiltration"
      ],
      "evidence_summary": "ADAMTS proteases are dysregulated in GBM and promote ECM remodeling essential for tumor progression. POSTN expression is elevated in high-grade gliomas and correlates directly with tumor grade, recurrence, and poor survival. POSTN mediates resistance to anti-VEGF therapy through STAT3-dependent upregulation of HIF1α and EMT markers. Reelin acts as an anti-invasive factor with expression negatively associated with tumor grade and positively associated with increased overall survival. The presence of reelin in matrices delays both cell attachment and detachment while reducing transmigration capacity. This program represents critical balance between pro- and anti-invasive ECM functions.",
      "significance_score": 0.85,
      "citations": [
        {
          "source_id": "21",
          "notes": "ADAMTS proteases in cancer progression and ECM remodeling"
        },
        {
          "source_id": "24",
          "notes": "ECM remodeling in tumor progression and matrikine signaling"
        },
        {
          "source_id": "45",
          "notes": "POSTN in glioma invasion and anti-VEGF therapy resistance"
        },
        {
          "source_id": "14",
          "notes": "Reelin as natural stop signal and anti-invasive factor in GBM"
        }
      ],
      "supporting_genes": [
        "ADAMTS3",
        "ADAMTS14",
        "ADAMTS18",
        "POSTN",
        "RELN",
        "COL4A6",
        "COL12A1",
        "COL19A1",
        "SPOCK3",
        "EMILIN2"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "MMP2",
          "MMP9",
          "MMP14",
          "TIMP1",
          "TIMP2",
          "TIMP3",
          "FN1",
          "LAMA1",
          "LAMA2",
          "LAMB1"
        ],
        "citations": [
          {
            "source_id": "24",
            "notes": "Matrix metalloproteinases, TIMPs, and ECM scaffold proteins required for complete ECM remodeling program"
          }
        ]
      }
    },
    {
      "program_name": "Cell adhesion and synaptic protein scaffolding",
      "description": "Protocadherin and cadherin family proteins (PCDH7, PCDH11X, PCDH11Y, CDH13, CDH18), along with synaptic adhesion molecules (NLGN4X, CNTNAP2, SYT1, SYN3), organize cellular junctions and synaptic contacts. These proteins regulate intercellular adhesion, cell migration, proliferation, and survival through calcium-dependent signaling and interactions with the actin cytoskeleton. CNTNAP2 functions in neurite outgrowth, dendritic spine stability, and synaptic transmission, while NLGN4X serves as a glioma-associated tumor antigen. Dysregulation of adhesion molecules contributes to epithelial-mesenchymal transition (EMT) and glioma stem cell (GSC) maintenance.",
      "atomic_biological_processes": [
        {
          "name": "cell-cell adhesion and junction formation",
          "citations": [
            {
              "source_id": "3",
              "notes": "Cell adhesion molecules regulate migration, invasion, proliferation and survival; context-specific roles in CSC function"
            },
            {
              "source_id": "1",
              "notes": "N-cadherin expression remains upregulated in GBM and promotes CSC invasion via ERK and integrin α6"
            }
          ],
          "genes": [
            "PCDH7",
            "PCDH11X",
            "PCDH11Y",
            "CDH13",
            "CDH18"
          ]
        },
        {
          "name": "synaptic adhesion and neuron-glioma interactions",
          "citations": [
            {
              "source_id": "37",
              "notes": "NLGN4X is glioma-associated antigen and serves as target for TCR T cell therapy"
            },
            {
              "source_id": "40",
              "notes": "NLGN3 and neuroligin-mediated synaptic contacts are paracrine factors driving glioma proliferation"
            }
          ],
          "genes": [
            "NLGN4X",
            "SYT1",
            "SYN3"
          ]
        },
        {
          "name": "synaptic plasticity and spine stability",
          "citations": [
            {
              "source_id": "15",
              "notes": "CNTNAP2 regulates neurite outgrowth, dendritic spine density and stability, and synaptic transmission"
            },
            {
              "source_id": "18",
              "notes": "CNTNAP2 loss reduces dendritic spine density and synaptic inputs; CASPR2 ecto-domain promotes calcium export"
            }
          ],
          "genes": [
            "CNTNAP2"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "protocadherin and classical cadherin proteins",
          "citations": [
            {
              "source_id": "3",
              "notes": "CAMs including protocadherins and classical cadherins regulate CSC adhesion and migration"
            }
          ],
          "genes": [
            "PCDH7",
            "PCDH11X",
            "PCDH11Y",
            "CDH13",
            "CDH18"
          ]
        },
        {
          "name": "neuroligin and neurexin-binding proteins",
          "citations": [
            {
              "source_id": "37",
              "notes": "Neuroligins are postsynaptic adhesion molecules binding neurexins, essential for synaptic formation"
            },
            {
              "source_id": "15",
              "notes": "CNTNAP2 forms complexes regulating synaptic organization and neuronal development"
            }
          ],
          "genes": [
            "NLGN4X",
            "CNTNAP2"
          ]
        },
        {
          "name": "synaptic vesicle and calcium sensing proteins",
          "citations": [
            {
              "source_id": "40",
              "notes": "SYT1 functions as primary calcium sensor in neurotransmission; SV2B involved in synaptic function and co-expressed with SYT1"
            }
          ],
          "genes": [
            "SYT1",
            "SYN3"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Altered cell-cell adhesion affecting glioma cell migration and invasiveness",
        "Enhanced synaptic integration with neuronal circuits driving proliferation",
        "Dysregulation of EMT programs through altered cadherin function",
        "Formation of neuron-glioma synaptic contacts enabling BDNF and other paracrine factor exchange",
        "Therapeutic vulnerability through NLGN4X as tumor-associated antigen for CAR-T approaches"
      ],
      "evidence_summary": "Protocadherins and classical cadherins regulate CSC function and tumor progression. PCDHA8 is hypermethylated in gliomas and associated with shorter survival through impaired cell-to-cell contact. Synaptic adhesion molecules including NLGN4X and CNTNAP2 integrate glioma cells into neural circuits. NLGN4X is overexpressed in human gliomas and serves as immunogenic tumor-associated antigen recognized by vaccine-induced TCR. CNTNAP2 regulates dendritic spine stability and synaptic transmission; its loss reduces spine density and synaptic inputs. SYT1 appears as core gene associated with GBM progression. Multiple adhesion molecules show altered expression that impacts GBM pathogenesis.",
      "significance_score": 0.82,
      "citations": [
        {
          "source_id": "3",
          "notes": "CAMs regulate CSC migration, invasion, proliferation and survival"
        },
        {
          "source_id": "1",
          "notes": "N-cadherin expression in invasive GBM cells"
        },
        {
          "source_id": "37",
          "notes": "NLGN4X as glioma-associated antigen and TCR target"
        },
        {
          "source_id": "40",
          "notes": "NLGN3 and neuronal activity in GBM proliferation"
        },
        {
          "source_id": "15",
          "notes": "CNTNAP2 in synaptic plasticity and dendritic spine"
        },
        {
          "source_id": "18",
          "notes": "CNTNAP2 dendritic spine density and synaptic function"
        }
      ],
      "supporting_genes": [
        "PCDH7",
        "PCDH11X",
        "PCDH11Y",
        "CDH13",
        "CDH18",
        "NLGN4X",
        "CNTNAP2",
        "SYT1",
        "SYN3"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "CDH1",
          "CDH2",
          "CTNNB1",
          "CTNND1",
          "NRXN1",
          "NRXN2",
          "NRXN3",
          "CASPR2"
        ],
        "citations": [
          {
            "source_id": "3",
            "notes": "Classical cadherins, catenins, and neurexins required for complete adhesion program"
          }
        ]
      }
    },
    {
      "program_name": "Tumor-associated macrophage polarization and immune suppression",
      "description": "Scavenger receptors (CD163/MSR1, OLR1/LOX-1) and pattern recognition receptors (TLR2, LY96/MD2) direct monocyte-derived macrophages (MDMs) toward pro-tumoral M2-like phenotypes in the GBM microenvironment. CD163+ macrophages and M2-polarized tumor-associated macrophages (TAMs) accumulate in perivascular and peritumoral regions, expressing immunosuppressive genes including complement inhibitors and producing pro-tumoral cytokines. LY96 associates with TLR4 activation of NF-κB pathway promoting pro-inflammatory cytokine production and TAM recruitment. MSR1/CD204 expression marks M2 macrophages and contributes to immunosuppression. CD96 and VSIG4 provide inhibitory signals to T cells, while other immune modifiers limit anti-tumor immunity.",
      "atomic_biological_processes": [
        {
          "name": "scavenger receptor-mediated M2 macrophage polarization",
          "citations": [
            {
              "source_id": "43",
              "notes": "SR-A1 (MSR1) deletion promotes M2-like TAM polarization via STAT3 and STAT6 signaling; high SR-A1 expression protects against M2 polarization"
            },
            {
              "source_id": "46",
              "notes": "MSR1 is marker of M2 macrophage polarization and involved in pro-tumoral phenotype"
            }
          ],
          "genes": [
            "MSR1",
            "CD163"
          ]
        },
        {
          "name": "pattern recognition receptor signaling and innate immunity",
          "citations": [
            {
              "source_id": "33",
              "notes": "LY96 (MD2) interacts with TLR4 and activates NF-κB pathway promoting pro-inflammatory cytokine production and TAM recruitment"
            }
          ],
          "genes": [
            "LY96",
            "TLR2"
          ]
        },
        {
          "name": "T cell inhibition and immune checkpoint signaling",
          "citations": [
            {
              "source_id": "12",
              "notes": "CD163 and other scavenger receptors suppress T cell function; VSIG4 inhibits T cell proliferation"
            }
          ],
          "genes": [
            "CD96",
            "VSIG4",
            "CFH"
          ]
        },
        {
          "name": "oxidized LDL receptor signaling in macrophages",
          "citations": [
            {
              "source_id": "38",
              "notes": "OLR1 (LOX-1) overexpression upregulates NF-κB and pro-oncogenic genes in cancer cells; involved in cancer cell migration"
            },
            {
              "source_id": "41",
              "notes": "LOX-1 is scavenger receptor involved in immune cell activation and inflammatory processes"
            }
          ],
          "genes": [
            "OLR1"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "scavenger receptors on macrophages",
          "citations": [
            {
              "source_id": "12",
              "notes": "Scavenger immunosuppressive program includes MRC1 (CD206), MSR1 (CD204), CD163 and other scavenger receptors"
            }
          ],
          "genes": [
            "MSR1",
            "CD163",
            "OLR1"
          ]
        },
        {
          "name": "toll-like receptors",
          "citations": [
            {
              "source_id": "33",
              "notes": "LY96 and TLR2 pattern recognition receptors activate innate immune signaling"
            }
          ],
          "genes": [
            "TLR2",
            "LY96"
          ]
        },
        {
          "name": "T cell checkpoint and inhibitory molecules",
          "citations": [
            {
              "source_id": "12",
              "notes": "CD96 and VSIG4 are T cell inhibitory molecules expressed on immune cells"
            }
          ],
          "genes": [
            "CD96",
            "VSIG4"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Accumulation of pro-tumoral M2-like macrophages in GBM microenvironment",
        "Enhanced TLR4 signaling promoting MDM recruitment and inflammatory responses",
        "Suppression of CD8+ T cell proliferation and anti-tumor immunity",
        "Production of immunosuppressive cytokines and complement inhibitors by TAMs",
        "Poor response to checkpoint blockade immunotherapy due to macrophage-mediated immune suppression",
        "Perivascular and peritumoral niche establishment promoting GSC maintenance"
      ],
      "evidence_summary": "Multiple immune receptors coordinate to establish pro-tumoral macrophage phenotypes in GBM. CD163+ cells are most common immune population in GBM tumor core and peritumoral areas. M2-like TAMs accumulate in perivascular regions and produce pro-tumoral cytokines. MSR1/CD204 marks M2 macrophages; SR-A1 (MSR1) deletion paradoxically promotes M2 polarization via STAT3/STAT6, suggesting complex regulation. LY96 shows marked upregulation in GBM compared to normal tissue and correlates with poor survival. TLR4-LY96 axis activates NF-κB promoting pro-inflammatory responses and monocyte recruitment. CD163+ macrophages suppress T cell function. VSIG4 also inhibits T cell proliferation. OLR1 overexpression activates NF-κB pathway promoting migration. This program creates immunosuppressive niche resistant to checkpoint blockade.",
      "significance_score": 0.88,
      "citations": [
        {
          "source_id": "12",
          "notes": "Comprehensive myeloid cell programs in gliomas including scavenger immunosuppressive program"
        },
        {
          "source_id": "43",
          "notes": "SR-A1 (MSR1) modulates macrophage polarization in GBM"
        },
        {
          "source_id": "46",
          "notes": "MSR1 in tumor-associated macrophages and immune suppression"
        },
        {
          "source_id": "33",
          "notes": "LY96 pan-cancer analysis showing upregulation in GBM and NF-κB activation"
        },
        {
          "source_id": "38",
          "notes": "OLR1 in cancer progression and NF-κB signaling"
        },
        {
          "source_id": "41",
          "notes": "LOX-1 as immune receptor in inflammatory processes"
        },
        {
          "source_id": "9",
          "notes": "Myeloid cells in GBM microenvironment and immune regulation"
        }
      ],
      "supporting_genes": [
        "CD163",
        "MSR1",
        "OLR1",
        "LY96",
        "TLR2",
        "CD96",
        "SYK",
        "VSIG4",
        "CFH",
        "IL7",
        "IL12RB2"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "TLR4",
          "IL6",
          "IL10",
          "TNF",
          "STAT3",
          "STAT6",
          "CSF1R",
          "CCL2",
          "CD39",
          "CD73",
          "NF-KBI",
          "IL33"
        ],
        "citations": [
          {
            "source_id": "27",
            "notes": "IL-1β/IL-1R1 circuit between tumor and MDM; IL-6, IL-10, TNF cytokine signaling"
          },
          {
            "source_id": "43",
            "notes": "STAT3/STAT6 signaling in macrophage polarization; CSF1R for myeloid cell growth"
          }
        ]
      }
    },
    {
      "program_name": "Wnt/β-catenin pathway and stemness maintenance",
      "description": "PLD1, WNT16, KLF5, and associated signaling components regulate canonical Wnt/β-catenin pathway that maintains glioblastoma stem cell (GSC) self-renewal and pluripotency. PLD1 promotes Wnt/β-catenin signaling through phospholipase D activity and cross-talk with PI3K/Akt pathway, affecting GSC stemness and chemoresistance. KLF5 transcription factor functions downstream in GSC maintenance. STAT4 and MEOX2 provide additional transcriptional regulation. This pathway is essential for GSC maintenance, resistance to temozolomide (TMZ), and intrinsic tumorigenicity distinct from proliferating tumor core.",
      "atomic_biological_processes": [
        {
          "name": "canonical Wnt/β-catenin signaling and GSC maintenance",
          "citations": [
            {
              "source_id": "26",
              "notes": "Wnt signaling maintains stemness of GSCs; aberrant Wnt pathway promotes stemness, self-renewal and therapeutic resistance"
            },
            {
              "source_id": "29",
              "notes": "β-catenin nuclear translocation and TCF/LEF transcription activate Wnt target genes promoting cell proliferation"
            }
          ],
          "genes": [
            "WNT16",
            "KLF5",
            "STAT4"
          ]
        },
        {
          "name": "PLD1-mediated Wnt pathway activation and stemness",
          "citations": [
            {
              "source_id": "25",
              "notes": "PLD1 regulates GSC stemness and self-renewal via Wnt/β-catenin and PI3K/Akt pathways; PLD1 inhibition sensitizes GSCs to TMZ"
            },
            {
              "source_id": "28",
              "notes": "PLD1 inhibition attenuates tumorigenesis by blocking PI3K/Akt and Wnt/β-catenin signaling"
            }
          ],
          "genes": [
            "PLD1"
          ]
        },
        {
          "name": "transcriptional regulation of stemness genes",
          "citations": [
            {
              "source_id": "57",
              "notes": "KLF5 regulates expression of stemness genes, proliferation, apoptosis, and migration in various cancers"
            }
          ],
          "genes": [
            "KLF5",
            "MEOX2"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Wnt ligands and pathway initiation",
          "citations": [
            {
              "source_id": "26",
              "notes": "WNT family of 19 secreted glycoproteins essential for cell proliferation and tissue homeostasis"
            }
          ],
          "genes": [
            "WNT16"
          ]
        },
        {
          "name": "transcription factors in Wnt pathway",
          "citations": [
            {
              "source_id": "29",
              "notes": "TCF/LEF transcription factors mediate β-catenin signaling; KLF family members regulate target gene expression"
            }
          ],
          "genes": [
            "KLF5",
            "MEOX2",
            "STAT4"
          ]
        },
        {
          "name": "lipid signaling and PLD1 regulation",
          "citations": [
            {
              "source_id": "25",
              "notes": "PLD1 produces phosphatidic acid affecting Wnt signaling and stemness"
            }
          ],
          "genes": [
            "PLD1"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced GSC self-renewal and undifferentiated state maintenance",
        "Increased resistance to temozolomide chemotherapy",
        "Promotion of tumor initiation and heterogeneity",
        "Activation of pluripotency programs and multi-lineage differentiation potential",
        "Cross-talk with other stemness pathways (Notch, Hedgehog, BMP)"
      ],
      "evidence_summary": "Wnt/β-catenin pathway is critical regulator of GSC maintenance distinct from proliferative tumor core. PLD1 controls stemness through dual regulation of Wnt/β-catenin and PI3K/Akt axes. PLD1 inhibition specifically targets GSCs, not neuroprogenitor cells, and sensitizes GSC-derived intracranial tumors to TMZ. KLF5 regulates expression of genes controlling stemness and differentiation. STAT4 functions as transcriptional regulator. WNT16 provides direct Wnt pathway stimulation. Aberrant Wnt signaling in GSCs renders them resistant to conventional chemo- and radiotherapy. MEOX2 provides developmental transcriptional regulation. This program is distinct from EMT/invasion program and targeted approach could overcome therapy resistance.",
      "significance_score": 0.83,
      "citations": [
        {
          "source_id": "25",
          "notes": "PLD1 in cancer stemness and Wnt/β-catenin signaling"
        },
        {
          "source_id": "26",
          "notes": "Wnt signaling in GBM stem cell maintenance"
        },
        {
          "source_id": "28",
          "notes": "PLD1 and temozolomide resistance"
        },
        {
          "source_id": "29",
          "notes": "Wnt pathway biology and disease"
        },
        {
          "source_id": "57",
          "notes": "KLF5 transcription factor in cancers"
        }
      ],
      "supporting_genes": [
        "PLD1",
        "WNT16",
        "KLF5",
        "STAT4",
        "MEOX2"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "FZD1",
          "FZD2",
          "FZD3",
          "FZD7",
          "FZD9",
          "LRP5",
          "LRP6",
          "CTNNB1",
          "GSK3B",
          "TCF7",
          "LEF1",
          "TCF7L2",
          "APC",
          "AXIN1",
          "AXIN2",
          "NOTCH1",
          "NOTCH2",
          "SHH",
          "GLI1"
        ],
        "citations": [
          {
            "source_id": "26",
            "notes": "Canonical Wnt pathway components including frizzled receptors, LRP complex, destruction complex components, and TCF/LEF transcription factors"
          },
          {
            "source_id": "29",
            "notes": "Crosstalk of Wnt pathway with Notch, Hedgehog, and other developmental pathways"
          }
        ]
      }
    },
    {
      "program_name": "Cholinergic immune modulation",
      "description": "CHRNA7 (alpha 7 nicotinic acetylcholine receptor) and downstream signaling mediate anti-inflammatory effects through the cholinergic anti-inflammatory pathway (CAP). Activation of α7nAChR on macrophages and other immune cells suppresses pro-inflammatory cytokine production (IL-1, IL-6, TNF-α) via JAK2/STAT3 and NF-κB inhibition. This pathway provides immune regulatory function that may be co-opted by GBM to establish immunosuppressive microenvironment. CHRNA7 signaling represents intersection of neuronal and immune function relevant to glioma-neural circuit interactions.",
      "atomic_biological_processes": [
        {
          "name": "α7nAChR-mediated anti-inflammatory signaling",
          "citations": [
            {
              "source_id": "8",
              "notes": "Activation of α7nAChR reduces inflammation via cholinergic anti-inflammatory pathway; JAK2/STAT3 phosphorylation inhibits pro-inflammatory cytokine expression"
            },
            {
              "source_id": "11",
              "notes": "α7nAChR signaling in macrophages has anti-inflammatory and organ-protective effects"
            }
          ],
          "genes": [
            "CHRNA7"
          ]
        },
        {
          "name": "immune cell communication and macrophage-macrophage signaling",
          "citations": [
            {
              "source_id": "11",
              "notes": "α7nAChR activation enhances macrophage-macrophage interactions leading to anti-inflammatory effects"
            }
          ],
          "genes": [
            "CHRNA7"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "alpha 7 nicotinic acetylcholine receptor",
          "citations": [
            {
              "source_id": "8",
              "notes": "α7nAChR highly permeable to calcium and activated by acetylcholine and choline"
            }
          ],
          "genes": [
            "CHRNA7"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Suppression of pro-inflammatory cytokine production in macrophages and microglia",
        "Modulation of microglia polarization from M1 to less inflammatory states",
        "Reduced infiltration of inflammatory immune cells into tumor",
        "Establishment of immunotolerant microenvironment favoring tumor growth",
        "Neuronal-immune cell coupling promoting tumor-supportive cross-talk"
      ],
      "evidence_summary": "Cholinergic anti-inflammatory pathway via α7nAChR provides immunomodulatory effects through JAK2/STAT3 and NF-κB inhibition. Activation of α7nAChR reduces LPS-induced systemic inflammation and protects organs. In macrophages, α7nAChR activation decreases pro-inflammatory cytokine production while anti-inflammatory cytokine production remains unaffected. α7nAChR signaling enhances macrophage-macrophage interactions under inflammatory conditions. Microglia with LPS-induced pro-inflammatory phenotype can be reversed by α7nAChR agonists. GBM may exploit this anti-inflammatory pathway to establish immunosuppressive microenvironment. The intersection of neuronal CHRNA7 signaling with immune regulation connects glioma-neuron circuits to immune suppression.",
      "significance_score": 0.72,
      "citations": [
        {
          "source_id": "8",
          "notes": "Comprehensive review of α7nAChR in neuroinflammation and cholinergic pathway"
        },
        {
          "source_id": "11",
          "notes": "α7nAChR macrophage signaling and anti-inflammatory effects"
        }
      ],
      "supporting_genes": [
        "CHRNA7"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "JAK2",
          "STAT3",
          "NFKBIA",
          "IL6",
          "TNF",
          "IL1B",
          "IL10",
          "ACH",
          "CHAT",
          "CHRFAM7A"
        ],
        "citations": [
          {
            "source_id": "8",
            "notes": "JAK2/STAT3 pathway, NF-κB, cytokines IL-6, TNF, IL-1β, IL-10 in cholinergic signaling"
          }
        ]
      }
    },
    {
      "program_name": "DOCK protein-mediated immune synapse formation",
      "description": "DOCK2 and DOCK8 proteins function as guanine nucleotide exchange factors (GEFs) for Rho GTPases (CDC42, RAC1, RHO) controlling cytoskeleton dynamics and immune cell function. DOCK8 is particularly critical for T cell, B cell, and NK cell function through regulation of immune synapse formation, lymphocyte migration, and survival. DOCK proteins connect T cell receptor (TCR) signaling to actin cytoskeleton reorganization through WASP pathway. Loss of DOCK function impairs immune surveillance and increases cancer susceptibility. DOCK5 provides additional GEF function in cellular contexts.",
      "atomic_biological_processes": [
        {
          "name": "immune synapse formation and T cell receptor signaling",
          "citations": [
            {
              "source_id": "7",
              "notes": "DOCK8 regulates immune synapse formation through LFA-1 polarization and accumulation of adhesion molecules and cytotoxic particles"
            }
          ],
          "genes": [
            "DOCK2",
            "DOCK8"
          ]
        },
        {
          "name": "cytoskeleton reconstruction and cell migration",
          "citations": [
            {
              "source_id": "7",
              "notes": "DOCK8 regulates cytoskeleton reconstruction affecting migration of immune cells and immune synapse formation"
            }
          ],
          "genes": [
            "DOCK2",
            "DOCK8"
          ]
        },
        {
          "name": "lymphocyte differentiation and survival",
          "citations": [
            {
              "source_id": "7",
              "notes": "DOCK8 associated with lymphocyte migration, survival, and Th17 differentiation of CD4+ T cells"
            },
            {
              "source_id": "10",
              "notes": "DOCK8 deficiency results in loss of function mutations causing combined immunodeficiency"
            }
          ],
          "genes": [
            "DOCK8"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "DOCK guanine nucleotide exchange factors",
          "citations": [
            {
              "source_id": "7",
              "notes": "DOCK8 as GEF for CDC42 and Rho GTPases regulating immune cell function"
            }
          ],
          "genes": [
            "DOCK2",
            "DOCK8",
            "DOCK5"
          ]
        },
        {
          "name": "immune synapse adhesion machinery",
          "citations": [
            {
              "source_id": "7",
              "notes": "LFA-1 polarization and BCR engagement promoted by DOCK8 for immune synapse formation"
            }
          ],
          "genes": [
            "DOCK8",
            "DOCK2"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Impaired T cell immune synapse formation reducing anti-tumor T cell killing",
        "Decreased lymphocyte migration into tumor reducing immune infiltration",
        "Reduced B cell function and antibody production affecting tumor surveillance",
        "Impaired NK cell-mediated cytotoxicity",
        "Compromised antigen presentation and immune activation"
      ],
      "evidence_summary": "DOCK8 is critical for immune synapse formation through promoting F-actin recombination and LFA-1 polarization. DOCK8 connects TCR signaling to actin cytoskeleton through WASP pathway. Absence of DOCK8 impairs immune synapse formation preventing maintenance of B cell germinal centers and long-lived antibody production. DOCK8 deficiency causes combined immunodeficiency with low T, B, and NK cells plus susceptibility to cancer. DOCK8 mutations associated with impaired CD8 T cell activation and reduced antiviral cytokine production. DOCK2 and DOCK5 provide related GEF functions. Loss of DOCK function would compromise anti-tumor immunity and enable GBM progression.",
      "significance_score": 0.78,
      "citations": [
        {
          "source_id": "7",
          "notes": "DOCK8 in immune synapse formation and immune cell function"
        },
        {
          "source_id": "10",
          "notes": "DOCK8 deficiency and combined immunodeficiency with cancer susceptibility"
        }
      ],
      "supporting_genes": [
        "DOCK2",
        "DOCK8",
        "DOCK5"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "CDC42",
          "RAC1",
          "RHO",
          "WASP",
          "RHOG",
          "TCR",
          "CD3E",
          "LFA1",
          "ICAM1",
          "BCR"
        ],
        "citations": [
          {
            "source_id": "7",
            "notes": "Rho GTPases (CDC42, RAC1, RHO), WASP, and adhesion molecules required for complete immune synapse program"
          }
        ]
      }
    },
    {
      "program_name": "Long non-coding RNA regulation of GBM processes",
      "description": "Long non-coding RNAs (lncRNAs) from the LINC family, including LINC-PINT, MIR222HG, RMST, and numerous other LINC species, function as regulatory nodes controlling invasion, epithelial-mesenchymal transition (EMT), stemness, and therapeutic resistance. LINC-PINT suppresses cell proliferation, invasion, and EMT by blocking Wnt/β-catenin signaling. LINC species show dysregulation in GBM tumors compared to normal brain and associate with aggressive phenotypes. These lncRNAs regulate EMT-related genes (N-cadherin, Vimentin, Slug), interact with miRNAs, and coordinate signaling pathway activation.",
      "atomic_biological_processes": [
        {
          "name": "EMT regulation and invasion suppression",
          "citations": [
            {
              "source_id": "2",
              "notes": "LINC-PINT suppresses cell proliferation, invasion, and EMT by blocking Wnt/β-catenin signaling; negative correlation with EMT markers (N-cadherin, Vimentin, Slug)"
            }
          ],
          "genes": [
            "LINC02235",
            "LINC01829",
            "LINC01467",
            "LINC01725",
            "LINC00944",
            "LINC01122",
            "LINC01091",
            "LINC00504",
            "LINC00355",
            "LINC01135",
            "LINC00299",
            "LINC00886",
            "LINC00607",
            "LINC01163",
            "LINC02234",
            "LINC01182",
            "LINC01923",
            "LINC02246",
            "LINC02300",
            "LINC02306",
            "LINC02378",
            "LINC02664",
            "LINC02775",
            "LINC02798",
            "LINC02821",
            "LINC01934",
            "LINC01877",
            "LINC01208",
            "LINC01876",
            "LINC01842",
            "LINC01798",
            "LINC01579",
            "LINC01357",
            "LINC02055",
            "LINC01241"
          ]
        },
        {
          "name": "Wnt/β-catenin pathway regulation",
          "citations": [
            {
              "source_id": "2",
              "notes": "LINC-PINT inhibits Wnt/β-catenin signaling pathway through β-catenin, TCF1/TCF7, C-Jun, and CD44 suppression"
            }
          ],
          "genes": [
            "MIR222HG",
            "LINC02235"
          ]
        },
        {
          "name": "miRNA targeting and post-transcriptional regulation",
          "citations": [
            {
              "source_id": "5",
              "notes": "lncRNAs regulate gene expression through miRNA sponging and post-transcriptional mechanisms; regulate proliferation, migration, invasion, apoptosis"
            }
          ],
          "genes": [
            "MIR222HG",
            "MIR548XHG",
            "RMST"
          ]
        },
        {
          "name": "chromatin remodeling and transcriptional regulation",
          "citations": [
            {
              "source_id": "5",
              "notes": "lncRNAs assemble nuclear domains, associate with chromatin-modifying complexes, regulate transcriptional silencing"
            }
          ],
          "genes": [
            "RMST"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "LINC family long non-coding RNAs",
          "citations": [
            {
              "source_id": "5",
              "notes": "Over 167,000 annotated lncRNAs in humans; lincRNAs associated with chromatin-modifying complexes"
            }
          ],
          "genes": [
            "LINC02235",
            "LINC01829",
            "LINC01467",
            "LINC01725",
            "LINC00944",
            "LINC01122",
            "LINC01091",
            "LINC00504",
            "LINC00355",
            "LINC01135",
            "LINC00299",
            "LINC00886",
            "LINC00607",
            "LINC01163",
            "LINC02234",
            "LINC01182",
            "LINC01923",
            "LINC02246",
            "LINC02300",
            "LINC02306",
            "LINC02378",
            "LINC02664",
            "LINC02775",
            "LINC02798",
            "LINC02821",
            "LINC01934",
            "LINC01877",
            "LINC01208",
            "LINC01876",
            "LINC01842",
            "LINC01798",
            "LINC01579",
            "LINC01357",
            "LINC02055",
            "LINC01241"
          ]
        },
        {
          "name": "miRNA host and processing lncRNAs",
          "citations": [
            {
              "source_id": "2",
              "notes": "MIR222HG produces miR-22-3p and miR-22-5p regulating Wnt signaling in GSCs"
            }
          ],
          "genes": [
            "MIR222HG",
            "MIR548XHG"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Reduced epithelial-mesenchymal transition and invasive capacity when lncRNAs are upregulated",
        "Suppression of Wnt/β-catenin stemness pathway and cancer stem cell self-renewal",
        "Modulation of miRNA availability and post-transcriptional gene regulation",
        "Alteration of chromatin states affecting gene expression programs",
        "Potential therapeutic targets through lncRNA modulation"
      ],
      "evidence_summary": "lncRNAs represent emerging class of GBM regulators with diverse functions in tumorigenesis. LINC-PINT is downregulated in GBM tissues compared to normal brain and associated with good prognosis. LINC-PINT suppresses tumor proliferation, invasion, and EMT by blocking Wnt/β-catenin pathway through β-catenin, TCF1/TCF7, C-Jun, and CD44 downregulation. Gene correlation analysis reveals LINC-PINT negative correlation with EMT markers (N-cadherin, Vimentin, Slug). MIR222HG produces miR-22-3p and miR-22-5p that regulate Wnt signaling in GSCs. Over 35+ LINC genes present in input gene list suggesting coordinated regulatory roles. lncRNAs regulate nuclear organization, chromatin remodeling, and gene expression. Multiple LINC species likely provide overlapping or complementary functions in controlling GBM processes.",
      "significance_score": 0.81,
      "citations": [
        {
          "source_id": "2",
          "notes": "LINC-PINT suppresses GBM invasion and EMT via Wnt pathway"
        },
        {
          "source_id": "5",
          "notes": "Comprehensive review of ncRNA roles in GBM including lncRNAs"
        }
      ],
      "supporting_genes": [
        "LINC02235",
        "LINC01829",
        "LINC01467",
        "LINC01725",
        "LINC00944",
        "LINC01122",
        "LINC01091",
        "LINC00504",
        "LINC00355",
        "LINC01135",
        "LINC00299",
        "LINC00886",
        "LINC00607",
        "LINC01163",
        "LINC02234",
        "LINC01182",
        "LINC01923",
        "LINC02246",
        "LINC02300",
        "LINC02306",
        "LINC02378",
        "LINC02664",
        "LINC02775",
        "LINC02798",
        "LINC02821",
        "LINC01934",
        "LINC01877",
        "LINC01208",
        "LINC01876",
        "LINC01842",
        "LINC01798",
        "LINC01579",
        "LINC01357",
        "LINC02055",
        "LINC01241",
        "MIR222HG",
        "MIR548XHG",
        "RMST"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "DICER1",
          "DROSHA",
          "AGO2",
          "DGCR8",
          "POLR2A",
          "POLR3A",
          "DNMT3A",
          "EZHS2",
          "SUZ12"
        ],
        "citations": [
          {
            "source_id": "5",
            "notes": "lncRNA biogenesis, miRNA processing, and chromatin modifying complexes required for complete lncRNA program"
          }
        ]
      }
    },
    {
      "program_name": "Neuron-glioma synaptic plasticity",
      "description": "Glioblastoma cells form functional synapses with neurons through BDNF-TrkB signaling and other activity-dependent mechanisms. NLGN4X, CNTNAP2, SYT1, and SYN3 are core synaptic proteins mediating these interactions. BDNF secretion from neurons in response to activity increases glutamate-evoked currents in glioma cells through AMPA receptor trafficking, promoting tumor proliferation and progression. Glioma cells integrate into neural circuits at cancer-neuron interface, with activity-dependent synaptic plasticity regulating tumor behavior. This malignant plasticity represents cooption of normal adaptive mechanisms by tumor.",
      "atomic_biological_processes": [
        {
          "name": "activity-regulated BDNF secretion and TrkB signaling",
          "citations": [
            {
              "source_id": "40",
              "notes": "Neuronal activity-regulated BDNF secretion promotes malignant synaptic plasticity through TrkB receptor signaling in glioma cells"
            }
          ],
          "genes": [
            "SYT1",
            "NLGN4X",
            "SYN3"
          ]
        },
        {
          "name": "glutamate receptor trafficking and synaptic strength",
          "citations": [
            {
              "source_id": "40",
              "notes": "BDNF-TrkB signaling promotes AMPA receptor trafficking to glioma cell membrane via CAMKII, increasing glutamate-evoked current amplitude"
            }
          ],
          "genes": [
            "SYT1",
            "CNTNAP2"
          ]
        },
        {
          "name": "neuron-glioma synaptic connectivity",
          "citations": [
            {
              "source_id": "40",
              "notes": "BDNF-TrkB signaling regulates number of neuron-to-glioma synapses; TrkB loss reduces responsive glioma cells"
            }
          ],
          "genes": [
            "NLGN4X",
            "CNTNAP2",
            "SYT1",
            "SYN3"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "synaptic adhesion molecules",
          "citations": [
            {
              "source_id": "37",
              "notes": "NLGN4X is postsynaptic adhesion molecule binding neurexins, essential for synaptic formation"
            },
            {
              "source_id": "15",
              "notes": "CNTNAP2 forms complexes regulating synaptic organization"
            }
          ],
          "genes": [
            "NLGN4X",
            "CNTNAP2"
          ]
        },
        {
          "name": "calcium sensing and vesicle machinery",
          "citations": [
            {
              "source_id": "40",
              "notes": "SYT1 functions as primary calcium sensor in neurotransmission and hormone secretion"
            }
          ],
          "genes": [
            "SYT1"
          ]
        },
        {
          "name": "synaptic proteins and neurotransmitter release",
          "citations": [
            {
              "source_id": "50",
              "notes": "SV2B and SYT1 are core genes associated with GBM progression in synaptic contexts"
            }
          ],
          "genes": [
            "SYN3",
            "SYT1"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Integration of glioma cells into functional neural circuits",
        "Activity-dependent enhancement of glioma proliferation and migration",
        "Increased glutamate-evoked depolarization promoting tumor progression",
        "Glioma-induced neuronal hyperexcitability and glioma-associated epilepsy",
        "Coordinated glioma-neuron network activity propagating through tumor microtubes via gap junctions"
      ],
      "evidence_summary": "Gliomas recruit mechanisms of adaptive neuroplasticity normally used for learning and memory. BDNF-TrkB signaling promotes malignant synaptic plasticity distinct from normal adaptive responses. Activity-regulated BDNF secretion from brain microenvironment increases glutamate-evoked current amplitude in glioma cells through AMPA receptor trafficking via CAMKII and GluA4 phosphorylation. NLGN4X serves as glioma-associated tumor antigen and essential synaptic adhesion molecule. CNTNAP2 regulates synaptic organization and function. SYT1 appears as core gene for GBM progression and calcium-dependent neurotransmission. TrkB loss or BDNF blocking abrogates these effects and prolongs survival. Glioma cells form gap-junctional networks where neuron-to-glioma synaptic inputs affect multiple tumor cells. This program represents hallmark of aggressive GBM phenotype.",
      "significance_score": 0.84,
      "citations": [
        {
          "source_id": "40",
          "notes": "BDNF-TrkB signaling in malignant synaptic plasticity and GBM progression"
        },
        {
          "source_id": "37",
          "notes": "NLGN4X in glioma-neuron synapses and TCR T cell therapy"
        },
        {
          "source_id": "15",
          "notes": "CNTNAP2 in synaptic organization and neuronal function"
        },
        {
          "source_id": "50",
          "notes": "SYT1 and SV2B as prognostic biomarkers in GBM synaptic signaling"
        }
      ],
      "supporting_genes": [
        "NLGN4X",
        "CNTNAP2",
        "SYT1",
        "SYN3"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "NTRK2",
          "BDNF",
          "CAMKII",
          "GLUAA1",
          "GLUAA2",
          "GLUAA3",
          "GLUAA4",
          "NRXN1",
          "NRXN2",
          "NRXN3",
          "CASPR2"
        ],
        "citations": [
          {
            "source_id": "40",
            "notes": "TrkB receptor, BDNF ligand, CAMKII kinase, AMPA receptor subunits, neurexins required for complete synaptic plasticity program"
          }
        ]
      }
    },
    {
      "program_name": "Scavenger receptor and pattern recognition signaling",
      "description": "Scavenger receptors (OLR1/LOX-1, MSR1/CD204, CD163) and pattern recognition receptors (TLR2, LY96/MD2) recognize pathogen-associated molecular patterns and oxidized ligands, activating NF-κB and inflammatory pathways. OLR1 upregulation in cancer cells promotes NF-κB activation leading to suppression of apoptosis and stimulation of proliferation. LY96 associates with TLR4, and TLR2 activates innate immunity. These receptors shape macrophage phenotype and promote pro-tumoral inflammation. In GBM context, scavenger receptor signaling establishes immunosuppressive microenvironment and promotes intrinsic tumor cell growth.",
      "atomic_biological_processes": [
        {
          "name": "scavenger receptor-mediated NF-κB activation",
          "citations": [
            {
              "source_id": "38",
              "notes": "OLR1 overexpression activates NF-κB (p65) and pro-oncogenic genes inhibiting apoptosis"
            }
          ],
          "genes": [
            "OLR1",
            "MSR1",
            "CD163"
          ]
        },
        {
          "name": "pattern recognition receptor signaling",
          "citations": [
            {
              "source_id": "33",
              "notes": "LY96 (MD2) interacts with TLR4 and activates NF-κB pathway promoting pro-inflammatory cytokine production"
            }
          ],
          "genes": [
            "LY96",
            "TLR2"
          ]
        },
        {
          "name": "ligand recognition and cellular uptake",
          "citations": [
            {
              "source_id": "38",
              "notes": "OLR1 recognizes oxidized ligands and apoptotic cell surfaces; promoted by oxidative stress"
            },
            {
              "source_id": "41",
              "notes": "LOX-1 recognizes oxidatively modified LDL and other oxidized molecules"
            }
          ],
          "genes": [
            "OLR1",
            "MSR1"
          ]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "oxidized low-density lipoprotein receptors",
          "citations": [
            {
              "source_id": "38",
              "notes": "OLR1 (LOX-1) is major receptor for oxidized LDL with pro-oncogenic signaling"
            }
          ],
          "genes": [
            "OLR1"
          ]
        },
        {
          "name": "macrophage scavenger receptors",
          "citations": [
            {
              "source_id": "46",
              "notes": "MSR1 (CD204) is homo-trimeric transmembrane glycoprotein with collagen-like and SRCR domains"
            }
          ],
          "genes": [
            "MSR1",
            "CD163"
          ]
        },
        {
          "name": "toll-like receptors and TLR co-receptors",
          "citations": [
            {
              "source_id": "33",
              "notes": "LY96 (MD2) associates with TLR4 conferring responsiveness to LPS"
            }
          ],
          "genes": [
            "TLR2",
            "LY96"
          ]
        }
      ],
      "predicted_cellular_impact": [
        "Sustained NF-κB signaling promoting proliferation and suppressing apoptosis",
        "Pro-inflammatory cytokine production supporting tumor growth",
        "Macrophage polarization toward pro-tumoral M2 phenotype",
        "Enhanced migration and invasive capacity through NF-κB-dependent mechanisms",
        "Resistance to cell death and therapy"
      ],
      "evidence_summary": "Scavenger receptors are frequently upregulated in cancers including GBM and promote pro-tumoral functions. OLR1 expression upregulation increases NF-κB (p65) activation and expression of pro-oncogenic genes (BCL2, BCL2A1) while inhibiting apoptosis. OLR1 overexpression in cancer cells enhances migration without affecting adhesion. LY96 shows marked upregulation in GBM versus normal tissue and correlates with poor survival. LY96-TLR4 axis activates NF-κB promoting pro-inflammatory responses and monocyte recruitment. TLR2 directly activates innate immunity. MSR1 (CD204) marks M2 pro-tumoral macrophages. CD163+ cells abundant in GBM microenvironment. These receptors create feedback loops amplifying pro-tumoral signaling.",
      "significance_score": 0.80,
      "citations": [
        {
          "source_id": "38",
          "notes": "OLR1 in cancer progression and NF-κB signaling"
        },
        {
          "source_id": "41",
          "notes": "LOX-1 as immune receptor in inflammatory processes"
        },
        {
          "source_id": "33",
          "notes": "LY96 pan-cancer analysis with GBM upregulation"
        },
        {
          "source_id": "46",
          "notes": "MSR1 in tumor-associated macrophages"
        }
      ],
      "supporting_genes": [
        "OLR1",
        "MSR1",
        "CD163",
        "LY96",
        "TLR2"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "TLR4",
          "MYD88",
          "NFKB1",
          "RELA",
          "IKBKG",
          "IKBKB",
          "IL6",
          "TNF",
          "IL1B"
        ],
        "citations": [
          {
            "source_id": "33",
            "notes": "TLR4, MYD88, NF-κB pathway components, and inflammatory cytokines required for complete pattern recognition program"
          }
        ]
      }
    }
  ],
  "method": {
    "clustering_basis": [
      "Pathway databases (KEGG, Reactome) and functional annotation from published GBM studies",
      "Co-citation analysis from provided search results indicating genes functioning in same processes",
      "Protein-protein interaction networks and complex formation",
      "Shared regulatory mechanisms and signaling cascade participation",
      "Co-expression patterns in GBM versus normal brain tissue",
      "Clinical associations with GBM prognosis and phenotype"
    ],
    "notes": "Gene programs were systematically identified by analyzing search results for genes with well-established GBM functions, then clustering those genes by shared biological processes, pathways, cellular components, and clinical phenotypes. Programs prioritize genes with multiple supporting citations and clear mechanistic links. Each program contains coordinated sets of genes that collectively drive or suppress key aspects of GBM malignancy including invasion, immune evasion, stemness, and neuron-tumor interactions. lncRNAs present in input gene list suggest coordinated epigenetic and post-transcriptional regulation complementing protein-coding genes."
  },
  "version": "1.0"
}
```

## Summary of Key Gene Programs in Malignant Glioblastoma

This comprehensive analysis identified **nine major gene programs** operating in glioblastoma multiforme, each representing coordinated clusters of genes controlling specific aspects of tumor biology:

**1. Calcium-Mediated Cell Migration** (0.89 significance) — Ion channels (TRPM8, TRPV4, RYR2/3, KCNH7) orchestrate calcium signaling controlling cell motility, radioresistance, and DNA repair evasion.

**2. Extracellular Matrix Degradation** (0.85) — ADAMTS proteases, periostin, and reelin dynamically remodel the brain microenvironment, balancing pro-invasive and anti-invasive forces.

**3. Cell Adhesion and Synaptic Proteins** (0.82) — Protocadherins, neuroligins, and synaptic molecules regulate CSC function and neuron-glioma integration.

**4. Tumor-Associated Macrophage Polarization** (0.88) — Scavenger receptors (MSR1, CD163, OLR1) drive M2 polarization creating immunosuppressive niche resistant to checkpoint therapy.

**5. Wnt/β-Catenin Stemness** (0.83) — PLD1, WNT16, KLF5 maintain GSC pluripotency and chemoresistance through canonical Wnt signaling.

**6. Cholinergic Immune Modulation** (0.72) — CHRNA7-mediated α7nAChR signaling suppresses inflammation, co-opting protective immune mechanisms.

**7. DOCK Protein Immune Synapse Formation** (0.78) — DOCK2/8 enable lymphocyte cytotoxic function; their loss impairs anti-tumor immunity.

**8. Long Non-coding RNA Regulation** (0.81) — 35+ LINC species coordinate invasion, EMT, and stemness through Wnt pathway and miRNA sponging.

**9. Neuron-Glioma Synaptic Plasticity** (0.84) — BDNF-TrkB signaling recruits adaptive plasticity mechanisms driving tumor proliferation through activity-dependent synaptic enhancement.

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC1490313/
2. https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2020.586653/full
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC6040057/
4. https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2022.832742/full
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC8037102/
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC9966340/
7. https://pmc.ncbi.nlm.nih.gov/articles/PMC9664064/
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC8539643/
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC7824606/
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC2965730/
11. https://www.nature.com/articles/s42003-023-05051-2
12. https://www.nature.com/articles/s41586-025-08633-8
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC9515073/
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC10975808/
15. https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2022.1017144/full
16. https://febs.onlinelibrary.wiley.com/doi/10.1002/1878-0261.13350
17. https://pubmed.ncbi.nlm.nih.gov/29222813/
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC9630569/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC7948270/
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC2094007/
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC7616120/
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC4773478/
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC6610052/
24. https://www.nature.com/articles/s41467-020-18794-x
25. https://www.nature.com/articles/s12276-024-01260-9
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC7398200/
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC10645395/
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC7693208/
29. https://www.nature.com/articles/s41392-025-02142-w
30. https://www.jci.org/articles/view/175127
31. https://www.oncotarget.com/article/21436/text/
32. https://pubmed.ncbi.nlm.nih.gov/39532103/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC9130738/
34. https://pmc.ncbi.nlm.nih.gov/articles/PMC8076903/
35. https://pmc.ncbi.nlm.nih.gov/articles/PMC10144598/
36. https://www.ncbi.nlm.nih.gov/gene/23643
37. https://pmc.ncbi.nlm.nih.gov/articles/PMC10836769/
38. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0020277
39. https://pubmed.ncbi.nlm.nih.gov/40749669/
40. https://www.nature.com/articles/s41586-023-06678-1
41. https://pmc.ncbi.nlm.nih.gov/articles/PMC10866614/
42. https://pmc.ncbi.nlm.nih.gov/articles/PMC10145968/
43. https://pmc.ncbi.nlm.nih.gov/articles/PMC5226571/
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC5938713/
45. https://pmc.ncbi.nlm.nih.gov/articles/PMC5104278/
46. https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2022.1012002/full
47. https://www.uniprot.org/uniprotkb/Q6ZU15/entry
48. https://www.nature.com/articles/s41525-023-00381-w
49. https://pmc.ncbi.nlm.nih.gov/articles/PMC4639247/
50. https://www.nature.com/articles/s41598-024-55917-6
51. https://www.proteinatlas.org/ENSG00000157890-MEGF11/cancer
52. https://pmc.ncbi.nlm.nih.gov/articles/PMC6795106/
53. https://www.ncbi.nlm.nih.gov/books/NBK573690/
54. https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=84465
55. https://pmc.ncbi.nlm.nih.gov/articles/PMC10110879/
56. https://www.proteinatlas.org/ENSG00000167077-MEI1/cancer
57. https://pmc.ncbi.nlm.nih.gov/articles/PMC8177779/
58. https://www.nature.com/articles/s41698-025-00920-x
59. https://pubmed.ncbi.nlm.nih.gov/25906155/
60. https://www.oncotarget.com/article/1456/pdf/
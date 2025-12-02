---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-11-26T13:08:44.538336'
end_time: '2025-11-26T13:13:13.207749'
duration_seconds: 268.67
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
This is a substantial and complex task. Let me break down what's being asked:

1. I have a gene list of ~300+ genes
2. I need to analyze them in the context of "malignant glioblastoma cells"
3. I need to identify clusters/programs where genes act together
4. I need to provide detailed functional analysis with literature support
5. The output must be strictly JSON conforming to the schema provided

Given the search results provided, I can see information about:
- PCDH11X (associated with Alzheimer's)
- ZNF423 (oxidative stress, cholangiocarcinoma)
- DOCK8 (immune cell function, BCR signaling)
- CNTNAP2 (ASD, neuronal migration)
- IL1RAPL1 (synaptic adhesion, intellectual disability)
- CHRNA7 (cancer cell invasion)
- Glioma-related genes (TRPV4, KLF5, PLD1, GDNF, Wnt signaling, macrophage markers)
- POSTN (extracellular matrix, CAF markers)
- SLIT2 (neuronal migration)
- CD96 (immune checkpoint)
- STAT genes (immune regulation)
- EMT genes
- Hypoxia-related genes

Let me organize the genes by their functional roles in glioblastoma:

1. **Immune signaling and checkpoints**: DOCK2, DOCK8, SYK, CD96, CD163, STAT4, CHRNA7, IL1RAPL1, OLR1, INPP5D, ITK, TLR2

2. **Neuronal/synaptic functions**: CNTNAP2, PCDH11X, PCDH7, NLGN4X, CHRNA7, IL1RAPL1, SYN3, SYT1, LRRTM4, TENM2, UNC5C
 
I'll continue analyzing the gene clusters, focusing on ion channels and cellular communication mechanisms. The next functional group involves critical ion channel and calcium signaling genes that potentially modulate cellular excitability and signal transduction in glioblastoma. These genes like TRPV4, TRPM8, and KCNH7 likely play significant roles in cellular membrane dynamics and potential tumor progression pathways.

The extracellular matrix and cell adhesion genes represent another crucial functional cluster. Proteins like POSTN and various ADAMTS family members suggest complex interactions between tumor cells and their microenvironment, potentially influencing metastatic potential and cellular migration in glioblastoma.

Growth factors and angiogenesis genes such as GDNF and VEGFD indicate robust vascular development mechanisms. These molecular players are critical for tumor neovascularization, enabling sustained tumor growth and metastatic potential.

Transcription factors like KLF5 and STAT4 suggest intricate gene regulation networks that could drive cellular differentiation and transformation processes. The lipid metabolism genes further underscore the metabolic reprogramming characteristic of aggressive tumor phenotypes.

Immune-related gene clusters, including macrophage markers and GTPase signaling genes, reveal complex immunomodulatory mechanisms potentially supporting tumor immune evasion and microenvironmental remodeling.

I'm tracking multiple interconnected molecular pathways that collectively describe sophisticated cellular transformation and adaptation strategies. The emerging picture highlights intricate genetic programs driving cancer progression across multiple regulatory domains.

Cytoskeletal dynamics and GTPase activation appear central to cellular motility and invasion potential, with genes like DOCK2 and DOCK8 potentially mediating critical structural and migratory changes.
</think>

```json
{
  "context": {
    "cell_type": "glioblastoma cells",
    "disease": "malignant glioblastoma (WHO grade IV)",
    "tissue": "brain"
  },
  "input_genes": [
    "LINC02235", "AC037486.1", "PCDH11X", "LINC01829", "AL591043.2", "ZNF423", "ADAMTS18", "AL133538.1", "DOCK2", "SCN1A-AS1", "AL022068.1", "SEPTIN14", "SGCZ", "ADAM28", "RYR2", "DOCK8", "ACER2", "AC128687.3", "AC120193.1", "OLR1", "AC110296.1", "AC109466.1", "SPOCK3", "ST6GALNAC5", "AL136441.1", "MLIP", "AL158077.2", "AP001021.3", "CCDC85A", "CD96", "NRK", "C8orf37-AS1", "PCDH7", "PLD1", "CHRNA7", "CLRN1", "MYO1D", "RMST", "CNTNAP2", "PURPL", "RALYL", "AL445426.1", "RCAN2", "AL392023.2", "RELN", "AL360091.3", "AC091946.1", "LRRIQ1", "CD163", "SYN3", "IL1RAPL1", "LINC01122", "LINC01091", "AC009126.1", "LINC00944", "LINC01467", "LINC01725", "KCNH7", "AC069228.1", "GNA14-AS1", "KCNIP4", "LINC00504", "AC006299.1", "TPRG1", "AC003092.1", "AC083855.2", "FXYD5", "SYK", "XK", "LINC02006", "KLF5", "WNT16", "NIBAN1", "LINC00355", "LINC01135", "MSR1", "MT2A", "LINC00299", "MX2", "NLGN4X", "LINC00886", "LINC00607", "NHSL2", "MYO1E", "NKAIN2", "NIPAL2", "MYO1F", "LINC01163", "NCMAP", "NHS", "MYRFL", "LINC02234", "LINC01182", "LINC01923", "LINC02246", "LINC02300", "LINC02306", "LINC02378", "LINC02664", "LINC02775", "LINC02798", "LINC02821", "LMNTD1", "LRRTM4", "LURAP1L-AS1", "LINC01934", "LY96", "MAP3K6", "LINC01877", "LINC01208", "LINC01876", "MCTP2", "LINC01842", "LINC01798", "LINC01579", "ME1", "MEGF11", "LINC01357", "MEOX2", "LINC01277", "MGAT4C", "LINC02055", "LINC01241", "MIR548XHG", "MIR222HG", "PTPN14", "OTP", "TAFA2", "TG", "TENT5A", "TENM2", "TEK", "TDO2", "TBX19", "TAPT1-AS1", "SYTL3", "THSD4", "SYT1", "SULF1", "SUCLG2-AS1", "STAT4", "STARD13", "STAC", "SPRY4-AS1", "TGM2", "TLR2", "SPATA48", "VEGFD", "WWTR1", "WIPF1", "WDR49", "VSTM2A-OT1", "VSTM2A", "VSIG4", "VLDLR-AS1", "UTY", "TMEM164", "UNC5C", "UNC13C", "TRPV4", "TRPM8", "TRPM3", "TRIM22", "TMEM63A", "SPINK5", "SPAG17", "PCA3", "POSTN", "RARRES1", "PTPRR", "LINC00158", "PTCHD4", "PTCHD1-AS", "PRSS48", "POU6F2", "PLIN2", "RNF6", "PLAC1", "PKD1L1", "PIP5K1B", "PGLYRP1", "PDE1C", "PCED1B", "PCDH11Y", "RASSF8", "RREB1", "SORCS1", "SLC18A1", "SOCS2-AS1", "SNTG1", "SMOC2", "SLIT2", "SLCO1B1", "SLC35G1", "SLC35E4", "SLC10A6", "RUNX1T1", "SIDT1", "SHOC1", "SAPCD2", "SAMD3", "SAA1", "RYR3", "RXRG", "LINC00278", "AC002074.1", "LGALS1", "AL117329.1", "ADAMTS3", "ADAMTS14", "ACOXL", "AC244472.1", "AC138409.3", "AC124947.1", "AC122697.1", "AC117464.1", "AC114689.3", "AC110023.1", "AC106845.1", "AC097518.2", "AC097462.3", "AC093535.1", "AC093523.1", "AC092958.2", "AC092957.1", "AGMO", "AL121904.2", "AC092131.1", "AL132633.1", "AP000446.1", "ALPK2", "ALDH1A2", "AL732509.1", "AL590608.1", "AL589935.1", "AL512452.1", "AL392086.3", "AL360178.1", "AL354696.2", "AL163636.1", "AL158195.1", "AL158058.1", "AL157911.1", "AL138824.1", "AL137139.2", "AL136038.5", "AC092819.3", "AC091078.1", "AP002495.1", "AC023095.1", "AC022325.2", "AC018616.1", "AC012404.1", "AC012063.1", "AC011246.1", "AC009646.2", "AC008080.4", "AC007681.1", "AC007389.1", "AC007364.1", "AC006994.2", "AC006387.1", "AC006206.2", "AC006041.2", "AC005162.3", "AC004943.2", "AC004879.1", "AC023051.1", "AC024145.1", "AC090578.1", "AC026202.2", "AC090403.1", "AC090337.2", "AC087627.1", "AC087473.1", "AC079950.1", "AC079763.1", "AC079465.1", "AC079298.3", "AC073529.1", "AC073050.1", "AC072062.1", "AC068305.2", "AC067956.1", "AC062022.2", "AC051619.6", "AC040174.1", "AC027097.2", "AP001025.1", "AP002813.1", "LCP2", "GPC3", "GNA14", "GLRA2", "GDNF-AS1", "GCNT2", "FYB1", "FXN", "FRG1-DT", "FRAS1", "FHIT", "FAR2", "FAP", "FAM189A1", "FAAH2", "ERI2", "EPSTI1", "EPHA3", "EPB41L4A", "GNGT1", "GREB1L", "EMILIN2", "GRIN2B", "LANCL3", "KREMEN1", "KCNMB4", "KCNE4", "ITK", "ITGAL", "INPP5D", "IL7", "IL12RB2", "IGSF10", "IAPP", "HS3ST3A1", "HRH1", "AC002429.2", "HMGB2", "HMGA2", "GRIP2", "ENOX2", "ELDR", "AP003066.1", "CFAP77", "CERNA2", "CDH18", "CDH13", "CD247", "CASC9", "C9orf153", "C9orf147", "BX284613.2", "BIRC3", "BEND6", "BCL2L14", "ATP8B4", "ASB18", "ARSJ", "ARRDC3-AS1", "ARHGAP11B", "APBB1IP", "CFAP47", "CFH", "EDN1", "CGNL1", "EBF2", "DOCK5", "DNAH3", "DIPK2A", "DANT2", "CPNE4", "COX8A", "COL4A6", "COL19A1", "COL12A1", "COBLL1", "CNTNAP3B", "CNDP1", "CNBD1", "CHRM3", "CHODL", "CHL1-AS2", "HNF4G"
  ],
  "programs": [
    {
      "program_name": "Immune Checkpoint Signaling",
      "description": "A gene program mediating immune escape through checkpoint molecule expression and T-cell exhaustion pathways. CD96 functions as an immune checkpoint regulating CD8+ T-cell antitumor function. STAT4 regulates PD-L1 expression and immune evasion. CD163 and MSR1 mark pro-tumoral macrophage populations. OLR1 associates with immune cell infiltration and immunosuppression. TLR2 initiates pathogen recognition signaling in innate immune cells. This program collectively enables glioblastoma immune evasion via checkpoint activation and immunosuppressive microenvironment establishment.",
      "atomic_biological_processes": [
        {
          "name": "CD8+ T-cell exhaustion and anergy",
          "citations": [
            {
              "source_id": "42",
              "notes": "CD96 demonstrated to regulate CD8+ T-cell antitumor function and suppress primary tumor growth in combination with other checkpoint inhibitors"
            },
            {
              "source_id": "39",
              "notes": "High CD96+ cell infiltration predicts exhausted CD8+ T-cell phenotype and poor prognosis in gastric cancer"
            }
          ],
          "genes": ["CD96", "STAT4"]
        },
        {
          "name": "PD-L1 transcriptional regulation",
          "citations": [
            {
              "source_id": "54",
              "notes": "STAT4 enrichment at PD-L1 DNA promoter; MET-STAT4-PD-L1 axis enforces glioma immune evasion"
            }
          ],
          "genes": ["STAT4", "CD96"]
        },
        {
          "name": "Macrophage-mediated immunosuppression",
          "citations": [
            {
              "source_id": "49",
              "notes": "MSR1 expressed on macrophages and dendritic cells; role in pro-inflammatory phenotype switching"
            },
            {
              "source_id": "31",
              "notes": "CD163 marks M2-like macrophage polarization in glioblastoma; TAMs promote immunosuppression and anti-inflammatory phenotype"
            }
          ],
          "genes": ["CD163", "MSR1", "OLR1"]
        },
        {
          "name": "Toll-like receptor signaling",
          "citations": [
            {
              "source_id": "44",
              "notes": "TLR2 cooperates with MSR1 to promote pathogen recognition and phagocytosis; activates NF-κB signaling"
            }
          ],
          "genes": ["TLR2"]
        }
      ],
      "atomic_cellular_components": [],
      "predicted_cellular_impact": [
        "Enhanced CD8+ T-cell exhaustion and reduced anti-tumor immunity",
        "Increased PD-L1 expression on tumor cells and immune cells",
        "Macrophage skewing toward pro-tumoral M2 phenotype",
        "Reduced interferon-gamma production and T-cell activation",
        "Increased IL-10 and TGF-β secretion"
      ],
      "evidence_summary": "CD96, STAT4, and CD163 are consistently associated with immune evasion in glioblastoma and other cancers. CD96 directly suppresses CD8+ T-cell function through DNAM-1 inhibition. STAT4 phosphorylation increases PD-L1 transcription. CD163 and MSR1 identify pro-tumoral macrophages enriched in the glioblastoma microenvironment. This convergent pathway enables immune checkpoint activation and T-cell exhaustion, hallmarks of glioblastoma's immunosuppressive microenvironment.",
      "significance_score": 0.85,
      "citations": [
        {
          "source_id": "42",
          "notes": "CD96 immune checkpoint regulates CD8+ T-cell function and metastasis"
        },
        {
          "source_id": "54",
          "notes": "MET-STAT4-PD-L1 axis in glioma immune evasion"
        },
        {
          "source_id": "31",
          "notes": "CD163 and Iba1 in TAM-mediated glioma progression"
        },
        {
          "source_id": "49",
          "notes": "MSR1 in immune regulation and macrophage phenotype"
        }
      ],
      "supporting_genes": ["CD96", "STAT4", "CD163", "MSR1", "OLR1", "TLR2"],
      "required_genes_not_in_input": {
        "genes": ["PD-L1", "PD-1", "CTLA4", "TIGIT", "DNAM-1", "FCER1G"],
        "citations": [
          {
            "source_id": "42",
            "notes": "PD-1, PD-L1, and TIGIT are canonical immune checkpoint molecules that interact with CD96"
          }
        ]
      }
    },
    {
      "program_name": "Receptor Tyrosine Kinase Signaling",
      "description": "A gene program comprising components of receptor tyrosine kinase (RTK) signaling pathways that drive glioblastoma proliferation, survival, and invasion. TEK (Tie2) mediates angiopoietin signaling and vessel maturation. DOCK2, DOCK8, and downstream SYK coordinate Rho GTPase activation for cytoskeletal reorganization. WIPF1 facilitates FAK-mediated actin polymerization. This program collectively enhances receptor-mediated signaling critical for glioblastoma growth and angiogenesis.",
      "atomic_biological_processes": [
        {
          "name": "Angiopoietin-Tie2 signaling",
          "citations": [
            {
              "source_id": "45",
              "notes": "Angiopoietin-1 binds Tie2 receptor to enhance tumor vessel maturation and regulate vascular growth in gliomas"
            },
            {
              "source_id": "48",
              "notes": "Tie2/TEK modulates interaction between glioma and brain tumor stem cells"
            }
          ],
          "genes": ["TEK"]
        },
        {
          "name": "DOCK-mediated Rho GTPase activation",
          "citations": [
            {
              "source_id": "7",
              "notes": "DOCK8 deficiency inhibits BCR signaling and B-cell development; DOCK8 mutation impairs Cdc42-dependent cell migration"
            },
            {
              "source_id": "10",
              "notes": "DOCK2 is Rac GEF critical for leukocyte migration; DOCK8 is Cdc42-specific GEF regulating dendritic cell interstitial migration"
            }
          ],
          "genes": ["DOCK2", "DOCK8"]
        },
        {
          "name": "Spleen tyrosine kinase (SYK) signaling",
          "citations": [
            {
              "source_id": "44",
              "notes": "SYK kinases initiate signaling downstream of Fc receptors and integrins in innate immune cells; activate MAPK and NF-κB"
            },
            {
              "source_id": "47",
              "notes": "SYK phosphorylation activates NLRP3 inflammasome and IL-1β secretion via NF-κB pathway"
            }
          ],
          "genes": ["SYK"]
        },
        {
          "name": "Actin polymerization and cytoskeletal dynamics",
          "citations": [
            {
              "source_id": "21",
              "notes": "TRPV4 colocalizes with F-actin at cellular protrusions; activates Cdc42/N-wasp axis for invadopodia formation"
            },
            {
              "source_id": "10",
              "notes": "WIPF1 and FAK mediate Rho/WASP pathway of actin polymerization for cell adhesion and migration"
            }
          ],
          "genes": ["WIPF1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Cell membrane receptor complexes",
          "citations": [
            {
              "source_id": "55",
              "notes": "RTK/Ras/PI3K signaling altered in 86-90% of GBM cases; RTK dimerization activates downstream signaling"
            }
          ],
          "genes": ["TEK", "DOCK2", "DOCK8"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced angiogenic signaling through Tie2 activation",
        "Increased Rac and Cdc42 GTPase activity driving cell migration",
        "Enhanced focal adhesion signaling and invasive capacity",
        "Elevated MAPK and PI3K/AKT pathway activation",
        "Increased cytoskeletal remodeling and invadopodia formation"
      ],
      "evidence_summary": "TEK/Tie2 signaling promotes glioblastoma angiogenesis and vessel maturation. DOCK2 and DOCK8 act as guanine nucleotide exchange factors (GEFs) for Rac and Cdc42, respectively, driving cytoskeletal reorganization essential for tumor cell migration. SYK couples downstream to both MAPK and PI3K/AKT pathways. WIPF1 coordinates FAK-mediated actin polymerization. Collectively, this program amplifies RTK signaling strength and transduces it into enhanced migration and invasion phenotypes characteristic of malignant glioblastoma.",
      "significance_score": 0.82,
      "citations": [
        {
          "source_id": "55",
          "notes": "RTK/Ras/PI3K pathway altered in 86-90% of GBM; critical for GBM pathogenesis"
        },
        {
          "source_id": "7",
          "notes": "DOCK8 mutation impairs B-cell and T-cell immune responses relevant to glioma microenvironment"
        },
        {
          "source_id": "21",
          "notes": "TRPV4/Cdc42/N-wasp signaling axis regulates invasion-growth in glioblastoma"
        }
      ],
      "supporting_genes": ["TEK", "DOCK2", "DOCK8", "SYK", "WIPF1"],
      "required_genes_not_in_input": {
        "genes": ["RAF", "MEK", "ERK1/2", "PI3K", "AKT", "mTOR", "RAC1", "CDC42"],
        "citations": [
          {
            "source_id": "55",
            "notes": "RAF, MEK, ERK, PI3K, AKT, and mTOR are canonical downstream effectors of RTK signaling in glioblastoma"
          }
        ]
      }
    },
    {
      "program_name": "Synaptic Adhesion and Neuronal Communication",
      "description": "A gene program mediating cell-cell adhesion at synapses and neuron-neuron interactions through adhesion molecules and signaling proteins. CNTNAP2 is essential for synaptic function and neuronal migration; loss impairs E/I balance and cortical development. IL1RAPL1 is a synaptic adhesion molecule recruiting PTPδ and inducing excitatory synapse formation. NLGN4X encodes neuroligin-4, crucial for synaptic organization and neurotransmission. PCDH7 and PCDH11X are protocadherins involved in cell-cell recognition. SYT1 and SYN3 mediate neurotransmitter release and synaptic plasticity. This program regulates the synaptic connectivity landscape that glioma cells aberrantly reactivate.",
      "atomic_biological_processes": [
        {
          "name": "Synaptic adhesion molecule expression",
          "citations": [
            {
              "source_id": "13",
              "notes": "CNTNAP2 is essential for synaptic function; deficiency results in decreased interneurons, impaired cortical layer modeling, and aberrant neuronal migration"
            },
            {
              "source_id": "17",
              "notes": "IL1RAPL1 is a synaptic adhesion molecule localized at postsynaptic membrane; recruits PTPδ for synapse formation"
            },
            {
              "source_id": "12",
              "notes": "NLGN4X mutations disrupt synaptic connectivity and synaptic organization; associated with autism and neurodevelopmental disorders"
            }
          ],
          "genes": ["CNTNAP2", "IL1RAPL1", "NLGN4X", "PCDH7", "PCDH11X"]
        },
        {
          "name": "Neurotransmitter release and synaptic transmission",
          "citations": [
            {
              "source_id": "16",
              "notes": "CNTNAP2 involved in neuron-glia adhesion complex with contactin 2 (TAG-1) and clustering of potassium channels"
            }
          ],
          "genes": ["SYT1", "SYN3", "CNTNAP2"]
        },
        {
          "name": "Neuronal migration and axon guidance",
          "citations": [
            {
              "source_id": "33",
              "notes": "SLIT2 is a secretory glycoprotein binding Robo receptors; acts as axon guidance molecule and regulates radial migration of cortical neurons via autocrine signaling"
            },
            {
              "source_id": "16",
              "notes": "CNTNAP2 implicated in neuronal migration, neuronal network activity, and synaptic spine development"
            }
          ],
          "genes": ["CNTNAP2", "SLIT2", "RELN"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Synaptic membrane proteins",
          "citations": [
            {
              "source_id": "12",
              "notes": "CHRNA7 mutations reduce receptor function; CNTNAP2 clusters at synapses with postsynaptic markers"
            }
          ],
          "genes": ["SYT1", "SYN3", "CNTNAP2", "IL1RAPL1", "NLGN4X"]
        },
        {
          "name": "Extracellular matrix anchoring proteins",
          "citations": [
            {
              "source_id": "33",
              "notes": "SLIT2 binds to heparan sulfate proteoglycans and interacts with extracellular matrix; localizes within basement membrane"
            }
          ],
          "genes": ["SLIT2", "RELN"]
        }
      ],
      "predicted_cellular_impact": [
        "Aberrant reactivation of synaptic adhesion programs in glioma cells",
        "Enhanced intercellular communication and adhesion between tumor cells",
        "Altered calcium signaling through synaptic-like connections",
        "Increased neurotransmitter-like signaling in tumor microenvironment",
        "Formation of tumor cell-neuron hybrid synaptic structures"
      ],
      "evidence_summary": "CNTNAP2, IL1RAPL1, NLGN4X, and protocadherins (PCDH7, PCDH11X) are canonical synaptic adhesion molecules critical for neuronal connectivity. CNTNAP2 mutations associate with neurodevelopmental disorders through disruption of cortical lamination and E/I imbalance—hallmarks of altered neural circuit function. IL1RAPL1 recruits PTPδ to drive postsynaptic density formation. SYT1 and SYN3 mediate presynaptic vesicle dynamics. Notably, glioma cells express synaptic proteins and form tumor-neuron hybrid synapses, facilitating invasion and seizure activity. This program captures the re-expression of synaptic machinery in malignant glioblastoma.",
      "significance_score": 0.78,
      "citations": [
        {
          "source_id": "13",
          "notes": "CNTNAP2 deficiency in ASD and neurodevelopmental disorders; role in E/I balance"
        },
        {
          "source_id": "17",
          "notes": "IL1RAPL1 synaptic adhesion and postsynaptic density formation"
        },
        {
          "source_id": "12",
          "notes": "NLGN4X mutations in autism; synaptic organization and neurotransmission"
        },
        {
          "source_id": "38",
          "notes": "IGSF3 interaction with Kir4.1 and glioma-related epileptiform activity"
        }
      ],
      "supporting_genes": ["CNTNAP2", "IL1RAPL1", "NLGN4X", "PCDH7", "PCDH11X", "SYT1", "SYN3", "SLIT2", "RELN", "CHRNA7"],
      "required_genes_not_in_input": {
        "genes": ["CONTACTIN", "PTPN", "PTPRO", "CONTACTIN-2", "STARGAZIN"],
        "citations": [
          {
            "source_id": "13",
            "notes": "CONTACTIN and PTPN family members are essential partners for CNTNAP2 function in synaptic adhesion"
          }
        ]
      }
    },
    {
      "program_name": "Ion Channel Dysregulation and Excitotoxicity",
      "description": "A gene program mediating alterations in ion channel expression and calcium homeostasis that promote glioma proliferation and seizure activity. TRPV4 elevates intracellular calcium and promotes invadopodia formation via Cdc42/N-wasp signaling. TRPM8 and TRPM3 modulate calcium and cation fluxes. KCNH7, KCNIP4, RYR2, and RYR3 regulate potassium and ryanodine-sensitive calcium channels. GRIN2B encodes NMDA receptor subunit 2B, contributing to glutamate-mediated calcium signaling. FXYD5 regulates Na+/K+-ATPase. This program collectively dysregulates ion homeostasis, promoting both tumor progression and neuronal hyperexcitability manifesting as glioma-related epilepsy.",
      "atomic_biological_processes": [
        {
          "name": "Calcium influx and intracellular calcium elevation",
          "citations": [
            {
              "source_id": "21",
              "notes": "TRPV4 stimulation promotes glioblastoma cell migration and invasion; TRPV4 regulates invadopodia and filopodia formation via Cdc42/N-wasp axis"
            },
            {
              "source_id": "11",
              "notes": "Alterations in Ca2+ toolkit (TRPC and TRPV channels) in glioblastoma; increased expression of TRPC1, TRPC6, TRPV1, TRPV2"
            },
            {
              "source_id": "8",
              "notes": "Glutamate-mediated calcium signaling provides positive feedback to promote glioma formation; enhanced Ca2+ activates nitric oxide synthase"
            }
          ],
          "genes": ["TRPV4", "TRPM8", "TRPM3", "RYR2", "RYR3", "GRIN2B"]
        },
        {
          "name": "Potassium channel dysregulation and ion imbalance",
          "citations": [
            {
              "source_id": "38",
              "notes": "IGSF3 interacts with Kir4.1 to suppress potassium buffering; impaired K+ handling linked to glioma proliferation and seizure activity"
            }
          ],
          "genes": ["KCNH7", "KCNIP4", "FXYD5"]
        },
        {
          "name": "Glutamate-mediated excitotoxicity",
          "citations": [
            {
              "source_id": "8",
              "notes": "Glutamatergic and calcium signaling provides positive feedback for glioma formation; upregulation of GluRs and enhanced glutamate release facilitate seizure-like activity"
            }
          ],
          "genes": ["GRIN2B"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Calcium-activated signaling complexes",
          "citations": [
            {
              "source_id": "8",
              "notes": "CaMK2A intimately interacts with GluRs; elevated intracellular Ca2+ activates downstream kinases and promotes metabolic reprogramming"
            }
          ],
          "genes": ["TRPV4", "TRPM8", "RYR2", "GRIN2B"]
        }
      ],
      "predicted_cellular_impact": [
        "Increased intracellular free calcium concentration",
        "Enhanced invadopodia formation and invasion capacity",
        "Dysregulated potassium buffering and loss of ion homeostasis",
        "Amplified glutamate-mediated excitatory signaling",
        "Glioma-related seizures and epileptiform activity",
        "Metabolic reprogramming via calcium-dependent kinases"
      ],
      "evidence_summary": "TRPV4 channel activation directly promotes glioblastoma invasion by elevating intracellular calcium and activating the Cdc42/N-wasp axis. TRPV4 expression is elevated in malignant glioma compared to low-grade glioma and correlates with poor prognosis. KCNH7, KCNIP4, and related potassium channels are downregulated in glioma, impairing potassium buffering. IGSF3-mediated suppression of Kir4.1 potassium channel function links ion dysregulation to proliferation and seizure activity. GRIN2B and glutamate receptor upregulation contribute to Ca2+-mediated excitotoxicity and formation of tumor-neuron hybrid synapses. RYR2 and RYR3 release calcium from intracellular stores. This convergent program dysregulates ion homeostasis, driving both invasion and glioma-related epileptic activity.",
      "significance_score": 0.81,
      "citations": [
        {
          "source_id": "21",
          "notes": "TRPV4 elevated in malignant glioma; TRPV4/Cdc42/N-wasp axis regulates invasion and invadopodia formation"
        },
        {
          "source_id": "38",
          "notes": "IGSF3-Kir4.1 interaction impairs potassium buffering; dysregulation linked to glioma proliferation and seizures"
        },
        {
          "source_id": "8",
          "notes": "Glutamate-calcium signaling provides positive feedback for glioma progression"
        },
        {
          "source_id": "11",
          "notes": "Calcium channel alterations in glioblastoma stem cells and glioma tissue"
        }
      ],
      "supporting_genes": ["TRPV4", "TRPM8", "TRPM3", "KCNH7", "KCNIP4", "RYR2", "RYR3", "GRIN2B", "FXYD5"],
      "required_genes_not_in_input": {
        "genes": ["STIM1", "ORAI1", "CAMK2A", "CAMK2D", "KNCJ10"],
        "citations": [
          {
            "source_id": "11",
            "notes": "STIM1 and ORAI1 mediate store-operated calcium entry; CAMK2A couples calcium to downstream signaling in glioma"
          },
          {
            "source_id": "38",
            "notes": "KNCJ10 (Kir4.1) is essential for potassium buffering but suppressed by IGSF3 in glioma"
          }
        ]
      }
    },
    {
      "program_name": "Extracellular Matrix Remodeling and Invasion",
      "description": "A gene program controlling extracellular matrix (ECM) degradation, remodeling, and production that facilitates glioma invasion and infiltration into normal brain parenchyma. ADAMTS3, ADAMTS14, and ADAMTS18 are metalloproteases cleaving lecticans and other ECM components. POSTN (periostin) is upregulated in cancer-associated fibroblasts and promotes ECM remodeling and invasion. SULF1 modifies heparan sulfate proteoglycans. COL4A6, COL12A1, COL19A1 are collagen scaffolds. SMOC2 and other matricellular proteins regulate cell-matrix interactions. This program collectively restructures the brain microenvironment to enable glioma cell dissemination.",
      "atomic_biological_processes": [
        {
          "name": "Lectin cleavage and ECM degradation",
          "citations": [
            {
              "source_id": "18",
              "notes": "BEHAB/brevican proteolytic processing by ADAMTS family at specific sites is necessary for pro-invasive effect in glioma"
            }
          ],
          "genes": ["ADAMTS3", "ADAMTS14", "ADAMTS18"]
        },
        {
          "name": "Periostin-mediated matrix remodeling",
          "citations": [
            {
              "source_id": "32",
              "notes": "POSTN exclusively upregulated in cancer-associated fibroblasts (matCAFs); promotes fibroblast proliferation, migration, and ECM remodeling"
            },
            {
              "source_id": "35",
              "notes": "POSTN mediates collagen production and ECM remodeling in tissue fibrosis and cancer"
            }
          ],
          "genes": ["POSTN"]
        },
        {
          "name": "Heparan sulfate proteoglycan modification",
          "citations": [
            {
              "source_id": "33",
              "notes": "SLIT2 is a ligand of heparan sulfate proteoglycan glypican-1; proper localization within basement membrane is key for axon guidance"
            }
          ],
          "genes": ["SULF1"]
        },
        {
          "name": "Collagen fiber organization",
          "citations": [
            {
              "source_id": "15",
              "notes": "Collagen density and organization in ECM profoundly influence glioma invasion; intermediate collagen concentrations maximize invasion in vitro"
            }
          ],
          "genes": ["COL4A6", "COL12A1", "COL19A1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Extracellular matrix scaffold",
          "citations": [
            {
              "source_id": "15",
              "notes": "ECM composition includes fibrous collagen and afibrous components; glioma cells interact with both via cell-cell and cell-ECM contacts"
            }
          ],
          "genes": ["POSTN", "ADAMTS3", "COL4A6", "COL12A1", "SMOC2"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced ECM degradation and proteolytic remodeling",
        "Increased invasive capacity into surrounding brain parenchyma",
        "Altered collagen fiber alignment facilitating migration",
        "Enhanced cell-matrix interactions promoting dissemination",
        "Reduced ECM mechanical impedance to tumor infiltration"
      ],
      "evidence_summary": "ADAMTS metalloproteases are the predominant ECM-degrading enzymes in glioma. BEHAB/brevican, a CNS-specific lecticans, requires ADAMTS-mediated cleavage at specific sites (396SRG398) to promote glioma invasion in vitro and in vivo. Periostin (POSTN) is highly expressed in matrix-remodeling cancer-associated fibroblasts (matCAFs) and promotes both CAF migration and ECM remodeling. SULF1 modifies heparan sulfate, altering growth factor availability and cell-matrix interactions. Collagen organization influences glioma invasiveness—intermediate collagen density maximizes invasion. This program collectively restructures the neural ECM, reducing mechanical resistance to glioma infiltration and creating pro-invasive microenvironment.",
      "significance_score": 0.80,
      "citations": [
        {
          "source_id": "18",
          "notes": "ADAMTS-mediated BEHAB/brevican cleavage necessary for glioma invasion"
        },
        {
          "source_id": "32",
          "notes": "POSTN upregulation in cancer-associated fibroblasts; promotes ECM remodeling and invasion"
        },
        {
          "source_id": "15",
          "notes": "ECM composition and organization profoundly influence glioma invasion patterns"
        }
      ],
      "supporting_genes": ["ADAMTS3", "ADAMTS14", "ADAMTS18", "POSTN", "SULF1", "COL4A6", "COL12A1", "COL19A1", "SMOC2"],
      "required_genes_not_in_input": {
        "genes": ["MMP2", "MMP9", "TIMP1", "TIMP2", "ADAMTS1", "ADAMTS2"],
        "citations": [
          {
            "source_id": "18",
            "notes": "MMP2 and MMP9 are major ECM-degrading enzymes; TIMP1/2 are natural inhibitors"
          }
        ]
      }
    },
    {
      "program_name": "Angiogenesis and Vascular Development",
      "description": "A gene program regulating blood vessel formation and vascular endothelial cell function that supports glioma growth. VEGFD (VEGF-D) is secreted by tumor cells and activates VEGFR-2 and VEGFR-3 on endothelial cells. TEK (Tie2) mediates angiopoietin signaling for vessel maturation and stabilization. KLF5 promotes glioblastoma angiogenesis by inducing AGGF1 gene transcription in glioma-associated endothelial cells. This program collectively drives pathological neovascularization that perfuses the tumor and enables growth beyond diffusion limits.",
      "atomic_biological_processes": [
        {
          "name": "VEGF-D signaling and vascular proliferation",
          "citations": [
            {
              "source_id": "50",
              "notes": "VEGF-D is a secreted glycoprotein binding VEGFR-2 and VEGFR-3; higher mitogenic ability than VEGF-A; upregulated in glioblastoma"
            },
            {
              "source_id": "53",
              "notes": "VEGF-D mature form strongly supports angiogenesis and lymphangiogenesis; dual functionality in coordinating vascular and lymphatic growth"
            }
          ],
          "genes": ["VEGFD"]
        },
        {
          "name": "Tie2-angiopoietin vascular stabilization",
          "citations": [
            {
              "source_id": "45",
              "notes": "Angiopoietin-1 activates Tie2 to enhance tumor vessel maturation; inhibits vascular leakage"
            }
          ],
          "genes": ["TEK"]
        },
        {
          "name": "KLF5-mediated angiogenic factor expression",
          "citations": [
            {
              "source_id": "19",
              "notes": "KLF5 promotes glioblastoma angiogenesis by inducing AGGF1 transcription in glioma-associated endothelial cells"
            }
          ],
          "genes": ["KLF5"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Vascular endothelial cell surface receptors",
          "citations": [
            {
              "source_id": "53",
              "notes": "VEGFR2 and VEGFR3 are primary receptors for VEGF-D; expressed on endothelial cells and lymphatic endothelial cells"
            }
          ],
          "genes": ["VEGFD", "TEK"]
        }
      ],
      "predicted_cellular_impact": [
        "Increased endothelial cell proliferation and vascular sprouting",
        "Enhanced vascular permeability and blood-brain barrier dysfunction",
        "Vessel stabilization and reduced hemorrhagic necrosis",
        "Increased oxygen and nutrient delivery to tumor",
        "Promotion of glioma cell intravasation and dissemination"
      ],
      "evidence_summary": "VEGF-D exhibits higher mitogenic potency than VEGF-A and is upregulated in glioblastoma in response to anti-VEGF-A therapy, enabling antiangiogenic resistance. VEGF-D activates both VEGFR-2 (blood angiogenesis) and VEGFR-3 (lymphangiogenesis), providing dual-pathway vascular stimulation. TEK/Tie2 signaling complements VEGF-D by stabilizing nascent vessels through angiopoietin binding. KLF5-driven AGGF1 expression in glioma-associated endothelial cells further amplifies angiogenic signals. This convergent program overcomes anti-VEGF-A therapy and sustains the neovascular network essential for glioma progression.",
      "significance_score": 0.77,
      "citations": [
        {
          "source_id": "50",
          "notes": "VEGF-D role in glioblastoma angiogenesis and resistance to anti-VEGF therapy"
        },
        {
          "source_id": "45",
          "notes": "Angiopoietin-Tie2 signaling in glioma vessel maturation"
        },
        {
          "source_id": "19",
          "notes": "KLF5 promotes glioblastoma angiogenesis via AGGF1"
        }
      ],
      "supporting_genes": ["VEGFD", "TEK", "KLF5"],
      "required_genes_not_in_input": {
        "genes": ["VEGFA", "VEGFR1", "VEGFR2", "ANGPT1", "ANGPT2", "FLT1"],
        "citations": [
          {
            "source_id": "50",
            "notes": "VEGF-A and angiopoietins are canonical angiogenic factors; VEGFR1/2 are essential receptors"
          }
        ]
      }
    },
    {
      "program_name": "Wnt/β-Catenin Self-Renewal Signaling",
      "description": "A gene program mediating Wnt signaling pathway activation that promotes glioma stem cell self-renewal and inhibits differentiation. WNT16 is a Wnt ligand activating canonical β-catenin signaling. This program drives stemness maintenance and chemotherapy resistance characteristic of glioblastoma stem cells (GSCs), which are responsible for tumor recurrence.",
      "atomic_biological_processes": [
        {
          "name": "Canonical Wnt/β-catenin pathway activation",
          "citations": [
            {
              "source_id": "27",
              "notes": "WNT signaling involved in maintaining stemness of normal stem cells; aberrant activation in GBM promotes GSC growth and invasion"
            },
            {
              "source_id": "30",
              "notes": "Dysregulation of Wnt pathway supports onset of cancer stem cells (CSCs); alterations in Wnt components discriminate normal from malignant cells in adult brain"
            }
          ],
          "genes": ["WNT16"]
        },
        {
          "name": "Stemness maintenance and self-renewal",
          "citations": [
            {
              "source_id": "30",
              "notes": "β-catenin nuclear localization and TCF4 expression significantly higher in glioma than normal brain tissue; positively correlates with WHO grade"
            }
          ],
          "genes": ["WNT16"]
        }
      ],
      "atomic_cellular_components": [],
      "predicted_cellular_impact": [
        "Increased glioma stem cell self-renewal capacity",
        "Enhanced resistance to differentiation signals",
        "Improved tumor growth and propagation",
        "Enhanced chemotherapy and radiotherapy resistance",
        "Tumor recurrence and regrowth after standard therapy"
      ],
      "evidence_summary": "WNT/β-catenin signaling is aberrantly activated in glioblastoma and drives GSC self-renewal. β-catenin and TCF4 nuclear accumulation correlates with glioma grade and poor prognosis. Inhibition of WNT signaling via β-catenin modulation impedes glioma stem cell clonogenic growth. WNT signaling activation promotes GSC stemness while inhibiting differentiation, enabling indefinite self-renewal and tumor propagation. This program captures the dysregulated developmental pathway that maintains glioma stem cell identity.",
      "significance_score": 0.72,
      "citations": [
        {
          "source_id": "27",
          "notes": "WNT signaling roles in GSC self-renewal and glioma progression"
        },
        {
          "source_id": "30",
          "notes": "Wnt/β-catenin pathway dysregulation in glioblastoma; correlation with WHO grade and poor prognosis"
        }
      ],
      "supporting_genes": ["WNT16"],
      "required_genes_not_in_input": {
        "genes": ["FZD", "LRP5", "LRP6", "GSK3B", "APC", "AXIN", "TCF", "LEF1", "β-CATENIN"],
        "citations": [
          {
            "source_id": "30",
            "notes": "FZD, LRP, GSK3B, APC, AXIN, TCF, and β-catenin are canonical Wnt pathway components"
          }
        ]
      }
    },
    {
      "program_name": "Epithelial-Mesenchymal Transition and Invasion",
      "description": "A gene program regulating epithelial-mesenchymal transition (EMT) that enables glioma cell migration, invasion, and dissemination. EMT transcription factors (TWIST-family, SNAIL-family, ZEB-family, SOX2) promote acquisition of mesenchymal phenotype and down-regulation of epithelial markers. TGM2 (tissue transglutaminase) is upregulated during EMT and promotes invasion. POSTN supports EMT through CAF interactions. This program collectively drives the phenotypic plasticity enabling glioma cells to invade adjacent brain tissue and metastasize.",
      "atomic_biological_processes": [
        {
          "name": "EMT transcription factor activation",
          "citations": [
            {
              "source_id": "56",
              "notes": "TWIST1 mediates EMT by inhibiting E-cadherin and promoting N-cadherin expression; drives invasive glioma phenotype"
            },
            {
              "source_id": "59",
              "notes": "SNAIL, TWIST, and ZEB families are major EMT regulators; overexpression associated with invasive ability and chemotherapy resistance"
            }
          ],
          "genes": ["TGM2"]
        },
        {
          "name": "E-cadherin to N-cadherin switch",
          "citations": [
            {
              "source_id": "56",
              "notes": "Loss of E-cadherin often accompanied by increased N-cadherin; N-cadherin overexpression linked to invasion and metastasis"
            }
          ],
          "genes": ["TGM2"]
        },
        {
          "name": "Vimentin upregulation and EMT markers",
          "citations": [
            {
              "source_id": "56",
              "notes": "Overexpression of vimentin linked to enhanced invasiveness and metastasis in glioblastoma; EMT marker"
            }
          ],
          "genes": ["TGM2"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Adherens junction remodeling",
          "citations": [
            {
              "source_id": "59",
              "notes": "EMT involves disruption of E-cadherin/catenin complexes; remodeling of adherens junctions enabling migration"
            }
          ],
          "genes": ["TGM2", "POSTN"]
        }
      ],
      "predicted_cellular_impact": [
        "Increased cell motility and migration capacity",
        "Enhanced invasive capability into surrounding brain parenchyma",
        "Reduced intercellular adhesion and increased dissemination",
        "Acquisition of stem cell-like properties",
        "Increased resistance to chemotherapy and radiotherapy"
      ],
      "evidence_summary": "EMT is fundamentally linked to glioma invasion and stemness. TWIST, SNAIL, and ZEB transcription factors suppress E-cadherin and promote mesenchymal marker expression. TGM2 (transglutaminase-2) catalyzes cross-linking of EMT-related proteins and supports invasion. POSTN from cancer-associated fibroblasts promotes EMT through YAP1/TEAD1 signaling. Notably, the E-cadherin to N-cadherin switch is not universally required in glioblastoma EMT, suggesting context-dependent mechanisms. This program captures the phenotypic plasticity enabling glioma dissemination and therapy resistance.",
      "significance_score": 0.75,
      "citations": [
        {
          "source_id": "56",
          "notes": "EMT and E-cadherin/N-cadherin switching in glioblastoma invasion"
        },
        {
          "source_id": "59",
          "notes": "EMT transcription factors and stemness maintenance in glioma"
        },
        {
          "source_id": "32",
          "notes": "POSTN promotes EMT and invasion in gastric cancer; relevant to glioma microenvironment"
        }
      ],
      "supporting_genes": ["TGM2", "POSTN"],
      "required_genes_not_in_input": {
        "genes": ["TWIST", "SNAIL", "ZEB", "SOX2", "CDH1", "CDH2", "VIM"],
        "citations": [
          {
            "source_id": "56",
            "notes": "TWIST, SNAIL, ZEB, SOX2 are canonical EMT transcription factors; CDH1/2 and VIM are marker genes"
          }
        ]
      }
    },
    {
      "program_name": "Hypoxia-Responsive Transcription",
      "description": "A gene program activated under hypoxic conditions (low oxygen) in glioblastoma that drives metabolic reprogramming, angiogenesis, and stemness maintenance. This program includes HIF-1α and HIF-2α-dependent transcriptional responses, though HIFs themselves are not in the input list. VEGFD, TEK, and KLF5 are key HIF-target genes promoting angiogenesis. Downstream metabolic enzymes (ME1 for gluconeogenesis; SUCLG2 for TCA cycle) support hypoxic metabolism. This program collectively enables tumor survival and growth in the hypoxic glioblastoma microenvironment.",
      "atomic_biological_processes": [
        {
          "name": "Angiogenic factor upregulation",
          "citations": [
            {
              "source_id": "57",
              "notes": "Under hypoxia, HIF1α upregulates expression of VEGF and other pro-angiogenic factors; essential for glioblastoma vascularization"
            },
            {
              "source_id": "60",
              "notes": "HIF-1α and HIF-2α regulate VEGF expression; HIF-2α promotes stem cell phenotype in glioblastoma stem cells"
            }
          ],
          "genes": ["VEGFD", "TEK", "KLF5"]
        },
        {
          "name": "Metabolic reprogramming and glycolysis",
          "citations": [
            {
              "source_id": "57",
              "notes": "Under hypoxia, HIF1α promotes glycolysis via upregulation of HK2 and PDK1; shift from glucose to glutamine metabolism"
            },
            {
              "source_id": "60",
              "notes": "HIF-regulated metabolic reprogramming essential for glioblastoma survival and proliferation in hypoxic microenvironment"
            }
          ],
          "genes": ["ME1", "SUCLG2"]
        },
        {
          "name": "Cancer stem cell maintenance",
          "citations": [
            {
              "source_id": "57",
              "notes": "Hypoxia-induced HIF1α promotes stemness and self-renewal of GSCs; maintains pluripotency markers"
            },
            {
              "source_id": "60",
              "notes": "HIF-2α serves unique role in GSC development and maintenance; induces pluripotent stem cell markers (OCT4, NANOG, SOX2)"
            }
          ],
          "genes": ["VEGFD", "KLF5"]
        }
      ],
      "atomic_cellular_components": [],
      "predicted_cellular_impact": [
        "Enhanced survival under hypoxic stress",
        "Increased VEGF production and angiogenesis",
        "Metabolic shift toward glycolysis and amino acid metabolism",
        "Enhanced glioma stem cell self-renewal",
        "Resistance to hypoxia-induced apoptosis"
      ],
      "evidence_summary": "Hypoxia is endemic to glioblastoma due to rapid growth outpacing oxygen diffusion. HIF-1α and HIF-2α accumulation activates transcriptional programs supporting glioma survival, proliferation, and stemness. VEGFD is a canonical HIF-target gene promoting angiogenesis that partially circumvents hypoxic stress. TEK-mediated vessel maturation further improves perfusion. KLF5 drives glioma-associated endothelial cell angiogenic programs. ME1 and SUCLG2 support hypoxic metabolic reprogramming. Notably, IDH-mutant gliomas exhibit altered HIF signaling, suggesting context-dependent hypoxic responses. This program captures the transcriptional adaptation enabling glioblastoma survival in its oxygen-poor microenvironment.",
      "significance_score": 0.74,
      "citations": [
        {
          "source_id": "57",
          "notes": "Hypoxia-induced HIF signaling in glioblastoma; metabolic reprogramming and GSC maintenance"
        },
        {
          "source_id": "60",
          "notes": "HIF-1α and HIF-2α in stemness and metabolic adaptation in glioblastoma"
        }
      ],
      "supporting_genes": ["VEGFD", "TEK", "KLF5", "ME1", "SUCLG2"],
      "required_genes_not_in_input": {
        "genes": ["HIF1A", "HIF2A", "HIF3A", "PHD2", "PHD3", "VHL", "HK2", "PDK1", "GLUT1"],
        "citations": [
          {
            "source_id": "57",
            "notes": "HIF1A, HIF2A, PHD, and VHL are central to hypoxic signaling; HK2, PDK1, GLUT1 are HIF-target metabolic genes"
          }
        ]
      }
    },
    {
      "program_name": "Lipid Metabolism and Signaling",
      "description": "A gene program regulating lipid metabolism, storage, and signaling that supports glioblastoma proliferation and stemness. PLD1 (phospholipase D1) catalyzes phosphatidic acid production, acting as both an enzymatic catalyst and scaffolding protein in Wnt/β-catenin, PI3K/Akt, and HIF signaling. OLR1 (LOX-1) is a scavenger receptor mediating oxidized lipid uptake and promoting EMT and stemness. ACER2 (alkaline ceramidase 2) regulates ceramide metabolism. This program collectively integrates lipid signaling into core oncogenic pathways.",
      "atomic_biological_processes": [
        {
          "name": "Phospholipase D signaling",
          "citations": [
            {
              "source_id": "20",
              "notes": "PLD1 catalyzes PA production; acts as scaffold protein in Wnt/β-catenin and PI3K/Akt pathways; dual roles in HIF-1α regulation"
            }
          ],
          "genes": ["PLD1"]
        },
        {
          "name": "Oxidized lipid uptake and scavenging",
          "citations": [
            {
              "source_id": "25",
              "notes": "OLR1 expression associated with cancer immune escape and targeting OLR1 increases tumor T-cell infiltration"
            },
            {
              "source_id": "52",
              "notes": "MSR1 mediates uptake of modified lipoprotein; involved in metabolic inflammation and cancer progression"
            }
          ],
          "genes": ["OLR1"]
        },
        {
          "name": "Cancer stem cell self-renewal via lipid signaling",
          "citations": [
            {
              "source_id": "20",
              "notes": "PLD1 governs self-renewal of cancer-initiating cells through E2F1–miR-4496–β-catenin axis"
            }
          ],
          "genes": ["PLD1", "OLR1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Plasma membrane lipid microdomains",
          "citations": [
            {
              "source_id": "20",
              "notes": "PLD1 acts as scaffold protein to increase signaling efficiency and coordinate complex upstream signals"
            }
          ],
          "genes": ["PLD1", "OLR1"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced PI3K/Akt and mTOR signaling",
        "Increased Wnt/β-catenin pathway activation",
        "Enhanced stemness and self-renewal capacity",
        "Improved metabolic flexibility under diverse nutrient conditions",
        "Reduced immune cell infiltration and T-cell activation"
      ],
      "evidence_summary": "PLD1 operates as both an enzymatic catalyst and scaffolding platform in glioblastoma oncogenic signaling. PLD1 catalyzes production of phosphatidic acid (PA), a signaling lipid, while its protein domains scaffold Wnt/β-catenin and PI3K/Akt pathway components. PLD1-mediated HIF-1α translation and protein stabilization supports hypoxic survival. Targeting PLD1 decreases RB1 and promotes E2F1-dependent apoptosis via miR-192/4465. OLR1 is a scavenger receptor mediating oxidized lipid uptake; high OLR1 expression correlates with EMT, stemness, and immune escape. This convergent program integrates lipid signaling into core stem cell renewal and metabolic adaptation pathways.",
      "significance_score": 0.71,
      "citations": [
        {
          "source_id": "20",
          "notes": "PLD1 as key player in cancer stemness and Wnt/PI3K cross-talk"
        },
        {
          "source_id": "25",
          "notes": "OLR1 in cancer immune escape and EMT"
        }
      ],
      "supporting_genes": ["PLD1", "OLR1", "ACER2"],
      "required_genes_not_in_input": {
        "genes": ["PTEN", "PI3K", "AKT", "mTOR", "WNT", "FZD", "GSK3B"],
        "citations": [
          {
            "source_id": "20",
            "notes": "PLD1 scaffolds and coordinates PI3K/Akt and Wnt pathway signaling"
          }
        ]
      }
    },
    {
      "program_name": "Tumor-Associated Macrophage Polarization",
      "description": "A gene program regulating polarization and activation of tumor-associated macrophages (TAMs) that create an immunosuppressive microenvironment. CD163 identifies M2-like pro-tumor macrophages enriched in glioblastoma. MSR1 (CD204) is a macrophage-specific receptor involved in pro-inflammatory phenotype. OLR1 is overexpressed in myeloid-derived suppressor cells (MDSCs) and promotes immunosuppression. LCP2 and FYB1 facilitate leukocyte signaling. VSIG4 is an immunosuppressive receptor on macrophages. This program collectively recruits and polarizes TAMs toward anti-tumor immunity suppression.",
      "atomic_biological_processes": [
        {
          "name": "M2 macrophage polarization",
          "citations": [
            {
              "source_id": "31",
              "notes": "CD163 marks M2-like macrophage polarization; IL-33 produced by Iba1+ TAMs feeds back to GSCs to maintain stemness"
            },
            {
              "source_id": "34",
              "notes": "IL-6 promotes macrophage transition to pro-tumor phenotype and secretion of IL-10 and TGF-β"
            }
          ],
          "genes": ["CD163", "MSR1"]
        },
        {
          "name": "Immunosuppressive cell recruitment",
          "citations": [
            {
              "source_id": "25",
              "notes": "OLR1 expression associated with T-cell exhaustion and immunosuppressive cell infiltration"
            },
            {
              "source_id": "34",
              "notes": "CCL8 secreted by TAMs binds CCR5/CCR1 to activate ERK1/2 in glioma cells"
            }
          ],
          "genes": ["OLR1", "LCP2"]
        },
        {
          "name": "Leukocyte adhesion and migration",
          "citations": [
            {
              "source_id": "10",
              "notes": "DOCK2 critical for leukocyte migration and trafficking; DOCK8 deficiency impairs immune cell development"
            }
          ],
          "genes": ["LCP2", "FYB1"]
        },
        {
          "name": "Immunosuppressive checkpoint signaling",
          "citations": [
            {
              "source_id": "34",
              "notes": "VSIG4 is B7 family member functioning as immunosuppressive receptor on macrophages"
            }
          ],
          "genes": ["VSIG4"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Macrophage surface receptors",
          "citations": [
            {
              "source_id": "49",
              "notes": "MSR1 and CD163 are macrophage-specific scavenger receptors; CD36 also involved in lipid uptake"
            }
          ],
          "genes": ["CD163", "MSR1", "OLR1", "VSIG4"]
        }
      ],
      "predicted_cellular_impact": [
        "Increased macrophage infiltration into glioblastoma",
        "Polarization toward pro-tumor M2 phenotype",
        "Enhanced IL-10 and TGF-β secretion",
        "Reduced CD8+ T-cell activation and infiltration",
        "Increased glioma stem cell maintenance via IL-33"
      ],
      "evidence_summary": "CD163, a marker of M2-like pro-tumor macrophages, is highly expressed in glioblastoma-associated macrophages (Iba1+ cells). CD163-positive macrophages secrete anti-inflammatory cytokines (IL-10, TGF-β) that suppress CD8+ T-cell responses. IL-6 promotes CD40 expression and M2 polarization via Stat3/HIF-1α. Notably, Iba1+ TAMs produce IL-33, which feeds back to glioma stem cells to maintain stemness and support tumor progression. MSR1 (CD204) mediates lipid uptake and links lipid metabolism to macrophage polarization. OLR1 is enriched in pro-tumor PMN-MDSCs. VSIG4 on macrophages delivers immunosuppressive signals. This convergent program shapes the TAM-rich immunosuppressive microenvironment enabling glioblastoma immune evasion.",
      "significance_score": 0.79,
      "citations": [
        {
          "source_id": "31",
          "notes": "CD163, Iba1, and IL-33 in TAM-mediated glioma progression"
        },
        {
          "source_id": "34",
          "notes": "TAM polarization and CCL8 secretion in glioma immune evasion"
        },
        {
          "source_id": "25",
          "notes": "OLR1 in immunosuppressive cell infiltration"
        },
        {
          "source_id": "49",
          "notes": "MSR1 in macrophage-mediated immune regulation"
        }
      ],
      "supporting_genes": ["CD163", "MSR1", "OLR1", "LCP2", "FYB1", "VSIG4"],
      "required_genes_not_in_input": {
        "genes": ["IL10", "TGFB1", "IL6", "CCL2", "CSF1", "M-CSFR"],
        "citations": [
          {
            "source_id": "31",
            "notes": "IL-10, TGF-β, IL-6, and CCL2 are key cytokines in macrophage polarization and immune suppression"
          }
        ]
      }
    },
    {
      "program_name": "GTPase Activation and Cytoskeletal Remodeling",
      "description": "A gene program regulating small GTPase (Rho, Rac, Cdc42) activation and actin cytoskeleton reorganization that enables glioma cell migration and invasion. DOCK2 and DOCK8 are guanine nucleotide exchange factors (GEFs) that activate Rac (DOCK2) and Cdc42 (DOCK8). Downstream effectors (N-WASP, WAVE) nucleate actin filaments. WIPF1 facilitates FAK-Rac coupling. STAC and RCAN2 coordinate Cdc42 and calcium signaling. This program collectively enables rapid morphological changes and invasion-promoting cellular protrusions.",
      "atomic_biological_processes": [
        {
          "name": "Rac1 GTPase activation",
          "citations": [
            {
              "source_id": "10",
              "notes": "DOCK2 mediates GDP-GTP exchange for Rac; crystal structure shows DHR-2 domain binds Rac exclusively at lobes B and C"
            }
          ],
          "genes": ["DOCK2"]
        },
        {
          "name": "Cdc42 GTPase activation",
          "citations": [
            {
              "source_id": "10",
              "notes": "DOCK8 is Cdc42-specific GEF; different lobe orientation than DOCK2-Rac1 complex"
            },
            {
              "source_id": "21",
              "notes": "TRPV4 activates Cdc42/N-wasp axis in glioblastoma; promotes invadopodia and filopodia formation"
            }
          ],
          "genes": ["DOCK8", "TRPV4"]
        },
        {
          "name": "Actin filament nucleation and polymerization",
          "citations": [
            {
              "source_id": "10",
              "notes": "DOCK8 couples to LRAP35a and MRCKα to phosphorylate myosin II regulatory light chain (MLC2)"
            }
          ],
          "genes": ["WIPF1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Guanine nucleotide exchange factor complexes",
          "citations": [
            {
              "source_id": "10",
              "notes": "DOCK DHR-2 domain is core GEF module; DOCK8 associates with adaptor proteins like LRAP35a"
            }
          ],
          "genes": ["DOCK2", "DOCK8", "STAC"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced Rac1 activation and lamellipodia formation",
        "Enhanced Cdc42 activation and filopodia formation",
        "Increased actin polymerization and cytoskeletal reorganization",
        "Enhanced cell migration velocity and invasiveness",
        "Increased invadopodia formation for ECM degradation"
      ],
      "evidence_summary": "DOCK2 and DOCK8 are non-canonical GEFs lacking DH domains but retaining GDP-GTP exchange activity via DHR-2 domains. DOCK2-Rac coupling promotes lymphocyte migration; DOCK8-Cdc42 coupling regulates interstitial dendritic cell migration. In glioblastoma, TRPV4 activates Cdc42 downstream to N-WASP, promoting invadopodia formation and invasion. WIPF1 links FAK to Rho/WASP pathway actin polymerization. STAC coordinates Cdc42 signaling. Collectively, this program enables rapid GTPase cycling and actin dynamics underlying glioma cell motility and invasive morphology.",
      "significance_score": 0.76,
      "citations": [
        {
          "source_id": "10",
          "notes": "DOCK2 and DOCK8 as Rho GTPase GEFs in immune cell migration"
        },
        {
          "source_id": "21",
          "notes": "TRPV4-Cdc42-N-wasp axis in glioblastoma invasion"
        }
      ],
      "supporting_genes": ["DOCK2", "DOCK8", "WIPF1", "STAC", "RCAN2", "TRPV4"],
      "required_genes_not_in_input": {
        "genes": ["RAC1", "CDC42", "NWASP", "WAVE", "ARPC", "ARP2", "ARP3", "FAK"],
        "citations": [
          {
            "source_id": "10",
            "notes": "RAC1, CDC42, N-WASP, and WAVE are canonical downstream effectors of DOCK GEFs"
          }
        ]
      }
    }
  ],
  "method": {
    "clustering_basis": [
      "Pathway databases (KEGG, Reactome) for signaling pathways",
      "Co-citation analysis of genes in glioblastoma literature",
      "Protein-protein interaction networks for physical associations",
      "Shared cellular functions and biological processes",
      "Tissue-specific expression patterns in glioblastoma"
    ],
    "notes": "Genes were clustered into programs by identifying convergent functions relevant to glioblastoma pathobiology: immune evasion, receptor signaling, synaptic reactivation, ion dysregulation, ECM remodeling, angiogenesis, EMT/invasion, metabolic adaptation, and cytoskeletal dynamics. Many genes appear in multiple programs reflecting pathway cross-talk (e.g., TRPV4 in both ion channels and GTPase programs; PLD1 in lipid metabolism and Wnt signaling). Programs were prioritized by literature support, number of supporting genes, and functional coherence within glioblastoma context. Long non-coding RNAs with limited functional annotation were not assigned to specific programs."
  },
  "version": "1.0"
}
```

# Comprehensive Literature Analysis: Gene Programs in Malignant Glioblastoma

## Executive Summary

The analyzed gene list comprises approximately 330 genes with diverse functions in glioblastoma biology. Through systematic literature analysis, **twelve coherent gene programs** have been identified that collectively drive glioblastoma hallmark phenotypes: immune evasion, proliferation, invasion, angiogenesis, and therapy resistance. These programs cluster around core oncogenic processes including immune checkpoint signaling, receptor tyrosine kinase activation, synaptic reactivation, ion dysregulation, extracellular matrix remodeling, and metabolic reprogramming. The programs demonstrate extensive pathway cross-talk, with individual genes frequently participating in multiple processes (e.g., TRPV4 in both calcium signaling and Cdc42 activation; PLD1 in lipid signaling and Wnt pathway scaffolding). Notably, **many genes in the input list appear poorly characterized in the glioblastoma literature**, particularly long non-coding RNAs and genes identified primarily through genomic studies without functional validation. The most robustly supported programs involve immune checkpoints (CD96, STAT4, CD163), receptor signaling (DOCK2/8, TEK), synaptic adhesion (CNTNAP2, IL1RAPL1), ion channels (TRPV4, KCNIP4), and ECM remodeling (ADAMTS3/14/18, POSTN).

## Overview of Gene Program Architecture

The twelve identified programs operate through interconnected molecular networks:

**Tier 1 - Boundary and Communication Programs** (Programs 1-3): These programs establish glioblastoma's interactions with the tumor microenvironment through immune evasion (immune checkpoint signaling), angiogenic factor secretion (angiogenesis), and aberrant synaptic-like communication (synaptic adhesion reactivation).

**Tier 2 - Signaling and Transduction Programs** (Programs 4-5, 10): These programs amplify and transduce extracellular signals into intracellular responses via receptor tyrosine kinases, ion channel dysregulation, and GTPase activation, collectively enabling rapid cellular responses to microenvironmental cues.

**Tier 3 - Cellular Phenotype and Behavior Programs** (Programs 6-9, 12): These programs drive the characteristic malignant behaviors of glioblastoma—invasion through EMT programs and ECM remodeling, self-renewal through Wnt signaling and stemness maintenance, metabolic adaptation through hypoxia responses, and immune evasion through macrophage polarization.

## Program 1: Immune Checkpoint Signaling - Mechanisms of Immune Escape

The immune checkpoint program represents one of the most clinically significant gene programs, as it directly enables glioblastoma's evasion of anti-tumor immunity. **CD96** functions as a novel immune checkpoint molecule expressed on exhausted CD8+ T-cells[42]. Blocking CD96 suppresses primary tumor growth in multiple experimental mouse tumor models in a CD8+ T-cell-dependent manner[42], establishing CD96 as both a marker and driver of T-cell exhaustion. Mechanistically, CD96 coexpresses with PD-1 on tumor-infiltrating lymphocytes in both mouse and human cancers[42], suggesting coordinated checkpoint activation.

**STAT4** serves as the critical transcriptional linker between receptor signaling and PD-L1 expression. In glioblastoma, chromatin immunoprecipitation-PCR demonstrates STAT4 enrichment in the PD-L1 DNA promoter[54], establishing STAT4 as a direct transcriptional activator of immune checkpoint molecule expression. Correlation analysis across multiple glioma datasets shows STAT4 expression strongly predicts PD-L1 upregulation and poor overall survival[54]. Importantly, the MET-STAT4-PD-L1 axis associates with increased macrophage infiltration, suggesting crosstalk between receptor tyrosine kinase signaling and immune evasion.

**CD163 and MSR1** identify pro-tumor macrophage populations in glioblastoma. CD163, a marker of M2-like pro-tumor macrophages, is enriched in glioblastoma-associated macrophages[31]. IL-33 production by Iba1+ CD163+ cells provides paracrine signals to glioma stem cells, sustaining stemness and tumor propagation[31]. MSR1 (also CD204) is a class A scavenger receptor mediating pro-inflammatory macrophage phenotype switching[49]. Co-expression of MSR1 with TLR4 activates NF-κB signaling and inflammatory cytokine production[49].

**OLR1** (LOX-1) represents an emerging axis in glioblastoma immune evasion. OLR1 expression is enriched in myeloid-derived suppressor cells (PMN-MDSCs) and other immunosuppressive cell types[25]. High OLR1 expression in tumors correlates with reduced T-cell infiltration, increased T-cell exhaustion, and elevated MSI scores (marker of immunosuppression)[25]. Remarkably, OLR1 knockdown in head and neck squamous cell carcinoma restricts epithelial-mesenchymal plasticity and invasiveness[25], suggesting OLR1 couples immune suppression to EMT programs.

**TLR2** initiates pathogen recognition signaling in innate immune cells. TLR2 cooperates with MSR1 to activate NF-κB signaling and promote pro-inflammatory cytokine production[44]. In glioblastoma macrophages, TLR2 signaling may reinforce pro-tumor polarization through context-dependent inflammatory signals.

The mechanistic integration of this program involves STAT4-mediated PD-L1 transcription in response to upstream receptor signaling, CD163-marked macrophage infiltration supporting IL-33 production, and OLR1+ MDSC-mediated T-cell exhaustion. Collectively, these genes establish a multi-layered immune checkpoint program enabling glioblastoma immune escape through both direct checkpoint expression and macrophage-mediated immunosuppression.

## Program 2: Receptor Tyrosine Kinase Signaling - Amplification of Growth Signals

RTK signaling pathways are altered in 86-90% of glioblastomas[55], making this program fundamental to glioblastoma pathogenesis. **TEK** (Tie2), a tyrosine kinase receptor, mediates angiopoietin signaling for vascular maturation and vessel stability[45]. Angiopoietin-1 binding to Tie2 enhances tumor vessel maturation while simultaneously promoting glioma stem cell maintenance through paracrine signaling[48].

**DOCK2 and DOCK8** occupy unique positions as non-canonical GEFs lacking DH domains but retaining full GDP-GTP exchange activity[10]. DOCK2 specifically activates Rac1, a small GTPase critical for leukocyte migration[10]. Crystal structural analysis reveals the DHR-2 domain of DOCK2 engages Rac exclusively through lobes B and C, explaining Rac specificity[10]. In contrast, DOCK8 is a Cdc42-specific GEF with different lobe orientations[10]. DOCK8 mutations cause autosomal recessive hyper-IgE syndrome through impaired B and T cell function[7], and DOCK8 deficiency inhibits BCR clustering and signalosome recruitment during B cell activation[7]. In glioblastoma, DOCK-mediated GTPase activation drives actin cytoskeleton reorganization essential for invasion.

**SYK** (Spleen Tyrosine Kinase) couples downstream to both MAPK and PI3K/AKT pathways. SYK phosphorylation activates NLRP3 inflammasome formation via NF-κB pathway[47], linking immune signaling to metabolic reprogramming. SYK-dependent signaling exhibits context-dependent effects: in vaccinated macrophages, SYK coupling to C-type lectin receptors drives inflammasome activation[47], while in tumor microenvironments, SYK may promote pro-tumor myeloid polarization.

**WIPF1** (WAS Interacting Protein Family Member 1) links focal adhesion kinase (FAK) to the Rho/WASP actin polymerization pathway. WIPF1-mediated FAK signaling promotes cytoskeletal reorganization essential for both leukocyte and tumor cell migration[10].

Integration of this RTK program amplifies growth factor signaling through multiple mechanisms: (1) TEK-angiopoietin coupling maintains vascular support; (2) DOCK-mediated GTPase activation enables rapid morphological responses; (3) SYK coupling activates both metabolic and inflammatory downstream pathways; (4) FAK-WIPF1 coupling promotes invasive morphology. The prevalence of RTK pathway alterations in glioblastoma makes this program central to understanding therapeutic resistance to single-agent RTK inhibitors.

## Program 3: Synaptic Adhesion and Neuronal Communication

Glioblastoma cells aberrantly reactivate synaptic adhesion programs normally confined to neurons. **CNTNAP2** (Contactin-Associated Protein-Like 2) is essential for synaptic function and neuronal migration. CNTNAP2 deficiency results in decreased interneurons, impaired cortical layer modeling, and aberrant neuronal migration[13]. Loss of CNTNAP2 suppresses excitatory synaptic transmission in pyramidal neurons through E/I imbalance[13]. CNTNAP2 functions as a key hub linking neuronal migration, synaptic plasticity, and potential seizure susceptibility in glioblastoma.

**IL1RAPL1** (Interleukin-1 Receptor Accessory Protein-Like 1) is a synaptic adhesion molecule localized at the postsynaptic membrane[17]. IL1RAPL1 recruits protein tyrosine phosphatase δ (PTPδ) to drive excitatory synapse formation[17]. Over-expression of IL1RAPL1 induces increased PSD-95 (excitatory postsynaptic marker) and dendritic protrusion number, promoting synaptic development.

**NLGN4X** (Neuroligin-4, X-linked) encodes a postsynaptic cell adhesion molecule critical for synaptic organization and neurotransmission. NLGN4X mutations disrupt synaptic connectivity and function, contributing to autism spectrum disorders[12]. These mutations impair social communication and repetitive behaviors through aberrant synaptic organization. In glioblastoma, NLGN4X reactivation may enable tumor cell-neuron hybrid synapse formation, contributing to seizure activity and invasion.

**PCDH7 and PCDH11X** are protocadherins involved in cell-cell recognition and adhesion. PCDH11X polymorphisms associate with late-onset Alzheimer's disease[2], reflecting its role in neuronal connectivity. In glioblastoma, protocadherin reactivation may enable aberrant cell-cell communication.

**SYT1** (Synaptotagmin-1) mediates neurotransmitter release through calcium-dependent SNARE complex regulation. **SYN3** (Synapsin-3) regulates synaptic vesicle dynamics and neurotransmitter release probability. Both genes are neural-specific and typically silenced in non-neuronal tissues.

**SLIT2** and **RELN** represent secreted axon guidance molecules. SLIT2 binds Robo receptors to regulate radial migration of cortical neurons through an autocrine signaling mechanism—transfection of individual neurons with SLIT2 knockdown results in migration delay in only those cells, without affecting neighboring untransfected neurons[33]. SLIT2 binds heparan sulfate proteoglycans and directly to dystroglycan in the basement membrane, establishing physical ECM anchoring[33]. This extracellular matrix-dependent signaling mechanism may enable glioma cells to hijack neuronal guidance cues.

Mechanistically, this program enables glioblastoma cells to form synaptic-like structures with surrounding neurons through coordinated expression of pre- and postsynaptic adhesion molecules. The presence of functional synaptic proteins on tumor cells facilitates (1) enhanced intercellular adhesion within the tumor; (2) formation of tumor-neuron hybrid synapses that promote invasion and facilitate seizure activity; (3) neurotransmitter-like signaling in the tumor microenvironment.

## Program 4: Ion Channel Dysregulation and Calcium Excitotoxicity

**TRPV4** (Transient Receptor Potential Vanilloid 4) is a calcium-permeable cation channel dramatically upregulated in malignant glioma[21]. TRPV4 expression increases with glioma malignancy grade and negatively correlates with patient prognosis[21]. Functionally, TRPV4 stimulation promotes glioblastoma cell migration and invasion[21]. Mechanistically, TRPV4 strongly colocalizes and interacts with F-actin at cellular protrusions[21], and TRPV4 activation promotes invadopodia and filopodia formation via Cdc42/N-WASP signaling axis[21]. Remarkably, TRPV4 inhibitor treatment or TRPV4 downregulation significantly reduces invasion-growth of both subcutaneous and intracranial transplanted glioblastoma in mice[21], establishing TRPV4 as a therapeutic target.

**TRPM8** and **TRPM3** modulate calcium and cation fluxes. These channels are members of the TRP channel family implicated in diverse cellular functions. In glioblastoma, TRPM8 is discussed as a potential diagnostic and prognostic marker[24].

**Potassium Channels (KCNH7, KCNIP4)** regulate resting membrane potential and excitability. In glioblastoma, potassium channel dysregulation is mechanistically linked to both proliferation and seizure activity. **IGSF3** (Immunoglobulin Superfamily Member 3) interacts with Kir4.1 (encoded by KCNJ10, not in input list) to suppress potassium buffering capacity[38]. This IGSF3-Kir4.1 interaction impairs astrocytic potassium handling, leading to potassium accumulation and enhanced neuronal excitability. Remarkably, Kir4.1 overexpression restores mouse survival in IGSF3-overexpressing tumors, demonstrating that impaired K+ buffering is mechanistically required for IGSF3-driven glioma progression[38]. Patient scRNA-seq analysis reveals that tumor cells from glioma-related epilepsy (GRE) patients exhibit decreased expression of potassium-handling genes (ATP1A2, ATP1B2, KCNIP1, KCNJ10, KCNIP4)[38], linking ion dysregulation to seizure pathophysiology.

**RYR2 and RYR3** are ryanodine-sensitive intracellular calcium release channels. These channels mobilize calcium from the sarcoplasmic/endoplasmic reticulum in response to depolarization and calcium influx, amplifying intracellular calcium signals.

**GRIN2B** encodes the NMDA receptor subunit 2B, a key component of glutamate-mediated calcium signaling. **FXYD5** (FXYD Domain Containing Ion Transport Regulator 5) regulates Na+/K+-ATPase activity, directly influencing ionic gradients.

Mechanistically, this program dysregulates ion homeostasis through multiple mechanisms: (1) TRPV4 activation elevates intracellular calcium and promotes invadopodia formation; (2) IGSF3-mediated suppression of Kir4.1 impairs potassium buffering; (3) GRIN2B upregulation amplifies glutamate-mediated calcium excitotoxicity; (4) RYR2/3 augment intracellular calcium mobilization. Collectively, these alterations create a pro-invasive, hyperexcitable state characterized by elevated intracellular calcium, impaired ion homeostasis, and glioma-related seizure activity.

## Program 5: Extracellular Matrix Remodeling and Invasion

**ADAMTS Metalloproteases (ADAMTS3, ADAMTS14, ADAMTS18)** are critical ECM-degrading enzymes. ADAMTS proteins belong to the "A Disintegrin And Metalloproteinase with ThromboSpondin Motifs" family. ADAMTS-mediated cleavage of brain-specific lectican BEHAB/brevican at a specific site (396SRG398 → NVY) is necessary for pro-invasive effect in glioma[18]. Remarkably, an uncleavable BEHAB/brevican mutant is unable to enhance glioma cell invasion in vitro or tumor progression in vivo[18], establishing ADAMTS-mediated lectin cleavage as a necessary step in invasion. ADAMTS enzymatic activity must occur at specific sites to generate functional matrix-remodeling fragments.

**POSTN** (Periostin) is a matricellular protein upregulated in cancer-associated fibroblasts (matCAFs). POSTN is predominantly enriched in matrix-remodeling CAFs (~30% of fibroblasts express high POSTN)[32]. POSTN expression correlates with poor prognosis in gastric cancer and promotes CAF proliferation, migration, and ECM remodeling[32]. Mechanistically, POSTN transcription is directly regulated by YAP1/TEAD1 co-transcription factor binding[32]. POSTN-positive fibroblasts exhibit elevated expression of ECM regulators, suggesting coordinated matrix remodeling[32]. In the glioblastoma microenvironment, POSTN-expressing CAFs provide both secreted POSTN and physical ECM scaffolds that facilitate tumor cell invasion.

**SULF1** (Sulfatase 1) modifies heparan sulfate proteoglycans. By removing 6-O-sulfate groups, SULF1 alters the binding of growth factors to heparan sulfate, influencing their bioavailability and signaling intensity.

**Collagen Genes (COL4A6, COL12A1, COL19A1)** encode structural ECM proteins. The organization and density of collagen fibers profoundly influence glioma invasiveness[15]. Remarkably, glioma invasion is maximized at intermediate collagen concentrations—very high collagen density becomes inhibitory, suggesting that optimal invasion requires a balance between ECM support and penetrability[15].

**SMOC2** (SPARC-related modular calcium-binding protein 2) is a matricellular protein regulating cell-matrix interactions.

Mechanistically, this program restructures the neural ECM to enable glioma infiltration through: (1) ADAMTS-mediated specific cleavage of lectican components; (2) POSTN-expressing CAF-derived ECM remodeling; (3) SULF1-mediated heparan sulfate modification altering growth factor signaling; (4) optimized collagen density and organization. The program collectively reduces ECM mechanical impedance while maintaining sufficient scaffold for tumor cell migration.

## Program 6: Angiogenesis and Vascular Development

**VEGFD** (VEGF-D/VEGF-D) is a secreted vascular growth factor distinct from canonical VEGF-A. VEGF-D exhibits higher mitogenic potency than VEGF-A and binds both VEGFR-2 (blood endothelial cells) and VEGFR-3 (lymphatic endothelial cells)[50]. Notably, anti-VEGF-A monoclonal antibody therapy (bevacizumab) upregulates VEGF-D expression in gliosarcomas; although tumor growth is initially slower, established tumors show better vascularization[50], suggesting VEGF-D mediates resistance to anti-VEGF-A monotherapy. VEGF-D undergoes proteolytic processing by proprotein convertases and ADAMTS3, generating a mature form (~21 kDa) with high affinity for both VEGFR-2 and VEGFR-3[53]. This dual receptor specificity enables VEGF-D to coordinate both blood and lymphatic vascular growth.

**TEK** (Tie2) is a tyrosine kinase receptor for angiopoietins. Angiopoietin-1 binding to Tie2 promotes vascular maturation, reduces permeability, and stabilizes nascent blood vessels[45]. In glioblastoma, Tie2 signaling complements VEGF-D by shifting the vascular phenotype from proliferative to mature, reducing hemorrhagic necrosis and hypoxic stress.

**KLF5** (Krüppel-Like Factor 5) is a transcription factor promoting glioblastoma angiogenesis by inducing AGGF1 (Angiogenic Factor With G Patch And FHA Domains 1) expression in glioma-associated endothelial cells[19]. KLF5 also regulates numerous target genes involved in proliferation, stemness, and invasion[19]. Notably, KLF5 expression is elevated in multiple cancer types, and KLF5 somatic superenhancer duplications and hotspot mutations drive cancer cell proliferation and tumorigenesis[22].

Mechanistically, this program enables glioblastoma vascularization through: (1) VEGF-D secretion by tumor cells directly activating endothelial VEGFR-2/3; (2) TEK-angiopoietin coupling stabilizing vessel maturation; (3) KLF5-driven endothelial angiogenic programs. The program collectively establishes robust blood vessel formation, reducing diffusion-dependent constraints on tumor growth.

## Program 7: Wnt/β-Catenin Self-Renewal Signaling

**WNT16** is a Wnt ligand activating canonical β-catenin signaling. WNT signaling is aberrantly activated in glioblastoma and promotes glioma stem cell self-renewal[27][30]. In normal development, WNT/β-catenin signaling directs neural progenitor cell commitment and proliferation, but in glioblastoma, constitutive activation promotes indefinite stem cell-like properties. Nuclear β-catenin and TCF4 levels are significantly elevated in glioma compared to normal brain tissue and positively correlate with WHO glioma grade[30].

Mechanistically, this program enables GSC maintenance through: (1) WNT16 binding to frizzled and LRP5/6 receptors (not in input list); (2) prevention of β-catenin phosphorylation and degradation; (3) β-catenin nuclear translocation and TCF/LEF complex formation; (4) transcriptional activation of stemness genes. Notably, WNT inhibition via β-catenin modulation impedes glioma stem cell clonogenic growth, establishing this pathway as necessary for GSC maintenance.

## Program 8: Epithelial-Mesenchymal Transition and Invasion

**TGM2** (Transglutaminase-2, also called tissue transglutaminase) is upregulated during EMT and promotes invasion. TGM2 catalyzes protein cross-linking, stabilizing EMT-related proteins and promoting invasive capacity.

**POSTN** also supports EMT programs through interactions with cancer-associated fibroblasts. POSTN-expressing CAFs promote tumor cell EMT via YAP1/TEAD1-regulated paracrine signaling[32].

Mechanistically, this program drives phenotypic plasticity and invasion through: (1) activation of EMT transcription factors (TWIST, SNAIL, ZEB—not in input list); (2) TGM2-mediated protein cross-linking; (3) adherens junction remodeling; (4) increased cell motility and reduced intercellular adhesion. Notably, the canonical E-cadherin to N-cadherin switch is not universally required in glioblastoma EMT[56], suggesting context-dependent mechanisms.

## Program 9: Hypoxia-Responsive Transcription and Metabolic Reprogramming

**VEGFD, TEK, KLF5** are canonical HIF-target genes upregulated under hypoxic stress. Under hypoxia (typical in glioblastoma cores), HIF-1α and HIF-2α accumulate and activate transcriptional programs supporting survival[57][60]. HIF-1α promotes glycolysis via upregulation of HK2 and PDK1[57], enabling ATP generation under oxygen deprivation. Notably, HIF-2α exhibits unique roles in glioblastoma stem cells, promoting pluripotent stem cell marker expression (OCT4, NANOG, SOX2)[60].

**ME1** (Malic Enzyme 1) catalyzes the conversion of malate to pyruvate, supporting gluconeogenesis and NADPH production. **SUCLG2-AS1** (lncRNA associated with SUCLG2) may regulate TCA cycle flux through its mRNA target.

Mechanistically, this program enables glioblastoma survival in hypoxic microenvironments through: (1) HIF-dependent VEGF-D upregulation promoting angiogenesis; (2) metabolic shift toward glycolysis; (3) amino acid metabolism (glutamine → α-KG); (4) GSC stemness maintenance via HIF-2α. The program directly couples hypoxic stress to both metabolic adaptation and stem cell programs.

## Program 10: Lipid Metabolism and Signaling

**PLD1** (Phospholipase D1) catalyzes phosphatidic acid (PA) production and serves as a scaffolding platform in multiple oncogenic pathways. PLD1 enzymatic activity promotes HIF-1α translation via mTOR coupling[20], while PLD1 protein directly destabilizes HIF-1α by interacting with VHL-dependent degradation machinery[20]. This dual activity enables fine-tuning of HIF-1α levels. Remarkably, PLD1 governs cancer-initiating cell self-renewal through the E2F1–miR-4496–β-catenin axis[20], linking lipid signaling to Wnt pathway activation. PLD1 inhibition decreases RB1 via miR-192/4465, promoting E2F1-dependent apoptosis[20].

**OLR1** (Oxidized Lipoprotein Receptor 1, LOX-1) mediates uptake of oxidized lipoproteins. OLR1 expression is associated with cancer immune escape, EMT, and stemness[25]. Remarkably, OLR1 expression is enriched in pro-tumor PMN-MDSCs and correlates with T-cell dysfunction[25]. Targeting OLR1 increases tumor T-cell infiltration and MSI (microsatellite instability)[25].

**ACER2** (Alkaline Ceramidase 2) regulates ceramide metabolism, a key lipid signaling molecule.

Mechanistically, this program integrates lipid signaling into core oncogenic pathways through: (1) PLD1-mediated PA generation supporting PI3K/AKT, mTOR, and Wnt signaling; (2) PLD1 scaffolding of signaling complexes; (3) OLR1-mediated immune escape and EMT; (4) ceramide-mediated cell death evasion.

## Program 11: Tumor-Associated Macrophage Polarization

**CD163, MSR1, OLR1** identify and mark pro-tumor macrophage and myeloid populations. CD163 is specifically enriched in M2-like pro-tumor macrophages[31]. IL-33 produced by CD163+ TAMs feeds back to glioma stem cells to maintain stemness[31]. MSR1 mediates lipid uptake and pro-inflammatory signaling[49]. OLR1 is enriched in immunosuppressive PMN-MDSCs[25].

**LCP2** (Lymphocyte Cytoplasmic Protein 2, also called Lyn substrate 1) and **FYB1** (FYB1 Protein Homolog With EVH1 Domain) facilitate leukocyte signaling through coupling to adaptor proteins.

**VSIG4** (V-Set Immunoregulatory Receptor) is an immunosuppressive B7 family member expressed on macrophages.

Mechanistically, this program shapes the immunosuppressive microenvironment through: (1) recruitment of CD163+ M2 macrophages; (2) IL-33-mediated GSC stemness maintenance; (3) MSR1-driven lipid-inflammation axis; (4) OLR1+ MDSC immunosuppression; (5) VSIG4 checkpoint signaling. Collectively, these genes establish a pro-tumor myeloid infiltrate.

## Program 12: GTPase Activation and Cytoskeletal Remodeling

**DOCK2, DOCK8** are guanine nucleotide exchange factors (GEFs) that activate Rho family GTPases. DOCK2 activates Rac1; DOCK8 activates Cdc42[10]. These GTPases directly couple to actin polymerization machinery (N-WASP, WAVE). **WIPF1** links FAK to the Rho/WASP pathway[10].

**STAC** and **RCAN2** coordinate GTPase and calcium signaling, providing cross-talk between ion homeostasis and cytoskeletal dynamics.

**TRPV4** also contributes to this program through Cdc42 activation[21].

Mechanistically, this program enables rapid cytoskeletal reorganization through: (1) DOCK-mediated GTPase cycling; (2) WIPF1-FAK coupling to actin polymerization; (3) synchronized calcium-GTPase signaling. The program collectively drives the morphological plasticity enabling glioma invasion.

---

## Cross-Program Integration and Pathway Convergence

The twelve identified programs exhibit extensive cross-talk and redundancy. For example:

- **Immune checkpoint signaling (Program 1)** converges with **TAM polarization (Program 11)** through shared use of STAT4 and IL-33 signaling.
- **RTK signaling (Program 2)** activates both **GTPase remodeling (Program 12)** and **lipid metabolism (Program 10)** through PLD1 and FAK coupling.
- **Ion channel dysregulation (Program 4)** synergizes with **GTPase activation (Program 12)** in invadopodia formation through TRPV4-Cdc42 coupling.
- **Hypoxia response (Program 9)** converges with **angiogenesis (Program 6)** through HIF-dependent VEGF-D upregulation.
- **Wnt signaling (Program 7)** cross-talks with **lipid metabolism (Program 10)** through PLD1 scaffolding of β-catenin complexes.

## Therapeutic Implications

The program-level analysis reveals multiple therapeutic opportunities:

1. **Dual checkpoint blockade**: Combining CD96 inhibition with PD-1/PD-L1 blockade is superior to single-agent therapy[42].
2. **ADAMTS inhibition**: Blocking lectin cleavage may reduce invasion without broad metalloproteinase inhibition[18].
3. **TRPV4 targeting**: TRPV4 inhibitors effectively reduce glioblastoma invasion in vivo[21].
4. **PLD1 inhibition**: Combined with standard chemotherapy to overcome stemness-mediated resistance[20].
5. **OLR1 targeting**: May restore T-cell infiltration and overcome immune evasion[25].

## Conclusions

The analyzed gene list reveals twelve coherent gene programs collectively driving hallmark glioblastoma phenotypes. These programs operate through interconnected signaling networks with extensive cross-talk and redundancy. The most robustly supported programs involve immune evasion, receptor signaling, synaptic reactivation, ion dysregulation, and EMT/invasion. Many genes in the input list require additional functional validation in glioblastoma-specific contexts, particularly long non-coding RNAs and genes identified primarily through genomic studies. The program-level analysis framework enables integrated therapeutic targeting that addresses multiple hallmark phenotypes simultaneously, potentially overcoming monotherapy resistance that characterizes glioblastoma.

## Citations

1. https://www.genecards.org/cgi-bin/carddisp.pl?gene=LINC02235
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC2873177/
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC6681239/
4. https://maayanlab.cloud/Harmonizome/search?q=Protein-tyrosine+phosphatase%2C+receptor%2Fnon-receptor+type
5. https://www.proteinatlas.org/ENSG00000102290-PCDH11X/cancer
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC6364698/
7. https://www.nature.com/articles/s41419-024-07180-w
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC8403340/
9. https://pubmed.ncbi.nlm.nih.gov/26719016/
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC6949370/
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC7691577/
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC11438927/
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC11646403/
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC4867007/
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC2599859/
16. https://onlinelibrary.wiley.com/doi/10.1111/jnc.13403
17. https://www.semanticscholar.org/paper/c3bf37c20c7c21a10a6a01764b6b02c448aa0237
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC3896091/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC8177779/
20. https://www.nature.com/articles/s12276-024-01260-9
21. https://www.nature.com/articles/s41598-020-70822-4
22. https://aacrjournals.org/cancerdiscovery/article/8/1/108/112872/Somatic-Superenhancer-Duplications-and-Hotspot
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC5593623/
24. https://pubmed.ncbi.nlm.nih.gov/33928077/
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC10454104/
26. https://en.wikipedia.org/wiki/Glial_cell_line-derived_neurotrophic_factor
27. https://www.nature.com/articles/labinvest2015140
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC7438715/
29. https://pubmed.ncbi.nlm.nih.gov/21865882/
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC5852601/
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC12070867/
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC12278709/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC11646887/
34. https://www.nature.com/articles/s41698-023-00431-7
35. https://www.nature.com/articles/s41598-025-11409-9
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC8376357/
37. https://www.nature.com/articles/s41388-023-02883-4
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC9991983/
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC9746045/
40. https://pmc.ncbi.nlm.nih.gov/articles/PMC11249581/
41. https://livrepository.liverpool.ac.uk/3137928/1/200850788_Jan2020.pdf
42. https://pubmed.ncbi.nlm.nih.gov/30894377/
43. https://pubmed.ncbi.nlm.nih.gov/35029322/
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC3039931/
45. https://pmc.ncbi.nlm.nih.gov/articles/PMC8095963/
46. https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.16347
47. https://www.embopress.org/doi/10.15252/emmm.202215888
48. https://www.oncotarget.com/article/204/
49. https://pmc.ncbi.nlm.nih.gov/articles/PMC9618966/
50. https://pmc.ncbi.nlm.nih.gov/articles/PMC10487419/
51. https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2021.625234/full
52. https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2022.1050984/full
53. https://www.nature.com/articles/s41392-025-02249-0
54. https://pmc.ncbi.nlm.nih.gov/articles/PMC8527154/
55. https://www.nature.com/articles/sigtrans201740
56. https://pmc.ncbi.nlm.nih.gov/articles/PMC12547761/
57. https://pmc.ncbi.nlm.nih.gov/articles/PMC10177528/
58. https://pmc.ncbi.nlm.nih.gov/articles/PMC6609345/
59. https://pmc.ncbi.nlm.nih.gov/articles/PMC7586027/
60. https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2023.1227884/full
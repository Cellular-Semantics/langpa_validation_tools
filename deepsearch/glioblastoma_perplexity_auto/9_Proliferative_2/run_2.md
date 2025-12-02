---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-11-26T14:39:47.065153'
end_time: '2025-11-26T14:43:25.006020'
duration_seconds: 217.94
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 59
---

## Question

Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: ["FAM111B", "MYBL2", "EXO1", "ZNF367", "BRIP1", "CLSPN", "CHAF1A", "DTL", "PCLAF", "CHEK1", "CDC45", "FANCA", "MCM6", "RRM2", "MCM10", "ASF1B", "CENPU", "FANCD2", "POLA2", "MIR924HG", "CCNE2", "WDR76", "ESCO2", "FBLN7", "CENPK", "NXPH2", "MELK", "CHAF1B", "GRM8", "HELLS", "POLE2", "E2F1", "E2F7", "DHFR", "ABHD3", "CDCA7", "ASPN", "FANCI", "RAD18", "XRCC2", "AC008543.1", "GINS1", "AL034348.1", "BRCA1", "BRCA2", "SPC24", "KIF15", "AC011447.3", "VRK1", "WDHD1", "KIF24", "XYLB", "SKA3", "RAB39A", "LRRC63", "RAD54L", "DIAPH3", "CGAS", "CENPP", "SPC25", "CENPI", "PRIM2", "POLQ", "KBTBD12", "RAD51AP1", "AMPH", "LIG1", "AC007681.1", "MCM5", "AC130324.2", "TNFAIP8", "AURKB", "DDX11-AS1", "SIMC1", "MMS22L", "MCM4", "ATAD2", "FANCB", "DNA2", "AC006115.2", "TRPC3", "PLD5", "PLK4", "LIMK2", "ESPL1", "TP73", "ARNTL2", "ZNF90", "MBNL3", "AC004943.2", "KIAA0319", "COL9A1", "MYBL1", "NEIL3", "WDR62", "SDK1", "LAMA1", "CLN6", "PER3", "PCNA", "CCDC138", "ECM2", "CAMK4", "EFNA5", "CD83", "REXO5", "DDB2", "MCM8", "KIFC1", "CEP152", "IQGAP3", "AC104073.4", "DAPK2", "KNTC1", "ZGRF1", "RFC2", "MND1", "UHRF1", "MBOAT1", "SFMBT1", "RFC3", "CKAP2L", "POLA1", "KCTD16", "ARHGAP11B", "BICC1", "SVEP1", "AP002495.1", "FAM189A1", "SYK", "ORC6", "GHR", "FOXM1", "HMGN2", "ZNF730", "GLYATL2", "ARHGAP19", "HMGB2", "HESX1", "AC009630.1", "STAC", "PBK", "TCF19", "MASTL"]

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
This is a complex query that asks me to perform a comprehensive literature analysis of a gene list in the context of malignant glioblastoma cells. The user wants me to:

1. Analyze ~150 genes provided
2. Identify clusters of genes that act together in pathways/processes
3. Create gene programs from these clusters
4. Interpret findings in light of normal physiology and disease-specific alterations
5. Return results in JSON format following a specific schema

Looking at the genes provided and the search results, I can see strong evidence for several gene programs in glioblastoma context:

1. **DNA Replication and S-phase progression** - MCM2-7 complex, CDC45, GINS1, POLA1, POLA2, PRIM2, POLE2, RRM2, MCM10, MCM4, MCM5, MCM6, MCM8, PCNA, RFC2, RFC3, ORC6, CDT1 (not in list), etc.

2. **DNA Damage Response and Checkpoint Control** - CHEK1, ATM, ATR (not in list), BRCA1, BRCA2, RAD51, RAD18, XRCC2, BRIP1, FANCI, FANCD2, FANCA, FANCB, DNA2, EXO1, etc.

3. **Homologous Recombination Repair** - BRCA1, BRCA2, RAD51, RAD18, RAD54L, XRCC2, RRM2, MND1, RAD51AP1

4. **Cell Cycle Regulation and Mitosis** - AURKB, PLK4, ESPL1, MYBL2, E2F1, E2F7, CDKs, Cyclins (CCNE2, etc.), WEE1, CDC25 (not in list)
 
I identify additional critical gene programs that highlight cellular regulation mechanisms in glioblastoma:

5. **Centrosome Dynamics** - Key genes like PLK4 and multiple CENP proteins suggest intricate mechanisms controlling cellular division and structural organization.

6. **Epigenetic Regulation** - Genes involved in chromatin modification indicate complex transcriptional control, with proteins like ASF1B and UHRF1 potentially driving aberrant gene expression.

7. **Proliferation Control** - Transcription factors such as FOXM1 and MYBL2 emerge as potential master regulators driving uncontrolled cellular growth characteristic of glioblastoma.

8. **DNA Repair and Genomic Stability** - The Fanconi Anemia pathway genes like FANCA and FANCD2 reveal sophisticated mechanisms for maintaining chromosomal integrity during cellular stress.

Emerging gene networks highlight E2F1, E2F7, and TP73 as critical nodes in transcriptional and cell cycle regulation, suggesting complex interactions driving tumor progression.

Key observations span DNA repair strategies, including trans-lesion synthesis, mismatch repair mechanisms, and checkpoint activation pathways. The intricate interplay between DNA replication proteins and damage response systems underscores cellular resilience and potential therapeutic vulnerabilities.

Checkpoint kinases, homologous recombination factors, and replication licensing proteins form interconnected networks that modulate genomic stability in cancer contexts, particularly in glioblastoma research.

I'll systematically map gene programs across critical cellular processes, emphasizing molecular interactions and regulatory dynamics that govern genomic maintenance and cell cycle progression.
</think>

```json
{
  "context": {
    "cell_type": "malignant glioblastoma cells; glioblastoma stem-like cells",
    "disease": "glioblastoma multiforme; high-grade glioma",
    "tissue": "brain"
  },
  "input_genes": [
    "FAM111B", "MYBL2", "EXO1", "ZNF367", "BRIP1", "CLSPN", "CHAF1A", "DTL", "PCLAF", "CHEK1", "CDC45", "FANCA", "MCM6", "RRM2", "MCM10", "ASF1B", "CENPU", "FANCD2", "POLA2", "MIR924HG", "CCNE2", "WDR76", "ESCO2", "FBLN7", "CENPK", "NXPH2", "MELK", "CHAF1B", "GRM8", "HELLS", "POLE2", "E2F1", "E2F7", "DHFR", "ABHD3", "CDCA7", "ASPN", "FANCI", "RAD18", "XRCC2", "AC008543.1", "GINS1", "AL034348.1", "BRCA1", "BRCA2", "SPC24", "KIF15", "AC011447.3", "VRK1", "WDHD1", "KIF24", "XYLB", "SKA3", "RAB39A", "LRRC63", "RAD54L", "DIAPH3", "CGAS", "CENPP", "SPC25", "CENPI", "PRIM2", "POLQ", "KBTBD12", "RAD51AP1", "AMPH", "LIG1", "AC007681.1", "MCM5", "AC130324.2", "TNFAIP8", "AURKB", "DDX11-AS1", "SIMC1", "MMS22L", "MCM4", "ATAD2", "FANCB", "DNA2", "AC006115.2", "TRPC3", "PLD5", "PLK4", "LIMK2", "ESPL1", "TP73", "ARNTL2", "ZNF90", "MBNL3", "AC004943.2", "KIAA0319", "COL9A1", "MYBL1", "NEIL3", "WDR62", "SDK1", "LAMA1", "CLN6", "PER3", "PCNA", "CCDC138", "ECM2", "CAMK4", "EFNA5", "CD83", "REXO5", "DDB2", "MCM8", "KIFC1", "CEP152", "IQGAP3", "AC104073.4", "DAPK2", "KNTC1", "ZGRF1", "RFC2", "MND1", "UHRF1", "MBOAT1", "SFMBT1", "RFC3", "CKAP2L", "POLA1", "KCTD16", "ARHGAP11B", "BICC1", "SVEP1", "AP002495.1", "FAM189A1", "SYK", "ORC6", "GHR", "FOXM1", "HMGN2", "ZNF730", "GLYATL2", "ARHGAP19", "HMGB2", "HESX1", "AC009630.1", "STAC", "PBK", "TCF19", "MASTL"
  ],
  "programs": [
    {
      "program_name": "DNA Replication Licensing and Origin Recognition",
      "description": "MCM2-7 complex assembly and licensing of replication origins during G1 phase. CDC45 and GINS1 form the CMG (Cdc45-MCM2-7-GINS) helicase complex required for replication fork progression. ORC6 and RFC proteins coordinate origin licensing and replication factor loading. This program is dysregulated in glioblastoma where origins fire aberrantly during S-phase.",
      "atomic_biological_processes": [
        {
          "name": "Origin licensing complex assembly",
          "citations": [
            {
              "source_id": "45",
              "notes": "CMG helicase structure and MCM2-7 ring assembly at origins"
            },
            {
              "source_id": "48",
              "notes": "Cdc45 association with MCM ring and GINS co-activator for CMG assembly"
            }
          ],
          "genes": ["CDC45", "MCM6", "MCM5", "MCM4", "MCM8", "GINS1", "ORC6"]
        },
        {
          "name": "Replication fork initiation and CMG helicase function",
          "citations": [
            {
              "source_id": "1",
              "notes": "Replication fork pausing differences near origins between normal fibroblasts and glioblastoma cells"
            },
            {
              "source_id": "45",
              "notes": "CMG helicase unwinds parental duplex and organizes replisome"
            }
          ],
          "genes": ["CDC45", "MCM6", "MCM5", "GINS1", "RFC2", "RFC3"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Pre-replication complex and replication origins",
          "citations": [
            {
              "source_id": "27",
              "notes": "CDT1 licensing factor and pre-RC assembly during G1-S transition"
            }
          ],
          "genes": ["ORC6", "MCM6", "MCM5", "MCM4", "MCM8", "RFC2", "RFC3"]
        }
      ],
      "predicted_cellular_impact": [
        "Aberrant firing of replication origins in glioblastoma leading to increased replication stress",
        "Enhanced MCM10-dependent compensatory activation of dormant origins to tolerate replication stress",
        "Temporal alterations in replication timing with early-replicating GC-rich regions showing different kinetics than normal cells"
      ],
      "evidence_summary": "In normal human fibroblasts, replication initiates at multiple early S-phase origins with precise spatiotemporal regulation. Glioblastoma T98G cells show delayed clustering of origins and shorter fork lengths in mid-late S-phase compared to normal fibroblasts, indicating dysregulated replication licensing. MCM2-7 complex components are abundantly expressed in cancer cells, though only ~1/10 are converted to active CMG helicases. MCM10 is highly upregulated in glioblastoma cells and cancer stem cells to compensate for endogenous replication stress by activating dormant replication origins.",
      "significance_score": 0.92,
      "citations": [
        {
          "source_id": "1",
          "notes": "Temporal differences in DNA replication during S-phase between normal human fibroblasts and glioblastoma cells"
        },
        {
          "source_id": "9",
          "notes": "MCM10 compensates for Myc-induced DNA replication stress in cancer stem cells"
        },
        {
          "source_id": "12",
          "notes": "MCM10 as diagnostic and prognostic biomarker elevated in glioblastoma"
        },
        {
          "source_id": "45",
          "notes": "CMG helicase architecture and replication fork progression mechanisms"
        },
        {
          "source_id": "48",
          "notes": "Cdc45 structural determinants for CMG assembly"
        }
      ],
      "supporting_genes": [
        "MCM6", "MCM5", "MCM4", "MCM8", "MCM10", "CDC45", "GINS1", "ORC6", "RFC2", "RFC3"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "CDT1",
          "MCM2",
          "MCM3",
          "MCM7",
          "GINS2",
          "GINS3",
          "GINS4",
          "ORC1",
          "ORC2",
          "ORC3",
          "ORC4",
          "ORC5"
        ],
        "citations": [
          {
            "source_id": "27",
            "notes": "CDT1 licensing factor essential for pre-RC assembly"
          },
          {
            "source_id": "45",
            "notes": "MCM2-7 hexamer and GINS complex required for CMG function"
          }
        ]
      }
    },
    {
      "program_name": "DNA Polymerase Alpha-Primase Priming",
      "description": "Initiation of DNA synthesis through primase complex (POLA1, POLA2, PRIM1, PRIM2) that generates RNA-DNA primers on both leading and lagging strands. The polymerase alpha complex acts at the replication fork initiation site before handoff to processive polymerases (Polδ and Polε). PRIM2 and POLA2 subunits are essential for geminiviral and cellular DNA replication initiation.",
      "atomic_biological_processes": [
        {
          "name": "De novo RNA primer synthesis",
          "citations": [
            {
              "source_id": "38",
              "notes": "PRIM1 and PRIM2 subunits required for initial 7-12 ribonucleotide synthesis for geminiviral and cellular replication"
            }
          ],
          "genes": ["PRIM2", "POLA2", "POLA1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "DNA polymerase alpha-primase holoenzyme",
          "citations": [
            {
              "source_id": "38",
              "notes": "Primase subunits PRIM1 and PRIM2 comprise primase activity within polymerase alpha complex"
            },
            {
              "source_id": "48",
              "notes": "Pol alpha-primase on lagging strand in asymmetric replisome architecture"
            }
          ],
          "genes": ["POLA1", "POLA2", "PRIM2"]
        }
      ],
      "predicted_cellular_impact": [
        "Dysregulated primer synthesis leading to increased lagging strand discontinuities",
        "Accumulation of Okazaki fragment intermediates requiring increased nucleotide metabolism",
        "Potential vulnerability to primase inhibition as therapeutic target in glioblastoma"
      ],
      "evidence_summary": "PRIM1 and PRIM2 are required for initial DNA synthesis initiation, including in viral replication assays. The primase subunits can display activity independently of other polymerase alpha subunits. In the replisome architecture, Pol alpha-primase is positioned on the lagging strand face of the CMG helicase. Glioblastoma cells with elevated nucleotide demands may be particularly dependent on efficient primer synthesis.",
      "significance_score": 0.75,
      "citations": [
        {
          "source_id": "38",
          "notes": "Primase subunits PRIM1 and PRIM2 required for DNA replication initiation"
        },
        {
          "source_id": "48",
          "notes": "Pol alpha-primase architecture in replisome"
        }
      ],
      "supporting_genes": [
        "POLA1", "POLA2", "PRIM2"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "PRIM1"
        ],
        "citations": [
          {
            "source_id": "38",
            "notes": "PRIM1 small subunit essential for primase activity"
          }
        ]
      }
    },
    {
      "program_name": "Leading and Lagging Strand DNA Synthesis",
      "description": "Processive DNA polymerases (POLE2, DNA polymerase delta subunits, PCNA) catalyze bulk DNA synthesis on leading and lagging strands. POLE2 is the catalytic subunit of polymerase epsilon. PCNA serves as the processivity factor and platform for recruitment of replication accessory proteins. Flap processing by DNA2, FEN1, and other nucleases is required for Okazaki fragment maturation.",
      "atomic_biological_processes": [
        {
          "name": "Leading strand DNA synthesis",
          "citations": [
            {
              "source_id": "20",
              "notes": "POLE2 facilitates malignant phenotypes of glioblastoma through AURKA-mediated FOXM1 stability"
            }
          ],
          "genes": ["POLE2", "PCNA", "RFC2", "RFC3", "RRM2"]
        },
        {
          "name": "Lagging strand synthesis and Okazaki fragment processing",
          "citations": [
            {
              "source_id": "39",
              "notes": "DNA2 helicase-endonuclease processes long ssDNA flaps during Okazaki fragment maturation"
            },
            {
              "source_id": "42",
              "notes": "DNA2 nuclease activity promotes EXO1-independent mismatch repair via DNA polymerase delta strand-displacement"
            }
          ],
          "genes": ["DNA2", "EXO1", "PCNA", "POLD2", "LIG1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Replisome polymerase complex",
          "citations": [
            {
              "source_id": "48",
              "notes": "Leading Pol epsilon and lagging Pol alpha-primase on opposite faces of CMG"
            }
          ],
          "genes": ["POLE2", "PCNA"]
        }
      ],
      "predicted_cellular_impact": [
        "POLE2 overexpression enhances glioblastoma proliferation and EMT through AURKA-FOXM1 axis",
        "Increased nucleotide demand from elevated DNA synthesis rates necessitating RRM2 upregulation",
        "Impaired Okazaki fragment maturation when DNA2 is depleted leads to accumulation of ssDNA flaps and DNA damage response activation"
      ],
      "evidence_summary": "POLE2 is highly expressed in glioblastoma and negatively associated with survival. POLE2 knockdown inhibits cell proliferation, colony formation, invasiveness, and sensitivity to chemo/radiation. Mechanistically, POLE2 facilitates AURKA-mediated stabilization of FOXM1, a key proliferation and EMT regulator in glioblastoma. DNA2 processes long ssDNA flaps behind replication forks through coordinated action with Pif1 helicase and DNA polymerase delta. DNA2 depletion generates lethal DNA structures activating the DNA damage response.",
      "significance_score": 0.88,
      "citations": [
        {
          "source_id": "20",
          "notes": "POLE2 promotes GBM proliferation through AURKA-mediated FOXM1 stability"
        },
        {
          "source_id": "23",
          "notes": "POLD2 highly expressed in human glioma and correlates with poor patient survival"
        },
        {
          "source_id": "39",
          "notes": "DNA2 processes flaps behind replication forks and prevents DNA damage response hyper-activation"
        },
        {
          "source_id": "42",
          "notes": "DNA2 nuclease activity in mismatch repair"
        }
      ],
      "supporting_genes": [
        "POLE2", "PCNA", "DNA2", "EXO1", "LIG1", "RRM2"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "POLD1",
          "POLD3",
          "FEN1"
        ],
        "citations": [
          {
            "source_id": "39",
            "notes": "Fen1 processes shorter flaps; DNA2 handles longer flaps"
          }
        ]
      }
    },
    {
      "program_name": "Nucleotide Metabolism and dNTP Synthesis",
      "description": "Ribonucleotide reductase (RRM2) catalyzes conversion of ribonucleotides to deoxyribonucleotides, providing dNTP pools for DNA replication. RRM2 is transcriptionally regulated by BRCA1 in glioblastoma cells and is essential for replication fork progression and protection from replication stress. DHFR provides NADPH cofactor required for RRM2 catalytic function.",
      "atomic_biological_processes": [
        {
          "name": "Deoxyribonucleotide synthesis",
          "citations": [
            {
              "source_id": "7",
              "notes": "BRCA1 acts as transcriptional co-activator of RRM2 to protect glioblastoma from replication stress"
            },
            {
              "source_id": "32",
              "notes": "RRM2 dynamic interaction with IMPDH2 enhances metabolic adaptations underlying glioblastoma chemoresistance"
            }
          ],
          "genes": ["RRM2", "DHFR"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Ribonucleotide reductase complex",
          "citations": [
            {
              "source_id": "7",
              "notes": "RRM2 catalytic subunit requires proper expression levels for fork stability and progression"
            }
          ],
          "genes": ["RRM2", "DHFR"]
        }
      ],
      "predicted_cellular_impact": [
        "BRCA1-mediated RRM2 upregulation protects glioblastoma cells from endogenous replication stress despite genomic instability",
        "Increased dNTP pools enable rapid proliferation and DNA synthesis in glioblastoma",
        "RRM2 expression correlates with higher grade gliomas and shorter survival, marking BRCA1-RRM2 axis as negative prognostic factor",
        "Potential therapeutic vulnerability via RRM2 inhibition to sensitize glioblastoma to replication stress"
      ],
      "evidence_summary": "RRM2 mRNA and protein levels are significantly higher in high-grade gliomas (WHO grade III+IV) compared to low-grade gliomas. BRCA1 functions as a transcriptional co-activator of RRM2 in glioblastoma cells but not in normal cells, establishing this as a tumor-specific regulatory mechanism. BRCA1 is recruited to RRM2 promoter via chromatin immunoprecipitation. BRCA1 knockdown reduces RRM2 protein levels and impairs replication fork stability. Conversely, ectopic RRM2 expression rescues the replication stress phenotype in BRCA1-depleted glioblastoma cells.",
      "significance_score": 0.85,
      "citations": [
        {
          "source_id": "7",
          "notes": "BRCA1-regulated RRM2 protects glioblastoma from replication stress"
        },
        {
          "source_id": "32",
          "notes": "RRM2-IMPDH2 interaction and metabolic adaptation in glioblastoma chemoresistance"
        }
      ],
      "supporting_genes": [
        "RRM2", "DHFR", "BRCA1"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "IMPDH2",
          "RRM1"
        ],
        "citations": [
          {
            "source_id": "32",
            "notes": "RRM2 interacts with IMPDH2 for enhanced metabolic adaptation"
          }
        ]
      }
    },
    {
      "program_name": "DNA Damage Response and Cell Cycle Checkpoints",
      "description": "ATM and ATR kinases detect DNA damage and activate checkpoint kinases CHK1 and CHK2 to halt cell cycle progression. CLSPN (Claspin) mediates ATR-CHK1 signaling. CDC25 phosphatases are inhibited by CHK1/CHK2, preventing CDK dephosphorylation and cell cycle progression. WEE1 kinase maintains CDK inactivation through inhibitory phosphorylation. In glioblastoma, these checkpoint pathways are frequently dysregulated.",
      "atomic_biological_processes": [
        {
          "name": "ATR-CHK1 intra-S checkpoint signaling",
          "citations": [
            {
              "source_id": "2",
              "notes": "ATR-CHK1 pathway activated by single-stranded DNA at stalled replication forks"
            },
            {
              "source_id": "21",
              "notes": "ATR-CHK1 pathway essential for maintaining cell cycle arrest during DNA damage response in glioblastoma stem-like cells"
            },
            {
              "source_id": "28",
              "notes": "MMR proteins MSH2, MSH6, MLH1, PMS2 required for ATR activation after temozolomide treatment"
            }
          ],
          "genes": ["CHEK1", "CLSPN", "RPA"]
        },
        {
          "name": "G2/M checkpoint control",
          "citations": [
            {
              "source_id": "2",
              "notes": "WEE1 and MYT1 maintain CDK1 inactivation through phosphorylation at tyrosine 15 and threonine 14"
            },
            {
              "source_id": "37",
              "notes": "CHK1-mediated WEE1 activation and CDC25c degradation prevents G2/M progression after TMZ-induced DNA damage"
            }
          ],
          "genes": ["CHEK1"]
        },
        {
          "name": "Mismatch repair-dependent ATR activation",
          "citations": [
            {
              "source_id": "28",
              "notes": "MMR pathway processes temozolomide lesions to generate ssDNA that recruits ATR-CHK1 signaling"
            }
          ],
          "genes": ["EXO1", "CHEK1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "RPA-coated single-stranded DNA",
          "citations": [
            {
              "source_id": "2",
              "notes": "RPA-coated ssDNA activates ATR-CHK1 checkpoint"
            }
          ],
          "genes": ["CHEK1", "CLSPN"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced ATR-CHK1 signaling in glioblastoma stem-like cells provides radioresistance through maintained G2 checkpoint",
        "Mismatch repair-dependent ssDNA generation recruits RAD18 for trans-lesion synthesis, enabling temozolomide tolerance",
        "CHK1 inhibition abrogates G2 checkpoint but causes unequal effects in bulk glioblastoma versus stem-like cells",
        "Combined ATR and PARP inhibition maximally radiosensitizes glioblastoma by inhibiting both checkpoint and DNA repair",
        "CHEK2 depletion enhances glioblastoma immunotherapy response via STING-mediated type I interferon activation"
      ],
      "evidence_summary": "ATR-CHK1 checkpoint pathway is preferentially active in glioblastoma stem-like cells compared to bulk tumor, conferring radioresistance. CHK1 inhibition induces DNA double-strand breaks and mitotic catastrophe but shows pronounced effect only in bulk cells. Dual ATR and PARP inhibition achieves maximum radiosensitization. Mismatch repair proteins are required for ATR activation upon temozolomide treatment in MGMT-methylated glioblastomas. CHEK2 depletion paradoxically sensitizes glioblastoma to PD-1 blockade through STING pathway activation and enhanced antigen presentation.",
      "significance_score": 0.89,
      "citations": [
        {
          "source_id": "2",
          "notes": "Cell cycle checkpoints and DNA damage response checkpoint kinases"
        },
        {
          "source_id": "21",
          "notes": "ATR-CHK1 pathway and radioresistance of glioblastoma stem-like cells"
        },
        {
          "source_id": "24",
          "notes": "CHK2 inhibition potentiates anti-tumoral immunotherapy in glioblastoma"
        },
        {
          "source_id": "28",
          "notes": "Mismatch repair and ATR activation in temozolomide response"
        }
      ],
      "supporting_genes": [
        "CHEK1", "CLSPN"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "ATM",
          "ATR",
          "CHK2",
          "WEE1",
          "CDC25A",
          "CDC25C",
          "RPA1",
          "RPA2",
          "RPA3"
        ],
        "citations": [
          {
            "source_id": "2",
            "notes": "ATM, ATR, WEE1, CDC25 required for checkpoint control"
          }
        ]
      }
    },
    {
      "program_name": "Homologous Recombination DNA Repair",
      "description": "High-fidelity double-strand break repair through homologous recombination mediated by BRCA1, BRCA2, RAD51, and accessory factors including BRIP1 (FANCJ), FANCI, FANCD2, XRCC2, MND1, RAD54L. RAD51 catalyzes strand invasion and homology searching. Fanconi anemia proteins coordinate RAD51 loading. This pathway is restricted to S and G2 phases when sister chromatids are available as repair templates.",
      "atomic_biological_processes": [
        {
          "name": "RAD51 filament formation and homology searching",
          "citations": [
            {
              "source_id": "3",
              "notes": "HR pathway requires homologous DNA sequence template for high-fidelity DSB repair"
            },
            {
              "source_id": "6",
              "notes": "RAD51, ATM, ATR, and Fanconi anemia factors mediate temozolomide sensitivity in gliomas"
            }
          ],
          "genes": ["BRCA1", "BRCA2", "RAD51AP1", "XRCC2"]
        },
        {
          "name": "Fanconi anemia pathway coordination",
          "citations": [
            {
              "source_id": "6",
              "notes": "Homologous recombination repair molecules including RAD51, ATM, ATR implicated in temozolomide resistance"
            },
            {
              "source_id": "10",
              "notes": "BRCC3 interacts with BRCA1 to trigger BRCA-associated DNA repair pathway; BRCA1, BRCA2, RAD51 required for HR in gliomas"
            },
            {
              "source_id": "11",
              "notes": "FANCD2 re-expression in glioblastoma associated with glioma grade"
            }
          ],
          "genes": ["FANCA", "FANCB", "FANCI", "FANCD2", "BRIP1"]
        },
        {
          "name": "DNA end-resection and 3' single-stranded DNA tail generation",
          "citations": [
            {
              "source_id": "3",
              "notes": "EXO1 or BLM/DNA2 mediates extensive resection to produce 3' ssDNA overhangs"
            },
            {
              "source_id": "44",
              "notes": "HELLS chromatin remodeller promotes end-resection and RAD51 foci formation for HR during G2"
            }
          ],
          "genes": ["EXO1", "DNA2", "HELLS", "MND1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "RAD51 nucleoprotein filament",
          "citations": [
            {
              "source_id": "3",
              "notes": "RAD51 nucleofilament mediates homology searching and strand invasion after BRCA2-mediated RPA replacement"
            }
          ],
          "genes": ["BRCA1", "BRCA2", "RAD51AP1"]
        },
        {
          "name": "Fanconi anemia complex",
          "citations": [
            {
              "source_id": "33",
              "notes": "Multiple Fanconi anemia genes mutated across cancer types with tissue-specific patterns"
            }
          ],
          "genes": ["FANCA", "FANCB", "FANCI", "FANCD2"]
        }
      ],
      "predicted_cellular_impact": [
        "HR pathway overexpression in glioblastoma enables survival despite high levels of endogenous and therapy-induced DNA damage",
        "BRCA1-mediated RRM2 upregulation and HR gene expression collectively protect glioblastoma from temozolomide-induced cytotoxicity",
        "Fanconi anemia gene re-expression (FANCD2) in glioblastoma compared to normal brain suggests tumor-specific HR dependence",
        "IDH-mutant gliomas exhibit 'BRCAness' phenotype with impaired HR but enhanced sensitivity to PARP and ATR inhibitors",
        "BRCA1 abrogation impairs glioblastoma tumorigenicity and enhances radiosensitivity through combined replication stress and HR deficiency"
      ],
      "evidence_summary": "Glioblastoma cells with higher BRCA1 expression show shorter survival, identifying BRCA1 as a negative prognostic factor. BRCA1 simultaneously protects replication fork stability via RRM2 regulation and enables HR-mediated double-strand break repair. BRCA1 depletion impairs tumorigenicity in xenograft models. FANCD2 is re-expressed in high-grade gliomas compared to normal brain and benign schwannomas, suggesting tumor-specific reliance on Fanconi anemia pathway. Treatment with temozolomide induces upregulation of BRCC3, BRCA1, BRCA2, RAD51, and FANCD2 in resistant glioblastoma lines. IDH-mutant gliomas exhibit impaired HR from enhanced oncometabolites but respond well to PARP and ATR inhibitors.",
      "significance_score": 0.91,
      "citations": [
        {
          "source_id": "6",
          "notes": "Homologous recombination repair and temozolomide chemosensitivity in gliomas"
        },
        {
          "source_id": "7",
          "notes": "BRCA1-RRM2 axis protects glioblastoma from replication stress and supports tumorigenicity"
        },
        {
          "source_id": "10",
          "notes": "BRCC3 and HR-dependent DNA repair genes upregulated in TMZ-treated glioma cells"
        },
        {
          "source_id": "11",
          "notes": "FANCD2 re-expression associated with glioma grade"
        }
      ],
      "supporting_genes": [
        "BRCA1", "BRCA2", "RAD51AP1", "XRCC2", "FANCA", "FANCB", "FANCI", "FANCD2", "BRIP1", "EXO1", "DNA2", "HELLS", "MND1", "MND1"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "RAD51",
          "CtIP",
          "MRE11",
          "RAD50",
          "NBS1",
          "BLM",
          "RPA1",
          "RPA2",
          "RPA3"
        ],
        "citations": [
          {
            "source_id": "3",
            "notes": "RAD51, MRN complex, and RPA essential for HR pathway"
          }
        ]
      }
    },
    {
      "program_name": "Fanconi Anemia Pathway and Interstrand Crosslink Repair",
      "description": "Fanconi anemia (FA) proteins coordinate repair of interstrand crosslinks (ICLs) and other DNA lesions through formation of the FA core complex, monoubiquitination of FANCD2 and FANCI, and recruitment of structure-specific nucleases. The pathway intersects with homologous recombination and translesion synthesis. FANCD2 re-expression in glioblastoma compared to normal brain is associated with higher tumor grade.",
      "atomic_biological_processes": [
        {
          "name": "Fanconi anemia core complex assembly and FANCD2 monoubiquitination",
          "citations": [
            {
              "source_id": "8",
              "notes": "FANCD2 key protein of Fanconi Anaemia DNA repair pathway re-expressed in glioblastoma"
            },
            {
              "source_id": "11",
              "notes": "FA pathway confers glioma resistance to DNA alkylating agents"
            }
          ],
          "genes": ["FANCA", "FANCB", "FANCI", "FANCD2"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Fanconi anemia core complex",
          "citations": [
            {
              "source_id": "33",
              "notes": "Multiple Fanconi anemia complex proteins including FANCA, FANCB, FANCI, FANCD2 identified"
            }
          ],
          "genes": ["FANCA", "FANCB", "FANCI", "FANCD2"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced FA pathway activity in glioblastoma provides resistance to DNA alkylating agents including temozolomide",
        "FANCD2 re-expression distinguishes high-grade from low-grade gliomas, suggesting tumor-grade-dependent activation",
        "Targeting FA pathway components may sensitize alkylating agent-resistant glioblastoma",
        "FA pathway synergizes with HR pathway to enable glioblastoma survival under replication stress"
      ],
      "evidence_summary": "Glioblastoma cells exhibit re-expression of FANCD2 compared to normal brain tissue and benign schwannomas. This re-expression is associated with glioma grade, suggesting a tumor-promoting function. The FA pathway confers glioma resistance to DNA alkylating agents. FANCD2 levels increase in malignant glioma cells and are higher in resistant cell lines. FA pathway components are coordinately upregulated with HR genes following temozolomide treatment.",
      "significance_score": 0.78,
      "citations": [
        {
          "source_id": "8",
          "notes": "FANCD2 re-expression in glioblastoma associated with glioma grade and grade-related resistance"
        },
        {
          "source_id": "11",
          "notes": "Fanconi anemia pathway confers glioma resistance to DNA alkylating agents"
        }
      ],
      "supporting_genes": [
        "FANCA", "FANCB", "FANCI", "FANCD2"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "FANCC",
          "FANCE",
          "FANCF",
          "FANCG",
          "FANCL",
          "SLX4",
          "ERCC4",
          "BLM",
          "BRCA2",
          "PALB2"
        ],
        "citations": [
          {
            "source_id": "33",
            "notes": "Multiple Fanconi anemia complex members required for pathway function"
          }
        ]
      }
    },
    {
      "program_name": "Trans-Lesion Synthesis and Post-Replication Repair",
      "description": "Error-prone DNA polymerases (Polη, Polι, Polκ, REV1) specialized for bypass of DNA lesions through trans-lesion synthesis (TLS). RAD18-mediated monoubiquitination of PCNA recruits Y-family polymerases to damaged sites. Mismatch repair (MMR) processing of temozolomide lesions generates ssDNA gaps filled by TLS. This mechanism enables glioblastoma tolerance of temozolomide genotoxicity.",
      "atomic_biological_processes": [
        {
          "name": "RAD18-mediated PCNA monoubiquitination and TLS polymerase recruitment",
          "citations": [
            {
              "source_id": "4",
              "notes": "RAD18 activated in mismatch repair-dependent manner to promote post-replicative gap-filling and survival in TMZ-treated glioblastoma"
            },
            {
              "source_id": "25",
              "notes": "RAD18 E3 ubiquitin ligase monoubiquitinates PCNA K164 to recruit error-prone TLS polymerases"
            }
          ],
          "genes": ["RAD18", "PCNA"]
        },
        {
          "name": "Mismatch repair processing of O6-methylguanine lesions",
          "citations": [
            {
              "source_id": "4",
              "notes": "MMR-mediated futile cycles generate ssDNA gaps that recruit RAD18 for post-replication repair"
            },
            {
              "source_id": "25",
              "notes": "MMR proteins recognize O6mG:T mismatches; EXO1 excision generates ssDNA gaps"
            },
            {
              "source_id": "28",
              "notes": "MMR pathway processes TMZ lesions to generate ssDNA for ATR-CHK1 and RAD18 recruitment"
            }
          ],
          "genes": ["EXO1", "RAD18"]
        },
        {
          "name": "Error-free bypass of O6-methylguanine lesions",
          "citations": [
            {
              "source_id": "4",
              "notes": "RAD18 promotes error-free bypass of O6mG (most toxic TMZ lesion) and error-prone bypass of other lesions"
            },
            {
              "source_id": "25",
              "notes": "RAD18 suppresses mutagenicity of TMZ-induced O6mG lesions while allowing tolerance of other lesions"
            }
          ],
          "genes": ["RAD18", "POLQ"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "PCNA monoubiquitination and TLS polymerase switch",
          "citations": [
            {
              "source_id": "4",
              "notes": "RAD18-PCNA mono-ubiquitination forms 'TLS polymerase switch' activating post-replicative repair synthesis"
            }
          ],
          "genes": ["RAD18", "PCNA", "POLQ"]
        }
      ],
      "predicted_cellular_impact": [
        "RAD18-dependent TLS enables glioblastoma tolerance of temozolomide-induced DNA damage",
        "Error-free bypass of O6-methylguanine through RAD18 reduces temozolomide-induced mutagenesis",
        "RAD18 expression correlates inversely with hypermutation in recurrent glioblastoma patient samples",
        "Mismatch repair-mediated ssDNA generation simultaneously activates ATR-CHK1 checkpoint and RAD18-TLS pathway for dual damage tolerance",
        "RAD18 inhibition combined with temozolomide or MMR pathway targeting may overcome glioblastoma chemoresistance",
        "Low RAD18 expression in recurrent gliomas associates with hypermutation phenotype from unrepaired lesions"
      ],
      "evidence_summary": "RAD18 is activated in mismatch repair-dependent manner in temozolomide-treated MGMT-deficient glioblastoma cells. RAD18 mono-ubiquitinates PCNA at damaged DNA sites, recruiting Y-family polymerases for gap-filling. Analysis of mutation signatures shows RAD18 suppresses COSMIC signature 11 (temozolomide signature) by promoting error-free repair of O6-methylguanine. In MGMT-expressing cells with lower O6-methylguanine accumulation, RAD18 still enables TLS through error-prone polymerases for other lesions. RAD18-deficient cells accumulate persistent ssDNA and DSBs when treated with temozolomide. Clinical analysis of recurrent glioblastoma reveals correlation between low RAD18 expression and hypermutation phenotype.",
      "significance_score": 0.87,
      "citations": [
        {
          "source_id": "4",
          "notes": "RAD18 and trans-lesion synthesis pathway crosstalk with mismatch repair in temozolomide-treated glioblastoma"
        },
        {
          "source_id": "25",
          "notes": "Trans-lesion synthesis and mismatch repair pathway crosstalk with multi-pathway mechanisms of DNA damage tolerance"
        }
      ],
      "supporting_genes": [
        "RAD18", "PCNA", "EXO1", "POLQ"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "POLH",
          "POLI",
          "POLK",
          "REV1",
          "MSH2",
          "MSH6",
          "MLH1",
          "PMS2",
          "POLD1",
          "POLD3"
        ],
        "citations": [
          {
            "source_id": "4",
            "notes": "Y-family polymerases and MMR proteins required for TLS pathway"
          },
          {
            "source_id": "25",
            "notes": "Y-family polymerases recruited by monoubiquitinated PCNA"
          }
        ]
      }
    },
    {
      "program_name": "G1/S Cell Cycle Checkpoint and E2F-Dependent Proliferation",
      "description": "E2F transcription factors (E2F1, E2F7) regulate S-phase entry through cyclin E-CDK2 complex-mediated hyperphosphorylation of retinoblastoma (RB) protein. MYBL2 (B-Myb) and E2F7/E2F8 drive G2/M genes for continued proliferation. CCNE2 (Cyclin E2) and cell cycle checkpoint regulators coordinate G1/S transition. Elevated E2F and cyclin expression drives aggressive glioblastoma proliferation.",
      "atomic_biological_processes": [
        {
          "name": "RB phosphorylation and E2F activation at G1/S transition",
          "citations": [
            {
              "source_id": "40",
              "notes": "Cyclin E-CDK2 complex drives RB hyperphosphorylation at G1/S transition to activate E2F transcription factors"
            }
          ],
          "genes": ["E2F1", "CCNE2"]
        },
        {
          "name": "E2F7-mediated proliferation and EMT",
          "citations": [
            {
              "source_id": "13",
              "notes": "E2F7 promotes cell proliferation, cell-cycle progression, and cell metastasis in glioblastoma via EZH2-mediated PTEN/AKT/mTOR pathway"
            },
            {
              "source_id": "16",
              "notes": "E2F7 and E2F8 highly correlated with cell cycle oncogenes and aggressive proliferation; E2F7 regulates radioresistance via EZH2"
            }
          ],
          "genes": ["E2F7", "FOXM1"]
        },
        {
          "name": "MYBL2-driven G2/M transition",
          "citations": [
            {
              "source_id": "43",
              "notes": "MYBL2 (B-Myb) transcription factor regulates cell cycle progression and directly activates G2/M genes including cyclin B1 and CDK1"
            },
            {
              "source_id": "37",
              "notes": "MYBL2 repression and B-Myb-mediated cell cycle arrest occurs following TMZ-induced senescence"
            }
          ],
          "genes": ["MYBL2"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "E2F-DP transcription factor complex",
          "citations": [
            {
              "source_id": "2",
              "notes": "RB binds and inhibits E2F-DP complexes in G0; CDK-mediated RB hyperphosphorylation releases E2F"
            }
          ],
          "genes": ["E2F1", "E2F7"]
        }
      ],
      "predicted_cellular_impact": [
        "E2F7 overexpression drives glioblastoma proliferation and predicts poor radiotherapy response",
        "E2F7-EZH2 axis activates AKT/mTOR signaling to promote cell proliferation and EMT",
        "MYBL2 upregulation in glioblastoma enables continuous cell cycle progression through coordinated G1/S and G2/M regulation",
        "High E2F7 expression correlates with epithelial-mesenchymal transition markers and tumor invasiveness",
        "E2F7 silencing enhances radiosensitivity through reduced EZH2-mediated radioresistance"
      ],
      "evidence_summary": "E2F7 is upregulated in glioblastoma patients and high expression associates with poor overall survival. E2F7 promotes cell proliferation and cell-cycle progression through regulation of cyclin D1 and CDK4 expression. E2F7 drives epithelial-mesenchymal transition via triggering of EMT process. E2F7 directly binds to EZH2 promoter and activates its transcription, which in turn inhibits PTEN and activates AKT/mTOR signaling. Silencing E2F7 reduces proliferation and enhances radiosensitivity. E2F7 and E2F8 are highly enriched in epithelial-mesenchymal transition gene signatures and show associations with multiple cancer-promoting pathways including NFκB, STAT3, angiogenesis, and glycolysis.",
      "significance_score": 0.90,
      "citations": [
        {
          "source_id": "13",
          "notes": "E2F7-EZH2 axis regulates PTEN/AKT/mTOR signaling to promote glioblastoma proliferation and metastasis"
        },
        {
          "source_id": "16",
          "notes": "E2F7 as regulator of radioresistance in high-grade gliomas via EZH2 regulation"
        },
        {
          "source_id": "40",
          "notes": "Cyclin-CDK complexes and RB phosphorylation in G1/S transition"
        },
        {
          "source_id": "43",
          "notes": "MYBL2 transcription factor regulation of cell cycle progression"
        }
      ],
      "supporting_genes": [
        "E2F1", "E2F7", "CCNE2", "MYBL2", "FOXM1"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "CCND1",
          "CDK4",
          "CDK6",
          "CDK2",
          "RB1",
          "E2F4",
          "E2F5",
          "DP1",
          "EZH2",
          "PTEN"
        ],
        "citations": [
          {
            "source_id": "13",
            "notes": "EZH2 and PTEN as downstream targets of E2F7"
          },
          {
            "source_id": "40",
            "notes": "Cyclin D and CDK4/6 in G1 phase; RB as E2F target"
          }
        ]
      }
    },
    {
      "program_name": "FOXM1-ADAM17 Feedback Loop and Epithelial-Mesenchymal Transition",
      "description": "FOXM1 is a proliferation-specific transcription factor driving glioblastoma progression through regulation of cell cycle genes, EMT factors, and ADAM17 (a sheddase for EGFR ligands). FOXM1-ADAM17 axis activates EGFR/AKT/GSK3β signaling, which in turn stabilizes FOXM1 through the feedback loop. FoxM1 also regulates VEGF expression for angiogenesis and promotes invasion through TGF-β signaling modulation.",
      "atomic_biological_processes": [
        {
          "name": "FOXM1 transcriptional activation of proliferation genes",
          "citations": [
            {
              "source_id": "15",
              "notes": "FoxM1 drives ADAM17/EGFR activation loop to promote mesenchymal transition in glioblastoma"
            },
            {
              "source_id": "18",
              "notes": "FoxM1 plays critical role in GBM development through regulation of cell proliferation and cell cycle transition"
            }
          ],
          "genes": ["FOXM1", "MYBL2"]
        },
        {
          "name": "FOXM1-mediated EMT through ADAM17-EGFR axis",
          "citations": [
            {
              "source_id": "15",
              "notes": "FoxM1 binds to ADAM17 promoter to transcriptionally upregulate its expression; ADAM17/EGFR axis promotes mesenchymal transition"
            }
          ],
          "genes": ["FOXM1"]
        },
        {
          "name": "EGFR-AKT-GSK3β signaling and FOXM1 stabilization",
          "citations": [
            {
              "source_id": "15",
              "notes": "FOXM1/ADAM17 axis activates EGFR/AKT/GSK3β pathway; EGFR signaling stabilizes FOXM1 protein expression"
            },
            {
              "source_id": "18",
              "notes": "FoxM1 regulates NEDD4-1 upregulation which promotes PTEN ubiquitination and Akt activation"
            }
          ],
          "genes": ["FOXM1"]
        },
        {
          "name": "FOXM1-mediated angiogenesis",
          "citations": [
            {
              "source_id": "18",
              "notes": "FoxM1 overexpression is key event in driving angiogenesis in glioma formation; control over VEGF transcription plays important functional role"
            }
          ],
          "genes": ["FOXM1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "ADAM17 sheddase complex",
          "citations": [
            {
              "source_id": "15",
              "notes": "ADAM17 sheds EGFR ligands; FOXM1 transcriptionally upregulates ADAM17"
            }
          ],
          "genes": ["FOXM1"]
        },
        {
          "name": "EGFR signaling complex",
          "citations": [
            {
              "source_id": "15",
              "notes": "ADAM17-released EGFR ligands activate EGFR receptor; downstream PI3K/AKT and MAPK activation"
            }
          ],
          "genes": ["FOXM1"]
        }
      ],
      "predicted_cellular_impact": [
        "FOXM1 expression drives glioblastoma proliferation, invasion, and mesenchymal differentiation",
        "FOXM1-ADAM17-EGFR feedback loop establishes self-sustaining proliferation and EMT program",
        "High FOXM1 levels correlate with shorter survival and increased tumor invasiveness",
        "FOXM1-mediated VEGF upregulation promotes angiogenesis enabling nutrient delivery for tumor growth",
        "FOXM1 modulation of TGF-β signaling through interaction with SMAD3/4 enhances EMT",
        "FOXM1 contributes to temozolomide and radiotherapy resistance through EMT-associated mechanisms"
      ],
      "evidence_summary": "FOXM1 expression is elevated in glioblastoma patients and associated with shorter overall survival. FOXM1 expression positively correlates with ADAM17 expression, and both are correlated with mesenchymal features and poor survival. Overexpression of either FOXM1 or ADAM17 increases glioma cell mesenchymal phenotype. FOXM1 directly binds to the ADAM17 promoter to transcriptionally upregulate its expression. FOXM1-ADAM17 axis activates EGFR/AKT/GSK3β signaling pathway. The resulting AKT/GSK3β activation stabilizes FOXM1 protein through prevention of GSK3β-mediated degradation. FOXM1 controls Wnt/β-catenin signaling through β-catenin nuclear translocation. FoxM1 regulates VEGF expression, which is essential for angiogenesis in glioblastoma.",
      "significance_score": 0.88,
      "citations": [
        {
          "source_id": "15",
          "notes": "FoxM1 drives ADAM17/EGFR activation loop to promote mesenchymal transition in glioblastoma"
        },
        {
          "source_id": "18",
          "notes": "FoxM1 plays critical role in GBM formation and progression through regulation of proliferation, EMT, invasion, and angiogenesis"
        }
      ],
      "supporting_genes": [
        "FOXM1", "MYBL2"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "ADAM17",
          "EGFR",
          "VEGF",
          "SMAD3",
          "SMAD4",
          "GSK3B",
          "AKT1",
          "CTNNB1",
          "TCF4",
          "NEDD4"
        ],
        "citations": [
          {
            "source_id": "15",
            "notes": "ADAM17, EGFR, and downstream signaling partners required for FOXM1 feedback loop"
          },
          {
            "source_id": "18",
            "notes": "VEGF, SMAD proteins, and other factors regulated by FOXM1"
          }
        ]
      }
    },
    {
      "program_name": "Centrosome Organization and Centriole Duplication",
      "description": "Polo-like kinase 4 (PLK4) is the master regulator of centriole duplication through phosphorylation of STIL. Centrosome proteins (SPC24, SPC25, CENPU, CENPK, CENPI, CENPP) organize the pericentriolar material. CEP152 recruits PLK4 to centrosomes. Proper centrosome duplication is essential for bipolar spindle formation. Overexpression of PLK4 causes centrosome amplification, chromosomal instability, and tumor formation.",
      "atomic_biological_processes": [
        {
          "name": "Polo-like kinase 4 regulation of centriole duplication",
          "citations": [
            {
              "source_id": "56",
              "notes": "PLK4 plays key role in initiating centriole duplication; overexpression promotes centriole overduplication and centrosome amplification"
            },
            {
              "source_id": "59",
              "notes": "PLK4 is master regulator of centriole duplication; regulated by CRL4DCAF1 ubiquitin ligase in G2 phase"
            }
          ],
          "genes": ["PLK4", "CEP152"]
        },
        {
          "name": "Centrosome protein assembly and function",
          "citations": [
            {
              "source_id": "19",
              "notes": "CENP-A regulates centromere protein assembly and essential for chromosome segregation during mitosis and cell division"
            }
          ],
          "genes": ["SPC24", "SPC25", "CENPU", "CENPK", "CENPI", "CENPP"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Centrosome containing centriole pair and pericentriolar material",
          "citations": [
            {
              "source_id": "56",
              "notes": "Centrosomes comprised of pair of centrioles surrounded by amorphous pericentriolar material"
            },
            {
              "source_id": "59",
              "notes": "Centrosome consists of paired centrioles; PLK4 required for centriole duplication exactly once per cell cycle"
            }
          ],
          "genes": ["PLK4", "CEP152", "SPC24", "SPC25"]
        }
      ],
      "predicted_cellular_impact": [
        "PLK4 overexpression in glioblastoma may cause centrosome amplification and chromosomal instability",
        "Centrosome amplification leads to errors in spindle formation and chromosome missegregation during mitosis",
        "Supernumerary centrosomes contribute to aneuploidy characteristic of glioblastoma",
        "Enhanced centrosome nucleation in glioblastoma may support rapid proliferation and migration",
        "CRL4DCAF1-mediated PLK4 degradation in G2 is therapeutic target to prevent mitotic defects"
      ],
      "evidence_summary": "PLK4 kinase activity is inherently unstable through autoregulation via autophosphorylation of a 24-amino acid phosphodegron. Multiple phosphorylation sites are required for PLK4 instability, establishing threshold-based regulation. PLK4 overexpression promotes centriole overduplication and formation of extra centrosomes. CRL4DCAF1 ubiquitin ligase complex regulates PLK4 protein levels through ubiquitination in G2 phase of cell cycle to prevent premature centriole duplication. PLK4 overexpression is sufficient to induce tumor formation in mice through centrosome amplification and chromosome missegregation.",
      "significance_score": 0.76,
      "citations": [
        {
          "source_id": "56",
          "notes": "PLK4 autoregulation of kinase activity and centrosome overduplication"
        },
        {
          "source_id": "59",
          "notes": "PLK4 regulation by CRL4DCAF1 ubiquitin ligase and centriole duplication control"
        }
      ],
      "supporting_genes": [
        "PLK4", "CEP152", "SPC24", "SPC25", "CENPU", "CENPK", "CENPI", "CENPP"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "STIL",
          "DSLD1",
          "SCL/TAL1 interrupting locus",
          "DCAF1"
        ],
        "citations": [
          {
            "source_id": "59",
            "notes": "STIL and DCAF1 required for PLK4 function and regulation"
          }
        ]
      }
    },
    {
      "program_name": "Centromeric and Kinetochore Function",
      "description": "Centromeric protein CENP-A (centromeric histone H3 variant) maintains centromere identity and is essential for chromosome segregation during mitosis. Overexpression of CENP-A causes ectopic deposition and chromosomal instability. Kinetochore proteins including SPC24, SPC25, SKA3, and KNTC1 coordinate spindle attachment and checkpoint control. High CENP-A expression predicts poor prognosis in gliomas.",
      "atomic_biological_processes": [
        {
          "name": "Centromere protein CENP-A-mediated centromere identity",
          "citations": [
            {
              "source_id": "19",
              "notes": "CENP-A regulates centromere integrity and chromosome segregation; overexpression leads to ectopic CENP-A deposition and chromosomal instability"
            }
          ],
          "genes": ["CENPU", "CENPK", "CENPI", "CENPP"]
        },
        {
          "name": "Kinetochore assembly and spindle checkpoint control",
          "citations": [
            {
              "source_id": "19",
              "notes": "Centromeric factors increasingly shown to be involved in tumor pathogenesis; CENP-A and kinetochore proteins associated with chromosomal instability"
            }
          ],
          "genes": ["SPC24", "SPC25", "SKA3", "KNTC1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Centromere chromatin containing CENP-A nucleosomes",
          "citations": [
            {
              "source_id": "19",
              "notes": "CENP-A enriched at active centromeres and serves as epigenetic mark of centromere identity"
            }
          ],
          "genes": ["CENPU", "CENPK", "CENPI", "CENPP"]
        },
        {
          "name": "Kinetochore structure",
          "citations": [
            {
              "source_id": "19",
              "notes": "Kinetochore proteins coordinate spindle attachment and chromosome segregation"
            }
          ],
          "genes": ["SPC24", "SPC25", "SKA3", "KNTC1"]
        }
      ],
      "predicted_cellular_impact": [
        "High CENP-A expression in glioblastoma correlates with worse prognosis and higher tumor grade",
        "CENP-A overexpression causes ectopic centrosome formation and chromosomal instability",
        "Aneuploidy from CENP-A mislocalization contributes to glioblastoma genomic instability and tumor evolution",
        "Kinetochore dysfunction from dysregulated CENP-A impairs spindle checkpoint and promotes mitotic errors",
        "CENP-A-induced aneuploidy may increase mutational burden and immunogenicity in glioblastoma"
      ],
      "evidence_summary": "CENP-A is significantly upregulated in high-grade gliomas (WHO grade III+IV) compared to low-grade gliomas. High CENP-A expression is associated with worse overall survival in glioma patients. CENP-A is independently prognostic for overall survival in multivariate analysis. CENP-A is correlated with high tumor grade, wild-type IDH, and absence of 1p/19q co-deletion. GSEA analysis shows enrichment of cell cycle, chromosome segregation, G2M checkpoint, and apoptosis pathways in high CENP-A phenotype. Genomic instability and aneuploidy from CENP-A mislocalization contribute to poor prognosis.",
      "significance_score": 0.82,
      "citations": [
        {
          "source_id": "19",
          "notes": "CENP-A as prognostic biomarker and driver of chromosomal instability in gliomas"
        }
      ],
      "supporting_genes": [
        "CENPU", "CENPK", "CENPI", "CENPP", "SPC24", "SPC25", "SKA3", "KNTC1"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "CENPC",
          "CENPW",
          "CENPH",
          "CENPJ",
          "CENPF",
          "BUB1",
          "MAD2L1"
        ],
        "citations": [
          {
            "source_id": "19",
            "notes": "Multiple centromeric and kinetochore proteins required for chromosome segregation"
          }
        ]
      }
    },
    {
      "program_name": "Chromatin Remodeling and Histone Chaperones",
      "description": "ASF1B (anti-silencing function 1B) is a histone chaperone involved in histone H3/H4 deposition and nucleosome assembly during DNA replication. HELLS (helicase, lymphoid-specific) is a SNF2-like chromatin remodeller promoting DNA end-resection and homologous recombination during G2 phase. Chromatin remodellers including DTL, CHAF1A, CHAF1B coordinate chromatin dynamics during replication and DNA repair.",
      "atomic_biological_processes": [
        {
          "name": "Histone H3/H4 deposition and chromatin assembly",
          "citations": [
            {
              "source_id": "55",
              "notes": "ASF1B high expression correlated with poor prognosis in glioma patients; involved in cell proliferation regulation"
            }
          ],
          "genes": ["ASF1B", "CHAF1A", "CHAF1B"]
        },
        {
          "name": "Chromatin remodeling during DNA repair",
          "citations": [
            {
              "source_id": "44",
              "notes": "HELLS chromatin remodeller facilitates DNA end-resection and RAD51 foci formation for homologous recombination during G2"
            }
          ],
          "genes": ["HELLS", "ATAD2"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Nucleosome and chromatin fiber",
          "citations": [
            {
              "source_id": "55",
              "notes": "ASF1B involved in nucleosome assembly and chromatin dynamics during cell proliferation"
            }
          ],
          "genes": ["ASF1B", "CHAF1A", "CHAF1B"]
        },
        {
          "name": "Heterochromatin structure",
          "citations": [
            {
              "source_id": "44",
              "notes": "HELLS required for efficient repair of double-strand breaks within heterochromatic regions of genome"
            }
          ],
          "genes": ["HELLS"]
        }
      ],
      "predicted_cellular_impact": [
        "High ASF1B expression in glioblastoma enables rapid DNA synthesis and proliferation through efficient histone deposition",
        "ASF1B expression predicts poor prognosis and correlates with high-grade glioma and wild-type IDH status",
        "HELLS-mediated chromatin remodeling facilitates efficient DNA repair in heterochromatin during glioblastoma growth",
        "Chromatin remodelers coordinate replication fork progression with chromatin dynamics in replicating glioblastoma cells",
        "Targeting ASF1B or HELLS may impair glioblastoma proliferation and sensitize to DNA-damaging therapy"
      ],
      "evidence_summary": "ASF1B belongs to the histone chaperone H3/H4 family and is mainly involved in regulation of cell proliferation. High ASF1B expression is considerably higher in glioma tissues than in normal tissues. Increased ASF1B expression is linked with poor prognosis and high WHO grade in glioma patients. ASF1B is an independent predictive factor for overall survival. HELLS facilitates DNA end-resection required for homologous recombination by promoting CtIP accumulation at DSB sites. HELLS-depleted cells show persistent γ-H2AX foci after ionizing radiation, indicating impaired DSB repair. HELLS is particularly required for repair of breaks in heterochromatic regions.",
      "significance_score": 0.80,
      "citations": [
        {
          "source_id": "44",
          "notes": "HELLS chromatin remodeller promotes homologous recombination and end-resection"
        },
        {
          "source_id": "55",
          "notes": "ASF1B high expression and poor prognosis in gliomas"
        }
      ],
      "supporting_genes": [
        "ASF1B", "HELLS", "CHAF1A", "CHAF1B", "ATAD2", "DTL"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "CHD3",
          "SMARCA5",
          "ACF1",
          "SNF2H"
        ],
        "citations": [
          {
            "source_id": "44",
            "notes": "Multiple chromatin remodellers coordinate DNA repair in different chromatin contexts"
          }
        ]
      }
    },
    {
      "program_name": "Sister Chromatid Cohesion and Separation",
      "description": "Cohesin complex maintains sister chromatid cohesion from S phase through metaphase. Separase (ESPL1) cleaves cohesin at anaphase onset to allow chromatid separation. Securin regulates separase until metaphase-anaphase transition when APC/C-mediated degradation releases separase. Proper cohesion/separation is essential for error-free chromosome segregation.",
      "atomic_biological_processes": [
        {
          "name": "Cohesin-mediated sister chromatid cohesion",
          "citations": [
            {
              "source_id": "57",
              "notes": "Separase (ESPL1) triggers cleavage of Scc1/Rad21 cohesin subunit to inactivate complex at anaphase"
            }
          ],
          "genes": ["ESPL1"]
        },
        {
          "name": "Securin-mediated separase inhibition until metaphase-anaphase transition",
          "citations": [
            {
              "source_id": "57",
              "notes": "Securin forms complex with separase to arrest cell cycle at metaphase; ubiquitin-dependent degradation by APC/C releases separase"
            }
          ],
          "genes": ["ESPL1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Cohesin protein complex",
          "citations": [
            {
              "source_id": "57",
              "notes": "Cohesin complex comprised of multiple proteins including SMC3, SMC1A, RAD21, STAG proteins"
            }
          ],
          "genes": ["ESPL1"]
        }
      ],
      "predicted_cellular_impact": [
        "Aberrant separase expression in glioblastoma leads to errors in sister chromatid separation",
        "Dysregulated cohesin-separase interactions contribute to chromosome missegregation and aneuploidy",
        "Abnormal separase regulation may facilitate rapid cell division in glioblastoma",
        "Separase-securin-cyclin B1 dysregulation in glioblastoma suggests therapeutic vulnerability"
      ],
      "evidence_summary": "Separase is tightly regulated by complex inhibitory interactions with securin and cyclin B1. Uncontrolled separase activity leads to uncontrolled and premature sister chromatid segregation, impairing genetic inheritance. In normal cells, mitotic separase co-expresses with cyclin B1 but not securin, consistent with proper separase-dependent cell cycle control. Aberrant expression patterns in cancer cells suggest dysregulated cohesin-separase interactions.",
      "significance_score": 0.68,
      "citations": [
        {
          "source_id": "57",
          "notes": "Separase regulation by securin and cyclin B1 in mitotic cell cycle control"
        }
      ],
      "supporting_genes": [
        "ESPL1"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "RAD21",
          "STAG1",
          "STAG2",
          "SMC1A",
          "SMC3",
          "SECURIN",
          "CCNB1",
          "APC/C"
        ],
        "citations": [
          {
            "source_id": "57",
            "notes": "Cohesin and securin proteins required for separase regulation"
          }
        ]
      }
    },
    {
      "program_name": "Aurora Kinase B and Mitotic Checkpoint Regulation",
      "description": "Aurora kinase B (AURKB) is component of chromosomal passenger complex (CPC) mediating chromatin modification, spindle checkpoint regulation, cytokinesis, and kinetochore-microtubule attachment. AURKB polymorphisms associate with altered glioblastoma risk. AURKB overexpression induces chromosomal instability and aneuploidy.",
      "atomic_biological_processes": [
        {
          "name": "Aurora kinase B-mediated chromosomal passenger complex functions",
          "citations": [
            {
              "source_id": "14",
              "notes": "AURKB component of chromosomal passenger complex; mediates chromatin modification, spindle checkpoint regulation, cytokinesis"
            }
          ],
          "genes": ["AURKB"]
        },
        {
          "name": "AURKB regulation of chromosome segregation",
          "citations": [
            {
              "source_id": "14",
              "notes": "AURKB overexpression induces abnormalities in chromosome segregation, aneuploidy, and tumor development"
            }
          ],
          "genes": ["AURKB"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Chromosomal passenger complex",
          "citations": [
            {
              "source_id": "14",
              "notes": "CPC contains AURKB and other proteins; covers segregation of chromatids, cytokinesis, and histone modifications"
            }
          ],
          "genes": ["AURKB"]
        }
      ],
      "predicted_cellular_impact": [
        "AURKB genetic variations influence glioblastoma risk through altered checkpoint kinase function",
        "AURKB overexpression causes chromosomal instability and aneuploidy in glioblastoma",
        "AURKB-mediated spindle checkpoint dysfunction enables rapid mitotic progression",
        "AURKB targeting may impair glioblastoma proliferation and induce mitotic failure"
      ],
      "evidence_summary": "AURKB rs2289590 AC genotype shows association with decreased glioblastoma risk compared to other genotypes. In silico analysis of rs2289590 polymorphic region detected additional binding site for Yin-Yang 1 (YY1) transcription factor in presence of C allele, suggesting functional significance. AURKB is overexpressed in different cancer types including brain cancers. AURKB overexpression induces abnormalities in chromosome segregation and aneuploidy.",
      "significance_score": 0.72,
      "citations": [
        {
          "source_id": "14",
          "notes": "AURKB genetic variations and association with glioblastoma risk"
        }
      ],
      "supporting_genes": [
        "AURKB"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "INCENP",
          "SURVIVIN",
          "BOREALIN",
          "AURKC"
        ],
        "citations": [
          {
            "source_id": "14",
            "notes": "CPC proteins including AURKC form chromosomal passenger complex"
          }
        ]
      }
    },
    {
      "program_name": "Epigenetic Modifier Targeting and Cell Cycle Inhibition",
      "description": "Onametostat targets protein arginine methyltransferase PRMT5, an epigenetic writer regulating gene expression and nucleolar functions. Cell cycle kinase inhibitors (CDK, Aurora, PLK) impair glioblastoma proliferation under both normoxic and hypoxic conditions. Combination of epigenetic and cell cycle targeting shows synergistic effects in glioblastoma treatment.",
      "atomic_biological_processes": [
        {
          "name": "PRMT5-mediated protein arginine methylation",
          "citations": [
            {
              "source_id": "5",
              "notes": "Onametostat PRMT5 inhibitor identified as new player affecting cell cycle and nucleolar protein levels in glioblastoma"
            }
          ],
          "genes": []
        },
        {
          "name": "Cell cycle kinase inhibition",
          "citations": [
            {
              "source_id": "5",
              "notes": "Cell cycle-related protein kinase inhibitors (Aurora, CDK families) tested for glioblastoma treatment under normoxic and hypoxic conditions"
            }
          ],
          "genes": ["AURKB"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Nucleolus",
          "citations": [
            {
              "source_id": "5",
              "notes": "Onametostat causes reduction in nucleolar protein levels"
            }
          ],
          "genes": []
        }
      ],
      "predicted_cellular_impact": [
        "PRMT5 inhibition impairs glioblastoma proliferation even in chemotherapy-resistant cells",
        "Cell cycle kinase inhibition shows efficacy in glioblastoma under both normoxic and hypoxic conditions",
        "Combined epigenetic and cell cycle targeting achieves synergistic glioblastoma growth inhibition",
        "PRMT5 inhibition represents viable strategy for glioblastoma treatment with reduced toxicity to normal cells"
      ],
      "evidence_summary": "Screening of epigenetic modifier inhibitors and cell cycle kinase inhibitors against glioblastoma cell lines identified onametostat (PRMT5 inhibitor) as effective compound. Onametostat treatment reduces cell viability and proliferation. Immunostaining confirmed onametostat affects cell cycle and causes reduction in nucleolar protein levels. The effect observed under both normoxic and hypoxic culture conditions, suggesting potential clinical application.",
      "significance_score": 0.65,
      "citations": [
        {
          "source_id": "5",
          "notes": "Screening of epigenetic and cell cycle-related targets in glioblastoma"
        }
      ],
      "supporting_genes": [
        "AURKB"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "PRMT5",
          "CDK4",
          "CDK6"
        ],
        "citations": [
          {
            "source_id": "5",
            "notes": "PRMT5 and CDK inhibitors as therapeutic targets in glioblastoma"
          }
        ]
      }
    },
    {
      "program_name": "Mitotic Spindle Assembly and Checkpoint Control",
      "description": "Mitotic spindle checkpoint (spindle assembly checkpoint, SAC) genes including KNTC1 coordinate kinetochore-spindle microtubule attachments and checkpoint signaling. TTK (monopolar spindle 1-like kinase) is essential for chromosome alignment and centrosome duplication. Spindle checkpoint activation prevents cell cycle progression until proper chromosome alignment is achieved.",
      "atomic_biological_processes": [
        {
          "name": "Kinetochore-spindle microtubule attachment monitoring",
          "citations": [
            {
              "source_id": "31",
              "notes": "Spindle assembly checkpoint genes including KNTC1 coordinate proper chromosome attachment before anaphase"
            }
          ],
          "genes": ["KNTC1", "SKA3"]
        },
        {
          "name": "TTK-mediated chromosome alignment",
          "citations": [
            {
              "source_id": "31",
              "notes": "TTK dual specificity kinase essential for chromosome alignment at centromere during mitosis; required for centrosome duplication"
            }
          ],
          "genes": ["KNTC1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "Spindle checkpoint complex",
          "citations": [
            {
              "source_id": "31",
              "notes": "Spindle assembly checkpoint involves multiple proteins including KNTC1, BUBR1, MAD2, BUB1"
            }
          ],
          "genes": ["KNTC1"]
        }
      ],
      "predicted_cellular_impact": [
        "Mitotic checkpoint impairment in glioblastoma enables rapid mitotic progression despite chromosomal misalignment",
        "Checkpoint gene dysregulation contributes to chromosomal instability and aneuploidy in glioblastoma",
        "TTK overexpression in glioblastoma promotes proliferation and resistance to therapy",
        "Targeting spindle checkpoint may induce mitotic catastrophe in glioblastoma cells"
      ],
      "evidence_summary": "Mitotic spindle checkpoint genes represent potential targets for anticancer therapy. TTK gene is overexpressed in cancer and is associated with increased proliferation, colony formation, and resistance to targeted drugs. TTK plays important role in early hepatocellular carcinoma development and is upregulated when cells acquire drug resistance.",
      "significance_score": 0.70,
      "citations": [
        {
          "source_id": "31",
          "notes": "Mitotic spindle checkpoint genes in cancer development and resistance"
        }
      ],
      "supporting_genes": [
        "KNTC1", "SKA3"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "BUB1",
          "BUBR1",
          "MAD2L1",
          "MAD1L1",
          "TTK"
        ],
        "citations": [
          {
            "source_id": "31",
            "notes": "Multiple spindle checkpoint proteins required for mitotic control"
          }
        ]
      }
    },
    {
      "program_name": "FAM111B-PI3K/AKT Pathway and Glioma Malignancy",
      "description": "FAM111B (Family with sequence similarity 111, member B) is overexpressed in glioma tissues and associated with poor prognosis. FAM111B enhances glioma cell proliferation, invasion, and migration through activation of PI3K/AKT signaling pathway. PI3K/AKT inhibition reverses FAM111B-induced malignant phenotypes.",
      "atomic_biological_processes": [
        {
          "name": "FAM111B-mediated PI3K/AKT pathway activation",
          "citations": [
            {
              "source_id": "49",
              "notes": "FAM111B enhances proliferation, invasion, and migration via PI3K/AKT pathway; knockdown inhibits these activities"
            },
            {
              "source_id": "52",
              "notes": "FAM111B overexpression promotes glioma malignancy via PI3K/AKT pathway"
            }
          ],
          "genes": ["FAM111B"]
        }
      ],
      "atomic_cellular_components": [],
      "predicted_cellular_impact": [
        "FAM111B overexpression drives glioblastoma proliferation, invasion, and poor prognosis",
        "PI3K/AKT pathway hyperactivation from FAM111B upregulation promotes tumor growth",
        "FAM111B serves as potential therapeutic target to sensitize glioblastoma to PI3K/AKT inhibitors",
        "FAM111B expression correlates with disease stage and predicts overall survival"
      ],
      "evidence_summary": "FAM111B is significantly overexpressed in glioma tissues compared to adjacent normal tissues. Overexpression of FAM111B is associated with shorter overall survival, disease-specific survival, and increased disease stage. FAM111B knockdown significantly inhibits glioma cell proliferation, migration, and invasion. Knockdown also reduces the malignant properties of glioma cells. FAM111B overexpression enhances cell proliferation, colony formation, and invasion. The malignant phenotype induced by FAM111B correlates with PI3K/AKT pathway activation. PI3K/AKT inhibition reverses FAM111B-induced enhancement of glioma cell malignancy.",
      "significance_score": 0.79,
      "citations": [
        {
          "source_id": "49",
          "notes": "FAM111B role in glioma proliferation, migration, and invasion via PI3K/AKT pathway"
        },
        {
          "source_id": "52",
          "notes": "FAM111B overexpression promotes glioma malignancy and is potential therapeutic target"
        }
      ],
      "supporting_genes": [
        "FAM111B"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "PIK3CA",
          "AKT1",
          "AKT2",
          "AKT3"
        ],
        "citations": [
          {
            "source_id": "49",
            "notes": "PI3K/AKT pathway components downstream of FAM111B"
          }
        ]
      }
    },
    {
      "program_name": "Antigen Presentation and Immunotherapy Response",
      "description": "CHEK2 depletion in glioblastoma activates STING pathway and enhances antigen presentation genes (B2M, H2 molecules), leading to increased type I interferon response. Enhanced MHC-I expression sensitizes glioblastoma to PD-1 checkpoint blockade. CHEK2 loss paradoxically enhances immunotherapy efficacy despite impairing DNA repair.",
      "atomic_biological_processes": [
        {
          "name": "CHEK2-regulated STING pathway activation",
          "citations": [
            {
              "source_id": "24",
              "notes": "CHEK2 depletion results in STING pathway activation marked by phosphorylation of TBK1"
            }
          ],
          "genes": ["CHEK1"]
        },
        {
          "name": "Antigen presentation and MHC-I upregulation",
          "citations": [
            {
              "source_id": "24",
              "notes": "CHEK2 inhibition/depletion enhances expression of B2m, H2.D1, H2.K1 MHC-I chain genes and other IFN-γ-regulated genes"
            }
          ],
          "genes": []
        }
      ],
      "atomic_cellular_components": [],
      "predicted_cellular_impact": [
        "CHEK2 inhibition sensitizes glioblastoma to PD-1 blockade immunotherapy",
        "STING pathway activation from CHEK2 loss drives type I interferon response",
        "Enhanced MHC-I expression increases CD8 T cell recognition of tumor cells",
        "CHEK2-targeted therapy combined with immune checkpoint blockade shows synergistic efficacy",
        "CHEK2 depletion generates long-term survivors in immunotherapy-treated glioblastoma models"
      ],
      "evidence_summary": "CHEK2 depletion in glioblastoma results in STING pathway activation and upregulation of antigen presentation genes. CHEK2 knockout glioma cells treated with anti-PD-1 show improved survival compared to control cells. Thirty percent long-term survivors achieved in CHEK2 knockout gliomas treated with anti-PD-1, compared to no survival benefit with anti-PD-1 alone in wild-type gliomas. CHEK2 inhibition-induced immunotherapy response is predominantly dependent on antigen presentation and type I interferon pathways.",
      "significance_score": 0.77,
      "citations": [
        {
          "source_id": "24",
          "notes": "CHEK2 inhibition enhances glioblastoma response to PD-1 blockade through STING pathway and antigen presentation"
        }
      ],
      "supporting_genes": [
        "CHEK1"
      ],
      "required_genes_not_in_input": {
        "genes": [
          "CHEK2",
          "STING",
          "TBK1",
          "IRF3"
        ],
        "citations": [
          {
            "source_id": "24",
            "notes": "STING pathway components downstream of CHEK2"
          }
        ]
      }
    }
  ],
  "method": {
    "clustering_basis": [
      "Pathway databases (DNA repair, cell cycle, replication)",
      "Literature co-citation of genes in glioblastoma context",
      "Functional protein-protein interactions",
      "Coordinated gene expression in cancer cells",
      "Shared involvement in same cellular process or complex"
    ],
    "notes": "Analysis prioritized recent publications (2023-2024) on glioblastoma-specific mechanisms while anchoring to well-established roles of gene products. Programs were identified through systematic integration of functional roles, disease-specific alterations, and pathway interconnections. Multiple genes clustering in same program indicate pathway-level coordination relevant to glioblastoma biology."
  },
  "version": "1.0"
}
```

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC2829940/
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC8833533/
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC8732357/
4. https://www.nature.com/articles/s41467-024-45979-5
5. https://www.nature.com/articles/s41598-024-54707-4
6. https://academic.oup.com/carcin/article/doi/10.1093/carcin/bgaf017/8090478
7. https://www.nature.com/articles/ncomms13398
8. https://pubmed.ncbi.nlm.nih.gov/25071006/
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC7935783/
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC4279418/
11. https://www.oncotarget.com/article/2225/text/
12. https://www.nature.com/articles/s41598-023-44946-2
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC7591888/
14. https://www.nature.com/articles/s41598-021-96935-y
15. https://www.nature.com/articles/s41419-018-0482-4
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC7299000/
17. https://www.ncbi.nlm.nih.gov/gene/9212
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC4380124/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC9465177/
20. https://www.nature.com/articles/s41419-021-04498-7
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC5440309/
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC8799097/
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC7198369/
24. https://www.nature.com/articles/s41467-023-36878-2
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC147676/
26. https://www.nature.com/articles/s41467-018-05177-6
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC8987098/
28. https://aacrjournals.org/cancerres/article/63/23/8181/510846/Homologous-Recombination-Deficiency-Leads-to
29. https://pubmed.ncbi.nlm.nih.gov/30301766/
30. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0097739
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC9660312/
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC11483370/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC8492343/
34. https://aacrjournals.org/mct/article/20/1/64/92838/Reprogramming-of-Nucleotide-Metabolism-Mediates
35. https://ascopubs.org/doi/10.1200/PO-25-00435
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC12049523/
37. https://pmc.ncbi.nlm.nih.gov/articles/PMC9853271/
38. https://www.nature.com/articles/s41467-018-07378-5
39. https://www.nature.com/articles/s41392-024-02080-z
40. https://www.uniprot.org/uniprotkb/P33610/entry
41. https://pmc.ncbi.nlm.nih.gov/articles/PMC9036127/
42. https://pmc.ncbi.nlm.nih.gov/articles/PMC5520903/
43. https://academic.oup.com/nar/article/48/4/1872/5658445
44. https://pubmed.ncbi.nlm.nih.gov/29405332/
45. https://www.nature.com/articles/s41389-021-00309-y
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC7722765/
47. https://www.nature.com/articles/ncomms11638
48. https://pmc.ncbi.nlm.nih.gov/articles/PMC12087166/
49. https://pmc.ncbi.nlm.nih.gov/articles/PMC12370488/
50. https://pmc.ncbi.nlm.nih.gov/articles/PMC11963297/
51. https://www.eurekalert.org/news-releases/1085688
52. https://pmc.ncbi.nlm.nih.gov/articles/PMC6788831/
53. https://rupress.org/jcb/article/219/6/e201906204/151688/MASTL-promotes-cell-contractility-and-motility
54. https://pmc.ncbi.nlm.nih.gov/articles/PMC9298524/
55. https://pubmed.ncbi.nlm.nih.gov/20100909/
56. https://www.nature.com/articles/bjc2017301
57. https://www.tandfonline.com/doi/full/10.1080/07853890.2023.2169751
58. https://archiv.ub.uni-heidelberg.de/volltextserver/34989/
59. https://www.ncbi.nlm.nih.gov/gene/9700
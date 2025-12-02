---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-11-26T13:58:14.688694'
end_time: '2025-11-26T14:02:23.448421'
duration_seconds: 248.76
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 50
---

## Question

Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: ["SERPINE1", "EMP1", "SPOCD1", "ARHGAP29", "IL1R1", "COL6A2", "MYOF", "F13A1", "CXCL10", "CHI3L1", "MET", "IL6", "SAA2", "BIRC3", "MCTP2", "ANGPTL4", "ICAM1", "CCN1", "CAV1", "APLN", "FOSL1", "SNTG2-AS1", "TPD52L1", "SAA4", "KRT75", "NFATC2", "COL5A1", "AC243829.2", "CLCF1", "ARSJ", "PLA2G2A", "HMGA2", "PTX3", "TLR2", "LINC00698", "ALPK2", "TNFAIP3", "TNFAIP2", "NDRG1", "SMOC2", "ADGRL2", "KANK4", "GEM", "FAS", "CXCL8", "CFH", "ABCC3", "CXCL14", "ZFP36", "RCAN2", "GADD45A", "COL1A2", "LTF", "DHRS3", "IDO1", "HAP1", "AXL", "ATP6V0D2", "KLF5", "ST6GALNAC5", "GPD1", "PAPPA2", "BAG3", "MYBPH", "MYBPC1", "MX2", "APBB1IP", "ANPEP", "ALPL", "GPRC5A", "SPP1", "CXCL2", "GPC5", "RRAD", "LIF", "CHRNA9", "IL4R", "NPNT", "SAA1", "NPR3", "PROM1", "SLIT3", "ITGBL1", "MYO5B", "RPS5", "RPS27", "ETS2", "PTGS2", "RPS18", "BNC2", "CPA4", "NPAS2", "CD274", "SLC10A6", "LRAT", "LINC01993", "LINC02832", "LINC02821", "GBP5", "AC021851.2", "AKAP12", "LINC02154", "FN1", "MIR222HG", "VEGFA", "GBP2", "ZNF735", "TSHZ2", "TRPM2", "LUCAT1", "PI3"]

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
This is a comprehensive task requesting a systematic literature-based analysis of a gene list in the context of malignant glioblastoma cells. The user wants me to:

1. Identify gene programs (clusters of genes acting in specific pathways/processes)
2. Provide JSON output conforming to their schema
3. Base all claims on the literature provided

Let me analyze the search results and input gene list:

The context is: malignant glioblastoma (GBM) cells
The input genes are: A large list of 95 genes

From the search results, I can identify several key programs:

1. **EMT and Invasion Program**: SERPINE1, EMP1, COL5A1, COL6A2, COL1A2, FN1, FOSL1, CCN1, CTGF (related), MET, ITGBL1, SMOC2
   - Supporting evidence: [1] discusses SERPINE1 upregulation in dispersive GBM cells and its role in invasion
   - [2] shows EMP1 promotes invasion and migration
   - [5] shows COL5A1 promotes invasion
   - [30] discusses FN1 and EMT in glioma
   - [46] discusses EMT markers in glioblastoma

2. **Inflammatory Cytokine Signaling**: IL6, IL-8 (implied as CXCL8), IL1R1, TNFα (implied), IL4R, LIF
   - Supporting evidence: [4] extensively covers cytokine profiles in GBM
   - [10] discusses pentraxin 3 in inflammation
   - [18] covers COX-2/PGE2 inflammatory pathways

3. **Angiogenesis and Vascular Signaling**: VEGFA, APLN, HIF-1α (implied), CLCF1, CHI3L1, PTX3
   - Supporting evidence: [16] discusses HIF-1α and VEGF in angiogenesis, [21] discusses apelin (APLN) in angiogenesis, and [17] discusses CHI3L1 in angiogenesis

4. **Immune Evasion and Immunosuppression**: PD-L1 (CD274), IDO1, CFH, CXCL10, CXCL14, CXCL2, GBP2
   - Supporting evidence: [24] discusses PD-L1 and Treg expansion, [12] covers additional immune checkpoint mechanisms through IDO1, [36] examines CFH's role in immune evasion, and [8] addresses CXCL family involvement in immunosuppression

5. **Extracellular Matrix Remodeling**: COL5A1, COL6A2, COL1A2, FN1, MYOF, F13A1, SMOC2, SAA1, SAA2, SAA4
   - Supporting evidence: [1] discusses ECM degradation via SERPINE1, [5] discusses COL5A1 in ECM remodeling, [33] comprehensive systematic review on ECM in GBM, and [27] discusses SAA effects on ECM

6. **Cancer Stem Cell Maintenance**: HMGA2, SOX2 (implied), OCT4 (implied), BAG3, KLF5, NFATC2, LIF, ANGPTL4
   - Supporting evidence: [19] discusses HMGA2 in stemness, [23] discusses BAG3 in cancer stem cell maintenance

, [31] discusses LIF in stem cell maintenance, and [34] discusses ANGPTL4 in stemness

7. **Protease Activity and ECM Degradation**: SERPINE1, SAA1, SAA2, SAA4, ANPEP, CPM (implied), MYOF, F13A1
   - Supporting evidence: [1] SERPINE1 regulates plasminogen system, [27] SAA induces MMP expression

8. **Hypoxia Response**: NDRG1, HIF-1α pathway (implied), IDO1
   - Supporting evidence: [26] discusses NDRG1 in hypoxia, [16] discusses HIF-1α and VEGF

9. **Signaling Pathways (PI3K/AKT/

mTOR)**: PTEN loss (implied), AKT pathway, multiple genes
   - Supporting evidence: [2] discusses PI3K/AKT/mTOR activation, [50] discusses metabolic rewiring

10. **Apoptosis Resistance**: BAG3, BIRC3, BCL2 family (implied), TNFAIP3, GADD45A
    - Supporting evidence: [23] discusses BAG3 in apoptosis resistance, [13] discusses BIRC3 in inhibiting apoptosis

11. **Cell Adhesion and Migration**: ICAM1, CAV1, MYOF, KANK4, AKAP12
    - Supporting evidence: [7] discusses VCAM-1 in adhesion, [1] discusses focal adhesion in SERPINE1-mediated migration

12. **Metabolic Reprogramming**: IDO1, PTGS2 (COX-2), glycolysis genes
    - Supporting evidence: [50] discusses metabolic rewiring in GBM, [18] discusses COX-2/PGE2 signaling

13. **Growth Factor Signaling**: MET, EGFR (implied), IL4R, SPP1
    - Supporting evidence: [6] discusses HGF/MET signaling

, [50] discusses EGFR in metabolic reprogramming

14. **Transcriptional Regulation**: FOSL1, KLF5, NFATC2, NFATC1 (implied)
    - Supporting evidence: [9] discusses FOSL1 in mesenchymal GBM, [22] discusses KLF5 in various cancers, [25] discusses NFAT proteins in GBM

15. **Macrophage/Microglia Reprogramming**: TLR2, CXCL10, CXCL14, CXCL2, CCN1, SAA proteins
    - Supporting evidence: [11] discusses TLR2 in macrophage reprogramming, [48] discusses macrophage/microglia in GBM

Now I'll structure this into a JSON format, ensuring each program is properly referenced to the relevant search results.
</think>

```json
{
    "context": {
        "cell_type": "malignant glioblastoma cells",
        "disease": "glioblastoma multiforme",
        "tissue": "brain"
    },
    "input_genes": [
        "SERPINE1", "EMP1", "SPOCD1", "ARHGAP29", "IL1R1", "COL6A2", "MYOF", "F13A1",
        "CXCL10", "CHI3L1", "MET", "IL6", "SAA2", "BIRC3", "MCTP2", "ANGPTL4", "ICAM1",
        "CCN1", "CAV1", "APLN", "FOSL1", "SNTG2-AS1", "TPD52L1", "SAA4", "KRT75",
        "NFATC2", "COL5A1", "AC243829.2", "CLCF1", "ARSJ", "PLA2G2A", "HMGA2", "PTX3",
        "TLR2", "LINC00698", "ALPK2", "TNFAIP3", "TNFAIP2", "NDRG1", "SMOC2", "ADGRL2",
        "KANK4", "GEM", "FAS", "CXCL8", "CFH", "ABCC3", "CXCL14", "ZFP36", "RCAN2",
        "GADD45A", "COL1A2", "LTF", "DHRS3", "IDO1", "HAP1", "AXL", "ATP6V0D2", "KLF5",
        "ST6GALNAC5", "GPD1", "PAPPA2", "BAG3", "MYBPH", "MYBPC1", "MX2", "APBB1IP",
        "ANPEP", "ALPL", "GPRC5A", "SPP1", "CXCL2", "GPC5", "RRAD", "LIF", "CHRNA9",
        "IL4R", "NPNT", "SAA1", "NPR3", "PROM1", "SLIT3", "ITGBL1", "MYO5B", "RPS5",
        "RPS27", "ETS2", "PTGS2", "RPS18", "BNC2", "CPA4", "NPAS2", "CD274", "SLC10A6",
        "LRAT", "LINC01993", "LINC02832", "LINC02821", "GBP5", "AC021851.2", "AKAP12",
        "LINC02154", "FN1", "MIR222HG", "VEGFA", "GBP2", "ZNF735", "TSHZ2", "TRPM2",
        "LUCAT1", "PI3"
    ],
    "programs": [
        {
            "program_name": "EMT-Driven Invasion Program",
            "description": "A coordinated gene program mediating epithelial-mesenchymal transition and cellular invasiveness in glioblastoma. This program includes transcriptional regulators (FOSL1, KLF5, NFATC2), extracellular matrix components and remodelers (SERPINE1, COL5A1, COL6A2, COL1A2, FN1, SMOC2, ITGBL1), and cell adhesion/migration effectors (EMP1, CAV1, MYOF, KANK4, ICAM1). The program drives mesenchymal identity, enhanced cell motility, and increased invasive capacity into surrounding brain tissue.",
            "atomic_biological_processes": [
                {
                    "name": "transcriptional regulation of EMT",
                    "citations": [
                        {
                            "source_id": "9",
                            "notes": "FOSL1 controls mesenchymal transcriptional program and maintains EMT phenotype in GBM"
                        },
                        {
                            "source_id": "22",
                            "notes": "KLF5 regulates EMT-related transcription factors and cell motility"
                        },
                        {
                            "source_id": "25",
                            "notes": "NFATC2 associated with cancer progression and EMT processes"
                        }
                    ],
                    "genes": ["FOSL1", "KLF5", "NFATC2"]
                },
                {
                    "name": "extracellular matrix proteolysis and remodeling",
                    "citations": [
                        {
                            "source_id": "1",
                            "notes": "SERPINE1 regulates ECM degradation via plasminogen activator system and cell-substrate adhesion"
                        },
                        {
                            "source_id": "5",
                            "notes": "COL5A1 plays pivotal role in ECM remodeling and cell cytoskeleton regulation during metastasis"
                        },
                        {
                            "source_id": "33",
                            "notes": "Comprehensive review of ECM components and their role in GBM invasion; collagen types I, V, VI and fibronectin critical for tumor progression"
                        }
                    ],
                    "genes": ["SERPINE1", "COL5A1", "COL6A2", "COL1A2", "FN1", "SMOC2", "ITGBL1"]
                },
                {
                    "name": "cell adhesion and focal contact dynamics",
                    "citations": [
                        {
                            "source_id": "1",
                            "notes": "SERPINE1 regulates focal adhesion formation and cell-ECM interactions"
                        },
                        {
                            "source_id": "7",
                            "notes": "ICAM-1 mediates cell-cell adhesion and macrophage-GBM interaction"
                        }
                    ],
                    "genes": ["ICAM1", "CAV1", "KANK4", "MYOF"]
                }
            ],
            "atomic_cellular_components": [
                {
                    "name": "focal adhesions",
                    "citations": [
                        {
                            "source_id": "1",
                            "notes": "SERPINE1 controls focal adhesion dynamics during cell migration"
                        }
                    ],
                    "genes": ["SERPINE1", "KANK4"]
                },
                {
                    "name": "extracellular matrix",
                    "citations": [
                        {
                            "source_id": "33",
                            "notes": "ECM actively shapes GBM development and invasion"
                        }
                    ],
                    "genes": ["COL5A1", "COL6A2", "COL1A2", "FN1", "SMOC2", "ITGBL1"]
                }
            ],
            "predicted_cellular_impact": [
                "Enhanced cell migration and invasiveness into brain parenchyma",
                "Increased mesenchymal identity with reduced epithelial markers",
                "Remodeling of focal adhesion architecture",
                "Facilitated ECM degradation and rearrangement",
                "Acquisition of stem-like properties",
                "Enhanced resistance to conventional therapies"
            ],
            "evidence_summary": "Multiple complementary lines of evidence support this program: (1) SERPINE1 is the most upregulated EMT gene in dispersive GBM cells and correlates with poor survival; (2) multiple collagen and adhesion molecules are coordinately expressed during mesenchymal transition; (3) FOSL1 directly controls mesenchymal gene expression including SERPINE1; (4) EMT transcription factors (FOSL1, KLF5, NFATC2) are upregulated in high-grade, invasive tumors.",
            "significance_score": 0.92,
            "citations": [
                {
                    "source_id": "1",
                    "notes": "SERPINE1 identified as key regulator of GBM cell dispersal and invasion"
                },
                {
                    "source_id": "5",
                    "notes": "COL5A1 promotes GBM malignancy through EMT-related mechanisms"
                },
                {
                    "source_id": "9",
                    "notes": "FOSL1 controls mesenchymal GBM plasticity and aggressiveness"
                },
                {
                    "source_id": "30",
                    "notes": "Fibronectin expression determines distinct malignant glioma progressions via TGF-β-induced EMT"
                },
                {
                    "source_id": "46",
                    "notes": "EMT in GBM progression involves TGF-β, WNT/β-catenin, and transcription factors"
                }
            ],
            "supporting_genes": [
                "SERPINE1", "EMP1", "COL5A1", "COL6A2", "COL1A2", "FN1", "SMOC2",
                "ITGBL1", "FOSL1", "KLF5", "NFATC2", "CAV1", "MYOF", "KANK4", "ICAM1"
            ],
            "required_genes_not_in_input": {
                "genes": ["TWIST1", "SNAIL", "SLUG", "ZEB1", "SMAD2", "SMAD3", "TGFB1"],
                "citations": [
                    {
                        "source_id": "46",
                        "notes": "EMT master regulators including TWIST1, SNAIL, SLUG, and ZEB1 are upregulated in mesenchymal GBM"
                    }
                ]
            }
        },
        {
            "program_name": "Pro-Inflammatory Cytokine Signaling",
            "description": "A gene program centered on production and signaling of pro-inflammatory cytokines that drive GBM development and progression. This program includes IL-6, IL-8 (CXCL8), IL-1 receptor (IL1R1), IL-4 receptor (IL4R), leukemia inhibitory factor (LIF), and cardiotrophin-like cytokine factor 1 (CLCF1). These cytokines signal through receptors and downstream pathways (STAT3, NF-κB) to promote tumor cell proliferation, survival, and create an immunosuppressive microenvironment.",
            "atomic_biological_processes": [
                {
                    "name": "IL-6 and IL-8 production and signaling",
                    "citations": [
                        {
                            "source_id": "4",
                            "notes": "IL-6 and IL-8 are the most consistently elevated pro-inflammatory cytokines in GBM with highest diagnostic potential (RR = 2.923 and 3.151 respectively)"
                        },
                        {
                            "source_id": "18",
                            "notes": "IL-6 and IL-8 participate in COX-2/PGE2 inflammatory cascade in GBM"
                        }
                    ],
                    "genes": ["IL6", "CXCL8"]
                },
                {
                    "name": "IL-1 receptor signaling and NF-κB activation",
                    "citations": [
                        {
                            "source_id": "4",
                            "notes": "IL-1β binds IL-1R and activates NF-κB pathway, leading to upregulation of pro-inflammatory genes including IL-6 and IL-8"
                        }
                    ],
                    "genes": ["IL1R1", "TNFAIP3"]
                },
                {
                    "name": "LIF-mediated immunosuppression and stemness",
                    "citations": [
                        {
                            "source_id": "31",
                            "notes": "LIF prevents GBM cell differentiation, increases cancer stem cell markers (CD133), and promotes TAM formation"
                        }
                    ],
                    "genes": ["LIF"]
                },
                {
                    "name": "CLCF1-mediated cytokine signaling",
                    "citations": [
                        {
                            "source_id": "39",
                            "notes": "CLCF1 (IL-6 superfamily member) promotes GBM cell proliferation, migration and invasion; serves as unfavorable prognostic marker"
                        }
                    ],
                    "genes": ["CLCF1"]
                }
            ],
            "atomic_cellular_components": [
                {
                    "name": "cytokine receptors (gp130, IL-4R, IL-1R)",
                    "citations": [
                        {
                            "source_id": "4",
                            "notes": "IL-1R, IL-6R, IL-8R signaling is central to GBM cytokine-driven pathology"
                        }
                    ],
                    "genes": ["IL1R1", "IL4R", "CLCF1"]
                }
            ],
            "predicted_cellular_impact": [
                "Enhanced proliferation via STAT3 and NF-κB activation",
                "Increased cell survival and reduced apoptosis",
                "Promotion of immunosuppressive microenvironment",
                "Maintenance of cancer stem cell properties",
                "Enhanced angiogenesis through secondary signals",
                "Recruitment and polarization of myeloid cells"
            ],
            "evidence_summary": "Pro-inflammatory cytokines are markedly elevated in GBM specimens. IL-6 and IL-8 demonstrate the highest diagnostic relevance with approximately 3-fold higher probability of GBM development above threshold levels. These cytokines coordinate with each other through IL-1β-driven NF-κB amplification, creating a sustained inflammatory milieu. LIF and CLCF1 extend this program by directly supporting stemness and invasiveness while reprogramming immune cells toward suppressive functions.",
            "significance_score": 0.88,
            "citations": [
                {
                    "source_id": "4",
                    "notes": "Comprehensive profiling of cytokine changes in GBM; IL-6 and IL-8 as key pro-inflammatory mediators"
                },
                {
                    "source_id": "10",
                    "notes": "PTX3 regulation of pro-inflammatory cytokines in GBM microenvironment"
                },
                {
                    "source_id": "31",
                    "notes": "LIF as immunosuppressive factor promoting TAM formation and cancer stemness"
                },
                {
                    "source_id": "39",
                    "notes": "CLCF1 as unfavorable prognostic marker in GBM promoting proliferation"
                }
            ],
            "supporting_genes": [
                "IL6", "CXCL8", "IL1R1", "IL4R", "LIF", "CLCF1", "TNFAIP3"
            ],
            "required_genes_not_in_input": {
                "genes": ["STAT3", "NFKB1", "RELA", "IL1B", "TNF", "IL10"],
                "citations": [
                    {
                        "source_id": "4",
                        "notes": "STAT3 and NF-κB are downstream effectors of IL-1β, IL-6, and IL-8 signaling in GBM"
                    }
                ]
            }
        },
        {
            "program_name": "Angiogenesis and Vascular Signaling",
            "description": "A gene program driving tumor neovascularization through VEGF and apelin signaling pathways. This program includes VEGFA, APLN (apelin), CHI3L1, PTX3, and CLCF1. These genes promote endothelial cell proliferation, migration, and vascular formation, particularly under hypoxic conditions. The program creates the highly vascularized phenotype characteristic of GBM and enables nutrient delivery to support rapid tumor growth.",
            "atomic_biological_processes": [
                {
                    "name": "VEGF-mediated endothelial proliferation and sprouting",
                    "citations": [
                        {
                            "source_id": "16",
                            "notes": "VEGF is essential factor for angiogenesis in GBM; upregulated in necrotic regions; VEGF and VEGFR highly expressed in GBM tissues"
                        },
                        {
                            "source_id": "49",
                            "notes": "Pseudopalisading cells in GBM secrete VEGF and IL-8 to promote angiogenesis"
                        }
                    ],
                    "genes": ["VEGFA"]
                },
                {
                    "name": "apelin-mediated sprouting angiogenesis",
                    "citations": [
                        {
                            "source_id": "21",
                            "notes": "APLN/APLNR signaling required for GBM sprouting angiogenesis; loss of APLN reduces vascular density and tumor growth; APLN co-expressed with VEGFA in hypoxic regions"
                        }
                    ],
                    "genes": ["APLN"]
                },
                {
                    "name": "CHI3L1-mediated angiogenesis",
                    "citations": [
                        {
                            "source_id": "17",
                            "notes": "CHI3L1 exerts pro-angiogenic effect promoting tumor angiogenesis through vascular endothelial cells and maintaining vascular integrity; elevated serum levels in GBM"
                        }
                    ],
                    "genes": ["CHI3L1"]
                },
                {
                    "name": "PTX3-mediated inflammation-driven angiogenesis",
                    "citations": [
                        {
                            "source_id": "10",
                            "notes": "PTX3 regulates macrophage-associated tumor-promoting inflammation and angiogenesis in glioblastoma"
                        }
                    ],
                    "genes": ["PTX3"]
                }
            ],
            "atomic_cellular_components": [
                {
                    "name": "endothelial cells and vascular structures",
                    "citations": [
                        {
                            "source_id": "16",
                            "notes": "VEGF targets endothelial cells and promotes vascular proliferation; abnormal GBM vasculature leads to BBB disruption"
                        },
                        {
                            "source_id": "21",
                            "notes": "APLN expressed in endothelial tip cells during sprouting angiogenesis"
                        }
                    ],
                    "genes": ["VEGFA", "APLN", "CHI3L1"]
                }
            ],
            "predicted_cellular_impact": [
                "Enhanced vascular density and complexity within tumor",
                "Increased oxygen and nutrient delivery to tumor core",
                "Facilitation of tumor expansion into surrounding brain",
                "Promotion of aberrant vascular morphology (tortuous, leaky vessels)",
                "Enhanced BBB disruption and vasogenic edema",
                "Promotion of vascular-associated tumor cell invasion"
            ],
            "evidence_summary": "GBM exhibits extensive neovascularization as a hallmark feature. VEGF is the canonical driver, highly expressed particularly in necrotic and hypoxic regions. APLN provides a complementary sprouting angiogenesis signal that is essential for tumor vascular patterning. CHI3L1 and PTX3 operate through inflammatory mechanisms to support vascular formation. The synergy of multiple angiogenic signals enables the dense, pathological vasculature characteristic of aggressive GBM.",
            "significance_score": 0.85,
            "citations": [
                {
                    "source_id": "16",
                    "notes": "HIF-1α and VEGF are potent biomarkers of GBM prognosis; VEGF upregulated in necrotic regions"
                },
                {
                    "source_id": "21",
                    "notes": "Apelin/APLNR signaling required for in vivo tumor angiogenesis and GBM growth"
                },
                {
                    "source_id": "17",
                    "notes": "CHI3L1 elevated in GBM serum; promotes tumor angiogenesis"
                },
                {
                    "source_id": "49",
                    "notes": "Pseudopalisades hyperexpress HIF-1 and secrete VEGF and IL-8 promoting angiogenesis"
                }
            ],
            "supporting_genes": [
                "VEGFA", "APLN", "CHI3L1", "PTX3", "CLCF1"
            ],
            "required_genes_not_in_input": {
                "genes": ["VEGFR1", "VEGFR2", "APLNR", "NRP1", "NRP2", "FLT1", "KDR"],
                "citations": [
                    {
                        "source_id": "16",
                        "notes": "VEGF receptors (VEGFR1/2) required for VEGF-mediated endothelial signaling"
                    },
                    {
                        "source_id": "21",
                        "notes": "APLNR required for apelin signaling in endothelial cells"
                    }
                ]
            }
        },
        {
            "program_name": "Immune Evasion and Checkpoint Activation",
            "description": "A gene program enabling GBM escape from anti-tumor immune surveillance through upregulation of checkpoint ligands, immunosuppressive factors, and immune cell reprogramming mechanisms. This program includes PD-L1 (CD274), IDO1, complement factor H (CFH), and chemokines (CXCL10, CXCL14, CXCL2). These genes create an immunosuppressive microenvironment through T cell exhaustion, regulatory T cell expansion, myeloid-derived suppressor cell recruitment, and complement inhibition.",
            "atomic_biological_processes": [
                {
                    "name": "PD-L1-mediated T cell exhaustion and Treg expansion",
                    "citations": [
                        {
                            "source_id": "24",
                            "notes": "PD-L1 upregulation in GBM promotes Treg expansion and maintains immunosuppressive microenvironment; elevated CD274 mRNA correlates with increased FOXP3 and poor survival"
                        }
                    ],
                    "genes": ["CD274"]
                },
                {
                    "name": "IDO1-mediated tryptophan depletion and immunosuppression",
                    "citations": [
                        {
                            "source_id": "12",
                            "notes": "IDO1 converts tryptophan to immunosuppressive kynurenines; high IDO1 expression correlates with poor outcomes and increased tumor grade; promotes T cell apoptosis and Treg expansion"
                        }
                    ],
                    "genes": ["IDO1"]
                },
                {
                    "name": "complement evasion via CFH",
                    "citations": [
                        {
                            "source_id": "36",
                            "notes": "CFH inhibits complement-mediated immune responses; increased CFH and FHL-1 associated with poor GBM survival; prevents opsonization and C3d-mediated immune cell activation"
                        }
                    ],
                    "genes": ["CFH"]
                },
                {
                    "name": "chemokine-mediated immune cell recruitment and polarization",
                    "citations": [
                        {
                            "source_id": "8",
                            "notes": "CXCL family (CXCL9, CXCL10, CXCL11, CXCL14) enriched in high-risk IDH wild-type gliomas; promote immunocyte infiltration but in context of immunosuppressive microenvironment with high ICG expression"
                        }
                    ],
                    "genes": ["CXCL10", "CXCL14", "CXCL2"]
                }
            ],
            "atomic_cellular_components": [
                {
                    "name": "immune checkpoint molecule expression",
                    "citations": [
                        {
                            "source_id": "24",
                            "notes": "PD-L1 highly expressed on GBM tumor cells and myeloid cells"
                        }
                    ],
                    "genes": ["CD274"]
                },
                {
                    "name": "immunosuppressive enzyme production",
                    "citations": [
                        {
                            "source_id": "12",
                            "notes": "IDO1 rapidly induced in response to immune surveillance in cancer"
                        }
                    ],
                    "genes": ["IDO1"]
                }
            ],
            "predicted_cellular_impact": [
                "Impaired anti-tumor CD8+ T cell response",
                "Expansion of immunosuppressive regulatory T cells (Tregs)",
                "Increased immunosuppressive myeloid cell accumulation",
                "Enhanced complement resistance on tumor cell surface",
                "Reduced responsiveness to checkpoint inhibitor monotherapy",
                "Creation of immunosuppressive microenvironment resistant to immunotherapy"
            ],
            "evidence_summary": "GBM establishes robust immune evasion through multiple complementary mechanisms. PD-L1 expression directly drives Treg expansion and T cell exhaustion. IDO1 creates a tryptophan-depleted microenvironment that sustains immunosuppression. CFH provides complement evasion, a less-appreciated but critical immune escape mechanism. Coordinated chemokine signaling recruits immune cells but reprograms them toward immunosuppressive phenotypes. The convergence of these mechanisms explains the limited efficacy of single checkpoint inhibitor therapy in GBM.",
            "significance_score": 0.87,
            "citations": [
                {
                    "source_id": "24",
                    "notes": "PD-L1 expression in GBM correlates with Treg expansion and poor prognosis"
                },
                {
                    "source_id": "12",
                    "notes": "IDO1 activation correlates with poor outcomes in GBM; immunotherapeutic targeting rationale"
                },
                {
                    "source_id": "36",
                    "notes": "CFH as innate immune checkpoint; overexpression associated with poor GBM survival"
                },
                {
                    "source_id": "8",
                    "notes": "CXCL family in high-risk gliomas with immunosuppressive microenvironment"
                }
            ],
            "supporting_genes": [
                "CD274", "IDO1", "CFH", "CXCL10", "CXCL14", "CXCL2", "GBP2"
            ],
            "required_genes_not_in_input": {
                "genes": ["PDCD1", "CTLA4", "LAG3", "TIM3", "FOXP3", "IL10", "TGFB1", "STAT3"],
                "citations": [
                    {
                        "source_id": "24",
                        "notes": "PD-1 and other immune checkpoints on T cells are ligands for PD-L1"
                    },
                    {
                        "source_id": "12",
                        "notes": "STAT3 and other signaling mediators downstream of immunosuppressive pathways"
                    }
                ]
            }
        },
        {
            "program_name": "Extracellular Matrix Proteolysis",
            "description": "A gene program controlling degradation and remodeling of extracellular matrix through multiple protease systems and their regulators. This program includes serine protease inhibitors and activators (SERPINE1, SAA1, SAA2, SAA4), metalloproteinase regulators (MYOF), and cross-linking enzymes (F13A1). These genes enable ECM degradation to facilitate tumor cell migration, invasion, and colonization of brain tissue.",
            "atomic_biological_processes": [
                {
                    "name": "plasminogen activator system regulation",
                    "citations": [
                        {
                            "source_id": "1",
                            "notes": "SERPINE1 (PAI-1) is key regulator of plasminogen activator system; has central role in ECM degradation and remodeling; facilitates cell migration"
                        }
                    ],
                    "genes": ["SERPINE1"]
                },
                {
                    "name": "matrix metalloproteinase regulation and activation",
                    "citations": [
                        {
                            "source_id": "27",
                            "notes": "SAA induces expression of MMP-2 and MMP-9; rSAA activates plasminogen and MMPs for ECM degradation"
                        },
                        {
                            "source_id": "41",
                            "notes": "MYOF regulates MMP production and secretion affecting cancer cell invasion"
                        }
                    ],
                    "genes": ["SAA1", "SAA2", "SAA4", "MYOF"]
                },
                {
                    "name": "fibrin cross-linking and matrix stabilization",
                    "citations": [
                        {
                            "source_id": "42",
                            "notes": "F13A1 (Factor XIII-A) stabilizes fibrin networks; may regulate fibrin turnover in extravascular tumor microenvironment; TAM-derived F13A1 supports micrometastasis survival"
                        }
                    ],
                    "genes": ["F13A1"]
                }
            ],
            "atomic_cellular_components": [
                {
                    "name": "serine protease inhibitors and activators",
                    "citations": [
                        {
                            "source_id": "1",
                            "notes": "SERPINE1 is member of serine proteinase inhibitor superfamily"
                        }
                    ],
                    "genes": ["SERPINE1"]
                },
                {
                    "name": "membrane trafficking and vesicular transport",
                    "citations": [
                        {
                            "source_id": "41",
                            "notes": "MYOF regulates membrane trafficking and receptor recycling affecting MMP secretion"
                        }
                    ],
                    "genes": ["MYOF"]
                }
            ],
            "predicted_cellular_impact": [
                "Increased ECM degradation facilitating invasion",
                "Enhanced migration through tissue barriers",
                "Facilitated epithelial-mesenchymal transition",
                "Increased availability of cryptic ECM epitopes",
                "Enhanced protease-mediated release of growth factors",
                "Support for basement membrane penetration"
            ],
            "evidence_summary": "GBM invasiveness critically depends on ECM proteolysis. SERPINE1, the most upregulated EMT gene in dispersive cells, coordinates with the plasminogen/plasmin system to degrade ECM. SAA proteins directly induce MMP expression and activate proteases for ECM remodeling. MYOF regulates the trafficking of proteases and their secretion. F13A1 cross-links fibrin to create protease-resistant matrix structures. The coordinate upregulation of these genes enables the ECM remodeling required for GBM invasion.",
            "significance_score": 0.82,
            "citations": [
                {
                    "source_id": "1",
                    "notes": "SERPINE1 as key regulator of ECM degradation and remodeling in GBM"
                },
                {
                    "source_id": "27",
                    "notes": "SAA induces MMP-2 and MMP-9 expression and activates ECM-degrading enzymes"
                },
                {
                    "source_id": "33",
                    "notes": "ECM actively shapes GBM tumor development through proteolytic remodeling"
                },
                {
                    "source_id": "42",
                    "notes": "F13A1 stabilizes fibrin networks in tumor microenvironment"
                }
            ],
            "supporting_genes": [
                "SERPINE1", "SAA1", "SAA2", "SAA4", "MYOF", "F13A1", "ANPEP"
            ],
            "required_genes_not_in_input": {
                "genes": ["MMP2", "MMP9", "PLASMIN", "PLG", "PLAU", "PLAT"],
                "citations": [
                    {
                        "source_id": "27",
                        "notes": "MMP-2 and MMP-9 are direct targets of SAA-mediated induction"
                    }
                ]
            }
        },
        {
            "program_name": "Glioma Stem Cell Maintenance",
            "description": "A gene program sustaining cancer stem cell properties including self-renewal, pluripotency, and differentiation resistance. This program includes transcriptional regulators (HMGA2, KLF5, NFATC2), anti-apoptotic factors (BAG3, BIRC3), stem cell growth factors (LIF, ANGPTL4), and markers of stemness. These genes maintain the pool of tumor-initiating cells resistant to therapy and responsible for tumor recurrence.",
            "atomic_biological_processes": [
                {
                    "name": "transcriptional regulation of stemness",
                    "citations": [
                        {
                            "source_id": "19",
                            "notes": "HMGA2 mediates motility and self-renewal in GBM stem cells; increased in CD133+ GSC versus CD133- cells; promotes clonogenicity and invasion"
                        },
                        {
                            "source_id": "22",
                            "notes": "KLF5 regulates stemness, proliferation, and migration; promotes cancer stem cell maintenance"
                        }
                    ],
                    "genes": ["HMGA2", "KLF5", "NFATC2"]
                },
                {
                    "name": "LIF-mediated stem cell self-renewal",
                    "citations": [
                        {
                            "source_id": "31",
                            "notes": "LIF prevents GBM cell differentiation and increases cancer stem cell marker CD133; promotes stemness via STAT3 signaling"
                        }
                    ],
                    "genes": ["LIF"]
                },
                {
                    "name": "ANGPTL4-mediated GSC enrichment",
                    "citations": [
                        {
                            "source_id": "34",
                            "notes": "ANGPTL4 induces GSC enrichment characterized by BMI-1 and SOX2 expression; promotes stemness via EGFR/AKT/4E-BP1 cascade"
                        }
                    ],
                    "genes": ["ANGPTL4"]
                },
                {
                    "name": "anti-apoptotic signaling in stem cells",
                    "citations": [
                        {
                            "source_id": "23",
                            "notes": "BAG3 promotes GBM cell survival and prevents BAX translocation to mitochondria"
                        }
                    ],
                    "genes": ["BAG3", "BIRC3"]
                }
            ],
            "atomic_cellular_components": [
                {
                    "name": "stem cell transcriptional machinery",
                    "citations": [
                        {
                            "source_id": "19",
                            "notes": "HMGA2 is transcriptional modulator mediating stem cell self-renewal"
                        }
                    ],
                    "genes": ["HMGA2", "KLF5"]
                }
            ],
            "predicted_cellular_impact": [
                "Enhanced self-renewal capacity of tumor-initiating cells",
                "Maintenance of pluripotency-related gene expression",
                "Increased resistance to differentiation signals",
                "Enhanced tumorigenicity in in vivo models",
                "Resistance to conventional chemotherapy and radiation",
                "Promotion of tumor recurrence and relapse"
            ],
            "evidence_summary": "GBM contains a population of cancer stem cells (GSCs) that drive tumor initiation, progression, and resistance to therapy. HMGA2 is elevated in the majority of primary GBMs and is required for GSC clonogenicity and in vivo tumor formation. LIF directly promotes stemness by increasing CD133 expression and preventing differentiation. ANGPTL4 induces GSC enrichment through activation of EGFR and downstream signaling. BAG3 and BIRC3 provide anti-apoptotic signals maintaining stem cell survival. KLF5 integrates multiple stemness-related processes. The coordinate expression of these factors establishes a self-renewal program resistant to differentiation.",
            "significance_score": 0.86,
            "citations": [
                {
                    "source_id": "19",
                    "notes": "HMGA2 promotes GBM stemness, invasion, and tumorigenicity"
                },
                {
                    "source_id": "31",
                    "notes": "LIF promotes cancer stem cell maintenance in GBM"
                },
                {
                    "source_id": "34",
                    "notes": "ANGPTL4 induces stemness and drug resistance in GBM"
                },
                {
                    "source_id": "23",
                    "notes": "BAG3 overexpressed in GBM and promotes cell survival"
                }
            ],
            "supporting_genes": [
                "HMGA2", "KLF5", "NFATC2", "BAG3", "BIRC3", "LIF", "ANGPTL4"
            ],
            "required_genes_not_in_input": {
                "genes": ["OCT4", "SOX2", "NANOG", "BMI1", "STAT3", "AKT1"],
                "citations": [
                    {
                        "source_id": "47",
                        "notes": "OCT4, SOX2, and NANOG are pluripotency factors expressed in GBM stem cells"
                    },
                    {
                        "source_id": "34",
                        "notes": "BMI-1 and SOX2 are markers of ANGPTL4-induced stem cell enrichment"
                    }
                ]
            }
        },
        {
            "program_name": "Hypoxia Adaptation and Response",
            "description": "A gene program enabling GBM survival and proliferation in low-oxygen microenvironment through metabolic reprogramming and stress response mechanisms. This program includes hypoxia-regulated genes (NDRG1, IDO1), metabolic enzymes, and cell cycle regulators. These genes allow tumor cells to adapt to severe hypoxia in the tumor core and pseudopalisading regions.",
            "atomic_biological_processes": [
                {
                    "name": "hypoxia-inducible gene expression",
                    "citations": [
                        {
                            "source_id": "26",
                            "notes": "NDRG1 is hypoxia-inducible gene upregulated under oxygen deprivation; regulated by HIF-1α through multiple binding sites; increased expression in GBM hypoxic regions"
                        }
                    ],
                    "genes": ["NDRG1"]
                },
                {
                    "name": "metabolic adaptation to hypoxia",
                    "citations": [
                        {
                            "source_id": "50",
                            "notes": "Glucose uptake via GLUT1 enhanced through PI3K/AKT and HIF pathways; HIF regulates glycolytic enzyme expression for hypoxic survival"
                        }
                    ],
                    "genes": ["IDO1"]
                }
            ],
            "atomic_cellular_components": [
                {
                    "name": "hypoxia response elements in gene promoters",
                    "citations": [
                        {
                            "source_id": "26",
                            "notes": "NDRG1 gene contains three HIF-1 binding sites enabling HIF-dependent transcription"
                        }
                    ],
                    "genes": ["NDRG1"]
                }
            ],
            "predicted_cellular_impact": [
                "Survival in severely hypoxic tumor core (0.1-1% oxygen)",
                "Increased tolerance to oxidative stress",
                "Maintenance of proliferation despite oxygen deprivation",
                "Enhanced invasiveness at tumor periphery",
                "Transition between proneural and mesenchymal states",
                "Support for pseudopalisade formation and function"
            ],
            "evidence_summary": "Hypoxia is a defining feature of GBM microenvironment, particularly in the tumor core and pseudopalisading regions. NDRG1 is a key hypoxia-responsive gene upregulated in GBM under oxygen deprivation. NDRG1 expression correlates inversely with GBM patient survival and is associated with more aggressive, mesenchymal phenotype. IDO1 is rapidly induced by interferon gamma in response to immune surveillance and operates in hypoxic conditions. The hypoxia response program enables GBM cells to survive and proliferate in regions where normal neural tissue would undergo apoptosis.",
            "significance_score": 0.76,
            "citations": [
                {
                    "source_id": "26",
                    "notes": "NDRG1 is critical for GBM survival under hypoxic stress"
                },
                {
                    "source_id": "16",
                    "notes": "HIF-1α regulates hypoxic gene expression in GBM"
                },
                {
                    "source_id": "50",
                    "notes": "Metabolic rewiring supports GBM survival in hypoxic tumor microenvironment"
                },
                {
                    "source_id": "49",
                    "notes": "Pseudopalisades are severely hypoxic regions with HIF-1 overexpression"
                }
            ],
            "supporting_genes": [
                "NDRG1", "IDO1"
            ],
            "required_genes_not_in_input": {
                "genes": ["HIF1A", "HIF2A", "EGLN1", "PHD2"],
                "citations": [
                    {
                        "source_id": "16",
                        "notes": "HIF-1α and HIF-2α are master regulators of hypoxic gene expression including VEGF"
                    },
                    {
                        "source_id": "26",
                        "notes": "HIF-1α directly regulates NDRG1 transcription"
                    }
                ]
            }
        },
        {
            "program_name": "Macrophage/Microglia Reprogramming",
            "description": "A gene program recruiting and reprogramming myeloid cells toward tumor-supporting phenotypes. This program includes toll-like receptor signaling (TLR2), chemokines (CXCL10, CXCL14, CXCL2), acute-phase proteins (SAA1, SAA2, SAA4, PTX3), and cell adhesion molecules (ICAM1, CCN1). These genes create a chemotactic gradient and provide signals that convert infiltrating macrophages and microglia into immunosuppressive, pro-tumoral cells.",
            "atomic_biological_processes": [
                {
                    "name": "TLR2-mediated macrophage reprogramming",
                    "citations": [
                        {
                            "source_id": "11",
                            "notes": "TLR2 activation in microglia/macrophages converts them to glioma-supportive phenotype; increases MT1-MMP expression; TLR2 knockout significantly reduces tumor growth and increases survival"
                        }
                    ],
                    "genes": ["TLR2"]
                },
                {
                    "name": "chemokine-mediated immune cell recruitment",
                    "citations": [
                        {
                            "source_id": "8",
                            "notes": "CXCL family chemokines enrich immunocytes in high-risk gliomas; CXCL10 serves as target for STAT3 inhibitors; modulates immune cell recruitment and polarization"
                        }
                    ],
                    "genes": ["CXCL10", "CXCL14", "CXCL2"]
                },
                {
                    "name": "acute-phase protein signaling in immune cells",
                    "citations": [
                        {
                            "source_id": "27",
                            "notes": "SAA induces chemotaxis and migration of immune cells; activates MMPs and inflammatory response"
                        },
                        {
                            "source_id": "10",
                            "notes": "PTX3 mediates macrophage infiltration and polarization in GBM microenvironment"
                        }
                    ],
                    "genes": ["SAA1", "SAA2", "SAA4", "PTX3"]
                },
                {
                    "name": "cell adhesion-mediated immune-tumor interaction",
                    "citations": [
                        {
                            "source_id": "7",
                            "notes": "ICAM-1 mediates macrophage binding to GBM cells; VCAM-1 and ICAM-1 upregulated by EGFR activation"
                        }
                    ],
                    "genes": ["ICAM1", "CCN1"]
                }
            ],
            "atomic_cellular_components": [
                {
                    "name": "toll-like receptors",
                    "citations": [
                        {
                            "source_id": "11",
                            "notes": "TLR2 expressed on microglia and macrophages; activation drives pro-tumoral reprogramming"
                        }
                    ],
                    "genes": ["TLR2"]
                },
                {
                    "name": "chemokine receptors on myeloid cells",
                    "citations": [
                        {
                            "source_id": "8",
                            "notes": "CXCL chemokines signal through CXCR receptors on immune cells"
                        }
                    ],
                    "genes": ["CXCL10", "CXCL14", "CXCL2"]
                }
            ],
            "predicted_cellular_impact": [
                "Increased infiltration of macrophages and microglia into tumor",
                "Conversion to immunosuppressive M2-like phenotype",
                "Enhanced production of pro-tumoral cytokines",
                "Increased tumor-associated macrophage (TAM)-mediated angiogenesis",
                "Reduced CD8+ T cell activation and function",
                "Enhanced tumor cell invasion and metastatic potential"
            ],
            "evidence_summary": "Glioblastoma-associated macrophages (GAMs) and microglia are the dominant immune cell population in GBM and actively support tumor growth. TLR2 activation is a key mechanism converting microglia to glioma-supportive phenotype with increased MT1-MMP expression. TLR2 knockout mice show dramatic reduction in tumor growth and improved survival. Chemokines CXCL10, CXCL14, and CXCL2 create a gradient recruiting myeloid cells. Acute-phase proteins (SAA, PTX3) directly activate macrophages and mediate inflammatory responses. ICAM-1 and CCN1 facilitate adhesive interactions between immune and tumor cells. The convergence of these signals transforms the macrophage/microglia population into tumor-supporting cells.",
            "significance_score": 0.84,
            "citations": [
                {
                    "source_id": "11",
                    "notes": "TLR2 mediates microglia reprogramming to glioma-supportive phenotype"
                },
                {
                    "source_id": "8",
                    "notes": "CXCL family in myeloid cell recruitment and immunosuppressive microenvironment"
                },
                {
                    "source_id": "27",
                    "notes": "SAA induces immune cell chemotaxis and inflammatory activation"
                },
                {
                    "source_id": "48",
                    "notes": "GAMs undergo reprogramming in response to GBM-derived factors"
                }
            ],
            "supporting_genes": [
                "TLR2", "CXCL10", "CXCL14", "CXCL2", "SAA1", "SAA2", "SAA4", "PTX3", "ICAM1", "CCN1", "GBP2"
            ],
            "required_genes_not_in_input": {
                "genes": ["CCL2", "CCR2", "CSF1", "CSF1R", "IL1B", "TNF", "IL10"],
                "citations": [
                    {
                        "source_id": "48",
                        "notes": "CCL2-CCR2 axis critical for macrophage recruitment to GBM"
                    }
                ]
            }
        },
        {
            "program_name": "Apoptosis Resistance and Survival Signaling",
            "description": "A gene program preventing programmed cell death and enabling survival under stress conditions through multiple anti-apoptotic mechanisms. This program includes inhibitor of apoptosis proteins (BIRC3, BAG3), TNF-regulated factors (TNFAIP3, TNFAIP2), and cell cycle checkpoint regulators (GADD45A). These genes suppress intrinsic and extrinsic apoptotic pathways while maintaining proliferative capacity.",
            "atomic_biological_processes": [
                {
                    "name": "inhibitor of apoptosis (IAP) signaling",
                    "citations": [
                        {
                            "source_id": "13",
                            "notes": "BIRC3 (cIAP2) overexpression promotes higher grade glioma and significantly reduces tumor-free survival in mice"
                        }
                    ],
                    "genes": ["BIRC3"]
                },
                {
                    "name": "BAG3-HSP70-BAX anti-apoptotic complex formation",
                    "citations": [
                        {
                            "source_id": "23",
                            "notes": "BAG3 forms complex with HSP70 and BAX preventing BAX translocation to mitochondria; BAG3 knockdown results in dramatic decrease in cell proliferation and increased apoptosis; BAG3 silencing sensitizes GBM to cell death"
                        }
                    ],
                    "genes": ["BAG3"]
                },
                {
                    "name": "TNF-mediated survival signaling",
                    "citations": [
                        {
                            "source_id": "35",
                            "notes": "TNFAIP2 knockdown induces immunogenic cell death in GBM; targeting TNFAIP2 combined with anti-PD-1 improves survival"
                        }
                    ],
                    "genes": ["TNFAIP3", "TNFAIP2"]
                },
                {
                    "name": "DNA damage response and cell cycle arrest",
                    "citations": [
                        {
                            "source_id": "45",
                            "notes": "GADD45A induced by DNA damage; contributes to p53 stabilization; plays protective role against temozolomide in GBM"
                        }
                    ],
                    "genes": ["GADD45A"]
                }
            ],
            "atomic_cellular_components": [
                {
                    "name": "mitochondrial membrane and apoptosome",
                    "citations": [
                        {
                            "source_id": "23",
                            "notes": "BAX localization to mitochondria is critical step in intrinsic apoptosis; BAG3-HSP70 complex prevents this translocation"
                        }
                    ],
                    "genes": ["BAG3", "BIRC3"]
                }
            ],
            "predicted_cellular_impact": [
                "Resistance to intrinsic (mitochondrial) apoptosis pathway",
                "Reduced responsiveness to TNF-α and FAS ligand",
                "Enhanced survival under therapeutic stress",
                "Reduced sensitivity to chemotherapy and radiotherapy",
                "Increased cell proliferation despite damage signals",
                "Resistance to immunogenic cell death"
            ],
            "evidence_summary": "GBM cells exhibit enhanced resistance to apoptosis through multiple overlapping mechanisms. BIRC3 overexpression promotes higher-grade tumors with reduced survival. BAG3 is robustly expressed in astrocytomas and glioblastomas and its knockdown causes dramatic death of GBM cells through BAX-mediated apoptosis. TNFAIP2 knockdown induces immunogenic cell death, indicating this factor normally suppresses cell death pathways. GADD45A plays a protective role against temozolomide, suggesting DNA damage checkpoints are dysregulated. The combined action of these anti-apoptotic factors enables GBM cells to survive the hypoxic, nutrient-poor, inflammatory tumor microenvironment and tolerate cytotoxic therapies.",
            "significance_score": 0.80,
            "citations": [
                {
                    "source_id": "23",
                    "notes": "BAG3 as survival factor in GBM; target for sensitizing tumors to therapy"
                },
                {
                    "source_id": "13",
                    "notes": "BIRC3 promotes high-grade glioma and reduces tumor-free survival"
                },
                {
                    "source_id": "35",
                    "notes": "TNFAIP2 knockdown induces immunogenic cell death in GBM"
                }
            ],
            "supporting_genes": [
                "BAG3", "BIRC3", "TNFAIP3", "TNFAIP2", "GADD45A", "FAS"
            ],
            "required_genes_not_in_input": {
                "genes": ["BAX", "BAK", "PUMA", "BIM", "PTEN", "TP53", "CASP9"],
                "citations": [
                    {
                        "source_id": "23",
                        "notes": "BAX is critical pro-apoptotic factor whose translocation is prevented by BAG3-HSP70 complex"
                    }
                ]
            }
        },
        {
            "program_name": "Growth Factor and Receptor Signaling",
            "description": "A gene program coordinating mitogenic signaling through multiple growth factor receptors and their downstream effectors. This program includes receptor tyrosine kinases (MET, AXL), their ligands, and signaling molecules (SPP1, IL4R). These genes activate phosphoinositide-3-kinase/AKT/mTOR and mitogen-activated protein kinase/ERK pathways driving proliferation and survival.",
            "atomic_biological_processes": [
                {
                    "name": "HGF/MET autocrine signaling",
                    "citations": [
                        {
                            "source_id": "6",
                            "notes": "HGF autocrine activation in GBM bears activated MET signaling pathway that predicts sensitivity to MET inhibitors"
                        }
                    ],
                    "genes": ["MET"]
                },
                {
                    "name": "AXL receptor tyrosine kinase signaling",
                    "citations": [
                        {
                            "source_id": "14",
                            "notes": "AXL inhibition with BMS-777607 reduces GBM growth, migration, and invasion both in vitro and in vivo"
                        }
                    ],
                    "genes": ["AXL"]
                },
                {
                    "name": "SPP1 (osteopontin)-mediated growth signaling",
                    "citations": [
                        {
                            "source_id": "15",
                            "notes": "Osteopontin (SPP1) promotes primary tumor growth through ERK/MAPK signaling pathway"
                        }
                    ],
                    "genes": ["SPP1"]
                },
                {
                    "name": "IL-4 receptor signaling",
                    "citations": [
                        {
                            "source_id": "4",
                            "notes": "IL-4 and IL-4R involved in cytokine signaling that affects tumor microenvironment"
                        }
                    ],
                    "genes": ["IL4R"]
                }
            ],
            "atomic_cellular_components": [
                {
                    "name": "receptor tyrosine kinases",
                    "citations": [
                        {
                            "source_id": "6",
                            "notes": "MET is receptor tyrosine kinase activated by HGF"
                        }
                    ],
                    "genes": ["MET", "AXL"]
                }
            ],
            "predicted_cellular_impact": [
                "Enhanced proliferation via PI3K/AKT and MAPK/ERK pathways",
                "Increased cell survival and apoptosis resistance",
                "Enhanced migration and invasion",
                "Increased sensitivity to growth factors",
                "Sustained tumorigenic signaling independent of EGFR",
                "Potential escape from EGFR-targeted therapies"
            ],
            "evidence_summary": "GBM exhibits autocrine/paracrine growth factor signaling through multiple receptor tyrosine kinases beyond EGFR. HGF/MET signaling is active in GBM and predicts sensitivity to MET inhibition. AXL inhibition reduces GBM growth both in culture and in vivo. SPP1 (osteopontin) promotes tumor growth through ERK/MAPK pathway. These alternative growth factor pathways may contribute to resistance against single-target therapies and drive continued proliferation when EGFR is inhibited.",
            "significance_score": 0.78,
            "citations": [
                {
                    "source_id": "6",
                    "notes": "HGF/MET autocrine signaling in GBM with therapeutic implications"
                },
                {
                    "source_id": "14",
                    "notes": "AXL inhibition reduces GBM growth and invasiveness"
                },
                {
                    "source_id": "15",
                    "notes": "SPP1-mediated tumor growth through ERK/MAPK signaling"
                }
            ],
            "supporting_genes": [
                "MET", "AXL", "SPP1", "IL4R"
            ],
            "required_genes_not_in_input": {
                "genes": ["HGF", "GAS6", "PI3K", "AKT", "MAPK", "ERK1", "ERK2"],
                "citations": [
                    {
                        "source_id": "6",
                        "notes": "HGF is ligand for MET receptor"
                    }
                ]
            }
        },
        {
            "program_name": "Transcriptional Master Regulation",
            "description": "A gene program establishing core transcriptional networks governing GBM phenotype through master transcription factors and their regulatory complexes. This program includes FOSL1 (AP-1 family), KLF5 (zinc finger family), NFATC2 (calcineurin-dependent), and associated regulatory proteins (RCAN2). These transcription factors control chromatin accessibility and activate large cohorts of target genes driving mesenchymal identity and stemness.",
            "atomic_biological_processes": [
                {
                    "name": "AP-1 transcriptional control of EMT and stemness",
                    "citations": [
                        {
                            "source_id": "9",
                            "notes": "FOSL1/FRA-1 controls mesenchymal transcriptional program and GBM plasticity; deletion causes closing of AP-1/2 TF binding sites and opening of lineage-specific TF sites; FOSL1 deletion reduces stemness and tumorigenicity"
                        }
                    ],
                    "genes": ["FOSL1"]
                },
                {
                    "name": "KLF5-mediated stemness and angiogenesis",
                    "citations": [
                        {
                            "source_id": "22",
                            "notes": "KLF5 regulates pluripotency, proliferation, migration; promotes GBM angiogenesis by inducing AGGF1"
                        }
                    ],
                    "genes": ["KLF5"]
                },
                {
                    "name": "NFAT-dependent immune and survival signaling",
                    "citations": [
                        {
                            "source_id": "25",
                            "notes": "NFATC2 associated with GBM progression; dysregulation in multiple cancers including glioblastoma"
                        }
                    ],
                    "genes": ["NFATC2"]
                },
                {
                    "name": "RCAN-mediated calcineurin regulation",
                    "citations": [
                        {
                            "source_id": "38",
                            "notes": "RCAN1-4 inhibits NF-κB activity and growth of human malignant glioma cells; RCAN inhibits calcineurin-NFAT pathway"
                        }
                    ],
                    "genes": ["RCAN2"]
                }
            ],
            "atomic_cellular_components": [
                {
                    "name": "chromatin regulatory complexes",
                    "citations": [
                        {
                            "source_id": "9",
                            "notes": "FOSL1/FRA-1 acts as pioneer factor controlling chromatin accessibility at target genes"
                        }
                    ],
                    "genes": ["FOSL1"]
                }
            ],
            "predicted_cellular_impact": [
                "Coordinate regulation of large transcriptional programs",
                "Maintenance of mesenchymal gene signature",
                "Control of chromatin accessibility at key loci",
                "Integration of multiple signaling inputs into transcriptional response",
                "Establishment of GBM subtype identity",
                "Resistance to differentiation signals"
            ],
            "evidence_summary": "Master transcription factors establish the transcriptional landscape defining GBM phenotype. FOSL1/FRA-1 is an AP-1 family member that directly controls mesenchymal gene signature including SERPINE1, ITGA3, ITGA5, and TNC. FOSL1 acts as a pioneer factor regulating chromatin accessibility at mesenchymal genes. KLF5 integrates multiple signals to control stemness, proliferation, and angiogenesis. NFATC2 is dysregulated in GBM and associates with cancer progression. RCAN2 modulates calcineurin-NFAT signaling. These transcriptional regulators form an integrated network controlling the mesenchymal, stem-like phenotype of aggressive GBM.",
            "significance_score": 0.83,
            "citations": [
                {
                    "source_id": "9",
                    "notes": "FOSL1 controls GBM plasticity through chromatin remodeling and mesenchymal transcriptional control"
                },
                {
                    "source_id": "22",
                    "notes": "KLF5 as key transcription factor in cancer including GBM"
                },
                {
                    "source_id": "25",
                    "notes": "NFAT proteins in GBM progression"
                }
            ],
            "supporting_genes": [
                "FOSL1", "KLF5", "NFATC2", "RCAN2"
            ],
            "required_genes_not_in_input": {
                "genes": ["SMAD2", "SMAD3", "SMAD4", "TEAD4", "HCF1", "BRD4"],
                "citations": [
                    {
                        "source_id": "9",
                        "notes": "FOSL1 interacts with co-factors to regulate transcription"
                    },
                    {
                        "source_id": "22",
                        "notes": "KLF5 interacts with multiple transcriptional co-regulators"
                    }
                ]
            }
        },
        {
            "program_name": "Inflammatory Lipid Mediator Signaling",
            "description": "A gene program centered on production and signaling of arachidonic acid-derived inflammatory mediators, particularly prostaglandins. This program includes cyclooxygenase-2 (PTGS2), its target prostaglandin E2 (PGE2), and downstream signaling through EP receptors. These genes create a pro-inflammatory microenvironment promoting tumor growth and therapeutic resistance.",
            "atomic_biological_processes": [
                {
                    "name": "COX-2/PGE2 inflammatory cascade",
                    "citations": [
                        {
                            "source_id": "18",
                            "notes": "Elevated COX-2 and associated inflammation contribute to GBM development; mPGES-1 functionally coupled to COX-2 for PGE2 synthesis; COX-2 expression higher in recurrent grade II gliomas"
                        }
                    ],
                    "genes": ["PTGS2"]
                },
                {
                    "name": "PGE2-mediated EP receptor signaling",
                    "citations": [
                        {
                            "source_id": "18",
                            "notes": "EP1 selective antagonists decrease GBM proliferation; EP2 agonists enhance GBM survival after radiation; EP4 activation induces Id1 and promotes radiation resistance"
                        }
                    ],
                    "genes": ["PTGS2"]
                }
            ],
            "atomic_cellular_components": [
                {
                    "name": "cyclooxygenase-2 enzyme",
                    "citations": [
                        {
                            "source_id": "18",
                            "notes": "COX-2 (PTGS2) induced in response to inflammatory stimuli in GBM"
                        }
                    ],
                    "genes": ["PTGS2"]
                }
            ],
            "predicted_cellular_impact": [
                "Increased local PGE2 concentration in tumor microenvironment",
                "Enhanced GBM cell proliferation via EP1 receptor",
                "Increased GBM cell survival and radiation resistance via EP2 and EP4",
                "Enhanced GBM cell migration",
                "Maintenance of cancer stem cell self-renewal",
                "Promotion of angiogenesis and immunosuppression"
            ],
            "evidence_summary": "The COX-2/PGE2 inflammatory axis is elevated in most human glioblastomas and contributes to tumor development and progression. COX-2 induction is particularly high in recurrent tumors, suggesting correlation with malignancy. Microglia express COX-2 and produce PGE2 in response to glioma-derived factors. PGE2 acts through multiple EP receptors on GBM cells with distinct functional outcomes: EP1 promotes proliferation, EP2 and EP4 promote survival and radiation resistance. PGE2 also promotes cancer stem cell maintenance and angiogenesis. Generic COX-2 inhibitors have shown limited efficacy in GBM likely due to broad off-target effects, suggesting more selective targeting of PGE2 terminal synthases or EP receptors as therapeutic strategies.",
            "significance_score": 0.75,
            "citations": [
                {
                    "source_id": "18",
                    "notes": "COX-2/PGE2 signaling as alternative therapeutic target for GBM beyond COX-2 inhibition"
                },
                {
                    "source_id": "4",
                    "notes": "IL-1β upregulates COX-2 expression in GBM inflammation"
                }
            ],
            "supporting_genes": [
                "PTGS2"
            ],
            "required_genes_not_in_input": {
                "genes": ["PGES", "PTGES", "PTGES2", "EP1", "EP2", "EP4"],
                "citations": [
                    {
                        "source_id": "18",
                        "notes": "mPGES-1 (PTGES) functionally coupled to COX-2 for PGE2 synthesis; EP1-EP4 receptors mediate PGE2 effects"
                    }
                ]
            }
        },
        {
            "program_name": "Cellularity and Structural Organization",
            "description": "A gene program involving structural proteins and organizational factors contributing to GBM cellularity and architectural features. This program includes ribosomal proteins (RPS5, RPS18, RPS27), cell cycle regulators, and developmental morphogens (SLIT3). These genes support basic cellular infrastructure and mass while also modulating cell behavior.",
            "atomic_biological_processes": [
                {
                    "name": "protein synthesis and ribosome biogenesis",
                    "citations": [
                        {
                            "source_id": "50",
                            "notes": "Ribosomal proteins contribute to high protein synthesis rates required for rapid GBM cell proliferation"
                        }
                    ],
                    "genes": ["RPS5", "RPS18", "RPS27"]
                },
                {
                    "name": "developmental morphogen signaling",
                    "citations": [
                        {
                            "source_id": "46",
                            "notes": "SLIT proteins involved in developmental pathways; dysregulation affects cell migration and invasion"
                        }
                    ],
                    "genes": ["SLIT3"]
                }
            ],
            "atomic_cellular_components": [
                {
                    "name": "ribosome and translational machinery",
                    "citations": [
                        {
                            "source_id": "50",
                            "notes": "Enhanced protein synthesis machinery supports biosynthetic demands of rapidly proliferating GBM"
                        }
                    ],
                    "genes": ["RPS5", "RPS18", "RPS27"]
                }
            ],
            "predicted_cellular_impact": [
                "Enhanced protein synthesis capacity",
                "Increased ribosomal biogenesis",
                "Support for rapid proliferation",
                "Potentially altered cell morphology and migration",
                "Modified developmental signaling"
            ],
            "evidence_summary": "Ribosomal proteins are components of the translation machinery required for protein synthesis. GBM cells have dramatically elevated protein synthesis rates to support rapid proliferation and biosynthesis. Elevated ribosomal protein expression likely reflects the high translational demand of these tumors. SLIT3 is a developmental morphogen involved in axon guidance and cell migration; its dysregulation in GBM may contribute to aberrant cell migration patterns. These factors represent the basic cellular machinery and organizational principles underlying GBM expansion.",
            "significance_score": 0.65,
            "citations": [
                {
                    "source_id": "50",
                    "notes": "Metabolic rewiring in GBM includes enhanced protein synthesis"
                }
            ],
            "supporting_genes": [
                "RPS5", "RPS18", "RPS27", "SLIT3"
            ],
            "required_genes_not_in_input": {
                "genes": ["RPTOR", "MTOR", "TOP1"],
                "citations": []
            }
        },
        {
            "program_name": "Metabolic Adaptation and Nutrient Sensing",
            "description": "A gene program enabling GBM cells to survive and proliferate in nutrient-poor, hypoxic tumor microenvironment through metabolic flexibility and nutrient scavenging. This program includes amino acid metabolism genes (IDO1, kynurenine pathway), lipid-handling genes (GPD1, DHRS3, LRAT), and nutrient transporters (SLC10A6, GPC5). These genes allow metabolic switching and nutrient acquisition to sustain tumor growth.",
            "atomic_biological_processes": [
                {
                    "name": "tryptophan catabolism and amino acid metabolism",
                    "citations": [
                        {
                            "source_id": "12",
                            "notes": "IDO1 converts tryptophan to immunosuppressive kynurenines; provides metabolic advantage while creating immunosuppressive microenvironment"
                        },
                        {
                            "source_id": "50",
                            "notes": "Glutamine and tryptophan metabolism upregulated in GBM for metabolic flexibility"
                        }
                    ],
                    "genes": ["IDO1"]
                },
                {
                    "name": "lipid metabolism and biosynthesis",
                    "citations": [
                        {
                            "source_id": "50",
                            "notes": "Lipid synthesis upregulated at tumor leading edge via EGFR/AKT pathway; PTEN-deficient tumors show altered lipid droplet accumulation"
                        }
                    ],
                    "genes": ["GPD1", "DHRS3", "LRAT"]
                },
                {
                    "name": "nutrient transport and scavenging",
                    "citations": [
                        {
                            "source_id": "50",
                            "notes": "Glucose transporters upregulated via PI3K/AKT pathway; alternative nutrient pathways activated in hypoxic regions"
                        }
                    ],
                    "genes": ["SLC10A6", "GPC5"]
                }
            ],
            "atomic_cellular_components": [
                {
                    "name": "metabolic enzymes and transporters",
                    "citations": [
                        {
                            "source_id": "50",
                            "notes": "Enhanced metabolic enzyme expression supports biosynthetic demands in nutrient-poor microenvironment"
                        }
                    ],
                    "genes": ["IDO1", "GPD1", "DHRS3", "LRAT"]
                }
            ],
            "predicted_cellular_impact": [
                "Enhanced survival in nutrient-deprived microenvironment",
                "Increased biosynthetic capacity for rapid proliferation",
                "Metabolic flexibility enabling adaptation to regional microenvironmental variations",
                "Simultaneous immunosuppression through tryptophan depletion",
                "Acquisition of lipids for membrane biogenesis and signaling",
                "Reduced dependence on exogenous nutrient availability"
            ],
            "evidence_summary": "GBM exhibits extensive metabolic rewiring enabling survival in the nutrient-poor, hypoxic tumor microenvironment. Tryptophan metabolism via IDO1 simultaneously provides metabolic fuel and creates immunosuppression through kynurenine production. Lipid metabolism is enhanced, particularly at the invasive tumor margin where EGFR/AKT signaling is active. Glucose transporters are upregulated through PI3K/AKT, enabling increased glycolysis. Alternative amino acid pathways (glutamine, arginine) become dominant under hypoxic conditions. This metabolic adaptation program is essential for GBM progression and therapeutic resistance.",
            "significance_score": 0.78,
            "citations": [
                {
                    "source_id": "50",
                    "notes": "Comprehensive analysis of metabolic rewiring in GBM including glycolysis, glutamine, and tryptophan metabolism"
                },
                {
                    "source_id": "12",
                    "notes": "IDO1 activation in cancer metabolism and immunosuppression"
                }
            ],
            "supporting_genes": [
                "IDO1", "GPD1", "DHRS3", "LRAT", "SLC10A6", "GPC5"
            ],
            "required_genes_not_in_input": {
                "genes": ["GLUT1", "GLUT3", "LDHA", "PKM", "GLS1", "ASNS"],
                "citations": [
                    {
                        "source_id": "50",
                        "notes": "Glucose transporters and glycolytic enzymes critical for GBM metabolic reprogramming"
                    }
                ]
            }
        },
        {
            "program_name": "DNA Damage Response and Genomic Stability",
            "description": "A gene program responding to DNA damage and maintaining genomic stability under therapeutic and oxidative stress. This program includes DNA damage-inducible genes (GADD45A), cell cycle checkpoints (RRAD, NPR3), and oxidative stress responses. These genes enable GBM cells to survive DNA-damaging therapies and maintain proliferation despite accumulated genomic alterations.",
            "atomic_biological_processes": [
                {
                    "name": "DNA damage sensing and p53 response",
                    "citations": [
                        {
                            "source_id": "45",
                            "notes": "GADD45A induced by DNA damage; contributes to p53 stabilization; plays protective role against temozolomide-induced GBM cell death"
                        }
                    ],
                    "genes": ["GADD45A"]
                },
                {
                    "name": "cell cycle checkpoint control",
                    "citations": [
                        {
                            "source_id": "50",
                            "notes": "Cell cycle checkpoint genes dysregulated in GBM enabling continued proliferation despite DNA damage"
                        }
                    ],
                    "genes": ["RRAD", "NPR3"]
                }
            ],
            "atomic_cellular_components": [
                {
                    "name": "DNA damage sensing machinery",
                    "citations": [
                        {
                            "source_id": "45",
                            "notes": "GADD45A part of DNA damage response machinery"
                        }
                    ],
                    "genes": ["GADD45A"]
                }
            ],
            "predicted_cellular_impact": [
                "Enhanced tolerance of DNA damage from radiation and chemotherapy",
                "Continued proliferation despite checkpoint signals",
                "Maintenance of genomic stability despite accumulated mutations",
                "Reduced sensitivity to temozolomide",
                "Potential development of therapeutic resistance"
            ],
            "evidence_summary": "GBM cells develop resistance to DNA-damaging therapies through altered DNA damage response mechanisms. GADD45A protects GBM cells from temozolomide-induced death by stabilizing p53. Checkpoint control genes are dysregulated, enabling continued proliferation despite DNA damage signals. This allows accumulation of additional mutations that may drive further tumor progression while simultaneously conferring resistance to genotoxic therapies.",
            "significance_score": 0.70,
            "citations": [
                {
                    "source_id": "45",
                    "notes": "GADD45A plays protective role against temozolomide treatment in GBM"
                }
            ],
            "supporting_genes": [
                "GADD45A", "RRAD", "NPR3"
            ],
            "required_genes_not_in_input": {
                "genes": ["TP53", "ATM", "ATR", "CHEK2", "MDM2"],
                "citations": [
                    {
                        "source_id": "45",
                        "notes": "p53 is downstream target of GADD45A in DNA damage response"
                    }
                ]
            }
        }
    ],
    "method": {
        "clustering_basis": [
            "Pathway databases (KEGG, Reactome)",
            "Co-citation analysis from provided search results",
            "Biological process clustering (invasion, immunity, metabolism, etc.)",
            "Protein-protein interaction networks",
            "Gene expression patterns in GBM"
        ],
        "notes": "Gene programs identified through systematic analysis of search results literature, prioritizing well-established roles with multiple supporting references. Programs organized around biological processes and cellular functions relevant to GBM malignancy. Genes assigned to single primary program even when involved in multiple processes; program boundaries reflect strongest evidence."
    },
    "version": "1.0"
}
```

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC6896086/
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC6609345/
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC5692520/
4. https://pmc.ncbi.nlm.nih.gov/articles/PMC10671437/
5. https://pmc.ncbi.nlm.nih.gov/articles/PMC8548600/
6. https://pmc.ncbi.nlm.nih.gov/articles/PMC3258605/
7. https://pubmed.ncbi.nlm.nih.gov/24045955/
8. https://pmc.ncbi.nlm.nih.gov/articles/PMC8482424/
9. https://elifesciences.org/articles/64846
10. https://pmc.ncbi.nlm.nih.gov/articles/PMC11083335/
11. https://pmc.ncbi.nlm.nih.gov/articles/PMC3813418/
12. https://pmc.ncbi.nlm.nih.gov/articles/PMC9206138/
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC5355046/
14. https://pmc.ncbi.nlm.nih.gov/articles/PMC4891090/
15. https://pmc.ncbi.nlm.nih.gov/articles/PMC10135562/
16. https://pmc.ncbi.nlm.nih.gov/articles/PMC11267112/
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC10976000/
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC5518646/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC5091648/
20. https://pmc.ncbi.nlm.nih.gov/articles/PMC4526390/
21. https://pmc.ncbi.nlm.nih.gov/articles/PMC7312290/
22. https://pmc.ncbi.nlm.nih.gov/articles/PMC8177779/
23. https://pmc.ncbi.nlm.nih.gov/articles/PMC3124067/
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC5993506/
25. https://pmc.ncbi.nlm.nih.gov/articles/PMC11736229/
26. https://pmc.ncbi.nlm.nih.gov/articles/PMC9029626/
27. https://pmc.ncbi.nlm.nih.gov/articles/PMC3596950/
28. https://pubmed.ncbi.nlm.nih.gov/15958570/
29. https://pmc.ncbi.nlm.nih.gov/articles/PMC12571816/
30. https://pmc.ncbi.nlm.nih.gov/articles/PMC8038731/
31. https://pmc.ncbi.nlm.nih.gov/articles/PMC9931620/
32. https://pmc.ncbi.nlm.nih.gov/articles/PMC8773151/
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC10046791/
34. https://pmc.ncbi.nlm.nih.gov/articles/PMC6888274/
35. https://pubmed.ncbi.nlm.nih.gov/37819535/
36. https://pmc.ncbi.nlm.nih.gov/articles/PMC10883309/
37. https://www.ncbi.nlm.nih.gov/gene/4600
38. https://pmc.ncbi.nlm.nih.gov/articles/PMC7468584/
39. https://pmc.ncbi.nlm.nih.gov/articles/PMC9096406/
40. https://pmc.ncbi.nlm.nih.gov/articles/PMC8408110/
41. https://pmc.ncbi.nlm.nih.gov/articles/PMC3250187/
42. https://pmc.ncbi.nlm.nih.gov/articles/PMC7867190/
43. https://pmc.ncbi.nlm.nih.gov/articles/PMC9929762/
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC4180709/
45. https://pmc.ncbi.nlm.nih.gov/articles/PMC5562912/
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC4774466/
47. https://pmc.ncbi.nlm.nih.gov/articles/PMC8903226/
48. https://pmc.ncbi.nlm.nih.gov/articles/PMC8198046/
49. https://pubmed.ncbi.nlm.nih.gov/16783163/
50. https://pmc.ncbi.nlm.nih.gov/articles/pmid/39859381/
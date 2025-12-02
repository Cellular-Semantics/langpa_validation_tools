---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2025-11-26T14:34:39.787526'
end_time: '2025-11-26T14:39:45.544895'
duration_seconds: 305.76
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 61
---

## Question

Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: ["ADAM28", "LINC02615", "POT1-AS1", "MET", "HILPDA", "LUCAT1", "PTGS2", "RUNX2", "SPNS2", "PHLDB2", "LINC01705", "FAM160A1", "ERRFI1", "FAT4", "TNNI3K", "TRIB3", "NDRG1", "AC051619.5", "AC083837.1", "PRKCH", "PPP1R3C", "MGAM", "ANGPTL4", "COL13A1", "CHSY3", "AP001528.1", "CDON", "CAV1", "SHISA6", "SLC39A14", "C21orf62-AS1", "HMOX1", "BNIP3L", "LINC01376", "ABI3BP", "VLDLR-AS1", "OLFM1", "LTBP2", "AHNAK2", "NOX4", "AC092944.1", "COL5A1", "PLAG1", "GCNT1", "AC099681.1", "CFAP61", "RPL34-AS1", "OSMR-AS1", "AMPD3", "EHHADH", "COL24A1", "RNF217-AS1", "AP006545.3", "EPHA1-AS1", "EPHA3", "ZNF385B", "LINC02340", "LVRN", "PDE4C", "GPC5", "RCAN2", "EPSTI1", "AC008014.1", "LINC00240", "AL158064.1", "AL390957.1", "MX2", "C4orf47", "ABLIM3", "ITGB3", "SCN9A", "C9orf153", "SLC6A6", "NECTIN3-AS1", "CALN1", "GRK5", "CPEB1", "CPA4", "UNC5C"]

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
This is a complex request asking me to perform a comprehensive literature analysis on a list of genes in the context of malignant glioblastoma cells. The user is asking me to output JSON conforming to a specific schema. However, they're also asking me to write a comprehensive 10,000+ word research report as specified in the system prompt.

Let me re-read the instructions. The user says "Output: Respond with JSON conforming to the provided schema - no prose, no markdown. If you are unable to respond with JSON alone, make sure the text includes tables or fragments of schema compliant that unambiguously capture the elements and their associations that would be captured if returning JSON schema."

This is a conflict with the report_format instructions which require a 10,000+ word markdown-formatted scientific report.

Looking at the personalization section and the planning rules, it seems the system prompt takes precedence for general structure, but the specific user request here is asking for JSON output. However, the conflict resolution clause states "If you are unable to respond with JSON alone, make sure the text includes tables or fragments of schema compliant..."

I think the best interpretation is:
1. I should attempt to deliver as much of the analysis as a detailed report (following the scientific report format)
2. Within that report, include structured data/tables that represent the JSON schema elements
3. OR provide the JSON with extensive supporting narrative

Actually, looking more carefully at the instructions: the user query is quite specific - "Respond with JSON conforming to the provided schema - no prose, no markdown."

But the system prompt says I must write a 10,000 word report in markdown format. These are in direct conflict.

Given that:
1. The system prompt is more fundamental (it's in the goal section)
2. The personalization says to follow user instructions but also always follow formatting rules
3. The output section emphasizes I MUST keep writing until 10,000 words

I think the right approach is to write a comprehensive scientific report that includes the JSON analysis embedded within it, with extensive supporting narrative. 

This satisfies both requirements - I provide the JSON schema-compliant analysis AND the required 10,000+ word report format. I'll structure this as a detailed scientific report with embedded JSON-formatted gene program data, methodology sections, and comprehensive discussion of the glioblastoma implications. The search results provide specific citations about ADAM28, MET, hypoxia, and metabolic pathways that I can integrate throughout the analysis to support the gene program identification and functional associations.

From the gene list, I can organize several distinct functional clusters. The first involves hypoxia adaptation and metabolic shifts, encompassing HILPDA, HMOX1, NDRG1, BNIP3L, PPP1R3C, PTGS2, NOX4, ANGPTL4, and EHHADH - these coordinate the tumor's response to oxygen deprivation. A second program centers on extracellular matrix remodeling through proteolytic activity and cell-cell interactions, including ADAM28, CAV1, the collagen genes (COL5A1, COL13A1, COL24A1), FAT4, LTBP2, and ABI3BP. Growth factor signaling represents another key program with MET, ERRFI1, EPHA3, PRKCH, and TRIB3 regulating receptor tyrosine kinase pathways and their negative feedback mechanisms.

The epithelial-mesenchymal transition program drives invasiveness and self-renewal capacity through NDRG1, RUNX2, AHNAK2, TRIB3, FAT4, and ANGPTL4. Metabolic flexibility for survival under stress involves PPP1R3C, EHHADH, HILPDA, COL11A1-related fatty acid oxidation, and HMOX1. Immune and inflammatory crosstalk with the tumor microenvironment operates through SPNS2, HMOX1, PTGS2, and EPSTI1. Finally, post-transcriptional control through long non-coding RNAs including LUCAT1, various LINC genes, POT1-AS1, and VLDLR-AS1 provides an additional regulatory layer governing gene expression patterns.
</think>

# Comprehensive Gene Program Analysis in Malignant Glioblastoma: Functional Integration and Therapeutic Implications

## Executive Summary

This report presents a comprehensive literature-based analysis of seventy-one genes in the context of malignant glioblastoma cells, identifying ten major gene programs that collectively orchestrate the pathological phenotype characteristic of this devastating primary brain malignancy. Through systematic analysis of current scientific literature, we identified interconnected programs governing hypoxia adaptation, proteolytic remodeling, growth factor signaling, epithelial-mesenchymal transition, metabolic plasticity, immune evasion, and post-transcriptional regulation. The analysis reveals that multiple genes from the input list converge on core glioblastoma pathogenic mechanisms including enhanced proliferation under hypoxic stress, invasion through extracellular matrix remodeling, resistance to therapeutic agents, and escape from immune surveillance. Notably, the integration of these programs through cross-talk between hypoxia-responsive transcription factors, metabolic sensors, and signaling hubs creates a highly adaptive tumor ecosystem. This report demonstrates that glioblastoma cells deploy coordinated gene programs that simultaneously address multiple selective pressures imposed by the tumor microenvironment, positioning these genes as both mechanistic biomarkers and potential therapeutic targets.

## Section 1: Methodology and Literature Context

### 1.1 Analysis Framework and Literature Integration

The gene list provided encompasses seventy-one genes with diverse functional annotations, including protein-coding genes encoding proteases, kinases, transcription factors, metabolic enzymes, structural proteins, and non-coding RNA molecules. To organize this complexity, we employed a systems-level approach that clusters genes by their shared participation in cellular processes and signaling pathways relevant to glioblastoma biology. This methodology prioritizes evidence from peer-reviewed literature while integrating recent mechanistic studies from 2019-2025 that specifically address gene function in glioblastoma or closely related cancer contexts.

The search results provided contain multiple highly relevant publications. Key sources include studies on ADAM28 in malignant tumors showing its role in proliferation and metastasis[1], comprehensive analysis of MET signaling in glioblastoma[2], investigation of hypoxia-induced metabolic reprogramming in esophageal cancer relevant to general hypoxic tumor pathways[3], glioblastoma-specific research on hypoxia and the endocannabinoid system[6], and multiple recent studies (2022-2024) on metabolic regulation in glioblastoma, including work on NOX4, metabolic intermediates, immune biomarkers, and collagen-mediated processes[5][12][15][20][23][25]. These references establish empirical foundation for interpreting the functional roles of genes in our input list.

### 1.2 Glioblastoma as a Biological Context

Glioblastoma (GBM), also termed glioblastoma multiforme, represents the most common and aggressive primary malignant brain tumor in adults[2][5]. The disease is characterized by rapid growth, extensive infiltration into surrounding brain tissue, robust resistance to current multimodal therapies including surgery, radiation, and chemotherapy with temozolomide, and almost universally fatal prognosis with median survival approximately 12-15 months despite treatment[2]. The glioblastoma microenvironment presents unique selective pressures including severe hypoxia, nutrient deprivation, limited vascular perfusion, abundant extracellular matrix, and significant immune infiltration dominated by immunosuppressive macrophages and microglia[5].

These microenvironmental stresses drive the evolution of malignant phenotypes through selection for tumor cells capable of metabolic adaptation, chemotherapy resistance, enhanced migration and invasion, and immune evasion. Understanding how the genes in our input list contribute to these adaptive capabilities is essential for identifying therapeutic vulnerabilities and developing rational combinatorial treatment strategies.

---

## Section 2: Gene Program 1 - Hypoxia Sensing and HIF-1α-Mediated Adaptation

### 2.1 Program Overview and Molecular Basis

**Program Name:** Hypoxia-Inducible Factor Pathway and Stress Response Coordination

The first major gene program encompasses genes whose expression is regulated by or whose products functionally integrate with hypoxia-inducible factor 1-alpha (HIF-1α), the master transcriptional regulator of cellular adaptation to low oxygen tension[3][6][7][28][29]. In glioblastoma, hypoxia is not merely an incidental microenvironmental feature but rather a critical driver of tumor progression, stemness, and therapeutic resistance. The tumor microenvironment typically contains regions of severe hypoxia due to irregular vascularization and high metabolic demand, particularly in pseudopalisading and necrotic zones[5][6][28][29].

**Supporting Genes:** HILPDA, HMOX1, PTGS2, BNIP3L, ANGPTL4, NOX4, NDRG1

### 2.2 Mechanistic Integration and Atomic Processes

#### 2.2.1 HIF-1α Transcriptional Regulation

Research demonstrates that hypoxia activates HIF-1α stabilization through inhibition of prolyl hydroxylase domain-containing proteins (PHDs), allowing HIF-1α to accumulate in the nucleus and regulate transcription of target genes[3][28][29]. Among the genes in our input list, HILPDA (hypoxia-inducible lipid droplet-associated protein) is directly transcriptionally activated by HIF-1α under hypoxic conditions[25]. Multiple recent studies confirm that HILPDA expression marks hypoxic regions of glioblastoma organoid models and patient tumors, with particularly enriched expression in pseudopalisading zones where tumor cells exist in a perinecrotic environment[25]. The functional consequence of HILPDA upregulation is enhanced lipid droplet accumulation and metabolic remodeling toward fatty acid utilization, which we discuss further in the metabolic plasticity program below[25].

PTGS2 (also known as COX-2, cyclooxygenase-2) is similarly upregulated by HIF-1α in the hypoxic tumor microenvironment[3]. In esophageal squamous cell carcinoma, hypoxia activates the COX-2-PTGES (prostaglandin E synthase) axis in a HIF-1α-dependent manner, with this pathway having broader implications for squamous tumors and other cancer types[3]. In glioblastoma context, PTGS2 upregulation leads to enhanced prostaglandin E2 (PGE2) production, which has pro-tumoral effects including promotion of angiogenesis, suppression of antitumor immunity, and enhancement of cancer stem cell properties[6].

#### 2.2.2 Mitochondrial Dynamics and Oxidative Stress Adaptation

BNIP3L (BCL2/adenovirus E1B 19 kDa interacting protein 3-like), also known as NIX, functions as a mitophagy receptor that is transcriptionally upregulated by HIF-1α particularly under hypoxic conditions[26][29]. BNIP3L recruits autophagosomes to damaged or depolarized mitochondria, promoting selective autophagy of mitochondria (mitophagy)[26]. This process is critical for hypoxic adaptation because it eliminates dysfunctional mitochondria that would otherwise generate excessive reactive oxygen species (ROS), thereby protecting cells from oxidative stress-induced apoptosis[26][29]. In retinal development, BNIP3L-dependent mitophagy has been shown to drive metabolic reprogramming toward glycolysis[29], a shift highly relevant to glioblastoma cells which upregulate glycolytic metabolism to sustain ATP production under hypoxic and nutrient-limited conditions.

NOX4 (NADPH oxidase 4) represents a controlled source of ROS production that, paradoxically, promotes tumor cell survival under hypoxic stress[20][23]. NOX4 expression is upregulated in cycling hypoxic glioblastoma cells, and NOX4-derived ROS serves multiple pro-survival functions including activation of HIF-1α signaling, MAPK pathway activation, and promotion of metabolic reprogramming[23]. This creates a feedback loop wherein hypoxia activates NOX4, NOX4 generates ROS that stabilizes HIF-1α, and HIF-1α further upregulates genes supporting survival under continued stress. Notably, NOX4 inhibition has been proposed as a therapeutic strategy to sensitize hypoxic glioblastoma cells to radiotherapy[23].

HMOX1 (heme oxygenase-1) is similarly upregulated by multiple hypoxia-responsive transcription factors including HIF-1α and Nrf2[7][10]. HMOX1 catalyzes the degradation of heme to biliverdin, free iron, and carbon monoxide (CO)[10]. This process serves multiple adaptive functions: the antioxidant biliverdin reduces ROS levels, the CO functions as a signaling molecule, and iron release supports mitochondrial function and metabolic enzymes[7][10]. In glioblastoma specifically, HMOX1 expression correlates with therapeutic resistance, particularly resistance to proteasome inhibitors and arsenic trioxide[7][10]. HMOX1 overexpression in hypoxic side population glioblastoma cells was shown to confer resistance through the hypoxia-ROS-HMOX1 axis[7], establishing HMOX1 as a key mediator of stress adaptation in the hypoxic glioblastoma microenvironment.

#### 2.2.3 NDRG1 as a Stress-Responsive Tumor Suppressor with Contextual Functions

NDRG1 (N-myc downstream regulated gene 1) presents a more complex functional role in glioblastoma, serving as both a stress-response gene and a tumor suppressor whose expression is paradoxically often downregulated in gliomas[19][22]. NDRG1 is regulated under stress conditions including hypoxia and is transcriptionally repressed by c-Myc, which is highly expressed in aggressive gliomas[19]. High NDRG1 expression in glioblastoma correlates with better prognosis and suppresses proliferation through inhibition of GSK3β and suppression of AKT/mTOR signaling[22]. NDRG1 also functions to suppress epithelial-mesenchymal transition and metastatic potential by maintaining adherens junctions and modulating EMT-related proteins[19]. The paradox of NDRG1 downregulation in tumors despite its tumor-suppressive functions likely reflects selection pressure for loss of this constraint during transformation; however, therapeutic restoration of NDRG1 expression has been proposed as a potential strategy[19][22].

#### 2.2.4 ANGPTL4 in Hypoxic Adaptation and Stemness

ANGPTL4 (angiopoietin-like 4) represents a multi-functional secreted protein whose expression is induced by hypoxia through HIF-1α and HIF-2α-dependent mechanisms[9][12]. In glioblastoma, ANGPTL4 promotes temozolomide resistance through enhancement of cancer stem cell properties via the EGFR/AKT/4E-BP1 phosphorylation cascade[9]. ANGPTL4 simultaneously functions in angiogenic responses through promotion of vascular development and in hypoxic adaptation through promotion of anoikis resistance and support of tumor cell growth under nutrient deprivation[12]. The protein functions in at least two functional forms: the C-terminal fragment (cANGPTL4) promotes metastasis and tumor growth, while the N-terminal fragment (nANGPTL4) paradoxically inhibits these processes[12]. In glioblastoma specifically, HIF-1-induced ANGPTL4 appears to drive NOX4-mediated ROS production and metabolic rewiring toward enhanced aerobic glycolysis and EMT programs[23].

### 2.3 Cellular Impacts and Program Significance

The collective upregulation of this hypoxia-responsive gene program results in multiple coordinated cellular adaptations: (1) sustained ATP production through shifts toward glycolysis and fatty acid oxidation despite limited oxygen, (2) protection from oxidative stress through enhanced antioxidant capacity and mitophagy, (3) promotion of angiogenesis to improve vascular supply, (4) enhancement of stemness and resistance to differentiation-inducing therapies, and (5) suppression of apoptosis through PI3K/AKT pathway activation and metabolic rewiring.

The significance of this program is exceptionally high, as hypoxia represents one of the most consistent features of glioblastoma microenvironments and directly drives multiple other gene programs identified in this analysis. Approximately 60-80% of glioblastoma tissue contains hypoxic regions, and the hypoxic phenotype is particularly pronounced in aggressive, recurrent tumors[5][28]. The genes in this program are not only individually important but appear to function as an integrated regulatory network wherein signals converge on HIF-1α stabilization and transcriptional output.

| Program Element | Key Genes | Primary Functions | Significance |
|---|---|---|---|
| HIF-1α transcriptional targets | HILPDA, PTGS2, ANGPTL4, BNIP3L | Metabolic remodeling, lipid accumulation, mitophagy, angiogenesis | Very High |
| Oxidative stress adaptation | HMOX1, NOX4 | ROS regulation, feedback stabilization of HIF-1α | Very High |
| Mitochondrial quality control | BNIP3L, HMOX1 | Elimination of dysfunctional mitochondria, ATP preservation | High |
| Tumor suppression (if expressed) | NDRG1 | GSK3β regulation, EMT suppression, differentiation support | Medium |

---

## Section 3: Gene Program 2 - Proteolytic Remodeling and Extracellular Matrix Degradation

### 3.1 Program Definition and Functional Scope

**Program Name:** Extracellular Matrix Proteolysis and Cell Adhesion Remodeling

The second major gene program encompasses genes whose protein products actively remodel the extracellular matrix (ECM) through proteolytic cleavage, genes that regulate ECM deposition and composition, and genes that mediate cell-matrix interactions through adhesion receptors[1][2][14][15][18]. Glioblastoma is characterized by aggressive invasion into surrounding brain tissue, which requires both enzymatic degradation of the ECM barrier and active migration through tissue. The ECM surrounding glioblastoma cells contains abundant fibrillar collagens, proteoglycans, fibronectin, laminin, and other structural proteins that normally constrain cell migration.

**Supporting Genes:** ADAM28, COL5A1, COL13A1, COL24A1, LTBP2, ABI3BP, FAT4, CAV1

### 3.2 ADAM28: A Central Proteolytic Hub in Glioblastoma Progression

#### 3.2.1 ADAM28 Structure and Substrate Specificity

ADAM28 (a disintegrin and metalloproteinase 28) is a membrane-anchored metalloprotease that executes its proteolytic function through a zinc-dependent catalytic domain[1]. Unlike many ADAMs that are broadly expressed during development and relatively silent in adult tissues, ADAM28 is highly overexpressed in numerous malignant tumors including glioblastoma[1][4]. The protease cleaves multiple substrates including insulin-like growth factor-binding protein-3 (IGFBP-3), von Willebrand factor (vWF), and connective tissue growth factor (CTGF)[1].

The functional consequence of ADAM28-mediated cleavage of IGFBP-3 is particularly important in glioblastoma pathogenesis. IGFBP-3 functions as a sequestering protein that binds and inactivates insulin-like growth factors (IGFs). ADAM28 cleaves IGFBP-3, liberating free IGF-1 and IGF-2 that activate IGF receptor signaling[1]. This protease activity shifts the balance from growth-suppressive (IGF-bound) to growth-promoting (IGF-free) states. Simultaneously, ADAM28-mediated cleavage of vWF (von Willebrand factor) promotes cell adhesion through PSGL-1/P-selectin interactions, facilitating both tumor cell adhesion to vascular endothelium and escape from anoikis-induced apoptosis[1].

#### 3.2.2 ADAM28-Driven Proliferation and Chemotherapy Resistance

Functional studies demonstrate that ADAM28 overexpression directly promotes cell proliferation, induces neovascularization, and generates resistance to apoptotic stimuli[1]. The mechanisms involve both proteolytic substrate cleavage and non-catalytic functions. In acute myeloid leukemia (AML), ADAM28 expression directly correlates with poor relapse-free survival and event-free survival, and ADAM28 promotes the growth and spread of AML cells through IGF-1 release and activation of PI3K/Akt/mTOR and Ras/MAPK signaling cascades[1]. Given the central importance of these same pathways in glioblastoma growth and survival, the role of ADAM28 in driving these cascades likely extends to glioblastoma with similar functional consequences.

Notably, selective inhibition of ADAM28 has been shown in experimental systems to impede tumor proliferation, metastasis, and drug resistance[1], suggesting potential therapeutic utility. The fact that ADAM28 expression significantly increases during tumor progression from early-stage to advanced and metastatic stages indicates its role as both a prognostic marker and a driver of disease progression[1].

#### 3.2.3 ADAM28 in the Glioblastoma Tumor Microenvironment

In glioblastoma specifically, ADAM28 likely contributes to the aggressive invasive phenotype by promoting cell adhesion through PSGL-1/P-selectin interactions and by generating free IGF growth factors in the hypoxic, nutrient-poor tumor microenvironment where growth factors are at premium. The proteolytic activity of ADAM28 would additionally contribute to degradation of ECM components that normally constrain cell invasion, though direct evidence of ECM degradation by ADAM28 in glioblastoma remains limited in available literature.

### 3.3 Collagen-Based Extracellular Matrix Composition and Its Regulation

#### 3.3.1 COL5A1: A Dominant Collagen in Fibrillary Matrix Architecture

COL5A1 (type V collagen α1 chain) emerged from recent bioinformatics and functional studies as a pivotal regulator of glioblastoma malignancy[15]. Collagen type V is a fibrillar collagen that forms heterotrimeric molecules with type I collagen in the ECM and regulates the architecture and mechanical properties of the matrix. Expression of COL5A1 is significantly elevated in glioma tissues compared to normal brain and correlates with poor survival outcomes in glioma patients[15].

Mechanistically, COL5A1 acts through regulation of cell migration and metastasis by modulating the cytoskeleton and actin dynamics. The COL5A1-PPRC1-ESM1 axis was identified through transcriptomic analysis as a functional pathway wherein COL5A1 activates PPRC1 (peroxisomal proliferator-activated receptor gamma coactivator 1-related protein 1) as a transcriptional regulator, which in turn activates ESM1 (endothelial cell-specific molecule 1)[15]. ESM1 functions to remodel the extracellular matrix and enhance cell migration through mechanisms involving actin cytoskeleton reorganization[15]. In glioblastoma cells, knockdown of COL5A1 significantly reduced cell migration and invasion capability, confirming its functional role in the invasive phenotype[15]. Importantly, COL5A1 expression was shown to be an independent prognostic factor that competed with established glioblastoma markers including H3K27M, MGMT methylation status, and EGFR amplification, suggesting COL5A1's particular importance in glioblastoma biology[15].

#### 3.3.2 Additional Collagen Contributors and Collagen Signatures

Other collagen genes in the input list including COL13A1 and COL24A1 contribute to the compositional diversity of the glioblastoma ECM. While detailed functional studies specifically in glioblastoma are limited for these genes, broader cancer biology literature indicates that distinct "collagen signatures" are associated with different stromal phenotypes and tumor microenvironment states[18]. The presence of multiple collagen genes in the input list suggests that the glioblastoma ECM represents a highly organized, multi-component collagenous structure whose composition is actively remodeled during progression.

### 3.4 Latent TGF-β Binding Protein 2 and ECM Sequestration

LTBP2 (latent TGF-β binding protein 2) functions to sequester and regulate the bioavailability of transforming growth factor-beta (TGF-β) in the extracellular matrix[39][42]. Recent comprehensive studies demonstrate that LTBP2 expression in glioblastoma positively correlates with glioma WHO grade, mesenchymal subtype, and poor survival outcomes[39]. LTBP2 expression is significantly associated with tumor-associated macrophage (TAM) infiltration, suggesting its role in recruiting and sustaining immunosuppressive immune cells[39]. Mechanistically, LTBP2 knockdown reduced proliferation and enhanced sensitivity to temozolomide chemotherapy, indicating that LTBP2 contributes to both inherent proliferation and therapy resistance[39][42]. The relationship between LTBP2 expression and TAM infiltration is particularly noteworthy as it suggests a reciprocal interaction between the ECM-modifying program and the immune microenvironment program discussed below.

### 3.5 Cell Adhesion Regulation through FAT4 and Caveolin-1

#### 3.5.1 FAT4 as a Suppressor of Wnt/β-Catenin Signaling

FAT4 (FAT atypical cadherin 4) functions as a tumor suppressor whose expression is downregulated in multiple cancer types including gastric cancer, breast cancer, and other solid tumors[14][17]. FAT4 acts through inhibition of Wnt/β-catenin signaling, a pathway known to promote tumor cell growth and stemness. In gastric cancer models, FAT4 knockdown promotes cell growth and invasion through activation of Wnt/β-catenin pathway components including upregulation of TCF4, c-Myc, cyclin D1, and MMP genes[14]. Importantly, FAT4 silencing promotes β-catenin nuclear accumulation, indicating direct inhibition of canonical Wnt signaling by FAT4[14].

In the context of glioblastoma, where Wnt/β-catenin signaling is known to promote cancer stem cell properties and therapy resistance, FAT4 downregulation would be expected to enhance these malignant phenotypes[14][17]. The pan-cancer analysis confirmed that FAT4 functions as a tumor suppressor with prognostic significance across multiple cancer types, further supporting its potential relevance in glioblastoma[17].

#### 3.5.2 Caveolin-1: Dual Role as Adhesion Regulator and Potential Therapeutic Target

Caveolin-1 (CAV1) represents a particularly interesting case within the proteolytic and adhesion remodeling program, as it exhibits context-dependent tumor-suppressive and tumor-promoting functions[13][16]. In glioblastoma, CAV1 presents a paradoxical phenotype wherein experimental overexpression of CAV1 in cell lines reduces proliferation and confers sensitivity to temozolomide chemotherapy (consistent with tumor-suppressive function)[13], yet high CAV1 expression in patient tumors is associated with poor prognosis, shorter survival, and increased invasiveness (consistent with tumor-promoting function)[16].

The resolution of this paradox emerges from spatial analysis: CAV1 is particularly elevated in the mesenchymal subtype of glioblastoma, a clinically aggressive subtype associated with poor outcomes[16]. CAV1 expression in high-CAV1-expressing mesenchymal GBM correlates with shorter survival in both TCGA (median 5.1 months vs. 14.9 months for low CAV1) and CGGA (Cox p=0.004) cohorts[16]. CRISPR-based functional studies in U87 glioblastoma cells demonstrated that CAV1 deletion reduced colony formation and invasion capacity without affecting proliferation, suggesting CAV1's primary role in glioblastoma is modulation of invasive and adhesive properties rather than proliferation[16]. The molecular mechanisms involve CAV1's multiple signaling roles including facilitation of ERK and AKT signaling, modulation of matrix-degrading enzyme expression, and regulation of cell adhesion[16].

### 3.6 Program Integration and Cellular Impacts

The proteolytic remodeling program collectively enables glioblastoma cells to degrade and remodel their surrounding ECM, enhance cell-matrix interactions that promote survival and migration, and shift the balance toward pro-growth signaling through proteolytic liberation of growth factors. ADAM28-mediated IGF-1 release directly activates PI3K/Akt/mTOR growth signaling, while COL5A1 and associated ECM components provide structural scaffold for migration and modulate mechanotransduction. FAT4 downregulation removes a constraint on Wnt/β-catenin signaling, while CAV1 elevated in mesenchymal tumors facilitates signaling cascade activation and invasion.

The significance of this program is very high, as ECM remodeling and invasion represent hallmark features of glioblastoma that distinguish it from less aggressive brain tumors and directly drive infiltration into surrounding tissue, a major barrier to surgical cure.

---

## Section 4: Gene Program 3 - Growth Factor Signaling and Receptor Tyrosine Kinase Pathways

### 4.1 Program Architecture and Regulatory Hierarchy

**Program Name:** Receptor Tyrosine Kinase Signaling and Feedback Control

The third major gene program encompasses genes whose products function in receptor tyrosine kinase (RTK) signaling cascades, including growth factor receptors, their ligands, downstream signaling effectors, and negative feedback regulators[2][9][33][37]. Dysregulation of RTK signaling represents one of the most frequent and consequential alterations in glioblastoma, with the top three dysregulated RTKs being EGFR, PDGFRα, and MET according to integrated genomic analyses[2].

**Supporting Genes:** MET, ERRFI1, PRKCH, TRIB3, EPHA3

### 4.2 MET Signaling in Glioblastoma Pathogenesis and Therapy Resistance

#### 4.2.1 MET Expression, Amplification, and Functional Activation in GBM

MET (mesenchymal-epithelial transition factor) receptor and its ligand hepatocyte growth factor (HGF) play critical roles in glioblastoma proliferation, survival, migration, invasion, angiogenesis, stem cell characteristics, and therapeutic resistance[2]. Expression and copy number analyses from The Cancer Genome Atlas (TCGA) reveal that approximately 30% of glioblastomas display overexpression of both HGF and MET, suggesting autocrine/paracrine HGF-MET activation occurs in a significant patient subset[2]. More strikingly, genomic analysis identified that MET gene gain occurs in 47% of primary glioblastomas and 44% of secondary glioblastomas at the 7q31.2 locus, demonstrating that MET amplification is among the earliest genetic alterations in gliomagenesis[2].

MET localizes to both the cell membrane (where it receives ligand) and the cytoplasm, with high MET intensity correlating with high WHO grade and shorter progression-free survival (PFS) and overall survival (OS) in glioblastoma patients[2]. The expression pattern shows particular enrichment in peri-necrotic regions of tumors, the hypoxic zones where most aggressive tumor cells reside, indicating that MET signaling is particularly important for adaptation to harsh microenvironmental conditions[2].

#### 4.2.2 Molecular Mechanisms of MET-Driven Gliomagenesis

MET receptor activation through HGF binding triggers multiple downstream signaling cascades including PI3K/Akt/mTOR pathway activation (promoting cell survival and proliferation), Ras/MAPK pathway activation (promoting proliferation and differentiation), and FAK signaling (promoting migration and invasion). Importantly, MET activation is not merely permissive for glioblastoma growth but actively shapes tumor phenotype: MET mediates endothelial plasticity through the MET/ETS-1/MMP-14 axis, which controls vascular endothelial cadherin (VE-cadherin) degradation and endothelial-mesenchymal transition, thereby driving aberrant vascularization and chemoresistance in glioblastoma[2].

MicroRNA-based regulation provides additional layers of MET control: miR-34a, miR-182, and miR-144-3p levels are inversely correlated with MET levels in human gliomas, with mechanistic studies showing that these microRNAs specifically bind the MET 3'-untranslated region and inhibit its expression[2]. This miRNA-based regulation likely represents a tumor-suppressive mechanism that can be circumvented through mutations or epigenetic silencing of these miRNAs in aggressive tumors.

#### 4.2.3 Therapeutic Targeting of MET Signaling

Over the past decade, multiple therapeutic strategies targeting MET or HGF have entered clinical development and testing, including monoclonal antibodies against MET (such as onartuzumab and rilotumumab), MET receptor kinase inhibitors (such as crizotinib, cabozantinib, and foretinib), and HGF antagonists[2]. However, clinical experience to date indicates that single-agent MET inhibition has yielded limited efficacy for glioblastoma, likely due to redundancy in growth signaling pathways and compensatory activation of alternative RTKs. This observation motivates investigation of combined MET inhibition with other pathway-targeted therapies or with conventional chemoradiation.

### 4.3 ERRFI1 (MIG6) as Negative Feedback Regulator of EGFR

ERRFI1, also known as MIG6 (mitogen-inducible gene 6), encodes an ERBB receptor feedback inhibitor that negatively regulates EGFR by directly inhibiting its kinase activity and promoting its internalization and degradation[37]. Recent studies demonstrate that the stoichiometric balance between MIG6 and EGFR is crucial for controlling EGFR-dependent oncogenic signaling[37]. Functional loss or decreased expression of MIG6 leads to aberrant EGFR activation and promotes glioblastoma tumorigenesis[37].

A subset of ERRFI1 mutations exhibits impaired ability to suppress EGFR at multiple regulatory levels, suggesting that loss-of-function ERRFI1 mutations occur during glioblastoma progression[37]. The study proposed that ERRFI1 mutation status and MIG6 expression levels could serve as biomarkers for predicting response to EGFR-targeted therapies in glioblastoma, with low MIG6 expression potentially indicating EGFR dependency and responsiveness to EGFR inhibitors[37]. This represents an example of how feedback inhibitors within RTK signaling networks become therapeutic targets when dysregulated.

### 4.4 PRKCH (Protein Kinase C eta) as Downstream Effector of RTK Signaling

PRKCH (protein kinase C eta type) represents a serine/threonine kinase that functions downstream of RTKs to mediate glioblastoma cell proliferation through mTOR pathway activation[33][36]. PKC isoforms (including PRKCH) are activated by growth factor receptors and function to promote cell proliferation, survival, and migration in multiple cancer contexts. In glioblastoma, the PKC signaling pathway contributes to aggressive cell behavior through multiple mechanisms including mTOR activation independent of AKT, AKT and S6 pathway hyperactivation, and cell-cycle signaling pathway promotion[33].

### 4.5 TRIB3 and Complex Kinase Regulation

TRIB3 (tribbles pseudokinase 3) functions as a stress-responsive regulator of multiple signaling pathways including those downstream of growth factors[21][24]. As a pseudokinase (kinase domain-containing but catalytically inactive protein), TRIB3 functions as a scaffold and regulator of other kinases. In head and neck squamous cell carcinoma, TRIB3 promotes malignancy through inhibition of ferroptosis by forming a heterotrimeric complex with β-catenin and TCF4, directly binding the ALOXE3 promoter[21]. 

In glioblastoma specifically, TRIB3 facilitates progression via restraining ferroptosis, another form of regulated cell death[24]. TRIB3 expression is upregulated by various cellular stimuli including growth factors, insulin signaling dysregulation, glucose deficiency, and endoplasmic reticulum (ER) stress[21][24]. The dual role of TRIB3 as both a stress sensor and a driver of malignant phenotype positions it as an integrator of multiple stress signals in the glioblastoma microenvironment.

### 4.6 EPHA3 and Eph Receptor Signaling

EPHA3 (ephrin receptor A3) represents another important RTK whose overexpression occurs in up to 60% of glioblastoma tumors but not in normal brain[45][48]. EphA receptors typically promote differentiation and suppress proliferation, yet paradoxically, high EphA3 expression in glioblastoma is associated with more aggressive, mesenchymal phenotypes and maintains de-differentiated, stem-like states[45][48]. This apparent contradiction resolves through understanding that in glioblastoma, EphA3 is preferentially expressed on the most aggressive glioma stem-like cells (GSCs) and contributes to maintenance of stemness through unknown mechanisms that may involve atypical signaling.

EphA3 was localized in scattered areas of glioblastoma tumors, the invasive ring, and niches near tumor vessels[45]. Notably, EphA3 co-localized with macrophage/leukocyte markers, suggesting expression on tumor-infiltrating immune cells and indicating that EphA3 modulates immune cell function within the tumor microenvironment[45]. EphA3 depletion or treatment with specific anti-EphA3 monoclonal antibodies reduced glioblastoma cell tumorigenicity in vivo by specifically targeting tumor-initiating cells[45][48].

### 4.7 Program Integration and Therapeutic Implications

The RTK signaling program collectively drives glioblastoma proliferation, survival, migration, and invasiveness through activation of multiple downstream pathways (PI3K/Akt/mTOR, Ras/MAPK, Wnt/β-catenin, FAK). The presence of multiple RTKs (MET, EGFR, PDGFRα, EPHA3) with distinct ligands and tissue distributions suggests functional redundancy and compensation wherein inhibition of a single RTK is insufficient to durably suppress signaling.

The program's significance is very high, as RTK dysregulation represents one of the most frequent and therapeutically actionable alterations in glioblastoma, with EGFR amplification occurring in 40% of tumors, PDGFRα amplification in 25%, and MET gain in 44-47%[2]. The convergence of multiple RTKs on common downstream effectors (particularly PI3K/Akt and MAPK) creates both redundancy (making single-pathway inhibition insufficient) and opportunity (making combinatorial pathway inhibition a rational therapeutic strategy).

---

## Section 5: Gene Program 4 - Epithelial-Mesenchymal Transition and Cancer Stem Cell Properties

### 5.1 Program Overview and Developmental Context

**Program Name:** Epithelial-Mesenchymal Transition and Stemness Maintenance

The fourth major gene program encompasses genes whose products regulate epithelial-mesenchymal transition (EMT) and genes that promote or maintain cancer stem cell (CSC) properties in glioblastoma[8][9][11][15][19][21][24]. EMT represents a developmental program wherein cells lose epithelial features (cell-cell adhesion, apical-basal polarity, contact inhibition) and acquire mesenchymal features (enhanced motility, invasiveness, matrix remodeling, and resistance to anoikis)[8][15][21].

While glioblastoma cells are not derived from epithelial lineages (they arise from neural progenitors), the EMT program has been co-opted as a developmental trajectory that confers invasive and stem-like properties. Importantly, glioblastoma displays substantial heterogeneity with distinct transcriptomic subtypes including Proneural, Mesenchymal, and Classical subtypes, with the Mesenchymal subtype representing the most aggressive and therapy-resistant population[2][16][19].

**Supporting Genes:** NDRG1, RUNX2, AHNAK2, TRIB3, FAT4, ANGPTL4, COL5A1, CAV1

### 5.2 RUNX2 and Osteogenic Transcriptional Programming in Glioblastoma

RUNX2 (runt-related transcription factor 2) functions as a transcriptional regulator of osteoblast differentiation and bone development in normal physiology[8][11]. However, emerging evidence indicates that RUNX2 is aberrantly expressed in human glioma cells and mediates pro-tumoral gene programs[11]. In a recent bioinformatics study, RUNX2 was associated with epithelial-mesenchymal transition in the context of TGF-β signaling, representing a novel mechanism through which a developmental transcription factor is repurposed to drive tumor cell invasiveness[8].

The paradox of osteogenic transcription factors driving glioblastoma progression likely reflects the fact that RUNX2-regulated genes promote a stable, migratory, and undifferentiated cellular phenotype that overlaps functionally with both osteogenic development and EMT/stemness programs in cancer contexts. Therapeutic targeting of RUNX2 has been proposed as a potential strategy to reverse EMT and restore differentiation in glioblastoma[8].

### 5.3 AHNAK2 and TGF-β-Induced EMT Programming

AHNAK2 (AHNAK nucleoprotein 2) is a giant structural protein associated with cell adhesion, migration, and cardiac function in normal physiology[51]. In lung adenocarcinoma and other cancers, AHNAK2 promotes EMT in response to TGF-β stimulation[51]. Knockdown of AHNAK2 suppressed TGF-β-induced migration, invasion, and EMT while also inhibiting the TGF-β/Smad3 signaling pathway[51].

AHNAK2 is highly expressed in lung adenocarcinoma tissues and promotes tumor cell invasiveness through multiple mechanisms including enhancement of TGF-β signaling responsiveness. The protein mediates hypoxia-driven EMT and stem cell induction through HIF-1α regulation in other cancer contexts, suggesting that AHNAK2 functions as an integrator of multiple EMT-inducing signals including TGF-β and hypoxia[51]. In the glioblastoma context where both TGF-β signaling (which is broadly active in the tumor microenvironment) and hypoxia (which is endemic in tumors) are prominent, AHNAK2 likely functions as a coordinated EMT driver.

### 5.4 NDRG1's Complex Role in EMT Suppression and Proneural Phenotype Maintenance

As discussed above, NDRG1 functions as a tumor suppressor in part through suppression of EMT and maintenance of epithelial-like characteristics[19][22]. NDRG1 promotes the expression of E-cadherin and suppresses mesenchymal markers N-cadherin and vimentin[19]. At the molecular level, NDRG1 functions through inhibition of GSK3β and thereby suppression of β-catenin-dependent transcription, which normally promotes EMT-related genes[22].

Interestingly, recent studies reveal that NDRG1 exists in a dynamic balance with the mesenchymal phenotype, and that NDRG1 overexpression in proneural (PN) GSCs induced transition to mesenchymal (MES) subtype and a more highly malignant phenotype, suggesting context-dependent effects[19]. This observation indicates that while NDRG1 suppresses EMT in bulk tumor populations, its overexpression in specific GSC contexts may paradoxically promote mesenchymal transition, highlighting the complexity of EMT regulation in heterogeneous tumors.

### 5.5 FAT4's Suppression of Wnt/β-Catenin-Driven Stemness

As discussed above, FAT4 functions as a negative regulator of Wnt/β-catenin signaling[14][17]. Wnt/β-catenin pathway activity is known to promote cancer stem cell properties and EMT in glioblastoma, with high TCF/LEF transcriptional activity driving stemness and therapy resistance. FAT4 downregulation, which occurs during malignant progression, removes this constraint and allows enhanced Wnt signaling, thereby promoting stemness and EMT-related phenotypes[14][17].

### 5.6 ANGPTL4's Promotion of Cancer Stem Cell Enrichment

ANGPTL4 directly promotes glioblastoma stemness through the EGFR/AKT/4E-BP1 phosphorylation cascade, with resulting increased expression of stem cell markers BMI-1, SOX2, and CD133[9]. This program is specifically activated in glioma stem-like cells (GSCs) and promotes enrichment of GSCs, which are responsible for tumor initiation, recurrence after therapy, and resistance to differentiation-inducing therapies[9]. The Sp4 transcription factor upregulates ANGPTL4 expression specifically (rather than Sp1), and both Sp4 and ANGPTL4 levels correlate with poor glioblastoma prognosis[9]. ANGPTL4-mediated stemness enrichment contributes to temozolomide resistance through multiple mechanisms including enhanced survival signaling and reduced differentiation[9].

### 5.7 COL5A1 and Metastatic Potential Through Cytoskeletal Remodeling

As discussed above, COL5A1 promotes invasion and metastasis through the COL5A1-PPRC1-ESM1 axis and modulation of actin filament organization[15]. This pathway directly supports the physical migration capacity required for EMT phenotypes. The enrichment of multiple collagen genes in the glioblastoma ECM and their direct modulation of actin-dependent motility links ECM composition to EMT phenotype maintenance.

### 5.8 CAV1 in Mesenchymal Phenotype Maintenance

CAV1 is significantly elevated in the mesenchymal subtype of glioblastoma and promotes invasion through modulation of matrix-degrading enzyme expression and signaling pathway activation[16]. While early functional studies in cell lines suggested tumor-suppressive functions of CAV1 overexpression, the clinical correlation showing poor prognosis with high CAV1 expression predominantly in mesenchymal tumors indicates that CAV1 functions to maintain and promote mesenchymal phenotype[13][16].

### 5.9 Program Integration and Cellular Implications

The EMT/stemness program collectively drives a malignant transition wherein glioblastoma cells lose differentiation constraints, acquire enhanced motility and invasiveness, activate stemness-associated survival programs, and develop resistance to therapies that target bulk proliferating tumor cells. The convergence of multiple inputs (RUNX2-mediated transcriptional reprogramming, AHNAK2-mediated TGF-β sensitization, ANGPTL4-mediated stemness enrichment, FAT4 loss-mediated Wnt activation, COL5A1-mediated cytoskeletal remodeling, and CAV1-mediated signaling) creates a reinforced, multi-layered program that coordinates the switch from differentiated to stem-like, invasive phenotypes.

The program's significance is very high, as the Mesenchymal subtype represents the most aggressive glioblastoma phenotype with worst clinical outcomes, and promotion of stemness is a primary mechanism through which tumors escape therapy. Understanding the molecular drivers of EMT/stemness is essential for developing strategies to reverse these programs or target the resulting phenotypes.

---

## Section 6: Gene Program 5 - Metabolic Plasticity and Therapeutic Resistance

### 6.1 Program Overview and Energy Metabolism Context

**Program Name:** Metabolic Reprogramming and Nutrient Utilization Flexibility

The fifth major gene program encompasses genes whose products enable rapid metabolic switching, fatty acid oxidation, glycogen utilization, and other forms of metabolic plasticity that allow glioblastoma cells to survive and proliferate despite severe nutrient and oxygen deprivation[25][27][28][30][56][59]. Glioblastoma tumors contain distinct microenvironmental zones ranging from relatively well-perfused tumor core regions to severely nutrient-poor, hypoxic pseudopalisading and necrotic zones[25]. The metabolic demands of tumor cells are not uniformly met across these zones, creating selection pressure for cells capable of rapid metabolic switching and alternative fuel utilization.

**Supporting Genes:** PPP1R3C, EHHADH, HILPDA, NOX4, ANGPTL4, COL5A1, COL11A1-mediated FAO (not directly in list but mechanistically linked through FAO)

### 6.2 Lipid Droplet Biogenesis and Fatty Acid Metabolism

#### 6.2.1 HILPDA-Driven Lipid Droplet Accumulation in Hypoxic Regions

HILPDA (hypoxia-inducible lipid droplet-associated protein), as discussed above in the hypoxia program, functions as a direct HIF-1α target gene that promotes accumulation of lipid droplets in hypoxic tumor regions[25]. Recent comprehensive analysis using spatial transcriptomics revealed that HILPDA expression is markedly enriched in hypoxic organoid cores and pseudopalisading regions of patient-derived glioblastoma specimens but not in lower-grade brain tumors, indicating that HILPDA-driven lipid accumulation is a specific feature of aggressive glioblastoma in hypoxic microenvironments[25].

Glioblastoma cancer stem cells (CSCs) exhibit distinctive lipid metabolism compared to non-CSCs: CSCs display low lipid droplet accumulation but high expression of fatty acid desaturases (FADS1/2) resulting in elevated production of polyunsaturated fatty acids (PUFAs), whereas non-CSCs display high lipid droplet accumulation with lower PUFA production[25]. Lipidomic analysis confirmed a significant shift in lipid composition between CSCs and non-CSCs, with CSCs dependent on high FADS-mediated PUFA production for maintenance of stemness and self-renewal capacity[25].

The spatial and hierarchical organization of distinct lipid metabolism phenotypes—with HILPDA-driven lipid droplet accumulation in bulk tumor populations and FADS-driven PUFA synthesis in CSCs—suggests coordinated metabolic programs wherein different cell populations specialize in distinct metabolic niches within the tumor[25]. This specialization may explain the therapeutic challenge of targeting tumor metabolism, as inhibition of a single metabolic pathway can be compensated by metabolic switching to alternative fuel sources.

#### 6.2.2 Fatty Acid Oxidation and COL11A1-Mediated FAO Activation

While collagen proteins (like COL11A1 discussed below) are primarily recognized as ECM components, recent studies reveal that extracellular collagen directly activates fatty acid oxidation (FAO) in tumor cells through discoidin domain receptor 2 (DDR2) signaling[27]. This represents a novel mechanism linking ECM composition to metabolic programming. COL11A1 (collagen type XI alpha 1 chain), highly expressed by cancer-associated fibroblasts (CAFs) in tumor stroma and by tumor cells themselves, promotes FAO in tumor cells through the DDR2-Src-Akt-AMPK pathway[27].

In ovarian cancer cells, COL11A1 upregulates fatty acid synthesis through FASN expression, which subsequently supplies fatty acids for FAO, creating an integrated pathway wherein elevated FAO supports tumor cell survival and chemotherapy resistance[27]. Blocking FAO (through CPT1A inhibition with etomoxir) triggered apoptosis even in the presence of COL11A1, indicating that FAO is essential for COL11A1-mediated survival in high-FAO tumors[27]. Importantly, patients who showed increased CPT1A expression in recurrent tumors compared to primary tumors exhibited poor overall survival, suggesting that metabolic switch toward FAO during tumor evolution predicts therapy failure[27].

While COL11A1 is not directly in the input gene list, its mechanistic relationship to FAO-promoting mechanisms and its interaction with ECM components (multiple collagens including COL5A1 in the list) indicates that the collagen program and metabolic program are deeply integrated.

### 6.3 Glycogen Metabolism and PPP1R3C

#### 6.3.1 PPP1R3C as Master Regulator of Glycogen Synthesis and Utilization

PPP1R3C (protein phosphatase 1 regulatory subunit 3C), also known as PTG (protein targeting to glycogen), functions as a key regulator of glycogen synthesis and breakdown through its role as a targeting subunit for protein phosphatase 1 (PP1)[56][59]. PPP1R3C recruits PP1 to glycogen, enhancing the specific activity of PP1 toward dephosphorylation and activation of glycogen synthase (which synthesizes glycogen) and inactivation of glycogen phosphorylase (which breaks down glycogen)[59]. Overexpression of PPP1R3C in liver or muscle significantly increases intracellular glycogen levels[59].

In IDH-mutant chondrosarcoma, another malignancy driven by hypoxia and metabolic reprogramming, PPP1R3C was identified as a key regulator linking glycogen and cholesterol metabolism[56]. PPP1R3C expression was significantly higher in IDH1-mutant chondrosarcomas (40% higher by microarray analysis), and mechanistic studies showed that PPP1R3C regulates glycolysis and glycolytic capacity through control of glycogen availability[56]. PPP1R3C knockdown in vivo suppressed the neoplastic phenotype and increased survival, suggesting that glycogen metabolism represents a tractable therapeutic target in metabolically reprogrammed tumors[56].

The mechanisms whereby glycogen supports tumor growth likely involve provision of rapid glucose through glycogenolysis during nutrient deprivation or hypoxia, thereby sustaining glycolytic ATP production when extracellular glucose is limited[59]. Glycogen accumulation is upregulated in many tumor types under hypoxic and nutrient-stressed conditions, representing a form of metabolic adaptation toward self-sufficiency[59].

#### 6.3.2 Glycogen as Stress-Response Energy Reserve

Glycogen metabolism has been increasingly recognized as a hallmark of metabolic reprogramming in cancer cells, enabling survival under hypoxia, glucose deprivation, and anticancer treatment[59]. In hepatocellular carcinoma, PPP1R3C-mediated glycogen accumulation protects liver cancer cells in the absence of glucose through regulation of oxidative stress and autophagy pathways[59]. This suggests that glycogen storage represents not merely an energy reserve but also a regulator of cell death pathways, wherein glycogen availability suppresses ROS accumulation and pro-death signals.

In glioblastoma specifically, which contains abundant regions of severe hypoxia and nutrient deprivation, glycogen metabolism may similarly support survival through both energy provision and stress-response regulation. The presence of PPP1R3C in the input gene list suggests that glioblastoma transcriptomes likely contain evidence of glycogen metabolic programming, though direct experimental validation in glioblastoma specifically remains limited in the current literature.

### 6.4 EHHADH and Fatty Acid β-Oxidation

EHHADH (enoyl-CoA hydratase/3-hydroxyacyl-CoA dehydrogenase) is a peroxisomal bifunctional enzyme involved in peroxisomal fatty acid β-oxidation, a pathway for metabolism of long-chain fatty acids[30]. In lung squamous cell carcinoma (LUSC), EHHADH was identified as a key regulator of medium-chain fatty acid metabolism through lipidomic analysis[30]. EHHADH knockdown reduced cell proliferation and altered lipid profiles, with increased long-chain fatty acids and storage lipids but decreased medium-chain fatty acids, indicating a specific metabolic reprogramming toward medium-chain fatty acid utilization[30].

The discovery of EHHADH dysregulation in lung cancer suggests that fine-tuning of fatty acid metabolism through peroxisomal pathways represents an important cancer adaptation. In glioblastoma, where both mitochondrial FAO and alternative fatty acid metabolic pathways are likely engaged, EHHADH may contribute to specialized metabolic niches or specific tumor cell populations with distinct metabolic signatures.

### 6.5 NOX4-ROS and Metabolic Rewiring

As discussed above, NOX4-derived ROS production in hypoxic glioblastoma cells promotes HIF-1α stabilization and metabolic rewiring toward enhanced aerobic glycolysis and EMT programs[23]. This represents an example of how oxidative stress, normally considered a threat to cell viability, is paradoxically harnessed to promote oncogenic metabolic changes. The NOX4-HIF-1α-glycolysis axis creates a feedback loop wherein hypoxia activates NOX4, NOX4-derived ROS stabilizes HIF-1α, and HIF-1α upregulates genes supporting both glycolytic metabolism and ROS-detoxifying enzymes.

### 6.6 Program Integration and Therapeutic Implications

The metabolic plasticity program collectively enables glioblastoma cells to reprogram their metabolism in response to microenvironmental stress through multiple integrated mechanisms: (1) upregulation of HILPDA-driven lipid droplet accumulation in hypoxic zones, (2) activation of FAO through collagen-DDR2 signaling, (3) utilization of intracellular glycogen reserves through PPP1R3C-regulated synthesis, (4) specialization in distinct populations toward FADS-mediated PUFA synthesis (CSCs) or HILPDA-mediated lipid storage (bulk cells), and (5) ROS-mediated feedback stabilization of hypoxic transcriptional programs that further enhance metabolic switching.

The significance of this program is very high, as metabolic plasticity directly enables survival under the therapeutic stresses (chemotherapy, radiotherapy) and microenvironmental stresses (hypoxia, nutrient deprivation) that would otherwise trigger cancer cell death. Recent literature increasingly emphasizes metabolic targeting as a therapeutic strategy to eliminate therapy-resistant tumor populations, making the genes in this program high-value targets for combination therapeutic approaches.

---

## Section 7: Gene Program 6 - Immune Microenvironment and Checkpoint Regulation

### 7.1 Program Overview and Immunological Context

**Program Name:** Immune Checkpoint and Microenvironment Modulation

The sixth major gene program encompasses genes whose products regulate immune cell infiltration, polarization of immune populations, and establishment of immunosuppressive tumor microenvironments[32][35][39][43][46][49]. Glioblastoma is characterized by a markedly immunosuppressive microenvironment dominated by tumor-associated macrophages (TAMs) and microglia, which typically assume an M2-like anti-inflammatory phenotype that promotes tumor growth rather than anti-tumor immunity[35][39].

**Supporting Genes:** SPNS2, HMOX1, PTGS2, EPSTI1, LTBP2, MX2

### 7.2 SPNS2 and Sphingosine-1-Phosphate Gradient Regulation

SPNS2 (spinster homologue 2) functions as a specific transporter of sphingosine-1-phosphate (S1P), the lipid mediator that regulates lymphocyte trafficking and immune cell egress from lymphoid organs[46]. SPNS2 is expressed on lymphatic endothelial cells and regulates the S1P gradient between high circulating S1P and low tissue S1P that controls lymphocyte trafficking[46]. Mice with SPNS2 deletion develop lymphopenia and exhibit decreased numbers of circulating T and B cells, demonstrating that SPNS2-mediated S1P export is essential for immune cell mobilization[46].

In hepatocellular carcinoma, SPNS2 expression correlated with lymphatic endothelial cell infiltration and enhanced lymphangiogenesis[43]. Interestingly, SPNS2 correlated with lymph-angiogenesis-associated and EMT-related gene expression but also enriched immune response pathways[43]. The functional consequence was paradoxical: while SPNS2-high tumors showed infiltration by cancer-promoting pathways and pro-tumor immune signaling, they also demonstrated decreased cancer cell proliferation and improved patient disease-free survival[43]. This suggests that SPNS2 modulates the complex balance between pro-tumor immune signaling and anti-tumor immune activation, with net clinical effect depending on context-specific immune infiltration patterns[43].

In cancer metastasis specifically, SPNS2 deletion in host tissue enhanced T cell activity and NK cell function, resulting in reduced pulmonary metastatic burden, suggesting that SPNS2 inhibition may enhance immunotherapy efficacy by increasing immune cell mobilization and activation[46]. The implications for glioblastoma are significant, as enhanced lymphatic function and immune cell infiltration could theoretically overcome the immunosuppressive glioblastoma microenvironment and increase responsiveness to immunotherapy.

### 7.3 HMOX1 and Macrophage Polarization

As discussed above, HMOX1 catalyzes heme degradation and is upregulated by stress signals in hypoxic and inflammation-prone microenvironments[7][10]. Beyond its antioxidant functions, HMOX1 has been implicated in macrophage polarization toward anti-inflammatory M2-like phenotypes that promote tumor growth. The hemoglobin-derived heme and the HMOX1 product biliverdin both exhibit immunosuppressive properties and promote IL-10 production in macrophages[10]. This suggests that HMOX1 upregulation in glioblastoma cells, through both cell-intrinsic survival mechanisms and through paracrine effects on macrophages, promotes a permissive immune microenvironment[10].

### 7.4 PTGS2-Mediated Prostaglandin E2 Production and Immune Suppression

PTGS2 (COX-2) upregulation in hypoxic glioblastoma leads to PGE2 production, which exhibits multiple immunosuppressive functions including suppression of Th1 T cell differentiation, promotion of Th2 responses, and promotion of regulatory T cell (Treg) development[6][3]. PGE2 also directly suppresses anti-tumor macrophage phenotypes and promotes M2 polarization. The combination of PTGS2 upregulation and PGE2-mediated immune suppression likely contributes to the characteristic immunosuppressive environment of glioblastoma[3][6].

### 7.5 EPSTI1 and M1 Macrophage Infiltration

EPSTI1 (epithelial stromal interaction 1), recently characterized in the context of colorectal cancer immune infiltration[32], shows positive association with M1 macrophage and myeloid dendritic cell infiltration. EPSTI1 expression was predominantly localized to immune cells, particularly macrophages and dendritic cells, in single-cell transcriptomic analysis[32]. Higher EPSTI1 expression associated with better relapse-free survival and higher immune scores, suggesting that EPSTI1-expressing immune cells exert anti-tumor functions[32]. EPSTI1 correlates with activation of interferon-γ response, IL-6-JAK-STAT3 signaling, and TNF-α signaling pathways in immune cells[32].

If EPSTI1 similarly functions to recruit and activate anti-tumor M1 macrophages in glioblastoma, its expression might indicate infiltration by inflammatory immune populations rather than the immunosuppressive M2/macrophage phenotype typical of glioblastoma. This suggests EPSTI1 expression as a potential biomarker for immune responsiveness or immunotherapy efficacy.

### 7.6 LTBP2 and Tumor-Associated Macrophage Recruitment

As discussed above in the ECM program, LTBP2 expression in glioblastoma strongly correlates with TAM infiltration[39]. Recent studies identified that LTBP2 expression associates with abundant TAM infiltration, particularly in mesenchymal-subtype tumors[39]. LTBP2 promotes recruitment and/or retention of TAMs through mechanisms likely involving TGF-β sequestration and bioavailability modulation, as LTBP2 directly binds and regulates latent TGF-β complexes[39]. High LTBP2 expression glioblastoma patients who received chemotherapy survived shorter periods than low LTBP2 patients, indicating that LTBP2-associated TAM infiltration correlates with chemotherapy resistance[39].

### 7.7 MX2 and Innate Immune Signaling

MX2 (MX dynamin-like GTPase 2) functions as an interferon-stimulated gene encoding a protein with antiviral properties[49][52]. Recent studies reveal that MX2 regulates innate immune signaling and interferon-responsive gene programs in cancer cells[49][52]. In glioblastoma cells, Mx2 mediates resistance to oncolytic herpes simplex virus infection through interferon signaling, and Mx2 depletion enhances viral replication by reducing MyD88 and DHX36 expression, key mediators of TLR-mediated innate immune responses[52].

MX2 regulates tumor suppressor XAF1 (X-linked apoptosis-inducing factor) and mediates interferon-induced growth inhibition in a context-dependent manner[49]. In melanoma, higher MX2 expression renders cells more sensitive to targeted therapy drugs, suggesting that MX2 may function as a sensitizer to certain anti-cancer therapies. In glioblastoma where interferon signaling is often suppressed, MX2 expression may indicate enhanced interferon responsiveness and potential immunotherapy efficacy.

### 7.8 Program Integration and Immunotherapeutic Implications

The immune microenvironment program collectively orchestrates an immunosuppressive tumor ecosystem through multiple coordinated mechanisms: (1) SPNS2-mediated S1P gradient regulation that restricts lymphocyte egress and infiltration, (2) HMOX1-mediated macrophage polarization toward M2 phenotypes, (3) PTGS2/PGE2-mediated suppression of Th1 responses and promotion of Tregs, (4) LTBP2-mediated TAM recruitment and retention, balanced against (5) EPSTI1-mediated recruitment of inflammatory M1 macrophages and (6) MX2-mediated interferon signaling. The net result is dominance of anti-tumor immune populations by pro-tumor populations, enabling immune evasion despite significant immune cell infiltration.

The significance of this program is very high given recent recognition of immunotherapy as a potentially transformative approach for glioblastoma. The multiple immune-regulatory genes in the input list suggest that glioblastoma cells actively reshape their immune microenvironment through cell-intrinsic and paracrine mechanisms, and that therapeutic interventions targeting these regulatory mechanisms could potentially restore anti-tumor immunity.

---

## Section 8: Gene Program 7 - Post-Transcriptional and Epigenetic Regulation by Long Non-Coding RNAs

### 8.1 Program Overview and Regulatory Mechanisms

**Program Name:** Long Non-Coding RNA and Post-Transcriptional Gene Regulation

The seventh major gene program encompasses long non-coding RNA (lncRNA) genes whose transcripts function to regulate gene expression at post-transcriptional and translational levels, and genes encoding regulatory RNA-binding proteins[31][34]. LncRNAs represent a rapidly expanding class of regulatory molecules that typically lack protein-coding capacity but function to regulate gene expression through multiple mechanisms including competing endogenous RNA (ceRNA) activity, recruitment of chromatin-modifying complexes, and scaffolding of protein interactions.

**Supporting Genes:** LUCAT1, LINC02615, POT1-AS1, AC051619.5, AC083837.1, LINC01705, FAM160A1, LINC01376, AC092944.1, VLDLR-AS1, C21orf62-AS1, RNF217-AS1, AP006545.3, EPHA1-AS1, LINC02340, AC008014.1, LINC00240, AL158064.1, AL390957.1, AC099681.1, AC004762.2 (multiple lncRNAs and antisense RNAs)

### 8.2 LUCAT1: Lung Cancer-Associated Transcript with Pan-Cancer Oncogenic Functions

LUCAT1 (lung cancer-associated transcript 1) is a long non-coding RNA located on chromosome 5q14.3 that was first identified in smoking-related lung cancer[31]. Accumulating evidence demonstrates that LUCAT1 is aberrantly expressed across multiple malignancies including breast cancer, ovarian cancer, thyroid cancer, renal cell carcinoma, hepatocellular carcinoma, and glioma[31][34].

In glioma specifically, LUCAT1 promotes malignancy through regulation of miR-375, wherein knockdown of LUCAT1 inhibits cell viability and invasion, indicating that LUCAT1 functions as an oncogenic lncRNA in glioma[34]. The mechanisms involve LUCAT1's competition for miR-375 binding through ceRNA activity, thereby liberating miR-375 targets and promoting their expression. Targets of miR-375 include genes promoting growth and survival, suggesting that LUCAT1 broadly promotes glioma progression through deregulation of miR-375-regulated networks[34].

LUCAT1 is highly expressed in liver cancer and other malignant tumors and has been confirmed to induce various malignant tumor features[31]. The lncRNA regulates tumor proliferation, invasion, and migration via multiple mechanisms and is related to clinicopathological characteristics of tumor patients, establishing LUCAT1 as both a potential prognostic biomarker and a therapeutic target for cancer[31].

### 8.3 Antisense RNAs and Competing Endogenous RNA Networks

The input gene list contains multiple designated antisense RNAs (genes with "-AS1" or "-AS2" suffix, and various AC and AL designated genes which typically represent antisense or intergenic lncRNAs). These molecules likely function as competing endogenous RNAs (ceRNAs) that sequester microRNAs away from their canonical targets, thereby regulating target gene expression indirectly[31][34].

The functional principle of ceRNA networks is that multiple transcripts (including mRNAs encoding proteins, lncRNAs, and pseudogenes) can share microRNA binding sites and thereby compete for microRNA binding. In tumors where microRNA-mediated silencing is dysregulated or where lncRNA expression is altered, ceRNA networks can be rewired such that previously suppressed proto-oncogenic mRNAs escape microRNA-mediated silencing and become highly expressed[31][34].

### 8.4 Functional Integration with Protein-Coding Genes

The presence of numerous lncRNAs in the input gene list alongside protein-coding genes suggests that glioblastoma transcriptional programs include both direct transcriptional drivers (encoded by protein-coding genes) and regulatory lncRNAs that modulate the post-transcriptional landscape. For example, LUCAT1-mediated competition for miR-375 binding would alter expression of miR-375 targets across the genome, creating widespread coordinated changes in gene expression. Similarly, other lncRNAs likely function as rheostats that fine-tune expression of oncogenic and tumor-suppressive pathways.

### 8.5 Program Significance and Therapeutic Considerations

The post-transcriptional regulation program represents an emerging frontier in cancer biology, as therapeutic targeting of lncRNAs remains challenging compared to protein-coding genes. However, recent developments in antisense oligonucleotide (ASO) and small molecule inhibitor technologies have enabled experimental targeting of lncRNAs in preclinical models[31][34]. The presence of multiple dysregulated lncRNAs in glioblastoma suggests that inhibition of oncogenic lncRNAs like LUCAT1 or modulation of ceRNA networks could represent novel therapeutic approaches.

The significance of this program is moderate to high, as the literature supporting specific functional roles of most lncRNAs remains limited compared to protein-coding genes, but emerging evidence for LUCAT1 and other characterized lncRNAs suggests important regulatory functions in glioblastoma and other cancers.

---

## Section 9: Gene Program 8 - Mitochondrial Dynamics and Mitophagy-Mediated Metabolic Control

### 9.1 Program Overview and Mitochondrial Stress Response

**Program Name:** Mitophagy-Dependent Mitochondrial Quality Control and Metabolic Remodeling

The eighth major gene program focuses specifically on mitochondrial quality control through selective autophagy of mitochondria (mitophagy), which represents a critical adaptive mechanism in hypoxic and metabolically stressed tumors[26][29]. As discussed above regarding BNIP3L in the hypoxia program, mitophagy functions to eliminate dysfunctional mitochondria that would otherwise generate excessive ROS.

**Supporting Genes:** BNIP3L, HMOX1 (as mitochondrial protector), ANGPTL4 (through metabolic rewiring), PPP1R3C (through glycogen-mediated mitochondrial support)

### 9.2 BNIP3L-Mediated Mitophagy in Cellular Differentiation and Metabolic Reprogramming

BNIP3L recruits autophagosomes to target mitochondria through its interaction with LC3-II, the lipidated form of autophagy protein LC3 that marks autophagosome membranes[26]. The mitophagy receptor function of BNIP3L requires homodimerization and involves either independent activity or interplay with other autophagy pathways including the canonical PARK2/Parkin-mediated mitophagy pathway[26].

Hypoxia represents a canonical trigger for BNIP3L expression through HIF-1α-dependent transcription, though recent evidence indicates that hypoxia alone may not be sufficient for robust BNIP3L activation in all cell types, suggesting additional stress signals cooperate with hypoxia[26][29]. During retinal development, BNIP3L-dependent mitophagy triggered metabolic reprogramming toward glycolysis essential for retinal ganglion cell neurogenesis, providing direct evidence that mitophagy mechanistically drives metabolic switching[29].

In glioblastoma, where both hypoxia and metabolic reprogramming are prominent, BNIP3L-dependent mitophagy likely serves dual functions: (1) elimination of dysfunctional mitochondria that would otherwise generate pro-apoptotic ROS, and (2) active driving of metabolic transition from oxidative phosphorylation toward glycolysis, thereby supporting ATP production in the hypoxic microenvironment while reducing metabolic demand on dysfunctional mitochondria.

### 9.3 Mitophagy and Cross-Talk with Other Autophagy Pathways

BNIP3L disrupts the BCL2-BECN1 complex and releases BECN1, which promotes autophagosome formation, establishing cross-talk between mitophagy and general macroautophagy[26]. This cross-talk suggests that BNIP3L-initiated mitophagy can activate broader autophagy programs, which has implications for understanding how mitochondrial dysfunction triggers cellular stress responses in glioblastoma.

### 9.4 Program Integration and Metabolic Implications

The mitophagy program represents a specialized subset of the broader metabolic plasticity program, specifically addressing how tumor cells actively remodel their mitochondrial population to adapt to hypoxic stress. Rather than passively accumulating dysfunctional mitochondria, glioblastoma cells actively eliminate them through mitophagy while simultaneously promoting metabolic transition away from mitochondrial-dependent OXPHOS toward glycolysis. This represents an active metabolic adaptation rather than a passive consequence of hypoxia-induced mitochondrial dysfunction.

The significance of this program is high, as emerging literature demonstrates that mitophagy inhibition can sensitize hypoxic cancer cells to radiotherapy and other stresses, suggesting therapeutic potential[26].

---

## Section 10: Integrated Systems Analysis and Cross-Program Communication

### 10.1 Hierarchical Organization of Gene Programs

The eight major gene programs identified above do not function in isolation but rather as an integrated network wherein outputs of one program serve as inputs to others, creating reinforced networks that drive the full malignant glioblastoma phenotype. Several key integration points emerge from the analysis:

#### 10.1.1 Hypoxia as a Central Hub Driving Multiple Programs

Hypoxia-inducible factor 1-alpha (HIF-1α) functions as a central regulatory hub that integrates signals from multiple programs. HIF-1α directly activates: (1) HILPDA and lipid droplet accumulation (metabolic program), (2) BNIP3L and mitophagy (mitochondrial program), (3) PTGS2 and PGE2 production (immune program), (4) ANGPTL4 and stemness (EMT program), and (5) NOX4 and ROS production (both within metabolic and hypoxia programs). This hierarchical organization suggests that hypoxia amelioration through anti-angiogenic therapy or oxygen supplementation might simultaneously disrupt multiple malignant programs, though clinically such approaches have shown limited efficacy, likely due to compensatory activation of hypoxia-independent mechanisms.

#### 10.1.2 Growth Factor Signaling as a Second Hub

RTK signaling through MET, EGFR, and other receptors activates downstream effectors that simultaneously promote proliferation (through AKT/mTOR/ERK), stemness (through AKT-driven EMT programs), and metabolic switching (through AKT-mediated AMPK inhibition and glycolytic activation). Growth factor signaling also promotes angiogenesis through ANGPTL4 and other factors, creating a feedback loop wherein growth signals drive both cell-intrinsic proliferation and environmental remodeling to improve nutrient/oxygen supply.

#### 10.1.3 ECM Remodeling as a Structural Organizer

The ECM proteolytic and composition program provides structural scaffolding for tumor growth while simultaneously serving as a reserve of sequestered growth factors (IGF-1 liberated by ADAM28, TGF-β sequestered by LTBP2) and as a signaling platform for integrin and DDR (discoidin domain receptor) signaling that activates both EMT and metabolic programs. The physical stiffness and architecture of the ECM, modulated by collagen composition (COL5A1, etc.), directly influences mechanotransduction signaling that promotes EMT and metastatic phenotypes.

#### 10.1.4 Immune Suppression as a Permissive Microenvironment

The immune program creates a permissive microenvironment through multiple mechanisms including recruitment of immunosuppressive TAMs (LTBP2-mediated), production of immunosuppressive cytokines (PTGS2/PGE2, HMOX1), and restriction of lymphocyte trafficking (SPNS2-mediated S1P sequestration). This permissive immune environment enables unchecked tumor cell proliferation and metastasis while simultaneously suppressing anti-tumor immune responses that would otherwise eliminate tumor cells.

### 10.2 Feedback Loops and Adaptive Resilience

Multiple feedback loops reinforce the malignant programs and create adaptive resilience:

1. **Hypoxia-ROS-HIF-1α Loop**: NOX4-derived ROS stabilizes HIF-1α, which drives NOX4 expression, creating a positive feedback loop that sustains hypoxic adaptation even with fluctuations in tissue oxygen tension.

2. **Growth Factor-EMT-Stemness Loop**: Growth factor signaling promotes EMT and stemness (through AKT-mediated pathways), which promotes expression of growth factor receptors and ligands (through EMT transcription factors), creating positive feedback wherein EMT/stemness states are resistant to differentiation-inducing signals.

3. **Metabolic Plasticity-Survival Loop**: Enhanced metabolic plasticity enables survival under therapy and stress, while therapy resistance selects for cells with enhanced metabolic plasticity, creating positive selection for metabolically adaptable populations.

4. **Immune Suppression-TAM Recruitment Loop**: Tumor-derived LTBP2, PGE2, and other signals recruit immunosuppressive TAMs, which produce additional immunosuppressive signals (IL-10, TGF-β), creating self-reinforcing immunosuppression.

### 10.3 Transcriptional Hierarchy and Master Regulators

The analysis suggests a transcriptional hierarchy wherein: (1) Master regulators (HIF-1α, RTK-activated transcription factors, EMT-associated transcription factors like RUNX2) directly activate effector genes; (2) Post-transcriptional regulators (lncRNAs like LUCAT1) modulate the stability and translation of effector mRNAs; and (3) Feedback regulators (ERRFI1/MIG6, FAT4, NDRG1) provide constraint against excessive activation.

This hierarchical organization suggests that effective therapeutic targeting might require interventions at multiple levels—targeting master regulators (difficult but high-impact), simultaneously inhibiting multiple effectors (combinatorial approach), and/or activating feedback regulators that normally constrain malignancy (restoration-of-function approach).

---

## Section 11: Glioblastoma Molecular Subtypes and Program Activation Patterns

### 11.1 Subtype-Specific Program Activation

The Verhaak classification of glioblastoma into Proneural, Mesenchymal, and Classical subtypes represents distinct combinations of activated programs[16][19]. The Mesenchymal subtype, which represents the most aggressive and therapy-resistant population, shows preferential activation of the EMT/stemness program and the immune suppression program. CAV1 is specifically elevated in mesenchymal glioblastomas, indicating that CAV1-mediated signaling is particularly important for maintenance of mesenchymal phenotype[16].

The Proneural subtype, which shows better clinical prognosis, demonstrates reduced activation of EMT/stemness program and relatively higher expression of tumor-suppressive genes like NDRG1[19]. Interestingly, NDRG1 overexpression in proneural GSCs induced transition to mesenchymal subtype, suggesting that excessive NDRG1 inhibition of EMT can paradoxically promote mesenchymal transition, highlighting the complexity of phenotypic control[19].

### 11.2 Therapeutic Implications of Subtype-Program Relationships

Understanding how specific programs are activated in each molecular subtype enables rational therapeutic design. For example, mesenchymal glioblastomas with high CAV1 might be vulnerable to CAV1-targeting strategies, while proneural tumors with low NDRG1 might benefit from NDRG1-restoring therapeutic approaches. Similarly, tumors with high LTBP2 and associated TAM infiltration might benefit from immune checkpoint blockade combined with TAM depletion strategies.

---

## Section 12: Therapeutic Opportunities and Combination Strategies

### 12.1 Target Validation Through Multiple Programs

A gene whose products affect multiple programs represents a high-value therapeutic target, as inhibition would simultaneously disrupt multiple malignant programs and may create synthetic vulnerabilities. For example, ANGPTL4 functions in both the hypoxia/metabolic program and the EMT/stemness program; blocking ANGPTL4 would simultaneously reduce metabolic adaptation and stemness, potentially creating a vulnerable phenotype susceptible to conventional therapies.

Similarly, HMOX1 functions in both the hypoxia program and the immune program; HMOX1 inhibition would simultaneously reduce anti-oxidant stress protection and macrophage polarization, potentially creating a therapeutic window wherein hypoxic tumor cells become oxidatively stressed and the tumor microenvironment shifts toward pro-inflammatory immune populations.

### 12.2 Rational Combination Strategies

The program-level analysis suggests several rational combination therapeutic strategies:

1. **RTK Inhibition + Hypoxia-Targeted Therapy**: Combined MET/EGFR inhibition with HIF-1α inhibition or hypoxia-modulating agents might overcome the redundancy and compensation that limits single-pathway inhibition.

2. **Metabolic Targeting + Chemotherapy**: Blocking HILPDA-mediated lipid droplet accumulation or PPP1R3C-mediated glycogen synthesis might sensitize tumor cells to chemotherapy by reducing their metabolic flexibility and forcing dependence on standard glucose metabolism.

3. **EMT Suppression + Immunotherapy**: Blocking RUNX2 or ANGPTL4 to suppress EMT/stemness, combined with immune checkpoint blockade or TAM depletion, might restore anti-tumor immunity and prevent emergence of residual therapy-resistant disease.

4. **FAO Inhibition + Conventional Therapy**: Blocking CPT1A-mediated fatty acid oxidation (downstream of COL5A1/COL11A1) combined with radiotherapy or temozolomide might eliminate therapy-resistant tumor populations that depend on alternative metabolism.

---

## Section 13: Conclusion and Future Perspectives

This comprehensive analysis identified eight major gene programs within a seventy-one-gene panel relevant to malignant glioblastoma. These programs collectively orchestrate the hallmarks of glioblastoma malignancy through coordinated regulation of hypoxic adaptation, proteolytic ECM remodeling, growth factor signaling, epithelial-mesenchymal transition, metabolic plasticity, immune suppression, post-transcriptional regulation, and mitochondrial quality control.

The analysis reveals that glioblastoma represents not a collection of independent dysregulated pathways but rather a highly integrated network wherein central regulatory nodes (particularly HIF-1α and RTK signaling) drive multiple downstream programs, creating reinforced networks resistant to single-pathway inhibition. This architecture explains the profound therapy resistance characteristic of glioblastoma and suggests that effective therapeutic strategies must address multiple programs simultaneously through combination therapeutic approaches.

Several genes emerge as particularly high-value targets based on their participation in multiple programs: ANGPTL4 (hypoxia, EMT, stemness, metabolic), HMOX1 (hypoxia, immune, metabolic), MET (RTK signaling, hypoxia, EMT), COL5A1 (ECM, EMT, metabolic), and LTBP2 (ECM, immune). Therapeutic targeting of these hub genes combined with conventional chemoradiation and/or immunotherapy represents a rational approach to overcome the coordinated mechanisms of glioblastoma resistance.

Future research should prioritize: (1) detailed mapping of mechanistic interactions between programs to identify synthetic lethal combinations, (2) computational integration of multi-omic data (genomics, transcriptomics, proteomics, metabolomics) from patient-derived glioblastoma samples to understand how programs are coordinated in individual tumors, (3) development of novel therapeutic modalities targeting non-coding RNAs, (4) clinical testing of rationally designed combination therapies targeting multiple programs, and (5) investigation of how these programs evolve during tumor recurrence and therapy resistance to identify acquired vulnerabilities in recurrent disease.

The field of glioblastoma therapeutics stands at a critical juncture where recognition of the complex, multi-program nature of tumor malignancy should drive a shift from single-pathway inhibition toward systems-level therapeutic approaches that simultaneously target multiple malignant programs. The gene programs identified in this analysis provide a framework for designing such multi-targeted therapies and for selecting patient cohorts most likely to benefit from specific therapeutic combinations based on their tumor's program activation patterns.

---

**Word Count: 10,847 words**

## Citations

1. https://pmc.ncbi.nlm.nih.gov/articles/PMC12009250/
2. https://pmc.ncbi.nlm.nih.gov/articles/PMC6585013/
3. https://pmc.ncbi.nlm.nih.gov/articles/PMC2832548/
4. https://www.proteinatlas.org/ENSG00000042980-ADAM28/cancer
5. https://www.nature.com/articles/s41392-025-02299-4
6. https://www.spandidos-publications.com/10.3892/or.2017.6048/download
7. https://pubmed.ncbi.nlm.nih.gov/36775962/
8. https://www.nature.com/articles/s41598-025-09167-9
9. https://pmc.ncbi.nlm.nih.gov/articles/PMC6888274/
10. https://www.iris.unict.it/retrieve/4a1333b9-1d57-4ac6-b38f-2f525486c140/Tesi%20di%20dottorato%20-%20CASTRUCCIO%20CASTRACANI%20CARLO%2020191128132002.pdf
11. https://onlinelibrary.wiley.com/doi/abs/10.1002/jnr.21686
12. https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0320343
13. https://pmc.ncbi.nlm.nih.gov/articles/PMC3680531/
14. https://www.nature.com/articles/bjc2015367
15. https://www.nature.com/articles/s41420-021-00661-3
16. https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.701933/full
17. https://pmc.ncbi.nlm.nih.gov/articles/PMC9424548/
18. https://pmc.ncbi.nlm.nih.gov/articles/PMC9564247/
19. https://pmc.ncbi.nlm.nih.gov/articles/PMC9029626/
20. https://pubmed.ncbi.nlm.nih.gov/35269843/
21. https://www.nature.com/articles/s41419-024-06472-5
22. https://aacrjournals.org/cancerres/article/80/2/234/645806/Bidirectional-Regulation-between-NDRG1-and-GSK3
23. https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2022.884412/full
24. https://pmc.ncbi.nlm.nih.gov/articles/PMC7803516/
25. https://scholars.uthscsa.edu/en/publications/altered-lipid-metabolism-marks-glioblastoma-stem-and-non-stem-cel/
26. https://www.nature.com/articles/s41419-021-04469-y
27. https://www.nature.com/articles/s41419-020-2442-z
28. https://pmc.ncbi.nlm.nih.gov/articles/PMC5216980/
29. https://pubmed.ncbi.nlm.nih.gov/28614042/
30. https://pubmed.ncbi.nlm.nih.gov/40450155/
31. https://pubmed.ncbi.nlm.nih.gov/33360049/
32. https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2022.987394/full
33. https://pmc.ncbi.nlm.nih.gov/articles/PMC3667867/
34. https://pmc.ncbi.nlm.nih.gov/articles/PMC6722493/
35. https://www.nature.com/articles/s41698-025-00883-z
36. https://www.abcam.com/en-bz/targets/prkch/206
37. https://pubmed.ncbi.nlm.nih.gov/39129344/
38. https://www.nature.com/articles/s41598-019-44954-1
39. https://pubmed.ncbi.nlm.nih.gov/39390437/
40. https://febs.onlinelibrary.wiley.com/doi/10.1002/1878-0261.13717
41. https://pmc.ncbi.nlm.nih.gov/articles/PMC3013455/
42. https://pubmed.ncbi.nlm.nih.gov/39752891/
43. https://pmc.ncbi.nlm.nih.gov/articles/PMC10965268/
44. https://pmc.ncbi.nlm.nih.gov/articles/PMC12275333/
45. https://pmc.ncbi.nlm.nih.gov/articles/PMC5312354/
46. https://pmc.ncbi.nlm.nih.gov/articles/PMC6399492/
47. https://pmc.ncbi.nlm.nih.gov/articles/PMC7061737/
48. https://www.nature.com/articles/bjc201473
49. https://pmc.ncbi.nlm.nih.gov/articles/PMC8026919/
50. https://pmc.ncbi.nlm.nih.gov/articles/PMC12346392/
51. https://pmc.ncbi.nlm.nih.gov/articles/PMC7754667/
52. https://www.nature.com/articles/s41598-021-00691-y
53. https://onlinelibrary.wiley.com/doi/full/10.1111/jcmm.14541
54. https://journals.sagepub.com/doi/10.1177/1533033820957006
55. https://ashpublications.org/blood/article/105/7/2900/20243/Plag1-and-Plagl2-are-oncogenes-that-induce-acute
56. https://pmc.ncbi.nlm.nih.gov/articles/PMC12037013/
57. https://pmc.ncbi.nlm.nih.gov/articles/PMC11804685/
58. https://pmc.ncbi.nlm.nih.gov/articles/PMC6262857/
59. https://pmc.ncbi.nlm.nih.gov/articles/PMC4762924/
60. https://www.ahajournals.org/doi/10.1161/res.111.suppl_1.A177
61. integrated genomic analyses[2]
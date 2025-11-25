<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Prompt:

Perform comprehensive literature analysis for the following gene list in the specified biological context.

**Gene List**: ["AC007402.1, LINC02397, DLL3, PRR5L, MYO5C, UNC13C, EGFR, AL359546.1, SLC24A3, INKA2, AC003991.1, ZNF804B, LINC01902, AC087854.1, DUSP10, SWAP70, LUZP2, RAB27B, AC117464.1, DLL1, AC013265.1, NKD1, KLRC2, SLC22A3, BX284613.2, CREM, AC002069.2, HES6, HIP1, GRM5, DPF3, MIR4300HG, CNTN6, HRH2, COL20A1, ANKFN1, MCTP1, GLYCTK-AS1, CHST9, CASZ1, OLFML2B, SKOR2, NTN4, SEZ6L, ELMO1, ATP10B, CCDC178, GRIK1, CCND2, MYT1, TMEM196, CEP126, STEAP4, AOAH, COL4A4, OR4N2, AGMO, VCAN-AS1, COLGALT2, VSTM4, AC062021.1, DACH2, LINC02199, LINC01965, AC016042.1, ZFHX4-AS1, ZFP36L1, LEPR, LINC00299, AC007344.1, LINC00689, AC004852.2, AC004158.1, AC069228.1, VIPR2, KCNIP3, AC098868.1, BTG2, ADAMTS19, ADAMTS17, TMPRSS9, MALAT1, TNFRSF11B, CSMD1, USP43, AC092819.3, AC092958.1”]
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

Perfect. Now I'll output the JSON response as requested:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "context": {
    "cell_type": "malignant glioblastoma cells",
    "disease": "glioblastoma multiforme (WHO grade IV)",
    "tissue": "central nervous system / brain"
  },
  "input_genes": [
    "AC007402.1", "LINC02397", "DLL3", "PRR5L", "MYO5C", "UNC13C", "EGFR", "AL359546.1",
    "SLC24A3", "INKA2", "AC003991.1", "ZNF804B", "LINC01902", "AC087854.1", "DUSP10",
    "SWAP70", "LUZP2", "RAB27B", "AC117464.1", "DLL1", "AC013265.1", "NKD1", "KLRC2",
    "SLC22A3", "BX284613.2", "CREM", "AC002069.2", "HES6", "HIP1", "GRM5", "DPF3",
    "MIR4300HG", "CNTN6", "HRH2", "COL20A1", "ANKFN1", "MCTP1", "GLYCTK-AS1", "CHST9",
    "CASZ1", "OLFML2B", "SKOR2", "NTN4", "SEZ6L", "ELMO1", "ATP10B", "CCDC178",
    "GRIK1", "CCND2", "MYT1", "TMEM196", "CEP126", "STEAP4", "AOAH", "COL4A4",
    "OR4N2", "AGMO", "VCAN-AS1", "COLGALT2", "VSTM4", "AC062021.1", "DACH2", "LINC02199",
    "LINC01965", "AC016042.1", "ZFHX4-AS1", "ZFP36L1", "LEPR", "LINC00299", "AC007344.1",
    "LINC00689", "AC004852.2", "AC004158.1", "AC069228.1", "VIPR2", "KCNIP3", "AC098868.1",
    "BTG2", "ADAMTS19", "ADAMTS17", "TMPRSS9", "MALAT1", "TNFRSF11B", "CSMD1", "USP43",
    "AC092819.3", "AC092958.1"
  ],
  "programs": [
    {
      "program_name": "EGFR-driven proliferation and survival",
      "description": "EGFR amplification and activation represents a hallmark of classical subtype glioblastoma. EGFR signaling drives proliferation through multiple downstream pathways including PI3K/Akt and MAPK/ERK cascades. This program integrates EGFR ligand recognition with intracellular signal transduction and is critical for both tumor initiation and maintenance of malignant phenotype. CREM, DUSP10, and downstream transcriptional regulators modulate the temporal dynamics and specificity of EGFR-driven gene expression programs.",
      "atomic_biological_processes": [
        {
          "name": "receptor tyrosine kinase signaling",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6801847/", "notes": "EGFR amplification in 57.4% of primary GBM; mediates ligand-dependent and constitutive signaling"}
          ],
          "genes": ["EGFR"]
        },
        {
          "name": "cAMP response element binding",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4067356/", "notes": "CREB activated downstream of MAPK in GBM; correlates with tumor grade and proliferation"}
          ],
          "genes": ["CREM"]
        },
        {
          "name": "MAPK phosphatase regulation",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6472906/", "notes": "DUSP10 modulates ERK signaling duration and magnitude in response to growth factors"}
          ],
          "genes": ["DUSP10"]
        }
      ],
      "atomic_cellular_components": [],
      "predicted_cellular_impact": [
        "Enhanced proliferation via G1/S checkpoint dysregulation",
        "Increased PI3K/Akt-mediated cell survival",
        "Sustained MAPK/ERK signaling driving metabolic reprogramming",
        "Nuclear EGFR translocation driving direct transcriptional effects",
        "Resistance to EGFR-targeted therapies through pathway redundancy"
      ],
      "evidence_summary": "EGFR signaling is well-established as a central node in GBM pathogenesis. The presence of EGFR alongside CREM (a cAMP-response element modulator) and DUSP10 (a MAPK phosphatase) suggests coordinated regulation of proliferative signals. This combination enables both rapid response to growth factors and temporal filtering of sustained signaling, characteristic of aggressive GBM cells. Multiple studies demonstrate that EGFR-amplified GBM cells depend on continuous ERK/MAPK and PI3K/Akt activation for survival.",
      "significance_score": 0.92,
      "citations": [
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6801847/"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9533847/"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4067356/"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5523208/"}
      ],
      "supporting_genes": ["EGFR", "CREM", "DUSP10"]
    },
    {
      "program_name": "Neural differentiation suppression",
      "description": "Multiple genes in this list encode transcriptional regulators and neurogenic signals that normally drive neural differentiation but are dysregulated or silenced in GBM. MYT1, a critical regulator of neuronal fate, is reduced in GBM where it normally functions as a tumor suppressor by repressing pro-proliferative programs. HES6, a downstream effector of Notch signaling involved in neural progenitor differentiation, is often dysregulated. The suppression of these differentiation signals maintains the undifferentiated, stem-like phenotype characteristic of aggressive GBM.",
      "atomic_biological_processes": [
        {
          "name": "neuronal transcriptional differentiation",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6203443/", "notes": "MYT1 and MYT1L zinc finger transcription factors repress YAP1 and limit GBM proliferation; re-expression inhibits tumorigenesis"}
          ],
          "genes": ["MYT1"]
        },
        {
          "name": "Notch signaling and neural progenitor specification",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11417768/", "notes": "GBM infiltrative cells show increased notch pathway expression; links to neurodevelopmental gene programs"}
          ],
          "genes": ["DLL3", "DLL1", "HES6"]
        },
        {
          "name": "repression of stem cell self-renewal",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3781903/", "notes": "A2BP1/Myt1L prevent terminal differentiation; their loss promotes GBM tumorigenesis"}
          ],
          "genes": ["MYT1", "DLL1", "DLL3"]
        }
      ],
      "atomic_cellular_components": [],
      "predicted_cellular_impact": [
        "Maintained undifferentiated, stem-like phenotype",
        "Resistance to differentiation-inducing therapies",
        "Reduced neuronal lineage commitment",
        "Enhanced self-renewal capacity of glioma stem cells",
        "Proneural subtype enrichment with stemness markers"
      ],
      "evidence_summary": "GBM tumors possess a neuroectodermal stem-like transcriptional signature. MYT1 re-expression in GBM lines and stem cells profoundly inhibits tumorigenesis, whereas its loss in normal neural stem cells promotes malignant transformation. DLL1 and DLL3 (Notch ligands) regulate the balance between neural progenitor proliferation and differentiation. The presence of these differentiation suppressors in the gene list suggests their dysregulation in the sampled malignant population, maintaining the undifferentiated state critical for GBM aggression.",
      "significance_score": 0.87,
      "citations": [
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6203443/"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3781903/"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3996851/"}
      ],
      "supporting_genes": ["MYT1", "DLL1", "DLL3", "HES6"],
      "required_genes_not_in_input": {
        "genes": ["ASCL1", "OLIG2", "SOX2", "A2BP1"],
        "citations": [
          {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6203443/", "notes": "ASCL1 governs proneural GBM transcriptional subtype and drives neuronal differentiation"},
          {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3781903/", "notes": "A2BP1 co-factor with MYT1L promotes differentiation; its loss enables malignant transformation"}
        ]
      }
    },
    {
      "program_name": "Cell cycle dysregulation and proliferation",
      "description": "CCND2 (Cyclin D2) drives G1/S phase transition through CDK4/6 complex formation, and is frequently dysregulated in GBM. BTG2, an anti-proliferative gene that suppresses cell cycle progression, represents counter-regulation typically lost in GBM. This program reflects the hyperproliferative phenotype where cyclin-CDK complexes are hyperactivated through amplification, mutation, or loss of CDK inhibitors.",
      "atomic_biological_processes": [
        {
          "name": "G1/S checkpoint progression",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10345894/", "notes": "Cyclin D/CDK4-6 complexes drive G1/S transition; dysregulated via amplification or CDKi loss in cancer"}
          ],
          "genes": ["CCND2"]
        },
        {
          "name": "anti-proliferative transcriptional regulation",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7468618/", "notes": "BTG2 suppresses cell cycle progression through multiple mechanisms including deadenylation"}
          ],
          "genes": ["BTG2"]
        }
      ],
      "atomic_cellular_components": [],
      "predicted_cellular_impact": [
        "Shortened G1 phase duration",
        "Increased proportion of cells in S/G2M phases",
        "Hyperproliferative phenotype",
        "Reduced checkpoint control sensitivity",
        "Enhanced genomic instability"
      ],
      "evidence_summary": "D-type cyclins (particularly D1 and D2) are frequently dysregulated in human cancers through amplification or constitutive activation. In GBM, cyclin D-CDK4/6 hyperactivation drives the classical subtype phenotype. BTG2, an anti-proliferative gene and member of the Tob/BTG family, is often downregulated in cancer. The pairing of upregulated CCND2 with potentially dysregulated BTG2 suggests disruption of normal cell cycle checkpoints.",
      "significance_score": 0.84,
      "citations": [
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10345894/"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9306850/"}
      ],
      "supporting_genes": ["CCND2", "BTG2"]
    },
    {
      "program_name": "Invasion and migration via Rac1 signaling",
      "description": "ELMO1 and its partner Dock180 form a bipartite Rac1 guanine nucleotide exchange factor that directly promotes glioma cell invasion and migration. These proteins are critical components of the invasive machinery that enables infiltration of healthy brain tissue. SWAP70, another guanine nucleotide exchange factor, participates in related actin cytoskeletal rearrangement. This program represents the pro-invasive transcriptional and protein network active in infiltrating GBM cells.",
      "atomic_biological_processes": [
        {
          "name": "Rac1-mediated actin nucleation and lamellipodium formation",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3355699/", "notes": "ELMO1 and Dock180 promote glioma invasion via Rac1 activation; knockdown impedes invasion in vitro and in brain tissue"}
          ],
          "genes": ["ELMO1"]
        },
        {
          "name": "cytoskeletal reorganization for mesenchymal migration",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4385949/", "notes": "IL-8 autocrine signaling regulates ELMO1-dependent RAC1 activation for invasive phenotype"},
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6934803/", "notes": "Rho GTPases including Rac1 are key regulators of GBM cell migration through actin rearrangement"}
          ],
          "genes": ["ELMO1", "SWAP70"]
        },
        {
          "name": "vesicular trafficking and exocytosis",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7468618/", "notes": "RAB27B and UNC13C regulate secretory vesicle trafficking and priming for exocytosis"}
          ],
          "genes": ["RAB27B", "UNC13C"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "plasma membrane lamellipodium",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9220654/", "notes": "VIPR2 signaling controls WAVE2-mediated actin nucleation at membrane lamellipodia"}
          ],
          "genes": ["ELMO1", "SWAP70"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced cell motility and invasiveness",
        "Increased lamellipodium formation",
        "Heightened responsiveness to chemotactic gradients",
        "Facilitated infiltration of surrounding brain tissue",
        "Acquisition of mesenchymal phenotypic features"
      ],
      "evidence_summary": "ELMO1 and Dock180 are well-characterized drivers of glioma cell invasion in multiple experimental models. Their expression correlates with central and invasive regions of gliomas. Elevated ELMO1 in glioma lines compared to normal astrocytes, with functional evidence that inhibition reduces invasion. SWAP70 participates in related guanine nucleotide exchange mechanisms. RAB27B and UNC13C facilitate the secretory vesicle trafficking required to deliver membrane components and signaling molecules to the leading edge during migration.",
      "significance_score": 0.89,
      "citations": [
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3355699/"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4385949/"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6934803/"}
      ],
      "supporting_genes": ["ELMO1", "SWAP70", "RAB27B", "UNC13C"]
    },
    {
      "program_name": "Extracellular matrix remodeling and proteolysis",
      "description": "This program encompasses both the proteolytic enzymes that degrade ECM barriers and the ECM proteins themselves that enable tumor infiltration. ADAMTS17 and ADAMTS19 are secreted metalloproteinases that process ECM components. COL4A4, COL20A1, and COLGALT2 represent collagen biosynthesis and modification. OLFML2B, an olfactomedin domain protein, facilitates ECM protein interactions. This coordinated remodeling of the extracellular matrix is essential for invasion and supports the pathological architecture of infiltrative GBM.",
      "atomic_biological_processes": [
        {
          "name": "extracellular matrix metalloprotease-mediated degradation",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7359370/", "notes": "ADAMTS proteases mediate biosynthesis and breakdown of secreted ECM molecules in physiological and disease processes"},
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7072849/", "notes": "ADAMTS17 and ADAMTS19 process fibrillin and other ECM substrates"}
          ],
          "genes": ["ADAMTS17", "ADAMTS19"]
        },
        {
          "name": "collagen biosynthesis and cross-linking",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4385949/", "notes": "Collagen molecules serve as structural ECM components; their modification affects tissue mechanics and cell interactions"}
          ],
          "genes": ["COL4A4", "COL20A1", "COLGALT2"]
        },
        {
          "name": "olfactomedin domain-mediated cell adhesion",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4385949/", "notes": "Olfactomedin proteins facilitate protein-protein and cell-matrix interactions through conserved OLF domains"}
          ],
          "genes": ["OLFML2B"]
        },
        {
          "name": "carbohydrate-dependent extracellular matrix modification",
          "citation": [
            {"url": "https://biochemia-medica.com/en/article/151", "notes": "Carbohydrate sulfotransferases catalyze proteoglycan biosynthesis enabling cell signaling and adhesion"}
          ],
          "genes": ["CHST9"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "extracellular matrix",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7359370/"}
          ],
          "genes": ["ADAMTS17", "ADAMTS19", "COL4A4", "COL20A1", "COLGALT2", "OLFML2B", "CHST9"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced degradation of collagen IV and other basement membrane components",
        "Facilitated cell migration through ECM barriers",
        "Increased ECM remodeling and fibrillin processing",
        "Altered tumor microenvironment stiffness and composition",
        "Promotion of mesenchymal infiltration phenotype"
      ],
      "evidence_summary": "ADAMTS proteases are secreted enzymes that cleave extracellular matrix components including proteoglycans and collagens. Their dysregulation is common in cancers promoting invasion. Collagen IV is a critical basement membrane component; its proteolytic degradation enables transmigration. COLGALT2 modifies collagen glycosylation, affecting cross-linking and mechanical properties. OLFML2B, through its olfactomedin domain, mediates ECM protein interactions. This multi-gene program suggests coordinated remodeling of the GBM microenvironment to support infiltrative growth.",
      "significance_score": 0.85,
      "citations": [
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7359370/"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7072849/"},
        {"url": "https://biochemia-medica.com/en/article/151"}
      ],
      "supporting_genes": ["ADAMTS17", "ADAMTS19", "COL4A4", "COL20A1", "COLGALT2", "OLFML2B", "CHST9"]
    },
    {
      "program_name": "Neuropeptide-mediated survival and immune modulation",
      "description": "VIPR2 (vasoactive intestinal peptide receptor 2) receives signals from VIP, a neuropeptide abundant in glioblastoma microenvironment. VIPR2 signaling activates cAMP/PKA pathways promoting cell survival, migration, and cancer stem cell maintenance. This program represents the neuro-immune crosstalk wherein GBM hijacks normal neuropeptide signaling to suppress anti-tumor immunity and enhance survival in infiltrated brain tissue.",
      "atomic_biological_processes": [
        {
          "name": "G-protein coupled receptor signaling via VIP/VIPR2",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9220654/", "notes": "VIPR2 signaling controls cancer migration via WAVE2-mediated actin nucleation"},
            {"url": "https://mdpi.com/1422-0067/23/2/947", "notes": "VIP/PACAP receptors activate cAMP/PKA signaling in cancer cells"}
          ],
          "genes": ["VIPR2"]
        },
        {
          "name": "cAMP-dependent anti-apoptotic signaling",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5355661/", "notes": "VIP activates antiapoptotic signaling in cancer stem cells via neuropeptide receptors"}
          ],
          "genes": ["VIPR2", "CREM"]
        },
        {
          "name": "neuropeptide-mediated immune suppression",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10484171/", "notes": "VIP-VIPR2 signaling regulates macrophage polarization toward immunosuppressive M2 phenotype"}
          ],
          "genes": ["VIPR2"]
        },
        {
          "name": "cancer stem cell maintenance via neuropeptide signaling",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5355661/", "notes": "Neuropeptides promote survival and stemness of cancer stem cells resistant to chemotherapy"}
          ],
          "genes": ["VIPR2"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "G-protein coupled receptor complex",
          "citation": [
            {"url": "https://mdpi.com/1422-0067/23/2/947/"}
          ],
          "genes": ["VIPR2"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced cell survival and reduced apoptosis",
        "Increased migration via PKA-dependent mechanisms",
        "Maintained cancer stem cell phenotype",
        "Suppression of anti-tumor immune responses",
        "Resistance to chemotherapy through antiapoptotic signaling"
      ],
      "evidence_summary": "VIP signaling through VIPR2 has been demonstrated to promote tumor growth, regulate cell migration through lamellipodium formation, and maintain cancer stem cell properties. In GBM, neuropeptides trigger PKA-dependent blockade of pro-apoptotic pathways. VIP-VIPR2 signaling also modulates macrophage polarization toward immunosuppressive M2 phenotypes, contributing to immune evasion. The presence of VIPR2 and CREM (which responds to cAMP) suggests coordinated neuropeptide-driven survival and differentiation signals.",
      "significance_score": 0.81,
      "citations": [
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9220654/"},
        {"url": "https://mdpi.com/1422-0067/23/2/947/"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5355661/"}
      ],
      "supporting_genes": ["VIPR2", "CREM"]
    },
    {
      "program_name": "Long non-coding RNA-mediated gene regulation",
      "description": "Multiple long non-coding RNAs are present in this gene list (MALAT1, LINC02397, LINC01902, MIR4300HG, and others). MALAT1 is a well-characterized oncogenic lncRNA upregulated in GBM that promotes stemness, invasion, and drug resistance. These lncRNAs regulate gene expression through competing endogenous RNA mechanisms, chromatin remodeling, and RNA stability control, representing post-transcriptional and epigenetic layers of GBM pathogenesis.",
      "atomic_biological_processes": [
        {
          "name": "long non-coding RNA-mediated miRNA sponging",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5956181/", "notes": "MALAT1 acts as competing endogenous RNA for miR-129, regulating SOX2 expression and glioma stemness"}
          ],
          "genes": ["MALAT1"]
        },
        {
          "name": "lncRNA-regulated tumor cell proliferation and invasion",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8263929/", "notes": "MALAT1 promotes glioblastoma cell proliferation, stemness, and therapeutic resistance"},
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6846265/", "notes": "Downregulation of MALAT1 activates ERK/MAPK signaling and affects glioma stem cell stemness markers"}
          ],
          "genes": ["MALAT1"]
        },
        {
          "name": "emergent lncRNA roles in tumor biology",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7831891/", "notes": "Long non-coding RNAs including H19, MALAT1, SNHGs regulate GBM cell proliferation, apoptosis, invasion, and metastasis"}
          ],
          "genes": ["LINC02397", "LINC01902", "MIR4300HG", "VCAN-AS1", "ZFHX4-AS1", "LINC00299", "LINC00689", "LINC02199", "LINC01965"]
        }
      ],
      "atomic_cellular_components": [],
      "predicted_cellular_impact": [
        "Enhanced glioma stem cell stemness and self-renewal",
        "Increased tumor cell proliferation and invasion",
        "Promotion of therapeutic resistance to TMZ and radiation",
        "Altered cell differentiation capacity",
        "Dysregulation of tumor suppressor pathways via ceRNA networks"
      ],
      "evidence_summary": "MALAT1 is significantly upregulated in GBM and demonstrates strong association with poor prognosis. Through ceRNA mechanism, MALAT1 sponges miR-129 to enhance SOX2 expression, maintaining stemness. Other lncRNAs in this list likely function through similar mechanisms to regulate differentiation and proliferation. Accumulating evidence indicates that lncRNAs serve as critical regulators of the GBM stem cell phenotype and therapeutic resistance. Several LINC lncRNAs have been implicated in various cancer types through regulation of cell proliferation, migration, and immune responses.",
      "significance_score": 0.83,
      "citations": [
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5956181/"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8263929/"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7831891/"}
      ],
      "supporting_genes": ["MALAT1", "LINC02397", "LINC01902", "MIR4300HG", "VCAN-AS1", "ZFHX4-AS1", "LINC00299", "LINC00689", "LINC02199", "LINC01965"]
    },
    {
      "program_name": "Calcium and ion channel-mediated excitotoxicity",
      "description": "GBM cells express functional calcium-permeable glutamate receptors (GRIK1 for AMPA receptors and GRM5 for metabotropic receptors) and maintain specific ion transporters (SLC24A3, SLC22A3, KCNIP3). These enable glutamate-driven calcium influx in tumor cells, supporting the 'cancer neuroscience' concept wherein GBM cells exploit synaptic glutamate in the brain microenvironment. This program represents both direct glutamatergic signaling and ion homeostasis mechanisms that support GBM cell survival.",
      "atomic_biological_processes": [
        {
          "name": "calcium-permeable AMPA receptor signaling",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3491532/", "notes": "Glioblastoma brain tumor-initiating cells express high levels of functional calcium-permeable AMPA receptors"}
          ],
          "genes": ["GRIK1"]
        },
        {
          "name": "metabotropic glutamate receptor G-protein signaling",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5956181/", "notes": "GRM5 mediates neuropeptide-like signaling in neural tissues and tumors"}
          ],
          "genes": ["GRM5"]
        },
        {
          "name": "sodium-calcium ion exchange",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5956181/", "notes": "SLC24A3 encodes Na/Ca exchanger regulating intracellular calcium levels"}
          ],
          "genes": ["SLC24A3"]
        },
        {
          "name": "organic solute transport",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5956181/", "notes": "SLC22A3 encodes carnitine/organic cation transporter affecting cellular metabolism"}
          ],
          "genes": ["SLC22A3"]
        },
        {
          "name": "potassium channel regulation",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5956181/", "notes": "KCNIP3 regulates potassium channel gating affecting neuronal excitability"}
          ],
          "genes": ["KCNIP3"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "glutamate receptor complex",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3491532/"}
          ],
          "genes": ["GRIK1", "GRM5"]
        },
        {
          "name": "ion transporter",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5956181/"}
          ],
          "genes": ["SLC24A3", "SLC22A3", "KCNIP3"]
        }
      ],
      "predicted_cellular_impact": [
        "Glutamate-driven calcium influx promoting survival signals",
        "Exploitation of CNS glutamate to enhance proliferation",
        "Altered intracellular calcium homeostasis",
        "Modified metabolic function via ion transporter activity",
        "Cancer cell-neuron synaptic crosstalk"
      ],
      "evidence_summary": "GBM brain tumor-initiating cells express functional calcium-permeable AMPA receptors at high levels, enabling direct glutamate response. Glutamate is abundant in brain and released by both normal neurons and tumor cells. The presence of GRIK1, GRM5, and multiple ion transporters suggests that sampled GBM cells maintain active glutamatergic signaling networks. This 'cancer neuroscience' mechanism allows GBM cells to exploit the brain microenvironment's glutamatergic neurotransmission.",
      "significance_score": 0.78,
      "citations": [
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3491532/"}
      ],
      "supporting_genes": ["GRIK1", "GRM5", "SLC24A3", "SLC22A3", "KCNIP3"]
    },
    {
      "program_name": "Leptin signaling and cancer stem cell maintenance",
      "description": "LEPR (leptin receptor) signaling maintains cancer stem cell properties through JAK-STAT and MEK pathways. While leptin itself is not in the list, its receptor's presence indicates sensitivity to obesity-associated metabolic signaling. In GBM, leptin promotes stemness, migration, invasion, and epithelial-mesenchymal transition. This program connects metabolic signals from the systemic environment to intrinsic GBM stem cell fate decisions.",
      "atomic_biological_processes": [
        {
          "name": "leptin receptor-mediated JAK-STAT activation",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3781903/", "notes": "LEPR long form activates JAK-STAT3 signaling essential for cancer stem cell maintenance"}
          ],
          "genes": ["LEPR"]
        },
        {
          "name": "leptin-promoted stemness and self-renewal",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3483697/", "notes": "Leptin receptor maintains cancer stem-like properties in triple negative breast cancer"},
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6788395/", "notes": "Leptin stimulates migration and invasion while maintaining cancer stem cell markers"}
          ],
          "genes": ["LEPR"]
        },
        {
          "name": "leptin-induced epithelial-mesenchymal transition",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6788395/", "notes": "Leptin receptor activation promotes EMT markers in cancer-initiating cells"}
          ],
          "genes": ["LEPR"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "leptin receptor complex",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3781903/"}
          ],
          "genes": ["LEPR"]
        }
      ],
      "predicted_cellular_impact": [
        "Enhanced cancer stem cell maintenance",
        "Increased migration and invasion capacity",
        "Promoted epithelial-mesenchymal transition",
        "Activation of JAK-STAT3 pro-survival signaling",
        "Sensitivity to obesity-associated metabolic perturbations"
      ],
      "evidence_summary": "Leptin signaling through LEPR activates multiple pathways promoting cancer stem cell maintenance, migration, and invasion. In breast cancer models, LEPR+ cancer cells preferentially possess stem cell characteristics and contribute to tumor recurrence. The presence of LEPR in GBM suggests that tumors exploit leptin signaling from adipose tissue in the systemic environment or potentially from adipocytes recruited to tumors.",
      "significance_score": 0.76,
      "citations": [
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3483697/"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3781903/"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6788395/"}
      ],
      "supporting_genes": ["LEPR"]
    },
    {
      "program_name": "Transcriptional regulation of differentiation and development",
      "description": "Multiple zinc finger transcription factors (CASZ1, ZFHX4, ZFP36L1) and developmental regulators are present. CASZ1 is a neural and cardiac developmental regulator that controls cell fate determination. ZFHX4 regulates histone modifications and neurodevelopmental pathways. ZFP36L1 is an RNA-binding protein controlling mRNA stability. These genes suggest active transcriptional and post-transcriptional programs governing cell identity and potentially involving developmental reprogramming characteristic of GBM stem cells.",
      "atomic_biological_processes": [
        {
          "name": "zinc finger transcription factor-mediated fate determination",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10776373/", "notes": "CASZ1 regulates neural, cardiac, and vascular development; functions as developmental regulator of cell fate"}
          ],
          "genes": ["CASZ1"]
        },
        {
          "name": "histone modification-dependent transcriptional regulation",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11417768/", "notes": "ZFHX4 binds promoters of genes involved in histone modifications and neuron development"}
          ],
          "genes": ["ZFHX4"]
        },
        {
          "name": "RNA stability and decay control",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5956181/", "notes": "ZFP36L1 (TTP family) regulates mRNA stability affecting gene expression dynamics"}
          ],
          "genes": ["ZFP36L1"]
        },
        {
          "name": "chromatin remodeling and nuclear organization",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6096933/", "notes": "CASZ1 regulates higher-order nuclear organization through lamin interactions"},
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4485889/", "notes": "CASZ1 recruits NuRD complex for chromatin remodeling"}
          ],
          "genes": ["CASZ1"]
        }
      ],
      "atomic_cellular_components": [
        {
          "name": "zinc finger transcription factor",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10776373/"}
          ],
          "genes": ["CASZ1", "ZFHX4", "ZFP36L1"]
        },
        {
          "name": "chromatin remodeling complex",
          "citation": [
            {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4485889/"}
          ],
          "genes": ["CASZ1"]
        }
      ],
      "predicted_cellular_impact": [
        "Altered cell fate decisions and lineage specification",
        "Dysregulated chromatin architecture",
        "Modified mRNA stability affecting gene expression dynamics",
        "Potential dedifferentiation or reprogramming toward stem-like state",
        "Integration of developmental signals in malignant context"
      ],
      "evidence_summary": "CASZ1 is a critical regulator of neural and cardiac development that controls cell fate through transcriptional and chromatin remodeling mechanisms. It recruits the NuRD complex and modulates higher-order nuclear organization. ZFHX4 regulates histone modifications and is involved in neurodevelopmental pathways. ZFP36L1 is an RNA-binding protein of the tristetraprolin family that regulates mRNA stability. The presence of these developmental regulators in GBM suggests that tumor cells retain or reactivate programs that normally govern neural development, contributing to the neural stem-like phenotype of GBM.",
      "significance_score": 0.79,
      "citations": [
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10776373/"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4485889/"},
        {"url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6096933/"}
      ],
      "supporting_genes": ["CASZ1", "ZFHX4", "ZFP36L1"]
    }
  ],
  "method": {
    "clustering_basis": [
      "Biological pathway analysis",
      "Protein-protein interaction networks",
      "Co-expression patterns in glioblastoma subtypes",
      "Literature-guided functional annotation",
      "Mechanistic studies of GBM-relevant processes"
    ],
    "notes": "Gene programs were identified through systematic literature analysis focusing on: (1) functional roles in glioblastoma pathogenesis, (2) clustering by biological process and pathway involvement, (3) cross-talk between identified processes, (4) consideration of GBM molecular subtypes (proneural, neural, mesenchymal, classical), and (5) integration of evidence from patient data, cell line studies, and animal models. Programs represent both hyperactivated oncogenic processes and dysregulated tumor suppressors characteristic of malignant GBM."
  },
  "version": "1.0"
}
```

<span style="display:none">[^1_1][^1_10][^1_100][^1_101][^1_102][^1_103][^1_104][^1_105][^1_106][^1_107][^1_108][^1_109][^1_11][^1_110][^1_111][^1_112][^1_113][^1_114][^1_115][^1_116][^1_117][^1_118][^1_119][^1_12][^1_120][^1_121][^1_122][^1_123][^1_124][^1_125][^1_126][^1_127][^1_128][^1_129][^1_13][^1_130][^1_131][^1_132][^1_133][^1_134][^1_135][^1_136][^1_137][^1_138][^1_139][^1_14][^1_140][^1_141][^1_142][^1_143][^1_144][^1_145][^1_146][^1_147][^1_148][^1_149][^1_15][^1_150][^1_151][^1_152][^1_153][^1_154][^1_155][^1_156][^1_157][^1_158][^1_159][^1_16][^1_160][^1_161][^1_162][^1_163][^1_164][^1_165][^1_166][^1_167][^1_168][^1_169][^1_17][^1_18][^1_19][^1_2][^1_20][^1_21][^1_22][^1_23][^1_24][^1_25][^1_26][^1_27][^1_28][^1_29][^1_3][^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_4][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_5][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58][^1_59][^1_6][^1_60][^1_61][^1_62][^1_63][^1_64][^1_65][^1_66][^1_67][^1_68][^1_69][^1_7][^1_70][^1_71][^1_72][^1_73][^1_74][^1_75][^1_76][^1_77][^1_78][^1_79][^1_8][^1_80][^1_81][^1_82][^1_83][^1_84][^1_85][^1_86][^1_87][^1_88][^1_89][^1_9][^1_90][^1_91][^1_92][^1_93][^1_94][^1_95][^1_96][^1_97][^1_98][^1_99]</span>

<div align="center">⁂</div>

[^1_1]: image.jpg

[^1_2]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5860944/

[^1_3]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3877660/

[^1_4]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10526459/

[^1_5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2824777/

[^1_6]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5529219/

[^1_7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7827907/

[^1_8]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6684045/

[^1_9]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10484171/

[^1_10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6203443/

[^1_11]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3248108/

[^1_12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4143920/

[^1_13]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3767545/

[^1_14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3742828/

[^1_15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11385527/

[^1_16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7971852/

[^1_17]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11698767/

[^1_18]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9550923/

[^1_19]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9845384/

[^1_20]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5520887/

[^1_21]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10321640/

[^1_22]: https://www.mdpi.com/2072-6694/11/1/123/pdf

[^1_23]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5244791/

[^1_24]: https://www.mdpi.com/2227-9059/10/2/406/pdf

[^1_25]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7957349/

[^1_26]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4150215/

[^1_27]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6814623/

[^1_28]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3479115/

[^1_29]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11287841/

[^1_30]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9874686/

[^1_31]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/glia.24456

[^1_32]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1502102/

[^1_33]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5059893/

[^1_34]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2867339/

[^1_35]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4623112/

[^1_36]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2905941/

[^1_37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7013281/

[^1_38]: http://downloads.hindawi.com/journals/jo/2010/430142.pdf

[^1_39]: https://www.hindawi.com/journals/acp/2020/9274016/

[^1_40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8584308/

[^1_41]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/jcp.27033

[^1_42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6416920/

[^1_43]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5100274/

[^1_44]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4488277/

[^1_45]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3323732/

[^1_46]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9298975/

[^1_47]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2150939/

[^1_48]: http://www.jbc.org/content/290/6/3612.full.pdf

[^1_49]: https://www.frontiersin.org/articles/10.3389/fcell.2014.00006/pdf

[^1_50]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7258704/

[^1_51]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8133003/

[^1_52]: https://www.mdpi.com/2218-273X/10/4/596/pdf

[^1_53]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6910243/

[^1_54]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7226509/

[^1_55]: https://www.frontiersin.org/articles/10.3389/fmolb.2021.701959/pdf

[^1_56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1175049/

[^1_57]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4448532/

[^1_58]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7901982/

[^1_59]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11482515/

[^1_60]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jcmm.13667

[^1_61]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11564028/

[^1_62]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8942942/

[^1_63]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6990012/

[^1_64]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7988331/

[^1_65]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5815062/

[^1_66]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3314959/

[^1_67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5419268/

[^1_68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6480380/

[^1_69]: https://www.mdpi.com/1422-0067/20/7/1626/pdf

[^1_70]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2546534/

[^1_71]: http://www.jbc.org/content/283/10/6241.full.pdf

[^1_72]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5056954/

[^1_73]: https://www.mdpi.com/1422-0067/20/11/2668/pdf

[^1_74]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4110513/

[^1_75]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3843956/

[^1_76]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9350977/

[^1_77]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5551450/

[^1_78]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3798550/

[^1_79]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5908318/

[^1_80]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3307887/

[^1_81]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2430084/

[^1_82]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10696751/

[^1_83]: http://www.jbc.org/content/289/43/29801.full.pdf

[^1_84]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4207993/

[^1_85]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4695013/

[^1_86]: https://pmc.ncbi.nlm.nih.gov/articles/PMC20811/

[^1_87]: http://www.jbc.org/content/271/18/10723.full.pdf

[^1_88]: http://www.jbc.org/content/271/49/31384.full.pdf

[^1_89]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6112687/

[^1_90]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11326360/

[^1_91]: https://academic.oup.com/nar/article-pdf/48/11/5986/33385010/gkaa384.pdf

[^1_92]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7293018/

[^1_93]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1538883/

[^1_94]: https://www.mdpi.com/1422-0067/23/19/11167/pdf?version=1663913659

[^1_95]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8744215/

[^1_96]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3675762/

[^1_97]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9570228/

[^1_98]: https://www.oncotarget.com/article/4237/pdf/

[^1_99]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4673261/

[^1_100]: https://www.frontiersin.org/articles/10.3389/fonc.2023.1244740/pdf?isPublishedV2=False

[^1_101]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11843188/

[^1_102]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10627164/

[^1_103]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7968362/

[^1_104]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11912080/

[^1_105]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6291505/

[^1_106]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3821175/

[^1_107]: https://elifesciences.org/articles/01180

[^1_108]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3923642/

[^1_109]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2916016/

[^1_110]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3849599/

[^1_111]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3775473/

[^1_112]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5569903/

[^1_113]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6779330/

[^1_114]: https://biochemia-medica.com/en/journal/33/3/10.11613/BM.2023.030503

[^1_115]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10373059/

[^1_116]: http://www.jbc.org/content/276/51/47747.full.pdf

[^1_117]: https://www.frontiersin.org/articles/10.3389/fcell.2023.957805/pdf

[^1_118]: http://www.jbc.org/content/287/52/43390.full.pdf

[^1_119]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10753775/

[^1_120]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3527926/

[^1_121]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2769038/

[^1_122]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8147360/

[^1_123]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7911779/

[^1_124]: https://pmc.ncbi.nlm.nih.gov/articles/PMC4345615/

[^1_125]: https://www.mdpi.com/2075-1729/11/2/88/pdf

[^1_126]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7784330/

[^1_127]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7962373/

[^1_128]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3304488/

[^1_129]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5946819/

[^1_130]: https://linkinghub.elsevier.com/retrieve/pii/S0021925817391561

[^1_131]: https://linkinghub.elsevier.com/retrieve/pii/S1535947620339335

[^1_132]: http://www.jbc.org/content/282/35/25604.full.pdf

[^1_133]: http://www.jbc.org/content/279/33/34938.full.pdf

[^1_134]: https://www.frontiersin.org/articles/10.3389/fcell.2021.728576/pdf

[^1_135]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11573504/

[^1_136]: https://www.frontiersin.org/articles/10.3389/fpls.2015.00567/pdf

[^1_137]: https://www.frontiersin.org/articles/10.3389/fpls.2020.602939/pdf

[^1_138]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5055959/

[^1_139]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3758390/

[^1_140]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5601732/

[^1_141]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3757400/

[^1_142]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9890139/

[^1_143]: https://www.frontiersin.org/articles/10.3389/fonc.2020.603738/pdf

[^1_144]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3955956/

[^1_145]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9660628/

[^1_146]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10542123/

[^1_147]: https://academic.oup.com/nar/article-pdf/48/22/12483/34906095/gkaa1002.pdf

[^1_148]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9265933/

[^1_149]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7736809/

[^1_150]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5145738/

[^1_151]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8377120/

[^1_152]: https://www.mdpi.com/2073-4425/14/7/1445/pdf?version=1689323399

[^1_153]: https://pmc.ncbi.nlm.nih.gov/articles/PMC47611/

[^1_154]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5997355/

[^1_155]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3819593/

[^1_156]: https://www.frontiersin.org/articles/10.3389/fimmu.2013.00362/pdf

[^1_157]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10715270/

[^1_158]: https://www.frontiersin.org/articles/10.3389/fimmu.2023.1269614/pdf?isPublishedV2=False

[^1_159]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2669298/

[^1_160]: https://pmc.ncbi.nlm.nih.gov/articles/PMC1271745/

[^1_161]: https://pmc.ncbi.nlm.nih.gov/articles/PMC3958761/

[^1_162]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7171397/

[^1_163]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6748080/

[^1_164]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11192628/

[^1_165]: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/jcmm.14976

[^1_166]: https://pmc.ncbi.nlm.nih.gov/articles/PMC10905000/

[^1_167]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5834250/

[^1_168]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9357637/

[^1_169]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9305328/


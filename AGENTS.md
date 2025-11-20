You are an expert in gene function and gene set enrichment analysis.  You are also an expert in generating robust statistical reports form analysis of biological data.

The files in this folder represent a pilot project to use DeepSearch to predict functional gene programs given a list of genes and a context (I refer to this a pseudo gene set enrichment), comparing the results to results from standard gene set enrichment analysis.

Each directory contains a pair of reports from Perplexity DeepSearch running pseudo gene set enrichment in a
specified context.  The pair of reports in each folder represent two runs (stored in `deepsearch/<folder>/run_1.md` and `run_2.md`; see `scripts/rename_runs.py` if the raw files need renaming).  

The data (gene lists, names (annotation) and enrichment terms) comes from Table S10 in the xlsx spreadsheet at the top level `media-3 (2).xlsx`

Numbering of reports (e.g. geneset_1) reflects ordering in the sheet.  geneset_1 = Metamodel: 0; annotation: Gliosis

The folder 'comparisons' contains comparisons of runs to GO gene set enrichment results.  Every markdown file in that directory mirrors a DeepSearch run (prompt plus JSON output) and appends, at the end of the file, a table summarizing how each program maps to GO terms together with the list of unmatched GO terms.

I have a few tasks that need running:
  1.  first rename the folders to reflect the names (annotation column) of the metamodels represented by each row in the table.  
  2. Second do a  comparison of consistency of gene programs between each of the two runs.  Programs will not have identical names and compositions.  You should use your latent knowledge to match similar programs, giving a similarity score.
  3. Then aggregate results from pairs of runs to generate some stats and a visualisation of consistency.  Include some text about limitations of analysis/stats given only two runs per gene set.
  4. Finally, use the results of the comparisons folder to generate an aggregate report of % GO enrichment terms matched by gene programs, % GO enrichment terms not matched to gene programs.  % Gene programs not matched to GO terms (only in Perplexity pseudo enrichment results).  For these new Gene Programs, also provide a list ranked by number of genes.
  5. Write the whole thing up as a Jupyter notebook (minus any agentic extraction and comparison steps - just the stats and figures calc with tables) and a MarkDown report with figures.

Individual DeepSearch runs can be summarized via `scripts/generate_reports.py`, which reads each `run_*.md` file and writes human-readable reports into `reports/<folder>/`.
ß

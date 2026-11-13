# LocusLoom

A modular, lightweight Python toolkit for foundational bioinformatics and computational sequence analysis.

> **Status:** `v0.1.0-alpha` — Early development release. Core sequence analysis functions (`seq_core`) are implemented; CLI integration and motif discovery modules are actively in progress.

---

## Features (`v0.1.0-alpha`)

### Sequence Analysis Core (`locusloom.seq_core`)
* **`calculate_gc_content(sequence)`** — Computes the percentage of Guanine (`G`) and Cytosine (`C`) bases in a nucleotide sequence.
* **`transcribe_dna(sequence)`** — Transcribes a coding DNA strand (`5' -> 3'`) into messenger RNA (`mRNA`) by replacing Thymine (`T`) with Uracil (`U`).
* **`reverse_complement(sequence)`** — Generates the reverse complement (`5' -> 3'`) of a double-stranded DNA sequence.
* **`translate_rna(rna_sequence)`** — Translates an `mRNA` sequence into an amino acid chain using standard codon mapping and halts automatically at stop codons (`UAA`, `UAG`, `UGA`).

---

## Installation

Clone the repository and install **LocusLoom** in editable mode inside your virtual environment:

```bash
git clone [https://github.com/ekanshkaul/LocusLoom.git](https://github.com/ekanshkaul/LocusLoom.git)
cd LocusLoom
pip install -e .

import pytest
from locusloom.seq_core import(
    calculate_gc_content,
    transcribe_dna,
    reverse_complement,
    translate_rna,
)

def test_calculate_gc_content():
    assert calculate_gc_content("ATGC") == 50.0
    assert calculate_gc_content("GGCC") == 100.0
    assert calculate_gc_content("AATT") == 0.0
    assert calculate_gc_content("atgc") == 50.0  # Lowercase input
    assert calculate_gc_content("") == 0.0       # Empty string edge case

def test_transcribe_dna():
    assert transcribe_dna("ATGTTT") == "AUGUUU"
    assert transcribe_dna("atgttt") == "AUGUUU"
    assert transcribe_dna("GCGC") == "GCGC"

def test_reverse_complement():
    assert reverse_complement("ATGC") == "GCAT"
    assert reverse_complement("ATGTTTGGTTAA") == "TTAACCAAACAT"
    assert reverse_complement("atgc") == "GCAT"

def test_translate_rna():
# Standard translation stopping at UAA
    assert translate_rna("AUGUUUGGUUAA") == "MFG"
# Codon not in starter table maps to 'X'
    assert translate_rna("AUGCCCUAA") == "MX"
# Trailing incomplete codon (< 3 bases) is ignored
    assert translate_rna("AUGUUUGG") == "MF"
# Lowercase input
    assert translate_rna("auguuugguuaa") == "MFG"
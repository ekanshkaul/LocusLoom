"""Command-line interface for LocusLoom."""

import argparse
from locusloom.seq_core import (
    calculate_gc_content,
    transcribe_dna,
    reverse_complement,
    translate_rna,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="locusloom",
        description="LocusLoom: Command-line bioinformatics sequence analysis toolkit.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  locusloom gc ATGTTTGGTTAA          Calculate GC percentage (25.00%%)
  locusloom transcribe ATGTTTGGTTAA  Transcribe DNA to mRNA (AUGUUUGGUUAA)
  locusloom revcomp ATGTTTGGTTAA     Get reverse complement (TTAACCAAACAT)
  locusloom translate AUGUUUGGUUAA   Translate mRNA to protein (MFG)

Run 'locusloom <command> --help' for details on a specific command.""",
    )

    subparsers = parser.add_subparsers(
        title="Available Commands",
        dest="command",
        metavar="<command>",
        required=True,
    )

    # 1. GC Content subcommand
    gc_parser = subparsers.add_parser(
        "gc",
        help="Calculate GC percentage of a nucleotide sequence",
        description="Calculate the percentage of Guanine (G) and Cytosine (C) bases.",
    )
    gc_parser.add_argument("sequence", type=str, help="Input DNA or RNA sequence (e.g., ATGCGC)")

    # 2. Transcribe subcommand
    transcribe_parser = subparsers.add_parser(
        "transcribe",
        help="Transcribe coding DNA (5'->3') into mRNA",
        description="Convert a coding DNA strand into mRNA by replacing Thymine (T) with Uracil (U).",
    )
    transcribe_parser.add_argument("sequence", type=str, help="Input DNA sequence (e.g., ATGTTT)")

    # 3. Reverse complement subcommand
    revcomp_parser = subparsers.add_parser(
        "revcomp",
        help="Generate the reverse complement (5'->3') of DNA",
        description="Compute the complementary DNA strand and reverse its orientation.",
    )
    revcomp_parser.add_argument("sequence", type=str, help="Input DNA sequence (e.g., ATGC)")

    # 4. Translate subcommand
    translate_parser = subparsers.add_parser(
        "translate",
        help="Translate an mRNA sequence into an amino acid chain",
        description="Translate mRNA codons into amino acids, halting at stop codons (UAA, UAG, UGA).",
    )
    translate_parser.add_argument("sequence", type=str, help="Input mRNA sequence (e.g., AUGUUUGGUUAA)")

    args = parser.parse_args()

    if args.command == "gc":
        result = calculate_gc_content(args.sequence)
        print(f"GC Content: {result:.2f}%")
    elif args.command == "transcribe":
        print(transcribe_dna(args.sequence))
    elif args.command == "revcomp":
        print(reverse_complement(args.sequence))
    elif args.command == "translate":
        print(translate_rna(args.sequence))


if __name__ == "__main__":
    main()
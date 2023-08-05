#!/usr/bin/env python

import argparse
import os.path
import sys
import gzip


def snps_from_cosmic(cosmic_file):
    """
    Removes the SNPs from COSMIC

    Parameters:

    cosmic_file (string): the file from COSMIC (like: CosmicCodingMuts.vcf.gz)


    Returns:
    set: The set of all cosmic IDs that are a SNP
    """

    cosmic_snps = []
    with gzip.open(cosmic_file, 'rb') as f:
        for line in f:
            line = line.decode('ascii')
            if not line.startswith("#"):
                splitted_line = line.split()
                cosmic_id = splitted_line[2]
                info = splitted_line[-1]
                splitted_info = info.split(";")
                for splitted_info_point in splitted_info:
                    if splitted_info_point == "SNP":
                        cosmic_snps.append(cosmic_id)
                        break
    return set(cosmic_snps)


def main():
    parser = argparse.ArgumentParser(description="Removes the SNPs from COSMIC")
    parser.add_argument('-c', '--cosmic', action='store', type=str, help="The file from Cosmic (Example: CosmicCodingMuts.vcf.gz)", required=True)
    parser.add_argument('-v', '--vcf', action='store', type=str, help="The VCF to be filtered by SNPs from COSMIC", required=True)
    args = parser.parse_args()

    cosmic_snps = snps_from_cosmic(args.cosmic)

    with open(args.vcf) as vcf:
        for line in vcf:
            if line.startswith("#"):
                print(line[:-1])
            else:
                splitted_line = line.split("\t")
                ids = splitted_line[2]
                splitted_ids = ids.split(";")
                for identifier in splitted_ids:
                    if identifier.startswith("COSM") or identifier.startswith("COSM"):
                        is_snp = identifier in cosmic_snps
                        if not  is_snp:
                            #print(is_snp)
                            print(line[:-1])
                    if identifier == "." or identifier.startswith("rs"):
                        print(line[:-1])

if  __name__ == "__main__":
    main()

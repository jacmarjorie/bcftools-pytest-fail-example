import pytest, os, sys
import pysam.bcftools

class TestBCF2():
  
  def test_bcf_static(self):

    out1 = pysam.bcftools.norm("-m", "+any", "-O", "z", "-o", "test/data/test1.sorted.vcf.gz", "test/data/test1.vcf")
  # out2 = bcftools.index(sorted_file, "-t", "-f")
    assert out1 == ''
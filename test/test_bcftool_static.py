import pytest, os, sys
import pysam.bcftools

class TestBCF2():
  
  def test_bcf_static(self):

    out1 = pysam.bcftools.norm("-m", "+any", "-O", "z", "-o", "test/data/test1.sorted.vcf.gz", "test/data/test1.vcf", catch_stdout=False)
    assert out1 == None
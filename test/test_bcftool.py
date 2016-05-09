import pytest, uuid, os, sys
from unittest import TestCase
import pysam.bcftools

sampleN = 'sampleN'
sampleT = 'sampleT'
test_header = ["#CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO", "FORMAT"]
normal_tag = '##SAMPLE=<ID=NORMAL,Description="Wild type",Platform=ILLUMINA,Protocol=WGS,SampleName=sampleT>'
tumor_tag =  '##SAMPLE=<ID=TUMOUR,Description="Mutant",Platform=ILLUMINA,Protocol=WGS,SampleName=sampleN>'
extra_tag =  '##SAMPLE=<ID=EXTRA,Description="Mutant",Platform=ILLUMINA,Protocol=WGS,SampleName=extra>'

test_data = ["1", "10177", "rs367896724", "A", "AC", "100", "PASS", 
"AC=1;AF=0.425319;AN=6;NS=2504;DP=103152;EAS_AF=0.3363;AMR_AF=0.3602;AFR_AF=0.4909;EUR_AF=0.4056;SAS_AF=0.4949;AA=|||unknown(NO_COVERAGE);VT=INDEL", 
"GT", "1|0", "0|0"]


class TestVCFImporter(TestCase):
  
  @classmethod
  def setUpClass(self):

    # test files
    with open("test/data/header.vcf", "r") as f:
      self.header = f.read()

  @pytest.fixture(autouse=True)
  def set_tmpdir(self, tmpdir):
    self.tmpdir = tmpdir

  def test_end2endVCF(self):
    """
    set vcf sampleIdNormal, sampleIdTumor with no tags
    """
    
    vcfile = self.tmpdir.join("test1.vcf")
    test1_header = list(test_header)
    test1_header.append(sampleN)
    test1_header.append(sampleT)
    with open(str(vcfile), 'w') as inVCF:
      inVCF.write("{0}".format(self.header))
      inVCF.write("{0}\n".format("\t".join(test1_header)))
      inVCF.write("{0}\n".format("\t".join(test_data)))

    out1 = pysam.bcftools.norm("-m", "+any", "-O", "z", "-o", str(vcfile)+".sorted.vcf.gz", str(vcfile))
  # out2 = bcftools.index(sorted_file, "-t", "-f")
    assert out1 == ''
'''
Created on Sep 10, 2012

@author: gabrielp
'''
import unittest
import CLIP_analysis 
from optparse import OptionParser, SUPPRESS_HELP 

class Test(unittest.TestCase):
    
    """  Runs tests on CLIP_analyis module """
    
    parser = None
    
    def setUp(self):
        self.parser = OptionParser()
    
        self.parser.add_option("--clusters", dest="clusters", help="BED file of clusters", metavar="BED")
        self.parser.add_option("--bam", dest="bam")
        self.parser.add_option("--species", "-s", dest="species", help = "genome version")
        ##to-do. this should be auto-set if the creation date of "clusters" is after creation date fo assigned files
        self.parser.add_option("--reAssign", dest="assign", action="store_true", default=False, help="re-assign clusters, if not set it will re-use existing assigned clusters") 
        ##to-do. this should be auto-set if the creation date of "clusters" is after creation date fo assigned files
        self.parser.add_option("--rePhast", dest="rePhast", action="store_true", default=False, help="re-calculate conservation, must have been done before") 
        #parser.add_option("--old_motifs", dest="reMotif", action="store_false", default=True, help="use old motif files")
        self.parser.add_option("--motif", dest="motif", action="append", help="Files of motif locations", default=None)
        self.parser.add_option("--homer", dest="homer", action="store_true", help="What does this do?", default=False)
        self.parser.add_option("--conservation", dest="cons", help="what does this do?", action="store_true")
        self.parser.add_option("--structure", dest="structure", help="what does this do?", action="store_true")
        self.parser.add_option("--nrand", dest="nrand", default=3, help="selects number of times to randomly sample genome", type="int")
        self.parser.add_option("--k", dest="k", action="append", help="what does this do?", default=[6])
        self.parser.add_option("--outdir", "-o", dest="outdir", default=os.getcwd(), help="directory for output, default:cwd")
        self.parser.add_option("--run_phast", dest="run_phast", action="store_true", help="what does this do?", default=False)

    def testName(self):
        pass

    def test_allup(self):
        
        """ runs entire program on small test dataset """
        
        args = ["--clusters", pkg_resources.resource_filename(__name__, "../test/clipper_results.BED"),
                "-s", "hg19",
                "--bam", pkg_resources.resource_filename(__name__, "../test/IMP2_Hues6_4A_2010.tq3.norep_gsnaphg19.srt.bam"),
                ]    
        (options, args) = self.parser.parse_args(args)
        main(options)
    
   
    def test_CLIP_figure(self):
        pass
    
    def test_intersection(self):
        pass
    
    def test_adjust_offsets(self):
        pass
    
    def test_build_AS_STRUCTURE_dict(self):
        pass
    
    def test_assign_to_regions(self):
        pass
    
    def test_build_assigned_from_existing(self):
        pass
    
    def test_eliminate_invalid_bed12(self):
        pass
    
    def test_get_offsets_bed12(self):
        pass
    
    def test_get_offsets(self):
        pass
    
    def plot_motif_dist(self):
        pass
    
    def test_RNA_position(self):
        pass
    
    def test_run_kmerdiff(self):
        pass
    
    def test_run_homer(self):
        pass
    
    def test_write_seqs(self):
        pass
    
    def motif_boxplots(self):
        pass
    
    def bedlengths(self):
        pass
    
    def chop(self):
        pass
    
    def test_fa_file(self):
        pass
    
    def make_dir(self):
        pass
    
    def test_main(self):
        pass
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
import unittest
from content_pipeline import validate
class PipelineTests(unittest.TestCase):
 def test_blocks_unknown_rights(self):
  self.assertIn('Not authorized for export',validate([{'license_status':'unknown'}])[0]['issues'])
 def test_duplicates(self):
  r={'id':'a','type':'question','source':'original','license_status':'original','review_status':'verified','content':{'answer':0,'options':['a','b'],'explanation':'a because...'}}
  out=validate([r,r]);self.assertEqual(out[0]['issues'],[]);self.assertIn('Duplicate content',out[1]['issues'])
if __name__=='__main__':unittest.main()

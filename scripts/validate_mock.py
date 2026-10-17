"""Validate original mock structure and every bundled MP3. This is not teacher review."""
import hashlib,json,subprocess,unittest,re
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
WRITTEN=json.loads((ROOT/'src/mock-written.json').read_text());LISTENING=json.loads((ROOT/'src/mock-listening.json').read_text());ALL=WRITTEN+LISTENING
class MockTests(unittest.TestCase):
 def test_blueprint(self):
  self.assertEqual(Counter(x['subject'] for x in ALL),{'Vocabulary':28,'Grammar':21,'Reading':8,'Listening':28})
  self.assertEqual(len({x['id'] for x in ALL}),85)
 def test_keys_and_provenance(self):
  for x in ALL:
   self.assertIn('original',x['provenance']);self.assertTrue(x['explanation'])
   self.assertIsInstance(x['answer'],int);self.assertTrue(0<=x['answer']<len(x['options']))
   self.assertEqual(len(x['options']),len(set(x['options'])))
 def test_every_audio_asset_matches_script(self):
  manifest=json.loads((ROOT/'public/audio/manifest.json').read_text());self.assertEqual(len(manifest),28)
  for q,m in zip(LISTENING,manifest):
   p=ROOT/'public/audio'/m['file'];self.assertEqual(q['id'],m['id']);self.assertGreater(p.stat().st_size,10000)
   self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),m['sha256'])
   self.assertEqual(hashlib.sha256(q['spokenText'].encode()).hexdigest(),m['sourceTextSha256'])
   self.assertGreater(m['durationSeconds'],5);self.assertTrue(q['kana']);self.assertTrue(q['translationNo']);self.assertTrue(q['translationEn'])
 def test_all_recordings_decode_and_contain_signal(self):
  import array
  for q in LISTENING:
   p=ROOT/'public'/q['audioSrc'].lstrip('/')
   pcm=subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-f','s16le','-ac','1','-ar','16000','-'])
   samples=array.array('h',pcm);self.assertGreater(max(abs(n) for n in samples),1000)
 def test_audio_is_excluded_from_spa_rewrite(self):
  config=json.loads((ROOT/'vercel.json').read_text());pattern=config['rewrites'][0]['source']
  self.assertIsNone(re.fullmatch(pattern,'/audio/fl1.mp3'))
  self.assertIsNone(re.fullmatch(pattern,'/audio/CREDITS.txt'))
  self.assertIsNotNone(re.fullmatch(pattern,'/exams'))
 def test_credits_present(self):
  self.assertIn('CC BY 3.0',(ROOT/'public/audio/CREDITS.txt').read_text());self.assertTrue((ROOT/'public/audio/VOICE-LICENSE.txt').exists())
if __name__=='__main__':unittest.main()

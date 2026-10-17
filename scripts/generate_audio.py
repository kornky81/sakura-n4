"""Generate static, redistributable synthetic Japanese speech; no cloud credentials.
Dependencies: pyopenjtalk==0.4.1, numpy, ffmpeg. Voice attribution: public/audio/CREDITS.txt.
Run after build_listening.py. Model/dictionary remain outside the git repository.
"""
import hashlib,json,subprocess,tempfile,wave
from pathlib import Path
import numpy as np
import pyopenjtalk
root=Path(__file__).resolve().parents[1]
items=json.loads((root/'src/mock-listening.json').read_text())
assets=root/'public/audio';assets.mkdir(parents=True,exist_ok=True)
voice_dir=Path(pyopenjtalk.__file__).parent/'htsvoice'
license_text=(voice_dir/'LICENSE_mei_normal.htsvoice').read_text()
(assets/'VOICE-LICENSE.txt').write_text(license_text)
(assets/'CREDITS.txt').write_text('''Sakura N4 original Japanese synthetic recordings
Engine: pyopenjtalk 0.4.1 / Open JTalk (MIT / BSD-family software licenses).
Voice: HTS Voice "Mei", MMDAgent Project Team, Nagoya Institute of Technology.
Voice source: https://github.com/r9y9/pyopenjtalk/tree/master/pyopenjtalk/htsvoice
Voice license: Creative Commons Attribution 3.0 Unported (CC BY 3.0).
https://creativecommons.org/licenses/by/3.0/
Full supplied voice notice is in VOICE-LICENSE.txt.

These files synthesize original Sakura N4 Japanese scripts using that voice.
Changes: newly synthesized speech, speed 0.88, pauses between sentences, encoded
as mono MP3. Attribution is retained here and linked in the application's player.
For caution the generated recordings are distributed under CC BY 3.0 too.
No textbook, YouTube or third-party human recording is included. One synthetic
narrator reads every speaker; this is disclosed and is not an official JLPT recording.
No ElevenLabs generation was charged or included. No paid service was enabled.
''')
manifest=[]
for row in items:
 text=row['spokenText']
 # The kana aid covers the source dialogue, not the options/answer explanation.
 assert row.get('kana'), 'Manually checked orthographic kana is required'
 with tempfile.TemporaryDirectory(dir=root.parent) as temp:
  chunks=[];sr=48000
  for part in text.split('。'):
   if not part.strip():continue
   speech,sr=pyopenjtalk.tts(part+'。',speed=.88)
   chunks.extend([speech,np.zeros(int(sr*.55))])
  data=np.clip(np.concatenate(chunks),-32768,32767).astype('<i2')
  wav=Path(temp)/'speech.wav'
  with wave.open(str(wav),'wb') as f:f.setnchannels(1);f.setsampwidth(2);f.setframerate(sr);f.writeframes(data.tobytes())
  dst=assets/(row['id']+'.mp3')
  subprocess.run(['ffmpeg','-v','error','-y','-i',str(wav),'-ac','1','-ar','24000','-codec:a','libmp3lame','-b:a','64k',str(dst)],check=True)
  duration=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(dst)],text=True))
  manifest.append({'id':row['id'],'file':dst.name,'durationSeconds':round(duration,3),'bytes':dst.stat().st_size,'sha256':hashlib.sha256(dst.read_bytes()).hexdigest(),'sourceTextSha256':hashlib.sha256(text.encode()).hexdigest(),'engine':'pyopenjtalk 0.4.1','voice':'Mei','license':'CC-BY-3.0','integrityChecked':True,'humanReview':'pending'})
  print(row['id'],round(duration,1),'seconds',flush=True)
(root/'src/mock-listening.json').write_text(json.dumps(items,ensure_ascii=False,indent=2))
(assets/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('Generated',len(manifest),'files;',round(sum(x['durationSeconds'] for x in manifest),1),'seconds of audio')

# Sakura N4 🌸
A Japanese study prototype for Oblig 3, built with React, TypeScript, Vite,
Tailwind CSS and React Router. Supabase is a future integration; the app works
without credentials and saves study progress locally in the browser.

Existing live demo: https://sakura-n4.vercel.app/
Repository: https://github.com/kornky81/sakura-n4
Feature branch: https://github.com/kornky81/sakura-n4/tree/feature/sakura-n4-mvp
PR: https://github.com/kornky81/sakura-n4/pull/1

**The existing demo has not been redeployed in this update.** New source features
below require an authorized deployment and browser verification before they are
claimed as live/complete.

## Features
- Dashboard: selected exam date/countdown, daily plan, streak and real activity.
- Eight kanji with 17 example-linked readings, status and simple review intervals.
- Six vocabulary entries, four bilingual grammar lessons, quizzes and reading.
- Listening studio: 28 original tasks with bundled static MP3 files and native audio
  controls. No Japanese system voice is needed for these files. Browser speech is
  optional and handles missing voices; it is not the primary audio source.
- Original transcripts, conventional kana readings and Norwegian/English summaries
  can be revealed in learning mode and final exam review.
- Existing ten-question Short Practice Exam (11:30), clearly separate from Full Mock
  Exam 01, an **85-question full-length validation draft** with 25/55/35-minute
  sections, 115 minutes total. It is not declared independently validated/complete.
- Confirmation before section locking; saved answers, recovery after refresh,
  automatic expiry/submission, results and separate short/full attempt histories.
  Time away counts against deadlines; refreshing does not grant extra section time.
- Progress export, responsive CSS, PWA manifest and basic runtime caching. Partial
  audio range responses are not cached as complete files.

## Run and test
Node 22.12 or supported Node 24; verified here with Node 24.19.
```sh
npm ci
npm run dev
```
Open the terminal's Vite URL, normally http://localhost:5173.
```sh
npm test
npm run build
python scripts/test_pipeline.py
python scripts/validate_mock.py
```
The audio validation command needs FFmpeg/ffprobe. Python/FFmpeg and the TTS engine
are not needed to run the app: MP3 files are already included.

Vitest 4.1.12 replaces the older runner that stalled after tests completed. Tests
cover countdown/scoring, data integrity, section deadlines/transitions, persistence,
refresh recovery, final submission, hidden exam aids and audio fallback behavior.
Actual final results are recorded in AI_DEVELOPMENT_LOG.md.

## Original full-exam content
| Section | Questions | Time |
| --- | --- | --- |
| Vocabulary | 28 | 25 minutes |
| Grammar and reading | 29 | 55 minutes |
| Listening | 28 | 35 minutes |
| Total | 85 | 115 minutes |

The approximate task-count blueprint comes from the official JLPT update:
https://www.jlpt.jp/sp/e/topics/202009091599642827.html
All questions, dialogues and passages here are original AI-assisted drafts, not
copied official questions. See CONTENT_REVIEW.md for the category breakdown,
internal checks, uncertain items and required manual review. Independent teacher
review, real-browser playback of the new files and mobile testing are pending.

The listening files contain about 11 minutes of synthetic speech, with remaining
section time for reading/responding/replay. Playback is manual; visual tasks use
text-only adaptations and all voices use one synthetic narrator. These differences
are disclosed. Scores are raw practice counts, never official scaled JLPT scores.
Learning hints, translations and transcripts stay hidden in exam mode until review.
Client-side answers remain inspectable; this is not high-stakes assessment software.

## Audio generation and licensing
All 28 files in `public/audio` were generated from our original scripts using
pyopenjtalk 0.4.1 / Open JTalk and HTS Voice **Mei** from the MMDAgent Project Team,
Nagoya Institute of Technology. Attribution and the full voice notice are bundled
in `public/audio/CREDITS.txt` and `VOICE-LICENSE.txt`. Generated recordings are
conservatively distributed under CC BY 3.0 with attribution. No YouTube recording,
textbook recording or cloned personal voice is included. No paid service was enabled
or charged. The voice is synthetic and may sound less natural than a human speaker.

To regenerate (optional developer workflow, use a virtual environment and a working
C/C++ compiler if a wheel is unavailable):
```sh
pip install pyopenjtalk==0.4.1 numpy
python scripts/build_mock_content.py
python scripts/build_listening.py
python scripts/generate_audio.py
python scripts/validate_mock.py
```
FFmpeg must be on PATH. Open JTalk downloads its licensed dictionary on first use.
The engine/model are not committed. `manifest.json` records source/audio hashes and
file durations. Actual audible playback and pronunciation are not certified by a
successful decode or unit test.

## Deployment policy and Vercel settings
`vercel.json` sets `git.deploymentEnabled["feature/sakura-n4-mvp"]` to `false` to
prevent a Git-triggered Vercel deployment when this feature branch is updated.
This branch-scoped source setting does not change deployment protection, the
production branch or paid services. Other branches' settings are unchanged.
Reference: https://vercel.com/docs/project-configuration/git-configuration

No deployment should be made without the owner's approval. After approval, deploy
this feature branch to an explicitly verified **Preview** target on the existing
Vercel project: Vite, repository root, install `npm ci`, build `npm run build`, output
`dist`, no Supabase variables. Do not import/deploy `main`, promote to Production,
merge, change protection or enable paid services. Initial project deployments can
be classified as Production, so do not use New Project's default Deploy blindly.
Manual CLI deployment to an existing linked project uses an explicit target:
```sh
npx vercel@latest deploy --target=preview
```
Verify the environment and URL afterward. The source's Git auto-deploy disablement
is not permission for a manual deployment. Offline caching is basic, not guaranteed
full audio/offline synchronization; PWA installation is unverified.

## Database and content expansion (future work)
`supabase/migrations/001_initial.sql` prepares relational content/progress tables,
Auth-linked users and default-deny RLS. It has not been applied to a live database.
Cloud authentication/sync and secure server grading are not implemented. Setting
`.env.local` alone does not enable cloud mode. Only public URL/anon placeholders
belong in frontend configuration; privileged keys must stay server-side.

`scripts/content_pipeline.py` validates authorized intake, detects exact duplicates
and separates reviewed original/licensed records from the review queue. Optional
PDF inventory needs pypdf and does not export textbook text. This is a review
scaffold, not a license verifier or comprehensive PDF extraction system.
The supplied textbook, official chart and proprietary question banks are excluded.
Resource pages link to Jisho, NHK, JapaneseTest4You and official JLPT; supplied
YouTube playlist contents remain labeled unverified.

## Limitations and verification boundary
The old deployed version passed real desktop smoke tests for settings, grammar,
kanji review, reading, short-exam submission and persistence on 17 October 2026.
The new player/full-exam UI has automated component/logic tests but no new real
browser/mobile session yet. Local media access is blocked by the cloud browser.
Static audio decoding and non-silence checks do not substitute for listening.
See CONTENT_REVIEW.md before calling Full Mock Exam 01 complete. No comprehensive
N4 curriculum, account system, advanced adaptive learning, licensed audio library
or official exam equivalence is claimed. Browser storage is device/profile-local;
clearing site storage loses progress. JSON import is not implemented.

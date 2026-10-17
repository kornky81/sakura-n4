# AI development log
## Student direction and AI tools
The student supplied the Sakura N4 requirements, repository, references, deadlines
and priorities. The latest focus was static Japanese audio and one full-length
original mock, preserving the working MVP. ChatGPT/Codex wrote and revised code,
original content, tests and documentation. GitHub tools prepared source commits/PR
updates. Python and Open JTalk generated licensed static speech. FFmpeg encoded and
validated it. No student review or test execution is invented.

## Existing prototype and previous verification
The original local commits were uploaded through GitHub as one identical-tree
snapshot fe79cbc9c470287ed3ec98cda08cee4d8fb0d60c because terminal Git lacked
credentials and the integration could not preserve local commit metadata. PR #1
is open and unmerged; the original history is preserved in the earlier Git bundle.
The user supplied https://sakura-n4.vercel.app/.

On 17 October 2026, the old deployed app opened in Chrome without personal/Vercel
login. Desktop smoke tests passed for settings and correct 51-day countdown,
grammar feedback and persisted activity, kanji reveal/review recording, reading
feedback, short-exam answer recovery and a correct 4/10 result/history. The viewport
was 1363 × 936 CSS pixels. No horizontal document overflow was detected on the
inspected reading screen. The inspected console showed extension metadata errors,
not application-origin errors. Japanese system voices were unavailable and the
old TTS-only UI correctly reported that limitation.

## Vitest fix
Vitest 3.2.7 reported assertions passing but stalled after completion, including a
one-line Node test with no app imports. Instrumented jsdom teardown completed, so
application exam timers were not a necessary cause. Different pool/worker settings
did not fix it. Compatible Vitest 4.1.12 resolved the reproducer and full suite with
normal exit 0. The precise older upstream/runtime shutdown mechanism is unknown.
The prepared dependency fix is included in the current source, without forced
process exit or disabled tests.

## Audio implementation
Used free offline pyopenjtalk 0.4.1 / Open JTalk and the CC BY 3.0 Mei voice. The
first build lacked clang; a workspace-local installation with GCC/G++ succeeded.
An ElevenLabs estimate was inspected but no generation was charged. No paid service
was enabled. Twenty-eight original tasks were synthesized to mono 24 kHz, 64 kbps
MP3, with approximately 663.8 seconds of speech. Full attribution and source/audio
hash manifests are committed; model/dictionary/runtime are not.

The native HTML audio player is primary. Missing/failed media has a retry message;
optional system speech handles missing voices and has its own stop control. It is
not the sole audio source. Service-worker code avoids caching partial range
responses as complete assets. All speaker roles use one synthetic narrator.

Content review rejected phonetic G2P for displayed kana, replacing it with manually
written conventional orthography. Ambiguous fictional station names were simplified.
The ten-minute phrase was changed to 10分 to reduce a TTS 十分 ambiguity. Independent
accent/intelligibility review remains pending.

## Full Mock Exam 01 implementation
Original 85-question blueprint: 28 vocabulary, 29 grammar/reading, 28 listening;
25/55/35-minute sections, 115 total minutes. Counts and task types were checked
against the official approximate N4 chart, not copied questions. The existing
10-question sample remains a separate Short Practice Exam. Histories retain exam
identifiers. The new UI is labeled full-length validation draft, not independently
validated/complete; CONTENT_REVIEW.md names remaining content/audio checks.

Deadline recovery now advances through elapsed sections from their original time
boundaries instead of granting extra time after refresh. An added UI test found a
25:01 initial display caused by mismatched timestamps; shared start/deadline times
and a display cap fixed it. Section submission requires explicit confirmation.
Translations, transcript aids and spoken response text are absent during exam mode.

## QA results
Final results for this source version are recorded after the final commands below.
Commands: npm test; npm run build; python scripts/test_pipeline.py;
python scripts/validate_mock.py. Audio checks verify every file hash, script hash,
decode and non-silent signal; they do not establish actual listening quality.

The cloud browser rejected local-file media URLs by protocol policy. No attempt
was made to bypass that policy. Therefore new recording playback, changed-player
browser behavior and full-exam browser behavior are NOT claimed as verified.
Mobile emulation is not exposed by the supported controls; phone checks remain
pending. Earlier desktop results describe the old deployed version only.

## Publication boundary
Vercel is not connected to this session and GitHub has no Vercel status checks on
the old branch head. Existing account settings could not be inspected. To prevent
Git-triggered deployment during source publication, the feature branch now has an
explicit false git.deploymentEnabled rule in vercel.json, following Vercel's
branch-scoped configuration documentation. This does not change protection or
production settings. Any manual deployment, merge or release needs owner approval.
No deployment, protection change, merge or paid service was performed in this work.

## Student's next steps
Review the original Japanese/answer keys and listen to every recording; approve a
Preview deployment for new-code desktop/phone checks; then update the final demo
link in the submission if it changes. Student involvement and actual checks must
be represented truthfully. Supabase integration and a larger kanji database were
intentionally left out of this urgent scope.

Final commands completed normally: Vitest **5 files, 35 tests passed**, final summary,
3.61 seconds, exit 0. TypeScript/Vite production build passed with exit 0. Two
content-pipeline tests passed. The expanded mock/audio validator also checks that
/audio paths are excluded from the SPA HTML rewrite: the new static MP3s must not
be rewritten to index.html. All 28 uploaded Git blob hashes match the local files.

The final expanded Python validator completed **6/6 tests**, exit 0; together with
the pipeline tests this is **8 Python tests passed**. All 35 JavaScript tests and
the production build had already passed after the final application-code changes.

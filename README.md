# Sakura N4 🌸
A mobile-first Japanese study prototype for Oblig 3. Learn with short bilingual lessons, listen to an original dialogue, and complete a timed practice exam. All bundled educational text is original AI-assisted starter material, not copied textbook content.

## Working features
- Dashboard: configurable target date, calendar-day countdown, daily plan, real activity, streak and weak-subject recommendation.
- Eight kanji, 17 example-linked readings, optional romaji, self-assessed status and fixed-interval review scheduling (10 minutes / 1 day / 4 days).
- Six vocabulary entries, four grammar lessons, multiple-choice feedback, original message comprehension and Japanese browser TTS listening.
- Ten-question **shortened practice** exam, three separately locked timed sections, navigation, refresh recovery, automatic checking, review and attempt history.
- Local browser persistence, JSON progress export, responsive navigation, PWA manifest and basic runtime offline cache.

## Stack and architecture
React 19, TypeScript, Vite 6, Tailwind 4, React Router 7, Lucide, Vitest and React Testing Library. `src/data.ts` contains the reference starter set and original question provenance; `src/core.ts` isolates scoring/date/storage functions from UI. The browser is the working persistence layer, avoiding a cloud setup dependency. `supabase/migrations/001_initial.sql` models the future relational backend with RLS and non-public answer keys. Supabase client dependency is included but cloud authentication/sync is **not integrated**.

## Run
Node 22.12+ recommended (verified here with Node 24.19).
```sh
npm ci
npm run dev
```
Open the Vite URL shown in the terminal (normally http://localhost:5173).
```sh
npm test
python scripts/test_pipeline.py
npm run build
npm run preview
```

## Deployment to Vercel
No deployment has been created. After reviewing and authorizing public hosting:
1. Import existing `kornky81/sakura-n4`, selecting `feature/sakura-n4-mvp` or a reviewed merged branch.
2. Choose Vite, build command `npm run build`, output `dist`, install command `npm ci`.
3. No environment variables are required for demo mode. `vercel.json` supports React Router refreshes.
4. Deploy, test a deep link, mobile layout, audio voice availability and exam refresh recovery. Add the actual URL to SUBMISSION.md.
HTTPS enables service workers. Offline assets are cached as visited, not a guaranteed full offline library. Japanese TTS may require an OS-installed voice and may not work offline. SVG-only icons and installation have not been device-tested; production mobile icons remain a follow-up.

## Database setup (future integration)
Create a free Supabase project and run the migration in its SQL editor on a fresh database. Enable your chosen Auth provider. Copy only the project URL and public anon key to `.env.local` using `.env.example`; never put service-role keys in frontend variables. The migration has not been executed against a real database. Build and test server endpoints for starting/advancing/submitting exams before cloud exam writes: verify auth, server deadlines, option-question membership and immutable submission. RLS intentionally denies client writes to exam records/results and denies all client access to answer keys. Browser demo answers are visible in JS and are unsuitable for high-stakes assessment. Merely setting env variables does not activate cloud mode.

## Curriculum and sources
The explicit starter reference is the eight characters in `src/data.ts`: 食 飲 駅 旅 働 貸 借 親. Level tags are approximate study labels, not official JLPT lists. Every included reading has one example, kana and romaji; this does not assert exhaustive reading coverage. Counts and script/relationship consistency are tested; independent dictionary/teacher verification, stroke-count verification and full N4 coverage are pending. Kanji self-ratings are distinguished from quiz accuracy. No rare-reading inventory or exceptional-reading lesson is yet included.

Official timing reference: https://www.jlpt.jp/e/guideline/testsections.html (N4 25/55/35 minutes). This app uses 2:30/5:30/3:30 for a 10-question sample, not a complete exam. Raw results are not scaled JLPT scores or pass predictions.
Resources link to Jisho, JapaneseTest4You, NHK and official JLPT. The two supplied YouTube playlist contents remain unverified and are labeled accordingly. No recordings are downloaded. The supplied Langendoen PDF is excluded from source and has not been imported; no textbook explanations or exercises are reproduced.

## Authorized content workflow
`python scripts/content_pipeline.py intake.json reviewed.json` validates draft records, detects exact duplicate content, and exports only original/licensed records marked verified. Required fields: id, type, source, license_status, review_status, content. Question content needs options, answer index and explanation. Optional `--pdf /private/file.pdf` requires `pip install pypdf` and only reports a page inventory. This is a review/validation scaffold, not automatic Japanese extraction or a license verifier. Human review is required before marking records verified.

## Verification and limitations
See AI_DEVELOPMENT_LOG.md for actual results. No real browser/device QA or database integration test has been performed in this environment. Real-browser desktop/mobile review, Japanese voice playback and PWA installation are manual release checks. Content is small and requires qualified language review. No full mock exam, comprehensive syllabus, accounts, cloud sync, matching/sentence-order exercises, advanced adaptive scheduling, licensed PDF extraction or authorized audio library is claimed. Browser data belongs to this device/profile and is lost if site storage is cleared. Export progress for a backup; import is not implemented.

Basic security: no secrets or PDF files are tracked; React escapes content; external links use noreferrer; runtime cache is same-origin GET only; no server/cloud integration is falsely exposed. Dependency and migration testing should be repeated before public release.

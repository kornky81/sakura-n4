# AI development log
## Tools and prompt
ChatGPT/Codex generated and iterated actual source code in response to the student's “MASTER PROMPT — BUILD SAKURA N4”. Git/GitHub inspected the existing repository. npm installed dependencies; TypeScript/Vite built the app; Vitest/React Testing Library tested logic and interactions; Python validated the content pipeline. Official JLPT, Vite and Supabase documentation were consulted for timing, runtime compatibility and RLS.

## Decisions
Prioritized a functional local demo over incomplete cloud configuration. Used original, small educational content and explicit coverage disclosures. Implemented deadline timestamps rather than decrement-only timers to survive refresh/background delays. Kept raw practice scores separate from official scaled scoring. Added a relational migration with default-deny RLS and protected answer keys, without claiming a deployed backend.

## Bugs and improvements
An interaction test initially failed because audio cleanup referenced a missing global speechSynthesis in an unsupported environment. Changed cleanup to guarded window.speechSynthesis. Added unavailable-voice feedback, a fallback for corrupt browser storage, a warning on progress-save failure, explicit empty states, and idempotent exam result insertion by attempt ID.

## Verification
- Initial production build passed (TypeScript and Vite).
- Initial 14 core/data/UI control tests passed.
- Added actual quiz/exam interaction tests; one initially failed due to the audio issue above, then fixed and rerun. Final result recorded below.
- Two Python pipeline tests passed: unauthorized-license rejection and duplicate review queue.
- npm audit --omit=dev: zero vulnerabilities at check time.
- No browser viewport/device QA was performed: the required supported browser-control skill was unavailable in the managed environment. Layout responsiveness is implemented in CSS, not claimed as visually verified.
- Supabase SQL has not been applied or tested against a live PostgreSQL instance. No cloud auth, synchronization or deployment is claimed.
- Japanese content received internal structural checks, not independent teacher verification. The supplied textbook and YouTube contents were not copied or validated.

## Student involvement
Student supplied requirements, priorities, repository and reference links. Before submission the student should review the code and Japanese, run the app, verify desktop/mobile flows, record the demo and supply its actual link. No review, testing or authorship by the student is invented here.

Final verification: all 17 Vitest assertions passed across two files (14 core/data tests and 3 quiz/exam flow tests). Test runner process completion is being checked separately. Production build passed after the audio fix. Two Python tests passed. GitHub feature-branch push was blocked by automatic approval review because the repository is public and public publishing requires student confirmation; local commits and source package are available.

Runner limitation: the environment reported passing test files but did not return a final Vitest exit/summary. Attempts with single workers, threads and forks did not resolve clean termination. Therefore automated assertions passed, but a clean test-command exit is **not verified**. Re-run `npm test` locally before submission. Production build exits successfully.

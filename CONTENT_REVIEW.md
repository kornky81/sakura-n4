# Full Mock Exam 01 — content and audio review

Status: **full-length validation draft, not declared complete**. Original AI-assisted
content received an internal answer/distractor review and structural tests. It has
not received independent Japanese-teacher or perceptual audio review. Static MP3s
are present and decode correctly, but the new assets have not been played in a real
browser: the cloud browser blocks local files and no new deployment was authorized.

## Blueprint
Based on the official approximate item-count update:
https://www.jlpt.jp/sp/e/topics/202009091599642827.html
and its N4 chart: https://www.jlpt.jp/userdata/image/N4eng.jpg
The chart itself is not distributed. Actual official counts can vary by session.

| Section | Original tasks | Minutes |
| --- | --- | --- |
| Vocabulary | 7 reading, 5 spelling, 8 context, 4 paraphrase, 4 usage = 28 | 25 |
| Grammar/reading | 13 selection, 4 ordering, 4 text grammar, 3 short reading, 3 medium reading, 2 information retrieval = 29 | 55 |
| Listening | 8 task comprehension, 7 point comprehension, 5 utterance expression, 8 quick response = 28 | 35 |
| Total | 85 | 115 |

Three short passages, two medium passages (three questions between them), an
informational notice (two questions), and a coherent four-gap grammar text are
original. No official or proprietary questions/audio are copied. The full draft
is separate from the existing ten-question Short Practice Exam.

## Checks completed
- Unique IDs, section membership, answer-index bounds, distinct alternatives,
  explanations and original-content provenance checked automatically.
- Answer logic checked internally against each original prompt and passage.
- All 28 audio files match their source-text hashes and decode to non-silent PCM.
- Numbered responses for utterance/quick-response tasks are recorded; their text is
  hidden during the exam. Transcripts/translations appear only in final review.
- Phonetic G2P output was rejected for display: manually written orthographic kana
  preserves は/へ and normal long-vowel spelling. No unverified romaji is invented.
- Ambiguous station names were replaced with fictional さくら駅 / みどり駅.
  The ten-minute lateness script uses 10分 to reduce a 十分 reading ambiguity.

## Required manual review before calling this complete
| Items | Review needed |
| --- | --- |
| fg14–fg17 | Confirm that alternative natural phrase orders cannot change the starred answer; check N4 ordering-task fidelity. |
| fg18–fg21 | Confirm discourse coherence and distractor exclusivity in the four-gap text. |
| fr1–fr6, fr8–fr9 | Confirm reading load, N4 difficulty and answer uniqueness against each passage/notice. |
| fl1–fl28 | Listen to every recording and verify intelligibility, accent, turn boundaries, question wording and absence of truncation. One synthetic narrator reads all speaker labels. |
| fl9, fl11, fl14, fl19 | Pay particular attention to negative response prosody and number/time pronunciation. |
| fl16–fl28 | Confirm all three spoken alternatives and their order match the UI answer key. |
| Full listening section | The 28 files contain about 11 minutes of speech; the 35-minute timer leaves reading/response/replay time. Playback is manual, not an official continuously paced listening track. |
| Desktop and phones | Check the newly changed exam/player UI in a permitted Preview deployment. Previous desktop checks cover the old deployed app only. |

Text-only adaptations replace visual-choice tasks. Replay is available. These are
explicit differences from the official exam, not a claim of official equivalence.
Raw correct counts/percentages are not official JLPT scaled scores or a pass guarantee.

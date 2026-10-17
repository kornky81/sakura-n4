-- Future cloud integration. Run in a fresh Supabase SQL editor. Not applied by the demo.
begin;
create table public.content_sources(id uuid primary key default gen_random_uuid(), title text not null, url text, license_status text not null check(license_status in ('original','licensed','reference_only','unknown')), review_status text not null default 'pending' check(review_status in ('pending','verified','rejected')));
create table public.profiles(id uuid primary key references auth.users(id) on delete cascade, display_name text);
create table public.study_settings(user_id uuid primary key references auth.users(id) on delete cascade, exam_date date, minutes integer not null default 20 check(minutes between 5 and 120), show_romaji boolean not null default true);
create table public.kanji(id uuid primary key default gen_random_uuid(), character text unique not null, study_level text check(study_level in ('N5','N4')), meaning_no text not null, meaning_en text not null, strokes integer check(strokes>0), source_id uuid references public.content_sources(id), verified boolean not null default false);
create table public.kanji_readings(id uuid primary key default gen_random_uuid(), kanji_id uuid not null references public.kanji(id), reading_type text not null check(reading_type in ('on','kun','exceptional')), kana text not null, romaji text not null, common boolean not null default true, review_status text not null default 'pending');
create table public.kanji_reading_examples(id uuid primary key default gen_random_uuid(), reading_id uuid not null references public.kanji_readings(id), spelling text not null, kana text not null, romaji text not null, meaning_no text not null, meaning_en text not null);
create table public.vocabulary(id uuid primary key default gen_random_uuid(), spelling text not null, kana text not null, romaji text not null, meaning_no text not null, meaning_en text not null, part_of_speech text not null, theme text, study_level text, example jsonb not null, source_id uuid references public.content_sources(id));
create table public.vocabulary_kanji(vocabulary_id uuid references public.vocabulary(id),kanji_id uuid references public.kanji(id),primary key(vocabulary_id,kanji_id));
create table public.grammar_lessons(id uuid primary key default gen_random_uuid(), pattern text not null, study_level text, structure text not null, explanation_no text not null, explanation_en text not null, examples jsonb not null, usage_notes text, common_mistakes text, source_id uuid references public.content_sources(id));
create table public.reading_passages(id uuid primary key default gen_random_uuid(), title text not null, japanese text not null, aids jsonb, source_id uuid references public.content_sources(id));
create table public.listening_exercises(id uuid primary key default gen_random_uuid(), title text not null, japanese text not null, aids jsonb, audio_url text, youtube_id text, source_id uuid references public.content_sources(id));
create table public.questions(id uuid primary key default gen_random_uuid(), subject text not null, prompt text not null, grammar_id uuid references public.grammar_lessons(id), passage_id uuid references public.reading_passages(id), listening_id uuid references public.listening_exercises(id), source_id uuid not null references public.content_sources(id));
create table public.question_options(id uuid primary key default gen_random_uuid(),question_id uuid not null references public.questions(id),position integer not null check(position between 0 and 3),text text not null,unique(question_id,position));
-- Keys must only be read by a privileged grading function/server, never the browser.
create table public.answer_keys(question_id uuid primary key references public.questions(id), correct_option_id uuid not null references public.question_options(id), explanation text not null);
create table public.mock_exams(id uuid primary key default gen_random_uuid(), code text unique not null, title text not null, is_sample boolean not null default true);
create table public.exam_sections(id uuid primary key default gen_random_uuid(),exam_id uuid not null references public.mock_exams(id),title text not null,position integer not null,duration_seconds integer not null check(duration_seconds>0),unique(exam_id,position));
create table public.exam_questions(section_id uuid references public.exam_sections(id),question_id uuid references public.questions(id),position integer not null,primary key(section_id,question_id),unique(section_id,position));
create table public.exam_attempts(id uuid primary key default gen_random_uuid(),user_id uuid not null references auth.users(id) on delete cascade,exam_id uuid not null references public.mock_exams(id),started_at timestamptz not null default now(),submitted_at timestamptz);
create table public.student_answers(attempt_id uuid references public.exam_attempts(id),question_id uuid references public.questions(id),option_id uuid references public.question_options(id),primary key(attempt_id,question_id));
create table public.exam_results(attempt_id uuid primary key references public.exam_attempts(id), raw_correct integer not null check(raw_correct>=0),total integer not null check(total>0),check(raw_correct<=total));
create table public.study_progress(user_id uuid references auth.users(id) on delete cascade,item_type text not null,item_id text not null,status text not null check(status in ('new','learning','reviewing','mastered')),due_at timestamptz,correct integer not null default 0 check(correct>=0),attempts integer not null default 0 check(attempts>=correct),primary key(user_id,item_type,item_id));
create table public.learning_resources(id uuid primary key default gen_random_uuid(),title text not null,url text not null,description text,source_id uuid references public.content_sources(id));
create index readings_kanji on public.kanji_readings(kanji_id);
create index examples_reading on public.kanji_reading_examples(reading_id);
create index attempts_user on public.exam_attempts(user_id);
create index progress_due on public.study_progress(user_id,due_at);
-- Default deny on ALL tables. Only reference tables get anonymous read access.
do $$ declare t text; begin
foreach t in array array['content_sources','profiles','study_settings','kanji','kanji_readings','kanji_reading_examples','vocabulary','vocabulary_kanji','grammar_lessons','reading_passages','listening_exercises','questions','question_options','answer_keys','mock_exams','exam_sections','exam_questions','exam_attempts','student_answers','exam_results','study_progress','learning_resources'] loop
execute format('alter table public.%I enable row level security',t);
end loop;
foreach t in array array['content_sources','kanji','kanji_readings','kanji_reading_examples','vocabulary','vocabulary_kanji','grammar_lessons','reading_passages','listening_exercises','questions','question_options','mock_exams','exam_sections','exam_questions','learning_resources'] loop
execute format('create policy reference_read on public.%I for select using (true)',t);
execute format('grant select on public.%I to anon, authenticated',t);
end loop;
foreach t in array array['profiles','study_settings','study_progress'] loop
execute format('create policy own_data on public.%I for all to authenticated using (auth.uid() = %I) with check (auth.uid() = %I)',t,case when t='profiles' then 'id' else 'user_id' end,case when t='profiles' then 'id' else 'user_id' end);
execute format('grant select,insert,update,delete on public.%I to authenticated',t);
end loop;
end $$;
create policy own_attempts on public.exam_attempts for select to authenticated using(user_id=auth.uid());
create policy own_answers on public.student_answers for select to authenticated using(exists(select 1 from public.exam_attempts a where a.id=attempt_id and a.user_id=auth.uid()));
create policy own_results on public.exam_results for select to authenticated using(exists(select 1 from public.exam_attempts a where a.id=attempt_id and a.user_id=auth.uid()));
grant select on public.exam_attempts,public.student_answers,public.exam_results to authenticated;
revoke all on public.answer_keys from anon,authenticated;
-- Exam writes intentionally require a future server endpoint: enforce deadlines, option/question
-- relationships, submission immutability, and scoring there with a server-only service role.
commit;

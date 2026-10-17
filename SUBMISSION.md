# Oblig 3 — Sakura N4

Sakura N4 er en nettbasert prototype for å øve til japanskprøven JLPT N4.
Applikasjonen er utviklet med React, TypeScript og Vite og inneholder kanjikort,
grammatikkoppgaver, leseforståelse, japanske lydøvelser og tidsbegrensede
øvingsprøver. Full Mock Exam 01 har 85 originale spørsmål fordelt på tre deler
med en samlet tidsramme på 115 minutter. Svar, resultater og fremgang lagres
lokalt i nettleseren, uten krav om konto eller Supabase-oppsett.

Generativ KI (ChatGPT/Codex) har støttet planlegging, programmering, originale
øvingsoppgaver, automatiserte tester, feilretting og dokumentasjon. Jeg har
styrt krav og prioriteringer og manuelt testet lydavspilling, prøvedeler,
tidtaking, navigasjon, innlevering og resultater i Chrome på datamaskin.
35 JavaScript-tester og 8 Python-tester bestod, og produksjonsbygget lyktes.
Mobiltesting pågår. Prototypen har et begrenset pensum; prøven er et originalt
fullengde-utkast, ikke en offisiell JLPT-eksamen eller faglig sertifisert prøve.

Demo (Vercel Preview): https://sakura-n4-n22chwc2z-kornky.vercel.app/
GitHub: https://github.com/kornky81/sakura-n4
Kildekode: https://github.com/kornky81/sakura-n4/tree/feature/sakura-n4-mvp
PR: https://github.com/kornky81/sakura-n4/pull/1

## Verifikasjon og begrensninger
- Studenten bekreftet 17. oktober 2026 at demoen åpnes i inkognito uten
  Vercel-innlogging. Dette er en offentlig tilgjengelig Preview, ikke Production.
- Desktop Chrome: studenten bekreftet japansk MP3-avspilling, alle tre
  prøvedeler, tidtaking, navigasjon, innlevering og delresultater.
- Mobiltesting pågår; fullført mobiltest er ikke bekreftet.
- Uavhengig kontroll av japansk innhold/uttale og PWA-installasjon gjenstår.
- Supabase, større pensum og offisiell JLPT-poengskalering inngår ikke i MVP-en.
- PR #1 forblir åpen. Ingen sammenslåing eller ny deploy kreves for å bruke
  den eksisterende offentlige Preview-lenken i Canvas.

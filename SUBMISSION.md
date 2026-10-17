# Oblig 3 — Sakura N4
## Kort beskrivelse til innleveringen
Sakura N4 er en nettbasert prototype for japanskøving, utviklet med React og
TypeScript. Den tilbyr kanjikort, grammatikkoppgaver, leseforståelse og en kort,
tidsbegrenset øvingsprøve. Fremgang lagres lokalt i nettleseren. Generativ KI har
bidratt til planlegging, kode, originale øvingsoppgaver, testing og feilretting.
Prototypen har et begrenset startpensum og er ikke en offisiell JLPT-eksamen.

GitHub: https://github.com/kornky81/sakura-n4
Kildekode: https://github.com/kornky81/sakura-n4/tree/feature/sakura-n4-mvp
Eksisterende demo: https://sakura-n4.vercel.app/
PR: https://github.com/kornky81/sakura-n4/pull/1

## Ny kildeversjon — må kvalitetssikres før den beskrives som ferdig
Kildekoden inneholder nå 28 originale, syntetiske japanske lydfiler og et større
prøveutkast med 85 spørsmål og 115 minutters samlet tidsramme (25/55/35 minutter).
Dette er merket som et fullengde-utkast under validering. Lydavspilling i nettleser,
uttale og uavhengig faglig kontroll gjenstår; vellykket dekoding er ikke det samme
som bekreftet avspilling. Den gamle korte prøven er beholdt separat.

Den eksisterende demoen er ikke deployet på nytt i denne oppdateringen. Ikke påstå
at den nye lyden og fullengde-utkastet er testet eller tilgjengelig på den gamle
lenken før en godkjent deploy og faktiske kontroller er gjennomført. Git-utløst
Vercel-deploy er deaktivert for funksjonsgrenen i kildekonfigurasjonen. Manuell
Preview-deploy, sammenslåing og eventuell release krever eierens godkjenning.

Supabase-kontoer og skysynkronisering er fremtidig arbeid. Oppgi det faktiske
resultatet fra AI_DEVELOPMENT_LOG.md og mobiltesten; ikke finn på studenttesting.

# Arbeitsamt Jobsuche API 
Die Bundesagentur für Arbeit verfügt über die größte Datenbank für offene Stellen in Deutschland. Obwohl sie vollständig staatlich ist und es sich dabei um einen sehr spannenden Basisdatensatz handelt, mit dem viele Analysen möglich wären, bietet die Bundesagentur für Arbeit dafür bis heute keine offizielle API an.


## Authentifizierung
Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs.
Die Client Credentials sind z.B. in der App hinterlegt:

**ClientID:** c003a37f-024f-462a-b36d-b001be4cd24a

**ClientSecret:** 32a39620-32b3-4307-9aa1-511e3d7f48a8

```bash
curl -H 'Host: api-con.arbeitsagentur.de' -H 'Accept: */*' -H 'Content-Type: application/x-www-form-urlencoded; charset=utf-8' -H 'Cookie: JSESSIONID=DF392405E8F00714FBFE17EDAB5DDD98' -H 'Accept-Language: en-us' -H 'User-Agent: Jobsuche/1070 CFNetwork/1220.1 Darwin/20.3.0' --data-binary "client_id=c003a37f-024f-462a-b36d-b001be4cd24a&client_secret=32a39620-32b3-4307-9aa1-511e3d7f48a8&grant_type=client_credentials" --compressed 'https://api-con.arbeitsagentur.de/oauth/gettoken_cc'
```

## Jobsuche

**URL:** https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service/pc/v2/app/jobs?FCT.AKTUALITAET=100&FCT.ANGEBOTSART=ARBEIT


Die Jobsuche ermöglicht verfügbare Jobangebote mit verschiedenen get Parametern zu filtern:



**Parameter:** *was* (Optional)
Freitext suche Jobtitel


**Parameter:** *wo*  (Optional)
Freitext suche Jobtitel


**Parameter:** *page* (Optional)
Seite…



**Parameter:** *ARBEITGEBER* (Optional)
ID des Arbeitgebers. z.B. "Deutsche%20Bahn%20AG_W4qFQypjw_IWOJAkn2NMSE-Yf-mRbt_6_PvZr0FLdX4%3D" (*arbeitgeberHashId*)



**Parameter:** *size* (Optional)
Anzahl der Ergebnisse

### Filter

**Parameter:** *FCT.AKTUALITAET* (Optional)

Anzahl der Tage, seit der Job veröffentlicht wurde. Kann zwischen 0 und 100 Tagen liegen.



**Parameter:** *FCT.ARBEITSVERMITTLUNG* (Optional)
- MIT_AV

Gibt an, ob Jobs von externen Arbeitsvermittlungen in die Suchergebnisse einbezogen werden sollen.



**Parameter:** *FCT.ANGEBOTSART*  (Optional)
- ARBEIT
- SELBSTAENDIGKEIT
- AUSBILDUNG
- PRAKTIKUM_TRAINEE



**Parameter:** *FCT.BEFRISTUNG*  (Optional)
- UNBEFRISTET
- KEINE_ANGABE
- BEFRISTET

Kann mehrere Werte haben z.B. FCT.BEFRISTUNG=UNBEFRISTET&FCT.BEFRISTUNG=KEINE_ANGABE.



**Parameter:** *FCT.BEHINDERUNG*  (Optional)
- AUS
- AN



**Parameter:** *FCT.AKTION*  (Optional)
- AN

Wenn AN, werden nur Jobs die im Kontext von Corona angeboten werden angezeigt.



**Parameter:** *FCT.UMKREIS* (Optional)

Umkreis in Kilometern von Wo-Parameter. (z.B. 25 oder 200)



**Parameter:** *FCT.ARBEITSZEITMODELL*  (Optional)
- VOLLZEIT
- TEILZEIT
- SCHICHT_NACHTARBEIT_WOCHENENDE
- HEIM_TELEARBEIT
- MINIJOB

Kann mehrere Werte haben z.B. FCT.ARBEITSZEITMODELL=HEIM_TELEARBEIT&FCT.ARBEITSZEITMODELL=MINIJOB



Beispiel:
```bash
curl -H 'Host: api-con.arbeitsagentur.de' -H 'Accept: application/json' -H 'OAuthAccessToken: Bearer [JWT]'  -H 'User-Agent: Jobsuche/1070 CFNetwork/1220.1 Darwin/20.3.0' -H 'Accept-Language: en-us' --compressed 'https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service/pc/v2/app/jobs?FCT.AKTUALITAET=100&FCT.ANGEBOTSART=ARBEIT&FCT.BEHINDERUNG=AUS&FCT.UMKREIS=200&page=0&size=100&wo=Berlin'
```

## Jobdetails

### Detailseite
Abrufen von Details zu einem Job.

**URL** https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service/pc/v1/jobdetails/[hashId]

### Bewerbung
Kontaktdaten für eine Bewerbung. (Ansprechpartner, Telefonnummer, …)

**URL** https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service/pc/v1/app/jobs/[hashId]/bewerbung

### Arbeitgeberlogo zu einem Job
Logo des Unternehmens

**URL** https://api-con.arbeitsagentur.de/prod/jobboerse/jobsuche-service/ed/v1/arbeitgeberlogo/[hashId]

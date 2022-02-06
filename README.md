# Arbeitsamt Jobsuche API 
Die Bundesagentur für Arbeit verfügt über die größte Datenbank für offene Stellen in Deutschland. Obwohl sie vollständig staatlich ist und es sich dabei um einen sehr spannenden Basisdatensatz handelt, mit dem viele Analysen möglich wären, bietet die Bundesagentur für Arbeit dafür bis heute keine offizielle API an.


## Authentifizierung
Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs.
Die Client Credentials sind z.B. in der App hinterlegt:

**ClientID:** c003a37f-024f-462a-b36d-b001be4cd24a

**ClientSecret:** 32a39620-32b3-4307-9aa1-511e3d7f48a8

```bash
curl \
-H 'Host: rest.arbeitsagentur.de' \
-H 'Accept: */*' \
-H 'Content-Type: application/x-www-form-urlencoded; charset=utf-8' \
-H 'Accept-Language: en-us' \
-H 'User-Agent: Jobsuche/1070 CFNetwork/1220.1 Darwin/20.3.0' \
--data-binary "client_id=c003a37f-024f-462a-b36d-b001be4cd24a&client_secret=32a39620-32b3-4307-9aa1-511e3d7f48a8&grant_type=client_credentials" \
--compressed 'https://rest.arbeitsagentur.de/oauth/gettoken_cc'
```

Der generierte Token muss bei folgenden GET-requests im header als 'OAuthAccessToken' inkludiert werden.

## Jobbörse

**URL:** https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs?angebotsart=1
	

Die Jobsuche ermöglicht verfügbare Jobangebote mit verschiedenen get Parametern zu filtern:



**Parameter:** *was* (Optional)

Freitext suche Jobtitel


**Parameter:** *wo*  (Optional)

Freitext suche Jobtitel


**Parameter:** *page* (Optional)

Seite…


**Parameter:** *arbeitgeber* (Optional)

ID des Arbeitgebers. z.B. "Deutsche%20Bahn%20AG"


**Parameter:** *zeitarbeit* (Optional)

Gibt an, ob Jobs von Zeitarbeitsfirmen in die Suchergebnisse einbezogen werden sollen (default true).


**Parameter:** *size* (Optional)

Anzahl der Ergebnisse

### Filter

**Parameter:** *veröffentlichtseit* (Optional)

Anzahl der Tage, seit der Job veröffentlicht wurde. Kann zwischen 0 und 100 Tagen liegen.



**Parameter:** *pav* (Optional)
- false 
- true

Gibt an, ob Jobs von privaten Arbeitsvermittlungen in die Suchergebnisse einbezogen werden sollen.



**Parameter:** *angebotsart*  (Optional)
- 1 
- 2 
- 3 
- 34

1=ARBEIT; 2=SELBSTAENDIGKEIT, 4=AUSBILDUNG/Duales Studium, 34=Praktikum/Trainee

**Parameter:** *befristung*  (Optional)
- 1
- 2

Semikolon-separierte mehrere Werte möglich (z.B. befristung=1;2) 1 = befristet; 2 = unbefristet


Parameter: behinderung (Optional)
- false 
- true


Parameter: corona (Optional)
- false 
- true

Wenn AN, werden nur Jobs die im Kontext von Corona angeboten werden angezeigt.

**Parameter:** *umreis* (Optional)

Umkreis in Kilometern von Wo-Parameter. (z.B. 25 oder 200)



**Parameter:** *arbeitszeit*  (Optional)
- vz 
- tz 
- snw
- ho 
- mj 

Semikolon-separierte mehrere Werte möglich (z.B. arbeitszeit=vz;tz) vz=VOLLZEIT, tz=TEILZEIT, snw=SCHICHT_NACHTARBEIT_WOCHENENDE, ho=HEIM_TELEARBEIT, mj=MINIJOB



### Beispiel:
```bash
jobs=$(curl -m 60 -H "Host: rest.arbeitsagentur.de" \
-H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0" \
-H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" \
-H "Accept-Language: de,en-US;q=0.7,en;q=0.3" \
-H "Accept-Encoding: gzip, deflate, br" \
-H "Origin: https://web.arbeitsagentur.de" \
-H "DNT: 1" \
-H "Connection: keep-alive" \
-H "Pragma: no-cache" \
-H "Referer: https://jobboerse.arbeitsagentur.de/vamJB/stellenangeboteFinden.html?execution=e1s4&" \
-H "Cache-Control: no-cache" \
-H "OAuthAccessToken: $token" \
'https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs?angebotsart=1&wo=Berlin&umkreis=200&arbeitszeit=ho;mj&page=1&size=25&pav=false')
```

## Jobdetails

### Detailseite
Abrufen von Details zu einem Job.

**URL** https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobdetails/[hashId]

### Bewerbung
Kontaktdaten für eine Bewerbung. (Ansprechpartner, Telefonnummer, …)

**URL** https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs/[hashId]/bewerbung

### Arbeitgeberlogo zu einem Job
Logo des Unternehmens

**URL** https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/arbeitgeberlogo/[hashId]


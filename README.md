# Arbeitsagentur Jobsuche API 
Die Bundesagentur für Arbeit verfügt über die größte Datenbank für offene Stellen in Deutschland. Obwohl sie vollständig staatlich ist und es sich dabei um einen sehr spannenden Basisdatensatz handelt, mit dem viele Analysen möglich wären, bietet die Bundesagentur für Arbeit dafür bis heute keine offizielle API an.


## Authentifizierung
Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs.
Die Client Credentials sind z.B. in der App hinterlegt:

**client_id:** c003a37f-024f-462a-b36d-b001be4cd24a

**client_secret:** 32a39620-32b3-4307-9aa1-511e3d7f48a8

**grant_type:** client_credentials

Die Credentials sind im body POST-request an https://rest.arbeitsagentur.de/oauth/gettoken_cc zu senden.

```bash
token=$(curl \
-d "client_id=c003a37f-024f-462a-b36d-b001be4cd24a&client_secret=32a39620-32b3-4307-9aa1-511e3d7f48a8&grant_type=client_credentials" \
-X POST 'https://rest.arbeitsagentur.de/oauth/gettoken_cc' |grep -Eo '[^"]{500,}'|head -n 1)
```

Der generierte Token muss bei folgenden GET-requests an https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs o.ä. im header als 'OAuthAccessToken' inkludiert werden.

## Jobbörse

**URL:** https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs?angebotsart=1
	

Die Jobsuche ermöglicht verfügbare Jobangebote mit verschiedenen get Parametern zu filtern:


### Filter


**Parameter:** *was* (Optional)

Freitextsuche Jobtitel (z.B. Referatsleiter).


**Parameter:** *wo*  (Optional)

Freitextsuche Beschäftigungsort (z.B. Berlin).


**Parameter:** *berufsfeld*  (Optional)

Freitextsuche Berufssfeld (z.B. Informatik).


**Parameter:** *page* (Optional)

Seite (beginnend mit 1).


**Parameter:** *arbeitgeber* (Optional)

ID des Arbeitgebers. z.B. "Deutsche%20Bahn%20AG"


**Parameter:** *zeitarbeit* (Optional)

Gibt an, ob Jobs von Zeitarbeitsfirmen in die Suchergebnisse einbezogen werden sollen (default true).


**Parameter:** *size* (Optional)

Anzahl der Ergebnisse


**Parameter:** *veroeffentlichtseit* (Optional)

Anzahl der Tage, seit der Job veröffentlicht wurde. Kann zwischen 0 und 100 Tagen liegen.


**Parameter:** *pav* (Optional)
- false 
- true

Private Arbeitsvermittlung: Gibt an, ob Jobs von privaten Arbeitsvermittlungen in die Suchergebnisse einbezogen werden sollen.


**Parameter:** *angebotsart*  (Optional)
- 1 
- 2 
- 4 
- 34

Angebotsart: 1=ARBEIT; 2=SELBSTAENDIGKEIT; 4=AUSBILDUNG/Duales Studium; 34=Praktikum/Trainee.


**Parameter:** *befristung*  (Optional)
- 1
- 2

Befristung: 1 = befristet; 2 = unbefristet. Mehrere Semikolon-separierte Werte möglich (z.B. befristung=1;2).


Parameter: behinderung (Optional)
- false 
- true


Parameter: corona (Optional)
- false 
- true

Corona: Es werden nur Jobs die im Kontext von Corona angeboten werden angezeigt wenn *true*.


**Parameter:** *umkreis* (Optional)

Umkreis: in Kilometern von *Wo*-Parameter (z.B. 25 oder 200).


**Parameter:** *arbeitszeit*  (Optional)
- vz 
- tz 
- snw
- ho 
- mj 

Arbeitszeit: vz=VOLLZEIT, tz=TEILZEIT, snw=SCHICHT_NACHTARBEIT_WOCHENENDE, ho=HEIM_TELEARBEIT, mj=MINIJOB. 
Mehrere Semikolon-separierte Werte möglich (z.B. arbeitszeit=vz;tz).


### Beispiel:
```bash
jobs=$(curl -m 60 \
-H "OAuthAccessToken: $token" \
'https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs?angebotsart=1&wo=Berlin&umkreis=200&arbeitszeit=ho;mj&page=1&size=25&pav=false')
```

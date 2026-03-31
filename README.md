# Arbeitsagentur Jobsuche API 
Die Bundesagentur für Arbeit verfügt über die größte Datenbank für offene Stellen in Deutschland. Obwohl sie vollständig staatlich ist und es sich dabei um einen sehr spannenden Basisdatensatz handelt, mit dem viele Analysen möglich wären, bietet die Bundesagentur für Arbeit dafür bis heute keine offizielle API an.


## Authentifizierung
ie Authentifizierung funktioniert über die clientId:

**clientId:** jobboerse-jobsuche

Bei folgenden GET-requests ist die clientId als Header-Parameter 'X-API-Key' zu übergeben.

**Update:** Falls client_id nicht funktioniert kann man stattdessen "X-API-KEY: jobboerse-jobsuche" verwenden


## Ablauf

Der typische Ablauf ist:

1. **Stellen suchen** via `/pc/v4/jobs` oder `/pc/v4/app/jobs` → `refnr` aus der Antwort merken.
2. **Details abrufen** via `/pc/v4/jobdetails/{base64(refnr)}` (empfohlen) oder `/pc/v3/jobdetails/{base64(refnr)}`.
3. **Arbeitgeberlogo abrufen** via `/ct/v1/arbeitgeberlogo/{arbeitgeberKundennummerHash}` (sofern im Detail-Response vorhanden).

## Jobbörse

**URL:** https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs
	

Die Jobsuche ermöglicht verfügbare Jobangebote mit verschiedenen get Parametern zu filtern:

**Hinweis:** Die Details der Jobangebote können in einem weiteren Schritt mittels der gefundenen Referenznummern abgerufen werden (siehe Beispielskripte)

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
-H "X-API-Key: jobboerse-jobsuche" \
'https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs?angebotsart=1&wo=Berlin&umkreis=200&arbeitszeit=ho;mj&page=1&size=25&pav=false')
```


## Jobdetails

**URL (empfohlen):** https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobdetails/{encryptedJobCode}

**URL (alternativ):** https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v3/jobdetails/{encryptedJobCode}

Der `encryptedJobCode` ist der Base64-kodierte Wert der `refnr` aus der Jobsuche-Antwort.

**Beispiel:** `refnr = 10001-1002716922-S` → `base64(refnr) = MTAwMDEtMTAwMjcxNjkyMi1T`

Die Detail-Antwort enthält u.a.:
- `stellenangebotsTitel` – Titel der Stelle
- `stellenangebotsBeschreibung` – Beschreibung der Stelle
- `referenznummer` – Referenznummer der Stelle
- `arbeitgeberKundennummerHash` – Hash für den Logo-Abruf (kann `null` sein)

### Hinweise zu Sonderfällen

- Manche Stellenanzeigen haben kein `kundennummerHash` in der Suchantwort und kein `arbeitgeberKundennummerHash` in der Detail-Antwort – in diesem Fall steht kein Logo zur Verfügung.
- Externe Stellenanzeigen können ein `externeUrl`-Feld in der Suchantwort enthalten.

### Beispiel:
```bash
refnr="10001-1002716922-S"
encoded=$(python3 -c "import base64; print(base64.b64encode('$refnr'.encode()).decode())")
curl -m 60 \
  -H "X-API-Key: jobboerse-jobsuche" \
  "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobdetails/$encoded"
```


## Arbeitgeberlogo

**URL:** https://rest.arbeitsagentur.de/vermittlung/ag-darstellung-service/ct/v1/arbeitgeberlogo/{kundennummerHash}

Der `kundennummerHash` entspricht dem Feld `arbeitgeberKundennummerHash` aus der Jobdetail-Antwort (URL-kodiert falls nötig, da der Wert `=`-Zeichen enthalten kann).

Gibt `200 image/webp` oder `200 image/png` zurück, wenn ein Logo vorhanden ist.  
Gibt `404` zurück, wenn kein Logo für diesen Arbeitgeber hinterlegt ist – dies ist ein normaler Fall, kein Fehler.

### Beispiel:
```bash
curl -m 60 \
  -H "X-API-Key: jobboerse-jobsuche" \
  "https://rest.arbeitsagentur.de/vermittlung/ag-darstellung-service/ct/v1/arbeitgeberlogo/Z-HzVkUCLGQiQFxQSAICs302sSdB9Sp7XtgOiO4GGCA%3D"
```

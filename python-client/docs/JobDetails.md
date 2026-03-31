# JobDetails

Detaillierte Informationen zu einem Stellenangebot. Hinweis: Die Feldnamen entsprechen der tatsächlichen API-Antwort (Stand 2024/2025), nicht den ursprünglich dokumentierten camelCase-Namen.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**referenznummer** | **str** | Referenznummer des Stellenangebots (API-Feldname: referenznummer, nicht refnr) | [optional] 
**stellenangebots_titel** | **str** | Titel des Stellenangebots (API-Feldname: stellenangebotsTitel, nicht titel) | [optional] 
**stellenangebotsart** | **str** | Art des Stellenangebots | [optional] 
**firma** | **str** | Name des Arbeitgebers (API-Feldname: firma, nicht arbeitgeber) | [optional] 
**arbeitgeber_kundennummer_hash** | **str** | Hash der Arbeitgeber-Kundennummer | [optional] 
**hauptberuf** | **str** | Hauptberuf für das Stellenangebot | [optional] 
**stellenangebots_beschreibung** | **str** | Beschreibung des Stellenangebots (API-Feldname: stellenangebotsBeschreibung, nicht stellenbeschreibung) | [optional] 
**stellenlokationen** | [**[JobDetailsStellenlokationenInner]**](JobDetailsStellenlokationenInner.md) | Arbeitsorte (API-Feldname: stellenlokationen, nicht arbeitsorte) | [optional] 
**arbeitszeit_vollzeit** | **bool** | Gibt an, ob es sich um Vollzeit handelt (API-Feldname: arbeitszeitVollzeit, nicht arbeitszeitmodelle) | [optional] 
**verguetungsangabe** | **str** | Vergütungsangabe (API-Feldname: verguetungsangabe, nicht verguetung) | [optional] 
**vertragsdauer** | **str** | Dauer des Vertrags | [optional] 
**eintrittszeitraum** | [**JobDetailsEintrittszeitraum**](JobDetailsEintrittszeitraum.md) |  | [optional] 
**veroeffentlichungszeitraum** | [**JobDetailsVeroeffentlichungszeitraum**](JobDetailsVeroeffentlichungszeitraum.md) |  | [optional] 
**datum_erste_veroeffentlichung** | **date** | Datum der ersten Veröffentlichung | [optional] 
**aenderungsdatum** | **datetime** | Datum der letzten Änderung | [optional] 
**ist_betreut** | **bool** | Gibt an, ob das Angebot betreut wird | [optional] 
**ist_behinderung_gefordert** | **bool** | Nur für Schwerbehinderte (API-Feldname: istBehinderungGefordert, nicht nurFuerSchwerbehinderte) | [optional] 
**ist_geringfuegige_beschaeftigung** | **bool** | Gibt an, ob es sich um eine geringfügige Beschäftigung handelt | [optional] 
**ist_arbeitnehmer_ueberlassung** | **bool** | Gibt an, ob es sich um Arbeitnehmerüberlassung handelt | [optional] 
**ist_private_arbeitsvermittlung** | **bool** | Gibt an, ob es sich um private Arbeitsvermittlung handelt | [optional] 
**quereinstieg_geeignet** | **bool** | Gibt an, ob das Angebot für Quereinsteiger geeignet ist | [optional] 
**allianzpartner_name** | **str** | Name des Allianzpartners (API-Feldname: allianzpartnerName, nicht allianzpartner) | [optional] 
**allianzpartner_url** | **str** | URL des Allianzpartners | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



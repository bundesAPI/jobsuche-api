# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.jobsuche.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.jobsuche.model.job_application_details import JobApplicationDetails
from deutschland.jobsuche.model.job_application_details_angebotskontakt import (
    JobApplicationDetailsAngebotskontakt,
)
from deutschland.jobsuche.model.job_application_details_angebotskontakt_festnetznummer import (
    JobApplicationDetailsAngebotskontaktFestnetznummer,
)
from deutschland.jobsuche.model.job_application_details_angebotskontakt_mobilnummer import (
    JobApplicationDetailsAngebotskontaktMobilnummer,
)
from deutschland.jobsuche.model.job_details import JobDetails
from deutschland.jobsuche.model.job_details_arbeitgeber_adresse import (
    JobDetailsArbeitgeberAdresse,
)
from deutschland.jobsuche.model.job_details_arbeitsorte_inner import (
    JobDetailsArbeitsorteInner,
)
from deutschland.jobsuche.model.job_details_arbeitsorte_items_koordinaten import (
    JobDetailsArbeitsorteItemsKoordinaten,
)
from deutschland.jobsuche.model.job_details_ausbildungen_inner import (
    JobDetailsAusbildungenInner,
)
from deutschland.jobsuche.model.job_details_fertigkeiten_inner import (
    JobDetailsFertigkeitenInner,
)
from deutschland.jobsuche.model.job_details_fuehrungskompetenzen import (
    JobDetailsFuehrungskompetenzen,
)
from deutschland.jobsuche.model.job_details_links import JobDetailsLinks
from deutschland.jobsuche.model.job_details_links_arbeitgeberlogo import (
    JobDetailsLinksArbeitgeberlogo,
)
from deutschland.jobsuche.model.job_details_links_bewerbung import (
    JobDetailsLinksBewerbung,
)
from deutschland.jobsuche.model.job_details_links_details import JobDetailsLinksDetails
from deutschland.jobsuche.model.job_details_links_self import JobDetailsLinksSelf
from deutschland.jobsuche.model.job_details_mobilitaet import JobDetailsMobilitaet
from deutschland.jobsuche.model.job_details_sprachkenntnisse_inner import (
    JobDetailsSprachkenntnisseInner,
)
from deutschland.jobsuche.model.job_search_response import JobSearchResponse
from deutschland.jobsuche.model.job_search_response_aggregierungen import (
    JobSearchResponseAggregierungen,
)
from deutschland.jobsuche.model.job_search_response_aggregierungen_bundesland import (
    JobSearchResponseAggregierungenBundesland,
)
from deutschland.jobsuche.model.job_search_response_aggregierungen_plzebene2 import (
    JobSearchResponseAggregierungenPlzebene2,
)
from deutschland.jobsuche.model.job_search_response_embedded import (
    JobSearchResponseEmbedded,
)
from deutschland.jobsuche.model.job_search_response_embedded_jobs_inner import (
    JobSearchResponseEmbeddedJobsInner,
)
from deutschland.jobsuche.model.job_search_response_embedded_jobs_items_arbeitsort import (
    JobSearchResponseEmbeddedJobsItemsArbeitsort,
)
from deutschland.jobsuche.model.job_search_response_embedded_jobs_items_arbeitsort_koordinaten import (
    JobSearchResponseEmbeddedJobsItemsArbeitsortKoordinaten,
)
from deutschland.jobsuche.model.job_search_response_embedded_jobs_items_links import (
    JobSearchResponseEmbeddedJobsItemsLinks,
)
from deutschland.jobsuche.model.job_search_response_embedded_jobs_items_links_arbeitgeberlogo import (
    JobSearchResponseEmbeddedJobsItemsLinksArbeitgeberlogo,
)
from deutschland.jobsuche.model.job_search_response_embedded_jobs_items_links_details import (
    JobSearchResponseEmbeddedJobsItemsLinksDetails,
)
from deutschland.jobsuche.model.job_search_response_embedded_jobs_items_links_jobdetails import (
    JobSearchResponseEmbeddedJobsItemsLinksJobdetails,
)
from deutschland.jobsuche.model.job_search_response_facetten_inner import (
    JobSearchResponseFacettenInner,
)
from deutschland.jobsuche.model.job_search_response_facetten_items_auswahl_inner import (
    JobSearchResponseFacettenItemsAuswahlInner,
)
from deutschland.jobsuche.model.job_search_response_links import JobSearchResponseLinks
from deutschland.jobsuche.model.job_search_response_links_first import (
    JobSearchResponseLinksFirst,
)
from deutschland.jobsuche.model.job_search_response_links_last import (
    JobSearchResponseLinksLast,
)
from deutschland.jobsuche.model.job_search_response_links_next import (
    JobSearchResponseLinksNext,
)
from deutschland.jobsuche.model.job_search_response_links_self import (
    JobSearchResponseLinksSelf,
)
from deutschland.jobsuche.model.job_search_response_page import JobSearchResponsePage
from deutschland.jobsuche.model.job_search_response_parser_result import (
    JobSearchResponseParserResult,
)
from deutschland.jobsuche.model.job_search_response_parser_result_koordinaten_inner import (
    JobSearchResponseParserResultKoordinatenInner,
)

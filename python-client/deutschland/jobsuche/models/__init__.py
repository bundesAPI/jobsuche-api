# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.jobsuche.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.jobsuche.model.job_details import JobDetails
from deutschland.jobsuche.model.job_details_arbeitgeber_adresse import (
    JobDetailsArbeitgeberAdresse,
)
from deutschland.jobsuche.model.job_details_arbeitsorte_inner import (
    JobDetailsArbeitsorteInner,
)
from deutschland.jobsuche.model.job_details_arbeitsorte_inner_koordinaten import (
    JobDetailsArbeitsorteInnerKoordinaten,
)
from deutschland.jobsuche.model.job_details_fertigkeiten_inner import (
    JobDetailsFertigkeitenInner,
)
from deutschland.jobsuche.model.job_details_fuehrungskompetenzen import (
    JobDetailsFuehrungskompetenzen,
)
from deutschland.jobsuche.model.job_details_mobilitaet import JobDetailsMobilitaet
from deutschland.jobsuche.model.job_search_response import JobSearchResponse
from deutschland.jobsuche.model.job_search_response_facetten_inner import (
    JobSearchResponseFacettenInner,
)
from deutschland.jobsuche.model.job_search_response_facetten_inner_befristung import (
    JobSearchResponseFacettenInnerBefristung,
)
from deutschland.jobsuche.model.job_search_response_stellenangebote_inner import (
    JobSearchResponseStellenangeboteInner,
)
from deutschland.jobsuche.model.job_search_response_stellenangebote_inner_arbeitsort import (
    JobSearchResponseStellenangeboteInnerArbeitsort,
)
from deutschland.jobsuche.model.job_search_response_stellenangebote_inner_arbeitsort_koordinaten import (
    JobSearchResponseStellenangeboteInnerArbeitsortKoordinaten,
)

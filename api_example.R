#----------------
# Simple Example
#----------------
install.packages(c("devtools","jsonlite","httr","png"))
devtools::install_github("AndreasFischer1985/qqBaseX")
clientId="jobboerse-jobsuche"
url="https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/app/jobs?angebotsart=1"
url="https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs?angebotsart=1"

data_request=httr::GET(url=url, httr::add_headers(.headers=c("X-API-Key"=clientId)),
        config=httr::config(connecttimeout=60))
data_request
data=httr::content(data_request)

writeLines(jsonlite::toJSON(data$facetten,pretty=TRUE,auto_unbox=TRUE),paste0(Sys.Date(),"_jobsuche_facetten.json"))

urlLogo="https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/ed/v1/arbeitgeberlogo/arJ0dxbYlPFXeMuZtdZzooRdCOnK2TjUXjLQlkBr-Ew="
dataLogo=httr::content(httr::GET(url=urlLogo, httr::add_headers(.headers=c("X-API-Key"=clientId)), config=httr::config(connecttimeout=60)))



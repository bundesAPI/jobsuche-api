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

# Jobdetails abrufen: base64(refnr) als Pfadparameter
refnr <- data$stellenangebote[[1]]$refnr
encryptedJobCode <- base64enc::base64encode(charToRaw(refnr))
urlDetails <- paste0("https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobdetails/", encryptedJobCode)
details_request <- httr::GET(url=urlDetails, httr::add_headers(.headers=c("X-API-Key"=clientId)),
        config=httr::config(connecttimeout=60))
details <- httr::content(details_request)

# Arbeitgeberlogo abrufen (sofern arbeitgeberKundennummerHash vorhanden)
# Endpoint: GET /vermittlung/ag-darstellung-service/ct/v1/arbeitgeberlogo/{kundennummerHash}
# 404 bedeutet: kein Logo vorhanden (kein Fehler)
urlLogo="https://rest.arbeitsagentur.de/vermittlung/ag-darstellung-service/ct/v1/arbeitgeberlogo/Z-HzVkUCLGQiQFxQSAICs302sSdB9Sp7XtgOiO4GGCA%3D"
dataLogo=httr::content(httr::GET(url=urlLogo, httr::add_headers(.headers=c("X-API-Key"=clientId)), config=httr::config(connecttimeout=60)))


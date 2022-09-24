#----------------
# Simple Example
#----------------
install.packages(c("devtools","jsonlite","httr","png"))
devtools::install_github("AndreasFischer1985/qqBaseX")
clientId="c003a37f-024f-462a-b36d-b001be4cd24a"
clientSecret="32a39620-32b3-4307-9aa1-511e3d7f48a8"
postData=list( "grant_type"="client_credentials","client_id"=clientId,"client_secret"=clientSecret) 
token_request=httr::POST(
        url="https://rest.arbeitsagentur.de/oauth/gettoken_cc",
        body=postData,encode="form",
        config=httr::config(connecttimeout=60))
token=(httr::content(token_request, as='parsed')$access_token)
url="https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/app/jobs?angebotsart=1"
url="https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs?angebotsart=1"
data_request=httr::GET(url=url, httr::add_headers(.headers=c("OAuthAccessToken"=token)),
        config=httr::config(connecttimeout=60))
data_request
data=httr::content(data_request)

writeLines(jsonlite::toJSON(data$facetten,pretty=TRUE,auto_unbox=TRUE),paste0(Sys.Date(),"_jobsuche_facetten.json"))

urlLogo="https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/ed/v1/arbeitgeberlogo/arJ0dxbYlPFXeMuZtdZzooRdCOnK2TjUXjLQlkBr-Ew="
dataLogo=httr::content(httr::GET(url=urlLogo, httr::add_headers(.headers=c("OAuthAccessToken"=token)), config=httr::config(connecttimeout=60)))

hashID1=data$stellenangebote[[1]]$hashId 
urlDetails=paste0("https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v2/jobdetails/",jsonlite::base64_enc(hashID1))
dataDetails=httr::content(httr::GET(url=urlDetails, httr::add_headers(.headers=c("OAuthAccessToken"=token)), config=httr::config(connecttimeout=60)))





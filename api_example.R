#----------------
# Simple Example
#----------------
install.packages(c("devtools","rjson","httr"))
devtools::install_github("AndreasFischer1985/qqBaseX")
clientId="c003a37f-024f-462a-b36d-b001be4cd24a"
clientSecret="32a39620-32b3-4307-9aa1-511e3d7f48a8"
postData=list( "grant_type"="client_credentials","client_id"=clientId,"client_secret"=clientSecret) 
token_request=httr::POST(
        url="https://rest.arbeitsagentur.de/oauth/gettoken_cc",
        body=postData,encode="form",
        config=httr::config(connecttimeout=60))
token=(httr::content(token_request, as='parsed')$access_token)
url="https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/app/jobs?angebotsart=1&wo=Berlin&umkreis=200&arbeitszeit=ho;mj&page=1&size=25&pav=false"
url="https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs?angebotsart=1&wo=Berlin&umkreis=200&arbeitszeit=ho;mj&page=1&size=25&pav=false"
data_request=httr::GET(url=url, httr::add_headers(.headers=c("OAuthAccessToken"=token)),
        config=httr::config(connecttimeout=60))
data_request
data=httr::content(data_request)

hashID1=data$stellenangebote[[1]]$hashId 

urlLogo="https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/ed/v1/arbeitgeberlogo/arJ0dxbYlPFXeMuZtdZzooRdCOnK2TjUXjLQlkBr-Ew="
httr::GET(url=urlLogo, httr::add_headers(.headers=c("OAuthAccessToken"=token)), config=httr::config(connecttimeout=60))

urlDetails="https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v2/jobdetails/MTQ3NTEtNjExMzcwLVM"
httr::GET(url=urlDetails, httr::add_headers(.headers=c("OAuthAccessToken"=token)), config=httr::config(connecttimeout=60))



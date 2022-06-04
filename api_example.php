<?php

// POST-request:
//--------------
$url = 'https://rest.arbeitsagentur.de/oauth/gettoken_cc';
$data = array(
    'client_id' => 'c003a37f-024f-462a-b36d-b001be4cd24a', 
    'client_secret' => '32a39620-32b3-4307-9aa1-511e3d7f48a8', 
    'grant_type' => 'client_credentials');
$options = array(
    'http' => array(
        'method'  => 'POST',
        'content' => http_build_query($data)
    )
);
$context  = stream_context_create($options);
$tokendata = file_get_contents($url, false, $context);
header('Content-Type: application/json'); 
if(isset($_GET['token']) & $_GET['token']==='TRUE'){
	echo $tokendata;
} else {
    // GET-request:
    //-------------
    $url = 'https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs?'.$_SERVER['QUERY_STRING'];
    $options = array(
        'http' => array(
            'header'  => "OAuthAccessToken:".json_decode($tokendata, true)['access_token']." \r\n",
            'method'  => 'GET'    
        )
    );
    $context  = stream_context_create($options);
    $searchdata = file_get_contents($url, false, $context);
    echo $searchdata;
}
?>


*** Settings ***
Library       RequestsLibrary
Library       Collections

*** Test Cases ***
API Validation Test
    @{ls}      create list    user    pass
    ${auth}    evaluate    tuple(@{ls})
    ${response}  Get   https://httpbin.org/basic-auth/user/pass  auth=${auth}
    Log To Console  ${response.status_code}
    Log To Console  ${response.json()}
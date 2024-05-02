*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input Register Command
    Input Credentials  vili  vili1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Register Command
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Register Command
    Input Credentials  s  vili1234
    Output Should Contain  Username must contain atleast 3 characters

Register With Enough Long But Invalid Username And Valid Password
    Input Register Command
    Input Credentials  ääääää  vili1234
    Output Should Contain  Username must only contain characters a-z

Register With Valid Username And Too Short Password
    Input Register Command
    Input Credentials  valid_username  short
    Output Should Contain  Password must contain atleast 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Register Command
    Input Credentials  valid_username  long_password
    Output Should Contain  Password must contain characters and numbers

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123

Input Register Command
    Input  new

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application

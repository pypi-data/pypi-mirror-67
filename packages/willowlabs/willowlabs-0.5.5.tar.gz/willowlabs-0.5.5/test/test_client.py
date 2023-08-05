import pytest

from willowlabs.company_information.client import CompanyInformationClient

def test_get_basic_company_information():
    client = CompanyInformationClient("C:\\Users\\Sven\\projects\\client_config.yaml")
    organisation_number = 1
    company_basic_results = client.get_basic_company_information(organisation_number)

    assert company_basic_results.bad_request == True
    organisation_number = 923710809
    company_basic_results = client.get_basic_company_information(organisation_number)
    print(company_basic_results)
    assert company_basic_results.basic_company_information.company_name ==  "BEAUFORT SOLUTIONS AS"
    print(company_basic_results.basic_company_information.company_name)


def test_get_company_ownership():
    client = CompanyInformationClient("C:\\Users\\Sven\\projects\\client_config.yaml")
    organisation_number = 1
    record_year = 2018
    company_ownership_results = client.get_company_ownership(organisation_number, record_year)
    print(company_ownership_results)
    print(type(company_ownership_results))
    assert company_ownership_results.bad_request == True




test_get_basic_company_information()
# -*- coding: utf-8 -*-
"""
Includes the test scenarios to check the CIM compatibility of an Add-on.
"""
import logging
import pytest
from .field_test_helper import FieldTestHelper

INTERVAL = 3
RETRIES = 3


class CIMTestTemplates(object):
    """
    Test scenarios to check the CIM compatibility of an Add-on 
    Supported Test scenarios:
        - The eventtype should exctract all required fields of data model 
        - One eventtype should not be mapped with more than one data model 
        - Field Cluster should be verified (should be included with required field test)
        - Verify if CIM installed or not 
        - Not Allowed Fields should not be extracted 
    """

    logger = logging.getLogger("pytest-splunk-addon-cim-tests")

    def test_eventtype_mapped_datamodel(
        self, splunk_search_util, record_property, caplog
    ):
        """
        This test case check that event type is not be mapped with more than one data model 

        Args:
            splunk_search_util (SearchUtil): Object that helps to search on Splunk.
            record_property (fixture): Document facts of test cases.
            caplog (fixture): fixture to capture logs.
        """

        DATA_MODELS = [
            "Alerts",
            "Authentication",
            "Certificates",
            "Change",
            "Compute_Inventory",
            "DLP",
            "Databases",
            "Email",
            "Endpoint",
            "Event_Signatures",
            "Interprocess_Messaging",
            "Intrusion_Detection",
            "JVM",
            "Malware",
            "Network_Resolution",
            "Network_Sessions",
            "Network_Traffic",
            "Performance",
            "Splunk_Audit",
            "Ticket_Management",
            "Updates",
            "Vulnerabilities",
            "Web",
        ]

        test_helper = FieldTestHelper(
            splunk_search_util, [], interval=INTERVAL, retries=RETRIES
        )
        search = ""
        # Iterate data models list to create a search query
        for index, datamodel in enumerate(DATA_MODELS):
            if index == 0:
                search += f'| tstats count from datamodel={datamodel}  by eventtype | eval dm_type="{datamodel}"\n'
            else:
                search += f'| append [| tstats count from datamodel={datamodel}  by eventtype | eval dm_type="{datamodel}"]\n'

        search += """| stats delim=", " dc(dm_type) as datamodel_count, values(dm_type) as datamodels by eventtype | nomv datamodels
        | where datamodel_count > 1 and eventtype!="err0r"
        """
        record_property("search", search)

        results = list(splunk_search_util.getFieldValuesList(search, INTERVAL, RETRIES))
        if results:
            record_property("results", results)
            result_str = test_helper.get_table_output(
                headers=["Count", "Eventtype", "Datamodels"],
                value_list=[
                    [
                        each_result["datamodel_count"],
                        each_result["eventtype"],
                        each_result["datamodels"],
                    ]
                    for each_result in results
                ],
            )

        assert not results, (
            f"Query result greater than 0.\nsearch=\n{search} \n \n"
            f"Event type which associated with multiple data model \n{result_str}"
        )

    @pytest.mark.splunk_app_cim
    @pytest.mark.splunk_app_cim_fields
    def test_cim_required_fields(
        self, splunk_search_util, splunk_app_cim_fields, record_property
    ):
        """
        Test the the required fields in the data models are extracted with valid values. 
        Supports 3 scenarios. The test order is maintained for better test report.
        1. Check that there is at least 1 event mapped with the data model 
        2. Check that each required field is extracted in all of the events mapped with the data model.
        3. Check that if there are inter dependent fields, either all fields should be extracted or 
            none of them should be extracted.
        """

        # Search Query
        base_search = "search "
        for each_set in splunk_app_cim_fields["data_set"]:
            base_search += " ({})".format(each_set.search_constraints)

        base_search += " AND ({})".format(splunk_app_cim_fields["tag_stanza"])

        test_helper = FieldTestHelper(
            splunk_search_util,
            splunk_app_cim_fields["fields"],
            interval=INTERVAL,
            retries=RETRIES,
        )

        # Execute the query and get the results
        results = test_helper.test_field(base_search)
        record_property("search", test_helper.search)

        # All assertion are made in the same tests to make the test report with
        # very clear order of scenarios. with this approach, a user will be able to identify
        # what went wrong very quickly.
        assert all([each_result["event_count"] > 0 for each_result in results]), (
            "0 Events found in at least one sourcetype mapped with the dataset."
            f"\n{test_helper.format_exc_message()}"
        )
        if len(splunk_app_cim_fields["fields"]) == 1:
            test_field = splunk_app_cim_fields["fields"][0].name
            assert all([each_field["field_count"] > 0 for each_field in results]), (
                f"Field {test_field} not extracted in any events."
                f"\n{test_helper.format_exc_message()}"
            )
            assert all(
                [
                    each_field["field_count"] == each_field["valid_field_count"]
                    for each_field in results
                ]
            ), (
                f"Field {test_field} have invalid values."
                f"\n{test_helper.format_exc_message()}"
            )
        elif len(splunk_app_cim_fields["fields"]) > 1:
            # Check that count for all the fields in cluster is same.
            # If all the fields are not extracted in an event, that's a passing scenario
            # The count of the field may or may not be same with the count of event.
            sourcetype_fields = dict()
            for each_result in results:
                sourcetype_fields.setdefault(each_result["sourcetype"], list()).extend(
                    [each_result["field_count"], each_result["valid_field_count"]]
                )
            for sourcetype_fields in sourcetype_fields.values():
                assert len(set(sourcetype_fields)) == 1, (
                    "All fields from the field-cluster should be extracted with valid values if any one field is extracted."
                    f"\n{test_helper.format_exc_message()}"
                )

    @pytest.mark.parametrize(
        "app_name",
        [pytest.param("Splunk_SA_CIM", marks=[pytest.mark.splunk_searchtime_cim])],
    )
    def test_app_installed(self, splunk_search_util, app_name, record_property):
        """
        This test case checks that addon is installed/enabled in the Splunk instance.

        Args:
            splunk_search_util (SearchUtil): Object that helps to search on Splunk.
            app_name (string): Add-on name.
            record_property (fixture): Document facts of test cases.
        """

        record_property("app_name", app_name)
        # Search Query
        search = "| rest /servicesNS/nobody/{}/configs/conf-app/ui".format(app_name)
        self.logger.info(f"Executing the search query: {search}")
        record_property("search", search)

        result = splunk_search_util.checkQueryCountIsGreaterThanZero(
            search, interval=INTERVAL, retries=RETRIES
        )

        assert result, (
            f"\nMessage: App {app_name} is not installed/enabled in this Splunk instance."
            f"The plugin requires the {app_name} to be installed/enabled in the Splunk instance."
            f"Please install the app and execute the tests again."
        )

from unittest import TestCase

import main


class BranchValidatorTest(TestCase):
    def test_check_entered_param_with_develop(self):
        # Given
        test_object = "develop"
        expected_result = None

        # When
        result = main.check_entered_param(test_object)

        # Then
        self.assertEqual(expected_result, result)

    def test_check_entered_param_with_none(self):
        # Given
        test_object = None
        expected_msg = "mandatory param name was not given"

        # When
        with self.assertRaises(SystemExit) as custom_exception:
            main.check_entered_param(test_object)

        # Then
        self.assertEqual(custom_exception.exception.code, expected_msg)

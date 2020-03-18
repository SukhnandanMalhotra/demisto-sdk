from demisto_sdk.commands.common.tools import print_color, LOG_COLORS
from demisto_sdk.commands.format.update_generic_json import BaseUpdateJSON
from demisto_sdk.commands.common.hook_validations.reputation import ReputationValidator

ARGUMENTS_DEFAULT_VALUES = {
    'system': False
}


class IndicatorTypeJSONFormat(BaseUpdateJSON):
    """IndicatorTypeJSONFormat class is designed to update indicator type JSON file according to Demisto's convention.

       Attributes:
            input (str): the path to the file we are updating at the moment.
            output (str): the desired file name to save the updated version of the YML to.
    """

    def __init__(self, input='', output='', old_file='', path='', from_version=''):
        super().__init__(input, output, old_file, path, from_version)

    def format_file(self):
        """Manager function for the integration YML updater."""
        super().update_json()

        print_color(F'========Starting updates for incident field: {self.source_file}=======', LOG_COLORS.YELLOW)

        super().set_default_values_as_needed(ARGUMENTS_DEFAULT_VALUES)
        super().save_json_to_destination_file()

        print_color(F'========Finished updates for incident field: {self.output_file_name}=======',
                    LOG_COLORS.YELLOW)

        return self.initiate_file_validator(ReputationValidator)
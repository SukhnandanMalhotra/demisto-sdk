from typing import Tuple

from demisto_sdk.commands.format.format_constants import SKIP_RETURN_CODE
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

    def __init__(self, input: str = '', output: str = '', path: str = '', from_version: str = '', no_validate: bool = False):
        super().__init__(input, output, path, from_version, no_validate)

    def run_format(self) -> int:
        try:
            super().update_json()
            super().set_default_values_as_needed()
            super().save_json_to_destination_file()
            return 0
        except Exception:
            return 1

    def format_file(self) -> Tuple[int, int]:
        """Manager function for the integration YML updater."""
        format = self.run_format()
        if format:
            return format, SKIP_RETURN_CODE
        else:
            return format, self.initiate_file_validator(ReputationValidator)

import sys

class HousingException(Exception):
    def __init__(self, error_message: str, error_details: Exception):
        super().__init__(error_message)
        self.error_message = error_message
        self.error_details = error_details

    @staticmethod
    def get_detailed_error_message(error_message: str, error_details: Exception) -> str:
        _, _, exec_tb = sys.exc_info()
        line_number = exec_tb.tb_frame.f_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename

        detailed_error_message = (
            f"Error occurred in script: [{file_name}] at line number: [{line_number}] "
            f"error_message: [{error_message}]"
        )

        return detailed_error_message

    
# Exception handling purpose
# Whereever we use try catch - we raise CustomException to get the message
import sys
import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() # store error that we fetech from the method exc_info
    file_name=exc_tb.tb_frame.f_code.co_filename # Get file name of error
    error_message= "Error occured in python script/file name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))

    return error_message


# Create a custom exception class that inherits from exception
class CustomException(Exception):
    # Create an object of this class when we raise an error from a try and catch
    def __init__(self, error_message, error_detail:sys):
        # inherit from error_message
        super().__init__(error_message)
        # store error message from the function error message
        self.error_message = error_message_detail(error_message,error_detail=error_detail)


    def __str__(self):
        # Print error message
        return self.error_message
    

    
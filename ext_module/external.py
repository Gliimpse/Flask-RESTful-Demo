from datetime import datetime


def give_me_time():
    """Some arbitrary external function to be implemented into API"""
    return datetime.now().strftime("%m/%d/%Y %H:%M:%S")

# -*- coding: utf-8 -*-
import requests
from datetime import datetime, timedelta

#Method that returns the date of the given medium a range of dates
def get_medium_date(start_date, end_date):
    s_date = datetime.strptime(str(start_date), "%Y-%m-%d")
    e_date = datetime.strptime(str(end_date), "%Y-%m-%d")
    days = abs(e_date - s_date).days / 2
    return s_date.date() + timedelta(days=days)




def get_count_number_invoices(id, start_date, end_date, count_calls):
    count_calls += 1                                                    #Number of times the endpoint is called
    response = requests.get("http://34.209.24.195/facturas\?id=" + str(id) + "&start=" + str(start_date) + "&finish="+str(end_date))
    #response = requests.get("http://127.0.0.1:8000/api/test/?id=" + str(id)
    #                        + "&start_date=" + str(start_date) + "&end_date="+str(end_date))

    if response.text.encode('utf-8').isdigit():                         #We check if the answer is a numerical value
        return int(response.text.encode('utf-8')), count_calls
    elif "100" in response.text.encode('utf-8'):                        #We check if you returned the answer There are more than 100 results
        medium_date = get_medium_date(start_date, end_date)             #In medium_date we obtain the date in the middle of the range
        left_tree, count_calls = get_count_number_invoices(id, start_date,
                                                          medium_date,count_calls)  #From the tree that forms, we call the method from
                                                                                    # the start date to the middle date
        rigth_tree, count_calls = get_count_number_invoices(id, medium_date         #From the tree that forms, we call the method from
                                                                                    # the date of the medium plus one day until the end date
                                                           + timedelta(days=1), end_date, count_calls)
        return left_tree + rigth_tree, count_calls
    else:
        raise Exception('Left parameters! :(')

number_invoices,count_calls= get_count_number_invoices("4e25ce61-e6e2-457a-89f7-116404990967", "2017-01-01", "2017-12-31", 0)
print (" El numero de facturas que hay es  %s y el numero de llamadas es de  %s" % (number_invoices,count_calls))





[![Build Status](https://travis-ci.com/locustio/locust.svg?branch=master)](https://travis-ci.com/anuj-ssharma/PayeSummary)
![GitHub](https://img.shields.io/github/license/anuj-ssharma/payesummary)

# NZ PAYE Summary

Calculate the PAYE Summary based on hourly rate. 

>>> `python main.py --hourly-rate 100 --hours-worked 40`

Result is shown in the format:

        +--------------+--------------+---------------------------+----------+-----------------+----------------+----------------------+-------------------+
        | Hours Worked | Total Income | Less Witholding Tax (10%) | Plus GST | Paid to Account | Remaining PAYE | Remaining GST + PAYE | Disposable Income |
        +--------------+--------------+---------------------------+----------+-----------------+----------------+----------------------+-------------------+
        |     40.0     |   4000.00    |          400.00           |  600.00  |     4200.00     |     745.38     |       1345.38        |      2854.62      |
        +--------------+--------------+---------------------------+----------+-----------------+----------------+----------------------+-------------------+


By default a withholding tax of 10% is used. You can change this.

>>> `python main.py --hourly-rate 100 --hours-worked 40 --withholding-tax 20`

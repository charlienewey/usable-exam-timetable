#! /usr/bin/env python

import csv
import json
import sys

exams = {"data": []}

with open(sys.argv[1], "r") as csvin:
    rdr = csv.reader(csvin)
    for row in rdr:
        row = [val.replace("\r", "") for val in row]

        # Ignore header rows
        if row[3] == "Room Code":
            continue

        """
        exam = {
            "module_code": row[0],
            "module_name": row[1],
            "num_students": row[2],
            "room_code": row[3],
            "room_name": row[4],
            "when_day_of_week": row[5],
            "when_date": row[6],
            "when_start_time": row[7],
            "length": row[8]
        }
        """

        exam = row
        exams["data"].append(exam)

if len(exams) > 0:
    with open(sys.argv[2], "w") as jsonout:
        json.dump(exams, jsonout, indent=4, sort_keys=True)
    # for exam in exams:
    #     mc = exam["module"]["code"]
    #     if mc.startswith("CS3") or mc.startswith("SE3"):
    #         print(json.dumps(exam, indent=4, sort_keys=True))

#!/usr/bin/env python
import json
import os

import argparse

def create_record(model_name,keys,values):
    '''

    Arguments:

    model_name: name of the model
    keys: header names as a list
    values: values from a row as a list

    Returns
     A dict representing a record.
    '''
    pk = values[0]
    record = {"model":'travel_agency.'+model_name,"pk":pk}
    fields = {attribute:value.strip() for attribute,value in zip(keys[1:],values[1:])}
    record['fields'] = fields

    return record

def csv_to_json(file):
    '''
    file: csv file name

    Results:
     writes a json file from a csv file.

    '''
    #open csv
    csv_file = open(file)
    #create json file
    json_file = open(file.replace('.csv','.json'),'w')

    header = csv_file.readline().strip().split(',')
    model = file[:file.find('.')]

    #get records in json format
    records = []
    for row in csv_file:
        row = row.replace('\"',"")
        row = row.strip().split(',')
        record = create_record(model,header,row)
        records.append(record)

    csv_file.close()

    #write to json file
    json_file.write(json.dumps(records))
    json_file.close()

def get_args():
    help_text = '''CSV files to be converted to json.
                   If no files are provided the current working
                   directory will be searched for any csv files to
                   covert to json.'''


    parser = argparse.ArgumentParser(description="Convert CSV to json for Django dumpdata.")
    parser.add_argument('infiles',
                        nargs="*",
                        help=help_text,
                        metavar="CSV file.",
                        default=None)

    args = parser.parse_args()
    return args

if __name__ == "__main__":

    args = get_args()
    if args.infiles:
        for file in args.infiles:
            csv_to_json(file)
    else:
        for file in os.listdir():
            if file.endswith(".csv"):
                csv_to_json(file)


from reports.simple_report import SimpleReport
from reports.complete_report import CompleteReport
import os.path
import csv
import json
from xml.dom import minidom


class Inventory:
    @classmethod
    def import_data(cls, report_type, arquive):
        extension = os.path.splitext(arquive)[1]

        type_file = {
            ".json": cls.convert_json_to_Dict,
            ".csv": cls.convert_csv_to_Dict,
            ".xml": cls.convert_xml_to_Dict,
        }
        file_to_report = type_file[extension](arquive)

        if report_type == "simple":
            return SimpleReport.generate(file_to_report)
        if report_type == "complete":
            return CompleteReport.generate(file_to_report)

    @classmethod
    def convert_csv_to_Dict(cls, path_to_file):
        with open(path_to_file) as file:
            header, *csvLines = csv.reader(file, delimiter=",")
            return [
                {item: line[index] for index, item in enumerate(header)}
                for line in csvLines
            ]

    @classmethod
    def convert_json_to_Dict(cls, path_to_file):
        with open(path_to_file) as file:
            return json.load(file)

    @classmethod
    def convert_xml_to_Dict(cls, path_to_file):
        xml = minidom.parse(path_to_file)
        records = xml.getElementsByTagName("record")
        return [
            {node.tagName: node.firstChild.data for node in record.childNodes}
            for record in records
        ]

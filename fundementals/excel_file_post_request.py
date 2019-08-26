import xlsxwriter
from flask import Flask, request

from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app, prefix='/api/v1.0')


class Exceltask(Resource):
    def post(self):
        data = request.get_json()
        filename = data["filename"]

        excel_file = filename + '.' + 'xlsx'

        workbook = xlsxwriter.Workbook(excel_file)
        sheet1 = workbook.add_worksheet('sheet1')
        sheet2 = workbook.add_worksheet('sheet2')
        for item in data["filedata"]:
            if item["sheetname"] == "sheet1":
                for subitem in item["sheetdata"]:
                    for i in range(len(subitem)):
                        for j in range(len(subitem)):
                            sheet1.write(i, j, item["sheetdata"][i][j])
            else:
                for subitem in item["sheetdata"]:
                    for i in range(len(subitem)):
                        for j in range(len(subitem)):
                            sheet2.write(i, j, item["sheetdata"][i][j])
        workbook.close()
        return "Sheet data added successfully"


api.add_resource(Exceltask, '/tasks')

if __name__ == "__main__":
    app.run(debug=True)

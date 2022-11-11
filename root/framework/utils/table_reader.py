import xlrd


class TableReader:

    def get_all_data_from_xls_table(self, path, sheet_number=0):

        result = []
        book = xlrd.open_workbook(path)
        sheet = book.sheet_by_index(sheet_number)
        headers = sheet.row_values(0)
        for row_number in range(1, sheet.nrows):
            item = {}
            row_vals = sheet.row_values(row_number)
            for i in range(len(headers)):
                if row_vals[i] != '':
                    try:
                        row_vals[i] = int(row_vals[i])
                    except ValueError:
                        item[headers[i]] = row_vals[i].replace(u'\xa0', u' ')
                    else:
                        item[headers[i]] = row_vals[i]
            result.append(item)

        return result

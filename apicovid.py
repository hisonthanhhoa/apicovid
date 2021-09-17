import requests
import xlsxwriter
c= ""
api = 'https://api.covid19api.com/'

print('Enter country (slug or ISO2, view in https://api.covid19api.com/countries): ')
country = input("nhap ten quoc gia ban can : ")

request = requests.get(''.join([api, 'dayone/country/', country])).json()

if (isinstance(request, dict) and request['message'] == 'Not Found'):
    print('Country not found. Please try again.')
    exit()

if (isinstance(request, list)):
    currentData = request[-1]
    workbook = xlsxwriter.Workbook(country+'.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'Country')
    worksheet.write('B1', 'Confirmed')
    worksheet.write('C1', 'Deaths')
    worksheet.write('D1', 'Recovered')
    worksheet.write('E1', 'Active')
    worksheet.write('F1', 'Date')

    worksheet.write('A2', currentData['Country'])
    worksheet.write('B2', currentData['Confirmed'])
    worksheet.write('C2', currentData['Deaths'])
    worksheet.write('D2', currentData['Recovered'])
    worksheet.write('E2', currentData['Active'])
    worksheet.write('F2', currentData['Date'])

    workbook.close()

    print('Done')
    exit()

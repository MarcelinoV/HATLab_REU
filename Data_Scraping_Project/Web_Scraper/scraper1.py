from bs4 import BeautifulSoup
import csv
import requests


# Establish link to page and store source content
print('Connecting...')

pages = ['34', '38', '41']

for i in pages:

    page = requests.get('https://community.myfitnesspal.com/en/discussion/10703170/what-were-eating/p' + i)
    src = page.content

    # Verify connection to page is good

    print('Connection established') if page.status_code == 200 else 'Error'

    print('Reading page...')

    # create BS4 object
    soup = BeautifulSoup(src, 'html.parser')

    # CSS selector of specific div tag targeted for scraping
    # container = soup.select('#vanilla_discussion_index > div.container > div.row > div.content.column > div.CommentsWrap > div.DataBox.DataBox-Comments > ul')

    # select and store div classes of targets (username, date, comment)
    postdata = soup.select('.Message')
    userdata = soup.select('.Username')
    datedata = soup.select('.DateCreated')

    # declare list where data will be stored
    all_data = []

    # parse/scrape data and store in all_data
    print('Parsing data...')

    for u, d, m in zip(userdata, datedata, postdata):
        all_data.append([u.text,
                         d.get_text(strip=True),
                         m.get_text(strip=True, separator='\n')])

    # write to csv file
    print('Writing to CSV...')

    with open('mfp_data' + i + '.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['user', 'date', 'post'])
        for row in all_data:
            writer.writerow(row)

    # End program
    print('Done')

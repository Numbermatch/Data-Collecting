import PyPDF2
import bs4 as bs
from urllib.request import Request, urlopen, urlretrieve
import requests
from io import BytesIO

tempRay = list()

def get_our_Soup(urlText):
	req = Request(urlText, headers={'User-Agent': 'Mozilla/5.0'})
	ourSource = urlopen(req).read()
	soup = bs.BeautifulSoup(ourSource, 'lxml')
	
	return soup

webScript = get_our_Soup('https://www.soa.org/education/general-info/exam-results/edu-exam-results-detail/')

for options in webScript.find_all('a'):
	if options.get('href') != None and options.get('href').find(".pdf") != -1 and options.get('href').find("names") != -1:
		PDFNAME = options.get('href')
		sourceURL = "https://www.soa.org" + PDFNAME
		x = sourceURL.split('/')[-1].replace(' ', '_')

		response = requests.get(sourceURL)
		my_raw_data = response.content
		
		ourCounter = 1
		
		with BytesIO(my_raw_data) as data:
			pdfReader = PyPDF2.PdfFileReader(data)
			
			for page in range(pdfReader.getNumPages()):
				text = pdfReader.getPage(page).extractText().replace("\n","")
				ourTest = False

				while (ourTest == False):
				
					if text.find(str(ourCounter) + ".") != -1 and text.find(str(ourCounter + 1) + ".") != -1:
						inputText = text[text.find(str(ourCounter) + "."):text.find(str(ourCounter + 1) + ".")]
						inputText = inputText.replace(str(ourCounter) + ".", "")
						tempRay.append(PDFNAME.split("-")[2] + "," + PDFNAME.split("-")[3] + "," + PDFNAME.split("-")[4] + "," + inputText)
					else:
						inputText = text[text.find(str(ourCounter) + "."):len(text)]
						inputText = inputText.replace(str(ourCounter) + ".", "")
						tempRay.append(PDFNAME.split("-")[2] + "," + PDFNAME.split("-")[3] + "," + PDFNAME.split("-")[4] + "," + inputText)
						ourTest = True
					
					ourCounter = ourCounter + 1

for i in range(len(tempRay)):
	print(tempRay[i])

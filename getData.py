import gspread
from oauth2client.service_account import ServiceAccountCredentials
from textblob import TextBlob

# Setup para acceder a Google Sheets
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('sentiment-analysis-credentials.json', scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("1GPRL6u9UoXaqx-G13o37R1N_IhndSqmJHAhne4tN9cU").sheet1

# Leer datos de la hoja de cálculo
data = sheet.get_all_records()

# Analizar sentimientos
for item in data:
    title = item['title']
    description = item['description']
    title_analysis = TextBlob(title)
    description_analysis = TextBlob(description)

    combined_polarity = (title_analysis.sentiment.polarity + description_analysis.sentiment.polarity) / 2
    combined_subjectivity = (title_analysis.sentiment.subjectivity + description_analysis.sentiment.subjectivity) / 2

    print(f"Date: {item['date']}\nTitle: '{title}'\nPolarity: {title_analysis.sentiment.polarity:.2f}, subjectivity: {title_analysis.sentiment.subjectivity:.2f}")
    print(f"Description: '{description}'\nPolarity: {description_analysis.sentiment.polarity:.2f}, subjectivity: {description_analysis.sentiment.subjectivity:.2f}")
    print(f"Combined Sentiment: Polarity: {combined_polarity:.2f}, subjectivity: {combined_subjectivity:.2f}\n")


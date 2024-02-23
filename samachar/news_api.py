import requests

api_key = '483b04da5f7243438b5dd5cf07819eb7'

try:
    url = f'https://newsapi.org/v2/everything?q=Apple&from=2024-02-23&sortBy=popularity&apiKey={api_key}'
    response = requests.get(url).json()

    # Check if the request was successful
    if response['status'] == 'ok':
        # Access the articles
        articles = response['articles']
        
        # Assuming you want the first article, you can access its details
        if articles:
            article = articles[0]  # Get the first article
            title = article.get('title', 'Title not available')
            author = article.get('author', 'Author not available')
            description = article.get('description', 'Description not available')
            image = article.get('urlToImage', 'Image not available')

            news_list = [title, author, description, image]
        else:
            print("No articles found.")
    else:
        print("Request failed:", response.get('message', 'Unknown error'))

except requests.RequestException as e:
    print("Request failed:", e)

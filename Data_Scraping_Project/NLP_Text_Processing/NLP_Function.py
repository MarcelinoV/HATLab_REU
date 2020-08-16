# Function to streamline NLP Process

def nlp(file):
    # Load Dataset
    raw_data = pd.read_csv(file + '.csv')
    
    # Convert to lowercase
    raw_data['post'] = [post.lower() for post in raw_data['post']]

    # Word & Sentence Tokenization
    token_post = [word_tokenize(post) for post in raw_data['post']]

    sent_token = [sent_tokenize(post) for post in raw_data['post']]
    
    # Remove Punctuation
    reg = re.compile('(@[a-z0-9]+)|([^0-9a-z \t])|(\w+:\/\/\S+)')

    no_punc = []

    for filt in token_post:
        review = []
        for token in filt:
            new_token = reg.sub(u'', token)
            if not new_token == u'':
                review.append(new_token)
        no_punc.append(review)
        
    # Remove Stopwords
    no_stop = []

    for post in no_punc:
        new_term_vector = []
        for word in post:
            if not word in stopwords.words('english'):
                new_term_vector.append(word)

        no_stop.append(new_term_vector)
        
    # Stemming & Lemmatization
    pstem = PorterStemmer()
    wlem = WordNetLemmatizer()

    preproc_text = []

    for text in no_stop:
        final_text = []
        for word in text:
            pstem.stem(word)
            final_text.append(wlem.lemmatize(word))

        preproc_text.append(final_text)
        
    # create final data set
    data = raw_data.copy()

    new_col = pd.Series(preproc_text)
    data['post'] = new_col
    print(data.head(5))
    
    # save processed data to csv
    data.to_csv(file + '_proc.csv', index=False,header=True, encoding='utf-8')
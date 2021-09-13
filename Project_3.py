with open('stopwords.txt','r',encoding = 'UTF-8') as stops:
    eng_words = [line.rstrip() for line in stops]
#print(eng_words)

def distill_tweet(tweet):
    words = tweet.lower().translate(tweet.maketrans("'-",'  ','.,!?\\|"')).split()
    result = []
    for word in words:
        if not (word in eng_words or word.startswith('https' and 'http') or word.isdigit()):         
            result.append(word)
    return result

def tweet_lists(filename): #this code works, don't change it, but you need to use it
    result = []
    cur_name = ''
    with open(filename, 'r', encoding='UTF8') as file:
        for line in file:
            line = line.split('\t')
            user = line[1]
            tweet = line[2]
            if user == cur_name:
                cur = open(user + '.txt', 'a')
            else:
            	if cur_name != '':
            		cur.close()
            	cur_name = user
            	result += [user]
            	cur = open(user + '.txt', 'w')
            cur.writelines(tweet + '\n')
            cur.close()
    return result

def tweets_from_file(filename):
    with open(filename, 'r', encoding='UTF8') as tweets:
        return [line for line in tweets]
        
    
def top_entries(tweets, num_cutoff = 1, hashes = False, mentions = False):
    entries = {}
    words = []
    for line in tweets:
        words += distill_tweet(line)
    for word in words:
        if words.count(word) >= num_cutoff:
            if hashes == True:
                if word.startswith('#'):
                    entries[word] = words.count(word)
            elif mentions == True:
                if word.startswith('@'):
                    entries[word] = words.count(word)
            else:
                if not (word.startswith('#') or word.startswith('@')):
                    entries[word] = words.count(word)
    return entries
    
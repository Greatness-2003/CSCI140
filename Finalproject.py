import datetime
import pandas as pd
import random
import numpy as np


class Forum_Page:

    def __init__(self, name):
        self.__name = name
        self.__board = pd.DataFrame(columns = ['Title','Date', 'Author', 'Post', 'Votes'])
        self.__board.set_index('Title', inplace = True)
        self.__board['Votes'] = self.__board['Votes'].astype('int')
        self.__anon_words = self.__process('words.txt')
        
    
    def __process(self, filename):
        with open(filename,'r', encoding = 'UTF8') as file:
            result = [line.rstrip() for line in file]
        return result
        
    def __exists(self, title):
        return title in self.__board.index
    
    def checker(self):
        return self.__board.copy()
    
    def __generate_anon(self):
        x= random.sample(self.__anon_words, k=2)
        y = random.choices(range(0, 9), k=2)
        username = x[0]+'_'+x[1] +'_'+str(y[0])+str(y[1])
        while username in self.__board['Author']:
            x= random.sample(self.__anon_words, k=2)
            y = random.choices(range(0, 9), k=2)
            username = x[0]+'_'+x[1] +'_'+str(y[0])+str(y[1])
        return username
            
        
    def add_post(self, title, post, author = None):
        if not self.__exists(title):
            if author == None:
                author= self.__generate_anon()
            self.__board.loc[title]= [str(datetime.date.today()), author, post, 0]
            
    def delete_post(self, title):
        if self.__exists(title):
            self.__board.loc[title,'Author'] = np.nan
            self.__board.loc[title, 'Post'] = np.nan
        
    def vote_post(self, title, up = True):
        if self.__exists(title):
            if pd.notnull(self.__board.loc[title,'Author']):
                if up == False:
                    self.__board.loc[title,'Votes'] -=1
                else:
                    self.__board.loc[title,'Votes'] +=1
           
    def top_voted(self):
        return self.__board.loc[self.__board['Votes']== self.__board['Votes'].max()]
        
    def get_titles(self):
        return self.__board.index.tolist()
        
    def get_post_info(self, title):
        if self.__exists(title):
            return self.__board.loc[title].tolist()
             
    
    def get_name(self):
        return self.__name
        
    def __str__(self):
        count = self.__board['Post'] 
        df_2 = count.value_counts(dropna = True)
        return str(df_2.sum()) + ' active posts on ' + str(self.__name)
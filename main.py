from kivy.config import Config
Config.set('graphics', 'width', '390')
Config.set('graphics', 'height', '650')


from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.behaviors import (
    BackgroundColorBehavior,
    RectangularElevationBehavior,
)

from kivymd.uix.button import MDFillRoundFlatButton, MDFillRoundFlatIconButton, MDFlatButton, MDRaisedButton
from kivymd.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty,StringProperty
from kivymd.uix.picker import MDDatePicker
from datetime import datetime, date
from kivymd.uix.bottomsheet import MDListBottomSheet
#from kivymd.toast import toast
from kivymd.uix.backdrop import MDBackdrop, MDBackdropBackLayer,MDBackdropFrontLayer
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCardSwipe,MDCard
from kivy.uix.screenmanager import ScreenManager
#from kivy.uix.widget import Widget
import json

from kivymd.uix.list import OneLineListItem
from kivymd_extensions.sweetalert import SweetAlert
#custom python files
from imdb import * 
import ui.rating as rate


screen_manager = None

class login(MDScreen):
    pass

class signup(MDScreen):
    pass

class forgot(MDScreen):
    pass

class verification(MDScreen,MDApp):
    pass

class MyMDCard(MDCard):
    title = StringProperty()
    img = StringProperty()
    info = StringProperty()    

class shahryar(MDScreen):    
    title = ObjectProperty(None)   
    # add_series_date = ObjectProperty(None)
    # add_series_title = ObjectProperty(None)
    # add_series_showrunner = ObjectProperty(None)
    # add_series_rating = ObjectProperty(None)
    # add_series_genre = ObjectProperty(None)
    # add_series_review = ObjectProperty(None)

    # #All of Add movie Textfields

    
    # add_movie_title = ObjectProperty(None)
    # add_movie_director = ObjectProperty(None)
    # add_movie_date = ObjectProperty(None)
    # add_movie_rating = ObjectProperty(None)
    # add_movie_review = ObjectProperty(None)
    # add_movie_genre = ObjectProperty(None)
    
    #hint for oop App.get_running_app()

    textfield_id = ""
    
  
    
    
    dataList_local = {'Search': [{'Title': 'Scream', 'Year': '1996', 'imdbID': 'tt0117571', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMjA2NjU5MTg5OF5BMl5BanBnXkFtZTgwOTkyMzQxMDE@._V1_SX300.jpg'}
                   , {'Title': 'Scream 2', 'Year': '1997', 'imdbID': 'tt0120082', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMDNlM2E2OTUtZTRhZi00ZDU1LWIxODAtN2E5OGZiNmIwMDIwXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg'},
                   {'Title': 'Scream 4', 'Year': '2011', 'imdbID': 'tt1262416', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMTk5OTcxNTUyNF5BMl5BanBnXkFtZTcwMDczMzE0NA@@._V1_SX300.jpg'}, 
                   {'Title': 'Scream 3', 'Year': '2000', 'imdbID': 'tt0134084', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMDljNmI1YzctNjJlZC00NzZlLWFlZTgtMDE4MjJiMDk0ZGY4XkEyXkFqcGdeQXVyMjg3MDQ0Mjk@._V1_SX300.jpg'},
                   {'Title': 'Scream Queens', 'Year': '2015–2016', 'imdbID': 'tt4145384', 'Type': 'series', 'Poster': 'https://m.media-amazon.com/images/M/MV5BYzIwYjkwYTgtNzlhOC00MGZhLWI0OTMtZTAwOTIyNGM4MTJjXkEyXkFqcGdeQXVyMTkzODUwNzk@._V1_SX300.jpg'},
                   {'Title': 'Scream: The TV Series', 'Year': '2015–2019', 'imdbID': 'tt3921180', 'Type': 'series', 'Poster': 'https://m.media-amazon.com/images/M/MV5BNjVmY2M3ZTUtMDhkZC00ODk4LTkwMjktNDRjNGRjYTIxZGZiXkEyXkFqcGdeQXVyNjEwNTM2Mzc@._V1_SX300.jpg'},
                   {'Title': 'Ice Cream, I Scream', 'Year': '2005', 'imdbID': 'tt0816150', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BODRjMjdjZTAtYjgyMy00MWEzLTk5ZTQtNGQzM2I3MTgwN2FlXkEyXkFqcGdeQXVyMTg5MDIyNTk@._V1_SX300.jpg'},
                   {'Title': "Hush! Girls Don't Scream", 'Year': '2013', 'imdbID': 'tt2440036', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BNzA1Nzk2Mzc0Nl5BMl5BanBnXkFtZTgwNDQzNzc2MDE@._V1_SX300.jpg'},
                   {'Title': 'Scream of Fear', 'Year': '1961', 'imdbID': 'tt0055505', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BM2M3MWZkN2MtYTFlYS00M2EzLWFmNzktNmMyMGNmMGQ1N2NmXkEyXkFqcGdeQXVyMjI4MjA5MzA@._V1_SX300.jpg'},
                   {'Title': 'Scream and Scream Again', 'Year': '1970', 'imdbID': 'tt0064949', 'Type': 'movie', 'Poster': 'https://m.media-amazon.com/images/M/MV5BMTMyMzI1MjA3Ml5BMl5BanBnXkFtZTcwOTkyMTM4NA@@._V1_SX300.jpg'}],
        'totalResults': '358',
        'Response': 'True'}
    
    
    def getCommand(self,com):
        command = com
        if(command == "ok"):
            #self.addWatchedSeries()
            print(command)
        elif(command == "cancel"):
            #self.addMoviesSeries
            print(command)
        else:
            print("Error")
    
    def showDialog(self,p):
        
        button_ok = MDRaisedButton(
            text='OK',
            font_size=16,
            on_release = lambda x:self.getCommand('ok'),
        )
        button_cancel = MDFlatButton(
            text='CANCEL',
            font_size=16,
            on_release = lambda x:self.getCommand('cancel'),
            
        )
        if (p == "movie"):
            SweetAlert().fire("Are You Sure (Movies) ?", type='warning', buttons=[button_ok, button_cancel])
        elif(p == "series"):
            SweetAlert().fire("Are You Sure (Series) ?",type='warning', buttons=[button_ok, button_cancel])
        else:
            print("Error")
        
    
    

    def salert(self):
        SweetAlert(timer=1.1,font_style_title="Button").fire("This Feature Will be Implemented in the Future",type="info",)
        
    def handleSearch(self):
        print("hello handleSearch")
        # cardItem = MyMDCard()
        # dataList = imdb.search_title(self,'scream')
        # self.change_screen("movies_list")
        dataList = imdb.search_title(self,screen_manager.get_screen("home").ids.movie_title.text)
        if (len(dataList) > 0):
            for i in range(len(dataList["Search"])):
                title = dataList["Search"][i]["Title"] 
                year = dataList["Search"][i]["Year"]
                img = dataList["Search"][i]["Poster"]
                id = dataList["Search"][i]["imdbID"]
                dtype = dataList["Search"][i]["Type"]
                
                screen_manager.get_screen("search_list").ids.movielist_dynamic.add_widget(MyMDCard(
                    title=title,
                    img = img,
                    info = "This " + dtype + " was released in  " + year + " with imdb id of  " + id 
                ))
        else:
            print("No Results found")
        self.change_screen("search_list")
        print(len(dataList["Search"]))
    
    
    def handleMovies(self):
        print("hello handleMovie")
        # cardItem = MyMDCard()
        #dataList = imdb.search_title(self,'scream')
        # self.change_screen("movies_list")
        for i in range(len(self.dataList_local["Search"])):
            title = self.dataList_local["Search"][i]["Title"] 
            year = self.dataList_local["Search"][i]["Year"]
            img = self.dataList_local["Search"][i]["Poster"]
            id = self.dataList_local["Search"][i]["imdbID"]
            dtype = self.dataList_local["Search"][i]["Type"]
            
            screen_manager.get_screen("movies_list").ids.movielist_dynamic.add_widget(MyMDCard(
                title=title,
                img = img,
                info = "This " + dtype + " was released in " + year + "with imdb id of " + id 
            ))
        self.change_screen("movies_list")
        # print(len(self.dataList_local["Search"]))
           
    def handleSeries(self):
        print("hello handleSeries")
        # cardItem = MyMDCard()
        #dataList = imdb.search_title(self,'scream')
        # self.change_screen("movies_list")
        for i in range(len(self.dataList_local["Search"])):
            title = self.dataList_local["Search"][i]["Title"] 
            year = self.dataList_local["Search"][i]["Year"]
            img = self.dataList_local["Search"][i]["Poster"]
            id = self.dataList_local["Search"][i]["imdbID"]
            dtype = self.dataList_local["Search"][i]["Type"]
            
            screen_manager.get_screen("series_list").ids.serieslist_dynamic.add_widget(MyMDCard(
                title=title,
                img = img,
                info = "This " + dtype + " was released in " + year + "with imdb id of " + id 
            ))
        self.change_screen("series_list")
        # print(len(self.dataList_local["Search"]))
        
    
        
        
    
    
    
    # m = MDScreen()
        
    def change_screen(self,name):
        screen_manager.current = name
    
    def clear_all(self,id):
       if(id == "movie"):
            #self.screen.get_screen('home').ids.forgot_email.text
            #self.root.manager.get_screen('<screen name>').ids
            screen_manager.get_screen("home").ids.add_movie_title.text = ""
            screen_manager.get_screen("home").ids.add_movie_director.text = ""
            screen_manager.get_screen("home").ids.add_movie_date.text = ""
            screen_manager.get_screen("home").ids.add_movie_rating.text = ""
            screen_manager.get_screen("home").ids.add_movie_review.text = ""
            screen_manager.get_screen("home").ids.add_movie_genre.text = ""
       if(id == "series"): 
            screen_manager.get_screen("home").ids.add_series_date.text = ""
            screen_manager.get_screen("home").ids.add_series_title.text = ""
            screen_manager.get_screen("home").ids.add_series_showrunner.text = ""
            screen_manager.get_screen("home").ids.add_series_rating.text = ""
            screen_manager.get_screen("home").ids.add_series_genre.text = ""
            screen_manager.get_screen("home").ids.add_series_review.text = ""
    
    
    def search(self):
        retrieved_data = imdb.search_title(self,screen_manager.get_screen("home").ids.movie_title.text)
        print(retrieved_data)
        
        
        
    
    def get_date(self,date):
        #print("get date function")
        #print(str(self.textfield_id) + " in the get_date function")
        #print(date)
        if(self.textfield_id == "movie"):
            screen_manager.get_screen("home").ids.add_movie_date.text = str(date)
        if(self.textfield_id == "series"):
            screen_manager.get_screen("home").ids.add_series_date.text = str(date)
    
      
    def show_date_picker(self,id):
            '''Open time picker dialog.'''
            #min_date = datetime.strptime("2021:02:15", '%Y:%m:%d').date()
            #max_date = datetime.strptime("2021:02:20", '%Y:%m:%d').date()
            self.textfield_id = id
            #print(self.textfield_id + " in the show_date_picker function")
            date_dialog = MDDatePicker(callback=self.get_date)
            date_dialog.open()
            
    def callback_for_menu_items(self, *args):
        #self.add_movie_genre.text = str(args[0]) 
        #toast(args[0])
        if(self.textfield_id == "movie"):
            screen_manager.get_screen("home").ids.add_movie_genre.text = str(args[0])
        if(self.textfield_id == "series"):
            #print(self.add_series_genre.text)
            screen_manager.get_screen("home").ids.add_series_genre.text = str(args[0])
    
    def show_genre_list_bottom_sheet(self,id):
        self.textfield_id = id
        bottom_sheet_menu = MDListBottomSheet()
        bottom_sheet_menu.radius_from = "top"
       
        
        genre = ["Horror","Action","Comedy","Supernatural","Superhero","Sci-Fi","Romantic"]
        for i in genre:
            bottom_sheet_menu.add_item(i,lambda x, y=i:self.callback_for_menu_items(f"{y}"), )
        bottom_sheet_menu.open()
    



     

    
    

    
    

class RectangularElevationButton(RectangularElevationBehavior,
                                MDFillRoundFlatIconButton):
    md_bg_color = [0, 0, 1, 1]

class TodayScreenElevationButton(RectangularElevationBehavior,
                                MDFillRoundFlatButton):
    pass

class RectangularElevationListItem(RectangularElevationBehavior,
                                    BackgroundColorBehavior,
                                    TwoLineAvatarIconListItem):
    md_bg_color = [1, 1, 1, 1]

class MyApp(MDApp):
    shahryar = shahryar()
    
  
    
    def build(self):
        global screen_manager
        
        screen_manager = ScreenManager()
        
        screen_manager.add_widget(Builder.load_file("ui//login.kv"))
        screen_manager.add_widget(Builder.load_file("ui//signup.kv"))
        screen_manager.add_widget(Builder.load_file("ui//forgot.kv"))
        screen_manager.add_widget(Builder.load_file("ui//verification.kv"))
        screen_manager.add_widget(Builder.load_file('main_screen.kv'))
        screen_manager.add_widget(Builder.load_file("ui//movies_list.kv"))
        screen_manager.add_widget(Builder.load_file("ui//series_list.kv"))
        screen_manager.add_widget(Builder.load_file("ui//search_list.kv"))
        
        self.theme_cls.theme_style="Light"
        
        #Builder.load_file("ui//login.kv")
        #main = Builder.load_file('main.kv')
        return screen_manager
        
    
        

MyApp().run()
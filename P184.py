from tkinter import *
import requests
import json
root=Tk()
root.title('P184')
root.geometry('600x600')
root.configure(background='lightgrey')

newsupdate = Label(root,text='BBC News Update',font=('Arial',20,'bold'),padx=5,pady=10,bg='lightgrey')
newsupdate.pack()

news1 = Label(root,font=('Arial',18,'bold'),bg='lightgrey',fg='green',wraplength=500)
news1.pack()
news_desc1 = Label(root,font=('Arial',18,'bold'),bg='lightgrey',fg='black',wraplength=500)
news_desc1.pack()

news2 = Label(root,font=('Arial',18,'bold'),bg='lightgrey',fg='green',wraplength=500)
news2.pack()
news_desc2 = Label(root,font=('Arial',18,'bold'),bg='lightgrey',fg='black',wraplength=500)
news_desc2.pack()

news3 = Label(root,font=('Arial',18,'bold'),bg='lightgrey',fg='green',wraplength=500)
news3.pack()
news_desc3 = Label(root,font=('Arial',18,'bold'),bg='lightgrey',fg='black',wraplength=500)
news_desc3.pack()

news4 = Label(root,font=('Arial',18,'bold'),bg='lightgrey',fg='green',wraplength=500)
news4.pack()
news_desc4 = Label(root,font=('Arial',18,'bold'),bg='lightgrey',fg='black',wraplength=500)
news_desc4.pack()

news5 = Label(root,font=('Arial',18,'bold'),bg='lightgrey',fg='green',wraplength=500)
news5.pack()
news_desc5 = Label(root,font=('Arial',18,'bold'),bg='lightgrey',fg='black',wraplength=500)
news_desc5.pack()

api_request = requests.get('https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=131f896369be4708a25b32f58e306116')
open_bbc_page = json.loads(api_request.content)

title1 = open_bbc_page['articles'][0]['title']
desc1 = open_bbc_page['articles'][0]['description']

title2 = open_bbc_page['articles'][1]['title']
desc2 = open_bbc_page['articles'][1]['description']

title3 = open_bbc_page['articles'][2]['title']
desc3 = open_bbc_page['articles'][2]['description']

title4 = open_bbc_page['articles'][3]['title']
desc4 = open_bbc_page['articles'][3]['description']

title5 = open_bbc_page['articles'][4]['title']
desc5 = open_bbc_page['articles'][4]['description']

news1['text'] = 'Title 1: ' + str(title1)
news_desc1['text'] = 'Description: ' + str(desc1)

news2['text'] = 'Title 2: ' + str(title2)
news_desc2['text'] = 'Description: ' + str(desc2)

news3['text'] = 'Title 3: ' + str(title3)
news_desc3['text'] = 'Description: ' + str(desc3)

news4['text'] = 'Title 4: ' + str(title4)
news_desc4['text'] = 'Description: ' + str(desc4)

news5['text'] = 'Title 5: ' + str(title5)
news_desc5['text'] = 'Description: ' + str(desc5)

mainloop()
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request,redirect,url_for,session,logging,flash
from flask_mysqldb import MySQL

#<h3 class="text-color-inherit margin-top-10"><a href="/faculty/pn-kumar">Dr. (Col.) Kumar P. N.</a></h3>

URL ='https://www.amrita.edu/school/engineering/coimbatore/computer-science/faculty'
page = requests.get(URL)

soup= BeautifulSoup(page.content,'html.parser')
# print(soup.find("a", { "class" : "text-color-inherit margin-top-10"}))

with open("out.html", "w", encoding='utf-8') as file:
    file.write(str(soup))

# app = Flask(__name__)

# @app.route('/')
# def front():
# 	return 
    
# if __name__ == '__main__':
#     app.run(debug = True )
    


# import httplib2
# from bs4 import BeautifulSoup, SoupStrainer

# http = httplib2.Http()
# status, response = http.request('https://www.amrita.edu/faculty?field_faculty_department_tid=All&field_faculty_designation_tid=All&field_faculty_campus_tid=53&field_faculty_department_main_tid=101&field_center_name_tid=All')

# for link in BeautifulSoup(response,'html.parser', parse_only=SoupStrainer('a')):
#     if link.has_attr('href'):
#         print(link['href'])
# "col-sm-4 col-sm-3 margin-bottom-10"
      
  
  
  
      
 
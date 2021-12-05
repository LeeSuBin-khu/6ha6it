import pandas
import matplotlib.pyplot
matplotlib.pyplot.switch_backend('agg')
import os
import sys

def make_html():
    dir = os.path.dirname(os.path.realpath(__file__))
    temp2 = dir + '\\templates\\hb_main\\statistics.html'
    html_file = open(temp2, 'w')
    #html_file = open('C:\\Users\\subin\\Desktop\\habitt\\6ha6it\\wp_pj8\\habit\\hb_main\\templates\\hb_main\\statistics.html', 'w')
    html_file.write("<html>\n<head>\n<title>statics</title>\n{% load static %}\n")

    html_file.write('<style type="text/css">\n#body {\nbackground: white url("background.jpg") repeat;\n}\n.stat-body{background: url("../../static/hb_main/image/background.jpg")}\n#calendar {\n\nborder-radius: 5px;\n-moz-border-radius: 5px;\n}\n')
    html_file.write('#calendar table {\nborder-collapse: collapse;\nbackground-color: white;\nmargin: 10px auto;\nfont-size: 18px;\npadding: 0px\nborder= 0px;\n}\n')
    html_file.write('td, th {\n\ntext-align: center;\nvertical-align: middle;\ncolor: #444;\nposition: relative;\n}\n')
    html_file.write('th {\n\nfont-weight: bold;\nfont-size: 14px;\nborder: 1px solid #444444;}\ntbody{width: 40px;}')
    html_file.write('th.month {\ntext-align: center;\n}\ntd {\nborder: 1px solid #444444;\n width: 40px;}\ntd.noday {\nborder: 0px;\n}\ntd:hover {\ncolor: #222;\n}\ntd.action_day {\ncolor:#21b7d5;;\nfont-weight: bold;\n}\n</style>\n')
    
    html_file.write('</head>\n<body class="stat-body">\n<div id="calendar" style="display:flex; margin-left: 330px">')
    html_file.close()
    return html_file

def month_html(htmlCalendar, month_action, data):
    for month in month_action: #월별 결과 값 html 추가
        q = htmlCalendar.formatmonth(2021, month, data)
        dir = os.path.dirname(os.path.realpath(__file__))
        temp2 = dir + '\\templates\\hb_main\\statistics.html'
        html_file = open(temp2, 'a')
        #html_file = open('C:\\Users\\subin\\Desktop\\habitt\\6ha6it\\wp_pj8\\habit\\hb_main\\templates\\hb_main\\statistics.html', 'a')
        html_file.write(q)
        if month==month_action[len(month_action)-1]:
            html_file.write("</div>\n") #"(\n</body>\n</html>")
        html_file.close()
    return html_file

def day_html(data):
    dir = os.path.dirname(os.path.realpath('day.xlsx'))
    temp = dir + '\\day.xlsx'
    data=pandas.read_excel(temp) #엑셀 데이터 읽기
    #data=pandas.read_excel("C:\\Users\\subin\\Desktop\\habitt\\6ha6it\\wp_pj8\\habit\\day.xlsx")
    data=pandas.DataFrame(data)
    num=0
    for i in data.action:
        if i==True:
            num+=1
    sum_statistic=(num/66)*100
    ratio=[sum_statistic,100-sum_statistic]
    label=["action","non"]
    color=['#21b7d5','white']
    wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}
    #print(round(sum_statistic,1))
    matplotlib.pyplot.title('day action result')
    matplotlib.pyplot.pie(ratio, labels=label, autopct='%.1f%%',colors=color, wedgeprops=wedgeprops)
    dir = os.path.dirname(os.path.realpath(__file__))
    temp3 = dir + '\\static\\hb_main\\image\\savefig_day.png'
    matplotlib.pyplot.savefig(temp3, transparent = True)
    #matplotlib.pyplot.savefig('C:\\Users\\subin\\Desktop\\habitt\\6ha6it\\wp_pj8\\habit\\hb_main\\static\\hb_main\\image\\savefig_day.png', transparent = True)
    dir = os.path.dirname(os.path.realpath(__file__))
    temp2 = dir + '\\templates\\hb_main\\statistics.html'
    html_file = open(temp2, 'a')
    #html_file = open('C:\\Users\\subin\\Desktop\\habitt\\6ha6it\\wp_pj8\\habit\\hb_main\\templates\\hb_main\\statistics.html', 'a')
    html_file.write('<div class="img-container" style="margin-left: 330px;"><img src="{% static \'hb_main/image/savefig_day.png\' %}" style="width: 500px; height: 400px;">')
    html_file.close()
    matplotlib.pyplot.clf()
    return html_file

def week_html(data):
    dir = os.path.dirname(os.path.realpath('day.xlsx'))
    temp = dir + '\\day.xlsx'
    data=pandas.read_excel(temp) #엑셀 데이터 읽기
    #data=pandas.read_excel("C:\\Users\\subin\\Desktop\\habitt\\6ha6it\\wp_pj8\\habit\\day.xlsx")
    data=pandas.DataFrame(data)
    num2=list()
    for i in range(66):
        if i%7==0:
            if i!=0:
                num2.append(len(temp))
            temp=list()
        if data.action[i]==True:
            temp.append(data.action[i])
        if i==65:
            num2.append(len(temp))
    x=[1,2,3,4,5,6,7,8,9,10]
    matplotlib.pyplot.title('week action result')
    matplotlib.pyplot.ylabel('7 days')
    matplotlib.pyplot.xlabel('weeks')
    matplotlib.pyplot.ylim(0,7)
    matplotlib.pyplot.xlim(1,10)
    matplotlib.pyplot.plot(x, num2, color="#21b7d5")
    dir = os.path.dirname(os.path.realpath(__file__))
    temp3 = dir + '\\static\\hb_main\\image\\savefig_week.png'
    matplotlib.pyplot.savefig(temp3, transparent = True)
    #matplotlib.pyplot.savefig('C:\\Users\\subin\\Desktop\\habitt\\6ha6it\\wp_pj8\\habit\\hb_main\\static\\hb_main\\image\\savefig_week.png', transparent = True)
    # dir = os.path.dirname(os.path.realpath('statistics.html'))
    # temp2 = dir + '\\statistics.html'
    # html_file = open(temp2, 'a')
    dir = os.path.dirname(os.path.realpath(__file__))
    temp2 = dir + '\\templates\\hb_main\\statistics.html'
    html_file = open(temp2, 'a')
    #html_file = open('C:\\Users\\subin\\Desktop\\habitt\\6ha6it\\wp_pj8\\habit\\hb_main\\templates\\hb_main\\statistics.html', 'a')
    html_file.write('<img src="{% static \'hb_main/image/savefig_week.png\' %}" style="width: 500px; height: 400px;"></div>')
    html_file.write('\n</body>\n</html>')
    html_file.close()
    matplotlib.pyplot.clf()
    return html_file


    
    
    
    
    
    


    



    

	
    
    



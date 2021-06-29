import pandas
import matplotlib.pyplot
matplotlib.pyplot.switch_backend('agg')

def make_html():
    html_file = open('C:\\Users\\subin\\Desktop\\wp_pj8\\habit\\hb_main\\templates\\hb_main\\statistics.html', 'w')
    html_file.write("<html>\n<head>\n<title>statics</title>\n{% load static %}\n")

    html_file.write('<style type="text/css">\n#body {\nbackground: white url("background.jpg") repeat;\n}\n#calendar {\nwidth: 310px;\nborder-radius: 5px;\n-moz-border-radius: 5px;\n}\n')
    html_file.write('#calendar table {\nborder-collapse: collapse;\nbackground-color: white;\nmargin: 10px auto;\nfont-size: 18px;\npadding: 0px\nborder= 0px;\n}\n')
    html_file.write('td, th {\nwidth: 40px;\nheight: 40px;\ntext-align: center;\nvertical-align: middle;\ncolor: #444;\nposition: relative;\n}\n')
    html_file.write('th {\nheight: 20px;\nfont-weight: bold;\nfont-size: 14px;\n}\n')
    html_file.write('th.month {\ntext-align: center;\n}\ntd {\nborder: 1px solid white;\n}\ntd.noday {\nborder: 0px;\n}\ntd:hover {\ncolor: #222;\n}\ntd.action_day {\ncolor:#21b7d5;;\nfont-weight: bold;\n}\n</style>\n')
    
    html_file.write('</head>\n<body>\n<div id="calendar" style="float: left;">')
    html_file.close()
    return html_file

def month_html(htmlCalendar, month_action, data):
    for month in month_action: #월별 결과 값 html 추가
        q = htmlCalendar.formatmonth(2021, month, data)
        html_file = open('C:\\Users\\subin\\Desktop\\wp_pj8\\habit\\hb_main\\templates\\hb_main\\statistics.html', 'a')
        html_file.write(q)
        if month==month_action[len(month_action)-1]:
            html_file.write("</div>\n") #"(\n</body>\n</html>")
        html_file.close()
    return html_file

def day_html(data):
    data=pandas.read_excel("C:\\Users\\subin\\Desktop\\wp_pj8\\habit\\day.xlsx")
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
    matplotlib.pyplot.savefig('C:\\Users\\subin\\Desktop\\wp_pj8\\habit\\hb_main\\static\\hb_main\\image\\savefig_day.png')
    html_file = open('C:\\Users\\subin\\Desktop\\wp_pj8\\habit\\hb_main\\templates\\hb_main\\statistics.html', 'a')
    html_file.write('<img src="{% static \'hb_main/image/savefig_day.png\' %}">')
    html_file.close()
    matplotlib.pyplot.clf()
    return html_file

def week_html(data):
    data=pandas.read_excel("C:\\Users\\subin\\Desktop\\wp_pj8\\habit\\day.xlsx")
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
    matplotlib.pyplot.savefig('C:\\Users\\subin\\Desktop\\wp_pj8\\habit\\hb_main\\static\\hb_main\\image\\savefig_week.png')
    html_file = open('C:\\Users\\subin\\Desktop\\wp_pj8\\habit\\hb_main\\templates\\hb_main\\statistics.html', 'a')
    html_file.write('<img src="{% static \'hb_main/image/savefig_week.png\' %}">')
    html_file.write('\n</body>\n</html>')
    html_file.close()
    matplotlib.pyplot.clf()
    return html_file


    
    
    
    
    
    


    



    

	
    
    



from calendar import HTMLCalendar

class HTMLCalendar(HTMLCalendar):
    def formatday(self, day, weekday, action):
        global html
        html='<td class="%s">%d</td>'
        if day==0:
            return '<td class="noday">&nbsp;</td>'
        else:
            for d in action:
                if day==d:
                    html='<td class="action_day %s">%d</td>'
                    return html % (self.cssclasses[weekday], day)
                else:
                    html='<td class="%s">%d</td>'
        return html % (self.cssclasses[weekday], day)
    
    def formatweek(self, theweek, action):
        s=''.join(self.formatday(d, wd, action) for (d,wd) in theweek)
        return '<tr>%s</tr>' % s
        
    def formatmonth(self, theyear, themonth, data, withyear=True):
        action_days=list()
        idx=0
        for j in data.action:
            if j==True:
                action_days.append(data.date[idx])
            idx+=1
        action=[]
        v=[]
        v.append('<table class="month" style="margin-left: -100px; background:transparent;border: 1px solid #444444;border-collapse: collapse;width: 300px; height: 300px;">')
        v.append(self.formatmonthname(theyear, themonth, withyear=withyear))
        v.append(self.formatweekheader())
        for week in self.monthdays2calendar(theyear, themonth):
            for day in action_days:
                if int(day[5:7])==themonth:
                    action.append(int(day[8:10]))
            v.append(self.formatweek(week, action))
        v.append('</table>\n')
        return '\n'.join(v)
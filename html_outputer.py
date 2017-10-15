# 最后的结果输出
# 提供两个功能，一个收集数据，另一个是输出数据


class HtmlOutputer(object):
    # 收集数据需要一个列表list进行维护
    def __init__(self):
        self.datas= []
    #收集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 输出一个html文档
    def output_html(self):
        fout = open("output.html","w",encoding='utf-8')
        fout.write("<html>")
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'>")
        fout.write("<meta charset=\'utf-8\'>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table>")

        #ascii
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

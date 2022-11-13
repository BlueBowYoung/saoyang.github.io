from flask import Flask, render_template

app = Flask(__name__)


book_data = [
    {
        'book':'蔡虚鲲跳跳乐',
        'author': '蓝虹',
        'publish': '跳出鸡你太美~',
        'price': 'C级0.5元',
        'type': '坤坤',
    },
    {
        'book': '鸡乐盒',
        'author': '蓝虹',
        'publish': '坤坤全部音乐，快来体验吧~',
        'price': 'B级1.5元',
        'type': '坤坤',

    },
    {
        'book': '2022新年倒计时',
        'author': '蓝虹',
        'publish': '一起跨年~',
        'price': 'B级1.5元',
        'type': '贺卡',
    },
    {
        'book': '坤坤钢琴块',
        'author': '蓝虹',
        'publish': '鸡~鸡~鸡~',
        'price': 'C级0.5元',
        'type': '坤坤',
    },
    {
        'book': '坤了个坤',
        'author': '蓝虹',
        'publish': '坤了个坤哦~',
        'price': 'A级3元',
        'type': '坤坤',
    },
    {
        'book': '母亲节贺卡',
        'author': '蓝虹',
        'publish': '亲爱的妈妈~',
        'price': 'C级0.5元',
        'type': '贺卡',
    },
    {
        'book': '五一贺卡',
        'author': '蓝虹',
        'publish': '劳动节你要做到五个一',
        'price': 'C级0.5元',
        'type': '贺卡',

    },
    {
        'book': '新年贺卡',
        'author': '蓝虹',
        'publish': '迎接新年，再见旧年~',
        'price': 'C级0.5元',
        'type': '贺卡'
    },
    {
        'book': '经典游戏机',
        'author': '蓝虹',
        'publish': '超十多种游戏~',
        'price': 'S级5.5元',
        'type': '经典',
    },
{
        'book': '小游戏大全',
        'author': 'poki',
        'publish': '超十多种游戏~',
        'price': 'S级5.5元',
        'type': '经典',
    },
{
        'book': '便捷小空调',
        'author': '蓝虹',
        'publish': '没空调那就花0.5元体验空调',
        'price': 'C级0.5元',
        'type': '经典',
    },{
        'book': '友情大考验',
        'author': '蓝虹',
        'publish': '我们是不是好盆友，快来测测吧~',
        'price': 'B级1.5元',
        'type': '贺卡',
    },{
        'book': '表白神器',
        'author': '蓝虹',
        'publish': 'Yes or No，你懂得~',
        'price': 'A级1.5元',
        'type': '贺卡',
    },{
        'book': '生日快乐贺卡',
        'author': '蓝虹',
        'publish': '生日快乐',
        'price': 'C级0.5元',
        'type': '贺卡',
    },{
        'book': '中秋贺卡',
        'author': '蓝虹',
        'publish': '中秋佳节，记得吃月饼~',
        'price': 'C级0.5元',
        'type': '贺卡',
    },{
        'book': '国庆贺卡',
        'author': '蓝虹',
        'publish': '十月国庆',
        'price': 'C级0.5元',
        'type': '贺卡',
    },
{
        'book': '发射篮球',
        'author': '蓝虹',
        'publish': '快用篮球打飞机吧~',
        'price': 'A级1.5元',
        'type': '坤坤',
    },
{
        'book': '表白神器（2）',
        'author': '蓝虹',
        'publish': '无',
        'price': 'C级0.5元',
        'type': '贺卡',
    },{
        'book': '表白神器（3）',
        'author': '蓝虹',
        'publish': '无',
        'price': 'C级0.5元',
        'type': '贺卡',
    }

]


welcome = '欢迎光临，这里有许多的小游戏哦。快选择你感兴趣的游戏吧～'
all_book = '【全部游戏】'
science_book = '【坤坤专题】'
history_book = '【贺卡专题】'
geography_book = '【经典游戏】'
class_book = '【微信支付】'


@app.route('/')
def index():
    return render_template('index.html',t_desc=welcome)

@app.route('/all')
def all():
    return render_template('index.html',t_data=book_data,t_desc=all_book)

@app.route('/science')
def science():
    science = []
    for i in book_data:
        if i['type'] == '坤坤':
            science.append(i)
    return render_template('index.html',t_data=science,t_desc=science_book)

@app.route('/history')
def history():
    history = []
    for i in book_data:
        if i['type'] == '贺卡':
            history.append(i)
    return render_template('index.html',t_data=history,t_desc=history_book)

@app.route('/geography')
def geography():
    geography = []
    for i in book_data:
        if i['type'] == '经典':
            geography.append(i)
    return render_template('index.html',t_data=geography,t_desc=geography_book)



app.run(port=5008, debug=True)

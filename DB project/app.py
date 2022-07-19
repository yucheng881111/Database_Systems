from flask import Flask, render_template, request, jsonify
from database import Database

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

#app的路由地址"/show"即為ajax中定義的url地址，采用POST、GET方法均可提交
@app.route("/show",methods=["GET", "POST"])
def show():
    #首先獲取前端傳入的name資料
    if request.method == "POST":
        year1 = request.form.get("year")
        year2 = request.form.get("year2")
        sortby = request.form.get("sortby")
        limit = request.form.get("limit")
    if request.method == "GET":
        year1 = request.args.get("year")
        year2 = request.args.get("year2")
        sortby = request.args.get("sortby")
        limit = request.args.get("limit")
    
    print(year1, year2)
    if int(year1) > int(year2):
        return jsonify({'status': "error"})

    sql = Database("anime")

    try:
        if sortby == "Score":
            s = 'select \"Name\", \"English name\", \"Score\", \"Popularity\", \"Genres\", \"Episodes\", \"Studios\", \"Duration\", \"Rating\" \
                from \"animelist\" where \"Start_year\" >= '+ year1 +'and \"Start_year\" <= '+ year2 +' \
                order by \"Score\" desc \
                limit '+ limit +''
        else:
            s = 'select \"Name\", \"English name\", \"Score\", \"Popularity\", \"Genres\", \"Episodes\", \"Studios\", \"Duration\", \"Rating\" \
                from \"animelist\" where \"Start_year\" >= '+ year1 +' and \"Start_year\" <= '+ year2 +' \
                and \"Popularity\"<> 0 order by \"Popularity\" \
                limit '+ limit +''

        result = sql.execute(s)

    except Exception as e:
        return {'status':"error", 'message': "code error"}
    else:
        print(result)
        if not len(result) == 0:
            #這個result，我覺得也可以把它當成資料表，查詢的結果至多一個，result[0][0]回傳陣列中的第一行第一列
            #return {'status':'success','message':result[1][2]}
            return jsonify({'status': "success", 'data': result})
        else:
            return "rbq"

@app.route("/show2",methods=["GET", "POST"])
def show2():
    #首先獲取前端傳入的name資料
    if request.method == "POST":
        name = request.form.get("name")
    if request.method == "GET":
        name = request.args.get("name")

    print(name)
    sql = Database("anime")
    s = 'select \"Name\", \"sypnopsis\" from \"animelist\" natural join \"synopsis\" where \"Name\" = \'' + name + '\''
    result = sql.execute(s)
    print(result)
    return jsonify({'status': "success", 'data': result})



app.run(port=8080)




'''
select * from "animelist" where "Start_year" >= 2015 and "Start_year" <= 2020
order by "Popularity"
order by "Score" desc
limit 100
'''







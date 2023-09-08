from django.shortcuts import render
import mysql.connector as sql

def homepage(request):
    user_data = []

    if request.method == "POST":
        query = request.POST.get('query')
        print(query)

        m = sql.connect(host="localhost", user="root", passwd="vishnu", database='website')
        cursor = m.cursor()
        c = "SELECT * FROM users WHERE Last_Name = '{}' OR First_Name = '{}'".format(query, query)
        cursor.execute(c)
        user_data = cursor.fetchall()

    return render(request, 'index.html', {'user_data': user_data})

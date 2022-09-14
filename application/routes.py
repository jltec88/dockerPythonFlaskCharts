from application import app
from flask import render_template, url_for, redirect,flash, get_flashed_messages
from application.form import UserDataForm
from application.models import IncomeExpenses
from application import db
import json
from decimal import *

@app.route('/')
def index():
    entries = IncomeExpenses.query.order_by(IncomeExpenses.date.desc()).all()
    return render_template('index.html', entries = entries)


@app.route('/add', methods = ["POST", "GET"])
def add_expense():
    form = UserDataForm()
    if form.validate_on_submit():
        entry = IncomeExpenses(type=form.type.data, category=form.category.data, amount=form.amount.data)
        db.session.add(entry)
        db.session.commit()
        flash(f"{form.type.data} has been added to {form.type.data}s", "success")
        return redirect(url_for('index'))
    return render_template('add.html', title="Add expenses", form=form)
    


@app.route('/delete-post/<int:entry_id>')
def delete(entry_id):
    entry = IncomeExpenses.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for("index"))


@app.route('/dashboard')    
def dashboard():
    income_vs_expense = db.session.query(db.func.sum(IncomeExpenses.amount), IncomeExpenses.type).group_by(IncomeExpenses.type).order_by(IncomeExpenses.type).all()

    category_comparison = db.session.query(db.func.sum(IncomeExpenses.amount), IncomeExpenses.category).group_by(IncomeExpenses.category).order_by(IncomeExpenses.category).all()

    dates = db.session.query(db.func.sum(IncomeExpenses.amount), IncomeExpenses.date).group_by(IncomeExpenses.date).order_by(IncomeExpenses.date).all()

    income_category = []
    for amounts, _ in category_comparison:
        income_category.append(int(amounts))

    income_expense = []
    for total_amount, _ in income_vs_expense:
        print(total_amount)
        income_expense.append(int(total_amount))
        print(income_expense)
    print(income_expense)
    
    
    over_time_expenditure = []
    dates_label = []
    for amount, date in dates:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_expenditure.append(int(amount))

    """ print("ATENTOOOOOOOOOO")
    print("ATENTOOOOOOOOOO")
    print("ATENTOOOOOOOOOO")
    print("ATENTOOOOOOOOOO")
    print("ATENTOOOOOOOOOO")
    print("ATENTOOOOOOOOOO")
    print("ATENTOOOOOOOOOO")
    print("ATENTOOOOOOOOOO")
    print("ATENTOOOOOOOOOO")
    print("ATENTOOOOOOOOOO")
    print("ATENTOOOOOOOOOO")
    print("ATENTOOOOOOOOOO")
    print("ATENTOOOOOOOOOO")
    print("ATENTOOOOOOOOOO")    
    print(over_time_expenditure)
    parte1 = int(income_expense[0])
    parte2 = int(income_expense[1])
    parte2 = int(income_category[0])
    print(parte1)
    print(parte2) """
    #income_expense = Decimal(income_expense)    
    #income_category=Decimal(income_category)
    #over_time_expenditure=Decimal(over_time_expenditure)
    #dates_label =Decimal(dates_label)
    return render_template('dashboard.html',
                            income_vs_expense=json.dumps(income_expense),
                            income_category=json.dumps(income_category),
                            over_time_expenditure=json.dumps(over_time_expenditure),
                            dates_label =json.dumps(dates_label)
                        )
    
    #dockerpythonflaskcharts_1  | [Decimal('16000'), Decimal('11000')]
    #dockerpythonflaskcharts_1  | [16000, 11000]
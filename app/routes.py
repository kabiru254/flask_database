from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import RegisterForm, ProductForm

@app.route('/')
@app.route('/shop')
def shop():
    """Shop URL"""
    return render_template('shop.html', title='Shop')

@app.route('/products', methods=['GET', 'POST'])
def add_products():
    """Products URL"""
    form = ProductForm()
    if form.validate_on_submit():
        flash(f'You are requesting to add a product {form.product_name.data}')
        return redirect(url_for('shop'))
    return render_template('add_products.html', title='Products', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register URL"""
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'You are requesting to register {form.username.data}')
        return redirect(url_for('shop'))
    return render_template('register.html', title='Register', form=form)
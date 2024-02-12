@app.route('/login', methods=['GET', 'POST'])
def login(): 

    flashed_message = get_flashed_messages(category_filter=['notAuth'])
    flashed_message = ','.join(flashed_message)

    if request.method == 'POST':
        match request.form.get("usernameInput"):
            case "":
                # code
            case "not an empty string":
                # code
    
    return render_template("login.html")
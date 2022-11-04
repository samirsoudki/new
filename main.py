from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
app = Flask(__name__)
df = pd.read_csv("C:\\Users\\Samir\\Desktop\\Data for Samir\\Sawa\\Journal Entry\\SAWA-JE.csv")
print(df.head())
@app.route('/', methods=['GET', 'POST'])
def account_number():
    if request.method == "POST":
        ac_details = request.form["AccountNumber"]
        return redirect(url_for("information", info=ac_details))
    else:
        return render_template('Homepage.html')

@app.route('/<info>')
def information(info):
    filtered_data = df[df["Acc. #"] == info].to_html()
    return f"<div>{filtered_data}</div>"
if __name__ != '__main__':
    pass
else:
    app.run()

from flask import Flask, render_template, make_response
import os
import json

HOST = os.getenv("HOST") or "0.0.0.0"
PORT = os.getenv("PORT") or 8080
app = Flask(__name__)

@app.route("/")
def main():
    with open("data.json", "r") as data:
        data = json.load(data)
        report_data = data["laporan"]
        del data["laporan"]

        return render_template("index.j2",  report_data=report_data, data=data)

@app.route("/text")
def to_text():
    with open("data.json", "r") as report_data:
        result = ""
        report_data = json.load(report_data)["laporan"]

        for data in report_data:
            result += f"{data['tanggal']}<br/>"

            if data["libur"]:
                result += "Libur"
                continue
            
            result += "<b>Kegiatan:</b><br/>"
            for kegiatan in data["deskripsi"]["kegiatan"]:
                result += f"&ensp;&ensp;o {kegiatan}<br/>"
            
            result += "<b>Hasil Kegiatan:</b><br/>"
            for hasil in data["deskripsi"]["hasil"]:
                result += f"&ensp;&ensp;o {hasil}<br/>"
            
            result += "<b>Pengalaman Belajar (softskill):</b><br/>"
            for softskill in data["deskripsi"]["pengalaman"]["softskill"]:
                result += f"&ensp;&ensp;o {softskill}<br/>"
            
            result += "<b>Pengalaman Belajar (hardskill):</b><br/>"
            for hardskill in data["deskripsi"]["pengalaman"]["hardskill"]:
                result += f"&ensp;&ensp;o {hardskill}<br/>"
            
            result += "<b>Dokumentasi:</b><br/>"
            for bukti in data["bukti"]:
                result += "&ensp;&ensp;<img src='static/{}' width='50%'><br/>".format(bukti)
            result += "<br/><br/><br/>"
        
        response = make_response(result, 200)
        response.mimetype = "text/html"
        return response

if __name__ == "__main__":
    if not os.path.isdir("static"):
        os.mkdir("static")

    app.run(host=HOST, port=PORT, debug=True)
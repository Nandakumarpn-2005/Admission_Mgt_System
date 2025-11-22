from flask import Flask, request, render_template, redirect, url_for, flash, Response
import pymysql
import random
from PIL import Image
import io
import re
import pytesseract
import os
from werkzeug.utils import secure_filename
from datetime import datetime
import traceback

app = Flask(__name__)
app.secret_key = "supersecretkey"

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\nanda\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
TESSERACT_CONFIG = "--psm 6"

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="Nandakumarpn@!",
    database="student"
)
mycursor = mydb.cursor()

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def save_file(field_name):
    """Saves an uploaded file and returns its relative static path."""
    file = request.files.get(field_name)
    if file and file.filename:
        filename = secure_filename(f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}")
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)
        # ✅ Return relative path for static access
        return f"uploads/{filename}"
    # ✅ Default placeholder image if not uploaded
    return "images/default_photo.png"


# OCR Patterns
UTR_PATTERNS = [
    r"UTR[:\s\-]*([0-9]{8,})",
    r"UPI\s*Ref\s*No[:\s\-]*([0-9]{8,20})",
    r"UPI\s*transaction\s*ID[:\s\-]*([0-9]{8,20})",
    r"Txn\s*Ref[:\s\-]*([0-9A-Z]{8,})",
    r"Google\s*transaction\s*ID[:\s\-]*([A-Za-z0-9]{6,30})"
]


def find_utr(text):
    for pat in UTR_PATTERNS:
        match = re.search(pat, text, re.IGNORECASE)
        if match:
            return match.group(1)
    return "Not Found"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/courses')
def courses():
    return render_template('courses.html')


@app.route('/regestration')
def regestration():
    return render_template('regestration.html')


@app.route('/inter')
def inter():
    return render_template('inter.html')


@app.route('/applicaton')
def applicaton():
    return render_template('applicaton.html')


@app.route('/submit_form', methods=['POST'])
def submit_form():
    full_name = request.form.get('full_name')
    Regester = request.form.get('Regester')
    course_id = request.form.get('course_id')
    Semester = request.form.get('Semester')
    phone = request.form.get('phone')
    photo = request.files.get('photo')

    if not photo:
        return "❌ No image uploaded."

    photo_data = photo.read()

    try:
        image = Image.open(io.BytesIO(photo_data))
        image = image.convert("L")
        text = pytesseract.image_to_string(image, config=TESSERACT_CONFIG)
        print("\n========== OCR OUTPUT ==========\n", text)
    except Exception as e:
        return f"❌ OCR processing failed: {e}"

    ocr_utr = find_utr(text)
    print(f"OCR Extracted UTR → {ocr_utr}")

    if ocr_utr == "Not Found":
        return "❌ Could not detect any UTR ID from the uploaded image."

    random_code = str(random.randint(100000, 999999))

    sql = """
        INSERT INTO admission 
        (full_name, Regester, course_id, Semester, phone, transaction_id, photo, random_code)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    val = (full_name, Regester, course_id, Semester, phone, ocr_utr, photo_data, random_code)
    mycursor.execute(sql, val)
    mydb.commit()

    return render_template('app.html', txn_id=ocr_utr, password=random_code)


@app.route("/submit", methods=["POST"])
def submit():
    try:
        user_id = request.form.get("user_id")
        semester = request.form.get("semester")
        course = request.form.get("course")
        date = request.form.get("date")
        student_name = request.form.get("student_name")
        father_name = request.form.get("father_name")
        father_occ = request.form.get("father_occ")
        mother_name = request.form.get("mother_name")
        mother_occ = request.form.get("mother_occ")
        address = request.form.get("address")
        bank_name = request.form.get("bank_name")
        ifsc = request.form.get("ifsc")
        acc_no = request.form.get("acc_no")
        scholarship = request.form.get("scholarship")
        mobile1 = request.form.get("mobile1")
        mobile2 = request.form.get("mobile2")
        religion = request.form.get("religion")
        caste = request.form.get("caste")
        category = request.form.get("category")
        income = request.form.get("income")
        sslc_reg = request.form.get("sslc_reg")
        caste_income_no = request.form.get("caste_income_no")
        aadhaar = request.form.get("aadhaar")
        email = request.form.get("email")

        # 📸 Save uploaded files dynamically
        photo_path = save_file("photo")
        bank_proof_path = save_file("bank_proof")
        ssp_image_path = save_file("ssp_image")
        caste_income_file_path = save_file("caste_income_file")
        aadhaar_file_path = save_file("aadhaar_file")

        sql = """INSERT INTO student_details (
            user_id,semester, course, date, student_name, father_name, father_occ,
            mother_name, mother_occ, address, bank_name, ifsc, acc_no, scholarship,
            mobile1, mobile2, religion, caste, category, income, sslc_reg,
            caste_income_no, aadhaar, email, photo_path, bank_proof_path,
            ssp_image_path, caste_income_file_path, aadhaar_file_path
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        val = (
            user_id, semester, course, date, student_name, father_name, father_occ,
            mother_name, mother_occ, address, bank_name, ifsc, acc_no, scholarship,
            mobile1, mobile2, religion, caste, category, income, sslc_reg,
            caste_income_no, aadhaar, email, photo_path, bank_proof_path,
            ssp_image_path, caste_income_file_path, aadhaar_file_path
        )

        mycursor.execute(sql, val)
        mydb.commit()

        # ✅ Pass dynamic image path to success page
        return render_template('admission_sucess.html',
                               student_name=student_name,
                               student_semester=semester,
                               student_course=course,
                               student_mobile=mobile1,
                               student_email=email,
                               photo_path=photo_path)

    except Exception as e:
        mydb.rollback()
        print("\n================= SQL ERROR TRACE =================")
        traceback.print_exc()
        print("===================================================")
        flash(f"❌ Failed to submit the application. {e}", "error")
        return redirect(url_for("regestration"))


@app.route('/show/<txn_id>')
def show_image(txn_id):
    sql = "SELECT photo FROM admission WHERE transaction_id=%s"
    mycursor.execute(sql, (txn_id,))
    row = mycursor.fetchone()
    if row and row[0]:
        return Response(row[0], mimetype='image/jpeg')
    return "❌ No image found."


@app.route('/verify', methods=['POST'])
def verify():
    transaction_id = request.form.get('transaction_id')
    unique_code = request.form.get('unique_code')

    sql = "SELECT * FROM admission WHERE transaction_id=%s AND random_code=%s"
    mycursor.execute(sql, (transaction_id, unique_code))
    record = mycursor.fetchone()

    if record:
        return render_template('inter.html', message="✅ Verification successful!", msg_type="success")
    else:
        return render_template('inter.html', message="❌ Invalid Transaction ID or Unique Code.", msg_type="error")


if __name__ == '__main__':
    app.run(debug=True)

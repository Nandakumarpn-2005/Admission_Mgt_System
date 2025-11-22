# 🎓 Student Admission & Verification System (Flask + MySQL + OCR)

This project is a complete **Student Admission Web Application** built with Flask.  
It includes:

- Student registration  
- Courses listing page  
- OCR-based fee payment extraction  
- Dynamic document & photo uploads  
- MySQL database storage  
- Student verification  
- Dynamic image display from `static/uploads/`  

Uploaded images are stored uniquely inside **`static/uploads/`** and displayed on the success page beside the student details.

---

# 🖼️ Screenshots (With Working Alternative Images)

Below, every screenshot is centered and fixed to **100×100** size.  
If your local `img/...` files are missing, you can still use the alternative placeholder links.

---

## 1️⃣ Home Page

<p align="center">
  <img src="img/home.jpg" alt="Home Page" width="300" height="300">
</p>
This is the landing page.  
Navigation includes:

- Courses Page  
- Registration Form  
- Payment OCR Page  
- Verification Page  

---

## 2️⃣ Courses Page

<p align="center">
  <img src="img/course.jpg" alt="Courses Page" width="300" height="300">
</p>

This page lists all available courses, their codes, and titles.  
It helps students choose the correct course before filling the registration form.

Accessed through the `/courses` route.

---

## 3️⃣ Registration Page

<p align="center">
  <img src="img/reg.jpg" alt="Registration Page" width="300" height="300">
</p>

Students provide:

- Personal details  
- Parent details  
- Academic info  
- Bank info  
- Upload documents (Photo, Aadhaar, Bank Proof, SSP Screenshot, Caste/Income Certificate)  

Student photo is saved into `static/uploads/`.

---

## 4️⃣ Payment Submission Page (OCR)

<p align="center">
  <img src="img/regss.jpg" alt="OCR Payment Page" width="300" height="300">
</p>

This page accepts a student's **fee payment receipt**.  
The backend uses OCR to extract:

- UTR number  
- Transaction reference ID  

The system also generates a **unique 6-digit code** for verification.

---

## 5️⃣ Admission Success Page

<p align="center">
  <img src="img/success_page.png" alt="Admission Success Page" width="300" height="300">
</p>

This page shows:

- Student name (uppercase)  
- Course  
- Semester  
- Mobile  
- Email  
- **Student photo displayed dynamically from `static/uploads/`**  

The photo appears nicely aligned beside the student details.

---

## 6️⃣ Verification Page

<p align="center">
  <img src="img/verification_page.png" alt="Verification Page" width="100" height="100">
</p>

<p align="center">
  <em>Alternative if missing → https://via.placeholder.com/900x500?text=Verification+Page+Screenshot</em>
</p>

Students verify their admission using:

- Transaction ID  
- Unique Code  

If both match database records → **“Verification Successful”**.  

If not → appropriate **error message** is displayed.

---

# 📁 Folder Structure

```text
project_root/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation (this file)
│
├── static/
│   ├── css/
│   │   └── styles.css      # Optional custom styles
│   └── uploads/            # All uploaded student images & documents
│
├── templates/
│   ├── index.html          # Home page
│   ├── courses.html        # Courses listing page
│   ├── register.html       # Student registration form
│   ├── ocr_payment.html    # Payment submission & OCR page
│   ├── success.html        # Admission success page (shows student photo)
│   └── verify.html         # Verification page
│
└── database/
    └── schema.sql          # MySQL table structure (students, payments, etc.)

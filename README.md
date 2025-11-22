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

## 5️⃣ Admission  Page

<p align="center">
  <img src="img/adim.jpg" alt="Admission Success Page" width="300" height="300">
</p>
<p align="center">
  <img src="img/adim2.jpg" alt="Admission Success Page" width="300" height="300">
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

7️⃣ Admission Success Form
<p align="center"> <img src="img/sucess.jpg" alt="Admission Success Form" width="300" height="300"> </p> <p align="center"> <em>Alternative if missing → https://via.placeholder.com/900x500?text=Admission+Success+Form+Screenshot</em> </p>

The Admission Success Form confirms that the student registration has been successfully completed.
It highlights the student details clearly in a modern green-themed card layout.

✔ Information Displayed

-Student Name

-Semester

-Course

-Mobile Number

-Email ID

-Uploaded Student Photograph
---


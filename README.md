# 🎓 Student Admission & Verification System (Flask + MySQL + OCR)

This project is a complete **Student Admission Web Application** built with Flask.  
It includes:

- Student registration  
- Courses listing page  
- OCR-based fee payment extraction  
- Dynamic document & photo uploads  
- MySQL database storage  
- Student verification  
- Dynamic image display from static/uploads/  

Uploaded images are stored uniquely inside **static/uploads/** and displayed on the success page beside the student details.

---

# 🖼️ Screenshots (With Working Alternative Images)

Below, every screenshot already includes a **fallback alternative image URL** so your README works even if your own images are not added yet.

---

## 1️⃣ Home Page

![Home Page](img/home.png)
*(Alternative if missing → https://via.placeholder.com/900x500?text=Home+Page+Screenshot)*

This is the landing page.  
Navigation includes:

- Courses Page  
- Registration Form  
- Payment OCR Page  
- Verification Page  

---

## 2️⃣ Courses Page

![Courses Page](img/course.jpg)
*(Alternative if missing → https://via.placeholder.com/900x500?text=Courses+Page+Screenshot)*

This page lists all available courses, their codes, and titles.  
It helps students choose the correct course before filling the registration form.

Accessed through the `/courses` route.

---

## 3️⃣ Registration Page

![Registration Page](img/registration_page.png)
*(Alternative if missing → https://via.placeholder.com/900x500?text=Registration+Page+Screenshot)*

Students provide:

- Personal details  
- Parent details  
- Academic info  
- Bank info  
- Upload documents (Photo, Aadhaar, Bank Proof, SSP Screenshot, Caste/Income Certificate)  

Student photo is saved into `static/uploads/`.

---

## 4️⃣ Payment Submission Page (OCR)

![OCR Page](img/ocr_page.png)
*(Alternative if missing → https://via.placeholder.com/900x500?text=OCR+Payment+Page+Screenshot)*

This page accepts a student's **fee payment receipt**.  
The backend uses OCR to extract:

- UTR number  
- Transaction reference ID  

The system also generates a **unique 6-digit code** for verification.

---

## 5️⃣ Admission Success Page

![Success Page](img/success_page.png)
*(Alternative if missing → https://via.placeholder.com/900x500?text=Success+Page+Screenshot)*

This page shows:

- Student name (uppercase)  
- Course  
- Semester  
- Mobile  
- Email  
- **Student photo displayed dynamically from static/uploads/**  

The photo appears nicely aligned beside the student details.

---

## 6️⃣ Verification Page

![Verification Page](img/verification_page.png)
*(Alternative if missing → https://via.placeholder.com/900x500?text=Verification+Page+Screenshot)*

Students verify their admission using:

- Transaction ID  
- Unique Code  

If both match database records → “Verification Successful”.

If not → error message.

---

# 📁 Folder Structure


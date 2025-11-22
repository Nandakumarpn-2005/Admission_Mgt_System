# 🎓 Student Admission & Verification System (Flask + MySQL + OCR)

This project is a complete **Student Admission Web Application** built with Flask.  
It supports:

- Student registration  
- Course listing page  
- Document & photo uploads  
- OCR extraction of UTR from payment receipts  
- MySQL database storage  
- Student verification  
- Dynamic image display from static/uploads/  

Uploaded images are saved uniquely inside **static/uploads**, and the same image appears on the success page beside the student details.

---

# 🖼️ Screenshots (With Explanation)

---

## 1️⃣ Home Page
*(Add image file: `static/images/screenshots/home_page.png`)*

This is the main landing page.  
Provides navigation to:

- Course list  
- Registration form  
- Payment submission page  
- Verification page  

---

## 2️⃣ Courses Page
*(Add image file: `static/images/screenshots/courses_page.png`)*

This page displays the **list of available courses** offered by the institution.

It is accessed using the `/courses` route.

### What the Courses Page Contains:
- List of degree and diploma programs  
- Course codes and titles  
- Clean green-themed UI matching the rest of the project  

This page helps students choose the correct course before filling the registration form.

---

## 3️⃣ Registration Page
*(Add image file: `static/images/screenshots/registration_page.png`)*

Here students provide:

- Personal details  
- Parent information  
- Academic details  
- Bank details  
- Document uploads (photo, Aadhaar, bank proof, caste/income, SSP screenshot)  

Uploaded photo is saved inside `static/uploads/`.

---

## 4️⃣ Payment Submission Page (OCR)
*(Add image file: `static/images/screenshots/ocr_page.png`)*

This page accepts the payment screenshot.  
The backend uses **Tesseract OCR** to extract:

- UTR ID  
- Transaction Reference Number  

The system then generates a unique 6-digit code and stores both in the database.

---

## 5️⃣ Admission Success Page
*(Add image file: `static/images/screenshots/success_page.png`)*

Shows:

- Student name (**uppercase**)  
- Semester  
- Course  
- Email  
- Mobile  
- **Student photo displayed from static/uploads**  

Photo appears in a rectangular box beside the details.

---

## 6️⃣ Verification Page
*(Add image file: `static/images/screenshots/verification_page.png`)*

Students enter:

- Transaction ID  
- Unique Code  

If both match an entry in the database → verification success.  
Else → error message.

---

# 📁 Folder Structure


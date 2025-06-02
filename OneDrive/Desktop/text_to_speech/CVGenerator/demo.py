from tkinter import *
from fpdf import FPDF
from tkinter import messagebox
import pyqrcode

class PDFCV(FPDF):
    def header(self):
        self.image("mywebsite.png", 10, 8, 33, title="Portfolio Site")

    def footer(self):
        pass

    def generate_cv(self,name,email,phone_number,address,skills,work_experience, education, about_me):
        self.add_page()
        self.ln(20)

        #Displaying name
        self.set_font("Helvetica", "B", size = 26)
        self.cell(0,10,name, new_x="LMARGIN", new_y="NEXT", align="C")

        #Displaying contact information
        self.set_font("Helvetica", "B", size = 15)
        self.cell(0,10,"Contact Information", new_x="LMARGIN", new_y="NEXT", align="L")
        
        self.set_font("Helvetica", size = 15)
        self.cell(0,10,"Email:{}".format(email), new_x="LMARGIN", new_y="NEXT")
        self.cell(0,10, "Phone Number:{}".format(phone_number), new_x="LMARGIN", new_y="NEXT")
        self.cell(0,10, "Address:{}".format(address), new_x="LMARGIN", new_y="NEXT")

        #Displaying skills
        self.ln(10)
        self.set_font("Helvetica", "B", size = 15)
        self.cell(0,10,"Skills", new_x="LMARGIN", new_y="NEXT", align="L")

        self.set_font("Helvetica", size = 15)
        for skill in skills:
            self.cell(0,5, "-{}".format(skill), new_x="LMARGIN", new_y="NEXT")

        #Displaying experience
        self.ln(10)
        self.set_font("Helvetica", "B", size = 15)
        self.cell(0, 10, "Work Experience", new_x="LMARGIN", new_y="NEXT")

        self.set_font("Helvetica", size = 15)
        for exp in work_experience:
            self.cell(0,5,"-{}:{}".format(exp["title"], exp["description"]), new_x="LMARGIN", new_y="NEXT")

        #Displaying education
        self.ln(10)
        self.set_font("Helvetica", "B", size = 15)
        self.cell(0, 10, "Education", new_x="LMARGIN", new_y="NEXT")

        self.set_font("Helvetica", size = 15)
        for edu in education:
            self.cell(0,5,"-{}:{}".format(edu["degree"],edu["university"]), new_x="LMARGIN", new_y="NEXT")

        #displaying about me
        self.ln(10)
        self.set_font("Helvetica", "B", size = 15)
        self.cell(0, 10, "About Me", new_x="LMARGIN", new_y="NEXT")

        self.set_font("Helvetica", size = 15)
        self.cell(0,5,"{}".format(about_me), new_x="LMARGIN", new_y="NEXT")

def generate_cv():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    phone_number = entry_phone.get().strip()
    address = entry_address.get().strip()
    website = entry_website.get().strip()

    work_experience = []
    education = []

    skills = [skill.strip() for skill in entry_skills.get("1.0", END).strip().split('\n') if skill.strip()]

    experience_lines = entry_experience.get("1.0", END).strip().split('\n')
    for line in experience_lines:
        if line.strip():
            try:
                title, description = line.split(':')
                work_experience.append({'title': title.strip(), 'description': description.strip()})
            except ValueError:
                messagebox.showerror("Error", f"Invalid job description format: {line}")
                return

    education_lines = entry_education.get("1.0", END).strip().split('\n')
    for line in education_lines:
        if line.strip():
            try:
                degree, university = line.split(':', 1)
                education.append({'degree':degree.strip(), 'university':university.strip()})
            except ValueError:
                messagebox.showerror("Error", f"Invalid education format: {line}")
                return
        

    about_me = entry_about_me.get("1.0", END).strip()

    #creating qr code
    qrcode = pyqrcode.create(website)
    qrcode.png("mywebsite.png", scale=6)

    if not name or not email or not phone_number or not address or not skills or not work_experience or not website or not about_me or not education_lines:
        messagebox.showerror("Error","Please fill in all the details")
        return
    

    cv = PDFCV()
    cv.generate_cv(name,email,phone_number,address,skills,work_experience, education, about_me)
    cv.output("generated_cv.pdf")
    messagebox.showinfo("Success", "Your CV has been generated successfully!")

window = Tk()

window.title("CV Generator")

Label(window, text="Name: ").pack()
entry_name = Entry(window)
entry_name.pack()

Label(window, text="Email: ").pack()
entry_email = Entry(window)
entry_email.pack()

Label(window, text="Phone: ").pack()
entry_phone = Entry(window)
entry_phone.pack()

Label(window, text="Address: ").pack()
entry_address = Entry(window)
entry_address.pack()

Label(window, text="Website: ").pack()
entry_website = Entry(window)
entry_website.pack()

Label(window, text="Skills(Enter one skill per line)").pack()
entry_skills = Text(window, height=5)
entry_skills.pack()

Label(window, text="Education(One per line in format 'Degree':'University')").pack()
entry_education = Text(window, height=5)
entry_education.pack()

Label(window, text="Experience(Enter one per line in format 'Job title':'Description')").pack()
entry_experience = Text(window, height=5)
entry_experience.pack()

Label(window, text="About Me").pack()
entry_about_me = Text(window, height=5)
entry_about_me.pack()

Button(window, text="Generate CV", command=generate_cv).pack()

window.mainloop()
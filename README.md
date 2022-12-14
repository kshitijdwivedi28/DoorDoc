
# Optum Stratethon: E-Track Season 4

DoorDoc - Recommends medical specialists. With the help of computer vision, it makes it easier for people who lack in-depth knowledge of medical domain. Additionally, it offers in-depth insights on data that is tailored for medical establishments. 





# Problem Statement

The two main actors in the medical industry are those who manage medical facilities and the patients who use them. In order to use technology to improve healthcare somewhat, we typically offer solutions at both ends.

- **For a patient with no medical knowledge:** Our system uses computer vision to locate the precise spot where the user is experiencing pain or discomfort by pointing their finger there. In order to better identify the source of the discomfort, we also pose a few questions that are tailored to the location the user has indicated is troublesome. Then, using a machine learning algorithm called decision tree classifier, we suggest potential medical conditions that our user may be experiencing. Along with that we predict the best suited medical specialist for the disease diagnosed by the symptoms incurred.
- **For bridging communication gap, and reducing wait time:** We offer a document or report that includes the Basic Details, Symptoms, Disease Predicted, and any other optional message our user wants to share with the Doctor prior (if selected) as well as to the user.
- **For medical establishments:** We analyse the data using the PowerBI tool and give the administrator several crucial insights, such as the number of reviews per month, the specialisation they are known for, sentiment analysis of the provided feedback (using Natural Language Processing), the average rating, the doctor who is most highly rated, the procedure they are best at, etc.

# Key Value Proposition
- DoorDoc places a high priority on providing people with explicit medical care.
- For the user's specific affected area, DoorDoc provides the precise medical specialist.
- Computer vision enables precise identification of the user's pain zone.
- Simplicity is favoured as the user just needs to point at the area of discomfort.
- Waiting time for patients is drastically reduced for consultation by General Physicians / Doctors and at Hospitals OPD's.
- The communication gap between doctors and patients is filled through DoorDoc.
- Ready Home Preparedness and Bilingual Support for the users.
- Utilizing data analysis provided by DoorDoc, simple audience targeting and clever marketing approach are possible.

# Target Customer
Everyone can find something on our website. 

- We notably target illiterate persons who have trouble locating their particular site of care and, consequently, the medical specialist who will be treating them.
- People with limited knowledge who are not familiar with medical terminology
- Doctors - For making the most of their scheduled appointments.
- Medical Organizations: To break up the chain of doctors and physicians and so lessen corruption in the future.
- Those who have difficulty in reading English. (Hindi as well as English language help is available on our website)
- Incharge of any type of medical facility can evaluate their presence of market using our Data Analysis tool. 

# Proposed Solution

Our software solution has the following components:

- **Computer Vision**\
    Our website gives the user the option to open his/her webcam and point their index finger at the area where there is discomfort. Then, with the help of computer vision, we will be identifying the pointed body part, thus deriving meaningful information through visual inputs.

- **Machine Learning**
    - **Disease Prediction**
    After gathering the symptoms from the user, the symptoms are matched with the trained model in order to get the accurate disease prediction. For training the dataset, we used Decision Tree Classifier. 
    - **Medical Practitioner Recommendation**
    In order to get the correct Medical Practitioner, the diseases are mapped to their respective Medical Practitioners, thus solving the problem of 'Which doctor to consult?'

- **Report Generation**\
    Our website also has the feature of generating report after filling the form to make an appointment with the doctor. 
    
    The generated report has the following content:\
      1. Name\
      2. Email\
      3. Contact No.\
      4. Date\
      5. Department\
      6. Doctor\
      7. Message\
      8. Symptoms 
  
    This will help the user as it will give prior information regarding the disease as well as for the doctor since the generated report will reduce consultancy time and will be time saving solution.

- **Data Analysis**\
    With the help of PowerBI we have built an interactive dashboard for people who are in control of any medical facility. Our dashboard encompasses features like - number of reviews per month, the specialisation they are known for, sentiment analysis of the provided feedback (using Natural Language Processing), the average rating, the doctor who is most highly rated, the procedure they are best at, etc.
    This will help them to evaluate their presence in market, and also to incorporate clever marketing techniques. 

- **Language**\
   As, India is a diversified country and a home of various cultures and languages.\
   Our website is bilingual, which supports both English and Hindi.

# Technology Stack 
#### Frontend – 
 - HTML5 for the structure
 - CSS3 for designing
 - JavaScript for interactivity.
 - Bootstrap Framework is used to enhance User Interface.
 - PowerBI - interactive dashboard
#### Backend –
- Python Language is used as it provided large library support
- Framework – Django is used for Integration with frontend requests.
- OpenCV captures the user video.
- Mediapipe module helps in the identification of the specific body part.
- Django_crispy_forms is used for user authentication and login database
- Fpdf module is used for PDF processing.
- Pandas, numpy, and sklearn is used for handling CSV files and data analysis.

# Implementation Screenshots
![1](https://user-images.githubusercontent.com/59134476/198878287-492a0493-0c8e-4de8-bf58-e3a6ccef4001.png)
![2](https://user-images.githubusercontent.com/59134476/198878332-ea64a3b8-cdc0-4a04-83c6-d02f773aca84.png)
![3](https://user-images.githubusercontent.com/59134476/198878334-24639cf4-b4fa-437b-be3a-5eb89f33c4af.png)
![4](https://user-images.githubusercontent.com/59134476/198878336-8eaaa1a2-f336-4291-aa72-fe8661378944.png)
![5](https://user-images.githubusercontent.com/59134476/198878338-ea84e00b-69d5-4291-aa96-5d8103cc6247.png)
![6](https://user-images.githubusercontent.com/59134476/198878339-d2dc887e-ef5c-4437-ac12-7676510ac87c.png)
![7](https://user-images.githubusercontent.com/59134476/198878320-f803f221-1a00-4b47-8365-a15c8cc12817.png)
![8](https://user-images.githubusercontent.com/59134476/198878321-f77a71f5-a95e-4e99-af1d-979301fbaaf9.png)
![9](https://user-images.githubusercontent.com/59134476/198878323-42ca34ed-0ef7-4f04-9637-6d6975e2bff8.png)
![10](https://user-images.githubusercontent.com/59134476/198878324-100b378d-c1bc-4f79-8b97-bdc6c2038ba5.png)
![11](https://user-images.githubusercontent.com/59134476/198878325-e7619a5f-f24c-456f-a13a-708fa5accf94.png)
![12](https://user-images.githubusercontent.com/59134476/198878326-4f531d86-b85b-46ae-a560-bf7b3535c58c.png)
![13](https://user-images.githubusercontent.com/59134476/198878327-8fd69b12-08af-4d17-bf2f-98e81914c5b0.png)
![14](https://user-images.githubusercontent.com/59134476/198878329-644b3e72-d081-4c4f-94d5-eac032358764.png)
![15](https://user-images.githubusercontent.com/59134476/198878330-4da0041b-34bf-45a2-8cf7-8b3b39d93232.png)
![powerbi](https://user-images.githubusercontent.com/59134476/198878331-cd50d122-6fdd-49d7-a342-fbe93f0420d9.png)



# Video Link 
## Demonstration of the project

# Step by Step Procedure to run the project on your Local Machine

 1. Download the project through the below mentioned link or as a ZIP file from GitHub. "GIVE LINK HERE"
 2.	Extract the Downloaded ZIP to a folder.
 3.	Download and Install Python on your platform through this link https://www.python.org/downloads/
 4.	Switch on to your favourite Integrated Development Environment (IDE) as the project is platform independent (Windows / Linux / MacOSX) as well as IDE independent (PyCharm, VS Code). We have preferred Visual Studio Code (VS Code) as our IDE.
 5.	Download and Installation link for Visual Studio Code – https://code.visualstudio.com/download
 6.	Open VS Code on your Platform and Navigate to File Button at the Top Corner
 7.	Click Open Folder, browse to your extracted folder and select that folder.
 8.	Navigate to required.txt file from the left pane in the folder and install the mentioned modules.
 9.	To install a specific module. For example – Django. Follow the below steps –

     I.   In VS Code, Press Ctrl+` (for windows) to open the terminal\
     II.  Type the following command pip install django --user\
     III. VS Code will automatically install the Django and its subsidiary modules.\
     IV.  Once done, you will see a successful installation message\
     V.   Similarly, install other mentioned modules following I, II, III and IV steps

 10.	Enter the following commands to migrate Schema - python manage.py makemigrations
 11.    Now, enter command - python manage.py migrate
 11.    Enter the following command in the terminal – python manage.py runserver
 12.	If you encounter with an error, file not found. Right Click on the manage.py file in the left side bar, click on copy path, and replace manage.py with the path in the above command.
 13.	Now, you will see Starting Development Server stating the link of the website.
 14. For the dashboard, download and install PowerBI - iska dekh lena yaar ek baar, ki tum link alag se share kr rhe ho ya kya?

 # Thank you :)
## TEAM NAME
### Ritik, Tanmay, Kshitij


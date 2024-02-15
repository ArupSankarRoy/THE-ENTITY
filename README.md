# The Entity - A Revolutionary Hybrid Video Analysis Computer Vision Web Application

![Screenshot 2024-02-15 133341](https://github.com/ArupSankarRoy/THE-ENTITY/assets/115450599/00cd2ebd-8e93-4358-b300-b042eab7df41)

## Overview

Welcome to The Entity, a cutting-edge hybrid video analysis computer vision web application designed to redefine real-time detection capabilities. This project is divided into three distinctive phases, each contributing to the application's prowess in analyzing video frames instantly.

### Login and Registration Section:
-   **USER LOGIN:**
    ![Screenshot 2024-02-15 133221](https://github.com/ArupSankarRoy/THE-ENTITY/assets/115450599/69610d2c-2d20-4c8b-99e0-05dc0146d0e7)

-   **USER REGISTRATION:**
    ![Screenshot 2024-02-15 133243](https://github.com/ArupSankarRoy/THE-ENTITY/assets/115450599/a202c0fe-79c2-45e8-80f5-b729283d9e98)

### Key Features

1. **Real-Time Object Identification and Monitoring**
   - Phase 1 focuses on immediate identification of weapons, military vehicles, and public anomalies in real-time, providing analysis per video frame rather than waiting for post-video completion.
   - **PHASE 1 OUTPUT:**
     ![Screenshot 2024-02-15 133559](https://github.com/ArupSankarRoy/THE-ENTITY/assets/115450599/857db05c-3e4a-46cd-9d17-2f4cd6ca6f69)
     

2. **Detection , Segmentation , Heatmap Visualization**
   - In Phase 2, the application excels in detecting, segmenting, and presenting heatmaps derived from images, offering a deeper layer of insight and understanding.
   - **PHASE 2 PAGE:**
     ![Screenshot 2024-02-15 133715](https://github.com/ArupSankarRoy/THE-ENTITY/assets/115450599/b6c6f9f1-2949-4c66-b0d0-e820685fbe88)
   - **PHASE 2 OUTPUT:**
      ![Screenshot 2024-02-15 134007](https://github.com/ArupSankarRoy/THE-ENTITY/assets/115450599/c84b57ee-a0fe-45f4-8b49-1495b83fc6bd)


3. **Webcam-Based Anomaly Detection**
   - Phase 3 introduces a sleek black theme, enhancing the aesthetics while enabling webcam-based detection of anomalous objects. The flexibility to use external webcams enhances the overall user experience.
   - **PHASE 3 PAGE:**
     ![Screenshot 2024-02-15 134044](https://github.com/ArupSankarRoy/THE-ENTITY/assets/115450599/4a41a7ca-e5f2-4d16-83b6-423510b8bda3)
   - **PHASE 3 OUTPUTS:**
     ![Screenshot 2024-02-15 134122](https://github.com/ArupSankarRoy/THE-ENTITY/assets/115450599/6ecd13dd-0d52-4263-a5d5-222885bb9724)
     ![Screenshot 2024-02-15 134154](https://github.com/ArupSankarRoy/THE-ENTITY/assets/115450599/5ffeb4ea-7dd0-4a73-ae1c-133c1f28b7be)



4. **Customized Training Function (Under Development)**
   - The ongoing development of a customized training function holds immense potential for refining the application's capabilities, allowing users to tailor the system to specific needs.

### User Interface

- The application boasts a meticulously designed user interface for maximum responsiveness, ensuring a seamless and efficient user experience.

## Future Developments

- **ROBOFLOW'S SUPERVISION INTEGRATION FOR OBJECT TRACKING:** Future updates will include the integration of supervision library to enhance the application's accuracy and efficiency in detecting and tracking objects.

- **CHATBOT INTEGRATION:** To foster enhanced user interaction, a chatbot feature is in the pipeline, providing users with informative and interactive assistance.

- **REALTIME PREDICTION GRAPH:** A real-time prediction graph will be introduced to offer users valuable insights, further solidifying The Entity's position as a leader in real-time video analysis and computer vision.

- **CUSTOMIZE TRAINING PAGE:** A seperate html page will be added for seeing the training progress live.

## Getting Started

To experience the cutting-edge capabilities of The Entity, follow the steps below:

1. CREATE A DATABASE :
```
-- DATABASE CODE:
-- USE XAMPP MUST

USE `user-system`;

CREATE TABLE `user` (
  `userid` int(11) AUTO_INCREMENT PRIMARY KEY,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `user` (`name`, `email`, `password`) VALUES
('John Smith', 'smith@webdamn.com', '123'),
('Adam William', 'adam@webdamn.com', '123');

```
2. CLONE THE DIRECTORY AND MOVE TO THE 'THE-ENTITY' FOLDER(USING cd folder_name).
-  **CODE:**
```
$ git clone https://github.com/ArupSankarRoy/THE-ENTITY.git
$ cd THE-ENTITY
$ pip install -r requirements.txt
```
3. CHANGE THE NAME AND PORT NUMBER ACCORDING TO YOUR DATABASE IN 'app.py' LOGIN SECTION.
4. **USE CHROME BROWSER AND BE CAUTIOUS THE GPU MUST BE ON BEFORE RUNNING THIS APPLICATION FOR BETTER PERFORMANCE.**
5. RUN BELOW TO 1ST ACTIVATE THE SITE
```
$ python launcher.py
```
6. IN CHROME TYPE `http://127.0.0.1:5000/` TO REDIRECT THE SITE.

## Stay Tuned

As The Entity continues to evolve, it aims to set new standards in real-time video analysis and computer vision. Stay tuned for regular updates, exciting features, and improvements.

Your feedback is crucial to our development process. Feel free to reach out, report issues, and share your suggestions as we work together to shape the future of video analysis and computer vision.

Happy exploring with The Entity!

- [**DEMO VIDEO**](https://drive.google.com/file/d/1bK_SFv0EmgxaIwiEx5I0Pa9NnVtSzHPB/view?usp=sharing)


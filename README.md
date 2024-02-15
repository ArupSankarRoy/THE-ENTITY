# The Entity - Revolutionary Hybrid Video Analysis and Computer Vision Web Application
![Screenshot 2024-02-15 133341](https://github.com/ArupSankarRoy/THE-ENTITY/assets/115450599/00cd2ebd-8e93-4358-b300-b042eab7df41)

## Overview

Welcome to The Entity, a cutting-edge hybrid video analysis computer vision web application designed to redefine real-time detection capabilities. This project is divided into three distinctive phases, each contributing to the application's prowess in analyzing video frames instantly.

### Key Features

1. **Real-Time Object Identification and Monitoring**
   - Phase 1 focuses on immediate identification of weapons, military vehicles, and public anomalies in real-time, providing analysis per video frame rather than waiting for post-video completion.
   - **PHASE 1 OUTPUT:**
     ![Screenshot 2024-02-15 133559](https://github.com/ArupSankarRoy/THE-ENTITY/assets/115450599/857db05c-3e4a-46cd-9d17-2f4cd6ca6f69)
     

2. **Detection , Segmentation , Heatmap Visualization**
   - In Phase 2, the application excels in detecting, segmenting, and presenting heatmaps derived from images, offering a deeper layer of insight and understanding.
   - **PHASE 2 PAGE:**
     ![Screenshot 2024-02-15 133715](https://github.com/ArupSankarRoy/THE-ENTITY/assets/115450599/b6c6f9f1-2949-4c66-b0d0-e820685fbe88)


3. **Webcam-Based Anomaly Detection**
   - Phase 3 introduces a sleek black theme, enhancing the aesthetics while enabling webcam-based detection of anomalous objects. The flexibility to use external webcams enhances the overall user experience.

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

```
$ git clone https://github.com/ArupSankarRoy/THE-ENTITY.git
$ cd THE-ENTITY
$ pip install -r requirements.txt
```
AFTER FINISHING THE ABOVE STEPS CREATE A DATABASE AND CHANGE THE NAME AND PORT NUMBER OF YOUR DATABASE IN 'app.py' LOGIN SECTION.

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
**USE CHROME BROWSER AND BE CAUTIOUS THE GPU MUST BE ON BEFORE RUNNING THIS APPLICATION FOR BETTER PERFORMANCE**

## Stay Tuned

As The Entity continues to evolve, it aims to set new standards in real-time video analysis and computer vision. Stay tuned for regular updates, exciting features, and improvements.

Your feedback is crucial to our development process. Feel free to reach out, report issues, and share your suggestions as we work together to shape the future of video analysis and computer vision.

Happy exploring with The Entity!

# The Entity - Revolutionary Hybrid Video Analysis and Computer Vision Web Application

## Overview

Welcome to The Entity, a cutting-edge hybrid video analysis computer vision web application designed to redefine real-time detection capabilities. This project is divided into three distinctive phases, each contributing to the application's prowess in analyzing video frames instantly.

### Key Features

1. **Real-Time Object Identification**
   - Phase 1 focuses on immediate identification of weapons, military vehicles, and public anomalies in real-time, providing analysis per video frame rather than waiting for post-video completion.

2. **Heatmap Visualization**
   - In Phase 2, the application excels in detecting, segmenting, and presenting heatmaps derived from images, offering a deeper layer of insight and understanding.

3. **Webcam-Based Anomaly Detection**
   - Phase 3 introduces a sleek black theme, enhancing the aesthetics while enabling webcam-based detection of anomalous objects. The flexibility to use external webcams enhances the overall user experience.

4. **Customized Training Function (Under Development)**
   - The ongoing development of a customized training function holds immense potential for refining the application's capabilities, allowing users to tailor the system to specific needs.

### User Interface

- The application boasts a meticulously designed user interface for maximum responsiveness, ensuring a seamless and efficient user experience.

## Future Developments

- **Supervised Learning Integration:** Future updates will include the integration of supervised learning to enhance the application's accuracy and efficiency in detecting and analyzing objects.

- **Chatbot Integration:** To foster enhanced user interaction, a chatbot feature is in the pipeline, providing users with informative and interactive assistance.

- **Real-Time Prediction Graph:** A real-time prediction graph will be introduced to offer users valuable insights, further solidifying The Entity's position as a leader in real-time video analysis and computer vision.

## Getting Started

To experience the cutting-edge capabilities of The Entity, follow the steps below:

```
$ git clone https://github.com/ArupSankarRoy/THE-ENTITY.git
$ cd THE-ENTITY
$ pip install -r requirements.txt
```
AFTER FINISHING THE ABOVE STEPS CREATE A DATABASE AND CHANGE THE NAME AND PORT NUMBER OF YOUR DATABASE IN 'app.py' LOGIN SECTION.
DATABASE CODE:
```
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

## Stay Tuned

As The Entity continues to evolve, it aims to set new standards in real-time video analysis and computer vision. Stay tuned for regular updates, exciting features, and improvements.

Your feedback is crucial to our development process. Feel free to reach out, report issues, and share your suggestions as we work together to shape the future of video analysis and computer vision.

Happy exploring with The Entity!

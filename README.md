<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Webcam Face Detection</title>
</head>

<body>

    <h1>Webcam Face Detection using OpenCV and MediaPipe</h1>

    <h2>Overview</h2>

    <p>This Python script utilizes the OpenCV and MediaPipe libraries to perform real-time face detection through a webcam feed. The program captures frames from the webcam, detects faces in each frame using the MediaPipe Face Detection module, and overlays rectangles around the detected faces on the live video stream.</p>

    <h2>Prerequisites</h2>

    <pre><code>pip install opencv-python mediapipe</code></pre>

    <h2>Usage</h2>

    <ol>
        <li>**Clone the repository:**</li>
        <pre><code>git clone https://github.com/your-username/your-repo.git cd your-repo</code></pre>

        <li>**Run the script:**</li>
        <pre><code>python face_detection.py</code></pre>

        <li>**Press the 'Esc' key to exit the application.**</li>
    </ol>

    <h2>Description</h2>

    <ul>
        <li>The script initializes the webcam using OpenCV (<code>cv2.VideoCapture(0)</code>).</li>
        <li>It sets up the MediaPipe Face Detection module for face recognition.</li>
        <li>The script continuously captures frames from the webcam and processes them to detect faces.</li>
        <li>Detected faces are outlined with rectangles, and the processed frames are displayed in a window titled "Webcam Faces."</li>
        <li>Press the 'Esc' key to exit the application.</li>
    </ul>

    <h2>Dependencies</h2>

    <ul>
        <li>Python 3.x</li>
        <li>OpenCV (<code>cv2</code>)</li>
        <li>MediaPipe (<code>mediapipe</code>)</li>
    </ul>

    <h2>Acknowledgments</h2>

    <ul>
        <li><a href="https://github.com/opencv/opencv">OpenCV</a></li>
        <li><a href="https://github.com/google/mediapipe">MediaPipe</a></li>
    </ul>

    <h2>Notes</h2>

    <ul>
        <li>Make sure your webcam is properly connected and accessible.</li>
        <li>Adjustments to the code may be needed depending on your system's camera index or if there are issues with the installation of required libraries.</li>
    </ul>

    <p>Feel free to explore and modify the code according to your needs! If you encounter any issues or have suggestions for improvements, please open an <a href="https://github.com/your-username/your-repo/issues">issue</a> or submit a <a href="https://github.com/your-username/your-repo/pulls">pull request</a>. Happy coding!</p>

</body>

</html>

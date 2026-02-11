# Traffic Sign AI

I started this project thinking the model architecture was the most important part, but I got stuck immediately. My first few runs were hitting only about **5% accuracy**, which was frustrating because the AI was basically just guessing.

**The Fix:**
It turns out the "brain" couldn't handle the raw pixel numbers (0-255). Once I divided the data by 255.0 to scale everything between 0 and 1, the accuracy jumped to **97%** almost instantly. That was a huge "aha" moment for me—it showed that how you prep the data is just as important as the model itself.

**What I used:**
* **Convolution & Pooling:** A standard setup to help the AI see shapes and keep the processing fast.
* **Dropout (0.5):** I added this to stop the AI from just memorizing the training images. It forced the model to actually learn what the signs look like.
* **Dense Layer:** Used a hidden layer of 128 neurons which gave the AI enough "memory" to tell all 43 signs apart without slowing down the training.

Overall, it was a cool project that went from a complete fail to nearly perfect just by fixing one line of math.
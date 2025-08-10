# 🎬 MovieMate

MovieMate is a sleek web application that provides personalized movie recommendations. Built with Python and Streamlit, it uses a content-based filtering model to suggest films based on your favorite movies.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://movierecommendationsystem01.streamlit.app/)



## ✨ Features

* **Instant Recommendations:** Select a movie from the dropdown list and instantly get 5 similar movie recommendations.
* **Content-Based Filtering:** The recommendation engine suggests movies based on content similarity (like genre, cast, and plot).
* **Rich Movie Details:** Fetches and displays key movie information, including posters, top cast members, release date, genres, and a plot overview using the TMDB API.
* **Interactive UI:** A clean, simple, and responsive user interface powered by Streamlit.

---

## 🛠️ Tech Stack & Tools

* **Backend:** Python
* **Web Framework:** Streamlit
* **ML/Data Science:** Pandas, Scikit-learn (for model building)
* **API:** The Movie Database (TMDB) API for fetching movie data.
* **Deployment:** Streamlit Community Cloud

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

* Python 3.8 or higher
* A free API key from [The Movie Database (TMDB)](https://www.themoviedb.org/signup).

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```sh
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    Create a file named `requirements.txt` with the following content:
    ```txt
    streamlit
    pandas
    requests
    python-dotenv
    ```
    Then, run this command in your terminal:
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    * Create a new file in the root directory named `.env`.
    * Add your TMDB API key to this file as shown below:
    ```
    TMDB_API_KEY="PASTE_YOUR_TMDB_API_KEY_HERE"
    ```

5.  **Run the application:**
    Once the setup is complete, run the following command to start the Streamlit server:
    ```sh
    streamlit run app.py
    ```
    The application should automatically open in your web browser at `http://localhost:8501`.

---

## 📊 Data

The recommendation model was trained on the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata). The pre-processed data (`movie_list.pkl`) and the similarity matrix (`similarity.pkl`) are included in this repository.

---
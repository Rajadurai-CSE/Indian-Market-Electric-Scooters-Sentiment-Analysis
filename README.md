<h1 align="center">🛵 Indian-Market-Electric-Scooters-Sentiment-Analysis</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue?logo=python" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Frameworks-NLTK%20%7C%20scikit--learn%20%7C%20Plotly-green" alt="Frameworks Badge"/>
  <img src="https://img.shields.io/badge/Visualization-Interactive%20Plots-orange?logo=plotly" alt="Plotly Badge"/>
</p>

<p align="center" style="font-size:16px; color:#475569;">
This project analyzes customer reviews of popular Indian family segment electric scooters to uncover <strong>key sentiment patterns</strong>, <strong>frequently discussed themes</strong>, and <strong>dominant topics</strong> using 
state-of-the-art NLP techniques and interactive visualizations.
</p>

<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">

<h2>📘 Project Overview</h2>

<ul style="line-height:1.8;">
  <li><strong>Goal:</strong> Understand what customers like or dislike about EV scooters using <em>Sentiment Analysis</em> and cluster customers based on their feedback using <em>Topic Modeling</em> to recommend actionable insights to brands.</li>
  <li><strong>Approach:</strong> Scraped real customer reviews → Exploratory Data Analysis + Data Cleaning → Sentiment Analysis → Clustering Customers → Visualizing insights.</li>
  <li><strong>Tech Stack:</strong> Python, Pandas, NLTK, Scikit-learn, Plotly, BERTopic</li>
</ul>

<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">

<h2> 📊 Sample Visualizations</h2>

<img width="1377" height="525" alt="newplot (11)" src="https://github.com/user-attachments/assets/99c2a9fd-4f4b-4024-a293-e140b172d1c7" />
<img width="562" height="432" alt="image" src="https://github.com/user-attachments/assets/74e776e3-3b1a-4795-b9cc-c77269a6e9c4" />
<img width="1259" height="329" alt="image (1)" src="https://github.com/user-attachments/assets/480f758a-5afc-4cca-93ad-5c4eef0e2ae2" />
<img width="1377" height="525" alt="newplot (3) (1)" src="https://github.com/user-attachments/assets/e62078c6-ad4a-4fc5-8f01-b8aa40c58329" />


<p align="center">
  <img src="<!-- Add sentiment distribution image link here -->" alt="Sentiment Distribution Visualization" width="700">
</p>

<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">


<h2>🧠 Topic Modeling Results</h2>

<p>
We used <strong>BERTopic / c-TF-IDF</strong> to group semantically similar reviews and extract the key themes driving user opinions.
</p>

<p align="center">
  <img width="1200" height="750" alt="newplot (10) (1)" src="https://github.com/user-attachments/assets/eb37c399-f97c-4783-ab15-2bba94a52f34" />
</p>

<p align="center">
  <img src="<!-- Add topic modeling visualization image link here -->" alt="Topic Modeling Visualization" width="700">
</p>

<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">


<p>
Explore interactive charts directly in your browser using the Google Colab notebook below 👇
</p>

<p align="center">
  🔗 <a href="https://colab.research.google.com/drive/1jmOW7TfyuqDBMTuxqR-PBoBwxa2eLafG?usp=sharing" target="_blank" style="font-size:16px; color:#0ea5a6; text-decoration:none;">
    Open on Google Colab
  </a>
</p>

<p align="center">
  🖼️ <em><img width="1917" height="871" alt="port" src="https://github.com/user-attachments/assets/03adebac-c73d-4bbf-a03c-c4ab59c18c53" /> </em>

</p>

<p align="center">
  <img src="<!-- Add example interactive plot screenshot -->" alt="Interactive Plot Screenshot" width="700">
</p>

<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">

<h2>⚙️ How It Works</h2>

<ol style="line-height:1.8;">
  <li><strong>Scraping Reviews:</strong> Collected real user reviews from trusted sources.</li>
  <li><strong>Data Cleaning:</strong> Removed stopwords, special characters, and normalized text.</li>
  <li><strong>Sentiment Analysis:</strong> Applied <code>Bert Models</code> to classify reviews as Positive, Neutral, or Negative.</li>
  <li><strong>Topic Modeling:</strong> Used <code>c-TF-IDF</code> and <code>BERTopic</code> for clustering review themes.</li>
  <li><strong>Visualization:</strong> Built interactive plots using <code>Plotly</code>.</li>
</ol>

<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">

<h2>📈 Key Findings</h2>

<ul style="line-height:1.8;">
  <li><strong>Bajaj Chetak:</strong> Loved for build quality and smooth ride, criticized for battery and service issues.</li>
  <li><strong>Ola S1X:</strong> Praised for performance and range, but users face inconsistent service experiences.</li>
  <a style="text-underline:None" href="https://colab.research.google.com/drive/1jmOW7TfyuqDBMTuxqR-PBoBwxa2eLafG?usp=sharing#scrollTo=aXEH0c5e0b03"> <li>Explore more on the notebook..</li></a>
  <li>Across all models, <strong>Service Centre response</strong> and <strong>Battery performance</strong> are recurring pain points.</li>
</ul>

<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">

<h2>📂 Repository Structure</h2>

<pre style="background:#f8fafc; padding:12px; border-radius:6px; border-left:4px solid #0ea5a6;">
EV_Sentiment_Analysis/
│
├── sentiment_analysis_notebook.ipynb    # Jupyter/Colab notebooks
├── results.pdf                  # Results of the study
├── script.py                   # Modified Web Scrapping Code
└── README.md                 # Project documentation
</pre>

<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">

<h2>📫 Contact</h2>

<p>
Feel free to reach out for collaborations, improvements, or project discussions.<br>
<strong>Author:</strong> S.Rajadurai <br>
<strong>Email:</strong> rajadurai3491@gmail.com <br>
<strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/rajadurai-2004cse" target="_blank">View Profile</a>
</p>

<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">

<p align="center" style="font-size:14px; color:#94a3b8;">
© 2025 EV Scooters Sentiment Analysis
</p>

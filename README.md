<h1 align="center">🛵 Indian-Market-Electric-Scooters-Sentiment-Analysis</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue?logo=python" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Frameworks-NLTK%20%7C%20scikit--learn%20%7C%20Plotly-green" alt="Frameworks Badge"/>
  <img src="https://img.shields.io/badge/Visualization-Interactive%20Plots-orange?logo=plotly" alt="Plotly Badge"/>
</p>

<p align="center" style="font-size:16px; color:#475569;">
This project analyzes customer reviews of popular Indian family-segment electric scooters to uncover 
<strong>key sentiment patterns</strong>, <strong>frequently discussed themes</strong>, and <strong>dominant topics</strong> 
using NLP and interactive visualizations.
</p>

<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">

<h2>📘 Project Overview</h2>

<ul style="line-height:1.8;">
  <li><strong>Goal:</strong> Understand what customers like or dislike about EV scooters using <em>Sentiment Analysis</em> and cluster feedback using <em>Topic Modeling</em> to provide actionable insights for brands.</li>
  <li><strong>Approach:</strong> Scraped real customer reviews → Cleaned & Processed text → Applied Sentiment Analysis → Topic Modeling → Interactive Visualization.</li>
  <li><strong>Tech Stack:</strong> Python, Pandas, NLTK, Scikit-learn, Plotly, BERTopic</li>
</ul>

<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">

<h2>📊 Sample Visualizations</h2>

<p align="center">
  <img width="1377" height="580" alt="Visualization 1" src="https://github.com/user-attachments/assets/99c2a9fd-4f4b-4024-a293-e140b172d1c7" />
</p>
<br>
<p align="center">
  <img width="1259" height="380" alt="Visualization 2" src="https://github.com/user-attachments/assets/480f758a-5afc-4cca-93ad-5c4eef0e2ae2" />
</p>
<br>
<p align="center">
  <img width="1377" height="570" alt="Visualization 3" src="https://github.com/user-attachments/assets/e62078c6-ad4a-4fc5-8f01-b8aa40c58329" />
</p>

<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">

<h2>🧠 Topic Modeling Results</h2>

<p>
We used <strong>BERTopic</strong> and <strong>c-TF-IDF</strong> to identify key topics within user feedback, uncovering 
semantically meaningful clusters of sentiments and discussions.
</p>

<p align="center">
  <img width="1200" height="750" alt="Topic Modeling Visualization" src="https://github.com/user-attachments/assets/eb37c399-f97c-4783-ab15-2bba94a52f34" />
</p>

<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">

<h2>🌐 Explore Interactive Notebook</h2>

<p>
You can explore the interactive Plotly charts and in-depth analysis directly in Google Colab below 👇
</p>

<p align="center">
  🔗 <a href="https://colab.research.google.com/drive/1jmOW7TfyuqDBMTuxqR-PBoBwxa2eLafG?usp=sharing" target="_blank" style="font-size:16px; color:#0ea5a6; text-decoration:none;">
    Open in Google Colab
  </a>
</p>

<p align="center">
  <img width="1917" height="871" alt="Colab Preview" src="https://github.com/user-attachments/assets/03adebac-c73d-4bbf-a03c-c4ab59c18c53" />
</p>

<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">

<h2>⚙️ How It Works</h2>

<ol style="line-height:1.8;">
  <li><strong>Scraping Reviews:</strong> Collected genuine user feedback from online sources.</li>
  <li><strong>Data Cleaning:</strong> Removed stopwords, special characters, and normalized text.</li>
  <li><strong>Sentiment Analysis:</strong> Classified text into Positive, Neutral, or Negative sentiments.</li>
  <li><strong>Topic Modeling:</strong> Grouped reviews by semantic similarity using <code>BERTopic</code>.</li>
  <li><strong>Visualization:</strong> Built interactive dashboards using <code>Plotly</code>.</li>
</ol>

<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">

<h2>📈 Key Findings</h2>

<ul style="line-height:1.8;">
  <li><strong>Bajaj Chetak:</strong> Appreciated for premium build and smooth ride; criticized for battery and service issues.</li>
  <li><strong>Ola S1X:</strong> Praised for performance and range; inconsistent service experiences noted.</li>
  <li><strong>Ather Rizta:</strong> Known for design, connectivity, and comfort but some complaints about service delays.</li>
  <li>Across all models, <strong>Service Centre response</strong> and <strong>Battery performance</strong> remain key customer pain points.</li>
</ul>

<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">

<h2>📂 Repository Structure</h2>

<pre style="background:#f8fafc; padding:12px; border-radius:6px; border-left:4px solid #0ea5a6;">
EV_Sentiment_Analysis/
│
├── sentiment_analysis_notebook.ipynb    # Jupyter/Colab notebook
├── results.pdf                          # Summary of key results
├── script.py                            # Web scraping code
└── README.md                            # Project documentation
</pre>

<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">

<h2>📫 Contact</h2>

<p>
<strong>Author:</strong> S. Rajadurai <br>
<strong>Email:</strong> rajadurai3491@gmail.com <br>
<strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/rajadurai-2004cse" target="_blank">View Profile</a>
</p>

<hr style="border:0; border-top:1px solid #e5e7eb; margin:24px 0;">

<p align="center" style="font-size:14px; color:#94a3b8;">
© 2025 EV Scooters Sentiment Analysis
</p>

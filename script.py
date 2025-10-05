import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

#Modified Web Scrapping code
#You can follow the structure make changes according to the website
def extract_reviews_from_page(page_num=1):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        url = f"url?pageno={page_num}" #Paste url

        
        res = requests.get(url, headers=headers)
        
        if res.status_code != 200:
            print(f"Error: Status code {res.status_code}")
            return []


        soup = BeautifulSoup(res.text, "html.parser")
        reviews_data = []
        
        # Find all review containers
        review_containers = soup.find_all("div", class_="readReviewBox")
        
        print(f"Found {len(review_containers)} review containers")
        
        for container in review_containers:
            try:
                review_data = {}
                
                # Extract author information
                author_info = container.find("div", class_="authorInfo")
                if author_info:
                    # Extract author name and date
                    name_element = author_info.find("div", class_="name")
               
                    if name_element:
                        name_text = name_element.get_text()
                     
                        if " on " in name_text:
                            name, date = name_text.split(" on ", 1)
                            review_data["reviewer_name"] = name.strip()
                            review_data["date"] = date.strip()

                        else:
                            review_data["reviewer_name"] = name_text
                            review_data["date"] = ""
                    
                
                # Extract review content
                content_space = container.find("div", class_="contentspace")
                if content_space:
                    # Extract title
                    title_element = content_space.find("span", class_="title")
                    if title_element:
                        review_data["review_title"] = title_element.get_text(strip=True)
                    else:
                        review_data["review_title"] = ""
                    
                    # Extract review text
                    content_height = content_space.find("div", class_="contentheight")
                    if content_height:
                        # Find the div with review text (usually the first div inside contentheight)
                        review_div = content_height.find("div")
                        if review_div:
                            review_text = review_div.get_text(strip=True)
                            # Remove "Read More" and similar trailing text
                            review_text = re.sub(r'\.+$', '', review_text)  # Remove trailing dots
                            review_data["review_text"] = review_text
                        else:
                            review_data["review_text"] = ""
                    else:
                        review_data["review_text"] = ""
                
                # Add page number for tracking
                review_data["page"] = page_num
                
                # Only add if we have meaningful data
                if review_data.get("reviewer_name") or review_data.get("review_text"):
                    reviews_data.append(review_data)
                    
            except Exception as e:
                print(f"Error processing review container: {e}")
                continue
        
        return reviews_data
        
    except Exception as e:
        print(f"Error fetching page {page_num}: {e}")
        return []
    
if __name__ == '__main__':
    for i in range(1,11):
      reviews_data = extract_reviews_from_page(i)
      df = pd.DataFrame(reviews_data)
      print(f"Page {i}: No of Reviews {len(df)}")
      df.to_csv("ModelName.csv",mode='a',index=False)
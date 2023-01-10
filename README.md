# web-scraper-and-data-visualizer

#### This script uses the Scrapy library to scrape data from a website and store it in a Pandas dataframe. The data is then cleaned and transformed as needed before being passed to Plotly for visualization. The final visualizations are displayed in a web-based interface, allowing users to easily explore and analyze the data. This script provides a powerful tool for extracting, cleaning, and visualizing data from the web. 

---
### Example Data Used

<img align="left" width="200" height="345" src="https://user-images.githubusercontent.com/109874492/211451993-97116871-f33b-4e93-9370-9921062e7561.PNG"/>

#### I used steam charts as an example dataset because it required me to pull data from multiple pages and had three different data sets I wanted to visualize.
  ![data folder](https://user-images.githubusercontent.com/109874492/211453396-2904bf99-7e85-4168-a9d8-0fbd05791859.PNG)
<br />


---
### Scrapy Spider config
#### I made three differnet spiders each resposible for a dataset.
![spiders](https://user-images.githubusercontent.com/109874492/211456658-0ec02301-fe19-41a7-8268-84788d496251.PNG)
#### They all have a custom feed export to generate the CSV files.
![spider_2](https://user-images.githubusercontent.com/109874492/211456726-8c9a754f-e2e0-4f93-baad-7dca9defbb52.PNG)
#### I made a seperate Python file to run all the spiders from a single function.
![run_spiders](https://user-images.githubusercontent.com/109874492/211457014-789bee00-391a-423e-8859-e227ffb5b038.PNG)

---
### Running Everything and Visualizing the Data
#### I made another seperate python file to tie everything together.
![main](https://user-images.githubusercontent.com/109874492/211457479-9ecbfe73-d245-4745-8fc8-8265fa0002e3.PNG)
<br />

#

#### I used pandas to access the three CSV files and created three plotly graphs.
  <img width="50" height="100" style="padding-right:50px;" src="https://user-images.githubusercontent.com/109874492/211453796-3fbc6a00-5beb-4dc2-a05c-b5dec03f922f.png"/>   <img width="50" height="100" style="padding-right:50px;" src="https://user-images.githubusercontent.com/109874492/211453800-bb5b921e-7185-449f-9330-f339dc37f56d.png"/>   <img width="50" height="100" style="padding-right:50px;" src="https://user-images.githubusercontent.com/109874492/211453812-c8b94915-6a0e-49a1-88ff-b06abf173afb.png"/>
---
#### This probably isnt the most efficient way to write this code but it was just a project to challenge myself and to continue to learn more.

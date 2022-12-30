# ♾️ entropy.random-data-generator
A python library to aid in the creation of random data for pandas data-frames. Some uses revolve around generating test data for machine learning exercises and for learning large data manipulation.
## ⏬ Installation
``` pip install entroPy ```
#### 🎟 Requirements
- ``` pip install pandas ```
- ``` pip install tqdm ```
## 🛠️ Functionality
#### 🤖 x = generator()
When a generator class is instanced as follows: 
``` x = generator() ``` , it is then possible to randomly generate any number of columns each with customizable variables and number of rows.
#### 🚀 x = complex_generator(x)
After generating several rows using the base generator class you can reassign your variable to a different generator, for instance: the complex_generator. This will then allow you to work with generating different and more obscure data formats such as dates or, in the future, time, currencies and colors. 

#### 📦 Pandas and TQDM
entroPy makes use of the dataframe capabilities of pandas to output the generated data. entroPy also makes us of TQDM to time and show the progress of the data being generated in real time.

![image](https://user-images.githubusercontent.com/99112649/210074779-f8ac5e1c-4435-48ba-999b-305cae6488b8.png)
## 🚗 Roadmap
- New Functions to tweak the dataset and insert specific values at random intervals such as NaN or None values.
- Allow for more complex datatypes to be generated. 
- Look into Polar for dataframe manipulation to speed up data generation.
- Allow for alternative output options. 

# MongoDashProject
Simple Dash framework to interact with MongoDB backend using a Python CRUD module I wrote. This is a project for my client/server development class.

About the Project/Project Title
The Grazioso Salvare dashboard is an interactive dashboard created for Graziozo Salvare, an innovative international rescue-animal training company. The dashboard provides users with a table featuring all of the rescue-animals in the system and the ability to filter by the desired training for the dog. 

Motivation
Having an interactive dashboard improves the efficiency of the company and allows them to quickly locate rescued dogs that are ideal for training for specific tasks, such as water rescue, mountain or wilderness rescue, and disaster rescue or individual tracking.
	
	Technology
The motivation behind choice of technologies varies. MongoDB was chosen as the database over a traditional relational database because of its document style architecture and ease of scaling. The document style architecture is perfect for storing all of the animals and their attributes. Dash was chosen as the web framework because of its simplicity and ease of use for the end user. The simple MVC framework allows for a wide array of data visualization and filtering tools to make accessing and interfacing with the Mongo database quicker and easier.

To explore these technologies further:
https://docs.mongodb.com/
https://dash.plotly.com/


Getting Started
To get started, visit the Grazioso Salvare dashboard website. 

Usage
The dashboard can be used to filter and sort rescue breeds and to see their respective locations on a map. To see the location of a particular dog, click on the dog’s row. The table, bar chart, and geolocation map can be filtered with the use of the radio buttons by desired task. Essentially, selecting “Water Rescue”, “Mountain or Wilderness Rescue”, or “Disaster Rescue or Individual Tracking” will filter the result to show the user the dogs with the ideal traits for the selected task. The reset button will return the table, bar chart, and geolocation map to their original states. The table can also be sort in ascending or descending order by any of its columns to make searching by additional characteristics easier. The table has been split into pages of length 10 to further enhance readability.

The Process
The key to the success of this dashboard is the CRUD module. That was the first step. Creating an interface to make queries between the front-end Dash dashboard and the backend Mongo database was essential to making a scalable, data-driven website with a smooth user experience. Once the CRUD module was complete, the only thing left to do was create the website with Dash and utilize Plotly functions to create data visualizations to help users navigate data from the database. 
The biggest challenge to this process was learning how to use the callback functionality typical of MVC frameworks. I have extensive experience with MVT frameworks where the controller aspect (callbacks) is handled by the framework itself. This proved to be quite a challenge at first, however, I quickly got myself up to speed by reading the thoroughly written Dash documentation. Reading documentation is an essential skill as a software engineer so I found this practice reading it to be extremely helpful and something that will prove to be helpful down the road as I enter the work force.

Contact
Your name: Jonathan Handy
Email: Jonathan.handy@snhu.edu

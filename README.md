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

	How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?

I write maintainable, readable, adaptable programs by applying object oriented programming concepts and by thoroughly commenting my code. In the case of the CRUD module, writing this way ensures I can easily adapt this program to work in any number of other contexts. I think I would also add a databaseSelection() method to the module to make it even more flexible.

	How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?

Approaching problems as a computer scientist requires breaking the problem down into smaller parts and tackling each part individually while keeping the larger picture in mind. I find it essential to test the incorporation of the smaller pieces together as soon as it's possible to help ensure I find and fix problems as soon as possible. My approach did not differ from previous assignments in other courses. I looked at each requirement and broke them down into "independent" or "dependent", meaning requirements that depend on me completing a different requirement first or not. I then start writing code for the independent requirements first.

	What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
	
Computer scientists solve problems by finding efficient, technological solutions. These solutions contribute to productivity as well as quality of life: things take less time to do leaving more time for further work and relaxation. This type of product increases the productivity of a company like Grazioso Salvare by significantly cutting down on the amount of time required to find the desired information.

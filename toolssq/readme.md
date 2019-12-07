Project description:

What is it:

This project creates a website using Django based on 2018_Central_Park_Squirrel_Census_Squirrel_Data.csv datafile.It keeps track of the record of all known squirrels spotted in Central Park. Besides viewing the spotted locations of known squirrels, this application also allows users to import the data add and update squirrel data when they made new discoveries. Moreover, users can see some general stats of the squirrels population and know more about our lovely little friends.

Main Features:

Import:

The data is imported into the website using management command import_squirrel_data.py.
Data is imported from local environment with the command
$ python manage.py import_squirrel_data /path/to/name of file.csv in the command line.

Export:

We welcome you to download our current data base from our website for further analysis! To export data from this application, simply type in $ python manage.py export_squirrel_data /path/to/name of file.csv
With the management command we incorporated in our application, this command would allow you to download the dataset and study it in your free time!
The exported data can also be reimported if necessary.

Views:

We have in total 4 different views in this application!
1. A view that shows a map which displays the location of the squirrel sightings on an OpenStreets map​.
Located at: ​/map
This view allows users to see squirrel locations on a map!
In the codes we plotted 250 but could be changed easily
2. A view that lists all squirrel sightings
Located at: ​/sightings
When click into it:  /sightings/<unique-squirrel-id>
Here when user clicks into the a squirrel, not only can she view its detailed information, but she can also edit attribute for that squirrel!
3. A view to create a new sighting
Located at: ​/sightings/add
When our user spots a new squirrel, she can add her observation in here!
4. A view with general stats about the sightings
Located at: ​/sightings/stats
Here users can see stats about the current squirrel population!

** Reference: Homepage template inspired by https://www.w3schools.com/w3css/w3css_templates.asp

Group name and section:
  Squirrel Hunter, Section 1

UNI list:
  UNIs: [yy3007, lh2991]

Link to the server running application:
  https://dulcet-aileron-255421.appspot.com/sightings

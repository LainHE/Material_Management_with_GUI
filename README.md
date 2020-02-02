# Material Management with GUI

The material management system aims the librarians have able to CRUD (Create, Read, Update, and Delete) materials. A clear and simple GUI (Graphical User Interface) would make the librarians works more efficiency and easier. The system is developed by python 3. It combines with the package of Tkinter and SQLite3, that makes system not only have a GUI, but also have able to store and read a mass of data.
  
  
## Please notice that when you using
**INSERT MATERIAL**:  
User should fill all boxes of Material Name, Author, Publisher, and Date of Publish.  
Please keep the format of date as DD/MM/YYYY as possible. I understand that some material may not give clear date. Such as, c1988 etc. so I did not set limit.  
The Type of Material is defaulted as Book. If the material is not book, user could change it.  
  
  
**REMOVE & UPDATE MATERIAL**:  
Select a material in listbox first.  
  
  
**CLEAR INPUT**:  
This function is only use to clear the text what user inputted in the boxes.  This button will not clear any data it stored.  
  
  
**SEARCH MATERIAL**:  
Due to the technical issues, it only allow user to search the material in one element. Which means only input one of material Name, Author, Publisher, or Date of Publish to search.  
The type element will not works in this function.  
Click again without input, to return full list.

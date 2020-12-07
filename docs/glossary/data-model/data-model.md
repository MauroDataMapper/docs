##**What is a Data Model?**

A **Data Model** is a description of an existing collection of metadata, or a specification of data that is to be collected. **Data Models** which contain existing data are known as a **Data Asset**, while models which contain templates for data collection are known as a **Data Standard**. Both are called models as they are effectively representations of the data that they describe. 

---
##**How are Data Models used?**

**Data Models** make the connection between the names of columns, fields or variables and our understanding of how the corresponding data is acquired, managed and interpreted. The **Mauro Data Mapper** acts as a directory for these **Data Models** and allows us to create, search and share these data descriptions.

Within each **Data Model** lies several **[Data Classes](../data-class/data-class.md)** which are groups of data that are related in some way. **[Data Classes](../data-class/data-class.md)** contain **Data Elements** which are the descriptions of an individual field or variable. 

For example, a webform where patients enter their details would be a **Data Model**. The **'Personal details'** and **'Contact details'** sections within the webform would each be a **[Data Class](../data-class/data-class.md)**. While the individual entries such as **'First Name'**, **'Last Name'**, **'Date of Birth'** etc would each be a **Data Element**. 

The **'Correspondence Address'** section is within the **'Contact details'** section and would therefore be a **Nested Data Class**.

![Webform Data Model example](your-details-webform.png)
 
![Flowchart of Webform Data Model example ](data-model-flowchart.png)

Each **Data Model** has a:

* **[Label](../label/label.md)**  
	This is the unique name of the **Data Model**.
	
* **[Aliases](../aliases/aliases.md)**  
	Alternative names that can help locate the **Data Model** in the Mauro Data Mapper when searched for.

* **Organisation**  
	Details of who is responsible for creating the **Data Model**. 

* **Description**  
	A definition either written in html or plain text which explains further contextual details relating to the **Data Model**.

* **Type**  
	This defines whether the **Data Model** is a **Data Asset**, which contains existing data, or a **Data Standard**, which contains templates for data collection. 

* **Classifications**  
	These are effectively tags that you can apply to the **Data Model**.

The above are all shown within the details panel, when the **Data Model** is selected in the **Model Tree**.

![Data Model details panel](data-model-details.png)

Other characteristics are displayed in the tabs underneath the details panel, when the **Data Model** is selected in the **Model Tree**.

* **[Data Classes](../data-class/data-class.md)**  
	This is a list of all the **[Data Classes](../data-class/data-class.md)** within the **Data Model**.

* **Types**  
	The various **Data Types** within the **Data Model**. These can be created by the user or imported from other **Data Models** within Mauro Data Mapper. **Data Types** can either be Enumeration, Primitive, Reference or Terminology. 

* **Properties**  
	Arbitrary additional metadata about this **Data Model**.

* **Summary**  
	Further metadata information on the nature of the **[Data Classes](../data-class/data-class.md)** within the **Data Model**. This can include aggregate data such as the number of entries or distribution information as well as textual information detailing aspects like the geographic representation of the data set or the duration of collection. 
	
* **Comments**  
	Any relevant comments or notes. 
	
* **History**  
	A detailed record of user, date, time and description of all the changes made to the **Data Model**. 

* **Diagram**  
	A UML diagram which is a graphical way of summarising the **[Data Classes](../data-class/data-class.md)** and **Data Elements** within the **Data Model**. 

* **Links**  
	**Semantic links** between relevant **Data Models**.

* **Attachments**  
	Files can be added to provide additional information and context. 
	
* **Dataflow**  
	A diagram illustrating where the data within the **Data Model** has come from and how it has moved across different databases and organisations. This gives users valuable information on the history of the data and how it has been manipulated.  

---
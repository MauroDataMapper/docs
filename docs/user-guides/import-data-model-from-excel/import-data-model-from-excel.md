This user guide will explain the steps you need to follow to import a health dataset to the **[Mauro Data Mapper](https://modelcatalogue.cs.ox.ac.uk/mdm-ui/#/home)** using an Excel spreadsheet.

---

To add an existing dataset to **[Mauro Data Mapper](https://modelcatalogue.cs.ox.ac.uk/mdm-ui/#/home)**, you can either enter all the information online as explained in the **['Document a Health Dataset user guide'](../document-a-health-dataset/document-a-health-dataset.md)**, or you may find it more convenient to import information automatically from an Excel spreadsheet. 

The importing functionality of **[Mauro Data Mapper](https://modelcatalogue.cs.ox.ac.uk/mdm-ui/#/home)** allows you to import several **[Data Models](../../glossary/data-model/data-model.md)** using the same spreadsheet. 

---

## **1. Create [Data Model](../../glossary/data-model/data-model.md) import file**

To ensure all the information is imported correctly, the dataset needs to be entered into a spreadsheet in a specific format. To help with this, you can download a zip file of the **[standard template here](Template_DataModel_Import_File.xlsx.zip)**.

This **‘Data Model import file’** standard spreadsheet consists of two types of sheets. Firstly, there is the **[Data Model listing sheet](../import-data-model-from-excel/import-data-model-from-excel.md#listing-sheet)**, titled **‘DataModels’**. This is effectively a contents page which lists the main details of each **[Data Model](../../glossary/data-model/data-model.md)** you wish to import. There must only ever be one **Data Models listing sheet**. 

The next sheet is the **[Data Model key sheet](../import-data-model-from-excel/import-data-model-from-excel.md#key-sheet)** which is titled **‘KEY_1’**. This contains all the relevant details of one **[Data Model](../../glossary/data-model/data-model.md)** listed in the **‘DataModels’** sheet. Therefore, if you wish to import several **[Data Models](../../glossary/data-model/data-model.md)**, you will need to add a **‘KEY_2’**, **‘KEY_3’** etc sheet for each additional **[Data Model](../../glossary/data-model/data-model.md)** and then include the details of each **[Data Model](../../glossary/data-model/data-model.md)** on the **[Data Model listing sheet](../import-data-model-from-excel/import-data-model-from-excel.md#listing-sheet)**.

### <a name="listing-sheet"></a> **1.1 Data Model listing sheet**

In the **Data Model listing sheet**, use one row for each **[Data Model](../../glossary/data-model/data-model.md)**. Enter the information according to the columns, which are illustrated below, along with any other properties or metadata which may be relevant. 

![Screenshot of Data Model listing sheet](data-model-listing-sheet.png)

*Note: the following columns must be included.*

* **SHEET_KEY**  
	The unique name of each **[Data Model key sheet](../import-data-model-from-excel/import-data-model-from-excel.md#key-sheet)** such as **‘KEY_1’** or **‘KEY_2’**. 


* **Name**  
	The unique name or **[Label](../../glossary/label/label.md)** of the **[Data Model](../../glossary/data-model/data-model.md)**. Remember this should be different to all the existing **[Data Models](../../glossary/data-model/data-model.md)** within **[Mauro Data Mapper](https://modelcatalogue.cs.ox.ac.uk/mdm-ui/#/home)**. 
	
* **Description**  
	Enter a description which explains the contextual details of the dataset within the **[Data Model](../../glossary/data-model/data-model.md)**. 
	
* **Author**  
	Record the name(s) of the authors who are creating and maintaining this **[Data Model](../../glossary/data-model/data-model.md)**.
	
* **Organisation**  
	Type the name of the organisation responsible for the **[Data Model](../../glossary/data-model/data-model.md)**, or the underlying data.
	
* **Type**  
	This is the type of the **[Data Model](../../glossary/data-model/data-model.md)**, which can either be a **Data Asset** or a **Data Standard**. A **Data Asset** is a collection of existing data, such as a database or a completed form. While a **Data Standard** is a specification template to collect new data, such as a form or schema.
	
* **Adding properties**  
	Any other relevant properties or metadata relating to the **[Data Model](../../glossary/data-model/data-model.md)** can be included in additional columns after the core columns. Metadata can have the following properties:
		
	* **Namespace**  
		This will be used to select the correct properties by the gateway interface such as **'uk.ac.hdrukgateway'** and should be entered in **row 1** of the spreadsheet. If it is left blank, the default namespace of **ox.softeng.metadatacatalogue.plugins.excel** will be adopted. 
		
	* **Key**  
		This is a relevant property name such as **‘contact email’** and ***must*** be entered in **row 2**. If no key is supplied, then the value will not be assigned.
	
	* **Value**  
		This is the **Value** of the given property, for example **‘enquiries-mydataset@hub.org’** and should be entered into the relevant row. If multiple rows are being imported and a **Namespace** and **Key** column is created, then the property will only be assigned if a **Value** is supplied. 
	
	
![Screenshot of Data Model listing sheet with metadata included in additional  property columns](data-model-listing-sheet-additional-metadata.png)
	
	

### <a name="key-sheet"></a> **1.2 Data Model key sheet**


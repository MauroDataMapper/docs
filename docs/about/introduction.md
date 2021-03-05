## What is Mauro Data Mapper?

Collecting accurate and reliable data takes a huge amount of time, money and resource. Therefore, it’s vital that researchers are able to extract the maximum value from this data for both current and future research projects. This is why the [National Institute for Health Research (NIHR)](https://www.nihr.ac.uk/) has collaborated with Universities to develop the [Mauro Data Mapper](https://modelcatalogue.cs.ox.ac.uk/mdm-ui/#/home) formerly known as the Metadata Catalogue.

**Mauro Data Mapper**, is a toolkit for combining, developing and standardising data, helping users to effectively record and analyse contextual data. This central hub of clinical informatics allows users to easily access the metadata they require, avoiding the need to repeat research tasks; saving time, reducing costs and boosting productivity. 

Furthermore, by employing standard definitions, terminologies and [Data Models](../glossary/data-model/data-model.md), the data can be accurately interpreted. Therefore, users can reliably compare datasets from different sources increasing the sample size of their investigations and consequently the validity of their conclusions.

<iframe src="https://player.vimeo.com/video/186242194" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

---

## Why is metadata important?

To fully understand the meaning of data, first we need to know some further information about its context, known as metadata. 

For example, consider a blood pressure reading. Although this has standard units, the method and state of the patient at the time the measurement was taken, will affect the recorded value. Therefore, by outlining this additional information, the reading can be understood and interpreted more accurately. In this way, metadata allows data to be more searchable, comparable and standardised enabling further interoperability.

---

## How does Mauro Data Mapper work?

The **Mauro Data Mapper** is a web based tool which stores and manages descriptions of data. These can be descriptions of data already collected, such as databases or csv files. Or these can be descriptions of data you wish to collect or transfer between organisations, such as a specification for a webform or an XML schema. 

**Mauro Data Mapper** represents both types of descriptions of data as **Data Models**. These are defined as a structured collection of metadata and effectively model the data that they describe.


![Mauro Data Mapper main screen](mdm-main-screen.png)

Each **Data Model** consists of several [Data Classes](../glossary/data-class/data-class.md), which are groups of data that are related in some way. For example, a group of data that appears in the same table of a database or the same section of a form. **Data Classes** can sometimes also contain **Nested Data Classes**.

Within each **Data Class** is then a number of [Data Elements](../glossary/data-element/data-element.md) which are the descriptions of an individual field or variable.

For example, a webform where patients enter their details would be a **Data Model**. This form could consist of two seperate sections such as **'Personal details'** and **'Contact details'** which would each be a **Data Class**. The individual entries within each of these sections, such as **'First Name'**, **'Last Name'**, **'Date of Birth'** etc, would each be a **Data Element**.

However, there might be a section within another section on the webform, such as **'Correspondence Address'** which lies within **'Contact details'**. In this case, **'Correspondence Address'** would become a **Nested Data Class**, where the **'Contact details' Data Class** would be the parent. 

![Webform Data Model example](../glossary/data-model/your-details-webform.png)
 
![Flowchart of Webform Data Model example](../glossary/data-model/data-model-flowchart.png)

By organising metadata in this way, **Mauro Data Mapper** allows users to easily search data but also automatically import database schemas and export forms; helping to record data in standardised formats.

---

## An open-source community

The Mauro platform and plugins are distributed under an open source [Apache 2.0 license](http://oss-watch.ac.uk/resources/apache2). We are keen 
to build an active community of users and developers, and encourage contributions to our code and documentation, and facilitate model sharing.  

---   

## Support

The development of **Mauro Data Mapper** has been primarily funded by the [NIHR Oxford Biomedical Research Center](https://oxfordbrc.nihr.ac.uk) as part of the [NIHR Health Informatics Collaborative (HIC)](https://hic.nihr.ac.uk). 

The **NIHR HIC** is a partnership of 27 NHS trusts and health boards, including the 20 hosting **NIHR Biomedical Research Centres (BRCs)**, working together to facilitate the equitable re-use of NHS data for translational research. 

The **NIHR HIC** has established cross-site data collaborations in areas such as cardiovascular medicine, critical
care, renal disease, infectious diseases, and cancer. **Mauro Data Mapper**, and its previous incarnation, the Metadata Catalogue, has been used for
collaboratively editing **Data Models** for research, and for generating software artefacts such as XML Schema.

---
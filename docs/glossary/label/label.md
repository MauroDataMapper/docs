##What is a Label?
A **Label** is a name that describes and uniquely identifies each item within **Mauro Data Mapper**. This **Label** will appear in the **Model Tree** on the left hand side of the catalogue and at the top of the page when the item is selected. The **Label** is also used to identify the item when searched for. 

![Label highlighted in Model Tree and in details panel](label-highlighted.png)

---

##How are Labels used?
The **Label** of each item must be unique within its parent group so that no two items share the same **Label**. Therefore, each [Data Model](../data-model/data-model.md) must have a unique **Label**. Each [Data Class](../data-class/data-class.md) must have a unique **Label** within its parent **Data Model**. Each [Data Element](../data-element/data-element.md) must have a unique **Label** within its parent **Data Class**. 

For example, there can only be one **Data Class** called **‘Personal details’** within a particular **Data Model**. Therefore, if you need to add a similar **Data Class**, include version information within the **Label** such as **‘Personal details 2.0’** to uniquely identify it. 

![Unique Labels for similar Data Classes highlighted](unique-label-example.png)

In some cases, two different **Data Models** could consist of a **Data Class** with the same **Label**, such as **'Personal details'**. However, because these two **Data Classes** are each associated with their own unique parent **Data Model**, then this is acceptable. Only when two items are within the same parent must they each have a unique **Label**.  

!!! Warning
	The following special characters are not permitted in labels, and will produce an error message:

	- `@`
	- `$`
	- `|`

---

##How do you edit a Label?

You can edit the **Label** of any item by selecting it in the **Model Tree** and clicking the **‘Edit’** pencil icon at the bottom right of the details panel. You will then be able to amend the **Label** at the top of the details panel. 

![Edit pencil icon highlighted on details panel](edit-label.png)

---
